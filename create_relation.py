# -*- coding: utf-8 -*-

"""
Create Relation 1.1
-------------------

QGIS plugin for creating and inspecting:

    * one-to-one relations
    * one-to-many relations
    * many-to-many relations

Designed for QGIS 3.28+ and QGIS 4.x (Qt6).
"""

import os
from datetime import datetime

from qgis.PyQt.QtCore import (
    QCoreApplication,
    QSettings,
    QTranslator,
    Qt,
)

from qgis.PyQt.QtGui import (
    QAction,
    QIcon,
)

from qgis.PyQt.QtWidgets import (
    QMessageBox,
    QFileDialog,
    QDialog,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
)

from qgis.core import (
    QgsFeature,
    QgsField,
    QgsProject,
    QgsRelation,
    QgsVectorFileWriter,
    QgsVectorLayer,
)

from .create_relation_dialog import (
    CreateRelationDialog,
    icon,
)


class CreateRelation:
    """Main QGIS plugin class."""

    PLUGIN_NAME = "Create Relation"
    PLUGIN_VERSION = "1.1"

    TYPE_ONE_TO_ONE = "one_to_one"
    TYPE_ONE_TO_MANY = "one_to_many"
    TYPE_MANY_TO_MANY = "many_to_many"

    def __init__(self, iface):
        self.iface = iface

        self.plugin_dir = os.path.dirname(__file__)

        self.actions = []
        self.menu = self.tr("&Create Relation")

        self.first_start = True
        self.dlg = None

        self.translator = None

        self._attribute_forms = []
        self._last_bridge_layer_id = None

        self._load_translation()

    # ==============================================================
    # TRANSLATION
    # ==============================================================

    def tr(self, message):
        return QCoreApplication.translate(
            "CreateRelation",
            message,
        )

    def _load_translation(self):
        """Load plugin translation."""

        locale = str(
            QSettings().value(
                "locale/userLocale",
                "en",
            )
        )

        locale = locale.replace("-", "_")

        locale_short = locale.split("_")[0]

        locale_path = os.path.join(
            self.plugin_dir,
            "i18n",
            f"create_relation_{locale_short}.qm",
        )

        if not os.path.exists(locale_path):
            return

        self.translator = QTranslator()

        if self.translator.load(locale_path):
            QCoreApplication.installTranslator(
                self.translator
            )

    # ==============================================================
    # GUI
    # ==============================================================

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        parent=None,
    ):
        """Create and register a QGIS action."""

        action = QAction(
            QIcon(icon_path),
            text,
            parent,
        )

        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip:
            action.setStatusTip(status_tip)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action,
            )

        self.actions.append(action)

        return action

    def initGui(self):
        """Initialize plugin GUI."""

        icon_path = os.path.join(
            self.plugin_dir,
            "icon.png",
        )

        self.add_action(
            icon_path,
            self.tr("Create Relation"),
            self.run,
            parent=self.iface.mainWindow(),
            status_tip=self.tr(
                "Create and manage layer relations"
            ),
        )

        self.first_start = True

    def unload(self):
        """Remove plugin GUI."""

        for action in self.actions:
            self.iface.removePluginMenu(
                self.menu,
                action,
            )

            self.iface.removeToolBarIcon(
                action
            )

        self.actions.clear()

        if self.translator:
            QCoreApplication.removeTranslator(
                self.translator
            )

    # ==============================================================
    # RUN
    # ==============================================================

    def run(self):
        """Show the main dialog."""

        if self.first_start or self.dlg is None:

            self.first_start = False

            self.dlg = CreateRelationDialog(
                self.iface.mainWindow()
            )

            self._connect_signals()

            self.populate_layers()

            self.update_relation_information()

            self._set_progress(0)

        self.populate_layers()

        self.update_relation_information()

        self.dlg.show()
        self.dlg.raise_()
        self.dlg.activateWindow()

    def _connect_signals(self):
        """Connect dialog signals."""

        self.dlg.layer1Combo.currentIndexChanged.connect(
            self.populate_fields_layer1
        )

        self.dlg.layer2Combo.currentIndexChanged.connect(
            self.populate_fields_layer2
        )

        self.dlg.relationTypeCombo.currentIndexChanged.connect(
            self.update_relation_information
        )

        self.dlg.createRelationButton.clicked.connect(
            self.create_relation
        )

        self.dlg.openTableButton.clicked.connect(
            self.open_attribute_table
        )

        self.dlg.showRelationsButton.clicked.connect(
            self.show_project_relations
        )

        self.dlg.projectPropertiesButton.clicked.connect(
            self.show_project_properties
        )

        self.dlg.showJoinsButton.clicked.connect(
            self.show_layer_joins
        )

        self.dlg.clearLogButton.clicked.connect(
            self.clear_log
        )

        self.dlg.closeButton.clicked.connect(
            self.close_dialog
        )

        self.dlg.saveToDiskCheckBox.toggled.connect(
            self.update_relation_information
        )

        self.dlg.prefillBridgeCheckBox.toggled.connect(
            self.update_relation_information
        )

    # ==============================================================
    # LAYERS
    # ==============================================================

    def get_vector_layers(self):
        """Return all vector layers loaded in the project."""

        return [
            layer
            for layer in QgsProject.instance()
            .mapLayers()
            .values()
            if isinstance(layer, QgsVectorLayer)
        ]

    def populate_layers(self):
        """Populate parent and child layer combos."""

        current1 = self.dlg.layer1Combo.currentData()
        current2 = self.dlg.layer2Combo.currentData()

        self.dlg.layer1Combo.blockSignals(True)
        self.dlg.layer2Combo.blockSignals(True)

        self.dlg.layer1Combo.clear()
        self.dlg.layer2Combo.clear()

        for layer in self.get_vector_layers():

            self.dlg.layer1Combo.addItem(
                layer.name(),
                layer.id(),
            )

            self.dlg.layer2Combo.addItem(
                layer.name(),
                layer.id(),
            )

        self.dlg.layer1Combo.blockSignals(False)
        self.dlg.layer2Combo.blockSignals(False)

        self._restore_layer(
            self.dlg.layer1Combo,
            current1,
        )

        self._restore_layer(
            self.dlg.layer2Combo,
            current2,
        )

        self.populate_fields_layer1()
        self.populate_fields_layer2()

    @staticmethod
    def _restore_layer(combo, layer_id):

        if not layer_id:
            return

        index = combo.findData(layer_id)

        if index >= 0:
            combo.setCurrentIndex(index)

    def get_layer_from_combo(self, combo):

        layer_id = combo.currentData()

        if not layer_id:
            return None

        return QgsProject.instance().mapLayer(
            layer_id
        )

    # ==============================================================
    # FIELDS
    # ==============================================================

    def populate_fields_layer1(self):

        layer = self.get_layer_from_combo(
            self.dlg.layer1Combo
        )

        self.dlg.field1Combo.blockSignals(True)
        self.dlg.field1Combo.clear()

        if layer:

            for field in layer.fields():

                self.dlg.field1Combo.addItem(
                    field.name(),
                    field.name(),
                )

        self.dlg.field1Combo.blockSignals(False)

        self.update_relation_information()

    def populate_fields_layer2(self):

        layer = self.get_layer_from_combo(
            self.dlg.layer2Combo
        )

        self.dlg.field2Combo.blockSignals(True)
        self.dlg.field2Combo.clear()

        if layer:

            for field in layer.fields():

                self.dlg.field2Combo.addItem(
                    field.name(),
                    field.name(),
                )

        self.dlg.field2Combo.blockSignals(False)

        self.update_relation_information()

    # ==============================================================
    # RELATION INFORMATION
    # ==============================================================

    def update_relation_information(self):

        relation_type = (
            self.dlg.relationTypeCombo.currentData()
        )

        parent = self.get_layer_from_combo(
            self.dlg.layer1Combo
        )

        child = self.get_layer_from_combo(
            self.dlg.layer2Combo
        )

        parent_name = (
            parent.name()
            if parent
            else self.tr("Layer padre")
        )

        child_name = (
            child.name()
            if child
            else self.tr("Layer figlio")
        )

        if relation_type == self.TYPE_ONE_TO_ONE:

            title = self.tr(
                "Relazione uno-a-uno (1:1)"
            )

            text = self.tr(
                "<b>1:1 — Uno a uno</b><br>"
                "Ogni record del layer padre può essere "
                "collegato ad un solo record del layer figlio "
                "e ogni record del figlio può riferirsi ad "
                "un solo record del padre.<br><br>"
                "<b>Esempio:</b> una particella catastale "
                "e la relativa scheda descrittiva.<br>"
                "Il campo del layer figlio viene utilizzato "
                "come chiave esterna verso il campo del "
                "layer padre."
            )

        elif relation_type == self.TYPE_MANY_TO_MANY:

            title = self.tr(
                "Relazione molti-a-molti (N:M)"
            )

            text = self.tr(
                "<b>N:M — Molti a molti</b><br>"
                "Un record del layer padre può essere "
                "associato a molti record del layer figlio "
                "e viceversa.<br><br>"
                "<b>Esempio:</b> un Comune può avere molti "
                "servizi e lo stesso servizio può essere "
                "presente in molti Comuni.<br>"
                "Il plugin crea automaticamente una "
                "<b>tabella ponte</b> contenente le due "
                "chiavi esterne e registra due relazioni "
                "QGIS:<br>"
                "• padre → tabella ponte<br>"
                "• figlio → tabella ponte"
            )

            if self.dlg.prefillBridgeCheckBox.isChecked():

                text += self.tr(
                    "<br>"
                    "<font color='#b36b00'>"
                    "<b>Precompilazione attiva:</b> verranno "
                    "create tutte le combinazioni possibili "
                    "tra i valori distinti dei due campi."
                    "</font>"
                )

        else:

            title = self.tr(
                "Relazione uno-a-molti (1:N)"
            )

            text = self.tr(
                "<b>1:N — Uno a molti</b><br>"
                "Un record del layer padre può essere "
                "associato a più record del layer figlio, "
                "mentre ogni record figlio appartiene "
                "ad un solo padre.<br><br>"
                "<b>Esempio:</b> un Comune può avere molti "
                "Edifici, mentre ogni Edificio appartiene "
                "ad un solo Comune."
            )

        text += self.tr(
            "<br><br>"
            "<b>Struttura selezionata:</b>"
            " {0} → {1}"
        ).format(
            parent_name,
            child_name,
        )

        self.dlg.relationStatusLabel.setText(
            title
        )

        self.dlg.relationInfoTextEdit.setHtml(
            text
        )

        self.dlg.manyToManyGroupBox.setVisible(
            relation_type == self.TYPE_MANY_TO_MANY
        )

    # ==============================================================
    # LOG
    # ==============================================================

    def log(self, message, level="INFO"):

        timestamp = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.dlg.processLogTextEdit.append(
            f"[{timestamp}] [{level}] {message}"
        )

        self.dlg.processLogTextEdit.ensureCursorVisible()

        QCoreApplication.processEvents()

    def clear_log(self):
        self.dlg.processLogTextEdit.clear()

    # ==============================================================
    # PROGRESS
    # ==============================================================

    def _set_progress(self, value):

        value = max(
            0,
            min(100, int(value)),
        )

        self.dlg.progressBar.setValue(
            value
        )

        QCoreApplication.processEvents()

    def _finish_progress(self):

        self._set_progress(100)

        QCoreApplication.processEvents()

        self._set_progress(0)

    # ==============================================================
    # VALIDATION
    # ==============================================================

    def validate_input(self):

        parent_layer = self.get_layer_from_combo(
            self.dlg.layer1Combo
        )

        child_layer = self.get_layer_from_combo(
            self.dlg.layer2Combo
        )

        parent_field = (
            self.dlg.field1Combo.currentData()
        )

        child_field = (
            self.dlg.field2Combo.currentData()
        )

        if not parent_layer or not child_layer:

            raise ValueError(
                self.tr(
                    "Selezionare entrambi i layer."
                )
            )

        if parent_layer.id() == child_layer.id():

            raise ValueError(
                self.tr(
                    "Il layer padre e il layer figlio "
                    "non possono coincidere."
                )
            )

        if not parent_field or not child_field:

            raise ValueError(
                self.tr(
                    "Selezionare entrambi i campi."
                )
            )

        if parent_layer.fields().indexOf(
            parent_field
        ) < 0:

            raise ValueError(
                self.tr(
                    "Il campo del layer padre non esiste."
                )
            )

        if child_layer.fields().indexOf(
            child_field
        ) < 0:

            raise ValueError(
                self.tr(
                    "Il campo del layer figlio non esiste."
                )
            )

        return (
            parent_layer,
            parent_field,
            child_layer,
            child_field,
        )

    def _field_type_compatible(
        self,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        field1 = parent_layer.fields().field(
            parent_field
        )

        field2 = child_layer.fields().field(
            child_field
        )

        if field1.type() == field2.type():
            return True

        if (
            field1.isNumeric()
            and field2.isNumeric()
        ):
            return True

        return False

    def _make_field_like(self, name, source_field):
        """
        Build a new QgsField named `name` that copies the type,
        type name, length and precision of `source_field`.

        QGIS 3.38+ (built against Qt6, as QGIS 4.x is) exposes
        QgsField.metaType() / a QMetaType::Type based QgsField
        constructor and deprecates the older QVariant::Type based
        one still required on QGIS 3.28-3.3x (Qt5). QVariant::Type
        itself no longer exists in Qt6. Try the modern metaType()
        API first and gracefully fall back to the legacy type()
        one, so bridge table fields are created correctly across
        the whole 3.28 - 4.x range declared in metadata.txt.
        """

        if hasattr(
            source_field,
            "metaType",
        ):

            try:

                return QgsField(
                    name,
                    source_field.metaType(),
                    source_field.typeName(),
                    source_field.length(),
                    source_field.precision(),
                )

            except TypeError:

                pass

        return QgsField(
            name,
            source_field.type(),
            source_field.typeName(),
            source_field.length(),
            source_field.precision(),
        )

    # ==============================================================
    # CREATE
    # ==============================================================

    def create_relation(self):

        self._set_progress(0)

        self.dlg.createRelationButton.setEnabled(
            False
        )

        try:

            self.log(
                self.tr(
                    "Avvio creazione della relazione."
                )
            )

            self._set_progress(10)

            (
                parent_layer,
                parent_field,
                child_layer,
                child_field,
            ) = self.validate_input()

            self.log(
                self.tr(
                    "Layer padre: {0}"
                ).format(
                    parent_layer.name()
                )
            )

            self.log(
                self.tr(
                    "Campo padre: {0}"
                ).format(
                    parent_field
                )
            )

            self.log(
                self.tr(
                    "Layer figlio: {0}"
                ).format(
                    child_layer.name()
                )
            )

            self.log(
                self.tr(
                    "Campo figlio: {0}"
                ).format(
                    child_field
                )
            )

            self._set_progress(20)

            if not self._field_type_compatible(
                parent_layer,
                parent_field,
                child_layer,
                child_field,
            ):

                answer = QMessageBox.question(
                    self.dlg,
                    self.tr(
                        "Tipi di campo differenti"
                    ),
                    self.tr(
                        "I due campi non hanno lo stesso "
                        "tipo di dato. Vuoi procedere "
                        "comunque?"
                    ),
                    QMessageBox.StandardButton.Yes
                    | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No,
                )

                if answer == QMessageBox.StandardButton.No:

                    self.log(
                        self.tr(
                            "Operazione annullata per "
                            "incompatibilità dei campi."
                        ),
                        "WARNING",
                    )

                    return

            self._set_progress(30)

            relation_type = (
                self.dlg.relationTypeCombo.currentData()
            )

            if relation_type == self.TYPE_ONE_TO_ONE:

                self.create_one_to_one(
                    parent_layer,
                    parent_field,
                    child_layer,
                    child_field,
                )

            elif relation_type == self.TYPE_MANY_TO_MANY:

                self.create_many_to_many(
                    parent_layer,
                    parent_field,
                    child_layer,
                    child_field,
                )

            else:

                self.create_one_to_many(
                    parent_layer,
                    parent_field,
                    child_layer,
                    child_field,
                )

            self._set_progress(95)

            self.log(
                self.tr(
                    "Operazione completata con successo."
                ),
                "SUCCESS",
            )

        except Exception as exc:

            self.log(
                self.tr(
                    "Errore: {0}"
                ).format(
                    str(exc)
                ),
                "ERROR",
            )

            QMessageBox.critical(
                self.dlg,
                self.tr("Errore"),
                str(exc),
            )

        finally:

            self.dlg.createRelationButton.setEnabled(
                True
            )

            self._finish_progress()

    # ==============================================================
    # RELATION HELPERS
    # ==============================================================

    def _relation_id(
        self,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        return (
            f"cr_{parent_layer.id()}_"
            f"{parent_field}_"
            f"{child_layer.id()}_"
            f"{child_field}_"
            f"{timestamp}"
        )

    def _bridge_relation_id(
        self,
        bridge_layer,
        referenced_layer,
        bridge_field,
        referenced_field,
        side,
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        return (
            f"cr_nm_{side}_"
            f"{bridge_layer.id()}_"
            f"{referenced_layer.id()}_"
            f"{bridge_field}_"
            f"{referenced_field}_"
            f"{timestamp}"
        )

    def _relation_exists(
        self,
        referencing_layer_id,
        referenced_layer_id,
        field_pairs,
    ):

        manager = (
            QgsProject.instance()
            .relationManager()
        )

        for relation in manager.relations().values():

            if (
                relation.referencingLayerId()
                == referencing_layer_id
                and
                relation.referencedLayerId()
                == referenced_layer_id
                and
                relation.fieldPairs()
                == field_pairs
            ):

                return relation

        return None

    def _add_relation(self, manager, relation):
        """
        Register a relation with the project relation manager and
        report whether it actually succeeded.

        QgsRelationManager.addRelation() does not return a usable
        boolean in every QGIS/PyQGIS build: depending on the bindings
        it may come back as ``None`` even when the relation was
        registered correctly. Relying on ``if manager.addRelation(...)``
        therefore raises a false "QGIS non ha accettato la relazione"
        error on a perfectly successful registration.

        The only trustworthy check is to ask the manager again
        afterwards whether the relation is present and valid.
        """

        manager.addRelation(
            relation
        )

        registered = manager.relation(
            relation.id()
        )

        return bool(
            registered
            and registered.isValid()
        )

    def _remove_relation(self, manager, relation_id):
        """
        Remove a relation from the project relation manager and
        report whether it actually succeeded.

        Same caveat as _add_relation(): QgsRelationManager.removeRelation()
        cannot be trusted to return a meaningful boolean, so success is
        verified by checking that the relation is no longer registered.
        """

        manager.removeRelation(
            relation_id
        )

        return relation_id not in manager.relations()

    def _build_relation(
        self,
        name,
        relation_id,
        referencing_layer,
        referencing_field,
        referenced_layer,
        referenced_field,
    ):

        relation = QgsRelation()

        relation.setId(
            relation_id
        )

        relation.setName(
            name
        )

        relation.setReferencingLayer(
            referencing_layer.id()
        )

        relation.setReferencedLayer(
            referenced_layer.id()
        )

        relation.addFieldPair(
            referencing_field,
            referenced_field,
        )

        if not relation.isValid():

            raise RuntimeError(
                self.tr(
                    "Relazione non valida: {0}"
                ).format(
                    relation.validationError()
                )
            )

        return relation

    # ==============================================================
    # 1:1
    # ==============================================================

    def create_one_to_one(
        self,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        self.log(
            self.tr(
                "Creazione relazione 1:1."
            )
        )

        self._validate_one_to_one_keys(
            parent_layer,
            parent_field,
            child_layer,
            child_field,
        )

        field_pairs = {
            child_field: parent_field
        }

        existing = self._relation_exists(
            child_layer.id(),
            parent_layer.id(),
            field_pairs,
        )

        if existing:

            self.log(
                self.tr(
                    "La relazione è già presente: {0}"
                ).format(
                    existing.name()
                ),
                "WARNING",
            )

            return

        relation = self._build_relation(
            self.tr(
                "{0} → {1} (1:1)"
            ).format(
                parent_layer.name(),
                child_layer.name(),
            ),
            self._relation_id(
                parent_layer,
                parent_field,
                child_layer,
                child_field,
            ),
            child_layer,
            child_field,
            parent_layer,
            parent_field,
        )

        if not self._add_relation(
            QgsProject.instance().relationManager(),
            relation,
        ):

            raise RuntimeError(
                self.tr(
                    "QGIS non ha accettato la relazione 1:1."
                )
            )

        self.log(
            self.tr(
                "Relazione 1:1 registrata nel progetto."
            ),
            "SUCCESS",
        )

    def _validate_one_to_one_keys(
        self,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        parent_values = set()
        parent_duplicates = 0

        for feature in parent_layer.getFeatures():

            value = feature[parent_field]

            if value in parent_values:
                parent_duplicates += 1
            else:
                parent_values.add(value)

        child_values = set()
        child_duplicates = 0

        for feature in child_layer.getFeatures():

            value = feature[child_field]

            if value in child_values:
                child_duplicates += 1
            else:
                child_values.add(value)

        if parent_duplicates:

            self.log(
                self.tr(
                    "Il campo padre contiene {0} "
                    "valori duplicati."
                ).format(
                    parent_duplicates
                ),
                "WARNING",
            )

        if child_duplicates:

            self.log(
                self.tr(
                    "Il campo figlio contiene {0} "
                    "valori duplicati."
                ).format(
                    child_duplicates
                ),
                "WARNING",
            )

        if parent_duplicates or child_duplicates:

            answer = QMessageBox.warning(
                self.dlg,
                self.tr(
                    "Chiavi non univoche"
                ),
                self.tr(
                    "Per una relazione 1:1 i valori delle "
                    "chiavi dovrebbero essere univoci.\n\n"
                    "Sono stati trovati duplicati. "
                    "Vuoi continuare?"
                ),
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if answer == QMessageBox.StandardButton.No:

                raise RuntimeError(
                    self.tr(
                        "Creazione della relazione 1:1 annullata."
                    )
                )

    # ==============================================================
    # 1:N
    # ==============================================================

    def create_one_to_many(
        self,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        self.log(
            self.tr(
                "Creazione relazione 1:N."
            )
        )

        field_pairs = {
            child_field: parent_field
        }

        existing = self._relation_exists(
            child_layer.id(),
            parent_layer.id(),
            field_pairs,
        )

        if existing:

            self.log(
                self.tr(
                    "La relazione 1:N è già presente: {0}"
                ).format(
                    existing.name()
                ),
                "WARNING",
            )

            return

        relation = self._build_relation(
            self.tr(
                "{0} → {1} (1:N)"
            ).format(
                parent_layer.name(),
                child_layer.name(),
            ),
            self._relation_id(
                parent_layer,
                parent_field,
                child_layer,
                child_field,
            ),
            child_layer,
            child_field,
            parent_layer,
            parent_field,
        )

        if not self._add_relation(
            QgsProject.instance().relationManager(),
            relation,
        ):

            raise RuntimeError(
                self.tr(
                    "QGIS non ha accettato la relazione 1:N."
                )
            )

        self.log(
            self.tr(
                "Relazione 1:N registrata nel progetto."
            ),
            "SUCCESS",
        )

    # ==============================================================
    # N:M
    # ==============================================================

    def create_many_to_many(
        self,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):
        """
        Create a complete many-to-many structure.

        Structure:

            PARENT
              |
              | 1:N
              v
        BRIDGE TABLE
              |
              | N:1
              v
            CHILD

        The bridge table is the referencing layer in both
        QgsRelation objects.
        """

        project = QgsProject.instance()
        manager = project.relationManager()

        self.log(
            self.tr(
                "Creazione struttura molti-a-molti."
            )
        )

        # ----------------------------------------------------------
        # BRIDGE NAME
        # ----------------------------------------------------------

        bridge_name = (
            self.dlg.ponteTableNameLineEdit
            .text()
            .strip()
        )

        if not bridge_name:

            bridge_name = (
                f"{parent_layer.name()}_"
                f"{child_layer.name()}_bridge"
            )

        bridge_name = self._unique_layer_name(
            bridge_name
        )

        self.log(
            self.tr(
                "Nome tabella ponte: {0}"
            ).format(
                bridge_name
            )
        )

        self._set_progress(40)

        # ----------------------------------------------------------
        # CREATE BRIDGE
        # ----------------------------------------------------------

        bridge_layer = self._create_bridge_layer(
            bridge_name,
            parent_layer,
            parent_field,
            child_layer,
            child_field,
        )

        if (
            not bridge_layer
            or not bridge_layer.isValid()
        ):

            raise RuntimeError(
                self.tr(
                    "La tabella ponte non è valida."
                )
            )

        self._set_progress(50)

        # ----------------------------------------------------------
        # PREFILL
        # ----------------------------------------------------------

        if self.dlg.prefillBridgeCheckBox.isChecked():

            self._prefill_bridge(
                bridge_layer,
                parent_layer,
                parent_field,
                child_layer,
                child_field,
            )

        self._set_progress(70)

        # ----------------------------------------------------------
        # SAVE BEFORE RELATIONS
        # ----------------------------------------------------------

        if self.dlg.saveToDiskCheckBox.isChecked():

            bridge_layer = self._save_bridge_layer(
                bridge_layer
            )

            if not bridge_layer:

                raise RuntimeError(
                    self.tr(
                        "La tabella ponte non è disponibile "
                        "dopo il salvataggio."
                    )
                )

            # Re-apply metadata because a newly loaded OGR
            # layer has a new QGIS layer id.
            self._set_bridge_properties(
                bridge_layer,
                parent_layer,
                parent_field,
                child_layer,
                child_field,
            )

        # ----------------------------------------------------------
        # ADD FINAL BRIDGE LAYER TO PROJECT
        # ----------------------------------------------------------

        if bridge_layer.id() not in project.mapLayers():

            project.addMapLayer(
                bridge_layer
            )

        self._last_bridge_layer_id = (
            bridge_layer.id()
        )

        self.log(
            self.tr(
                "Tabella ponte disponibile nel progetto: {0}"
            ).format(
                bridge_layer.name()
            ),
            "SUCCESS",
        )

        self._set_progress(75)

        # ----------------------------------------------------------
        # GET BRIDGE FIELDS
        # ----------------------------------------------------------

        bridge_parent_field = (
            bridge_layer.customProperty(
                "create_relation/parent_field"
            )
        )

        bridge_child_field = (
            bridge_layer.customProperty(
                "create_relation/child_field"
            )
        )

        if not bridge_parent_field:

            bridge_parent_field = self._bridge_field_name(
                "parent",
                parent_field,
            )

        if not bridge_child_field:

            bridge_child_field = self._bridge_field_name(
                "child",
                child_field,
            )

        # Make absolutely sure fields exist.
        if bridge_layer.fields().indexOf(
            bridge_parent_field
        ) < 0:

            raise RuntimeError(
                self.tr(
                    "Il campo ponte padre '{0}' "
                    "non esiste."
                ).format(
                    bridge_parent_field
                )
            )

        if bridge_layer.fields().indexOf(
            bridge_child_field
        ) < 0:

            raise RuntimeError(
                self.tr(
                    "Il campo ponte figlio '{0}' "
                    "non esiste."
                ).format(
                    bridge_child_field
                )
            )

        # ----------------------------------------------------------
        # CREATE RELATION OBJECTS
        # ----------------------------------------------------------

        relation_parent = self._create_bridge_relation(
            bridge_layer,
            parent_layer,
            parent_field,
            bridge_parent_field,
            "parent",
        )

        relation_child = self._create_bridge_relation(
            bridge_layer,
            child_layer,
            child_field,
            bridge_child_field,
            "child",
        )

        self.log(
            self.tr(
                "Due relazioni N:M preparate."
            )
        )

        self._set_progress(82)

        # ----------------------------------------------------------
        # REGISTER RELATION 1
        # ----------------------------------------------------------

        if self._add_relation(
            manager,
            relation_parent,
        ):

            self.log(
                self.tr(
                    "Relazione padre → tabella ponte registrata."
                ),
                "SUCCESS",
            )

        else:

            raise RuntimeError(
                self.tr(
                    "QGIS non ha accettato la relazione "
                    "padre → tabella ponte.\n\n"
                    "ID: {0}\n"
                    "Campo ponte: {1}\n"
                    "Campo padre: {2}"
                ).format(
                    relation_parent.id(),
                    bridge_parent_field,
                    parent_field,
                )
            )

        # ----------------------------------------------------------
        # REGISTER RELATION 2
        # ----------------------------------------------------------

        if self._add_relation(
            manager,
            relation_child,
        ):

            self.log(
                self.tr(
                    "Relazione figlio → tabella ponte registrata."
                ),
                "SUCCESS",
            )

        else:

            # Remove first relation.
            self._remove_relation(
                manager,
                relation_parent.id(),
            )

            raise RuntimeError(
                self.tr(
                    "QGIS non ha accettato la relazione "
                    "figlio → tabella ponte.\n\n"
                    "La prima relazione è stata annullata.\n\n"
                    "ID: {0}\n"
                    "Campo ponte: {1}\n"
                    "Campo figlio: {2}"
                ).format(
                    relation_child.id(),
                    bridge_child_field,
                    child_field,
                )
            )

        self._set_progress(90)

        # ----------------------------------------------------------
        # FINAL VALIDATION
        # ----------------------------------------------------------

        registered_parent = manager.relation(
            relation_parent.id()
        )

        registered_child = manager.relation(
            relation_child.id()
        )

        if not registered_parent.isValid():

            self._remove_relation(
                manager,
                relation_parent.id(),
            )

            self._remove_relation(
                manager,
                relation_child.id(),
            )

            raise RuntimeError(
                self.tr(
                    "La relazione padre → tabella ponte "
                    "risulta non valida dopo la registrazione."
                )
            )

        if not registered_child.isValid():

            self._remove_relation(
                manager,
                relation_parent.id(),
            )

            self._remove_relation(
                manager,
                relation_child.id(),
            )

            raise RuntimeError(
                self.tr(
                    "La relazione figlio → tabella ponte "
                    "risulta non valida dopo la registrazione."
                )
            )

        self.log(
            self.tr(
                "Entrambe le relazioni N:M sono state "
                "registrate correttamente."
            ),
            "SUCCESS",
        )

        self.log(
            self.tr(
                "Tabella ponte: {0}"
            ).format(
                bridge_layer.name()
            ),
            "INFO",
        )

        self.log(
            self.tr(
                "Campo ponte padre: {0}"
            ).format(
                bridge_parent_field
            ),
            "INFO",
        )

        self.log(
            self.tr(
                "Campo ponte figlio: {0}"
            ).format(
                bridge_child_field
            ),
            "INFO",
        )

        QMessageBox.information(
            self.dlg,
            self.tr(
                "Relazione N:M creata"
            ),
            self.tr(
                "La struttura molti-a-molti è stata "
                "creata correttamente.\n\n"
                "Tabella ponte:\n"
                "{0}\n\n"
                "Sono state registrate entrambe le "
                "relazioni QGIS:\n\n"
                "• {1} → tabella ponte\n"
                "• {2} → tabella ponte"
            ).format(
                bridge_layer.name(),
                parent_layer.name(),
                child_layer.name(),
            ),
        )

    # ==============================================================
    # BRIDGE RELATION
    # ==============================================================

    def _create_bridge_relation(
        self,
        bridge_layer,
        referenced_layer,
        referenced_field,
        bridge_field,
        side,
    ):
        """
        Create one QgsRelation for the N:M bridge.

        The bridge is always the referencing layer.

        Example:

            bridge.cr_parent_id -> parent.id

        therefore:

            referencingLayer = bridge
            referencingField = cr_parent_id
            referencedLayer  = parent
            referencedField  = id
        """

        if not bridge_layer or not bridge_layer.isValid():

            raise RuntimeError(
                self.tr(
                    "La tabella ponte non è valida."
                )
            )

        if not referenced_layer or not referenced_layer.isValid():

            raise RuntimeError(
                self.tr(
                    "Il layer referenziato non è valido."
                )
            )

        if bridge_layer.fields().indexOf(
            bridge_field
        ) < 0:

            raise RuntimeError(
                self.tr(
                    "Il campo '{0}' non esiste "
                    "nella tabella ponte."
                ).format(
                    bridge_field
                )
            )

        if referenced_layer.fields().indexOf(
            referenced_field
        ) < 0:

            raise RuntimeError(
                self.tr(
                    "Il campo '{0}' non esiste "
                    "nel layer '{1}'."
                ).format(
                    referenced_field,
                    referenced_layer.name(),
                )
            )

        bridge_qfield = (
            bridge_layer.fields().field(
                bridge_field
            )
        )

        referenced_qfield = (
            referenced_layer.fields().field(
                referenced_field
            )
        )

        if (
            bridge_qfield.type()
            != referenced_qfield.type()
        ):

            if not (
                bridge_qfield.isNumeric()
                and referenced_qfield.isNumeric()
            ):

                raise RuntimeError(
                    self.tr(
                        "Tipi incompatibili per la relazione "
                        "N:M '{0}': {1} → {2}."
                    ).format(
                        side,
                        bridge_qfield.typeName(),
                        referenced_qfield.typeName(),
                    )
                )

        relation_name = self.tr(
            "{0} → {1} (N:M)"
        ).format(
            referenced_layer.name(),
            bridge_layer.name(),
        )

        relation_id = self._bridge_relation_id(
            bridge_layer,
            referenced_layer,
            bridge_field,
            referenced_field,
            side,
        )

        field_pairs = {
            bridge_field: referenced_field
        }

        existing = self._relation_exists(
            bridge_layer.id(),
            referenced_layer.id(),
            field_pairs,
        )

        if existing:

            raise RuntimeError(
                self.tr(
                    "Esiste già una relazione tra "
                    "la tabella ponte '{0}' e il layer "
                    "'{1}' per i campi '{2}' → '{3}'."
                ).format(
                    bridge_layer.name(),
                    referenced_layer.name(),
                    bridge_field,
                    referenced_field,
                )
            )

        relation = self._build_relation(
            relation_name,
            relation_id,
            bridge_layer,
            bridge_field,
            referenced_layer,
            referenced_field,
        )

        if not relation.isValid():

            raise RuntimeError(
                self.tr(
                    "Relazione N:M '{0}' non valida: {1}"
                ).format(
                    relation_name,
                    relation.validationError(),
                )
            )

        return relation

    # ==============================================================
    # BRIDGE
    # ==============================================================

    def _create_bridge_layer(
        self,
        name,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        bridge = QgsVectorLayer(
            "None",
            name,
            "memory",
        )

        if not bridge.isValid():

            raise RuntimeError(
                self.tr(
                    "Impossibile creare la tabella ponte."
                )
            )

        parent_source_field = (
            parent_layer.fields().field(
                parent_field
            )
        )

        child_source_field = (
            child_layer.fields().field(
                child_field
            )
        )

        parent_bridge_field = (
            self._bridge_field_name(
                "parent",
                parent_field,
            )
        )

        child_bridge_field = (
            self._bridge_field_name(
                "child",
                child_field,
            )
        )

        parent_bridge_qfield = self._make_field_like(
            parent_bridge_field,
            parent_source_field,
        )

        child_bridge_qfield = self._make_field_like(
            child_bridge_field,
            child_source_field,
        )

        provider = bridge.dataProvider()

        if not provider.addAttributes(
            [
                parent_bridge_qfield,
                child_bridge_qfield,
            ]
        ):

            raise RuntimeError(
                self.tr(
                    "Impossibile creare i campi "
                    "della tabella ponte."
                )
            )

        bridge.updateFields()

        self._set_bridge_properties(
            bridge,
            parent_layer,
            parent_field,
            child_layer,
            child_field,
        )

        return bridge

    def _set_bridge_properties(
        self,
        bridge,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        parent_bridge_field = (
            self._bridge_field_name(
                "parent",
                parent_field,
            )
        )

        child_bridge_field = (
            self._bridge_field_name(
                "child",
                child_field,
            )
        )

        bridge.setCustomProperty(
            "create_relation/type",
            "many_to_many_bridge",
        )

        bridge.setCustomProperty(
            "create_relation/parent_layer_id",
            parent_layer.id(),
        )

        bridge.setCustomProperty(
            "create_relation/parent_field",
            parent_bridge_field,
        )

        bridge.setCustomProperty(
            "create_relation/child_layer_id",
            child_layer.id(),
        )

        bridge.setCustomProperty(
            "create_relation/child_field",
            child_bridge_field,
        )

        bridge.setCustomProperty(
            "create_relation/source_parent_field",
            parent_field,
        )

        bridge.setCustomProperty(
            "create_relation/source_child_field",
            child_field,
        )

    @staticmethod
    def _bridge_field_name(
        side,
        field_name,
    ):

        clean = (
            field_name
            .replace(" ", "_")
            .replace("-", "_")
        )

        return f"cr_{side}_{clean}"

    def _prefill_bridge(
        self,
        bridge,
        parent_layer,
        parent_field,
        child_layer,
        child_field,
    ):

        """Generate distinct parent/child combinations."""

        parent_values = self._distinct_values(
            parent_layer,
            parent_field,
        )

        child_values = self._distinct_values(
            child_layer,
            child_field,
        )

        total = (
            len(parent_values)
            * len(child_values)
        )

        self.log(
            self.tr(
                "Precompilazione N:M: {0} valori padre × "
                "{1} valori figlio = {2} combinazioni."
            ).format(
                len(parent_values),
                len(child_values),
                total,
            )
        )

        if total == 0:

            self.log(
                self.tr(
                    "Nessuna combinazione da creare."
                ),
                "WARNING",
            )

            return

        if total > 100000:

            answer = QMessageBox.warning(
                self.dlg,
                self.tr(
                    "Numero elevato di combinazioni"
                ),
                self.tr(
                    "La precompilazione genererebbe "
                    "{0} record.\n\n"
                    "Questa operazione può richiedere "
                    "molta memoria e molto tempo.\n\n"
                    "Vuoi continuare?"
                ).format(
                    total
                ),
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if answer == QMessageBox.StandardButton.No:

                self.log(
                    self.tr(
                        "Precompilazione annullata dall'utente."
                    ),
                    "WARNING",
                )

                return

        parent_bridge_field = (
            bridge.customProperty(
                "create_relation/parent_field"
            )
        )

        child_bridge_field = (
            bridge.customProperty(
                "create_relation/child_field"
            )
        )

        provider = bridge.dataProvider()

        batch = []
        inserted = 0

        batch_size = 1000

        for index, parent_value in enumerate(
            parent_values
        ):

            for child_value in child_values:

                feature = QgsFeature(
                    bridge.fields()
                )

                feature.setAttribute(
                    parent_bridge_field,
                    parent_value,
                )

                feature.setAttribute(
                    child_bridge_field,
                    child_value,
                )

                batch.append(feature)

                if len(batch) >= batch_size:

                    ok, added = provider.addFeatures(
                        batch
                    )

                    if not ok:

                        raise RuntimeError(
                            self.tr(
                                "Errore durante la "
                                "precompilazione della "
                                "tabella ponte."
                            )
                        )

                    inserted += len(added)

                    batch.clear()

            progress = (
                (index + 1)
                / len(parent_values)
            )

            self._set_progress(
                55 + int(progress * 15)
            )

        if batch:

            ok, added = provider.addFeatures(
                batch
            )

            if not ok:

                raise RuntimeError(
                    self.tr(
                        "Errore durante l'inserimento "
                        "dei record finali."
                    )
                )

            inserted += len(added)

        bridge.updateFields()
        bridge.updateExtents()

        self.log(
            self.tr(
                "Precompilazione completata: {0} record."
            ).format(
                inserted
            ),
            "SUCCESS",
        )

    @staticmethod
    def _distinct_values(
        layer,
        field_name,
    ):

        values = set()

        for feature in layer.getFeatures():

            value = feature[field_name]

            if value is None:
                continue

            try:

                if value.isNull():
                    continue

            except AttributeError:
                pass

            try:

                values.add(value)

            except TypeError:

                values.add(
                    str(value)
                )

        return list(values)

    def _unique_layer_name(
        self,
        base_name,
    ):

        names = {
            layer.name()
            for layer in self.get_vector_layers()
        }

        if base_name not in names:
            return base_name

        counter = 2

        while (
            f"{base_name}_{counter}"
            in names
        ):

            counter += 1

        return f"{base_name}_{counter}"

    # ==============================================================
    # SAVE BRIDGE
    # ==============================================================

    def _save_bridge_layer(
        self,
        bridge_layer,
    ):

        path, selected_filter = (
            QFileDialog.getSaveFileName(
                self.dlg,
                self.tr(
                    "Salva tabella ponte"
                ),
                "",
                self.tr(
                    "GeoPackage (*.gpkg);;"
                    "GeoJSON (*.geojson);;"
                    "Shapefile (*.shp)"
                ),
            )
        )

        if not path:

            self.log(
                self.tr(
                    "Salvataggio su disco annullato. "
                    "La tabella ponte rimane temporanea."
                ),
                "WARNING",
            )

            return bridge_layer

        if "GeoPackage" in selected_filter:

            driver = "GPKG"
            extension = ".gpkg"

        elif "GeoJSON" in selected_filter:

            driver = "GeoJSON"
            extension = ".geojson"

        else:

            driver = "ESRI Shapefile"
            extension = ".shp"

        if not path.lower().endswith(
            extension
        ):

            path += extension

        options = (
            QgsVectorFileWriter.SaveVectorOptions()
        )

        options.driverName = driver
        options.fileEncoding = "UTF-8"

        transform_context = (
            QgsProject.instance()
            .transformContext()
        )

        result = (
            QgsVectorFileWriter.writeAsVectorFormatV3(
                bridge_layer,
                path,
                transform_context,
                options,
            )
        )

        error = result[0]

        error_message = (
            result[1]
            if len(result) > 1
            else ""
        )

        if (
            error
            != QgsVectorFileWriter.WriterError.NoError
        ):

            raise RuntimeError(
                self.tr(
                    "Errore nel salvataggio della "
                    "tabella ponte: {0}"
                ).format(
                    error_message
                )
            )

        self.log(
            self.tr(
                "Tabella ponte salvata su disco: {0}"
            ).format(
                path
            ),
            "SUCCESS",
        )

        old_id = bridge_layer.id()

        if old_id in (
            QgsProject.instance()
            .mapLayers()
        ):

            QgsProject.instance().removeMapLayer(
                old_id
            )

        saved_layer = QgsVectorLayer(
            path,
            bridge_layer.name(),
            "ogr",
        )

        if not saved_layer.isValid():

            raise RuntimeError(
                self.tr(
                    "La tabella ponte salvata non "
                    "può essere ricaricata."
                )
            )

        QgsProject.instance().addMapLayer(
            saved_layer
        )

        self.log(
            self.tr(
                "Tabella ponte ricaricata dal file salvato."
            ),
            "SUCCESS",
        )

        return saved_layer

    # ==============================================================
    # ATTRIBUTE TABLE
    # ==============================================================

    def _selected_layer_for_tools(self):

        if self._last_bridge_layer_id:

            bridge = (
                QgsProject.instance()
                .mapLayer(
                    self._last_bridge_layer_id
                )
            )

            if bridge:
                return bridge

        layer1 = self.get_layer_from_combo(
            self.dlg.layer1Combo
        )

        if layer1:
            return layer1

        return self.get_layer_from_combo(
            self.dlg.layer2Combo
        )

    def open_attribute_table(self):

        layer = self._selected_layer_for_tools()

        if not layer:

            QMessageBox.warning(
                self.dlg,
                self.tr(
                    "Layer non selezionato"
                ),
                self.tr(
                    "Selezionare un layer padre o figlio."
                ),
            )

            return

        self.log(
            self.tr(
                "Apertura tabella attributi: {0}"
            ).format(
                layer.name()
            )
        )

        try:

            self.iface.setActiveLayer(
                layer
            )

            self.iface.showAttributeTable(
                layer
            )

            self.log(
                self.tr(
                    "Tabella attributi aperta: {0}"
                ).format(
                    layer.name()
                ),
                "SUCCESS",
            )

        except Exception as exc:

            self.log(
                self.tr(
                    "Impossibile aprire la tabella attributi: {0}"
                ).format(
                    str(exc)
                ),
                "ERROR",
            )

            QMessageBox.critical(
                self.dlg,
                self.tr("Errore"),
                self.tr(
                    "Impossibile aprire la tabella attributi.\n\n{0}"
                ).format(
                    str(exc)
                ),
            )

    # ==============================================================
    # PROJECT PROPERTIES
    # ==============================================================

    def show_project_properties(self):

        self.iface.showProjectPropertiesDialog()

        self.log(
            self.tr(
                "Proprietà del progetto aperte."
            )
        )

    # ==============================================================
    # PROJECT RELATIONS
    # ==============================================================

    def show_project_relations(self):
        """Show project relations and allow deletion."""

        manager = (
            QgsProject.instance()
            .relationManager()
        )

        dialog = QDialog(
            self.dlg
        )

        dialog.setWindowTitle(
            self.tr(
                "Relazioni del progetto"
            )
        )

        dialog.resize(
            760,
            500,
        )

        layout = QVBoxLayout(
            dialog
        )

        info_label = QLabel()

        layout.addWidget(
            info_label
        )

        list_widget = QListWidget()

        layout.addWidget(
            list_widget,
            1,
        )

        buttons_layout = QHBoxLayout()

        delete_button = QPushButton(
            icon("delete.svg"),
            self.tr(
                "Elimina relazione"
            ),
        )

        delete_button.setStyleSheet(
            """
            QPushButton {
                color: #b3261e;
            }

            QPushButton:hover {
                background-color: #fce8e6;
            }
            """
        )

        delete_button.setEnabled(
            False
        )

        close_button = QPushButton(
            icon("close.svg"),
            self.tr(
                "Chiudi"
            ),
        )

        buttons_layout.addWidget(
            delete_button
        )

        buttons_layout.addStretch()

        buttons_layout.addWidget(
            close_button
        )

        layout.addLayout(
            buttons_layout
        )

        def refresh_relations():

            list_widget.clear()

            relations = list(
                manager.relations().values()
            )

            info_label.setText(
                self.tr(
                    "Relazioni presenti: {0}"
                ).format(
                    len(relations)
                )
            )

            for relation in relations:

                referenced = (
                    relation.referencedLayer()
                )

                referencing = (
                    relation.referencingLayer()
                )

                referenced_name = (
                    referenced.name()
                    if referenced
                    else self.tr(
                        "Layer non disponibile"
                    )
                )

                referencing_name = (
                    referencing.name()
                    if referencing
                    else self.tr(
                        "Layer non disponibile"
                    )
                )

                text = (
                    f"{relation.name()} | "
                    f"{referenced_name} ← "
                    f"{referencing_name} | "
                    f"{relation.fieldPairs()}"
                )

                item = QListWidgetItem(
                    text
                )

                item.setData(
                    Qt.ItemDataRole.UserRole,
                    relation.id(),
                )

                list_widget.addItem(
                    item
                )

            delete_button.setEnabled(
                list_widget.currentItem()
                is not None
            )

        def selection_changed():

            delete_button.setEnabled(
                list_widget.currentItem()
                is not None
            )

        def delete_relation():

            item = list_widget.currentItem()

            if not item:
                return

            relation_id = item.data(
                Qt.ItemDataRole.UserRole
            )

            relation = manager.relation(
                relation_id
            )

            if not relation.isValid():

                QMessageBox.warning(
                    dialog,
                    self.tr(
                        "Relazione non disponibile"
                    ),
                    self.tr(
                        "La relazione selezionata "
                        "non è più disponibile."
                    ),
                )

                refresh_relations()

                return

            reply = QMessageBox.question(
                dialog,
                self.tr(
                    "Conferma eliminazione"
                ),
                self.tr(
                    "Vuoi eliminare la relazione "
                    "'{0}'?\n\n"
                    "La relazione verrà rimossa dal "
                    "progetto.\n\n"
                    "I layer e i dati non verranno eliminati."
                ).format(
                    relation.name()
                ),
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if (
                reply
                != QMessageBox.StandardButton.Yes
            ):

                return

            if self._remove_relation(
                manager,
                relation_id,
            ):

                self.log(
                    self.tr(
                        "Relazione eliminata: {0}"
                    ).format(
                        relation.name()
                    ),
                    "SUCCESS",
                )

                refresh_relations()

            else:

                QMessageBox.critical(
                    dialog,
                    self.tr(
                        "Errore"
                    ),
                    self.tr(
                        "QGIS non ha potuto eliminare "
                        "la relazione."
                    ),
                )

        list_widget.itemSelectionChanged.connect(
            selection_changed
        )

        delete_button.clicked.connect(
            delete_relation
        )

        close_button.clicked.connect(
            dialog.accept
        )

        refresh_relations()

        dialog.exec()

        self.log(
            self.tr(
                "Elenco delle relazioni del progetto visualizzato."
            )
        )

    # ==============================================================
    # JOINS
    # ==============================================================

    def show_layer_joins(self):
        """Show joins of the selected layer."""

        layer = self._selected_layer_for_tools()

        if not layer:

            QMessageBox.warning(
                self.dlg,
                self.tr(
                    "Layer non selezionato"
                ),
                self.tr(
                    "Selezionare un layer."
                ),
            )

            return

        dialog = QDialog(
            self.dlg
        )

        dialog.setWindowTitle(
            self.tr(
                "Join - {0}"
            ).format(
                layer.name()
            )
        )

        dialog.resize(
            700,
            450,
        )

        layout = QVBoxLayout(
            dialog
        )

        info_label = QLabel()

        layout.addWidget(
            info_label
        )

        list_widget = QListWidget()

        layout.addWidget(
            list_widget,
            1,
        )

        buttons_layout = QHBoxLayout()

        remove_button = QPushButton(
            icon("delete.svg"),
            self.tr(
                "Rimuovi join"
            ),
        )

        remove_button.setStyleSheet(
            """
            QPushButton {
                color: #b3261e;
            }

            QPushButton:hover {
                background-color: #fce8e6;
            }
            """
        )

        remove_button.setEnabled(
            False
        )

        close_button = QPushButton(
            icon("close.svg"),
            self.tr(
                "Chiudi"
            ),
        )

        buttons_layout.addWidget(
            remove_button
        )

        buttons_layout.addStretch()

        buttons_layout.addWidget(
            close_button
        )

        layout.addLayout(
            buttons_layout
        )

        def refresh_joins():

            list_widget.clear()

            joins = layer.vectorJoins()

            info_label.setText(
                self.tr(
                    "Join presenti: {0}"
                ).format(
                    len(joins)
                )
            )

            for join in joins:

                join_layer = (
                    QgsProject.instance()
                    .mapLayer(
                        join.joinLayerId()
                    )
                )

                join_layer_name = (
                    join_layer.name()
                    if join_layer
                    else self.tr(
                        "Layer non disponibile"
                    )
                )

                text = (
                    f"{join_layer_name} | "
                    f"{join.targetFieldName()} = "
                    f"{join.joinFieldName()}"
                )

                item = QListWidgetItem(
                    text
                )

                item.setData(
                    Qt.ItemDataRole.UserRole,
                    join,
                )

                list_widget.addItem(
                    item
                )

            remove_button.setEnabled(
                list_widget.currentItem()
                is not None
            )

        def selection_changed():

            remove_button.setEnabled(
                list_widget.currentItem()
                is not None
            )

        def remove_join():

            item = list_widget.currentItem()

            if not item:
                return

            join = item.data(
                Qt.ItemDataRole.UserRole
            )

            if join is None:
                return

            join_layer = (
                QgsProject.instance()
                .mapLayer(
                    join.joinLayerId()
                )
            )

            join_layer_name = (
                join_layer.name()
                if join_layer
                else self.tr(
                    "Layer non disponibile"
                )
            )

            reply = QMessageBox.question(
                dialog,
                self.tr(
                    "Conferma rimozione"
                ),
                self.tr(
                    "Vuoi rimuovere questo join?\n\n"
                    "Layer: {0}\n"
                    "Campo destinazione: {1}\n"
                    "Campo join: {2}\n\n"
                    "Verrà rimosso solo il join. "
                    "I layer e i dati originali "
                    "non verranno eliminati."
                ).format(
                    join_layer_name,
                    join.targetFieldName(),
                    join.joinFieldName(),
                ),
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if (
                reply
                != QMessageBox.StandardButton.Yes
            ):

                return

            layer.removeJoin(
                join.joinLayerId()
            )

            self.log(
                self.tr(
                    "Join rimosso da {0}: {1}"
                ).format(
                    layer.name(),
                    join_layer_name,
                ),
                "SUCCESS",
            )

            refresh_joins()

        list_widget.itemSelectionChanged.connect(
            selection_changed
        )

        remove_button.clicked.connect(
            remove_join
        )

        close_button.clicked.connect(
            dialog.accept
        )

        refresh_joins()

        dialog.exec()

        self.log(
            self.tr(
                "Elenco join visualizzato per {0}."
            ).format(
                layer.name()
            )
        )

    # ==============================================================
    # CLOSE
    # ==============================================================

    def close_dialog(self):

        self._set_progress(0)

        if self.dlg:

            self.dlg.hide()
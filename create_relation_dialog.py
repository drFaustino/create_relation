# -*- coding: utf-8 -*-

import os

from qgis.PyQt.QtCore import QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

ICONS_DIR = os.path.join(
    os.path.dirname(__file__),
    "icons",
)


def icon(name):
    """Return a QIcon for the given SVG file name in icons/, or a
    null QIcon if the file is missing (buttons simply show no icon)."""

    path = os.path.join(
        ICONS_DIR,
        name,
    )

    return QIcon(path) if os.path.exists(path) else QIcon()


class CreateRelationDialog(QDialog):
    """Main Create Relation 1.0 dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(
            self.tr("Create Relation")
        )

        # ----------------------------------------------------------
        # WINDOW SIZE
        # ----------------------------------------------------------

        self.setMinimumSize(
            760,
            600,
        )

        self.resize(
            900,
            700,
        )

        self._build_ui()

    # ==============================================================
    # TRANSLATION
    # ==============================================================

    @staticmethod
    def tr(message):
        return QCoreApplication.translate(
            "CreateRelationDialog",
            message,
        )

    # ==============================================================
    # UI
    # ==============================================================

    def _build_ui(self):

        # ----------------------------------------------------------
        # MAIN DIALOG LAYOUT
        # ----------------------------------------------------------

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            8,
            8,
            8,
            8,
        )

        main_layout.setSpacing(
            6
        )

        # ----------------------------------------------------------
        # SCROLL AREA
        # ----------------------------------------------------------

        scroll_area = QScrollArea()

        scroll_area.setWidgetResizable(
            True
        )

        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # ----------------------------------------------------------
        # SCROLL CONTENT
        # ----------------------------------------------------------

        content_widget = QWidget()

        content_layout = QVBoxLayout(
            content_widget
        )

        content_layout.setContentsMargins(
            4,
            4,
            8,
            4,
        )

        content_layout.setSpacing(
            8
        )

        # ----------------------------------------------------------
        # PARENT TABLE
        # ----------------------------------------------------------

        parent_group = QGroupBox(
            self.tr(
                "Tabella padre"
            )
        )

        parent_layout = QVBoxLayout(
            parent_group
        )

        parent_layer_layout = QHBoxLayout()

        parent_layer_layout.addWidget(
            QLabel(
                self.tr("Layer")
            )
        )

        self.layer1Combo = QComboBox()

        parent_layer_layout.addWidget(
            self.layer1Combo,
            1,
        )

        parent_layout.addLayout(
            parent_layer_layout
        )

        parent_field_layout = QHBoxLayout()

        parent_field_layout.addWidget(
            QLabel(
                self.tr("Campo chiave")
            )
        )

        self.field1Combo = QComboBox()

        parent_field_layout.addWidget(
            self.field1Combo,
            1,
        )

        parent_layout.addLayout(
            parent_field_layout
        )

        content_layout.addWidget(
            parent_group
        )

        # ----------------------------------------------------------
        # CHILD TABLE
        # ----------------------------------------------------------

        child_group = QGroupBox(
            self.tr(
                "Tabella figlio"
            )
        )

        child_layout = QVBoxLayout(
            child_group
        )

        child_layer_layout = QHBoxLayout()

        child_layer_layout.addWidget(
            QLabel(
                self.tr("Layer")
            )
        )

        self.layer2Combo = QComboBox()

        child_layer_layout.addWidget(
            self.layer2Combo,
            1,
        )

        child_layout.addLayout(
            child_layer_layout
        )

        child_field_layout = QHBoxLayout()

        child_field_layout.addWidget(
            QLabel(
                self.tr("Campo esterno")
            )
        )

        self.field2Combo = QComboBox()

        child_field_layout.addWidget(
            self.field2Combo,
            1,
        )

        child_layout.addLayout(
            child_field_layout
        )

        content_layout.addWidget(
            child_group
        )

        # ----------------------------------------------------------
        # RELATION TYPE
        # ----------------------------------------------------------

        relation_group = QGroupBox(
            self.tr(
                "Tipo di relazione"
            )
        )

        relation_layout = QHBoxLayout(
            relation_group
        )

        relation_layout.addWidget(
            QLabel(
                self.tr(
                    "Cardinalità"
                )
            )
        )

        self.relationTypeCombo = QComboBox()

        self.relationTypeCombo.addItem(
            self.tr(
                "uno-a-uno"
            ),
            "one_to_one",
        )

        self.relationTypeCombo.addItem(
            self.tr(
                "uno-a-molti"
            ),
            "one_to_many",
        )

        self.relationTypeCombo.addItem(
            self.tr(
                "molti-a-molti"
            ),
            "many_to_many",
        )

        relation_layout.addWidget(
            self.relationTypeCombo,
            1,
        )

        content_layout.addWidget(
            relation_group
        )

        # ----------------------------------------------------------
        # INFORMATION
        # ----------------------------------------------------------

        info_group = QGroupBox(
            self.tr(
                "Informazioni sulla relazione"
            )
        )

        info_layout = QVBoxLayout(
            info_group
        )

        self.relationStatusLabel = QLabel()

        self.relationStatusLabel.setStyleSheet(
            """
            QLabel {
                font-weight: bold;
                font-size: 14px;
                padding: 4px;
            }
            """
        )

        info_layout.addWidget(
            self.relationStatusLabel
        )

        self.relationInfoTextEdit = QTextEdit()

        self.relationInfoTextEdit.setReadOnly(
            True
        )

        self.relationInfoTextEdit.setMinimumHeight(
            130
        )

        self.relationInfoTextEdit.setMaximumHeight(
            220
        )

        info_layout.addWidget(
            self.relationInfoTextEdit
        )

        content_layout.addWidget(
            info_group
        )

        # ----------------------------------------------------------
        # N:M OPTIONS
        # ----------------------------------------------------------

        self.manyToManyGroupBox = QGroupBox(
            self.tr(
                "Opzioni tabella ponte N:M"
            )
        )

        nm_layout = QVBoxLayout(
            self.manyToManyGroupBox
        )

        bridge_name_layout = QHBoxLayout()

        bridge_name_layout.addWidget(
            QLabel(
                self.tr(
                    "Nome tabella ponte"
                )
            )
        )

        self.ponteTableNameLineEdit = QLineEdit()

        self.ponteTableNameLineEdit.setPlaceholderText(
            self.tr(
                "es. comuni_servizi_bridge"
            )
        )

        bridge_name_layout.addWidget(
            self.ponteTableNameLineEdit,
            1,
        )

        nm_layout.addLayout(
            bridge_name_layout
        )

        self.prefillBridgeCheckBox = QCheckBox(
            self.tr(
                "Precompila tutte le combinazioni possibili"
            )
        )

        nm_layout.addWidget(
            self.prefillBridgeCheckBox
        )

        nm_warning = QLabel(
            self.tr(
                "Attenzione: con molti valori questa opzione "
                "può generare migliaia o milioni di record."
            )
        )

        nm_warning.setWordWrap(
            True
        )

        nm_warning.setStyleSheet(
            """
            QLabel {
                color: #a05a00;
                padding: 3px;
            }
            """
        )

        nm_layout.addWidget(
            nm_warning
        )

        content_layout.addWidget(
            self.manyToManyGroupBox
        )

        # ----------------------------------------------------------
        # SAVE OPTIONS
        # ----------------------------------------------------------

        options_group = QGroupBox(
            self.tr(
                "Opzioni"
            )
        )

        options_layout = QVBoxLayout(
            options_group
        )

        self.saveToDiskCheckBox = QCheckBox(
            self.tr(
                "Salva tabella ponte su disco"
            )
        )

        options_layout.addWidget(
            self.saveToDiskCheckBox
        )

        content_layout.addWidget(
            options_group
        )

        # ----------------------------------------------------------
        # TOOLS
        # ----------------------------------------------------------
        
        tools_group = QGroupBox(
            self.tr(
                "Strumenti"
            )
        )
        
        tools_layout = QHBoxLayout(
            tools_group
        )
        
        self.openTableButton = QPushButton(
            icon("open_table.svg"),
            self.tr(
                "Apri tabella attributi"
            ),
        )
        
        self.showRelationsButton = QPushButton(
            icon("relations.svg"),
            self.tr(
                "Relazioni del progetto"
            ),
        )
        
        self.projectPropertiesButton = QPushButton(
            icon("properties.svg"),
            self.tr(
                "Proprietà progetto"
            ),
        )
        
        self.showJoinsButton = QPushButton(
            icon("joins.svg"),
            self.tr(
                "Visualizza join"
            ),
        )
        
        tools_layout.addWidget(
            self.openTableButton
        )
        
        tools_layout.addWidget(
            self.showRelationsButton
        )
        
        tools_layout.addWidget(
            self.projectPropertiesButton
        )
        
        tools_layout.addWidget(
            self.showJoinsButton
        )
        
        main_layout.addWidget(
            tools_group
        )

        # ----------------------------------------------------------
        # LOG
        # ----------------------------------------------------------

        log_group = QGroupBox(
            self.tr(
                "Log di elaborazione"
            )
        )

        log_layout = QVBoxLayout(
            log_group
        )

        self.processLogTextEdit = QTextEdit()

        self.processLogTextEdit.setReadOnly(
            True
        )

        self.processLogTextEdit.setMinimumHeight(
            150
        )

        self.processLogTextEdit.setMaximumHeight(
            240
        )

        log_layout.addWidget(
            self.processLogTextEdit
        )

        # ----------------------------------------------------------
        # LOG BUTTONS
        # ----------------------------------------------------------

        log_buttons_layout = QHBoxLayout()

        log_buttons_layout.addStretch()

        self.clearLogButton = QPushButton(
            icon("clear_log.svg"),
            self.tr(
                "Cancella log"
            ),
        )

        self.clearLogButton.setMinimumWidth(
            110
        )

        log_buttons_layout.addWidget(
            self.clearLogButton
        )

        log_layout.addLayout(
            log_buttons_layout
        )

        content_layout.addWidget(
            log_group
        )

        # ----------------------------------------------------------
        # STRETCH
        # ----------------------------------------------------------

        content_layout.addStretch()

        # ----------------------------------------------------------
        # SET SCROLL WIDGET
        # ----------------------------------------------------------

        scroll_area.setWidget(
            content_widget
        )

        main_layout.addWidget(
            scroll_area,
            1,
        )

        # ----------------------------------------------------------
        # PROGRESS BAR
        # ----------------------------------------------------------

        progress_group = QGroupBox(
            self.tr(
                "Avanzamento"
            )
        )

        progress_layout = QHBoxLayout(
            progress_group
        )

        self.progressBar = QProgressBar()

        self.progressBar.setRange(
            0,
            100,
        )

        self.progressBar.setValue(
            0
        )

        self.progressBar.setTextVisible(
            True
        )

        progress_layout.addWidget(
            self.progressBar
        )

        main_layout.addWidget(
            progress_group
        )

        # ----------------------------------------------------------
        # MAIN BUTTONS
        # ----------------------------------------------------------

        buttons_layout = QHBoxLayout()

        self.createRelationButton = QPushButton(
            icon("create_relation.svg"),
            self.tr(
                "Crea relazione"
            ),
        )

        self.createRelationButton.setDefault(
            True
        )

        self.createRelationButton.setMinimumWidth(
            140
        )

        self.closeButton = QPushButton(
            icon("close.svg"),
            self.tr(
                "Chiudi"
            ),
        )

        self.closeButton.setMinimumWidth(
            100
        )

        buttons_layout.addStretch()

        buttons_layout.addWidget(
            self.createRelationButton
        )

        buttons_layout.addWidget(
            self.closeButton
        )

        main_layout.addLayout(
            buttons_layout
        )

        # ----------------------------------------------------------
        # INITIAL STATE
        # ----------------------------------------------------------

        self.manyToManyGroupBox.setVisible(
            False
        )

        self.relationStatusLabel.setText(
            self.tr(
                "Selezionare una relazione"
            )
        )
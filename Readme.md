# Create Relation (Crea Relazioni)

**Create and manage one-to-one, one-to-many and many-to-many relationships between vector layer attribute tables, directly from a QGIS panel.**

> Crea e gestisce relazioni uno-a-uno, uno-a-molti e molti-a-molti tra le tabelle degli attributi di layer vettoriali, direttamente da un pannello di QGIS.

Version / Versione: **1.0** — QGIS 3.28+ and QGIS 4.x (Qt6) / QGIS 3.28+ e QGIS 4.x (Qt6)

---

## Features (Funzionalità)

- One-to-one (1:1), one-to-many (1:N) and many-to-many (N:M) relation creation.
- For N:M relations, an intermediate **bridge table** is generated automatically, with the two foreign keys and both QGIS relations (parent → bridge, child → bridge) registered for you.
- Optional prefill of the bridge table with every possible parent/child combination, with a warning before generating large numbers of records.
- Optional export of the bridge table to **GeoPackage**, **GeoJSON** or **Shapefile**, with automatic reload of the saved layer into the project.
- Built-in tools: open the attribute table of the selected layer, inspect and delete project relations, open project properties, inspect and remove layer joins.
- Detailed, timestamped processing log and progress bar.
- Full English translation alongside the Italian source strings (see [Translations](#translations-traduzioni) below).

> - Creazione di relazioni uno-a-uno (1:1), uno-a-molti (1:N) e molti-a-molti (N:M).
> - Per le relazioni N:M viene generata automaticamente una **tabella ponte** intermedia, con le due chiavi esterne, e vengono registrate entrambe le relazioni QGIS (padre → ponte, figlio → ponte).
> - Precompilazione opzionale della tabella ponte con tutte le combinazioni possibili padre/figlio, con avviso preventivo in caso di un numero elevato di record.
> - Esportazione opzionale della tabella ponte in **GeoPackage**, **GeoJSON** o **Shapefile**, con ricaricamento automatico del layer salvato nel progetto.
> - Strumenti integrati: apertura della tabella attributi del layer selezionato, ispezione ed eliminazione delle relazioni di progetto, apertura delle proprietà del progetto, ispezione e rimozione dei join di un layer.
> - Log di elaborazione dettagliato con timestamp e barra di avanzamento.
> - Traduzione inglese completa, accanto alle stringhe sorgente in italiano (vedi [Traduzioni](#translations-traduzioni)).

---

## Requirements (Requisiti)

- QGIS **3.28** or later, including QGIS **4.x** built on Qt6.
- No external Python dependencies: the plugin only uses PyQGIS and PyQt.

> - QGIS **3.28** o superiore, incluso QGIS **4.x** basato su Qt6.
> - Nessuna dipendenza Python esterna: il plugin utilizza solo PyQGIS e PyQt.

---

## Installation (Installazione)

1. Download the `create_relation.zip` archive (or clone this repository).
2. In QGIS, go to **Plugins → Manage and Install Plugins → Install from ZIP**, and select the archive — or copy the `create_relation` folder into your QGIS plugins directory:
   - Windows: `C:\Users\<user>\AppData\Roaming\QGIS\QGIS3\profiles\<profile>\python\plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/<profile>/python/plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/<profile>/python/plugins`
3. Enable **Create Relation** from the QGIS Plugin Manager.
4. The plugin adds a toolbar icon and a **Create Relation** entry under the Plugins menu.

> 1. Scaricare l'archivio `create_relation.zip` (oppure clonare questo repository).
> 2. In QGIS, andare su **Plugin → Gestisci e installa plugin → Installa da ZIP** e selezionare l'archivio — oppure copiare la cartella `create_relation` nella cartella dei plugin di QGIS:
>    - Windows: `C:\Users\<utente>\AppData\Roaming\QGIS\QGIS3\profiles\<profilo>\python\plugins`
>    - Linux: `~/.local/share/QGIS/QGIS3/profiles/<profilo>/python/plugins`
>    - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/<profilo>/python/plugins`
> 3. Abilitare **Create Relation** dal Gestore plugin di QGIS.
> 4. Il plugin aggiunge un'icona sulla barra degli strumenti e una voce **Create Relation** nel menu Plugin.

---

## Usage (Utilizzo)

Load at least two vector layers with attribute tables into the project. In the dialog:

1. Choose the **parent table** (layer and key field) and the **child table** (layer and foreign field).
2. Choose the relation **type**: one-to-one, one-to-many or many-to-many. The information panel explains the selected type and previews the structure that will be created.
3. For a many-to-many relation, the **N:M bridge table options** panel appears:
   - optionally set a custom name for the bridge table (default: `<parent>_<child>_bridge`);
   - optionally tick **prefill with every possible combination** — a confirmation is requested if this would generate a large number of records;
   - optionally tick **save bridge table to disk**, choosing GeoPackage, GeoJSON or Shapefile.
4. Click **Create relation**. Progress and outcome are reported in the processing log.
5. Use the **Tools** row at any time to open the attribute table of the currently selected layer, inspect/delete the project's relations, open the project properties, or inspect/remove a layer's joins.

> Caricare nel progetto almeno due layer vettoriali con tabelle degli attributi. Nella finestra del plugin:
>
> 1. Scegliere la **tabella padre** (layer e campo chiave) e la **tabella figlio** (layer e campo esterno).
> 2. Scegliere il **tipo** di relazione: uno-a-uno, uno-a-molti o molti-a-molti. Il pannello informativo spiega il tipo selezionato e anticipa la struttura che verrà creata.
> 3. Per una relazione molti-a-molti compare il pannello **Opzioni tabella ponte N:M**:
>    - è possibile impostare un nome personalizzato per la tabella ponte (predefinito: `<padre>_<figlio>_bridge`);
>    - è possibile spuntare **precompila tutte le combinazioni possibili** — viene richiesta conferma se ciò generasse un numero elevato di record;
>    - è possibile spuntare **salva tabella ponte su disco**, scegliendo GeoPackage, GeoJSON o Shapefile.
> 4. Fare clic su **Crea relazione**. L'avanzamento e l'esito vengono riportati nel log di elaborazione.
> 5. In qualsiasi momento è possibile usare la riga **Strumenti** per aprire la tabella attributi del layer selezionato, ispezionare/eliminare le relazioni del progetto, aprire le proprietà del progetto, oppure ispezionare/rimuovere i join di un layer.

### Viewing relations afterwards (Visualizzare le relazioni in seguito)

- **1:N and N:M relations**: Project menu → Project Properties → Relations tab, or the **Relazioni del progetto** tool inside the plugin, which also allows deleting a relation.
- **Joins** (e.g. created outside the plugin): layer Properties → Joins tab, or the **Visualizza join** tool inside the plugin.

> - **Relazioni 1:N e N:M**: menu Progetto → Proprietà del progetto → scheda Relazioni, oppure lo strumento **Relazioni del progetto** interno al plugin, che consente anche di eliminare una relazione.
> - **Join** (ad es. creati al di fuori del plugin): Proprietà del layer → scheda Join, oppure lo strumento **Visualizza join** interno al plugin.

---

## Changelog

**1.0**
- Fixed a bug where creating or deleting a relation (including the parent → bridge table leg of an N:M relation) could report a false "QGIS non ha accettato/potuto eliminare la relazione" error even though the operation actually succeeded. Success is now verified by re-querying the relation manager instead of trusting the return value of `addRelation()`/`removeRelation()`.
- Bridge table fields are now built with a Qt6/QMetaType-aware helper, with a fallback for QGIS 3.28–3.3x (Qt5).
- Added SVG icons to every button.
- Added the full English translation and the `i18n/` translation project described above.
- Complete redesign of the plugin interface, robust N:M bridge table creation with optional prefill and export, project relation and join inspection tools, processing log and progress bar.

> **1.0**
> - Corretto un bug per cui la creazione o l'eliminazione di una relazione (compreso il ramo padre → tabella ponte di una relazione N:M) poteva segnalare un falso errore "QGIS non ha accettato/potuto eliminare la relazione" anche quando l'operazione era in realtà riuscita. L'esito viene ora verificato interrogando di nuovo il relation manager, invece di fidarsi del valore restituito da `addRelation()`/`removeRelation()`.
> - I campi della tabella ponte vengono ora creati con un helper compatibile Qt6/QMetaType, con fallback per QGIS 3.28–3.3x (Qt5).
> - Aggiunte icone SVG a tutti i pulsanti.
> - Aggiunta la traduzione inglese completa e il progetto di traduzione `i18n/` descritto sopra.
> - Redesign completo dell'interfaccia del plugin, creazione robusta della tabella ponte N:M con precompilazione ed esportazione opzionali, strumenti di ispezione delle relazioni di progetto e dei join, log di elaborazione e barra di avanzamento.

---

## License (Licenza)

See [LICENSE](LICENSE) / [LICENSE.md](LICENSE.md).

## Author (Autore)

dr. Geol. Faustino Cetraro

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="en_US">
<context>
    <name>CreateRelationDialog</name>
    <message>
        <source>&amp;Create Relation</source>
        <translation>&amp;Create Relation</translation>
    </message>
    <message>
        <source>Create Relation</source>
        <translation>Create Relation</translation>
    </message>
    <message>
        <source>Create and manage layer relations</source>
        <translation>Create and manage layer relations</translation>
    </message>
    <message>
        <source>Layer padre</source>
        <translation>Parent layer</translation>
    </message>
    <message>
        <source>Layer figlio</source>
        <translation>Child Layer</translation>
    </message>
    <message>
        <source>Relazione uno-a-uno (1:1)</source>
        <translation>One-to-one relationship (1:1)</translation>
    </message>
    <message>
        <source>&lt;b&gt;1:1 — Uno a uno&lt;/b&gt;&lt;br&gt;Ogni record del layer padre può essere collegato ad un solo record del layer figlio e ogni record del figlio può riferirsi ad un solo record del padre.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; una particella catastale e la relativa scheda descrittiva.&lt;br&gt;Il campo del layer figlio viene utilizzato come chiave esterna verso il campo del layer padre.</source>
        <translation>&lt;b&gt;1:1 — One to one&lt;/b&gt;&lt;br&gt;Each record in the parent layer can be linked to only one record in the child layer, and each record in the child can refer to only one record in the parent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; a land registry parcel and its description sheet.&lt;br&gt;The field in the child layer is used as a foreign key to the field in the parent layer.</translation>
    </message>
    <message>
        <source>Relazione molti-a-molti (N:M)</source>
        <translation>Many-to-many (N:M) relationship</translation>
    </message>
    <message>
        <source>&lt;b&gt;N:M — Molti a molti&lt;/b&gt;&lt;br&gt;Un record del layer padre può essere associato a molti record del layer figlio e viceversa.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; un Comune può avere molti servizi e lo stesso servizio può essere presente in molti Comuni.&lt;br&gt;Il plugin crea automaticamente una &lt;b&gt;tabella ponte&lt;/b&gt; contenente le due chiavi esterne e registra due relazioni QGIS:&lt;br&gt;• padre → tabella ponte&lt;br&gt;• figlio → tabella ponte</source>
        <translation>&lt;b&gt;N:M — Many to Many&lt;/b&gt;&lt;br&gt;A record in the parent layer can be associated with many records in the child layer and vice versa.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; a municipality can have many services and the same service can be present in many municipalities.&lt;br&gt;The plugin automatically creates a &lt;b&gt;bridge table&lt;/b&gt; containing the two foreign keys and records two QGIS relations:&lt;br&gt;• parent → bridge table&lt;br&gt;• child → bridge table</translation>
    </message>
    <message>
        <source>&lt;br&gt;&lt;font color=&apos;#b36b00&apos;&gt;&lt;b&gt;Precompilazione attiva:&lt;/b&gt; verranno create tutte le combinazioni possibili tra i valori distinti dei due campi.&lt;/font&gt;</source>
        <translation>&lt;br&gt;&lt;font color=&apos;#b36b00&apos;&gt;&lt;b&gt;Prefill active:&lt;/b&gt; All possible combinations between the distinct values ​​of the two fields will be created.&lt;/font&gt;</translation>
    </message>
    <message>
        <source>Relazione uno-a-molti (1:N)</source>
        <translation>One-to-many relationship (1:N)</translation>
    </message>
    <message>
        <source>&lt;b&gt;1:N — Uno a molti&lt;/b&gt;&lt;br&gt;Un record del layer padre può essere associato a più record del layer figlio, mentre ogni record figlio appartiene ad un solo padre.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; un Comune può avere molti Edifici, mentre ogni Edificio appartiene ad un solo Comune.</source>
        <translation>&lt;b&gt;1:N — One to Many&lt;/b&gt;&lt;br&gt;A record in the parent layer can be associated with multiple records in the child layer, while each child record belongs to only one parent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; a Municipality can have many Buildings, while each Building belongs to only one Municipality.</translation>
    </message>
    <message>
        <source>&lt;br&gt;&lt;br&gt;&lt;b&gt;Struttura selezionata:&lt;/b&gt; {0} → {1}</source>
        <translation>&lt;br&gt;&lt;br&gt;&lt;b&gt;Selected structure:&lt;/b&gt; {0} → {1}</translation>
    </message>
    <message>
        <source>Selezionare entrambi i layer.</source>
        <translation>Select both layers.</translation>
    </message>
    <message>
        <source>Il layer padre e il layer figlio non possono coincidere.</source>
        <translation>The parent layer and child layer cannot match.</translation>
    </message>
    <message>
        <source>Selezionare entrambi i campi.</source>
        <translation>Select both fields.</translation>
    </message>
    <message>
        <source>Il campo del layer padre non esiste.</source>
        <translation>The parent layer field does not exist.</translation>
    </message>
    <message>
        <source>Il campo del layer figlio non esiste.</source>
        <translation>The child layer field does not exist.</translation>
    </message>
    <message>
        <source>Avvio creazione della relazione.</source>
        <translation>Start creating the relationship.</translation>
    </message>
    <message>
        <source>Layer padre: {0}</source>
        <translation>Parent layer: {0}</translation>
    </message>
    <message>
        <source>Campo padre: {0}</source>
        <translation>Parent field: {0}</translation>
    </message>
    <message>
        <source>Layer figlio: {0}</source>
        <translation>Child layer: {0}</translation>
    </message>
    <message>
        <source>Campo figlio: {0}</source>
        <translation>Child field: {0}</translation>
    </message>
    <message>
        <source>Tipi di campo differenti</source>
        <translation>Different field types</translation>
    </message>
    <message>
        <source>I due campi non hanno lo stesso tipo di dato. Vuoi procedere comunque?</source>
        <translation>The two fields don&apos;t have the same data type. Do you want to proceed anyway?</translation>
    </message>
    <message>
        <source>Operazione annullata per incompatibilità dei campi.</source>
        <translation>Operation cancelled due to incompatible fields.</translation>
    </message>
    <message>
        <source>Operazione completata con successo.</source>
        <translation>Operation completed successfully.</translation>
    </message>
    <message>
        <source>Errore: {0}</source>
        <translation>Error: {0}</translation>
    </message>
    <message>
        <source>Errore</source>
        <translation>Error</translation>
    </message>
    <message>
        <source>Relazione non valida: {0}</source>
        <translation>Invalid relationship: {0}</translation>
    </message>
    <message>
        <source>Creazione relazione 1:1.</source>
        <translation>Creating 1:1 relationships.</translation>
    </message>
    <message>
        <source>La relazione è già presente: {0}</source>
        <translation>The relationship already exists: {0}</translation>
    </message>
    <message>
        <source>{0} → {1} (1:1)</source>
        <translation></translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione 1:1.</source>
        <translation>QGIS did not accept the 1:1 relationship.</translation>
    </message>
    <message>
        <source>Relazione 1:1 registrata nel progetto.</source>
        <translation>1:1 relationship recorded in the project.</translation>
    </message>
    <message>
        <source>Il campo padre contiene {0} valori duplicati.</source>
        <translation>The parent field contains {0} duplicate values.</translation>
    </message>
    <message>
        <source>Il campo figlio contiene {0} valori duplicati.</source>
        <translation>The child field contains {0} duplicate values.</translation>
    </message>
    <message>
        <source>Chiavi non univoche</source>
        <translation>Non-unique keys</translation>
    </message>
    <message>
        <source>Per una relazione 1:1 i valori delle chiavi dovrebbero essere univoci.\n\nSono stati trovati duplicati. Vuoi continuare?</source>
        <translation>For a 1:1 relationship, key values ​​must be unique.\n\nDuplicates were found. Do you want to continue?</translation>
    </message>
    <message>
        <source>Creazione della relazione 1:1 annullata.</source>
        <translation>1:1 relationship creation canceled.</translation>
    </message>
    <message>
        <source>Creazione relazione 1:N.</source>
        <translation>Creating a 1:N relationship.</translation>
    </message>
    <message>
        <source>La relazione 1:N è già presente: {0}</source>
        <translation>The 1:N relationship already exists: {0}</translation>
    </message>
    <message>
        <source>{0} → {1} (1:N)</source>
        <translation></translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione 1:N.</source>
        <translation>QGIS did not accept the 1:N relationship.</translation>
    </message>
    <message>
        <source>Relazione 1:N registrata nel progetto.</source>
        <translation>1:N relationship recorded in the project.</translation>
    </message>
    <message>
        <source>Creazione struttura molti-a-molti.</source>
        <translation>Creating a many-to-many structure.</translation>
    </message>
    <message>
        <source>Nome tabella ponte: {0}</source>
        <translation>Bridge table name: {0}</translation>
    </message>
    <message>
        <source>La tabella ponte non è valida.</source>
        <translation>The bridge table is invalid.</translation>
    </message>
    <message>
        <source>La tabella ponte non è disponibile dopo il salvataggio.</source>
        <translation>The bridge table is not available after saving.</translation>
    </message>
    <message>
        <source>Tabella ponte disponibile nel progetto: {0}</source>
        <translation>Bridge table available in the project: {0}</translation>
    </message>
    <message>
        <source>Il campo ponte padre &apos;{0}&apos; non esiste.</source>
        <translation>The parent bridge field &apos;{0}&apos; does not exist.</translation>
    </message>
    <message>
        <source>Il campo ponte figlio &apos;{0}&apos; non esiste.</source>
        <translation>The child bridge field &apos;{0}&apos; does not exist.</translation>
    </message>
    <message>
        <source>Due relazioni N:M preparate.</source>
        <translation>Two N:M reports prepared.</translation>
    </message>
    <message>
        <source>Relazione padre → tabella ponte registrata.</source>
        <translation>Parent relationship → registered bridge table.</translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione padre → tabella ponte.\n\nID: {0}\nCampo ponte: {1}\nCampo padre: {2}</source>
        <translation>QGIS did not accept the parent → bridge table relationship.\n\nID: {0}\nBridge field: {1}\nParent field: {2}</translation>
    </message>
    <message>
        <source>Relazione figlio → tabella ponte registrata.</source>
        <translation>Child relation → registered bridge table.</translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione figlio → tabella ponte.\n\nLa prima relazione è stata annullata.\n\nID: {0}\nCampo ponte: {1}\nCampo figlio: {2}</source>
        <translation>QGIS did not accept the child → bridge table relation.\n\nThe first relation has been cancelled.\n\nID: {0}\nBridge field: {1}\nChild field: {2}</translation>
    </message>
    <message>
        <source>La relazione padre → tabella ponte risulta non valida dopo la registrazione.</source>
        <translation>The parent → bridge table relationship is invalid after registration.</translation>
    </message>
    <message>
        <source>La relazione figlio → tabella ponte risulta non valida dopo la registrazione.</source>
        <translation>Child → bridge table relationship is invalid after registration.</translation>
    </message>
    <message>
        <source>Entrambe le relazioni N:M sono state registrate correttamente.</source>
        <translation>Both N:M relationships were recorded successfully.</translation>
    </message>
    <message>
        <source>Tabella ponte: {0}</source>
        <translation>Bridge Table: {0}</translation>
    </message>
    <message>
        <source>Campo ponte padre: {0}</source>
        <translation>Parent bridge field: {0}</translation>
    </message>
    <message>
        <source>Campo ponte figlio: {0}</source>
        <translation>Child bridge field: {0}</translation>
    </message>
    <message>
        <source>Relazione N:M creata</source>
        <translation>N:M relationship created</translation>
    </message>
    <message>
        <source>La struttura molti-a-molti è stata creata correttamente.\n\nTabella ponte:\n{0}\n\nSono state registrate entrambe le relazioni QGIS:\n\n• {1} → tabella ponte\n• {2} → tabella ponte</source>
        <translation>The many-to-many structure was created successfully.\n\nBridge table:\n{0}\n\nBoth QGIS relations were registered:\n\n• {1} → bridge table\n• {2} → bridge table</translation>
    </message>
    <message>
        <source>Il layer referenziato non è valido.</source>
        <translation>The referenced layer is invalid.</translation>
    </message>
    <message>
        <source>Il campo &apos;{0}&apos; non esiste nella tabella ponte.</source>
        <translation>The field &apos;{0}&apos; does not exist in the bridge table.</translation>
    </message>
    <message>
        <source>Il campo &apos;{0}&apos; non esiste nel layer &apos;{1}&apos;.</source>
        <translation>The field &apos;{0}&apos; does not exist in layer &apos;{1}&apos;.</translation>
    </message>
    <message>
        <source>Tipi incompatibili per la relazione N:M &apos;{0}&apos;: {1} → {2}.</source>
        <translation>Incompatible types for N:M relation &apos;{0}&apos;: {1} → {2}.</translation>
    </message>
    <message>
        <source>{0} → {1} (N:M)</source>
        <translation></translation>
    </message>
    <message>
        <source>Esiste già una relazione tra la tabella ponte &apos;{0}&apos; e il layer &apos;{1}&apos; per i campi &apos;{2}&apos; → &apos;{3}&apos;.</source>
        <translation>There is already a relationship between the bridge table &apos;{0}&apos; and the layer &apos;{1}&apos; for the fields &apos;{2}&apos; → &apos;{3}&apos;.</translation>
    </message>
    <message>
        <source>Relazione N:M &apos;{0}&apos; non valida: {1}</source>
        <translation>Invalid N:M relation &apos;{0}&apos;: {1}</translation>
    </message>
    <message>
        <source>Impossibile creare la tabella ponte.</source>
        <translation>Unable to create bridge table.</translation>
    </message>
    <message>
        <source>Impossibile creare i campi della tabella ponte.</source>
        <translation>Unable to create bridge table fields.</translation>
    </message>
    <message>
        <source>Precompilazione N:M: {0} valori padre × {1} valori figlio = {2} combinazioni.</source>
        <translation>N:M Prefill: {0} parent values ​​× {1} child values ​​= {2} combinations.</translation>
    </message>
    <message>
        <source>Nessuna combinazione da creare.</source>
        <translation>No combinations to create.</translation>
    </message>
    <message>
        <source>Numero elevato di combinazioni</source>
        <translation>High number of combinations</translation>
    </message>
    <message>
        <source>La precompilazione genererebbe {0} record.\n\nQuesta operazione può richiedere molta memoria e molto tempo.\n\nVuoi continuare?</source>
        <translation>Prefilling would generate {0} records.\n\nThis operation can be memory-intensive and time-consuming.\n\nDo you want to continue?</translation>
    </message>
    <message>
        <source>Precompilazione annullata dall&apos;utente.</source>
        <translation>Prefill cancelled by user.</translation>
    </message>
    <message>
        <source>Errore durante la precompilazione della tabella ponte.</source>
        <translation>Error pre-populating the bridge table.</translation>
    </message>
    <message>
        <source>Errore durante l&apos;inserimento dei record finali.</source>
        <translation>Error inserting final records.</translation>
    </message>
    <message>
        <source>Precompilazione completata: {0} record.</source>
        <translation>Pre-population completed: {0} record.</translation>
    </message>
    <message>
        <source>Salva tabella ponte</source>
        <translation>Save bridge table</translation>
    </message>
    <message>
        <source>GeoPackage (*.gpkg);;GeoJSON (*.geojson);;Shapefile (*.shp)</source>
        <translation></translation>
    </message>
    <message>
        <source>Salvataggio su disco annullato. La tabella ponte rimane temporanea.</source>
        <translation>Save to disk canceled. The bridge table remains temporary.</translation>
    </message>
    <message>
        <source>Errore nel salvataggio della tabella ponte: {0}</source>
        <translation>Error saving bridge table: {0}</translation>
    </message>
    <message>
        <source>Tabella ponte salvata su disco: {0}</source>
        <translation>Bridge table saved to disk: {0}</translation>
    </message>
    <message>
        <source>La tabella ponte salvata non può essere ricaricata.</source>
        <translation>The saved bridge table cannot be reloaded.</translation>
    </message>
    <message>
        <source>Tabella ponte ricaricata dal file salvato.</source>
        <translation>Bridge table reloaded from saved file.</translation>
    </message>
    <message>
        <source>Layer non selezionato</source>
        <translation>Layer not selected</translation>
    </message>
    <message>
        <source>Selezionare un layer padre o figlio.</source>
        <translation>Select a parent or child layer.</translation>
    </message>
    <message>
        <source>Apertura tabella attributi: {0}</source>
        <translation>Opening attribute table: {0}</translation>
    </message>
    <message>
        <source>Tabella attributi aperta: {0}</source>
        <translation>Open attribute table: {0}</translation>
    </message>
    <message>
        <source>Impossibile aprire la tabella attributi: {0}</source>
        <translation>Unable to open attribute table: {0}</translation>
    </message>
    <message>
        <source>Impossibile aprire la tabella attributi.\n\n{0}</source>
        <translation>Unable to open attribute table.\n\n{0}</translation>
    </message>
    <message>
        <source>Proprietà del progetto aperte.</source>
        <translation>Open project properties.</translation>
    </message>
    <message>
        <source>Relazioni del progetto</source>
        <translation>Project relations</translation>
    </message>
    <message>
        <source>Elimina relazione</source>
        <translation>Delete relation</translation>
    </message>
    <message>
        <source>Chiudi</source>
        <translation>Close</translation>
    </message>
    <message>
        <source>Relazioni presenti: {0}</source>
        <translation>Current relations: {0}</translation>
    </message>
    <message>
        <source>Layer non disponibile</source>
        <translation>Layer not available</translation>
    </message>
    <message>
        <source>Relazione non disponibile</source>
        <translation>Relation not available</translation>
    </message>
    <message>
        <source>La relazione selezionata non è più disponibile.</source>
        <translation>The selected relation is no longer available.</translation>
    </message>
    <message>
        <source>Conferma eliminazione</source>
        <translation>Confirm deletion</translation>
    </message>
    <message>
        <source>Vuoi eliminare la relazione &apos;{0}&apos;?\n\nLa relazione verrà rimossa dal progetto.\n\nI layer e i dati non verranno eliminati.</source>
        <translation>Do you want to delete the relation &apos;{0}&apos;?\n\nThe relation will be removed from the project.\n\nThe layers and data will not be deleted.</translation>
    </message>
    <message>
        <source>Relazione eliminata: {0}</source>
        <translation>Relation deleted: {0}</translation>
    </message>
    <message>
        <source>QGIS non ha potuto eliminare la relazione.</source>
        <translation>QGIS could not delete the relation.</translation>
    </message>
    <message>
        <source>Elenco delle relazioni del progetto visualizzato.</source>
        <translation>List of project relationships displayed.</translation>
    </message>
    <message>
        <source>Selezionare un layer.</source>
        <translation>Select a layer.</translation>
    </message>
    <message>
        <source>Join - {0}</source>
        <translation></translation>
    </message>
    <message>
        <source>Rimuovi join</source>
        <translation>Remove join</translation>
    </message>
    <message>
        <source>Join presenti: {0}</source>
        <translation>Joins present: {0}</translation>
    </message>
    <message>
        <source>Conferma rimozione</source>
        <translation>Confirm removal</translation>
    </message>
    <message>
        <source>Vuoi rimuovere questo join?\n\nLayer: {0}\nCampo destinazione: {1}\nCampo join: {2}\n\nVerrà rimosso solo il join. I layer e i dati originali non verranno eliminati.</source>
        <translation>Do you want to remove this join?\n\nLayer: {0}\nTarget field: {1}\nJoin field: {2}\n\nOnly the join will be removed. The original layers and data will not be deleted.</translation>
    </message>
    <message>
        <source>Join rimosso da {0}: {1}</source>
        <translation>Join removed from {0}: {1}</translation>
    </message>
    <message>
        <source>Elenco join visualizzato per {0}.</source>
        <translation>Join list displayed for {0}.</translation>
    </message>
    <message>
        <source>Tabella padre</source>
        <translation>Parent table</translation>
    </message>
    <message>
        <source>Layer</source>
        <translation>Layer</translation>
    </message>
    <message>
        <source>Campo chiave</source>
        <translation>Key field</translation>
    </message>
    <message>
        <source>Tabella figlio</source>
        <translation>Child table</translation>
    </message>
    <message>
        <source>Campo esterno</source>
        <translation>Outfield</translation>
    </message>
    <message>
        <source>Tipo di relazione</source>
        <translation>Type of relation</translation>
    </message>
    <message>
        <source>Cardinalità</source>
        <translation>Cardinality</translation>
    </message>
    <message>
        <source>uno-a-uno</source>
        <translation>one-on-one</translation>
    </message>
    <message>
        <source>uno-a-molti</source>
        <translation>one-to-many</translation>
    </message>
    <message>
        <source>molti-a-molti</source>
        <translation>many-to-many</translation>
    </message>
    <message>
        <source>Informazioni sulla relazione</source>
        <translation>Relation Information</translation>
    </message>
    <message>
        <source>Opzioni tabella ponte N:M</source>
        <translation>N:M bridge table options</translation>
    </message>
    <message>
        <source>Nome tabella ponte</source>
        <translation>Bridge table name</translation>
    </message>
    <message>
        <source>es. comuni_servizi_bridge</source>
        <translation>e.g. municipalities_services_bridge</translation>
    </message>
    <message>
        <source>Precompila tutte le combinazioni possibili</source>
        <translation>Pre-fill all possible combinations</translation>
    </message>
    <message>
        <source>Attenzione: con molti valori questa opzione può generare migliaia o milioni di record.</source>
        <translation>Warning: With many values, this option can generate thousands or millions of records.</translation>
    </message>
    <message>
        <source>Opzioni</source>
        <translation>Options</translation>
    </message>
    <message>
        <source>Salva tabella ponte su disco</source>
        <translation>Save bridge table to disk</translation>
    </message>
    <message>
        <source>Strumenti</source>
        <translation>Tools</translation>
    </message>
    <message>
        <source>Apri tabella attributi</source>
        <translation>Open attribute table</translation>
    </message>
    <message>
        <source>Proprietà progetto</source>
        <translation>Project Properties</translation>
    </message>
    <message>
        <source>Visualizza join</source>
        <translation>View join</translation>
    </message>
    <message>
        <source>Log di elaborazione</source>
        <translation>Processing log</translation>
    </message>
    <message>
        <source>Cancella log</source>
        <translation>Clear log</translation>
    </message>
    <message>
        <source>Avanzamento</source>
        <translation>Progress</translation>
    </message>
    <message>
        <source>Crea relazione</source>
        <translation>Create relation</translation>
    </message>
    <message>
        <source>Selezionare una relazione</source>
        <translation>Select a relation</translation>
    </message>
</context>
</TS>

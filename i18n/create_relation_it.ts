<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="it_IT">
<context>
    <name>CreateRelation</name>
    <message>
        <source>&amp;Create Relation</source>
        <translation>&amp;Crea relazione</translation>
    </message>
    <message>
        <source>Create Relation</source>
        <translation>Crea relazione</translation>
    </message>
    <message>
        <source>Create and manage layer relations</source>
        <translation>Creare e gestisci relazioni tra livelli</translation>
    </message>
    <message>
        <source>Layer padre</source>
        <translation>Layer padre</translation>
    </message>
    <message>
        <source>Layer figlio</source>
        <translation>Layer figlio</translation>
    </message>
    <message>
        <source>Relazione uno-a-uno (1:1)</source>
        <translation>Relazione uno-a-uno (1:1)</translation>
    </message>
    <message>
        <source>&lt;b&gt;1:1 — Uno a uno&lt;/b&gt;&lt;br&gt;Ogni record del layer padre può essere collegato ad un solo record del layer figlio e ogni record del figlio può riferirsi ad un solo record del padre.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; una particella catastale e la relativa scheda descrittiva.&lt;br&gt;Il campo del layer figlio viene utilizzato come chiave esterna verso il campo del layer padre.</source>
        <translation>&lt;b&gt;1:1 — Uno a uno&lt;/b&gt;&lt;br&gt;Ogni record del layer padre può essere collegato ad un solo record del layer figlio e ogni record del figlio può riferirsi ad un solo record del padre.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; una particella catastale e la relativa scheda descrittiva.&lt;br&gt;Il campo del layer figlio viene utilizzato come chiave esterna verso il campo del layer padre.</translation>
    </message>
    <message>
        <source>Relazione molti-a-molti (N:M)</source>
        <translation>Relazione molti-a-molti (N:M)</translation>
    </message>
    <message>
        <source>&lt;b&gt;N:M — Molti a molti&lt;/b&gt;&lt;br&gt;Un record del layer padre può essere associato a molti record del layer figlio e viceversa.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; un Comune può avere molti servizi e lo stesso servizio può essere presente in molti Comuni.&lt;br&gt;Il plugin crea automaticamente una &lt;b&gt;tabella ponte&lt;/b&gt; contenente le due chiavi esterne e registra due relazioni QGIS:&lt;br&gt;• padre → tabella ponte&lt;br&gt;• figlio → tabella ponte</source>
        <translation>&lt;b&gt;N:M — Molti a molti&lt;/b&gt;&lt;br&gt;Un record del layer padre può essere associato a molti record del layer figlio e viceversa.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; un Comune può avere molti servizi e lo stesso servizio può essere presente in molti Comuni.&lt;br&gt;Il plugin crea automaticamente una &lt;b&gt;tabella ponte&lt;/b&gt; contenente le due chiavi esterne e registra due relazioni QGIS:&lt;br&gt;• padre → tabella ponte&lt;br&gt;• figlio → tabella ponte</translation>
    </message>
    <message>
        <source>&lt;br&gt;&lt;font color=&apos;#b36b00&apos;&gt;&lt;b&gt;Precompilazione attiva:&lt;/b&gt; verranno create tutte le combinazioni possibili tra i valori distinti dei due campi.&lt;/font&gt;</source>
        <translation>&lt;br&gt;&lt;font color=&apos;#b36b00&apos;&gt;&lt;b&gt;Precompilazione attiva:&lt;/b&gt; verranno create tutte le combinazioni possibili tra i valori distinti dei due campi.&lt;/font&gt;</translation>
    </message>
    <message>
        <source>Relazione uno-a-molti (1:N)</source>
        <translation>Relazione uno-a-molti (1:N)</translation>
    </message>
    <message>
        <source>&lt;b&gt;1:N — Uno a molti&lt;/b&gt;&lt;br&gt;Un record del layer padre può essere associato a più record del layer figlio, mentre ogni record figlio appartiene ad un solo padre.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; un Comune può avere molti Edifici, mentre ogni Edificio appartiene ad un solo Comune.</source>
        <translation>&lt;b&gt;1:N — Uno a molti&lt;/b&gt;&lt;br&gt;Un record del layer padre può essere associato a più record del layer figlio, mentre ogni record figlio appartiene ad un solo padre.&lt;br&gt;&lt;br&gt;&lt;b&gt;Esempio:&lt;/b&gt; un Comune può avere molti Edifici, mentre ogni Edificio appartiene ad un solo Comune.</translation>
    </message>
    <message>
        <source>&lt;br&gt;&lt;br&gt;&lt;b&gt;Struttura selezionata:&lt;/b&gt; {0} → {1}</source>
        <translation>&lt;br&gt;&lt;br&gt;&lt;b&gt;Struttura selezionata:&lt;/b&gt; {0} → {1}</translation>
    </message>
    <message>
        <source>Selezionare entrambi i layer.</source>
        <translation>Selezionare entrambi i layer.</translation>
    </message>
    <message>
        <source>Il layer padre e il layer figlio non possono coincidere.</source>
        <translation>Il layer padre e il layer figlio non possono coincidere.</translation>
    </message>
    <message>
        <source>Selezionare entrambi i campi.</source>
        <translation>Selezionare entrambi i campi.</translation>
    </message>
    <message>
        <source>Il campo del layer padre non esiste.</source>
        <translation>Il campo del layer padre non esiste.</translation>
    </message>
    <message>
        <source>Il campo del layer figlio non esiste.</source>
        <translation>Il campo del layer figlio non esiste.</translation>
    </message>
    <message>
        <source>Avvio creazione della relazione.</source>
        <translation>Avvio creazione della relazione.</translation>
    </message>
    <message>
        <source>Layer padre: {0}</source>
        <translation>Layer padre: {0}</translation>
    </message>
    <message>
        <source>Campo padre: {0}</source>
        <translation>Campo padre: {0}</translation>
    </message>
    <message>
        <source>Layer figlio: {0}</source>
        <translation>Layer figlio: {0}</translation>
    </message>
    <message>
        <source>Campo figlio: {0}</source>
        <translation>Campo figlio: {0}</translation>
    </message>
    <message>
        <source>Tipi di campo differenti</source>
        <translation>Tipi di campo differenti</translation>
    </message>
    <message>
        <source>I due campi non hanno lo stesso tipo di dato. Vuoi procedere comunque?</source>
        <translation>I due campi non hanno lo stesso tipo di dato. Vuoi procedere comunque?</translation>
    </message>
    <message>
        <source>Operazione annullata per incompatibilità dei campi.</source>
        <translation>Operazione annullata per incompatibilità dei campi.</translation>
    </message>
    <message>
        <source>Operazione completata con successo.</source>
        <translation>Operazione completata con successo.</translation>
    </message>
    <message>
        <source>Errore: {0}</source>
        <translation>Errore: {0}</translation>
    </message>
    <message>
        <source>Errore</source>
        <translation>Errore</translation>
    </message>
    <message>
        <source>Relazione non valida: {0}</source>
        <translation>Relazione non valida: {0}</translation>
    </message>
    <message>
        <source>Creazione relazione 1:1.</source>
        <translation>Creazione relazione 1:1.</translation>
    </message>
    <message>
        <source>La relazione è già presente: {0}</source>
        <translation>La relazione è già presente: {0}</translation>
    </message>
    <message>
        <source>{0} → {1} (1:1)</source>
        <translation></translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione 1:1.</source>
        <translation>QGIS non ha accettato la relazione 1:1.</translation>
    </message>
    <message>
        <source>Relazione 1:1 registrata nel progetto.</source>
        <translation>Relazione 1:1 registrata nel progetto.</translation>
    </message>
    <message>
        <source>Il campo padre contiene {0} valori duplicati.</source>
        <translation>Il campo padre contiene {0} valori duplicati.</translation>
    </message>
    <message>
        <source>Il campo figlio contiene {0} valori duplicati.</source>
        <translation>Il campo figlio contiene {0} valori duplicati.</translation>
    </message>
    <message>
        <source>Chiavi non univoche</source>
        <translation>Chiavi non univoche</translation>
    </message>
    <message>
        <source>Per una relazione 1:1 i valori delle chiavi dovrebbero essere univoci.\n\nSono stati trovati duplicati. Vuoi continuare?</source>
        <translation>Per una relazione 1:1 i valori delle chiavi dovrebbero essere univoci.\n\nSono stati trovati duplicati. Vuoi continuare?</translation>
    </message>
    <message>
        <source>Creazione della relazione 1:1 annullata.</source>
        <translation>Creazione della relazione 1:1 annullata.</translation>
    </message>
    <message>
        <source>Creazione relazione 1:N.</source>
        <translation>Creazione relazione 1:N.</translation>
    </message>
    <message>
        <source>La relazione 1:N è già presente: {0}</source>
        <translation>La relazione 1:N è già presente: {0}</translation>
    </message>
    <message>
        <source>{0} → {1} (1:N)</source>
        <translation></translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione 1:N.</source>
        <translation>QGIS non ha accettato la relazione 1:N.</translation>
    </message>
    <message>
        <source>Relazione 1:N registrata nel progetto.</source>
        <translation>Relazione 1:N registrata nel progetto.</translation>
    </message>
    <message>
        <source>Creazione struttura molti-a-molti.</source>
        <translation>Creazione struttura molti-a-molti.</translation>
    </message>
    <message>
        <source>Nome tabella ponte: {0}</source>
        <translation>Nome tabella ponte: {0}</translation>
    </message>
    <message>
        <source>La tabella ponte non è valida.</source>
        <translation>La tabella ponte non è valida.</translation>
    </message>
    <message>
        <source>La tabella ponte non è disponibile dopo il salvataggio.</source>
        <translation>La tabella ponte non è disponibile dopo il salvataggio.</translation>
    </message>
    <message>
        <source>Tabella ponte disponibile nel progetto: {0}</source>
        <translation>Tabella ponte disponibile nel progetto: {0}</translation>
    </message>
    <message>
        <source>Il campo ponte padre &apos;{0}&apos; non esiste.</source>
        <translation>Il campo ponte padre &apos;{0}&apos; non esiste.</translation>
    </message>
    <message>
        <source>Il campo ponte figlio &apos;{0}&apos; non esiste.</source>
        <translation>Il campo ponte figlio &apos;{0}&apos; non esiste.</translation>
    </message>
    <message>
        <source>Due relazioni N:M preparate.</source>
        <translation>Due relazioni N:M preparate.</translation>
    </message>
    <message>
        <source>Relazione padre → tabella ponte registrata.</source>
        <translation>Relazione padre → tabella ponte registrata.</translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione padre → tabella ponte.\n\nID: {0}\nCampo ponte: {1}\nCampo padre: {2}</source>
        <translation>QGIS non ha accettato la relazione padre → tabella ponte.\n\nID: {0}\nCampo ponte: {1}\nCampo padre: {2}</translation>
    </message>
    <message>
        <source>Relazione figlio → tabella ponte registrata.</source>
        <translation>Relazione figlio → tabella ponte registrata.</translation>
    </message>
    <message>
        <source>QGIS non ha accettato la relazione figlio → tabella ponte.\n\nLa prima relazione è stata annullata.\n\nID: {0}\nCampo ponte: {1}\nCampo figlio: {2}</source>
        <translation>QGIS non ha accettato la relazione figlio → tabella ponte.\n\nLa prima relazione è stata annullata.\n\nID: {0}\nCampo ponte: {1}\nCampo figlio: {2}</translation>
    </message>
    <message>
        <source>La relazione padre → tabella ponte risulta non valida dopo la registrazione.</source>
        <translation>La relazione padre → tabella ponte risulta non valida dopo la registrazione.</translation>
    </message>
    <message>
        <source>La relazione figlio → tabella ponte risulta non valida dopo la registrazione.</source>
        <translation>La relazione figlio → tabella ponte risulta non valida dopo la registrazione.</translation>
    </message>
    <message>
        <source>Entrambe le relazioni N:M sono state registrate correttamente.</source>
        <translation>Entrambe le relazioni N:M sono state registrate correttamente.</translation>
    </message>
    <message>
        <source>Tabella ponte: {0}</source>
        <translation>Tabella ponte: {0}</translation>
    </message>
    <message>
        <source>Campo ponte padre: {0}</source>
        <translation>Campo ponte padre: {0}</translation>
    </message>
    <message>
        <source>Campo ponte figlio: {0}</source>
        <translation>Campo ponte figlio: {0}</translation>
    </message>
    <message>
        <source>Relazione N:M creata</source>
        <translation>Relazione N:M creata</translation>
    </message>
    <message>
        <source>La struttura molti-a-molti è stata creata correttamente.\n\nTabella ponte:\n{0}\n\nSono state registrate entrambe le relazioni QGIS:\n\n• {1} → tabella ponte\n• {2} → tabella ponte</source>
        <translation>La struttura molti-a-molti è stata creata correttamente.\n\nTabella ponte:\n{0}\n\nSono state registrate entrambe le relazioni QGIS:\n\n• {1} → tabella ponte\n• {2} → tabella ponte</translation>
    </message>
    <message>
        <source>Il layer referenziato non è valido.</source>
        <translation>Il layer referenziato non è valido.</translation>
    </message>
    <message>
        <source>Il campo &apos;{0}&apos; non esiste nella tabella ponte.</source>
        <translation>Il campo &apos;{0}&apos; non esiste nella tabella ponte.</translation>
    </message>
    <message>
        <source>Il campo &apos;{0}&apos; non esiste nel layer &apos;{1}&apos;.</source>
        <translation>Il campo &apos;{0}&apos; non esiste nel layer &apos;{1}&apos;.</translation>
    </message>
    <message>
        <source>Tipi incompatibili per la relazione N:M &apos;{0}&apos;: {1} → {2}.</source>
        <translation>Tipi incompatibili per la relazione N:M &apos;{0}&apos;: {1} → {2}.</translation>
    </message>
    <message>
        <source>{0} → {1} (N:M)</source>
        <translation></translation>
    </message>
    <message>
        <source>Esiste già una relazione tra la tabella ponte &apos;{0}&apos; e il layer &apos;{1}&apos; per i campi &apos;{2}&apos; → &apos;{3}&apos;.</source>
        <translation>Esiste già una relazione tra la tabella ponte &apos;{0}&apos; e il layer &apos;{1}&apos; per i campi &apos;{2}&apos; → &apos;{3}&apos;.</translation>
    </message>
    <message>
        <source>Relazione N:M &apos;{0}&apos; non valida: {1}</source>
        <translation>Relazione N:M &apos;{0}&apos; non valida: {1}</translation>
    </message>
    <message>
        <source>Impossibile creare la tabella ponte.</source>
        <translation>Impossibile creare la tabella ponte.</translation>
    </message>
    <message>
        <source>Impossibile creare i campi della tabella ponte.</source>
        <translation>Impossibile creare i campi della tabella ponte.</translation>
    </message>
    <message>
        <source>Precompilazione N:M: {0} valori padre × {1} valori figlio = {2} combinazioni.</source>
        <translation>Precompilazione N:M: {0} valori padre × {1} valori figlio = {2} combinazioni.</translation>
    </message>
    <message>
        <source>Nessuna combinazione da creare.</source>
        <translation>Nessuna combinazione da creare.</translation>
    </message>
    <message>
        <source>Numero elevato di combinazioni</source>
        <translation>Numero elevato di combinazioni</translation>
    </message>
    <message>
        <source>La precompilazione genererebbe {0} record.\n\nQuesta operazione può richiedere molta memoria e molto tempo.\n\nVuoi continuare?</source>
        <translation>La precompilazione genererebbe {0} record.\n\nQuesta operazione può richiedere molta memoria e molto tempo.\n\nVuoi continuare?</translation>
    </message>
    <message>
        <source>Precompilazione annullata dall&apos;utente.</source>
        <translation>Precompilazione annullata dall&apos;utente.</translation>
    </message>
    <message>
        <source>Errore durante la precompilazione della tabella ponte.</source>
        <translation>Errore durante la precompilazione della tabella ponte.</translation>
    </message>
    <message>
        <source>Errore durante l&apos;inserimento dei record finali.</source>
        <translation>Errore durante l&apos;inserimento dei record finali.</translation>
    </message>
    <message>
        <source>Precompilazione completata: {0} record.</source>
        <translation>Precompilazione completata: {0} record.</translation>
    </message>
    <message>
        <source>Salva tabella ponte</source>
        <translation>Salva tabella ponte</translation>
    </message>
    <message>
        <source>GeoPackage (*.gpkg);;GeoJSON (*.geojson);;Shapefile (*.shp)</source>
        <translation></translation>
    </message>
    <message>
        <source>Salvataggio su disco annullato. La tabella ponte rimane temporanea.</source>
        <translation>Salvataggio su disco annullato. La tabella ponte rimane temporanea.</translation>
    </message>
    <message>
        <source>Errore nel salvataggio della tabella ponte: {0}</source>
        <translation>Errore nel salvataggio della tabella ponte: {0}</translation>
    </message>
    <message>
        <source>Tabella ponte salvata su disco: {0}</source>
        <translation>Tabella ponte salvata su disco: {0}</translation>
    </message>
    <message>
        <source>La tabella ponte salvata non può essere ricaricata.</source>
        <translation>La tabella ponte salvata non può essere ricaricata.</translation>
    </message>
    <message>
        <source>Tabella ponte ricaricata dal file salvato.</source>
        <translation>Tabella ponte ricaricata dal file salvato.</translation>
    </message>
    <message>
        <source>Layer non selezionato</source>
        <translation>Layer non selezionato</translation>
    </message>
    <message>
        <source>Selezionare un layer padre o figlio.</source>
        <translation>Selezionare un layer padre o figlio.</translation>
    </message>
    <message>
        <source>Apertura tabella attributi: {0}</source>
        <translation>Apertura tabella attributi: {0}</translation>
    </message>
    <message>
        <source>Tabella attributi aperta: {0}</source>
        <translation>Tabella attributi aperta: {0}</translation>
    </message>
    <message>
        <source>Impossibile aprire la tabella attributi: {0}</source>
        <translation>Impossibile aprire la tabella attributi: {0}</translation>
    </message>
    <message>
        <source>Impossibile aprire la tabella attributi.\n\n{0}</source>
        <translation>Impossibile aprire la tabella attributi.\n\n{0}</translation>
    </message>
    <message>
        <source>Proprietà del progetto aperte.</source>
        <translation>Proprietà del progetto aperte.</translation>
    </message>
    <message>
        <source>Relazioni del progetto</source>
        <translation>Relazioni del progetto</translation>
    </message>
    <message>
        <source>Elimina relazione</source>
        <translation>Elimina relazione</translation>
    </message>
    <message>
        <source>Chiudi</source>
        <translation>Chiudi</translation>
    </message>
    <message>
        <source>Relazioni presenti: {0}</source>
        <translation>Relazioni presenti: {0}</translation>
    </message>
    <message>
        <source>Layer non disponibile</source>
        <translation>Layer non disponibile</translation>
    </message>
    <message>
        <source>Relazione non disponibile</source>
        <translation>Relazione non disponibile</translation>
    </message>
    <message>
        <source>La relazione selezionata non è più disponibile.</source>
        <translation>La relazione selezionata non è più disponibile.</translation>
    </message>
    <message>
        <source>Conferma eliminazione</source>
        <translation>Conferma eliminazione</translation>
    </message>
    <message>
        <source>Vuoi eliminare la relazione &apos;{0}&apos;?\n\nLa relazione verrà rimossa dal progetto.\n\nI layer e i dati non verranno eliminati.</source>
        <translation>Vuoi eliminare la relazione &apos;{0}&apos;?\n\nLa relazione verrà rimossa dal progetto.\n\nI layer e i dati non verranno eliminati.</translation>
    </message>
    <message>
        <source>Relazione eliminata: {0}</source>
        <translation>Relazione eliminata: {0}</translation>
    </message>
    <message>
        <source>QGIS non ha potuto eliminare la relazione.</source>
        <translation>QGIS non ha potuto eliminare la relazione.</translation>
    </message>
    <message>
        <source>Elenco delle relazioni del progetto visualizzato.</source>
        <translation>Elenco delle relazioni del progetto visualizzato.</translation>
    </message>
    <message>
        <source>Selezionare un layer.</source>
        <translation>Selezionare un layer.</translation>
    </message>
    <message>
        <source>Join - {0}</source>
        <translation></translation>
    </message>
    <message>
        <source>Rimuovi join</source>
        <translation>Rimuovi join</translation>
    </message>
    <message>
        <source>Join presenti: {0}</source>
        <translation></translation>
    </message>
    <message>
        <source>Conferma rimozione</source>
        <translation>Conferma rimozione</translation>
    </message>
    <message>
        <source>Vuoi rimuovere questo join?\n\nLayer: {0}\nCampo destinazione: {1}\nCampo join: {2}\n\nVerrà rimosso solo il join. I layer e i dati originali non verranno eliminati.</source>
        <translation>Vuoi rimuovere questo join?\n\nLayer: {0}\nCampo destinazione: {1}\nCampo join: {2}\n\nVerrà rimosso solo il join. I layer e i dati originali non verranno eliminati.</translation>
    </message>
    <message>
        <source>Join rimosso da {0}: {1}</source>
        <translation>Join rimosso da {0}: {1}</translation>
    </message>
    <message>
        <source>Elenco join visualizzato per {0}.</source>
        <translation>Elenco join visualizzato per {0}.</translation>
    </message>
    <message>
        <source>Tabella padre</source>
        <translation>Tabella padre</translation>
    </message>
    <message>
        <source>Layer</source>
        <translation>Layer</translation>
    </message>
    <message>
        <source>Campo chiave</source>
        <translation>Campo chiave</translation>
    </message>
    <message>
        <source>Tabella figlio</source>
        <translation>Tabella figlio</translation>
    </message>
    <message>
        <source>Campo esterno</source>
        <translation>Campo esterno</translation>
    </message>
    <message>
        <source>Tipo di relazione</source>
        <translation>Tipo di relazione</translation>
    </message>
    <message>
        <source>Cardinalità</source>
        <translation>Cardinalità</translation>
    </message>
    <message>
        <source>uno-a-uno</source>
        <translation>uno-a-uno</translation>
    </message>
    <message>
        <source>uno-a-molti</source>
        <translation>uno-a-molti</translation>
    </message>
    <message>
        <source>molti-a-molti</source>
        <translation>molti-a-molti</translation>
    </message>
    <message>
        <source>Informazioni sulla relazione</source>
        <translation>Informazioni sulla relazione</translation>
    </message>
    <message>
        <source>Opzioni tabella ponte N:M</source>
        <translation>Opzioni tabella ponte N:M</translation>
    </message>
    <message>
        <source>Nome tabella ponte</source>
        <translation>Nome tabella ponte</translation>
    </message>
    <message>
        <source>es. comuni_servizi_bridge</source>
        <translation>es. comuni_servizi_bridge</translation>
    </message>
    <message>
        <source>Precompila tutte le combinazioni possibili</source>
        <translation>Precompila tutte le combinazioni possibili</translation>
    </message>
    <message>
        <source>Attenzione: con molti valori questa opzione può generare migliaia o milioni di record.</source>
        <translation>Attenzione: con molti valori questa opzione può generare migliaia o milioni di record.</translation>
    </message>
    <message>
        <source>Opzioni</source>
        <translation>Opzioni</translation>
    </message>
    <message>
        <source>Salva tabella ponte su disco</source>
        <translation>Salva tabella ponte su disco</translation>
    </message>
    <message>
        <source>Strumenti</source>
        <translation>Strumenti</translation>
    </message>
    <message>
        <source>Apri tabella attributi</source>
        <translation>Apri tabella attributi</translation>
    </message>
    <message>
        <source>Proprietà progetto</source>
        <translation>Proprietà progetto</translation>
    </message>
    <message>
        <source>Visualizza join</source>
        <translation>Visualizza join</translation>
    </message>
    <message>
        <source>Log di elaborazione</source>
        <translation>Log di elaborazione</translation>
    </message>
    <message>
        <source>Cancella log</source>
        <translation>Cancella log</translation>
    </message>
    <message>
        <source>Avanzamento</source>
        <translation>Avanzamento</translation>
    </message>
    <message>
        <source>Crea relazione</source>
        <translation>Crea relazione</translation>
    </message>
    <message>
        <source>Selezionare una relazione</source>
        <translation>Selezionare una relazione</translation>
    </message>
</context>
</TS>

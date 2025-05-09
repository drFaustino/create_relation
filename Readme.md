# Create Relation (Crea Relazioni)

## Create one-to-one, one-to-many, and many-to-many relationships between vector layer attribute tables. (Crea relazioni uno-a-uno, uno-a-molti e molti-a-molti tra le tabelle degli attributi dei livelli vettoriali).

It allows you to define a one-to-one (1:1), one-to-many (1:N) or many-to-many (N:M) relationship between two attribute tables of vector layers loaded in QGIS. You can select the parent layer with its link field, the child layer with its field, and specify the type of relationship to create. In the case of a many-to-many relationship, an intermediate link table is automatically generated, which you can assign a custom name to and save in Shapefile or GeoJSON formats.

> Permette di definire una relazione di tipo uno-a-uno (1:1), uno-a-molti (1:N) o molti-a-molti (N:M) tra due tabelle degli attributi di layer vettoriali caricati in QGIS. È possibile selezionare il layer padre con il relativo campo di collegamento, il layer figlio con il proprio campo, e specificare il tipo di relazione da creare. Nel caso di una relazione molti-a-molti, viene generata automaticamente una tabella di collegamento intermedia, alla quale è possibile assegnare un nome personalizzato e salvarla nei formati Shapefile o GeoJSON.

### Operating modes (Modalità operative)
To get started, you need to load at least two vector layers containing attributes into your QGIS project, so that you can establish a relationship between their tables. Next, you select the layer to be used as the parent table and the layer to be used as the child table, indicating the related link fields. Once you have set the layers and fields, you choose the type of relationship to create: one-to-one (1:1), one-to-many (1:N) or many-to-many (N:M).

In the case of a many-to-many relationship, an intermediate link table ("link table") is automatically generated, to which you can assign a custom name. If no name is specified, a default name will be assigned: "ponte_n_m". This table is initially created as a virtual entity within the QGIS project.

There is also an option to save the bridge table in Shapefile or GeoJSON format, choosing the destination path via a dialog box. At the bottom of the tool window there is a text box that displays messages and warnings related to the various processes performed.

> Per iniziare, è necessario caricare nel progetto QGIS almeno due layer vettoriali contenenti attributi, in modo da poter stabilire una relazione tra le rispettive tabelle. Successivamente, si selezionano il layer da utilizzare come tabella padre e quello da utilizzare come tabella figlio, indicando i relativi campi di collegamento. Una volta impostati i layer e i campi, si sceglie il tipo di relazione da creare: uno-a-uno (1:1), uno-a-molti (1:N) o molti-a-molti (N:M).

> Nel caso di una relazione molti-a-molti, viene generata automaticamente una tabella di collegamento intermedia ("tabella ponte"), alla quale è possibile assegnare un nome personalizzato. Se non viene specificato alcun nome, ne verrà attribuito uno predefinito: ponte_n_m. Questa tabella viene inizialmente creata come entità virtuale all'interno del progetto QGIS.

> È inoltre disponibile un'opzione per salvare la tabella ponte in formato Shapefile o GeoJSON, scegliendo il percorso di destinazione tramite una finestra di dialogo. In fondo alla finestra dello strumento è presente un riquadro di testo che mostra messaggi e avvisi relativi ai vari processi eseguiti.

### Relation one-to-one (Relazione 1:1)
![img1a](https://github.com/user-attachments/assets/c19575bb-c05d-47d3-9b0d-e337153f0f2b)

### Relation one-to-many (Relazione 1:N)
![img2](https://github.com/user-attachments/assets/55219c03-c8cc-4caf-8d00-443fe65ba211)

### Relation many-to-many (Relazione N:M)
![img3](https://github.com/user-attachments/assets/f8c3aef7-ae79-4c7f-ba9e-ad8708740907)

### View relationships (Visualizzare le relazioni)
To view relations in QGIS, you can follow these methods depending on the type of relation:
+ 1:1 relation (Join): select the parent layer in the Layers panel, right-click and choose Properties. In the window that opens, go to the Join tab to view the created relation.
+ 1:N and N:M relations: open the Project menu and select Project Properties. Inside the window, go to the Relations tab to view all the relations defined between the tables.
  
> Per visualizzare le relazioni in QGIS, è possibile seguire queste modalità a seconda del tipo di relazione:
> + Relazione 1:1 (Join): selezionare il layer padre nel pannello Layer, fare clic con il tasto destro e scegliere Proprietà. Nella finestra che si apre, accedere alla scheda Join per visualizzare la relazione creata.
> + Relazioni 1:N e N:M: aprire il menu Progetto e selezionare Proprietà del progetto. All'interno della finestra, andare alla scheda Relazioni per visualizzare tutte le relazioni definite tra le tabelle.

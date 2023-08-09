---
Title: PyQgis tips. QgsVectorLayer από postgis sql ερώτημα
Date: 2014-09-23 00:10
Category: GIS
Tags: postgis , pyqgis , python , qgis , sql
---

Μία πολύ χρήσιμη δυνατότητα που μας προσφέρεται από τo [pyqgis](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/index.html) είναι να "φορτώνουμε" vector layer που προέρχεται από ερώτημα sql στην [postgis](http://postgis.net/).
Έτσι ο χρήστης μπορεί να συνδυάσει την πληροφορία που θέλει με εντολές join και να φτιάξει το layer που επιθυμεί.
Ωστόσο, στην σχετική [τεκμηρίωση](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html) για το τρόπο που φορτώνουμε vector layers δεν αναφέρεται η σχετική δυνατότητα. Μετά από αρκετό ψάξιμο και δοκιμές κατέληξα σε μερικά tips για το πως γίνεται. Αναγκαίες προϋποθέσεις για το sql ερώτημα είναι:

- Να υπάρχει πεδίο γεωμετρίας μέσα σε αυτό
- να υπάρχει μοναδικό πεδίο τύπου integer
- ο κώδικας sql πρέπει να περικλείεται σε παρενθέσεις ώστε να είναι διακρίνεται ότι πρόκειται για sql ερώτημα και όχι για όνομα πίνακα.

Τα υπόλοιπα συντάσσονται με το ίδιο τρόπο που "φορτώνεται" ένας πίνακας postgis:

```python
sql ="(select the_geom, id, name from mytable)"
uri = QgsDataSourceURI()
uri.setConnection("localhost","5432","mydb","postgres","xxxxx")
uri.setDataSource("",sql,"the_geom","","id")
vlayer = QgsVectorLayer(uri.uri(),"LayerName","postgres")
QgsMapLayerRegistry.instance().addMapLayer(vlayer)
```

Επίσης, κατόπιν δοκιμών, παρατήρησα ότι το sql ερώτημα δεν πρέπει να τελειώνει με ερωτηματικό (;) αλλά ούτε πρέπει να οριστεί κάτι στο schema του QgsDataSourceURI (όπως φαίνεται και στην γραμμή 4, η πρώτη παράμετρος στο setDataSource είναι ""). 

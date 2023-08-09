---
Title: Python, διανυσματικά δεδομένα και η βιβλιοθήκη ogr
Date: 2011-06-22 00:10
Category: GIS
Tags: ogr , osr , python , vector
---
![]({static}images/extent1.png)

Λιάκος Λ., 2011, Python, διανυσματικά δεδομένα και η βιβλιοθήκη ogr, 1η Συνάντηση Ελλήνων Χρηστών GRASS and GFOSS, HellasGI, ΕΛ/ΛΑΚ, ΤΜΧΠΑ-Πανεπιστήμιο Θεσσαλίας,ΤΕΙ Σερρών, ελληνικό παράρτημα του OSGeo, Αργαλαστή Πηλίου, 17-19/6/2011

Περιγραφή παρουσίασης:

Tο τρέχον εκπαιδευτικό βοήθημα έχει σαν στόχο να εξοικειωθούν οι ενδιαφερόμενοι με ένα εναλλακτικό μοντέλο προγραμματισμού όσον αφορά την προσπέλαση και επεξεργασία γεωχωρικών δεδομένων. Εναλλακτικό γιατί στηρίζεται στις δυναμικές και συνεχώς εξελισσόμενες, αλλά πολλές φορές παρεξηγημένες και απρόσιτες για τον κοινό χρήστη, τεχνολογίες του ελεύθερου και ανοικτού λογισμικού. Για τον προγραμματισμό του εν λόγω βοηθήματος επελέγει η διερμηνευόμενη και αντικειμενοστραφής γλώσσα Python καθώς ο διερμηνευτής της είναι διαθέσιμος σε διάφορα λειτουργικά συστήματα αλλά και για την ευκολία και απλότητα της σύνταξή της. Σε συνάρτηση με την γλώσσα προγραμματισμού λειτουργούν και οι σχετικές βιβλιοθήκες για την προσπέλαση των γεωχωρικών δεδομένων.

Η βιβλιοθήκη gdal χρησιμοποιείται για την προσπέλαση ψηφιδωτών γεωχωρικών δεδομένων και η βιβλιοθήκη ogr για την προσπέλαση διανυσματικών δεδομένων. Το βοήθημα επικεντρώνεται στην ανάγνωση και εγγραφή διανυσματικών δεδομένων, την δημιουργία γεωμετριών και τον χειρισμό και μετατροπή προβολικών συστημάτων, το φιλτράρισμα και την παρουσίαση των λειτουργιών ανάλυσης που παρέχει η βιβλιοθήκη ogr. Για την παρακολούθηση των διαδικασιών του βοηθήματος θεωρείται απαραίτητη η γνώση βασικών αρχών προγραμματισμού και η σύνταξη στην γλώσσα Python. Τα παραδείγματα που θα παρουσιαστούν εκτελούνται σε περιβάλλον Linux ωστόσο οι χρήστες Windows με την εγκατάσταση του απαραίτητου λογισμικού μπορούν με ευκολία να ακολουθήσουν.



```
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
#http://www.gdal.org/ogr/ogr_arch.html
#Για help από το documentation του Python binding: pydoc -g osgeo
 
#********************** - ΕΙΣΑΓΩΓΗ ΑΠΑΡΑΙΤΗΤΩΝ ΒΙΒΛΙΟΘΗΚΩΝ - ********************** 
import sys, os
 
# Εισάγουμε την βιβλιοθήκη για πρόσβαση στα διανυσματικά δεδομένα (ogr) και 
#την βιβλιοθήκη  για την διαχείριση των προβολικών συστημάτων αναφοράς (osr)
try:
    #Σε περίπτωση που χρησιμοποιούμε κάποια διανομή OSGeo
    from osgeo import ogr , osr    
except:
    #Σε περίπτωση που χρησιμοποιούμε FWTools
    import ogr,  osr
 
# ********************** - ΑΝΑΓΝΩΣΗ ΔΙΑΝΥΣΜΑΤΙΚΩΝ ΔΕΔΟΜΕΝΩΝ - **********************************
#*************************************************************************************************************
 
#Ορίζουμε τη διαδρομή για τον τρέχοντα κατάλογο εργασίας και ονόμα αρχείου shapefile
scriptdir= os.path.dirname( os.path.realpath( __file__ ) )# η διαδρομή του φακέλου που βρίσκεται το τρέχον αρχείο
os.chdir(scriptdir+os.sep+'shps')#αλλαγή του τρέχοντος καταλόγου εργασίας
 
shapefile= 'oikismoi.shp'
 
# O driver είναι ένα αντικείμενο που μας βοηθά να αλληλεπιδρούμε (διαβάζουμε - γράφουμε) με έναν τύπο αρχείου
#http://www.gdal.org/ogr/ogr_formats.html
driver =  ogr.GetDriverByName('ESRI Shapefile') # Το όνομα παρέχεται από το documentation
 
# Με την μέθοδο Open() του driver επιστρεφεται ένα αντικείμενο datasource
dataSource = driver.Open(shapefile,  0) #0=readonly, 1=write
 
if dataSource is None: # Αν δεν υπάρχει τιμή στην dataSource
    print u'Η πηγή δεδομένων δεν αναγνώστηκε:' ,   shapefile
    sys.exit(1) #έξοδος με έναν κωδικό σφάλματος
 
layer = dataSource.GetLayer() 
#1.μπορούμε να χρησιμοποιήσουμε και index π.χ dataSource.GetLayer(1) αλλά για τα shapefiles είναι 0
#2.ή να περάσουμε το όνομα σαν string (π.χ. 'oikismoi')
print u'Το όνομα του layer:' , layer.GetName()
 
#Ο αριθμός των features στο layer
numFeatures = layer.GetFeatureCount()
print u'Αριθμός Features :', numFeatures
 
# επιστρέφει τα ακραία σημεία του layer
extent = layer.GetExtent() 
print u'Ακραία σημεία:', extent
 
# εφόσον γνωρίζουμε το FID ενος feature μπορούμε να το πάρουμε σαν αντικείμενο
feature = layer.GetFeature(2) #FID=2
 
CODE_OIK = feature.GetField('CODE_OIK') #GetField(&lt;όνομα πεδίου&gt;) μία μέθοδος του feature που μας επιστρέφει την τιμή του πεδίου 
#fields= layer.GetLayerDefn().GetFieldCount() # παίρνουμε τον αριθμό των πεδίων σε ένα layer
 
NAME_OIK = feature.GetField('NAME_OIK')
# Παραλλαγή:
#GetFieldAsString(&lt;όνομα πεδίου&gt;) και GetFieldAsInteger(&lt;όνομα πεδίου&gt;)
print u'CODE_OIK για το feature με id = 2:',  CODE_OIK
NAME_OIK = NAME_OIK.decode('iso-8859-7')
print u'NAME_OIK για το feature με id = 2:',  NAME_OIK
 
#μπορούμε να βάλουμε όλα τα features του layer σε έναν βρόγχο
feature = layer.GetNextFeature() # επιστρέφει το πρώτο Feature στην σειρά και κάθε φορά που το καλούμε πηγαίνει στο επόμενο
while feature:
    CODE_OIK = feature.GetField('CODE_OIK')
    print 'FID:%s,CODE_OIK:%s' % (feature.GetFID(), CODE_OIK)
    feature = layer.GetNextFeature()
 
layer.ResetReading() #επιστρέφει την ανάγνωση των features στην αρχή της λίστας των features
 
# ας ξανα πάμε στο πρώτο Feature
feature = layer.GetNextFeature() 
#ας πάρουμε την γεωμετρία του
geometry = feature.GetGeometryRef() #GetGeometryRef() μία μέθοδος του feature που επιστρέφει την γεωμετρία σαν αντικείμενο 
print "Geometry name: ", geometry.GetGeometryName() # as WKT
#Ειδικά τα σημειακά layers έχουν μια μέθοδο στο αντικείμενο της γεωμετρίας που τους επιστρέφει το X και το Y
x = geometry.GetX()
y = geometry.GetY()
print "X Y:",  x,  y
 
#********************************** - Φίλτρα στα περιγραφικά δεδομένα - **********************************
#************************************************************************************************************
# 1: .SetAttributeFilter
# 2: .ExecuteSQL
 
# ------1: layer.SetAttributeFilter
allFeatures = layer.GetFeatureCount()
print u'Όλα τα Features :', allFeatures
 
layer.SetAttributeFilter("CODE_NOM = '32'") # με την μέθοδο SetAttributeFilter ορίζουμε τα κριτήρια ενός φίλτρου π.χ. εδώ ζητήσαμε από τους οικισμούς να μας φέρει αυτούς που έχουν ("CODE_NOM = '32'") 
thesprotia = layer.GetFeatureCount() # πλέον η μέθοδος GetFeatureCount() του layer μας επιστρέφει μόνο τα Features με CODE_NOM = '32'
print u'Tα Features της Θεσπρωτίας :', thesprotia
 
feature = layer.GetNextFeature() # επιστρέφει το πρώτο Feature στην σειρά από την λίστα των φιλτραρισμένων και κάθε φορά που το καλούμε πηγαίνει στο επόμενο
 
layer.SetAttributeFilter(None) # κάνουμε reset του φίλτρου
 
# -------2: dataSource.ExecuteSQL
#Μπορούμε να κάνουμε και πιο προχωρημένα ερωτήματα με ExecuteSQL() στο datasource αντικείμενο
#http://www.gdal.org/ogr/ogr_sql.html
resultlayer = dataSource.ExecuteSQL("SELECT * from oikismoi  WHERE OBJECTID &gt; 13000 ORDER BY CODE_OIK DESC")
sqlFeatures = resultlayer.GetFeatureCount() # πλέον η μέθοδος GetFeatureCount() του layer μας επιστρέφει μόνο τα Features με CODE_NOM = '32'
print u'Tα Features με OBJECTID &gt; 13000 :', sqlFeatures
dataSource.ReleaseResultSet(resultlayer)# κάνουμε reset του φίλτρου
 
#********************************** - Φίλτρα στα χωρικά δεδομένα - **********************************
#************************************************************************************************************
 
#1.  .SetSpatialFilter()
#2.  .SetSpatialFilterRect(, ,, )
 
#Eπιλέγουμε το πολύγωνο της Θεσπρωτίας από τους νομούς για να το χρησιμοποιήσουμε σαν παράμετρο στο SetSpatialFilter
nomoishp= 'nomoi_okxe.shp'
dataSource2 = driver.Open(nomoishp,  0) #0=readonly, 1=write
layer2= dataSource2.GetLayer()
feature52 = layer2.GetFeature(52) #52 το fid του Ν. Θεσπρωτίας
polyThesprotia = feature52.GetGeometryRef()# πήραμε το γεωμετρικό αντικείμενο του feature52 (του Ν. Θεσπρωτίας)
 
#1.  .SetSpatialFilter()
layer.SetSpatialFilter(polyThesprotia) 
oikismoiThesprotias = layer.GetFeatureCount()
print u'Οι οικισμοί της Θεσπρωτίας από χωρικό φίλτρο :', oikismoiThesprotias
layer.SetSpatialFilter(None) # κάνουμε reset του φίλτρου
 
#SLIDE 9
 
#2. .SetSpatialFilterRect(, ,, )
layer.SetSpatialFilterRect(170000, 4270000,300000, 4500000)
numfromRect = layer.GetFeatureCount()
print u'Αριθμός από χωρικό φίλτρο :', numfromRect
 
#SLIDE 10
 
layer.SetSpatialFilter(None) # κάνουμε reset του φίλτρου
 
AllFeatures = layer.GetFeatureCount()
print u'Όλα τα Features ξανά :', AllFeatures
 
#************************************* - Simple analysis - Geoprocessing ***************************************************
#************************************************************************************************************
 
#Είναι μέθοδοι του geometry object όπου  επιστρέφουν boolean ή geometry objects ή αριθμός
#http://www.gdal.org/ogr/classOGRGeometry.html
#Within, Overlaps, Contains, Convexhull, Buffer, Union, Difference κ.α.
 
# Μερικά απαράιτητα δεδομένα:
 
# Η Παραμυθιά Θεσπρωτίας (point)
featParamythia= layer.GetFeature(3005) #feature object
ptParamythia= featParamythia.GetGeometryRef()#geometry object
print ptParamythia #σαν WKT
 
# Η Αργαλαστή (point)
featArgalasti= layer.GetFeature(11651) 
ptArgalasti = featArgalasti.GetGeometryRef()
print ptArgalasti
 
#Ποιά η  απόσταση από Παραμυθιά σε Αργαλαστή;
dist = ptParamythia.Distance(ptArgalasti) 
print u'Απόσταση Παραμυθιά-Αργαλαστή σε χλμ.:', dist/1000
 
#buffer 1000μ. για την Παραμυθιά
ptBuffer = ptParamythia.Buffer(1000) # geometry object
print ptBuffer #polygon
 
# Η Θεσπρωτία περιέχει την Παραμυθιά;
print polyThesprotia.Contains(ptParamythia)
 
# Η Παραμυθιά περιέχεται στην Θεσπρωτία;
print ptParamythia.Within(polyThesprotia)
 
#Το κεντροειδές της Θεσπρωτίας
centroid_obj = polyThesprotia.Centroid()
print  u'Το κεντροειδές της Θεσπρωτίας σαν WKT:' , centroid_obj
centroid = ogr.CreateGeometryFromWkt(str(centroid_obj))#Δημιουργία geometry object (σημείου) από  WKT
x = centroid.GetX()
y = centroid.GetY()
print u'Το κεντροειδές της Θεσπρωτίας: ',  x,  y
 
# Η γεωγραφική έκταση της Θεσπρωτίας (minx,maxx, miny, maxy):
print u'minx,maxx, miny, maxy για την Θεσπρωτία:', polyThesprotia.GetEnvelope()[0],  polyThesprotia.GetEnvelope()[1],  polyThesprotia.GetEnvelope()[2], polyThesprotia.GetEnvelope()[2]
 
#********************************* - ΕΓΓΡΑΦΗ ΔΕΔΟΜΕΝΩΝ -  ΠΡΟΒΟΛΙΚΑ ΣΥΣΤΗΜΑΤΑ*********************************************
#************************************************************************************************************
 
if os.path.exists('mypoints.shp'):# έλεγχος αν υπάρχει το path
    driver.DeleteDataSource('mypoints.shp')
 
ds = driver.CreateDataSource('mypoints.shp')
 
#Αναγκαία η εισαγωγή της βιβλιοθήκης: from osgeo import osr
 
#Ορίζουμε ένα αντικείμενο για το γεωγραφικό σύστημα αναφοράς
SpatialReference = osr.SpatialReference() #αρχικοποίηση αντικειμένου γεωγραφικού σύστηματος αναφοράς
#Πολλοί τρόποι σύνταξης/ορισμού ενός συστήματος αναφοράς,Well Known Text (WKT), Proj4, EPSG, ESRI .prj, JSON, GML, XML
#Σημαντικό: για το τρόπο σύνταξης και λεπτομέρειες ανά σύστημα αναφοράς μπορείτε να δείτε στο http://spatialreference.org/
 
#Περισσότεροι τρόποι:
#ImportFromWkt()
#ImportFromEPSG()
#ImportFromProj4()
#ImportFromESRI(&lt;proj_lines&gt;)
#ImportFromPCI(, ,
#ImportFromUSGS(&lt;proj_code&gt;, )
#ImportFromXML()
 
SpatialReference.ImportFromEPSG(2100)
#SpatialReference.SetFromUserInput('EPSG:2100')
#Μπορούμε να το ορίσουμε και με άλλο τρόπο μέσω του EPSG code:
#SpatialReference.ImportFromProj4("+proj=tmerc +lon_0=24 +k=.9996 +x_0=500000 +towgs84=-199.72,74.03,246.02+ellps=GRS80")
 
#------------Δημιουργία νέου layer--------------
newlayer = ds.CreateLayer('mypoints',geom_type=ogr.wkbPoint,  srs = SpatialReference)
#Τύπου γεωμετρίας: wkbPoint, wkbLineString, wkbPolygon, wkbGeometryCollection, wkbMultiPolygon, wkbMultiPoint, wkbMultiLineString.
 
# Αν θέλουμε να ανακτήσουμε το προβολικό σύστημα ενός layer σαν αντικείμενο:
SR = newlayer.GetSpatialRef()
print SR
# Μπορεί να ανακτηθεί και από ένα αντικείμενο γεωμετρίας: spatialRef = geom.GetSpatialReference()
print SR.ExportToXML() #εξαγωγή σαν GML
 
#Δημιουργία ενός FieldDefn
fieldDefn = ogr.FieldDefn('greekname', ogr.OFTString) #Constructor of Definition of an attribute of an OGRFieldDefn. , http://www.gdal.org/ogr/classOGRFieldDefn.html#fc375f038b548b5a86b854c214fee114
fieldDefn.SetWidth(15)
 
newlayer.CreateField(fieldDefn)#αποθήκευση του FieldDefn στο layer
 
#ορίζουμε ένα νέο γεωμετρικό αντικείμενο τύπου σημείου
geom = ogr.Geometry(type=ogr.wkbPoint)
geom.AddPoint(23.726683, 37.971505) #δεδομενα σε WGS84 , προαρετικά τρίτη παράμετρος το z  (default=0)
# για αλλαγή των Χ, Υ: geom.SetPoint(0, 23.0, 37.0), όπου για σημεία υποστηρίζεται μόνο το 0
#για αντικείμενα τύπου γραμμής προσθέτουμε νέα σημεία της γραμμής με το AddPoint
 
#------------Reprojection του geom από WGS84 σε Greek Grid
#Ορίζουμε τα προβολικά συστήματα ως objects και τους δίνουμε παραμέτρους:
 
#WGS84
wgs84SR= osr.SpatialReference()
wgs84SR.ImportFromEPSG(4326) #  WGS84
#Greek_Grid
greekGridSR= osr.SpatialReference()
greekGridSR.ImportFromEPSG(2100) # Greek Grid
 
#Απαιτείται ένα CoordinateTransformation αντικείμενο
coordTrans = osr.CoordinateTransformation(wgs84SR, greekGridSR)
 
#Καλούμε την function Transform του geometry αντικειμένου
geom.Transform(coordTrans)
 
xEgsa = geom.GetX()
yEgsa  = geom.GetY()
print "X, Y ΕΓΣΑ-87:",  xEgsa ,  yEgsa 
 
#Δημιουργία του Feature object
featureDefn = newlayer.GetLayerDefn() # ανάκτηση τους σχήματος του layer (σχήμα πεδίων και ιδιοτήτων τους των features του layer.Επιστρέφει: feature definition. 
feature = ogr.Feature(featureDefn) #Constructor για νέο feature object με το field definition του layer 
feature.SetGeometry(geom)#Του ορίζουμε σαν γεωμετρία το geom object
 
feature.SetField('greekname', u"Ακρόπολη".encode('iso-8859-7'))
 
newlayer.CreateFeature(feature)#αποθήκευση του feature στο layer
 
# Cleanup, απελευθερώνουμε πόρους
#Δεν καλούμε το Destroy() σε geometry objects που προέρχονται από features (Segmentation fault στην Python ) π.χ. polyThesprotia, ptArgalasti, ptParamythia
 
#Destroy geometries
centroid_obj.Destroy()
geom.Destroy()
 
#Destroy features
feature.Destroy()
feature52.Destroy()
featParamythia.Destroy()
featArgalasti.Destroy()
 
#Destroy datasources
dataSource.Destroy()
dataSource2.Destroy()
ds.Destroy() # Κλείσιμο και αποθήκευση του datasource για να αποθηκευτεί
 
print u'Δημιουργία εικόνας png με το Mapnik!'
 
import mapnik
 
#symbolizers
symbolizer = mapnik.PolygonSymbolizer(mapnik.Color("#fdf9e5"))
symbolizer1= mapnik.LineSymbolizer(mapnik.Color('black'),0.5)
symbolizer2= mapnik.ShieldSymbolizer('greekname','DejaVu Sans Bold',12,mapnik.Color('#000000'),'icon.png','png',32,32)
 
#
rule = mapnik.Rule()
rule.symbols.append(symbolizer)
rule.symbols.append(symbolizer1)
 
rule2 = mapnik.Rule()
rule2.symbols.append(symbolizer2)
 
#styles
style = mapnik.Style()
style.rules.append(rule)
 
style2 = mapnik.Style()
style2.rules.append(rule2)
 
#layers
layer = mapnik.Layer("nomoi")
layer.datasource = mapnik.Shapefile(file="nomoi_okxe.shp")
 
layer2= mapnik.Layer("oikismoi")
layer2.datasource = mapnik.Shapefile(file="mypoints.shp",  encoding='ISO-8859-7')
 
layer.styles.append("mapStyle")
layer2.styles.append("mapStyle2")
 
map = mapnik.Map(800, 400)
map.background = mapnik.Color("#c5edff")
 
map.append_style("mapStyle", style)
map.append_style("mapStyle2", style2)
 
map.layers.append(layer)
map.layers.append(layer2)
 
map.zoom_all()
 
mapnik.render_to_file(map, "map.png", "png")
 
print u'Η εκτέλεση του script ολοκληρώθηκε!'
 
#Παραδείγματα:
#//www.geographer.gr/gis/64-gefyria.html
```
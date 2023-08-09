---
Title: NMEA183toshp.py - Μετατροπή αρχείου ΝΜΕΑ183 σε shapefile
Date: 2009-07-07 00:10
Category: GIS
Tags: gps , nmea183 , ogr , python
---

![]({static}images/nmea.png)

Tο εργαλείο NMEA183toshp.py έχει σαν σκοπό την μετατροπή καταγεγραμμένων συντεταγμένων από το πρότυπο [ΝΜΕΑ183](https://en.wikipedia.org/wiki/NMEA_0183) σε αρχείο [shapefile](https://en.wikipedia.org/wiki/Shapefile#Spatial_representation).

Στον χρήστη δίνεται η δυνατότητα να εξάγει το αρχειο σε μορφή shapefile επιλέγοντας τον τύπο της γεωμετρίας (γραμμική ή σημειακή) καθώς και το γεωγραφικό σύστημα αναφοράς (WGS84 ή ΕΓΣΑ'87).

Το παρόν εργαλείο αποτελεί παραμετροποίηση και επέκταση από το arcgis script [gps2shp](http://arcscripts.esri.com/details.asp?dbid=13990) του [Δημήτρη Σταθάκη](http://dstath.users.uth.gr/).

Είναι γραμμένο με την γλώσσα Python και το γραφικό του περιβάλλον στηρίζεται στην πλατφόρμα pyQt4. Η περαιτέρω επεξεργασία για την μετατροπή των δεδομένων σε shapefile βασίζεται στην βιβλιοθήκη [osgeo για την python](https://wiki.osgeo.org/wiki/OSGeo_Python_Library). Το πρόγραμμα έχει δοκιμαστεί στο λειτουργικό σύστημα Ubuntu 9.04


Download [NMEA183toshp.py]({static}extra/NMEA183toshp.py)

Αφού κατεβάσετε το αρχείο πρέπει να το ορίσετε σαν εκτελέσιμο:

```
 chmod +x NMEA183toshp.py
```

Στην συνέχεια με διπλό κλικ στο αρχείο NMEA183toshp.py θα εμφανιστεί το γραφικό περιβάλλον του προγράμματος.

![]({static}images/nmea2shp.jpg)

Παρακάτω διατίθεται ο κώδικας του προγράμματος:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys,  os,  string
from osgeo import ogr
from osgeo import osr
from PyQt4 import QtGui, QtCore
 
class Ui_MainWindow(object):
def setupUi(self, MainWindow):
MainWindow.setObjectName("MainWindow")
MainWindow.resize(800, 600)
self.centralwidget = QtGui.QWidget(MainWindow)
self.centralwidget.setObjectName("centralwidget")
self.groupBox = QtGui.QGroupBox(self.centralwidget)
self.groupBox.setGeometry(QtCore.QRect(30, 20, 741, 331))
self.groupBox.setObjectName("groupBox")
self.textBrowser = QtGui.QTextBrowser(self.groupBox)
self.textBrowser.setGeometry(QtCore.QRect(20, 60, 701, 251))
self.textBrowser.setFrameShape(QtGui.QFrame.Box)
self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
self.textBrowser.setObjectName("textBrowser")
self.widget = QtGui.QWidget(self.groupBox)
self.widget.setGeometry(QtCore.QRect(20, 18, 701, 41))
self.widget.setObjectName("widget")
self.gridLayout = QtGui.QGridLayout(self.widget)
self.gridLayout.setObjectName("gridLayout")
self.label = QtGui.QLabel(self.widget)
self.label.setObjectName("label")
self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
self.lineEdit = QtGui.QLineEdit(self.widget)
self.lineEdit.setObjectName("lineEdit")
self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
self.pushButton = QtGui.QPushButton(self.widget)
self.pushButton.setObjectName("pushButton")
self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
self.groupBox_2.setGeometry(QtCore.QRect(30, 360, 741, 161))
self.groupBox_2.setObjectName("groupBox_2")
self.layoutWidget = QtGui.QWidget(self.groupBox_2)
self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 701, 41))
self.layoutWidget.setObjectName("layoutWidget")
self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
self.gridLayout_2.setObjectName("gridLayout_2")
self.label_2 = QtGui.QLabel(self.layoutWidget)
self.label_2.setObjectName("label_2")
self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
self.lineEdit_2.setObjectName("lineEdit_2")
self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
self.pushButton_2.setObjectName("pushButton_2")
self.gridLayout_2.addWidget(self.pushButton_2, 0, 2, 1, 1)
self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
self.groupBox_3.setGeometry(QtCore.QRect(20, 60, 151, 80))
self.groupBox_3.setObjectName("groupBox_3")
self.radioButton = QtGui.QRadioButton(self.groupBox_3)
self.radioButton.setGeometry(QtCore.QRect(10, 20, 141, 22))
self.radioButton.setObjectName("radioButton")
self.radioButton.setChecked(True)
self.radioButton_2 = QtGui.QRadioButton(self.groupBox_3)
self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 131, 22))
self.radioButton_2.setObjectName("radioButton_2")
self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
self.groupBox_4.setGeometry(QtCore.QRect(190, 60, 211, 80))
self.groupBox_4.setObjectName("groupBox_4")
self.comboBox = QtGui.QComboBox(self.groupBox_4)
self.comboBox.setGeometry(QtCore.QRect(10, 30, 121, 22))
self.comboBox.setObjectName("comboBox")
self.comboBox.addItem(QtCore.QString())
self.comboBox.addItem(QtCore.QString())
self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
self.pushButton_3.setGeometry(QtCore.QRect(310, 540, 80, 27))
self.pushButton_3.setObjectName("pushButton_3")
MainWindow.setCentralWidget(self.centralwidget)
self.statusbar = QtGui.QStatusBar(MainWindow)
self.statusbar.setObjectName("statusbar")
MainWindow.setStatusBar(self.statusbar)
 
self.retranslateUi(MainWindow)
QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.showDialog)
QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.saveDialog)
QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.Convert)
QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.GetSRS)
def Convert(self):
try:
# path &amp; name of the GPS log file
gpsFile = self.Openfilename.toLocal8Bit()
print gpsFile
print type(gpsFile)
 
# output folder &amp; SHAPEFILE name
outShapeFile = self.shp
drv = ogr.GetDriverByName('ESRI Shapefile')
if os.path.exists(str(outShapeFile)):
 
drv.DeleteDataSource(str(outShapeFile))
print ("shapefile deleted")
print outShapeFile
print type(outShapeFile)
t_srs = osr.SpatialReference()
 
if self.comboBox.currentText()=='Greek Grid':
print "Greek Grid"
t_srs.ImportFromProj4("+proj=tmerc +lon_0=24 +k=.9996 +x_0=500000 +towgs84=-199.72,74.03,246.02+ellps=GRS80")
 
t_srs.SetFromUserInput('EPSG:2100') #Greek Grid
else:
t_srs.SetFromUserInput('WGS84')
print "WGS84"
print str(outShapeFile)
ds = drv.CreateDataSource(str(outShapeFile))
if  self.radioButton.isChecked():
layer = ds.CreateLayer(ds.GetName(), geom_type = ogr.wkbPoint, srs = t_srs)
layer.CreateField(ogr.FieldDefn('TimeStamp', ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn('quality', ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn('NumbSats', ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn('HDOP', ogr.OFTReal))
layer.CreateField(ogr.FieldDefn('Altitude', ogr.OFTReal))
else:
print('line shp is created')
layer = ds.CreateLayer(ds.GetName(), geom_type = ogr.wkbLineString, srs = t_srs)
line = ogr.Geometry(ogr.wkbLineString)
 
# initialize variables.
numberOfLines = 0
numberOfSkippedLines = 0
gpsLine = ""
coord = ""
 
# open GPS log file to read.
f=open(str(gpsFile), 'r')
while gpsLine.isalnum:
gpsLine = f.readline()
if not gpsLine: break
numberOfLines = numberOfLines + 1
linesp = gpsLine.split(',',15)
 
if linesp[0]=='$GPGGA':
 
# convert Latitude from DDMM.MMM (variable no of digits) to DD.DDD
latDDMM = linesp[2].split('.',2)
latLen = len(latDDMM[0]) - 2
 
if len(latDDMM) == 1:
latDDDD = int(latDDMM[0][0:latLen]) + (float(latDDMM[0][-2:]) / 60)
else:
latDDDD = int(latDDMM[0][0:latLen]) + (float(latDDMM[0][-2:] + "." + latDDMM[1]) / 60)
 
# convert Longitude from DDMM.MMM (variable no of digits) to DD.DDD
longDDMM = linesp[4].split('.',2)
longLen = len(longDDMM[0]) - 2
 
if len(longDDMM) == 1:
longDDDD = int(longDDMM[0][0:longLen]) + (float(longDDMM[0][-2:]) / 60)
else:
longDDDD = int(longDDMM[0][0:longLen]) + (float(longDDMM[0][-2:] + "." + longDDMM[1]) / 60)
 
# Convert to negative for West and South coord.
if linesp[3] == "S":
longDDDD = longDDDD * (-1)
if linesp[5] == "W":
latDDDD = latDDDD * (-1)
 
# a simple test to skip corrupted NMEA sentences.
if latDDDD &lt;= -90 or latDDDD &gt;= 90:
numberOfSkippedLines = numberOfSkippedLines + 1
break
if longDDDD &lt;= -180 or longDDDD &gt;= 180:
numberOfSkippedLines = numberOfSkippedLines + 1
break
 
if  self.radioButton.isChecked():
 
print longDDDD, latDDDD
geom = ogr.Geometry(type=ogr.wkbPoint)
geom.AddPoint(longDDDD,latDDDD)
print geom.GetX(), geom.GetY()
 
if self.comboBox.currentText()=='Greek Grid':
sourceSR = osr.SpatialReference()
sourceSR.SetFromUserInput('WGS84')
targetSR = osr.SpatialReference()
targetSR.ImportFromProj4("+proj=tmerc +lon_0=24 +k=.9996 +x_0=500000 +towgs84=-199.72,74.03,246.02+ellps=GRS80")
 
coordTrans = osr.CoordinateTransformation(sourceSR, targetSR)
geom.Transform(coordTrans)
print geom.GetX(), geom.GetY()
 
feat = ogr.Feature(feature_def=layer.GetLayerDefn())
feat.SetGeometry(geom)
feat.SetFID(int(numberOfLines))
 
#change time stamp format to DDDHHMMSS. Looks better!
TStamp = linesp[1].split('.',2)
feat.SetField('TimeStamp', int(string.zfill(TStamp[1], 3) + string.zfill(TStamp[0], 6)))
feat.SetField('quality', int(linesp[6]))
feat.SetField('NumbSats', float(linesp[7]))
if not linesp[8]:
feat.SetField('HDOP', 0)
else:
feat.SetField('HDOP', float(linesp[8]))
feat.SetField('Altitude', float(linesp[9]))
layer.CreateFeature(feat)
else:
print('Add point in line ' + str(longDDDD )+ ','  + str(latDDDD))
line.AddPoint(longDDDD,latDDDD)
 
if  self.radioButton.isChecked():
pass
else:
print line.GetPointCount()
print('line is writen')
feat = ogr.Feature(feature_def=layer.GetLayerDefn())
if self.comboBox.currentText()=='Greek Grid':
sourceSR = osr.SpatialReference()
sourceSR.SetFromUserInput('WGS84')
targetSR = osr.SpatialReference()
targetSR.ImportFromProj4("+proj=tmerc +lon_0=24 +k=.9996 +x_0=500000 +towgs84=-199.72,74.03,246.02+ellps=GRS80")
coordTrans = osr.CoordinateTransformation(sourceSR, targetSR)
line.Transform(coordTrans)
feat.SetGeometry(line)
feat.SetFID(0)
layer.CreateFeature(feat)
 
# Clean up
ds.Destroy()
Done = QtGui.QMessageBox.question(None, u'Ενημέρωση', u'Η μετατροπή ολοκληρώθηκε επιτυχώς', QtGui.QMessageBox.Ok)
except AttributeError:
Error = QtGui.QMessageBox.critical(None, u'Σφάλμα', u'Παρακαλώ ελέγξτε τις διαδρομές των αρχείων', QtGui.QMessageBox.Ok)
#
#
 
def GetSRS(self):
item = self.comboBox.currentText()
print  item
 
def saveDialog(self):
home=os.environ.get('HOME')
self.Savefilename = QtGui.QFileDialog.getSaveFileName(None, u'Αποθήκευση δεδομένων σε αρχείο shapefile',  home,  "Shapefile (*.shp)");
 
if self.Savefilename.toLocal8Bit()=='' :
pass
else:
self.shp=self.Savefilename.toLocal8Bit() + '.shp'
self.lineEdit_2.setText(self.shp)
 
def showDialog(self):
home=os.environ.get('HOME')
 
self.Openfilename = QtGui.QFileDialog.getOpenFileName(None, u'Επιλογή αρχειου NMEA183', home)
 
if self.Openfilename.toLocal8Bit()=='' :
pass
else:
file=open(self.Openfilename.toLocal8Bit())
data = file.read()
self.lineEdit.setText(str(self.Openfilename))
self.textBrowser.setText(data)
file.close
 
def retranslateUi(self, MainWindow):
MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Μετατροπή αρχείου NMEA183 σε Shapefile", None, QtGui.QApplication.UnicodeUTF8))
self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Αρχείο NMEA183", None, QtGui.QApplication.UnicodeUTF8))
self.textBrowser.setToolTip(QtGui.QApplication.translate("MainWindow", "Δεδομένα του αρχείου Shapefile", None, QtGui.QApplication.UnicodeUTF8))
self.label.setText(QtGui.QApplication.translate("MainWindow", "Αρχείο:", None, QtGui.QApplication.UnicodeUTF8))
self.lineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Παρακαλώ επιλέξτε το αρχείο NMEA183", None, QtGui.QApplication.UnicodeUTF8))
self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Άνοιγμα", None, QtGui.QApplication.UnicodeUTF8))
self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Shapefile", None, QtGui.QApplication.UnicodeUTF8))
self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Αρχείο:", None, QtGui.QApplication.UnicodeUTF8))
self.lineEdit_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Παρακαλώ, αποθηκεύστε την μετατροπή σε ένα νέο αρχείο Shapefile", None, QtGui.QApplication.UnicodeUTF8))
self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Αποθήκευση", None, QtGui.QApplication.UnicodeUTF8))
self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Τύπος αρχείου", None, QtGui.QApplication.UnicodeUTF8))
self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "Point", None, QtGui.QApplication.UnicodeUTF8))
self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Line", None, QtGui.QApplication.UnicodeUTF8))
self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Γεωγραφικό Σύστημα Αναφοράς", None, QtGui.QApplication.UnicodeUTF8))
self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "WGS84", None, QtGui.QApplication.UnicodeUTF8))
self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Greek Grid", None, QtGui.QApplication.UnicodeUTF8))
self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Μετατροπή", None, QtGui.QApplication.UnicodeUTF8))
app = QtGui.QApplication(sys.argv)
widget = QtGui.QMainWindow()
mywidget = Ui_MainWindow()
mywidget.setupUi( widget )
widget.show()
app.exec_()

```


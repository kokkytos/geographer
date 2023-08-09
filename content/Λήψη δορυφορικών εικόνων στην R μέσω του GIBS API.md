---
Title: Λήψη δορυφορικών εικόνων στην R μέσω του GIBS API
Date: 2017-11-19 10:20
Category: GIS
Tags:    API , gdal , gdalUtils , GIBS , R
---

Η υπηρεσία [Global Imagery Browse Services (GIBS)](https://wiki.earthdata.nasa.gov/display/GIBS/Global+Imagery+Browse+Services+-+GIBS) του παρατηρητηρίου [Earth Observing System Data and Information System (EOSDIS)](https://earthdata.nasa.gov/) παρέχει δορυφορικές εικόνες πλήρους ανάλυσης σε παγκόσμιο επίπεδο. Η υπηρεσία παρέχει πρόσβαση σε 600 και πλέον προϊόντα δορυφορικών εικόνων τα οποία στην πλειονότητά τους είναι διαθέσιμα με χρονική υστέρηση λίγων ωρών από την διέλευση του δορυφόρου. Η οπτικοποίηση των δεδομένων αυτών υποστηρίζεται από σχετική διαδικτυακή εφαρμογή [WorldView](https://worldview.earthdata.nasa.gov/)αλλά και μέσω υπηρεσιών (πρωτόκολλα OGC Web Map Tile Service (WMTS)/Tiled Web Map Service (TWMS)) που επιτρέπουν την ενσωμάτωσή του σε τρίτες εφαρμογές. Επιπλέον μια από της πλέον χρήσιμες λειτουργίες της υπηρεσίας GIBS είναι δυνατότητα εκτέλεσης σεναρίου εντολών μέσω της βιβλιοθήκης [Geospatial Data Abstraction Library (GDAL)](http://www.gdal.org/). Αυτή η δυνατότητα παρέχει στον χρήση την ευκολία να αυτοματοποιήσει την λήψη δεδομένων (π.χ. μαζική λήψη δεδομένων, αυτόματη περιοδική λήψη, λήψη δεδομένων υπό συγκεκριμένες συνθήκες κτλ.).

Στην τρέχουσα ανάρτηση παρουσιάζεται ένα σενάριο λήψης δεδομένων από την πλατφόρμα GIBS με την γλώσσα προγραμματισμού R. Στόχος είναι να δημιουργηθεί ένα σενάριο εντολών όπου ο χρήστης θα παρέχει στο script πληροφορίες για το προϊόν και το script θα λαμβάνει τις σχετικές δορυφορικές εικόνες.

Οι πληροφορίες αυτές αφορούν το όνομα του προϊόντος, το προβολικό του σύστημα, την ημερομηνία λήψης και την περιοχή μελέτης που ενδιαφέρει τον χρήστη. Οι πληροφορίες για κάθε προϊόν (ονομασία, επίπεδα εστίασης, προβολικό σύστημα) είναι διαθέσιμες στην σχετική ενότητα της [υπηρεσίας](https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+Available+Imagery+Products). Στην συνέχεια θα αυτοματοποιήσουμε την λήψη μιας σειράς εικόνων VIIRS για ένα συγκεκριμένο χρονικό διάστημα.

Το σενάριο R απαιτεί το πακέτο [gdalUtils](https://cran.r-project.org/web/packages/gdalUtils/index.html), ένα πακέτο "περιτυλίγµατος" (wrapper) για την βιβλιοθήκη GDAL, το οποίο φορτώνουμε στο περιβάλλον εργασίας της R:

    
```R
library(gdalUtils)
```

Ακολουθεί η συνάρτηση (function) που πραγματοποιεί την λήψη των δορυφορικών εικόνων. Δέχεται ως παραμέτρους την ημερομηνία λήψης του προϊόντος (αν δεν οριστεί από τον χρήστη ορίζεται ως προκαθορισμένη η τρέχουσα), το όνομα του προϊόντος, τον κωδικό προβολικού συστήματος κατά EPSG, τον κατάλογο που θέλουμε να αποθηκεύσουμε τα δεδομένα (προκαθορισμένος ο $HOME/gibs_downloads) και την γεωγραφική έκταση (extent) της περιοχής ενδιαφέροντος.

Το σενάριο χρησιμοποιεί την υπηρεσία Tiled Web Map Service μέσω της συνάρτησης gdal_translate του πακέτου gdalUtils. Ανάλογα με τις πληροφορίες που παρέχει ο χρήστης δημιουργεί δυναμικά ένα προσωρινό αρχείο XML το οποίο μεταβιβάζει σαν παράμετρο στην συνάρτηση [gdal_translate](http://www.gdal.org/gdal_translate.html). Επιστρέφει την διαδρομή της ληφθείσας εικόνας στο τοπικό σύστημα αρχείων του χρήστη.

    
```R
rGIBS<-function(date=Sys.Date(), EPSGCODE,PRODUCT,projwin, outputdir=file.path(Sys.getenv("HOME"),"gibs_downloads"),...){
  dir.create(outputdir, showWarnings = FALSE)
  setwd(outputdir)
  #generate xml
  makeXML <- function(date, EPSGCODE,PRODUCT){
    myxml<- sprintf('https://gibs.earthdata.nasa.gov/twms/epsg%s/best/twms.cgi?%s tileset%s',EPSGCODE, PRODUCT, date)
    tmp <- tempfile(fileext=".xml")
    fileConn<-file(tmp)
    writeLines(myxml, fileConn)
    close(fileConn)
    return(tmp)
  }
 
  infile<-makeXML(date,EPSGCODE,PRODUCT)
  outfile<-gsub(" ","_",(sprintf('%s_%s_EPSG%s.tif',PRODUCT,date,EPSGCODE)))
 
 
  gdal_translate(
    infile,
    outfile,
    projwin=projwin,
    verbose = T,
    ...
  )
 
 #delete temp file
  unlink(infile)
  message(sprintf("Image %s was saved in %s", outfile, outputdir))
  return (file.path(outputdir,outfile))
 
}


```

Έστω ότι στόχος είναι η λήψη της εικόνας του προϊόντος VIIRS DayNightBand για την 15η Αυγούστου του 2017 για την Ελλάδα. Ο χρήστης καλείται να παρέχει της πληροφορίες αυτές στην συνάρτηση rGIBS. Τις πληροφορίες αυτές θα τις ορίσουμε με την μορφή μεταβλητών:

```R
PRODUCT<-'VIIRS SNPP DayNightBand ENCC' # όνομα προϊόντος
EPSGCODE<-4326 #  EPSG κωδικός
date<-'2017-08-15' # ημερομηνία λήψης
projwin <- c(19.07, 42.16, 28.39, 34.5) # γεωγραφική έκταση (extent) της περιοχής μελέτης
```

Στην συνέχεια θα καλέσουμε την συνάρτηση rGIBS και θα προσαρτήσουμε την επιστραφείσα τιμή στην μεταβλητή image


```R
image<-rGIBS(date=date,EPSGCODE=EPSGCODE,PRODUCT=PRODUCT, projwin=projwin, of = "GTiff")
```

Η μεταβλητή image περιέχει την διαδρομή της εικόνας που μεταφορτώθηκε και μπορεί να χρησιμοποιηθεί σε άλλες συναρτήσεις.
Ας οπτικοποιήσουμε την εικόνα VIIRS που λάβαμε.


```R
plotRGB(stack(image))
```

![]({static}images/Rplot_Nighttime_Imagery-286x300.png)


Όπως προαναφέρθηκε στόχος του σεναρίου είναι η μαζική λήψη εικόνων ενός χρονικού διαστήματος σε ημερήσια βάση.
Ας δημιουργήσουμε μια λίστα με τις ημερομηνίες ανά ημέρα για το διάστημα 01/08/2017 ως 05/08/2017. Η λίστα δεν είναι απαραίτητο να περιλαμβάνει διαδοχικές ημερομηνίες.

```R
dates<-seq(as.Date("2017/08/01"), as.Date("2017/08/05"), "days")
```
Μπορούμε για κάθε στοιχείο της λίστας (κάθε ημερομηνία) να κατεβάσουμε την σχετική δορυφορική εικόνα VIIRS μέσω της συνάρτησης lapply:

```
myresults<-lapply(
dates,
rGIBS,
EPSGCODE=EPSGCODE,
PRODUCT=PRODUCT,
projwin=projwin,
of = "GTiff"
)
```

Η μεταβλητή *myresults* είναι λίστα η οποία περιλαμβάνει τις διαδρομές των αρχείων που μεταφορτώθηκαν ανά ημέρα.

Υποσημειώσεις:
1. Ο κώδικας της ανάρτησης είναι διαθέσιμος σε [github gist](https://gist.github.com/kokkytos/59421f6b62df85fecba05a0ffd0cfba1).
2. Το script έχει δοκιμαστεί επιτυχώς με GDAL 2.2.1. Έχει αποτύχει με GDAL 2.1.2
3. Δεν έχει δοκιμαστεί η λήψη άλλων προϊόντων.

---
Title: Τρέξτε το CoordGr σε Ubuntu
Date: 2010-08-3 00:00
Category: GIS
Tags: coordgr , wine
---

Ένα από τα πλέον χρήσιμα προγράμματα για όσους ασχολούνται με την μετατροπή συντεταγμένων στον ελλαδικό χώρο είναι το [CoordGr](https://dasologoi.gr/%CE%B1%CF%81%CF%87%CE%B5%CE%AF%CE%B1-downloads/download/7-%CE%B3%CE%B5%CE%BD%CE%B9%CE%BA%CE%AC/127-coord_gr) του Γιάννη Συγγρού. Το εν λόγω λογισμικό δεν θέλει συστάσεις μιας και είναι αρκετά διαδεδομένο λόγω της χρησιμότητας και μοναδικότητάς του.

Δυστυχώς το CoordGr είναι σχεδιασμένο ώστε να εκτελείται σε Windows. Παρόλα αυτά είναι δυνατόν να εκτελεστεί και σε linux με την βοήθεια του Wine.

Τα βήματα για την εγκατάσταση είναι τα εξής:

1. Αρχικά εγκαθιστούμε το Wine:


``` bash
sudo apt-get install wine
```

2. Για να μη πάρετε μήνυμα σφάλματος κατά την εγκατάσταση του Coordgr σαν το παρακάτω εγκαταστήστε το πακέτο *Visual Basic 5 runtime* για το Wine αφού πρώτα κατεβάσετε το *winetricks*

```bash 
wget http://winetricks.org/winetricks
sh winetricks vb5run
```

![]({static}images/dtaddin.png)


3. Στο επόμενο βήμα πρέπει να κατεβάσουμε, να αποσυμπιέσουμε και να εγκαταστήσουμε το πρόγραμμα:

```shell
wget http://web.auth.gr/e-topo/TOMEIS_INDEX/TOMEASA/Katsambalos/Give/coords_gr.zip
unzip coords_gr.zip -d CoordGr
cd CoordGr
wine setup.exe
```



4. Στην συνέχεια πρέπει να ενεργοποιήσουμε τα κατάλληλα locales για την ελληνική γλώσσα ώστε τα διάφορα μενού να εμφανιστούν στα ελληνικά:

```
sudo locale-gen el_GR.UTF-8
```

Σε περίπτωση που τα ελληνικά εξακολουθούν να μην εμφανίζονται ελέγξτε αν στο φάκελο των Fonts του Wine (`~/.wine/dosdevices/c:/windows/Fonts`) είναι οι απαραίτητες γραμματοσειρές και πιο συγκεκριμένα η γραμματοσειρά *sserifeg.fon* και *tahoma.ttf*. Αν δεν υπάρχουν τότε κάντε μια αναζήτηση στο διαδίκτυο.

5. Τέλος μπορούμε να εκκινήσουμε το πρόγραμμα, αφού πρώτα αλλάξουμε τον τρέχων κατάλογο στην τοποθεσία που είναι εγκατεστημένο το CoordGr στο Wine ως εξής:

```
cd "~/.wine/dosdevices/c:/Program Files/COORD_GR" env  LC_CTYPE=el_GR.UTF-8 wine "C:\Program Files\COORD_GR\COORD_GR.exe"
```

Αν κατά την εκκίνηση λάβετε ένα μήνυμα σφάλματος σαν το παρακάτω, το πρόβλημα βρίσκεται στα regional settings του wine.

![]({static}images/error_coordgr_regional_settings.png)



Για να το διορθώσετε δώστε:

```
wine regedit
```

και ορίστε την μεταβλητή `sDecimal = .` και την μεταβλητή `sThousand=,`

Εναλλακτικά μπορείτε να δημιουργήσετε έναν εκκινητή (Launcher) στην επιφάνεια εργασίας. Δημιουργήστε έναν νέο αρχείο με την ονομασία `COORD_GR.desktop` με τα παρακάτω δεδομένα στο `~/Desktop`:

```
[Desktop Entry]
Name=COORD_GR
Exec=env LC_CTYPE=el_GR.UTF-8  WINEPREFIX="/home/leonidas/.wine" wine start "C:\Program Files\COORD_GR\COORD_GR.exe"
Type=Application
Terminal=false
Path=/home/leonidas/.wine/dosdevices/c:/Program Files/COORD_GR
Icon=/home/leonidas/.wine/drive_c/Program Files/COORD_GR/coordsGR.ico
```
**Προσοχή**: Αντικαταστήστε το `/home/leonidas` με το δικό σας home directory.

Στην συνέχεια ορίστε το αρχείο εκτελέσιμο και ο εκκινητής είναι έτοιμος:
```
chmod +x COORD_GR.desktop
```

Επειδή το εικονίδιο της συντόμευσης δεν είναι ιδιαίτερα καλαίσθητο μπορεί να αντικατασταθεί με το παρακάτω:


<img src={static}images/coordgr.svg  width="100" height="100">

Αν όλα λειτούργησαν σωστά πρέπει να δείτε το μήνυμα

![]({static}images/coord2.jpg)

Και στην συνέχεια το περιβάλλον εργασίας του CoordGr

![]({static}images/coord1.jpg)



(*Η εγκατάσταση και εκτέλεση του CoordGr έγινε στην διανομή Ubuntu 10.04 LTS-Lucid Lynx με  Wine-1.1.42*)
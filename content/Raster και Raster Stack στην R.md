---
Title: Raster και Raster Stack στην R
Date: 2019-10-03 10:20
Category: Διάφορα
slug: raster-και-raster-stack-στην-r
Tags: R, raster, stack, NTL, DMSP-OLS, github
--- 

Η ανάρτηση αυτή περιλαμβάνει το περιεχόμενο από το workshop στο [FOSSCOMM 2019](https://2019.fosscomm.gr/) στην Λαμία. Για περισσότερες λεπτομέρειες ανατρέξτε στο [github repository](https://github.com/kokkytos/rworkshop).

Στόχος του εργαστηρίου είναι η εξοικείωση του χρήστη με το πακέτο [raster](https://cran.r-project.org/web/packages/raster/index.html) της R το οποίο προσφέρει την δυνατότητα ανάγνωσης ψηφιδωτών δεδομένων (raster) και επεξεργασίας τους ([crop](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/crop), [reclassify](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/reclassify), [reproject](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/projectRaster), [resample](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/resample) κτλ.).

Επιπλέον, θα επικεντρωθούμε στην κλάση [raster stack](https://web.archive.org/web/20211006131229/https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/stack) η οποία δημιουργεί συστοιχίες ψηφιδωτών δεδομένων, κατάλληλες για χρονοσειρές και πολυκαναλικές εικόνες.

Η διεξαγωγή του εργαστηρίου θα γίνει μέσω παραδειγμάτων και με την χρήση δεδομένων νυκτερινών φώτων [DMSP-OLS Nighttime Lights Time Series (Stable Lights Version 4)](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/stack). Θα προηγηθεί μια σύντομη παρουσίαση των βημάτων και της διαδικασίας ώστε οι χρήστες να αποκτήσουν μια σύντομη αλλά περιεκτική εικόνα του στόχου του εργαστηρίου και των δυνατοτητων που προσφέρει ο προγραμματισμός με την R.

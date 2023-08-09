---
Title: Raster και Raster Stack στην R
Date: 2019-10-03 10:20
Category: GIS
slug: raster-και-raster-stack-στην-r
Tags: R, raster, stack, NTL, DMSP-OLS, github
--- 

Η ανάρτηση αυτή περιλαμβάνει το περιεχόμενο από το workshop στο [FOSSCOMM 2019](https://2019.fosscomm.gr/) στην Λαμία. Για περισσότερες λεπτομέρειες ανατρέξτε στο [github repository](https://github.com/kokkytos/rworkshop).

Στόχος του εργαστηρίου είναι η εξοικείωση του χρήστη με το πακέτο [raster](https://cran.r-project.org/web/packages/raster/index.html) της R το οποίο προσφέρει την δυνατότητα ανάγνωσης ψηφιδωτών δεδομένων (raster) και επεξεργασίας τους ([crop](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/crop), [reclassify](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/reclassify), [reproject](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/projectRaster), [resample](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/resample) κτλ.).

Επιπλέον, θα επικεντρωθούμε στην κλάση [raster stack](https://web.archive.org/web/20211006131229/https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/stack) η οποία δημιουργεί συστοιχίες ψηφιδωτών δεδομένων, κατάλληλες για χρονοσειρές και πολυκαναλικές εικόνες.

Η διεξαγωγή του εργαστηρίου θα γίνει μέσω παραδειγμάτων και με την χρήση δεδομένων νυκτερινών φώτων [DMSP-OLS Nighttime Lights Time Series (Stable Lights Version 4)](https://www.rdocumentation.org/packages/raster/versions/2.9-5/topics/stack). Θα προηγηθεί μια σύντομη παρουσίαση των βημάτων και της διαδικασίας ώστε οι χρήστες να αποκτήσουν μια σύντομη αλλά περιεκτική εικόνα του στόχου του εργαστηρίου και των δυνατοτητων που προσφέρει ο προγραμματισμός με την R.

### Εγκατάσταση των απαραίτητων βιβλιοθηκών

```
install.packages(c("raster","ggplot2","rasterVis","rgdal","leaflet"),dependencies=T)
```

### Εισαγωγή των απαραίτητων βιβλιοθηκών


```
library(raster)
library(ggplot2)
library(rasterVis)
library(rgdal)
library(leaflet)
```



### Ορισμός Working directory
    setwd('/home/leonidas/Desktop/rworkshop')

### Επιβεβαίωση ποιο είναι το working directory
    getwd()

    ###### [1] "/home/leonidas/Desktop/rworkshop"

### Δημιουργία rasterStack Object

    myfiles <- list.files(path=file.path("data","dmsp_ols"),  pattern="*.stable_lights.tif$", full.names = TRUE)
    s <- raster::stack(myfiles)

### Οπτικοποίηση raster stack

    plot(s)

![]({static}images/index.png)


### Μερικές ιδιότητες του rasterStack

```
class(s) # ποιάς κλάσης ειναι object?
```

```
## [1] "RasterStack"
## attr(,"package")
## [1] "raster"
```


```
s@ncols  # πλήθος στηλών 

```


```
## [1] 1422
```

    
```
s@nrows  # πλήθος γραμμών
```

```
 ## [1] 1122
```

```
s@extent # όρια γεωγραφικής έκτασης
```

```
## class      : Extent 
## xmin       : 18.50417 
## xmax       : 30.35417 
## ymin       : 33.8625 
## ymax       : 43.2125
```

```
names(s)   # όνομα των επιμέρους raster
```

```
##  [1] "F101992.v4b_web.stable_lights" "F101993.v4b_web.stable_lights"
##  [3] "F101994.v4b_web.stable_lights" "F121994.v4b_web.stable_lights"
##  [5] "F121995.v4b_web.stable_lights" "F121996.v4b_web.stable_lights"
##  [7] "F121997.v4b_web.stable_lights" "F121998.v4b_web.stable_lights"
##  [9] "F121999.v4b_web.stable_lights" "F141997.v4b_web.stable_lights"
## [11] "F141998.v4b_web.stable_lights" "F141999.v4b_web.stable_lights"
## [13] "F142000.v4b_web.stable_lights" "F142001.v4b_web.stable_lights"
## [15] "F142002.v4b_web.stable_lights" "F142003.v4b_web.stable_lights"
## [17] "F152000.v4b_web.stable_lights" "F152001.v4b_web.stable_lights"
## [19] "F152002.v4b_web.stable_lights" "F152003.v4b_web.stable_lights"
## [21] "F152004.v4b_web.stable_lights" "F152005.v4b_web.stable_lights"
## [23] "F152006.v4b_web.stable_lights" "F152007.v4b_web.stable_lights"
## [25] "F162004.v4b_web.stable_lights" "F162005.v4b_web.stable_lights"
## [27] "F162006.v4b_web.stable_lights" "F162007.v4b_web.stable_lights"
## [29] "F162008.v4b_web.stable_lights" "F162009.v4b_web.stable_lights"
## [31] "F182010.v4d_web.stable_lights" "F182011.v4c_web.stable_lights"
## [33] "F182012.v4c_web.stable_lights" "F182013.v4c_web.stable_lights"
```


```
nlayers(s) # πλήθος raster
```

```
## [1] 34
```


```
res(s) # resolution των raster
```

```
## [1] 0.008333333 0.008333333
```

```
inMemory(s) # επαληθέουμε αν τα δεδομένα είναι στην μνήμη
```

```
## [1] FALSE
```

```
fromDisk(s) # επαληθέουμε αν τα δεδομένα είναι στον δίσκο
```


```
## [1] TRUE
```

### Υποσύνολο από layers του stack

    sub_s <- subset(s, c(1:5))
    plot(sub_s)


![]({static}images/index2.png)

    sub_s

```
## class      : RasterStack 
## dimensions : 1122, 1422, 1595484, 5  (nrow, ncol, ncell, nlayers)
## resolution : 0.008333333, 0.008333333  (x, y)
## extent     : 18.50417, 30.35417, 33.8625, 43.2125  (xmin, xmax, ymin, ymax)
## crs        : +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0 
## names      : F101992.v4b_web.stable_lights, F101993.v4b_web.stable_lights, F101994.v4b_web.stable_lights, F121994.v4b_web.stable_lights, F121995.v4b_web.stable_lights 
## min values :                             0,                             0,                             0,                             0,                             0 
## max values :                            63,                            63,                            63,                            63,                            63
```

    rm(sub_s) #διαγραφή object από το περιβάλλον
    #sub_s


### Αποκοπή του rasterStack στα όρια του Ν. Μαγνησίας

#### Ανάγνωση διανυσματικών δεδομένων geopackage

```
pe <- readOGR(file.path("data","per_enot", "pe.gpkg"), "pe")
```

```
## OGR data source with driver: GPKG 
## Source: "/home/leonidas/Desktop/rworkshop/data/per_enot/pe.gpkg", layer: "pe"
## with 75 features
## It has 5 fields
```

```
# ?readOGR
crs(pe)
```

```

## CRS arguments:
##  +proj=tmerc +lat_0=0 +lon_0=24 +k=0.9996 +x_0=500000 +y_0=0
## +ellps=GRS80 +towgs84=-199.87,74.79,246.62,0,0,0,0 +units=m
## +no_defs

```
```
plot(pe)
```

![]({static}images/pe_gpkg.png)


### Reprojection σε WGS’84 και επιλογή του Ν. Μαγνησίας


```
pe_wgs <- sp::spTransform(pe, CRS("+init=epsg:4326"))
crs(pe_wgs)
```
```
## CRS arguments:
##  +init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84
## +towgs84=0,0,0
```
```
View(pe_wgs@data)
```
```
magnisia <- subset(pe_wgs, KALCODE==c(24)) #επιλογή του Ν. Μαγνησίας
plot(magnisia)
```


![]({static}images/magnisia.png)

```
print(magnisia)
```

```
## class       : SpatialPolygonsDataFrame 
## features    : 1 
## extent      : 22.49044, 23.35152, 38.96959, 39.60304  (xmin, xmax, ymin, ymax)
## crs         : +init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0 
## variables   : 5
## names       : OBJECTID, KALCODE,                        LEKTIKO,    SHAPE_Leng,    SHAPE_Area 
## value       :       24,      24, ΠΕΡΙΦΕΡΕΙΑΚΗ ΕΝΟΤΗΤΑ ΜΑΓΝΗΣΙΑΣ, 553550.759122, 2364238989.84
```

Ορισμός των ορίων της περιοχής μέσω της δημιουργίας ενός extent object


```
#ext<-extent(22.61,24.34,37.33,38.69) #Attiki
ext <- raster::extent(magnisia)
str(ext)
```

```
## Formal class 'Extent' [package "raster"] with 4 slots
##   ..@ xmin: num 22.5
##   ..@ xmax: num 23.4
##   ..@ ymin: num 39
##   ..@ ymax: num 39.6
```

```
plot(pe_wgs)
plot(as(ext, 'SpatialPolygons'),col=rgb(1, 0, 0, alpha=0.5), add=T)
```
![]({static}images/greece_magnisia.png)


```
s <-crop(s, ext) # εδώ διατηρεί το αρχικό resolution και προσαρμόζει τα άκρα, επίσης μετατρέπει το stack σε brick

inMemory(s) # επαληθέουμε αν τα δεδομένα είναι στην μνήμη
```

```
## [1] FALSE
```

```
fromDisk(s) # επαληθέουμε αν τα δεδομένα είναι στον δίσκο   
```

```
## [1] TRUE
```

```
s@extent
```

```
## class      : Extent 
## xmin       : 22.4875 
## xmax       : 23.35417 
## ymin       : 38.97083 
## ymax       : 39.60417
```

```
names(s)
```

```
##  [1] "F101992.v4b_web.stable_lights" "F101993.v4b_web.stable_lights"
##  [3] "F101994.v4b_web.stable_lights" "F121994.v4b_web.stable_lights"
##  [5] "F121995.v4b_web.stable_lights" "F121996.v4b_web.stable_lights"
##  [7] "F121997.v4b_web.stable_lights" "F121998.v4b_web.stable_lights"
##  [9] "F121999.v4b_web.stable_lights" "F141997.v4b_web.stable_lights"
## [11] "F141998.v4b_web.stable_lights" "F141999.v4b_web.stable_lights"
## [13] "F142000.v4b_web.stable_lights" "F142001.v4b_web.stable_lights"
## [15] "F142002.v4b_web.stable_lights" "F142003.v4b_web.stable_lights"
## [17] "F152000.v4b_web.stable_lights" "F152001.v4b_web.stable_lights"
## [19] "F152002.v4b_web.stable_lights" "F152003.v4b_web.stable_lights"
## [21] "F152004.v4b_web.stable_lights" "F152005.v4b_web.stable_lights"
## [23] "F152006.v4b_web.stable_lights" "F152007.v4b_web.stable_lights"
## [25] "F162004.v4b_web.stable_lights" "F162005.v4b_web.stable_lights"
## [27] "F162006.v4b_web.stable_lights" "F162007.v4b_web.stable_lights"
## [29] "F162008.v4b_web.stable_lights" "F162009.v4b_web.stable_lights"
## [31] "F182010.v4d_web.stable_lights" "F182011.v4c_web.stable_lights"
## [33] "F182012.v4c_web.stable_lights" "F182013.v4c_web.stable_lights"
```

```
res(s)
```

```
## [1] 0.008333333 0.008333333
```

```
nlayers(s)
```

```
## [1] 34
```

### Προβολή στο ΕΓΣΑ’ 87

```
greekgrid <- "+proj=tmerc +lat_0=0 +lon_0=24 +k=0.9996 +x_0=500000 +y_0=0 +ellps=GRS80 +towgs84=-199.87,74.79,246.62,0,0,0,0 +units=m +no_defs"

s <- projectRaster(from=s, res=1000, crs=greekgrid, method="ngb") 
```

```
plot(s[[1]])
```

![]({static}images/magnisia_ntl.png)


Προβολή σε χάρτη leaflet

```
leaflet() %>% 
  addTiles() %>%
  addRasterImage(s[[1]], opacity = 0.6)
```


### Compare rasters

```

compareRaster(s[[1]], s[[15]], extent=TRUE )
```


```
## [1] TRUE
```


```
compareRaster(s[[1]], s[[15]], rowcol=TRUE )
```


```
## [1] TRUE
```


```
compareRaster(s[[1]], s[[15]], crs=TRUE)
```


```
## [1] TRUE
```

```
compareRaster(s[[1]], s[[15]], res=TRUE)
```

```
## [1] TRUE
```

```
compareRaster(s[[1]], s[[15]], orig=TRUE)
```


```
## [1] TRUE
```


```
compareRaster(s[[1]], s[[15]], values=T,stopiffalse = F)
```

```
## [1] FALSE
```

# Resample rasters


```
#Δημιουργία νεόυ raster 
grid <- raster()
extent(grid) <- extent(s)
res(grid)=c(2000,2000)

resampled_s <- resample(s, grid, method = "ngb")
res(s)
```
```
## [1] 1000 1000
```
```
res(resampled_s)
```
```
## [1] 2000 2000
```

### Μέσος όρος ανά έτος με την χρήση stackApply

```
names(s)
```

```
##  [1] "F101992.v4b_web.stable_lights" "F101993.v4b_web.stable_lights"
##  [3] "F101994.v4b_web.stable_lights" "F121994.v4b_web.stable_lights"
##  [5] "F121995.v4b_web.stable_lights" "F121996.v4b_web.stable_lights"
##  [7] "F121997.v4b_web.stable_lights" "F121998.v4b_web.stable_lights"
##  [9] "F121999.v4b_web.stable_lights" "F141997.v4b_web.stable_lights"
## [11] "F141998.v4b_web.stable_lights" "F141999.v4b_web.stable_lights"
## [13] "F142000.v4b_web.stable_lights" "F142001.v4b_web.stable_lights"
## [15] "F142002.v4b_web.stable_lights" "F142003.v4b_web.stable_lights"
## [17] "F152000.v4b_web.stable_lights" "F152001.v4b_web.stable_lights"
## [19] "F152002.v4b_web.stable_lights" "F152003.v4b_web.stable_lights"
## [21] "F152004.v4b_web.stable_lights" "F152005.v4b_web.stable_lights"
## [23] "F152006.v4b_web.stable_lights" "F152007.v4b_web.stable_lights"
## [25] "F162004.v4b_web.stable_lights" "F162005.v4b_web.stable_lights"
## [27] "F162006.v4b_web.stable_lights" "F162007.v4b_web.stable_lights"
## [29] "F162008.v4b_web.stable_lights" "F162009.v4b_web.stable_lights"
## [31] "F182010.v4d_web.stable_lights" "F182011.v4c_web.stable_lights"
## [33] "F182012.v4c_web.stable_lights" "F182013.v4c_web.stable_lights"
```

```
years <- substr(names(s),4,7)


#Α' τρόπος
indices <- c(1,2,3,3,4,5,6,7,8,6,7,8,9,10,11,12,9,10,11,12,13,14,15,16,13,14,15,16,17,18,19,20,21,22)

# B' τρόπος
indices <- factor(years)
levels(indices) <-1:length(levels(indices))

nlayers(s)
```

```
## [1] 34
```

```
s<-stackApply(s, as.integer(indices), fun = mean, na.rm = TRUE)
nlayers(s)
```

```
## [1] 22
```

```
names(s) <-unique(years)
```


### Reclassify τιμών


Ορίζουμε όσες τιμές στο raster είναι μικρότερες/ίσες του 6 στα raster layers σε NA

#### 1^ος^ τρόπος


```
rc1 <- s

rc1[rc1<=6] <- NA #δεν ειναι memory safe

```

#### 2^ος^ τρόπος


```
s_calc <- raster::calc(s, fun=function(x){x[x<=6]<-NA; return(x)}) 
```



#### 3^ος^ τρόπος


rc2 <- raster::reclassify(s, c(-Inf,6,NA))

plot(s[[11]]) # plot  ενδέκατο raster από το αρχικό stac


![]({static}images/magnisia_ntl2.png)


```
plot(s_calc[[11]]) #plot από το αρχικό stack, από το φιλτραρισμένο, εναλλακτικά plot(s_calc$index_1992)
```

![]({static}images/magnisia_ntl3.png)


```
compareRaster(rc1, rc2, values=T)
```

```
## [1] TRUE
```

```
compareRaster(s_calc,rc2, values=T)
```

```
## [1] TRUE
```

```
compareRaster(s_calc,s, values=T,stopiffalse = F)
```
```
## [1] FALSE
```

### Οπτικοποίηση με το levelplot

    rasterVis::levelplot(s_calc) # προσοχή μπορεί να αργήσει αν ειναι πολλά raster


![]({static}images/levelplot.png)


```
names(s)
```

```
##  [1] "X1992" "X1993" "X1994" "X1995" "X1996" "X1997" "X1998" "X1999"
##  [9] "X2000" "X2001" "X2002" "X2003" "X2004" "X2005" "X2006" "X2007"
## [17] "X2008" "X2009" "X2010" "X2011" "X2012" "X2013"
```

```
(years <- substring(names(s),2))
```

```
##  [1] "1992" "1993" "1994" "1995" "1996" "1997" "1998" "1999" "2000" "2001"
## [11] "2002" "2003" "2004" "2005" "2006" "2007" "2008" "2009" "2010" "2011"
## [21] "2012" "2013"
```

```
rasterVis::levelplot(s_calc,main="Raster δεδομενα DMSP/OLS για την Μαγνησία, 1992-2013", 

                     scales=list(y=list(draw=FALSE),
                                 x=list(draw=FALSE)),  
                     names.attr=years,
                     colorkey=NULL)

```
![]({static}images/levelplot2.png)


# Υπολογισμός SoL μέσω cellStats


```
SoL <- cellStats(s_calc, stat='sum', na.rm=TRUE)

df<-data.frame(SoL=SoL, Year=as.integer(years) )#δημιουργία dataframe
write.csv(df,file.path('output','SoL.csv')) # εγγραφή σε csv
```

### Οπτικοποίηση δεδομένων SoL σε γράφημα

#### Γράφημα με τυπικά εργαλεία plot της R

```
#jpeg('SoL.jpg')
#dev.off
plot(x=df$Year,
       y=df$SoL, 
       type='l',
       xlab="Year", 
       ylab="Sum of Lights (SoL)",
       main='SoL for Magnesia',xaxt="n")
  axis(1, at=df$Year,cex.axis=0.8, las=2)
points(x=df$Year,y=df$SoL)
```
![]({static}images/sol_magnisia.png)


#### Γράφημα με ggplot

```
ggplot2::ggplot(data=df, aes(x=Year,y=SoL))+
  geom_line()+
  geom_point()+
  ggtitle("Sum of Lights (SoL) for Magnesia")+ 
  scale_x_continuous("Years", labels = as.character(df$Year), breaks = df$Year)+
  theme(plot.title = element_text(hjust = 0.5))+theme(text = element_text(size=14),
                                                      axis.text.x = element_text(angle=90)) 
```

![]({static}images/sol_magnisia2.png)

### Αποθήκευση γραφήματος

```
ggplot2::ggsave(file.path("output",'SoL.png'), plot = last_plot(), device = "png", 
       scale = 1, width = 10, height = 5, units = c("in", "cm", "mm"),
       dpi = 300, limitsize = TRUE)
```

### Αποθήκευση των rasterStack σαν ξεχωριστά αρχεία geotiff

```
# προσοχή στο data(t)ype όχι data(T)ype
raster::writeRaster(s_calc, filename=file.path("output",years), bylayer=TRUE,datatype="INT1U", options="COMPRESS=LZW", format="GTiff",overwrite=TRUE)
```











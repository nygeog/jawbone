dm <- read.csv("/Volumes/Echo/Dropbox/GIS/Data/Monitoring/JawboneUp/2013.csv",header=T) 
#dm <- read.table(text = Lines, header = TRUE)
dm$DATE <- as.Date(dm$DATE, "%Y %m %d")
plot(m_steps ~ DATE, dm, xaxt = "n", type = "l")
axis(1, dm$DATE, , cex.axis = .7)



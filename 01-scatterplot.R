df = read.csv("data/jawbone.csv")


df<-df[apply(df, 1, function(x) sum(is.na(x)))<6,]
rownames(df)<-c(1:nrow(df))

names(df)

df$DATE = strptime(df$DATE, "%Y%m%d")

plot(df$DATE,df$m_steps,xlab="Time", ylab="Steps", main="Steps - Time", col="blue")
lines(lowess(df$DATE,df$m_steps), col="red", lwd=3)
axis.Date(1,at=df$DATE,labels=format(df$DATE,"%m"),las=2)


dev.copy(png,filename="images/jawbone.png");
dev.off ();




#Here's the ggplot code andrew showed. 

#library(ggplot2)
#head(df)

#df$group<-sample(c(0,1), size=nrow(df), replace=T)

#ggplot(df, aes(x=DATE, y=m_steps, color=m_distance))+geom_point()+
  #facet_grid(~group)

df = read.csv("/Users/danielmsheehan/GitHub/jawbone/data/jawbone.csv")

names(df)

df$DATE = strptime(df$DATE, "%Y%m%d")

head(df, n=10)


plot(df$DATE,df$m_steps,xlab="Time", ylab="Steps", main="Steps - Time", col="blue")
axis.Date(1,at=df$DATE,labels=format(df$DATE,"%m"),las=2)
#scatter.smooth(x=df$DATE, y=df$m_steps) #if this is uncommented it shows the scatter but for some reason gets rid of the correct labels, it might be changing them to epoch time ie. 1970. 
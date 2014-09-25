
#Jawbone UP Plot


![jawbone steps](images/jawbone.pdf)


	df = read.csv("/Users/danielmsheehan/GitHub/jawbone/data/jawbone.csv")

	names(df)

	df$DATE = strptime(df$DATE, "%Y%m%d")

	head(df, n=10)


	plot(df$DATE,df$m_steps,xlab="Time", ylab="Steps", main="Steps - Time", col="blue")
	axis.Date(1,at=df$DATE,labels=format(df$DATE,"%m"),las=2)
	
	#Here's my problem
	#scatter.smooth(x=df$DATE, y=df$m_steps) 
	#if this is uncommented
	 it shows the scatter but for some reason gets rid of the correct labels, it might be changing them to epoch time ie. 1970. 






##First step
In Python, with pandas,

	import pandas as pd

	df2013 = pd.read_csv('/Users/danielmsheehan/Dropbox/GIS/Data/	Monitoring/JawboneUp/2013.csv')
	df2014 = pd.read_csv('/Users/danielmsheehan/Dropbox/GIS/Data/	Monitoring/JawboneUp/2014.csv')

	df = df2013.append(df2014)

	df = df[['DATE','m_active_time','m_distance','m_inactive_time','m_lcat','m_lcit','m_steps']]

	df.to_csv('/Users/danielmsheehan/GitHub/jawbone/data/	jawbone.csv',index=False)
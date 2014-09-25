import shutil

weather = '/Users/danielmsheehan/GitHub/python/weather_data/nyc_weather_data_'
up      = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/' 
for year in range(2013,2015):
	year = str(year)
	shutil.copy2(weather+year+'.csv', up+'weather'+year+'.csv')
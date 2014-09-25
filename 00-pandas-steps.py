import pandas as pd

df2013 = pd.read_csv('/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/2013.csv')
df2014 = pd.read_csv('/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/2014.csv')

df = df2013.append(df2014)

df = df[['DATE','m_active_time','m_distance','m_inactive_time','m_lcat','m_lcit','m_steps']]

df.to_csv('/Users/danielmsheehan/GitHub/jawbone/data/jawbone.csv',index=False)
import pandas as pd
import numpy as np

dict1 = {
    "Name": ['Himanshu', 'Shashank', 'Aman', 'Rohan', 'Sandeep'],
    "GPA": [8.3, 8.5, 8.0, 8.7, 9.0],
    "City": ['jabalpur', 'Ara', 'Eeta', 'ghazipur', 'Ghazipur']
}

df = pd.DataFrame(dict1)

df

df.to_csv('Freinds.csv')

df.to_csv('freinds_no_index.csv',index=False)

df.head(2)

df.tail(4)

df.describe()

info=pd.read_csv('trian.csv')

info

info[0]=11098

info

info.index=['First','Second','Third'] # This chnages the index like it was 0,1,2 now it is first 

info

ser = pd.Series(np.random.rand(34))

ser

newDef=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))

newDef


newDef[0][0]='First'

newDef.dtypes

newDef

newDef.to_numpy()

newDef[0][0]=0.2221

newDef

newDef.T # Transpose 

# to sort index in descendind as already in ascending
newDef.sort_index(axis=0,ascending=False) 
#axis=0 is a row
#axis=1 is column

type(newDef[0]) # This shows that a data frame is made up of series of dataframe

newdf=newDef # now newdf is view of newDef and if you change something in newdf their will be change in newDef

newdefCopy=newDef.copy()

newDef.loc[0,0]=55 # beter to use for someReason

newDef

newDef.columns=list("abcde")

newDef.head(3)

#To drop something write below snippet
#newDef.drop(0,axis=1) # removes from column


newDef.loc[[1,2],['C','D']]

newDef.loc[(newDef['a']<0.3)]


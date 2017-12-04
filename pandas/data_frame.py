import pandas as pd 

data={
     'students':['John','Mathew','Jonah'],
     'maths':[88,78,77],
     'science':[77,78,99]
 }

info=pd.DataFrame(data,columns=['students','maths','science'])
print(info)

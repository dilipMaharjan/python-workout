import pandas as pd

# list series
list=[1,2,3,4,'hi','hello']
s=pd.Series(list)
print(s)
print(s[0])

# dictionary series

dict={"one":1,"two":2,"three":3}
s=pd.Series(dict)
print(dict["two"])
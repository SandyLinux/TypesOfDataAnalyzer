
import pandas as pd

def get(n):
    for i in range(n):
        yield i

print (
    list(set(get(10)))[1]
    )

a=[1,3,4,5]
print(list(x*3 for x in a))

mydict = {'a':2,'b':4}
yourdict = mydict

print(yourdict)

hisdict = { k:v for (k,v) in zip(mydict.keys(),mydict.values())}
print(mydict==yourdict)
print(mydict == hisdict)
data = [1,2,3,5]
print(pd.Series(data))
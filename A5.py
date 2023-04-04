#In dumps function what are the parameters that we have and what do they do, explain with small program
import json
x={
    "Name": "Ankita",
    "Age": 23,
    "number":"831987"
  }
print(json.dumps(x))
print(type(json.dumps(x)))

#Parameters

'''sort_keys:- The sort_keys parameter to specify if the result should be sorted or not
   Indent:- The indent parameter to define the numbers of indents'''
print(json.dumps(x, indent=2, sort_keys=True))

#How can we raise an exception
'''The raise keyword is used to raise an exception.'''
x = -1

if x < 0:
  raise Exception("Sorry,  number is below zero")

#WAP on normal list comprehension and  another program on list comprehension by using conditions 
#with condition
names=["ankita","riya","mehak","pallavi","hirman"]
newlist=["simi" for x in names]
print(newlist)

#conditionless
names=["ankita","riya","mehak","pallavi","hirman"]
newlist=[x.upper() for x in names]
print(newlist)

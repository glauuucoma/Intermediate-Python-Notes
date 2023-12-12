#Tuple: ordered, immutable, allows duplicate elements
#The main Difference between tuples and lists is that tuples are immutable
#Tuples are much faster than arrays

mytuple = ("Max", 4, 5,5) # or you can just write = "Max",4,5
# If you want to create tuple that holds one element then add coma in the end
# mytuple = ("Max",)

#To turn array into tuple
toTuple = tuple([1,2,3,4,5])
#To turn tuple into array
toArray = list(toTuple)

#To count number of specific element that appears in tuple
print(mytuple.count(5)) # 2
#To find index of the first element
print(mytuple.index(4)) # 1 (second element)

#Reverse tuple
reversedTuple = mytuple[::-1]
print(reversedTuple)

#Assign each var to each tuple value
name,age,myId,workExp = mytuple


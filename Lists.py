#Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", True, 5, 10]
print(mylist[0])
print(mylist[-2])

print("\n")
for i in mylist: # Iterate thru all elements
	print(i)

if "banana" in mylist:
	print("yes, it's in the list")
else:
	print("it's not")

print(len(mylist), " elements") # Print length

mylist.append("New item") # Append item in the end

mylist.pop() # Remove last item

mylist.remove("cherry") # Remove specific item

# mylist.clear() # Delete all items

mylist.reverse() # Reverse the list

# sortedlist = sorted(mylist) # Create new sorted list (Working only on strings or numbers)

# You can also easily concantenate lists

#Slicing

print([1,2,3,4,5,6][1:3]) # Choose elements from 2 to 4
print([1,2,3,4,5,6][:3])
print([1,2,3,4,5,6][3:])
print([1,2,3,4,5,6][::-1]) # To reverse

#If you want to actually copy the list and not create pointer

#Dont do this

#list1 = list2

# Because if you would change list2, list1 will change as well

#Do this

#list1 = list2.copy()
# or list1 = list(list2)
# or list1 = list2[:]

#To copy list but apply certain math operations

mylist10 = [1,2,3,4,5,6,7,8]

b = [i*i for i in mylist10]

print(b) #[1, 4, 9, 16, 25, 36, 49, 64]

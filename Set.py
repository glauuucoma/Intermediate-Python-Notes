#Sets: unordered, mutable, no duplicates

# We put single elements separeted by comma, difference with dicts
myset = {1,2,3,5}
newSet = set()

# Add elements

myset.add(1)

# Remove elements

myset.remove(1)

# Discard

myset.discard(1) # Will not throw error like remove method if elements is not found

# Clear set

#myset.clear() - Deletes all the elements

# Pop element (remove first elm)

myset.pop()

# Check if element in set

if 3 in myset:
	print("Yes")
else:
	print("No")

# Combine elements wihout duplication

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
u = odds.union(evens)
print(u)

# intersection(): take elements that are in both sets
i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)


# Difference of sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference() : returns a set with all the elements from the setA that are not in setB.
diff_set = setA.difference(setB)
print(diff_set)

# A.difference(B) is not the same as B.difference(A)
diff_set = setB.difference(setA)
print(diff_set)

# symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
diff_set = setA.symmetric_difference(setB)
print(diff_set)

# A.symmetric_difference(B) = B.symmetric_difference(A)
diff_set = setB.symmetric_difference(setA)
print(diff_set)
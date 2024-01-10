# Strings: ordered, immutable, text representation

word = "KittyKittenCat"
char = word[-1] # Access character

print(char)

# Strings are immutable, so you can't character in a word

substring = word[0:5]
print(substring)

# Takes every second character

even = word[::2]

# Reverse string

reverseWord = word[::-1]
print(reverseWord)

my_string = "     Hello World "

# remove white space
my_string = my_string.strip()
print(my_string)

# number of characters
print(len(my_string))

# Upper and lower cases
print(my_string.upper())
print(my_string.lower())

# startswith and endswith
print("hello".startswith("he"))
print("hello".endswith("llo"))

# find first index of a given substring, -1 otherwise
print("Hello".find("o"))

# count number of characters/substrings
print("Hello".count("e"))

# replace a substring with another string (only if the substring is found)
# Note: The original string stays the same
message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)

# Formatting string

# %, .format, f-strings

var = "Tom"
mystring = "the variable is %s" % var # Old formatting style
mystring1= "the variable is {:.2f}".format(var)
mystring2= f"dasdasd {var}"
# Collections: Counter, namedtuple, OrderedDict, defaultDict, deque

from collections import Counter # Counts how many times each character appeared
a = "aaaaaabbbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)) # Show the most common types

from collections import namedtuple
Point = namedtuple("Point", "x,y") # This will create class Point with two fields
pt = Point(1, -4)
print(pt.x, pt.y)

from collections import OrderedDict # Like dict, but remember the order of inserted elements
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 1
ordered_dict["c"] = 1
ordered_dict["d"] = 1
ordered_dict["e"] = 1
print(ordered_dict)

from collections import defaultdict # Creates a dict that can contain default value
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d["c"]) # Will return 0, because it was set ti be a default value

from collections import deque # It can be used to remove elements from both ends
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.rotate(-1)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

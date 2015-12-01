# Mathematical operations always return Floating point numbers

17 / 3  # => 5.666...
17 // 3 # => 5
17 % 3  # => 2

2 ** 3 # => 8

list = [1,2,3,4,5]
list[0] # => 1
len(list) # => 5
list[0:2] # => [1,2] The index 2 is not included, but the 0 is
list[:2] # => [1,2]
list[1:] # => [2,3,4,5]

list.append(10)
list # => [1,2,3,4,5,10]
list.remove(10)
list # => [1,2,3,4,5]
del(list[0])
list # => [2,3,4,5]

list_2 = [1,2,3]
list + list_2 # => [1,2,3,4,5,1,2,3]

# Given a base-string and a sub-string, find the number of different ways the sub-string appears in the base-string

'''
find number of ways have a substring inside a string

be careful! This isn't as simple as s.count(sub_str)
since if have multiple places can appear with overlap, then count twice!

assume sub_str is not empty

"abc", "a"
> 1
"abc", "c"
> 1
"", "a"
> 0
"aaa", "a"
> 3
"aaa", "aa"
> 2
"aaa", "aaa"
> 1
'''

# For example, in the base-string  `aaa`, the sub-string  `aa`  appears twice and in the base-string  `aa`, the sub-string  `aaa`  appears 0 times.

s = "|**|*|*|**||***||"
p = s.split("|")
s = 0
for i in range(0, len(p), 2):
    s += p[i].count("*")
print(s)

# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words,
# the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
#
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
#
# # Note that each '|' will belong to exactly one pair.

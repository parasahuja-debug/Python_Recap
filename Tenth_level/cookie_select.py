# Problem: Each child i has a greed factor g[i] — 
# the minimum cookie size they'll be content with. 
# Each cookie j has a size s[j]. A cookie can satisfy a child only if s[j] >= g[i]. 
# Each child gets at most one cookie. 
# Maximize the number of content children.

def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    
    child = 0
    cookie = 0
    
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1  # this child is satisfied
        cookie += 1      # move to next cookie regardless
    
    return child

# Input: g = [1,2,3], s = [1,1]
from collections import Counter
def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)         # counts of chars we need t is ABC , need - {'A':1,'B':1,'C':1}

    missing = len(t)    # number of chars still missing in window , all characters are missing
    left = 0            #start from extreme left
    min_len = float("inf") #min length is infinite at start
    min_start = 0 #minstart is extreme left

    # iterate right pointer through s
    for right, ch in enumerate(s):
        # if ch is needed, decrement missing when it's useful
        if need[ch] > 0: #need is {'A':1,'B':1,'C':1} - ch is part of ADOBECODEBANC, need['A']
            missing -= 1 #i have found 1
        need[ch] -= 1  # use one ch (could go negative for excess), at first need - {'A':0,'B':1,'C':1}

        # when no missing chars, we have a valid window; try to shrink from left
        while missing == 0: #only runs when the whole length is met
            cur_len = right - left + 1 #current length
            if cur_len < min_len: #current length is smal
                min_len = cur_len #min is ccurrent
                min_start = left #min start changes to left

            # try to remove s[left] from window
            need[s[left]] += 1 # s[left] - 'A' , need A->+1 so need - {'A':1,'B':0,'C':0} 
            # if after increasing need[s[left]] it's >0, we lost a required char
            if need[s[left]] > 0: #now the i have lost the data
                missing += 1 #missing becomes 1 and while loop ends
            left += 1 #left is moved again

    return "" if min_len == float("inf") else s[min_start:min_start + min_len]

# Example
print("2) Minimum Window Substring")
print(min_window("ADOBECODEBANC", "ABC"))  # expected "BANC"
print()
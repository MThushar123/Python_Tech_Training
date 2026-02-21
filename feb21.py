def min_distance(s1, s2):
    m, n = len(s1), len(s2)
    
    # If one string empty - delete/insert all chars
    if m == 0: return n
    if n == 0: return m
    
    # Use smaller string for space optimization
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
    
    prev = list(range(n + 1))  # Row 0: [0,1,2,...,n]
    
    for i in range(1, m + 1):
        curr = [i]  # First column always i
        
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                # Match → diagonal (no cost)
                cost = prev[j-1]
            else:
                # Min of replace/insert/delete
                cost = 1 + min(prev[j-1], prev[j], curr[j-1])
            
            curr.append(cost)
        
        prev = curr
    
    return prev[n]

print("String 1: ", end="")
s1 = input().strip()
print("String 2: ", end="")
s2 = input().strip()
print(f"Min edits: {min_distance(s1, s2)}")

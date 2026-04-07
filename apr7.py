def find_content_children(g, s):

    g.sort()  
    s.sort()  
    
    child = 0  
    cookie = 0  
    content = 0
    
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            content += 1
            child += 1  
        cookie += 1  
    return content

print(" Assign Cookies")
print("Children greed factors:")
g = list(map(int, input().split()))
print("Cookie sizes:")
s = list(map(int, input().split()))

result = find_content_children(g, s)
print(f"\n Children: {g}")
print(f" Cookies: {s}")
print(f" Content children: {result}")
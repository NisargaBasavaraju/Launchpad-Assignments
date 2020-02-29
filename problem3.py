result = []
a = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
search_element=2
for i in range(len(a)):
    if a[i]==search_element:
        result.append(i)
print(result)
    

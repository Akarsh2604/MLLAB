def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
lst=[]
n=int(input("enter number of elements in the list:"))
for i in range(0,n+1):
    ele=int(input("enter list element:"))
    lst.append(ele)


lst2=[]
p=int(input("enter number of elements in the list:"))
for j in range(0,p+1):
    ele=int(input("enter list element:"))
    lst2.append(ele)

    
x= common_elements(lst,lst2)
print("The common elements are:",x)




    

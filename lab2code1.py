print("Enter string of your choice")
s = str(input("enter ur string in lowercase:"))
c=0
v=0
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
      v=v+1
    else:
        c=c+1

print("The number of vowels are:",+v)
print("The numner of consonants are:",+c)
        
        

# to capitlize the string


s=input('enter a statement:')

s=s.title() # frist letter capitlize
s=s.split()# seperate each letter
string=""
for i in s:
    string+=i[:-1]+i[-1].upper()+" " # ex akash -1
print(string)
statement=input('Enter a statement:')
string=statement.lower()
print(string)
count=0
list=['a','e','i','o','u']
for char in string:
    if char in list:
        count+=1
        print('enter a vowel: ',(count))
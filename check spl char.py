import re
def check_splcharacter(test):
    # Make own character set and pass 
    # this as argument in compile method
 
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
 
    # Pass the string in search 
    # method of regex object.
 
    if(string_check.search(test) == None):
        print("String does not contain Special Characters.",) 
    else: 
        print("String contains Special Characters.")

s=(input('enter a string:'))
print(s)
print(check_splcharacter(s))




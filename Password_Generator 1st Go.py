import random

#A function to shuffle all the characters of a string
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,99)) #Generate random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,99)) #Generate random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(65,99)) #Generate random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(65,99)) #Generate random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(65,99)) #Generate random Uppercase letter (based on ASCII code)
uppercaseLetter6=chr(random.randint(65,99)) #Generate random Uppercase letter (based on ASCII code)

lowercaseLetter1=chr(random.randint(65,99))
lowercaseLetter2=chr(random.randint(65,99))
lowercaseLetter3=chr(random.randint(65,99))
lowercaseLetter4=chr(random.randint(65,99))
lowercaseLetter5=chr(random.randint(65,99))
lowercaseLetter6=chr(random.randint(65,99))

#Generate more characters here
#...

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + for lowercaseLetter1 in range (0,5): # + ...
password = shuffle(password)
 
 #Output
print(password)
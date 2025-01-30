a = "Hello " ; b = "World. " ; c = "This is Kerem !" 
print(a + b + c)

x = 5 ; y = 10
print (x * y)

k = len(a + b + c)
print(k)

upperTest = "i need to convert this to uppers."

if(upperTest.islower):
    print("This sentence is upper")
print(upperTest.upper())


lowerTest = "I NEED TO CONVERT THIS TO LOWERS."

if(lowerTest.isupper()):
    print("The sentence is lower")
print(lowerTest.lower())

replaceTest = " Kerem Erkut "
replaceTestReplaced = replaceTest.replace("e","a")
print(replaceTestReplaced)

replaceTestStripted = replaceTestReplaced.strip()
print(replaceTestStripted)
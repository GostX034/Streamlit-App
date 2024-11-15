def prompt():
    message = input("What is your lucky number?")
    final_number = int(message)
    return final_number


luckynumber = prompt()

if luckynumber < 10 :
    print ("Interesting")
else :
    print("Number is too big to be a lucky number ")

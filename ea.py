
from time import sleep
while True :
    q1 = input('are you autistic? ')
    match q1:
        case 'yes':
            print('yep you are')
        case 'no':
            print('not true')
        case 'nigger':
            try:
                pcr = input('what percentage?')
                pcre = float(pcr)
                if pcre >= 70 :
                    print("i have called the police on you")
                    sleep(2)
                    print("You better run my nigga")
                    sleep(1)
                    y = input("Why are you still here")
                    if y ==  "i am not in danger" or "this is not true ":
                             print("This is very true")
                             sleep(3)
                             print("RUN!")
                             break
                if pcre <= 70 :
                    print("you are just autistic then, not a nigga")
                    break
            except ValueError :
                print("you goddam nigga you couldnt understand a simple question?")
                break




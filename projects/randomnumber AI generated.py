import random


range =input("Your number:\t")




if range.isdigit():
    range=int(range)
    
    
    if range <=0:
                print("Please enter a larger than 0.")
                quit()
else:        
     print("Please type a number")
     quit()

score=0
random_number=random.randint(0,range)
        
#print(random_number)
a=0
b=int(input("Enter how much loop is run:"))
while a<=b:
 

    guess=input("Make a guess-->\t")
    if guess.isdigit():
        guess=int(guess)
        
    else:        
           print("Please enter a number.")
           continue
        
        
    #if length==10:
     

        #print(random_number)
   


    if random_number== guess:
            random_number=random.randint(0,range)
            print("\t\t\tCongratulations!You got it.")
            score += 1        
        
                
    
    print("\t\t\tyou got ",score,"marks.")  

    a+=1
print("YOur term is over")
per=(score/a)*100
print("You got ",(per),"% marks.")
if per <= 40:
    print("Bad luck :) You Fail.")
else:
    print("Congrats :)(: You Pass.")

#print("\t\t\tBad Luck!! Your guess is incorrect.")   
            


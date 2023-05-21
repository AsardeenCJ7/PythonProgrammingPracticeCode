#initialis a variable with a hidden value 6

hidden_value = 6
  #Loop while the guess is NOT the hidden number
while True:
    #ask the user to enter a guess (number between 1 -30)
    guess_number = int(input("Enter number between 1 - 30 : "))
    if(0 < guess_number <= 30):
      
            if(guess_number == hidden_value):
                print("The guess number is correct")
                break
            else:
                print("Not Matching guess number")
    else:
        print("Invalid Number")


name="asardeen"
print(len(name))


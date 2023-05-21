while(True):
    marks = int(input("Enter your Marks : "));  
    if(75 <= marks <=100):
        print("A")
    elif(65 <= marks <=74):
        print("B")
    elif(55 <= marks <=64):
        print("C")
    elif(40 <= marks <=54):
        print("D")
    elif(0 <= marks <40):
        print("F")
    else:
        print("Invalid Number")
        
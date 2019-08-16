maincourse = ["fried rice", "biriyani", "pizza", "stake", "sushi"]
sidedish = ["beer can fish","chicken tikka masala","kung pao chicken", "mac n cheese","fish roe and wasabi"]
dessert = ["payasam","fortune cookie","Tiramisu","mochi","death by chocolate cake"]


ques = input(" Hey, do you want to eat something?")
            
if(ques =="no"):
    print("Get a life")
else:
    op = input( "Choose a cuisine : Indian, Chinese, Italian, Japanese, American")
if(op == "Indian"):
    print(maincourse[1], sidedish[1], dessert[0])
    print ("Enjoy!!")
elif(op == "Chinese"):
    print(maincourse[0], sidedish[2], dessert[1])
    print ("Enjoy!!")
elif(op == "Japanese"):
    print(maincouse[4], sideish[4], dessert[3])
    print ("Enjoy!!")
elif(op == "American"):
    print(maincourse[3], sidedish[0], dessert[4])
    print ("Enjoy!!")
else :
    print(maincourse[2], sidedish[3], dessert[2])
    print ("Enjoy!!")
                        
    
    

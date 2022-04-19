def cardGame():
    Card = str(input())
    Card = Card.replace("A","1")
    Card = Card.replace("J","0.5")
    Card = Card.replace("Q","0.5")
    Card = Card.replace("K","0.5")
    Ccard = Card.split(" ")
    Score = [float(Ccard[0]),float(Ccard[1])]
    for i in range(4):
        Cards = str(input())
        Cards = Cards.replace("A","1")
        Cards = Cards.replace("J","0.5")
        Cards = Cards.replace("Q","0.5")
        Cards = Cards.replace("K","0.5")
        Ccards = Cards.split(" ")
        for i in range(len(Ccards)):
            Ccards[i] = float(Ccards[i])
        if(len(Ccards)==4):
            Score[0] += Ccards[1]
            Score[1] += Ccards[3]
        elif(len(Ccards)==3 and Ccards[0]==1):
            Score[0] += Ccards[1]   
        elif(len(Ccards)==3 and Ccards[1]==1):
            Score[1] += Ccards[2]   
        elif(len(Ccards)==2):
            if(Score[0]>Score[1]):
                print("Player X is Winner")
                print(("Player X $ %d" %Score[0]) if (Score[0] - int(Score[0]))==0 else ("Player X $ %.1f" %Score[0]))        
                print(("Player Y $ %d" %Score[1]) if (Score[1] - int(Score[1]))==0 else ("Player Y $ %.1f" %Score[1]))  
            else:
                print("Player Y is Winner")
                print(("Player X $ %d" %Score[0]) if (Score[0] - int(Score[0]))==0 else ("Player X $ %.1f" %Score[0]))        
                print(("Player Y $ %d" %Score[1]) if (Score[1] - int(Score[1]))==0 else ("Player Y $ %.1f" %Score[1]))  
            break
        if(Score[0]>21):
            print("Player Y is Winner")
            print("Player X $ Bang!")
            print(("Player Y $ %d" %Score[1]) if (Score[1] - int(Score[1]))==0 else ("Player Y $ %.1f" %Score[1]))  
            break
        elif(Score[1]>21):
            print("Player X is Winner")
            print(("Player X $ %d" %Score[0]) if (Score[0] - int(Score[0]))==0 else ("Player X $ %.1f" %Score[0]))        
            print("Player Y $ Bang!")
            break
    else:
        if(Score[0]>Score[1]):
            print("Player X is Winner")
            print(("Player X $ %d" %Score[0]) if (Score[0] - int(Score[0]))==0 else ("Player X $ %.1f" %Score[0]))        
            print(("Player Y $ %d" %Score[1]) if (Score[1] - int(Score[1]))==0 else ("Player Y $ %.1f" %Score[1]))  
        else:
            print("Player Y is Winner")
            print(("Player X $ %d" %Score[0]) if (Score[0] - int(Score[0]))==0 else ("Player X $ %.1f" %Score[0]))        
            print(("Player Y $ %d" %Score[1]) if (Score[1] - int(Score[1]))==0 else ("Player Y $ %.1f" %Score[1]))  
cardGame()
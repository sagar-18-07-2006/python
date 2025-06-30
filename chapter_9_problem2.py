import random
def game():
    print("you are playing")
    score = random.randint(1,62)
    highscore =None
    with open("high-score.txt") as f :
        highscore = f.read()
    if(highscore==""):
         highscore=0
    else:
         highscore=int(highscore)
   
    print("your score is ",score)
    if(highscore<score):
        with open("high-score.txt","w"):
            
            
            f.write(str(score))
        
        

game()
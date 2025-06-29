import random

def game():
    print("You are playing")
    score = random.randint(1, 62)

    # Read existing high score (handle empty file case)
    with open("high-score.txt") as f:
        highscore = f.read().strip()

    # If file is empty, treat highscore as 0
    if highscore == "":
        highscore = 0
    else:
        highscore = int(highscore)

    print("Your score is", score)

    # Update high score if needed
    if score > highscore:
        print("Congratulations! New High Score!")
        with open("high-score.txt", "w") as f:
            f.write(str(score))

game()

import random
import time
random.seed(time.time())
print('''
s for Snake 
g for Gun 
w for Water
''')

# Randomly select computer choice
computer_choice = random.choice(['s', 'g', 'w'])

# Player input
you = input("Enter your option (s/g/w): ").lower()

# Validating input
if you not in ['s', 'g', 'w']:
    print("Invalid input. Choose s, g, or w only.")
    exit()

# Outcome mapping
# (player_choice, computer_choice): result
# 1 = win, 0 = draw, -1 = lose
outcomes = {
    ('s', 's'): 0,
    ('s', 'g'): -1,
    ('s', 'w'): 1,
    ('g', 'g'): 0,
    ('g', 'w'): -1,
    ('g', 's'): 1,
    ('w', 'w'): 0,
    ('w', 's'): -1,
    ('w', 'g'): 1
}

result = outcomes[(you, computer_choice)]

print(f"Computer chose: {computer_choice}")

if result == 1:
    print("✅ You Won!")
elif result == -1:
    print("❌ You Lost.")
else:
    print("➖ It's a Draw.")

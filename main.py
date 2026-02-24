import art,random
from game_data import data as game_data
print(art.logo)

def validate():
    global Compare_A, Compare_B, Score, is_correct
    user_chooses = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_chooses == "a":
        if Compare_A['follower_count'] > Compare_B['follower_count']:
            Score += 1
        else:
            is_correct = False
        return Compare_A
    elif user_chooses == "b":
        if Compare_B['follower_count'] > Compare_A['follower_count']:
            Score += 1
        else:
            is_correct = False
        return Compare_B
    else:
        print("you typed invalid value, try again")
        is_correct = False
        return None

Compare_A = random.choice(game_data)
Score = 0
is_correct = True

while is_correct:
    print(f"Compare A: {Compare_A['name']}, {Compare_A['description']}, {Compare_A['country']}, ")
    print(art.vs)
    Compare_B = random.choice(game_data)
    while Compare_B == Compare_A:
        Compare_B = random.choice(game_data)
    print(f"Compare B: {Compare_B['name']}, {Compare_B['description']}, {Compare_B['country']}")
    print(f"{Compare_A['follower_count']}, {Compare_B['follower_count']}")
    Compare_A = validate()
    if is_correct:
        print(f"You're right! Current score: {Score}")
    else: print(f"Sorry, that's wrong. Final score: {Score}")


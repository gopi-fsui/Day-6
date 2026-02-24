import art,random
from game_data import data as game_data
print(art.logo)

def validate(item_a, item_b):
    user_chooses = input("Who has more followers? Type 'A' or 'B': ").lower()
    while not user_chooses in ['a','b']:
        print("You typed invalid value,choose again!")
        user_chooses = input("Who has more followers? Type 'A' or 'B': ").lower()
    if item_a['follower_count'] > item_b['follower_count']:
        return user_chooses == "a"
    elif item_b['follower_count'] > item_a['follower_count']:
        return user_chooses == "b"
    return None


Compare_B = random.choice(game_data)
Score = 0
is_correct = True

while is_correct:
    Compare_A = Compare_B
    print(f"Compare A: {Compare_A['name']}, {Compare_A['description']}, {Compare_A['country']}, ")
    print(art.vs)
    Compare_B = random.choice(game_data)
    while Compare_B == Compare_A:
        Compare_B = random.choice(game_data)
    print(f"Compare B: {Compare_B['name']}, {Compare_B['description']}, {Compare_B['country']}")
    print(f"{Compare_A['follower_count']}, {Compare_B['follower_count']}")
    is_correct = validate(Compare_A,Compare_B)
    if is_correct:
        Score += 1
        print("\n" * 35)
        print(f"You're right! Current score: {Score}")
    else:
        print("\n"*20)
        print(f"Sorry, that's wrong. Final score: {Score}")


import random
EASY_TURNS=10
HARD_TURNS=5
def set_difficulty():
 level= input("choose 'easy' or 'hard'")
 if level=="easy":
   turns=EASY_TURNS
 else:
    turns=HARD_TURNS
num = random.randint(1,100)
print("Welcome to the guessing game")
print("I am thinking a number")
guess = int(input("make a guess:"))
turns = set_difficulty()

def check_ans(num,guess):
  if guess>num:
    print("your guess is too high")
  elif guess<num:
    print("your guess id to low")
  else:
    print(f"your guess is correct the number is:{num}")


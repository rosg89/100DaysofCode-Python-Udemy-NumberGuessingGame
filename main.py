from art import logo
from random import randint

#Global constants
EASY_LEVEL = 10
HARD_LEVEL = 5

#Funcion que compara resultado con guess del usuario
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns -1
  elif guess < answer:
    print("Too low.")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}.")

#Función que establece la dificultad
def set_dif():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100. Can you guess it?")
  
  #Choosing a random number between 1-100.
  answer = randint(1,100)
  turns = set_dif()
  
  
  guess = 0
  
  #While Loop
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    #User have to guess
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      #Para salir de la función y que termine el juego
      return

game()
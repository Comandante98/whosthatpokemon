import pypokedex
import random

def main():
    start()

def start():
    print("*-----------------------------------------------------------------------------------------------*")
    print("|                     Welcome to the Who's that pokemon gameshow!!                              |")
    print("|The game consists of ten rounds where a random pokemon will be chosen and a series of random   |")
    print("|hints will be given to you to guess the pokemon.                                               |")
    print("|3 hints will be given at the start, and 3 extra for each wrong guess gaining 10, 8, 5, 2 and 0 |")
    print("|depending on how many guesses it took to find the correct pokemon. Only pokemon with an unique |")
    print("|pokedex number will be chosen(no regional forms,pokemon with different forms, only base form)  |")
    print("|Whenever you are ready to start press enter!                                                   |")
    print("*-----------------------------------------------------------------------------------------------*")
    

if __name__ == "__main__":
    main()
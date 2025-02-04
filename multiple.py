from random import randint

class GenerateRANDOM:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.randi = randint(self.start, self.stop)
        print(f"Random Number : {self.randi}") 

    def generate1(self):
        return self.randi


class Get_Guess:
    def __init__(self):
        self.guess = None

    def set_guess(self, guess: int):
        self.guess = guess

    def return_guess(self):
        return self.guess


class PlayGame:
    def __init__(self, start, stop):
        self.random_gen = GenerateRANDOM(start, stop)
        self.guess_obj = Get_Guess()

    def compare(self):
        while True:
            try:
                guess = int(input("Enter your guess:\n"))
                self.guess_obj.set_guess(guess)
            except ValueError:
                print("Invalid data type, please enter an integer.")
                continue  

            if self.random_gen.generate1() == self.guess_obj.return_guess():
                print("Perfect!")
                break
            elif self.random_gen.generate1() > self.guess_obj.return_guess():
                print("The generated number is higher than your guess.")
            else:
                print("The generated number is lower than your guess.")


while True:
    try:
        start = int(input("Enter the start:\n"))
        stop = int(input("Enter the stop:\n"))
        if start < stop:  
            break
        else:
            print("Start must be less than stop.")
    except ValueError:
        print("Incorrect data type, please enter integers.")


game = PlayGame(start, stop)
game.compare()

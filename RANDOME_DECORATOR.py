from random import randint


def randomGame(func):
    def run(start,stop):
        rand_number=func(start,stop)
        print("the rand is:",rand_number)
        while True:
            try:
                guess=int(input("enter ur guess:\n"))
                if guess>rand_number:
                    print("higer")
                    
                elif guess<rand_number:
                    print("lower")
                    
                else:
                    print("perfect")
                    break
            except ValueError:
                print("incoorect value type")
                
    return run
    

while True:
    try:
        start=int(input("enter the int val for star:\n"))
        stop=int(input("enter the int val for stop:\n"))
        break
    except ValueError:
        print("incorrect value type")
@randomGame
def randRange_clac(start,stop):
    rand=randint(start,stop)
    
    return rand













randRange_clac(start,stop)
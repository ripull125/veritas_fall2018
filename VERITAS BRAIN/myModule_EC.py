
def my_function():
    print('hello')
import random

def computer_rps():
    cpu = random.randint(1,3)

    if cpu == 1:
        cpu = "rock"
    elif cpu == 2:
        cpu = "paper"
    elif cpu == 3:
        cpu = "scissor"
    return cpu


computer_rps()
        

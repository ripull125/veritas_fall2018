
import random
def my_function():
    print('hello')

def computer_rps(say):
    cpu = random.randint(1,4)

    if cpu == 1:
        cpu = "rock"
    elif cpu == 2:
        cpu = "paper"
    elif cpu == 3:
        cpu = "scissors"
    return cpu
    

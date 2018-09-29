import myModule_EC as a
rps = a.computer_rps()
def determine(say, rps) :
    if say == "rock" and rps == "rock":
        print ("tie!")
    elif say == "rock" and rps == "scissor":
        print ("you won!")
    elif say == "rock" and rps == "paper":
        print ("you lost!")
    elif say == "paper" and rps == "paper":
        print ("tie!")
    elif say == "paper" and rps == "scissor":
        print ("you lost!")
    elif say == "paper" and rps == "rock":
        print ("you won!")
    elif say == "scissor" and rps == "rock":
        print("you lost!")
    elif say == "scissor" and rps == "scissor":
        print ("tie!")
    elif say == "scissor" and rps == "paper":
        print ("you won!")


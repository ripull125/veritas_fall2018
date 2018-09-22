import myModule_EC as a

a.computer_rps()

say = input("rock, paper, or scissor?   ")

rps = a.computer_rps(say)



if say == "rock" and cpu == "rock":
    print ("tie")
elif say == "rock" and cpu == "scissor":
    print("you won")
elif say == "rock" and cpu == "paper":
    print ("you lost")
elif say == "paper" and cpu == "paper":
    print("tie!")
elif say == "paper" and cpu == "scissor":
    print ("you lost")
elif say == "paper" and cpu == "rock":
    print ("you won")
elif say == "scissor" and cpu == "rock":
    print("you lost")
elif say == "scissor" and cpu == "scissor":
    print ("tie!")
elif say == "scissor" and cpu == "paper":
        print("you won")

                     

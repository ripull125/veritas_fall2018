import myModule_EC as a
import rpsWhoWins_module as x
import random
a.computer_rps()

ay = input("rock, paper, or scissor?   ")

rpc = a.computer_rps()


print (rpc)
win = x.determine(ay, rpc)

win

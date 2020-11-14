#    _   _            _____        __  __ _      
#   | | | |          |  __ \      / _|/ _| |     
#   | |_| |__   ___  | |__) |__ _| |_| |_| | ___ 
#   | __| '_ \ / _ \ |  _  // _` |  _|  _| |/ _ \
#   | |_| | | |  __/ | | \ \ (_| | | | | | |  __/
#    \__|_| |_|\___| |_|  \_\__,_|_| |_| |_|\___|
#                                                
#   for swindlers...
#       *Last participant will win.       
#                                         
# made by: Ceyhun Gülbaş
# https://github.com/ceyhungulbas
#_________________________________________________
import random

print("<<<<<<<<<<<<<<<<<<<<<<<<<\n"+"|\t\t\t|"+"\n|Welcome to the Raffle. |"+"\n|\t\t\t|\n"+">>>>>>>>>>>>>>>>>>>>>>>>>")

size = int(input('\n\n\nHow many participants applied: '))
values = [(input('Names of participants: ')) for _ in range(size)]
# values.sort()
print("List of participants: ", ', '.join(values))


winner = values[-1]
print("Winner: ", ', '.join(winner))

input("Sonlandırın.")

from troll.main import *
import os
clear = lambda: os.system('cls')
clear()

mike = Troll()

loop_number = 0
while True:
    loop_number +=1
    print(f"loop number {loop_number}.\n")
    print("infos about Mike, the troll:")
    print("hungry: " + str(mike.hungry))
    print("life: " + str(mike.life))

    mike.update()
    input("Press enter to continue")
    clear()

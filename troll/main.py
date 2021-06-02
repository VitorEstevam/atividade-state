from state_pattern.main import *
import random


class Troll(Agent):
    life = 10
    hungry = 0
    def __init__(self):
        super().__init__(TrollStateSleeping())
        pass
    def update(self):
        if(self.life <=0): self.set_state(TrollStateDead())
        if(self.hungry >4): self.set_state(TrollStateHunting())
        
        super().update()


class TrollStateSleeping(State):
    def execute(self, troll: Troll):
        print("Mike is sleeping")
        if(troll.life<10): troll.life+=1
        troll.hungry+=1

        _input = input("Do you want fight some noobs?(y/n)\n")
        if(_input == "y"): 
            print("Mike is going to fight.")
            troll.set_state(TrollStateFighting())
    
class TrollStateFighting(State):
    def execute(self, troll: Troll):
        damage = random.randint(2,4)
        troll.life -= damage
        print(f"After the fight Mike has taken {damage} from damage")
        troll.set_state(TrollStateSleeping())


class TrollStateHunting(State):
    def execute(self, troll: Troll):
        print("Mike is hunting")
        troll.hungry-=3
        if(troll.hungry<0): troll.hungry = 0
        troll.life-=1

        if(troll.hungry == 0): troll.set_state(TrollStateSleeping())

class TrollStateDead(State):
    def execute(self, troll: Troll):
        print("Mike the troll is dead RIP")
        exit()

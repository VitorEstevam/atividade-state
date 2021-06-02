All you want is this:

```python
from __future__ import annotations
from abc import ABC, abstractmethod

class Agent:
    actual_state = None

    def __init__(self, _state: State):
        self.set_state(_state)

    def update(self):
        self.actual_state.execute(self)
        pass

    def set_state(self, _state: State):
        self.actual_state = _state

class State(ABC):
    @abstractmethod
    def execute(self, agent: Agent):
        pass
```


Just use heritage to create other classes to use with the pattern:
```python
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
        print("Troll is sleeping")
        if(troll.life<10): troll.life+=1
        troll.hungry+=1
    
class TrollStateHunting(State):
    def execute(self, troll: Troll):
        print("Troll is hunting")
        troll.hungry-=3
        if(troll.hungry<0): troll.hungry = 0
        troll.life-=1

        if(troll.hungry == 0): troll.set_state(TrollStateSleeping())
 
class TrollStateDead(State):
    def execute(self, troll: Troll):
        print("Troll is dead RIP")
        exit()
        
 #----------------------------------
import os
clear = lambda: os.system('cls')

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
```

reference:
https://refactoring.guru/design-patterns/state/python/example

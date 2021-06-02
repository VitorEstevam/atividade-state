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

from pyfsm import FSM, EndState

class testfsm(FSM):
    def __init__(self, name):
        super().__init__(name)

    def initial_state(self, data: dict):
        """
FSM.state
allowed_states: end_state
        """
        if data == {'test' : True }:
            self._change_state(self.end_state)
    
    

tester = testfsm('test')

#print(tester.initial_state.__doc__)
tester._change_state(tester.end_state)
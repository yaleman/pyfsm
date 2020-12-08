import pytest
from pyfsm import FSM, EndState

def test_endstate_raises():
    fsm = FSM(name='test')

    with pytest.raises(EndState):
        # you shouldn't ever force it like this, but it's a test
        fsm._change_state(fsm.end_state)

def test_simple_fsm():
    """ test sublcassing FSM as testfsm with a really simple example """
    class testfsm(FSM):
        def __init__(self, name):
            super().__init__(name)

        def initial_state(self, data: dict):
            if data == {'test' : True }:
                self._change_state(self.end_state)
        
    t = testfsm('test')
    with pytest.raises(EndState):
        t.state({'test' : True })
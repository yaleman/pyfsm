
# Data goes in
# Current state takes data, does things.
# If it should change state, do so

# State function should have a doc that includes an identifier string, and state change Only allow change to that state

# self.state_change(new state)
# Check
# Raise if bad
# Change

class EndState(Exception):
    pass

class FSM():
    def __init__(self, name: str):
        """ 
        please name your FSM's, name: str
        """
        self.state = self.initial_state
        self.name = name
        # this is an "internal" datastore, to store things between transitions
        # for example, last ten readings of a temp sensor, or last seen state of a door
        self.internal_state = {}

    def _is_valid_state(self, oldstate, newstate):
        if 'allowed_states' not in str(oldstate.__doc__):
            raise ValueError("no 'allowed_states' specified in state {}".format(self.state))
        for line in oldstate.__doc__.split("\n"):
            line = line.strip()
            if line.startswith("allowed_states"):
                print("found state sequence")
                line = line[16:]
            print(str(newstate))
            print(line)

    def _change_state(self, newstate):
        self._is_valid_state(self.state, newstate)
        self.state = newstate
        
        if self.state == self.end_state:
            raise EndState("End state for {}".format(self.name))

    def initial_state(self, data: dict):
        """
        FSM.state
        allowed_stadtes: end_state
        """
        raise NotImplementedError("FSM should always be subclassed.")

    def end_state(self, data: dict):
        pass
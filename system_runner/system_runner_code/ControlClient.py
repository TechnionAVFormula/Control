from pyFormulaClientNoNvidia.ModuleClient import ModuleClient, ClientSource
from pyFormulaClientNoNvidia.MessageDeque import MessageDeque
from pyFormulaClientNoNvidia import messages


class ControlClient(ModuleClient):
    def __init__(self, read_from_file, write_to_file):
        super().__init__(ClientSource.CONTROL, read_from_file, write_to_file)    
        self.server_messages = MessageDeque()                                              
        self.formula_state = MessageDeque(maxlen=1)        

    def _callback(self, msg):  
        if msg.data.Is(messages.state_est.FormulaState.DESCRIPTOR):
            self.formula_state.put(msg)
        else:
            self.server_messages.put(msg)

    def get_formula_state_message(self, blocking=True, timeout=None):
        return self.formula_state.get(blocking, timeout)

    def pop_server_message(self, blocking=False, timeout=None):
        return self.server_messages.get(blocking, timeout)

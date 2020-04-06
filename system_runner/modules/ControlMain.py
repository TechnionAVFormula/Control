import signal

# from pyFormulaClientNoNvidia import messages
from config import CONFIG, IN_MESSAGE_FILE, OUT_MESSAGE_FILE
from config import ConfigEnum

if CONFIG == ConfigEnum.REAL_TIME or CONFIG == ConfigEnum.COGNATA_SIMULATION:
    from pyFormulaClient import FormulaClient, messages
    from pyFormulaClient.ModuleClient import ModuleClient
    from pyFormulaClient.MessageDeque import MessageDeque
elif CONFIG == ConfigEnum.LOCAL_TEST:
    from pyFormulaClientNoNvidia import FormulaClient, messages
    from pyFormulaClientNoNvidia.ModuleClient import ModuleClient
    from pyFormulaClientNoNvidia.MessageDeque import MessageDeque
else:
    raise NameError('User Should Choose Configuration from config.py')

# TODO: import path is probably going to change after integration into system runner
from controller.controller import BasicController
from system_runner.modules.ControlClient import ControlClient


class Control:
    def __init__(self):
        # ControlClient reads messages from modules/state_est.messages and writes to modules/control.messages
        self._client = ControlClient('modules/state_est.messages', 'modules/control.messages')
        self._running_id = 1
        self.message_timeout = 0.01
        self._controller = BasicController()

    def start(self):
        self._client.connect(1)
        self._client.set_read_delay(0.05)  # Sets the delay between reading new messages from sensors.messages
        self._client.start()

    def stop(self):
        if self._client.is_alive():
            self._client.stop()
            self._client.join()

    def process_formula_state_message(self, formula_state_msg):
        formula_state = messages.state_est.FormulaState()
        formula_state_msg.Unpack(formula_state)

        driving_instructions = messages.control.DriveInstructions()

        # Insert algorithms
        out_msg = self._controller.process_state_est(formula_state)
        driving_instructions.gas = out_msg.gas
        driving_instructions.breaks = out_msg.breaks
        driving_instructions.steering = out_msg.wheel_angle
        # TODO: add speed to protocol
        # driving_instructions.speed = out_msg.speed

        return driving_instructions

    def process_server_message(self, server_messages):
        if server_messages.data.Is(messages.server.ExitMessage.DESCRIPTOR):
            return True

        return False

    def send_message2server(self, msg_id, driving_instruction):
        msg = messages.common.Message()
        msg.header.id = msg_id
        msg.data.Pack(driving_instruction)
        self._client.send_message(msg)

    def run(self):
        while True:
            try:
                server_msg = self._client.pop_server_message()
                if server_msg is not None:
                    if self.process_server_message(server_msg):
                        return
            except Exception as e:
                pass

            try:
                formula_state = self._client.get_formula_state_message(timeout=self.message_timeout)
                driving_instruction = self.process_formula_state_message(formula_state)
                self.send_message2server(formula_state.header.id, driving_instruction)
            except Exception as e:
                pass


control = Control()


def stop_all_threads():
    print("Stopping threads")
    control.stop()


def shutdown(a, b):
    print("Shutdown was called")
    stop_all_threads()
    exit(0)


def main():
    print("Initalized Control")

    control.start()
    control.run()

    stop_all_threads()
    exit(0)


if __name__ == "__main__":
    for signame in ('SIGINT', 'SIGTERM'):
        signal.signal(getattr(signal, signame), shutdown)
    main()

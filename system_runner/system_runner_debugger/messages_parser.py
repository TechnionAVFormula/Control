import argparse
import os

from google.protobuf import text_format
from pyFormulaClientNoNvidia import messages
from pyFormulaClientNoNvidia.FormulaClient import FormulaClient, ClientSource, SYSTEM_RUNNER_IPC_PORT


def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise argparse.ArgumentTypeError(f"Messages file {string} not found")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('message_file', type=file_path)
    # parser.add_argument('-d', '--print-default-values', required=False)

    return parser.parse_args()


def parse_file(message_file):
    # TODO: verify client source correctness for this task
    client = FormulaClient(ClientSource.CONTROL,
                           read_from_file=message_file, write_to_file=os.devnull)
    conn = client.connect(SYSTEM_RUNNER_IPC_PORT)

    out = []
    msg = messages.common.Message()
    while not msg.data.Is(messages.server.ExitMessage.DESCRIPTOR):
        msg = conn.read_message()
        if msg.data.Is(messages.control.DriveInstructions.DESCRIPTOR):
            di = messages.control.DriveInstructions()
            msg.data.Unpack(di)

            msg_id = msg.header.id
            msg_time = msg.header.timestamp.ToDatetime()
            msg_data = di

            out.append((msg_id, msg_time, msg_data))

    return out


# class FormulaProtoPrinter:
#     def __init__(self, print_default_values):
#         self.print_default_values = print_default_values
#
#     def _message_formatter(self, message, indent, as_one_line):
#         if message.DESCRIPTOR != messages.common.Header.DESCRIPTOR:
#             return None
#
#         indent_str = ' ' * indent
#         field_end_str = ' ' if as_one_line else '\n'
#
#         formatted_header = f'id: {message.id}{field_end_str}'
#         formatted_header += f'{indent_str}timestamp: {message.timestamp.ToDatetime()}{field_end_str}'
#         formatted_header += f'{indent_str}source: {ClientSource(message.source).name}{field_end_str}'
#         formatted_header += f'{indent_str}priority: {message.priority}'
#
#         return formatted_header
#
#     def print_message(self, msg):
#         msg_str = text_format.MessageToString(msg, message_formatter=self._message_formatter)
#         msg_str = msg_str.replace('type.googleapis.com/', '')
#         print(msg_str)
#
#
# def print_file(message_file):
#     client = FormulaClient(ClientSource.CONTROL,
#                            read_from_file=message_file, write_to_file=os.devnull)
#     conn = client.connect(SYSTEM_RUNNER_IPC_PORT)
#
#     printer = FormulaProtoPrinter(False)
#
#     msg = messages.common.Message()
#     while not msg.data.Is(messages.server.ExitMessage.DESCRIPTOR):
#         msg = conn.read_message()
#         printer.print_message(msg)


def main():
    args = parse_args()
    print(parse_file(args.message_file))
    # print_file(args.message_file)


if __name__ == '__main__':
    main()

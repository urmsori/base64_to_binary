import base64
import sys

output_name = "output.xlsx"
if len(sys.argv) == 2:
    output_name = sys.argv[1]


with open("input.txt", 'rb') as read_fd:
    read = read_fd.read()
    bytes = base64.decodebytes(read)

    with open(output_name, 'wb') as write_fd:
        write_fd.write(bytes)

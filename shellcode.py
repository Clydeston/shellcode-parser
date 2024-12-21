import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--binary")

args = parser.parse_args()
binary = args.binary

print(binary)
output = subprocess.run(["objdump", "-M", "intel", "-d", binary], capture_output=True, text=True)

text_section = repr(output.stdout).split("<_start>")[1]
opcodes = repr(text_section).split("\\n")

built_str = ""
for line in opcodes:
    text = line.split("\\t")
    arr_size = len(text)
    if(arr_size > 1):
        parsed_opcode = text[1].replace("\\", "").strip().replace(" ", "\\x")
        parsed_opcode = f"\\x{parsed_opcode}"
        built_str += parsed_opcode
print(built_str)

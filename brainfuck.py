#!/usr/bin/python
#
#Brainfuck interpreter
#

import sys


def main():
	filename = sys.argv[1]
	with open(filename, 'r') as f:
		code = cleanup(f.read())
	run(code)


def run(code):

	cells = n = [0 for n in range(0,30000)]
	data_pointer = 0
	code_pointer = 0
	brace_map = bracemapbuild(code)

	while code_pointer < len(code):
		op = code[code_pointer]

		if op == ">": data_pointer += 1

		if op == "<": data_pointer -= 1

		if op == "+": cells[data_pointer] += 1

		if op == "-": cells[data_pointer] -= 1

		if op == ".": print(chr(cells[data_pointer]), end='')

		if op == "[" and cells[data_pointer] == 0: code_pointer = brace_map[code_pointer]

		if op == "]" and cells[data_pointer] != 0: code_pointer = brace_map[code_pointer]

		code_pointer += 1

def bracemapbuild(code):
	brace_stack, brace_map = [], {}
	for index, op in enumerate(code):
		if op == '[': brace_stack.append(index)
		if op == ']':
			start = brace_stack.pop()
			brace_map[start] = index
			brace_map[index] = start
	return brace_map

def cleanup(code):
	return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


if __name__ == '__main__':
	main()

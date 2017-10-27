#!/usr/bin/env python3
import operator

ops = {
	'+': operator.add,
	'-': operator.sub
}

def calculate(string):
	stack = list()
	for token in string.split():
			try:
				stack.append(int(token))
			except ValueError:
				arg2 = stack.pop()
				arg1 = stack.pop()
				function = ops[token]
				result = function(arg1,arg2)
				stack.append(result)
	print(stack.pop())
	return(stack.pop())

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()
		

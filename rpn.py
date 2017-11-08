import operator
import readline 
import logging
import os

try:
	os.remove("example.log")
	logging.basicConfig(filename='example.log',level=logging.DEBUG)
except opps:
	logging.basicConfig(filename='example.log',level=logging.DEBUG)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        logging.info(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

def UNTESTED(x):
	y = x
	x = x + y
	if x is y:
		y = 0
	y = x
	x = x + y
	if x is y:
		y = 0
	y = x
	x = x + y
	if x is y:
		y = 0
	y = x
	x = x + y
	if x is y:
		y = 0
	y = x
	x = x + y
	if x is y:
		y = 0

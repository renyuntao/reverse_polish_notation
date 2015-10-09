#!/usr/bin/env python
import math
operators = ['*','/','+','-','%']
stack = []
input_ = input().split()
for elem in input_:
    if elem in operators:    #elem is a operator
        first_num = stack.pop()
        first_num = int(first_num)
        second_num = stack.pop()
        second_num = int(second_num)
        if elem == '*':
            result = second_num * first_num
        elif elem == '/':
            result = second_num / first_num
        elif elem == '+':
            result = second_num + first_num
        elif elem == '-':
            result = second_num - first_num
        else:
            result = second_num % first_num
        stack.append(result)
    else:               # elem is a operand
        stack.append(elem)
ans = stack.pop()
print(ans)

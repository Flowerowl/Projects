#coding: utf-8
"""
ref: http://www.mathsisfun.com/numbers/fibonacci-sequence.html
"""
MAX = 1000
sequence = [0, 1]

while sequence[-1] < MAX:
    sequence.append(sequence[-1] + sequence[-2])

print sequence

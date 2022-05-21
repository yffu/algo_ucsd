import random
import sys
import os

tests = int(sys.argv[1])

n = int(sys.argv[2])

for i in range(tests):
    print("Test #" +str(i))

    os.system("python gentest_2.py "+ str(n) + " " + str(i) + " > input.txt")
    os.system("python model.py < input.txt > model.txt")
    os.system("python main.py < input.txt > main.txt")

    with open('model.txt') as f: model=f.read()
    print("Model: ", model)

    with open('main.txt') as f: main = f.read()
    print("Main: ", main)

    if model != main:
        break

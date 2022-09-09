#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        # keep another stack of max at the time number of that index was pushed to the stack
        self.__stack_m = []

    def Push(self, a):
        self.__stack.append(a)
        if self.__stack_m:
            self.__stack_m.append(max(self.Max(), a))
        else:
            self.__stack_m.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__stack_m.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__stack_m[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)

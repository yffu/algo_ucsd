# python3

s1 = []
s2 = []
debug = False


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
        return self.__stack_m[-1] if self.__stack else False


def max_sliding_window(sequence, m):
    maximums = []
    s2_m = StackWithMax()
    s1_m = StackWithMax()
    for i in range(len(sequence)): # i range 0 ... 7
        # from 0 to len(sequence)
        # push() new element onto stack
        if i < m: # i range 0 ... 3
            s1.append(sequence[i])
            s1_m.Push(sequence[i])
            if debug:
                print('s1: ' + str(s1))
                print('s1_m: ' + str(s1_m.Max()))
        else:
            if s1_m.Max() is not False and s2_m.Max() is not False:
                maximums.append(max(s1_m.Max(), s2_m.Max()))
            elif s1_m.Max() is not False:
                maximums.append(s1_m.Max())
            elif s2_m.Max() is not False:
                maximums.append(s2_m.Max())
            else:
                None
            if debug:
                print('maximums: ' + str(maximums))
            # i >= m, pop() front of queue, get maximum from stack
            if not s2:
                while s1:
                    tmp = s1.pop()
                    s1_m.Pop()
                    s2.append(tmp)
                    s2_m.Push(tmp)
                    if debug:
                        print('s1: ' + str(s1))
                        print('s1_m: ' + str(s1_m.Max()))
                        print('s2: ' + str(s2))
                        print('s2_m: ' + str(s2_m.Max()))
            # assumption: if index >= len - m, then s2 is not empty
            # counterexample is when len = 1, m = 1,
            s2.pop()
            s2_m.Pop()
            s1.append(sequence[i])
            s1_m.Push(sequence[i])
            if debug:
                print('s1: ' + str(s1))
                print('s1_m: ' + str(s1_m.Max()))
                print('s2: ' + str(s2))
                print('s2_m: ' + str(s2_m.Max()))
    if s1_m.Max() is not False and s2_m.Max() is not False:
        maximums.append(max(s1_m.Max(), s2_m.Max()))
    elif s1_m.Max() is not False:
        maximums.append(s1_m.Max())
    elif s2_m.Max() is not False:
        maximums.append(s2_m.Max())
    else:
        None
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))


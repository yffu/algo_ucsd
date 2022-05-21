# Uses python3
debug = False


def edit_distance(s, t):
    #write your code here
    # last column is either: these are the conditions in your loop
    # insertion + 1 score
    # deletion + 1 score
    # mismatch + 1 score
    # match + 0 score
    # everything without last column is already optimal (the sub-problem)
    # remember to keep a pointer to the previous D position, iterate by x, then y values
    '''
    D(i,j) = min{
        D(i, j-1) + 1 -> insertion
        D(i-1, j) + 1 -> deletion
        D(i-1, j-1) + 1 -> match
        D(i-1, j-1) -> mismatch
    }
    '''
    # The length of both strings is at least 1 and at most 100.
    # Output the edit distance between the given two strings.
    d = []
    for j in range(len(s)+1):
        d.append([])
        for i in range(len(t)+1):
            if j == 0:
                d[j].append(i)
            elif i == 0:
                d[j].append(j)
            else:
                d_ins = d[j-1][i] + 1
                d_del = d[j][i-1] + 1
                d_mat = d[j-1][i-1] + (0 if t[i-1] == s[j-1] else 1)
                d[j].append(min(d_ins, d_del, d_mat))
                if debug:
                    print("j: " + str(j) + " i: " + str(i) + " str_j: " + s[j-1] + " str_i: " + t[i-1])
                    print("d_ins: " + str(d_ins) + " d_del: " + str(d_del) + " d_mat: " + str(d_mat))
                    print([c_t for c_t in t])
                    for i in range(len(d)):
                        print(s[i-1] + str(d[i]))
    return d[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

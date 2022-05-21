def max_pairwise_product(numbers):
    # Constraints. 2 ≤ n ≤ 2 · 105
    n = len(numbers)
    if numbers[1] >= numbers[0]:
        n1 = numbers[1]
        n0 = numbers[0]
    else:
        n1 = numbers[0]
        n0 = numbers[1]
            
    for i in range(2, n):
        if numbers[i]>n1:
            n0 = n1
            n1 = numbers[i]
        elif numbers[i]>n0:
            n0 = numbers[i]
        else:
            None
    #print('n0: '+ str(n0))
    #print('n1: '+ str(n1))
    return n0 * n1


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    #input_numbers = range(1,2*pow(10,5)+1)
    print(max_pairwise_product(input_numbers))

# binary search algorithm 
def binary_alogrithm(list,element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print(f'step {steps} :, {str(list[start:end+1])}')

        steps += 1
        middle = (start + end) // 2
         
        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
        
    return -1

my_list = [1,2,3,4,5,6,7,8,9,0]
target = 3

binary_alogrithm(my_list,target)
#print("HEllo world")

def filter_list(l):
    'return a new list with the strings filtered out'
    numbers = []
    for nums in l:
        if type(nums) == int:
            numbers.append(nums)
    
    print(numbers)
    
filter_list([1, 2, 4, "a", "b", "C", 4])



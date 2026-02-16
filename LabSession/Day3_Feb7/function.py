#function for sum of all the elment in  the list

def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total


print("the sum of the list is: ",sum_list([1, 2, 3, 4, 5]))


#find the maximum of three numbers

def largest(lst):
    return max(lst)

print("the largest number is: ",largest([1, 2, 3, 4, 5]))
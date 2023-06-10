"""
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
 
# to find the highest and lowest numbers


print (min_, max_)

"""

# list of numbers
def my_edges(lll):
    min_ = 100
    max_ = 0
    for num in lll:
        if num > max_:
            max_ = num

        if num < min_:
            min_ = num
    
    return min_, max_


list1 = [10, 21, 4, 45, 66, 93]
minn, maxx = my_edges(list1)
print(minn, maxx)
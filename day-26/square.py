#using list comprehension for square root of numbers
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

#using list comprehension to check for even numbers in a list of numbers
numbers = [1,1,2,3,5,8,13,21,34,55]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

#comparing two list and putting the same numbers in a new_list using List Comprehension 
list1 = [2,4,6,7,5,10]
list2 = [1,4,6,9,7,8]
newlist = [num for num in list1 if num in list2]
print(newlist)
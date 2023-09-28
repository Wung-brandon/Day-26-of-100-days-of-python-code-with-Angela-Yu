numbers = [1, 2, 3]
new_list = []
for n in numbers:
    item = n + 1
    new_list.append(item)
print(new_list)

#Using List Comprehension
new_n_list = [n + 1 for n in numbers]
print(new_n_list)

#an alternative other than the List comprehension
names = "wung"
empty_name = []
for letter in names:
    empty_name.append(letter)
print(empty_name)

#Using List Comprehensions on strings
new_name = [letter for letter in names]
print(new_name)

#List Comprehension on range functions
range_list = [n * 2 for n in range(1,5)]
print(range_list)

#Conditional List Comprehension
persons = ["wung", "brandon", "beth", "dave", "venia", "aloy", "alex", "caroline", "eleanor"]
new_persons = [name.upper() for name in persons if len(name) >= 5]
print(new_persons)
#Dictionary Comprehension
#new_dict = {key:value for (key,value) in dict.items()}

from random import randint
#generate random scores for names of students using dictionary comprehension
names = ["wung","gina","venia","lucas","brandon"]
student_scores = {student:randint(1,100) for student in names}
print(student_scores)

#print(student_scores.items())

#looping through a dictionary
#conditional dictionary comprehension
passed_students = {student:score for (student,score) in student_scores.items() if score >= 50}
print(passed_students)
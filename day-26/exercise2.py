#converting a dictionary of temperature in celcius to fahrenheit using the Dictionary Comprehension

weather_c = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}

weather_f = {days:temp*9/5+32 for (days,temp) in weather_c.items()}
#print(weather_f)

student_dict = {
    "student": ["wung","brandon","venia","gina"],
    "score": [45,78,56,39]
}
#looping through dictionary
for (key,value) in student_dict.items():
    print(key)
    #print(value)
    
#how to iterate over a pandas dataframe
import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame) 

#loop through a data frame
#for (key,value) in student_data_frame.items():
 #   print(key)
 
#pandas inbuilt method iterrows() to loop through a data frame
for (index, row) in student_data_frame.items():
    print(row)
    #if row.student == "wung":
     #   print(row.score)
    #print(index)


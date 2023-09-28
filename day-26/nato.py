import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
#print(df.iterrows())


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
phoenetic_code = {row["letter"]:row["code"] for (index,row) in df.iterrows() }
#print(phoenetic_code)
#print(df) 

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phoenetic():
    user_word = input("Enter a word: ").upper()

    try:
        output_list = [phoenetic_code[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        #if a word is not in the dictionary then the prompt should show again
        generate_phoenetic()
    else:
        print(output_list)
        
generate_phoenetic()
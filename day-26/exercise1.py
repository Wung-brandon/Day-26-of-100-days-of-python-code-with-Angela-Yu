sentence = "what is the Airspeed velocity of an unladen Swallow"
#print(len(sentence))
split_word = sentence.split()

#print(split_word)
result = {word:len(word) for word in split_word}
print(result)
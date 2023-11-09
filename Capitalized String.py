Name = "punit kumar singh"
words = Name.split() 
capitalized_words = [word[0].upper() + word[1:] for word in words]
capitalized_string = ' '.join(capitalized_words)
print(capitalized_string)
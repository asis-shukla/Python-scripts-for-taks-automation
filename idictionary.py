import json

file_ptr = open("dict_data.json", "r")  # Create a file pointer to dictionary data stored in disk
 
d_data = json.load(file_ptr)        # load json data to d_data


while True:
    word = input("Enter your word: ")
    word = word.lower()  # Convert string enttered by the user to all lower case
    
    if word == "" or word[0:1] == " ":
        print("This is not correct, Please enter correct word! ")

    elif word in d_data.keys():
        #word is found in the dictionary, we print the each meaning as a sentence on the screen
        for sentence in d_data[word]:
            print(sentence)         
    
    else:
        print(word,  "not found in the dictionary!, check for spelling error or enter another word!")
    

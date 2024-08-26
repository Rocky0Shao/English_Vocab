# Function to display the word and meaning
def display_vocab(vocab_list):
    for word, meaning in vocab_list.items():
        input(str(word)+"       ")
        print(f"{word} - {meaning}\n")
from Vocab_List import *
# Run the function
display_vocab(vocab_list)
def print_even_index_characters(string):
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i])
string = input("Enter a word: ")
print_even_index_characters(string)
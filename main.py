def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    string = "".join(string_list)
    return string


if __name__ == "__main__":

#inputs from user

    string = input("enter string: ")
    position = input("enter index position: ")
    character = input("enter character: ")

#call function
new_string = mutate_string(string, int(position), character)

#print mutated string
print(new_string)
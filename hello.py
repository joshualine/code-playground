def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    string = ""
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3: new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return string.join(char_list)

print(urlify_algo('replace the neccessary things correctly let us see', 1))


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(" ", "%20")


print(urlify_pythonic("replace the neccessary things correctly let us see", 0))


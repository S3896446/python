def no_of_palindrome_strings(strings_list):
    return strings_list == strings_list[::-1]

if __name__ == "__main__":
    strings_list = ["madam", "radar", "level", "eye", "asd"]
    for s in strings_list:
        if no_of_palindrome_strings(s):
            print(f"'{s}' is a palindrome.")
        else:
            print(f"'{s}' is not a palindrome.")

   


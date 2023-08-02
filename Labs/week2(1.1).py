#Write a Python program to count the number of strings where the string length is 2 or more and the
#first and last character are same from a given list of strings.
def no_of_matching_strings(strings_list):
    count = 0
    for s in strings_list:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

if __name__ == "__main__":
    # Sample list of strings
    strings_list = ["hello", "world", "python", "level", "eye", "apple", "radar"]

    matching_count = no_of_matching_strings(strings_list)
    print("Number of strings with length 2 or more and first and last characters the same are ", matching_count)

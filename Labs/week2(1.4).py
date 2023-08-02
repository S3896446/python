class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string[::-1]
       

    def reverse_words(self):
        words = self.input_string
        return words

if __name__ == "__main__":
    input_strings = ["hello .py", "this is a test", "python programming"]
    
    for s in input_strings:
        reverser = StringReverser(s)
        words = reverser.reverse_words()
        print(f"Input: '{s}'\nReversed: '{words}'\n")

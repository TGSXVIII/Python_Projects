# Function to convert a word to binary
def word_to_binary(word):
    binary_string = ""

    for char in word:
        binary_char = bin(ord(char))[2:]  # Convert character to binary, remove '0b' prefix
        binary_char = binary_char.zfill(8)  # Ensure each binary representation is 8 characters long
        binary_string += binary_char

    return binary_string


# Main program
if __name__ == "__main__":
    input_word = input("Enter a word: ")
    binary_representation = word_to_binary(input_word)

    print("Binary representation of the word:", binary_representation)

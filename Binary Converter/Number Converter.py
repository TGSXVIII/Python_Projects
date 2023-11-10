# Function to convert a number to binary
def number_to_binary(number):
    binary_representation = bin(number)[2:]  # Convert the number to binary, remove '0b' prefix
    return binary_representation

# Main program
if __name__ == "__main__":
    try:
        input_number = int(input("Enter a number: "))
        binary_representation = number_to_binary(input_number)
        print("Binary representation of the number:", binary_representation)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

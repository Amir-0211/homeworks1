##                                              EXCEPTION HANDLIING EXERCISES






##1



def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        result = numerator / denominator
        print(f"The result is: {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please provide a non-zero denominator.")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    finally:
        print("Operation completed.")

divide_numbers()



##2




def get_integer_input():
    try:
        user_input = input("Enter an integer: ")
        integer_value = int(user_input)
        print(f"Valid integer entered: {integer_value}")
    except ValueError:
        raise ValueError("Invalid input! Please enter a valid integer.")


try:
    get_integer_input()
except ValueError as e:
    print(e)





##3




def open_file():
    try:
        file_name = input("Enter the file name to open: ")
        
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

open_file()




##4



def get_two_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
            raise TypeError("Both inputs must be numerical values.")
        
        num1 = float(num1)
        num2 = float(num2)

        print(f"The numbers entered are: {num1} and {num2}")
    
    except TypeError as e:
        print(e)

get_two_numbers()




##5



def open_file_with_permission_check():
    try:
        file_name = input("Enter the file name to open: ")
        
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except PermissionError:
        print(f"Error: You do not have permission to access the file '{file_name}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


open_file_with_permission_check()




##6




def access_list_element():
    try:
        my_list = [10, 20, 30, 40, 50]
        print(f"List: {my_list}")
        
        index = int(input("Enter the index of the element you want to access: "))
        
        element = my_list[index]
        print(f"Element at index {index} is: {element}")
    
    except IndexError:
        print("Error: The index is out of range. Please enter a valid index.")
    
    except ValueError:
        print("Error: Please enter a valid integer for the index.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


access_list_element()




##7





def get_user_input():
    try:
        number = float(input("Enter a number: "))
        print(f"You entered: {number}")
    
    except KeyboardInterrupt:
        print("\nInput cancelled by the user.")
    
    except ValueError:
        print("Error: Please enter a valid number.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Program terminated.")


get_user_input()




##8




def perform_division():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        result = numerator / denominator
        print(f"The result of the division is: {result}")
    
    except ArithmeticError as e:
        print(f"Arithmetic error occurred: {e}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

perform_division()




##9



def open_file_with_encoding_check():
    try:
        file_name = input("Enter the file name to open: ")
        
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except UnicodeDecodeError:
        print(f"Error: The file '{file_name}' could not be decoded with UTF-8 encoding.")
        print("Tip: Try opening the file with a different encoding.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    
    except PermissionError:
        print(f"Error: You do not have permission to access the file '{file_name}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


open_file_with_encoding_check()




##10



def execute_list_operation():
    try:
        my_list = [1, 2, 3, 4, 5]
        print(f"List: {my_list}")
        
        operation = input("Enter the list operation (e.g., 'append', 'sort', 'nonexistent'): ").strip()
        
        if operation == "append":
            value = input("Enter a value to append: ")
            my_list.append(value)
            print(f"Updated list: {my_list}")
        elif operation == "sort":
            my_list.sort()
            print(f"Sorted list: {my_list}")
        else:
            getattr(my_list, operation)()
    
    except AttributeError:
        print(f"Error: '{operation}' is not a valid list operation or attribute.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

execute_list_operation()










##                                                  FILE HANDLING EXERCISES








##1




def read_text_file():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        with open(file_name, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{file_name}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_text_file()



##2




def read_first_n_lines():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        n = int(input("Enter the number of lines to read: "))
        
        with open(file_name, 'r') as file:
            print(f"\nFirst {n} lines of the file:")
            for i, line in enumerate(file):
                if i >= n:
                    break
                print(line, end='') 
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except ValueError:
        print("Error: Please enter a valid integer for the number of lines.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_first_n_lines()





##3




def append_and_display_file():
    try:
        file_name = input("Enter the name of the file to append to: ")
        
        text_to_append = input("Enter the text to append: ")
        
        with open(file_name, 'a') as file:
            file.write(text_to_append + '\n') 
        
        with open(file_name, 'r') as file:
            print("\nUpdated file content:")
            print(file.read())
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except PermissionError:
        print(f"Error: You do not have permission to modify the file '{file_name}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

append_and_display_file()





##4





def read_last_n_lines():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        n = int(input("Enter the number of last lines to read: "))
        
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        print(f"\nLast {n} lines of the file:")
        for line in lines[-n:]:
            print(line, end='')  
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except ValueError:
        print("Error: Please enter a valid integer for the number of lines.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_last_n_lines()





##5




def read_last_n_lines():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        n = int(input("Enter the number of last lines to read: "))
        
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        print(f"\nLast {n} lines of the file:")
        for line in lines[-n:]:
            print(line, end='') 
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except ValueError:
        print("Error: Please enter a valid integer for the number of lines.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_last_n_lines()





##6




def read_file_into_variable():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        with open(file_name, 'r') as file:
            lines = file.readlines() 
        
        print("\nFile content stored in the variable:")
        print(lines)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_into_variable()






##7




def read_file_into_array():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        with open(file_name, 'r') as file:
            array = [line.strip() for line in file]  
        
        print("\nLines stored in an array:")
        print(array)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_into_array()





##8





def find_longest_words():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        with open(file_name, 'r') as file:
            words = file.read().split()  
            max_length = max(len(word) for word in words)  
            longest_words = [word for word in words if len(word) == max_length] 
        
        print("\nLongest words in the file:")
        for word in longest_words:
            print(word)
        print(f"\nLength of the longest word(s): {max_length}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

find_longest_words()






##9





def count_lines_in_file():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        with open(file_name, 'r') as file:
            line_count = sum(1 for line in file)
        
        print(f"\nThe number of lines in the file '{file_name}' is: {line_count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

count_lines_in_file()






##10





from collections import Counter

def count_word_frequency():
    try:
        file_name = input("Enter the name of the text file to read: ")
        
        with open(file_name, 'r') as file:
            content = file.read()
        
        words = content.lower().split()  
        words = [word.strip('.,!?;"()[]') for word in words]  
        
        word_count = Counter(words)
        
        print("\nWord frequencies in the file:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

count_word_frequency()





##11





import os

def get_file_size():
    try:
        file_name = input("Enter the name of the file to check size: ")
        
        file_size = os.path.getsize(file_name)
        
        print(f"The size of the file '{file_name}' is: {file_size} bytes")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

get_file_size()





##12





def write_list_to_file():
    try:
        sample_list = ['Python', 'is', 'fun', 'and', 'powerful']
        print(f"Writing the following list to the file: {sample_list}")
        
        file_name = input("Enter the name of the file to write to: ")
        
        with open(file_name, 'w') as file:
            for item in sample_list:
                file.write(item + '\n') 
        
        print(f"The list has been successfully written to '{file_name}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

write_list_to_file()





##13





def copy_file_contents():
    try:
        source_file = input("Enter the name of the source file: ")
        destination_file = input("Enter the name of the destination file: ")
        
        with open(source_file, 'r') as src:
            content = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(content)
        
        print(f"Contents of '{source_file}' have been successfully copied to '{destination_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

copy_file_contents()






##14




def combine_lines_from_files():
    try:
        file1_name = input("Enter the name of the first file: ")
        file2_name = input("Enter the name of the second file: ")
        output_file_name = input("Enter the name of the output file: ")
        
        with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()
        
        with open(output_file_name, 'w') as output_file:
            for line1, line2 in zip(file1_lines, file2_lines):
                combined_line = line1.strip() + " " + line2.strip() + "\n"
                output_file.write(combined_line)
        
        print(f"The lines from '{file1_name}' and '{file2_name}' have been combined and written to '{output_file_name}'.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

combine_lines_from_files()






##15




import random

def read_random_line():
    try:
        file_name = input("Enter the name of the file: ")
        
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        if lines:
            random_line = random.choice(lines).strip()
            print(f"Random line from the file: {random_line}")
        else:
            print("The file is empty.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_random_line()






##16





def check_file_closed():
    try:
        file_name = input("Enter the name of the file: ")
        
        with open(file_name, 'r') as file:
            print(f"File '{file_name}' is open inside the 'with' block.")
            print(f"Is the file closed? {file.closed}")  
        
        print(f"File '{file_name}' is now outside the 'with' block.")
        print(f"Is the file closed? {file.closed}") 
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

check_file_closed()





##17






def remove_newline_characters():
    try:
        file_name = input("Enter the name of the file to process: ")
        output_file_name = input("Enter the name of the output file: ")
        
        with open(file_name, 'r') as file:
            lines = file.readlines()  
        
        with open(output_file_name, 'w') as output_file:
            for line in lines:
                output_file.write(line.strip())  
        
        print(f"Newline characters have been removed and saved to '{output_file_name}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

remove_newline_characters()






##18






def count_words_in_file():
    try:
        file_name = input("Enter the name of the text file: ")
        
        with open(file_name, 'r') as file:
            content = file.read()
        
        words = content.replace(',', ' ').split()
        
        word_count = len(words)
        
        print(f"The number of words in the file '{file_name}' is: {word_count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

count_words_in_file()






##19





import os

def extract_characters_from_files():
    try:
        folder_path = input("Enter the folder path containing text files: ")
        
        text_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
        
        if not text_files:
            print("No text files found in the specified folder.")
            return
        
        characters_list = []
        
        for text_file in text_files:
            file_path = os.path.join(folder_path, text_file)
            with open(file_path, 'r') as file:
                content = file.read()
                characters_list.extend(list(content))  
        
        print("\nExtracted characters:")
        print(characters_list)
    
    except FileNotFoundError:
        print("Error: The specified folder does not exist.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

extract_characters_from_files()





##20






import string
import os

def generate_alphabet_files():
    try:
        folder_name = "Alphabet_Files"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        
        for letter in string.ascii_uppercase:
            file_path = os.path.join(folder_name, f"{letter}.txt")
            with open(file_path, 'w') as file:
                file.write(f"This is the content of {letter}.txt\n")
        
        print(f"26 files (A.txt to Z.txt) have been successfully created in the '{folder_name}' directory.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

generate_alphabet_files()






##21





import string

def create_alphabet_file(letters_per_line):
    try:
        file_name = "alphabet.txt"
        
        alphabet = string.ascii_uppercase
        
        with open(file_name, 'w') as file:
            for i in range(0, len(alphabet), letters_per_line):
                file.write(' '.join(alphabet[i:i+letters_per_line]) + '\n')
        
        print(f"File '{file_name}' has been created with {letters_per_line} letters per line.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

letters_per_line = int(input("Enter the number of letters per line: "))
create_alphabet_file(letters_per_line)














##                                      CAR CLASS







class Car:
    def __init__(self, yearModel, make):
        """Initializer to set yearModel, make, and default speed."""
        self.yearModel = yearModel
        self.make = make
        self.speed = 0

    def accelerate(self):
        """Increase the speed by 5."""
        self.speed += 5

    def brake(self):
        """Decrease the speed by 5."""
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        """Return the current speed."""
        return self.speed


def main():
    my_car = Car(2022, "Toyota")
    
    print(f"Car created: {my_car.yearModel} {my_car.make}")
    print("Initial speed:", my_car.get_speed())

    print("\nAccelerating...")
    for i in range(5):
        my_car.accelerate()
        print(f"Speed after accelerate {i + 1}: {my_car.get_speed()}")

    print("\nBraking...")
    for i in range(5):
        my_car.brake()
        print(f"Speed after brake {i + 1}: {my_car.get_speed()}")


if __name__ == "__main__":
    main()












##                                                          MODEL A FARM











class Animal:
    """Parent class representing a generic animal."""

    def __init__(self, name, sound, diet):
        """Initialize common attributes for all animals."""
        self.name = name
        self.sound = sound
        self.diet = diet

    def make_sound(self):
        """Make the animal's sound."""
        return f"{self.name} says: {self.sound}"

    def eat(self):
        """Simulate eating behavior."""
        return f"{self.name} eats {self.diet}."

    def sleep(self):
        """Simulate sleeping behavior."""
        return f"{self.name} is sleeping."


class Cow(Animal):
    """Child class representing a cow."""

    def __init__(self, name):
        """Initialize the cow with specific attributes."""
        super().__init__(name, sound="Moo", diet="grass")

    def graze(self):
        """Specific behavior for cows."""
        return f"{self.name} is grazing in the field."


class Chicken(Animal):
    """Child class representing a chicken."""

    def __init__(self, name):
        """Initialize the chicken with specific attributes."""
        super().__init__(name, sound="Cluck", diet="grains")

    def lay_egg(self):
        """Specific behavior for chickens."""
        return f"{self.name} has laid an egg!"


class Pig(Animal):
    """Child class representing a pig."""

    def __init__(self, name):
        """Initialize the pig with specific attributes."""
        super().__init__(name, sound="Oink", diet="slop")

    def roll_in_mud(self):
        """Specific behavior for pigs."""
        return f"{self.name} is happily rolling in the mud."


def main():
    bessie = Cow("Bessie")
    clucky = Chicken("Clucky")
    porky = Pig("Porky")

    animals = [bessie, clucky, porky]

    print("Welcome to the farm!")
    for animal in animals:
        print(f"\n--- {animal.name} ---")
        print(animal.make_sound())
        print(animal.eat())
        print(animal.sleep())

        if isinstance(animal, Cow):
            print(animal.graze())
        elif isinstance(animal, Chicken):
            print(animal.lay_egg())
        elif isinstance(animal, Pig):
            print(animal.roll_in_mud())


if __name__ == "__main__":
    main()

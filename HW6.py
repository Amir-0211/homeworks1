import math

class Vector:
    def __init__(self, *components):
        """Initialize the vector with any number of components."""
        self.components = list(components)

    def __str__(self):
        """Return a readable string representation of the vector."""
        return f"Vector({', '.join(map(str, self.components))})"

    def __bool__(self):
        """Evaluate to False if all components are zero; otherwise True."""
        return any(self.components)

    def __add__(self, other):
        """Perform element-wise addition with another Vector."""
        if isinstance(other, Vector) and len(self) == len(other):
            return Vector(*(a + b for a, b in zip(self.components, other.components)))
        raise ValueError("Vectors must be of the same length for addition.")

    def __sub__(self, other):
        """Perform element-wise subtraction with another Vector."""
        if isinstance(other, Vector) and len(self) == len(other):
            return Vector(*(a - b for a, b in zip(self.components, other.components)))
        raise ValueError("Vectors must be of the same length for subtraction.")

    def __mul__(self, other):
        """Perform element-wise multiplication with another Vector."""
        if isinstance(other, Vector) and len(self) == len(other):
            return Vector(*(a * b for a, b in zip(self.components, other.components)))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        raise ValueError("Invalid operand for multiplication.")

    def __truediv__(self, scalar):
        """Divide the vector by a scalar."""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(*(a / scalar for a in self.components))
        raise ValueError("Division requires a non-zero scalar.")

    def __eq__(self, other):
        """Check if two vectors have the same components."""
        if isinstance(other, Vector):
            return self.components == other.components
        return False

    def __getitem__(self, index):
        """Get a component by index."""
        return self.components[index]

    def __setitem__(self, index, value):
        """Set a component by index."""
        self.components[index] = value

    def __len__(self):
        """Return the number of components in the vector."""
        return len(self.components)

    def __abs__(self):
        """Return the Euclidean norm of the vector."""
        return math.sqrt(sum(a**2 for a in self.components))

    def __neg__(self):
        """Return a vector with negated components."""
        return Vector(*(-a for a in self.components))


def main():
    v1 = Vector(3, 4, 5)
    v2 = Vector(1, 2, 3)

    print("Vector 1:", v1)
    print("Vector 2:", v2)

    print("Is Vector 1 non-zero?", bool(v1))
    print("Is Vector(Vector(0, 0, 0)) non-zero?", bool(Vector(0, 0, 0)))

    print("Addition:", v1 + v2)
    print("Subtraction:", v1 - v2)
    print("Element-wise Multiplication:", v1 * v2)

    print("Scalar Multiplication:", v1 * 2)
    print("Scalar Division:", v1 / 2)

    print("Negation of Vector 1:", -v1)

    print("Are Vector 1 and Vector 2 equal?", v1 == v2)
    print("Are Vector(1, 2, 3) and Vector(1, 2, 3) equal?", Vector(1, 2, 3) == Vector(1, 2, 3))

    print("Second component of Vector 1:", v1[1])
    v1[1] = 10
    print("Updated Vector 1:", v1)

    print("Number of components in Vector 1:", len(v1))

    print("Euclidean norm of Vector 1:", abs(v1))

if __name__ == "__main__":
    main()











##                                      CONSOLE NOTEBOOK APPLICATION









import json
import uuid
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def show_all_notes(notes):
    if not notes:
        print("\nNo notes found.")
    else:
        print("\nAll Notes:")
        for note in notes:
            print(f"ID: {note['id']}, Created Date: {note['created_date']}")

def show_note_details(notes):
    note_id = input("Enter the ID of the note to view: ")
    for note in notes:
        if note['id'] == note_id:
            print(f"\nID: {note['id']}")
            print(f"Created Date: {note['created_date']}")
            print(f"Text: {note['text']}")
            return
    print("Note not found.")

def create_note(notes):
    text = input("Enter the note text: ")
    note_id = str(uuid.uuid4())  # Generate a unique ID
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {"id": note_id, "text": text, "created_date": created_date}
    notes.append(new_note)
    save_notes(notes)
    print("Note created successfully.")

def update_note(notes):
    note_id = input("Enter the ID of the note to update: ")
    for note in notes:
        if note['id'] == note_id:
            new_text = input("Enter the new text for the note: ")
            note['text'] = new_text
            save_notes(notes)
            print("Note updated successfully.")
            return
    print("Note not found.")

def delete_note(notes):
    note_id = input("Enter the ID of the note to delete: ")
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully.")
            return
    print("Note not found.")

def main_menu():
    notes = load_notes()
    while True:
        print("\nNotebook Application")
        print("1. Show All Notes")
        print("2. Show Note Details")
        print("3. Create Note")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_notes(notes)
        elif choice == '2':
            show_note_details(notes)
        elif choice == '3':
            create_note(notes)
        elif choice == '4':
            update_note(notes)
        elif choice == '5':
            delete_note(notes)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

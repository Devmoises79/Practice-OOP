class Person:
    """
    A simple Person class to store personal information.
    """

    def __init__(self, name, age, height, phrase):
        """
        Initialize a new Person instance.

        Args:
            name (str): The person's name.
            age (int): The person's age.
            height (float): The person's height in meters.
            phrase (str): A phrase associated with the person.
        """
        self.name = name
        self.age = age
        self.height = height
        self.phrase = phrase


# Create an instance of Person
person = Person("Marie", 21, 1.75, "My name is Marie.")

# Print the information
print("====== Welcome to my Person class! ======\n")
print("The objects are:\n")
print(person.name, "\n")
print(person.age, "\n")
print(person.height, "\n")
print(person.phrase, "\n")
print("See you soon!")
print("===== This is the end of my class! =====")

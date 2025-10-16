# 🧑‍💻 Person Class Project

A simple Python project that demonstrates how to create and use a class (`Person`) with attributes and instance methods.  
This example is useful for beginners learning Object-Oriented Programming (OOP) in Python.

---

## 📘 Description

The `Person` class stores basic information about a person, such as:

- **Name**
- **Age**
- **Height**
- **Phrase**

It also demonstrates how to:
- Create a class with the `__init__` constructor.
- Instantiate an object.
- Access and print its attributes.

---

## 🧩 Code Example

```python
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
```



# Create an instance of Person
person = Person("Moisés", 21, 1.83, "My name is Moisés.")

# Print the information
```bash
print("====== Welcome to my Person class! ======\n")
print("The objects are:\n")
print(person.name, "\n")
print(person.age, "\n")
print(person.height, "\n")
print(person.phrase, "\n")
print("See you soon!")
print("===== This is the end of my class! =====")
```


🧠 Output Example

```bash
Copiar código
====== Welcome to my Person class! ======

The objects are:

Moisés 

21 

1.83 

My name is Moisés. 

See you soon!
===== This is the end of my class! =====

```

## 🚀 How to Run
- Make sure you have Python 3.10+ installed.

- Save the code above in a file named person.py.

- Run it from your terminal or IDE:

```bash
Copy code
python person.py
```

# 🧾 Author
- Moisés

* 📍 Python Student | Exploring Object-Oriented Programming
* 💬 “This is the end of my class!” 😄

<i>This project has been created as part of the 42 curriculum by jamsilva</i>

# 🐍 Python_Module_0-4

![Language](https://img.shields.io/badge/language-Python-blue.svg)
![42](https://img.shields.io/badge/42-Python-black.svg)
![Status](https://img.shields.io/badge/status-Completed-success.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB.svg)
![Flake8](https://img.shields.io/badge/flake8-passing-brightgreen.svg)
![Mypy](https://img.shields.io/badge/mypy-checked-blue.svg)

## Description

Python_Module_0-4 covers the Python track of the 42 curriculum, from Module 00 to Module 04. The goal is to build a solid foundation in Python — from core syntax to data engineering and resilient systems — while gaining a deeper understanding of object-oriented design, error handling, data structures, and file persistence.

The project is structured as the cultivation of a digital garden, where each module adds a new layer of complexity and robustness to the system.

Through this project, I learned how Python handles typing and object models internally, how to design resilient programs around exceptions, and how to build modular, reusable, and well-tested code while respecting PEP8 and static typing standards.

---

## Project Overview

The project is organized into 5 modules, each with its own theme and focus:

| Module | Theme | Main Focus |
|:------:|-------|-------------|
| **00** | Seeds of Code | Syntax, pure functions, recursion vs. iteration, type hints |
| **01** | The Object-Oriented Garden | Classes, inheritance, encapsulation, special methods |
| **02** | Agricultural Data Engineering | Exceptions, validation, resilience |
| **03** | Data Structures in Play | Collections, comprehensions, generators |
| **04** | Cyber Archives | File persistence, streams, context managers |

All exercises were implemented following PEP8 conventions and validated with:

```bash
flake8 .
mypy .
```

---

## Features

* Pure functions with full type hint coverage
* Custom class hierarchies with inheritance and encapsulation
* Custom exception classes for domain-specific error handling
* Data processing with comprehensions and generators
* File I/O with mandatory context managers
* PEP8-compliant, statically typed source code

---

## Module Breakdown

### Module 00 — Fundamentals and Sequential Logic

The initial phase where we "plant the first seeds" of code.

* Basic syntax and variable manipulation
* Pure functions for area calculations and harvest control
* Recursion vs. iteration
* First contact with Type Hints and static checking (`mypy`)

### Module 01 — Object-Oriented Programming (OOP)

Evolving from functional code to a system organized around objects.

* Classes (`Plant`) and object instantiation
* Instance methods, protected attributes, and encapsulation
* Inheritance hierarchies (Flowers, Trees, Vegetables) and `super()`
* Class methods, static methods, and nested classes

### Module 02 — Error Handling and Resilience

Turning the program into an agricultural data engineering tool capable of handling failures.

* Exception management with `try` / `except` / `finally`
* Custom exceptions for domain-specific cases (e.g., `WaterError`)
* Data integrity through sensor validation

### Module 03 — Collections and Performance

An adventure through data structures applied to a game context.

* Advanced manipulation of `List`, `Tuple`, `Set`, and `Dict`
* Comprehensions for elegant, performant data processing
* Generators and the `yield` keyword
* Command-line arguments (`sys.argv`)

### Module 04 — Data Persistence and Streams

Preserving digital knowledge through file manipulation in the Cyber Archives.

* File read/write operations (`open`, `read`, `write`)
* Standard output (`stdout`) and error (`stderr`) streams
* Mandatory use of context managers (`with`) to avoid resource leaks

---

## Project Structure

```
.
├── module00/
│   ├── ex00/
│   ├── ex01/
│   └── main.py
├── module01/
├── module02/
├── module03/
├── module04/
└── README.md
```

---

## Instructions

### Requirements

* Python 3.10+
* flake8
* mypy
* Linux or macOS

### Run

Each exercise must be run from its respective directory.

Module 00 uses the provided test helper:

```bash
python3 main.py
```

Other modules are run directly, with the shebang `#!/usr/bin/env python3` set:

```bash
chmod +x script_name.py
./script_name.py
```

### Validate

```bash
flake8 .
mypy .
```

Both commands must return with no errors for an exercise to be considered compliant.

---

## Usage

Example of the class hierarchy introduced in Module 01:

```python
#!/usr/bin/env python3
from plant import Plant, Flower

garden = Flower(name="Rose", height=0.3)
garden.grow()
print(garden)
```

Example of custom exception handling introduced in Module 02:

```python
#!/usr/bin/env python3
from errors import WaterError

try:
    check_moisture_level(sensor_value)
except WaterError as e:
    print(f"Irrigation failure: {e}")
```

---

## Technical Choices

Some implementation decisions made during the project:

* Type hints on every function signature, checked with `mypy --strict` where applicable
* Custom exception hierarchy instead of relying on generic `Exception`
* Generators preferred over lists for large or lazy data flows
* Context managers used for every file operation, with no manual `close()` calls
* Consistent PEP8 formatting enforced with `flake8`

---

## Testing

The project was validated using:

* Custom test cases per exercise
* Edge case testing (invalid input, empty collections, malformed files)
* `flake8` for style compliance
* `mypy` for type correctness

---

## Resources

### Documentation

* Python Official Documentation — https://docs.python.org/3/
* PEP 8 — Style Guide for Python Code
* PEP 484 — Type Hints
* 42 Subject PDF

### References

* https://docs.python.org/3/
* https://peps.python.org/
* https://realpython.com/

### AI Usage

Artificial Intelligence tools were used as learning assistants for:

* Concept clarification
* Debugging guidance
* Understanding edge cases
* Code review suggestions

All implementations, testing, debugging, and final validation were completed manually by the author.

---

## What I Learned

This project strengthened my understanding of:

* Type hints and static type checking
* Object-oriented design in Python (inheritance, encapsulation, `super()`)
* Custom exception hierarchies and defensive programming
* Comprehensions and generators for efficient data processing
* Context managers and safe resource handling
* Writing PEP8-compliant, maintainable Python code

---

## Author

Jamielly R.

GitHub: https://github.com/Jamielly

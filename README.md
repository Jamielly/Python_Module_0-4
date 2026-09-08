<i>This project has been created as part of the 42 curriculum by jamsilva</i>

# 🐍 Python_Module_0-4

![Language](https://img.shields.io/badge/language-Python-blue.svg)
![42](https://img.shields.io/badge/42-Python-black.svg)
![Status](https://img.shields.io/badge/status-In%20Progress-yellow.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB.svg)
![Flake8](https://img.shields.io/badge/flake8-passing-brightgreen.svg)
![Mypy](https://img.shields.io/badge/mypy-checked-blue.svg)

## Description

`Python_Module_0-4` is my personal walkthrough of the Python track of the 42 curriculum, from Module 00 to Module 04. Each module is framed as a chapter in the life of a **digital garden**: a small simulated ecosystem of plants, sensors, and archives that grows more sophisticated — and more resilient — with every exercise.

Module 00 plants the first seeds with pure functions and basic control flow. Module 01 turns that logic into a proper object model with classes, inheritance, and encapsulation. Module 02 hardens the garden against failure with exceptions and custom error hierarchies. Module 03 puts collections, comprehensions, and command-line input to work in a small scoring/inventory game. Module 04 will close the loop with file persistence and streams.

Every exercise is written with explicit type hints where the exercise calls for them, validated with `flake8` for style and `mypy` for typing, and organized so each script can be read, run, and reasoned about on its own.

---

## Progress

| Module | Theme                     | Focus                                                        | Status         | Exercises |
|:------:|---------------------------|---------------------------------------------------------------|----------------|:---------:|
| **00** | Seeds of Code             | Syntax, functions, conditionals, iteration vs. recursion       | ✅ Complete     | 8 / 8     |
| **01** | The Object-Oriented Garden| Classes, encapsulation, inheritance, nested & static members  | ✅ Complete     | 7 / 7     |
| **02** | Garden Under Pressure     | Exceptions, custom error hierarchies, `finally`                | ✅ Complete     | 5 / 5     |
| **03** | Data Structures in Play   | Collections, `sys.argv`, comprehensions, generators            | 🚧 In progress | 2 / 7     |
| **04** | Cyber Archives            | File persistence, streams, context managers                    | ⏳ Not started  | 0 / —     |

Validation for every finished exercise:

```bash
flake8 .
mypy .
```

---

## Module Breakdown

### Module 00 — Seeds of Code

The starting point: plain functions, `input()`/`print()`, conditionals, and the first comparison between recursion and iteration.

| Exercise | File | What it does |
|:--------:|------|---------------|
| ex0 | `ft_hello_garden.py` | Prints a first greeting to the garden community |
| ex1 | `ft_garden_name.py` | Reads a garden name from `input()` and echoes its status |
| ex2 | `ft_plot_area.py` | Computes a rectangular plot's area from length and width |
| ex3 | `ft_harvest_total.py` | Sums three days of harvest input into a total |
| ex4 | `ft_plant_age.py` | Branches on a plant's age to decide if it's ready to harvest |
| ex5 | `ft_water_reminder.py` | Branches on days-since-watering to trigger a reminder |
| ex6 | `ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py` | Counts down to harvest day with both a `for` loop and a recursive function, side by side |
| ex7 | `ft_seed_inventory.py` | First fully type-hinted function (`str`, `int`, `-> None`); reports seed inventory in packets, grams, or area depending on the unit passed in |

### Module 01 — The Object-Oriented Garden

Functional code evolves into a real object model, exercise by exercise: a plain `Plant` class first, then encapsulated state, then a small inheritance tree.

| Exercise | File | What it does |
|:--------:|------|---------------|
| ex0 | `ft_garden_intro.py` | Introduces the `-> None` return-type convention and an `if __name__ == "__main__":` entry point |
| ex1 | `ft_garden_data.py` | First `Plant` class: constructor, public attributes, a `show()` method, and a small plant registry |
| ex2 | `ft_plant_growth.py` | Adds `grow()` and `age_up()` methods that mutate state over a simulated week |
| ex3 | `ft_plant_factory.py` | Builds a list of `Plant` instances and iterates over them uniformly |
| ex4 | `ft_garden_security.py` | Introduces protected attributes (`_height`, `_age`) with setters that reject invalid (negative) values |
| ex5 | `ft_plant_types.py` | Adds class-level type annotations for protected attributes and getter/setter pairs |
| ex6 | `ft_garden_analytics.py` | The full hierarchy: a nested `Statistics` class, `@staticmethod` / `@classmethod` helpers, and `Flower`, `Seed(Flower)`, and `Tree` subclasses — each overriding `show()` and calling `super()` |

### Module 02 — Garden Under Pressure

The garden learns to fail gracefully: catching built-in exceptions, raising domain-specific ones, and guaranteeing cleanup.

| Exercise | File | What it does |
|:--------:|------|---------------|
| ex0 | `ft_first_exception.py` | First `try` / `except ValueError` around an `int()` conversion that may fail |
| ex1 | `ft_raise_exception.py` | Actively `raise`s `ValueError` when a temperature reading falls outside a valid range |
| ex2 | `ft_different_errors.py` | Catches several distinct built-ins (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError`) both individually and in one combined `except (...)` block |
| ex3 | `ft_custom_errors.py` | Introduces a custom exception hierarchy: `GardenError` as the base class, with `PlantError` and `WaterError` as subclasses |
| ex4 | `ft_finally_block.py` | Uses `finally` to guarantee the watering system is always "closed", even when a `PlantError` interrupts the loop |

### Module 03 — Data Structures in Play *(in progress)*

Collections, comprehensions, and command-line input, applied to a small scoring/inventory game.

| Exercise | File | Status | What it does |
|:--------:|------|:------:|---------------|
| ex0 | `ft_command_quest.py` | ✅ Done | Reads `sys.argv`, reports the program name, argument count, and each argument in turn |
| ex1 | `ft_score_analytics.py` | ✅ Done | Parses player scores from CLI arguments, skips invalid entries, and reports totals, average, high/low, and range |
| ex2 | `ft_coordinate_system.py` | 🚧 Planned | Tuple-based coordinate handling |
| ex3 | `ft_achievement_tracker.py` | 🚧 Planned | Set operations for tracking unlocked achievements |
| ex4 | `ft_inventory_system.py` | 🚧 Planned | Dictionary-based inventory management |
| ex5 | `ft_data_stream.py` | 🚧 Planned | Generators and `yield` for lazy data streaming |
| ex6 | `ft_data_alchemist.py` | 🚧 Planned | Comprehensions for transforming collections |

### Module 04 — Cyber Archives *(not started)*

The next chapter: persisting the garden's data to disk.

* File read/write operations (`open`, `read`, `write`)
* Standard output (`stdout`) and error (`stderr`) streams
* Mandatory use of context managers (`with`) to avoid resource leaks

---

## Project Structure

```
.
├── Python_Module_00/
│   ├── ex0/ft_hello_garden.py
│   ├── ex1/ft_garden_name.py
│   ├── ex2/ft_plot_area.py
│   ├── ex3/ft_harvest_total.py
│   ├── ex4/ft_plant_age.py
│   ├── ex5/ft_water_reminder.py
│   ├── ex6/ft_count_harvest_iterative.py
│   ├── ex6/ft_count_harvest_recursive.py
│   └── ex7/ft_seed_inventory.py
├── Python_Module_01/
│   ├── ex0/ft_garden_intro.py
│   ├── ex1/ft_garden_data.py
│   ├── ex2/ft_plant_growth.py
│   ├── ex3/ft_plant_factory.py
│   ├── ex4/ft_garden_security.py
│   ├── ex5/ft_plant_types.py
│   └── ex6/ft_garden_analytics.py
├── Python_Module_02/
│   ├── ex0/ft_first_exception.py
│   ├── ex1/ft_raise_exception.py
│   ├── ex2/ft_different_errors.py
│   ├── ex3/ft_custom_errors.py
│   └── ex4/ft_finally_block.py
├── Python_Module_03/
│   ├── ex0/ft_command_quest.py
│   ├── ex1/ft_score_analytics.py
│   ├── ex2/ft_coordinate_system.py     # planned
│   ├── ex3/ft_achievement_tracker.py   # planned
│   ├── ex4/ft_inventory_system.py      # planned
│   ├── ex5/ft_data_stream.py           # planned
│   └── ex6/ft_data_alchemist.py        # planned
├── Glossary python 42.pdf
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

Module 00 exercises are plain functions with no `__main__` guard — they're meant to be imported and called directly:

```bash
python3 -c "from ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

From Module 01 onward, every script carries a shebang and an `if __name__ == "__main__":` block, so it can be run on its own:

```bash
chmod +x ft_garden_analytics.py
./ft_garden_analytics.py
```

or simply:

```bash
python3 ft_garden_analytics.py
```

### Validate

```bash
flake8 .
mypy .
```

Both commands must return with no errors for an exercise to be considered compliant.

---

## Usage

Inheritance hierarchy from Module 01 (`ft_garden_analytics.py`):

```python
#!/usr/bin/env python3
rose = Flower("Rose", 15.0, 10, "red")
rose.grow()
rose.bloom()
rose.show()
# Rose: 23.0cm, 10 days old
# Color: red
# Rose is blooming beautifully!
```

Custom exception hierarchy from Module 02 (`ft_custom_errors.py`):

```python
#!/usr/bin/env python3
try:
    check_water(tank_empty=True)
except WaterError as error:
    print(f"Caught WaterError: {error}")
```

Command-line score analytics from Module 03 (`ft_score_analytics.py`):

```bash
python3 ft_score_analytics.py 88 92 abc 74 100
# Invalid parameter: 'abc'
# Scores processed: [88, 92, 74, 100]
# Total players: 4
# ...
```

---

## Technical Choices

* Type hints on every function and method signature from Module 00's last exercise onward, checked with `mypy`
* Protected attributes (`_name`, `_height`, …) with validating setters instead of raw public state
* A dedicated exception hierarchy (`GardenError → PlantError`, `WaterError`) instead of relying on generic `Exception`
* `super()` used consistently across the `Plant → Flower → Seed` and `Plant → Tree` hierarchies
* Consistent PEP 8 formatting enforced with `flake8`

---

## Testing

Each exercise is validated by:

* Manual execution against the expected 42 subject output
* Edge-case checks (invalid input, out-of-range values, missing arguments)
* `flake8` for style compliance
* `mypy` for type correctness

---

## Resources

### Documentation

* [Python Official Documentation](https://docs.python.org/3/)
* PEP 8 — Style Guide for Python Code
* PEP 484 — Type Hints
* `Glossary python 42.pdf` — the 42-provided glossary included in this repository

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

* Writing pure functions and reasoning about recursion vs. iteration
* Object-oriented design in Python — encapsulation, inheritance, `super()`, nested classes
* Custom exception hierarchies and defensive programming with `try` / `except` / `finally`
* Parsing and validating command-line input with `sys.argv`
* Type hints and static type checking with `mypy`
* Writing PEP8-compliant, maintainable Python code

---

## Author

**Jamielly R.**
GitHub: https://github.com/Jamielly

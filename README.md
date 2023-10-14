# 0x00. AirBnB clone - The console

Background Context

Welcome to the AirBnB clone project!

First step: Writing a command interpreter to manage AirBnB objects.
This is the first step towards building my first full web application: the AirBnB clone. This first step is very important because it will be used to build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help in:

putting in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
creating all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
creating the first abstracted storage engine of the project: File storage.
creating all unittests to validate all our classes and storage engine

# Using ’s command interpreter to manage the project
Creating a new object (ex: a new User or a new Place)
Retrieving an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

# working environment

This is a joint project involving 2 people, Jeff and Brenda using the pycodestyle (version 2.8.*)and tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

# Execution method used:

The shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

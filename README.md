# Airbnb clone - The CONSOLE

Team project to build a clone of AirBnB.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the Wiki.

The console willl perform the following tasks:

create a new object
retrive an object from a file
do operations on objects
destroy an object

## Installation, Usage & Example
```bash
   git clone https://github.com/Mmah-Zombo/AirBnB_clone.git
```

change to the AirBnb directory and enter the following command to run the program:
```bash
   ./console.py
```

Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```bash
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
```

## AUTHORS
> M'mah Zombo

My teammate deferred to another cohort, so I have built this program alone
# AirBnB Clone - The Console

## Description
This project is the first step toward building a full-stack clone of
the AirBnB web application. This first part implements a command-line
interpreter (the "console") used to manage the objects of the project:
create, update, destroy, and show objects, all through a simple shell.

Behind the console sit two building blocks:
- `BaseModel`: the parent class every future model (User, State, City,
  Place, etc.) will inherit from. It handles unique IDs, creation and
  update timestamps, and dictionary serialization.
- `FileStorage`: the storage engine that converts objects to/from JSON
  and writes/reads them to a file (`file.json`), so data persists
  between runs of the program.

## Command Interpreter

### How to start it
Make the file executable and run it directly, or call it with Python:

    $ ./console.py

or

    $ python3 console.py

### How to use it
The console runs as an interactive shell. Type a command and press
Enter; type `help` to see the list of commands, `help <command>` for
details on one, and `quit` or `EOF` (Ctrl+D) to exit.

It can also run in non-interactive mode, reading commands piped from
another program:

    $ echo "help" | ./console.py

### Examples

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    help  quit

    (hbnb) quit
    $

    $ echo "quit" | ./console.py
    (hbnb)
    $

## Authors
See the [AUTHORS](AUTHORS) file.

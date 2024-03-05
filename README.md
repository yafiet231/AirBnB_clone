# AirBnB clone - The console

#### Description
> This team project mainly aims to build Console part of a clone of [AirBnB](https://www.airbnb.com/). 
> This repository contains a console (command interpreter) which ables to manage AirBnB clone objects.
> The repository also contains parent or base class, child classes inherited from the basemodel and tests.
#### Command Interpreter
Command interpreter is a shell like with limited to a specific use-case. In this project the Command interpreter will help to manage the objects of our project, Like:
* To create a new object
* To retrive an object from a file, database, etc..
* To update attributes of an object
* To do operations on objects (count, compute stats, etc…)
* To destroy an object

#### Environment
* Language: Python3
* OS: Ubuntu 20.04 LTS

#### How to Start the Command Interpreter
To start the command interpreter, follow these steps:
- Clone the project repository to your local machine.
 ```bash
git clone git@github.com:Mahari9/AirBnB_clone.git
cd AirBnB_clone
```
- Navigate to the directory containing the project files.
  ```bash
cd AirBnB_clone
```
- Run the console.py file with: "./console.py" or "python console.py"
- And finallyType "help" in the console for documentation.

Interactive Mode
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
Non-Interactive Mode
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
#### How to Use Command Interpreter
---
| Commands  |        Usage                                  | Result                                        |
| --------- | --------------------------------------------- | ------------------------------------------    |
| `help`    | `help`                                        | displays list of all commands available       |
| `create`  | `create <class>`                              | creates new instance                          |
| `update`  | `User.update('7', {'name' : 'Hello'})`        | updates attribute of an instance              |
| `destroy` | `User.destroy('7')`                           | destroys specified instance                   |
| `show`    | `User.show('7')`                              | retrieve an instance  from a file, a database |
| `all`     | `User.all()`                                  | display all instance  in class                |
| `count`   | `User.count()`                                | returns count of instance  in specified class |
| `quit`    | `quit`                                        | exits                                         |

### Testing
Within the project, we have incorporated unit tests to verify the accuracy of the implemented functionality. To execute these tests, follow the instructions below:
- "python3 -m unittest discover tests" (interactive mode)
- "echo 'python3 -m unittest discover tests' | bash" (Non-interactive mode)


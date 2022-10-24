# AirBnB -Console

This console is a command interpreter similar to [hsh](https://github.com/3akare/simple_shell), but limited to a specific use-case.

## Functionalities of the console:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

This console is the first step towards building a full web application: the [AirBnB](airbnb.com) clone. The console allows us to understand what works in the storage engine and what doesn't

<img src='AirBnB-image.png' width=70%></img>

# Execution
This console works like this in interactive mode
```shell
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode
```shell
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | .console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
```
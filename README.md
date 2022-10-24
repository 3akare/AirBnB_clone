# AirBnB -Console

This console is a command interpreter similar to [hsh](//https://github.com/3akare/simple_shell), but limited to a specific use-case.

## Functionalities of the command intepreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do Operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

<img src='https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Credential%3DAKIARDDGGGOUSBVO6H7D%2F20221024%2Fus-east-1%2Fs3%2Faws4_request%26X-Amz-Date%3D20221024T120517Z%26X-Amz-Expires%3D86400%26X-Amz-SignedHeaders%3Dhost%26X-Amz-Signature%3D98df33f0b6ba6bdc3d1f1c6337bb4fe156e6aa08ab297cc306a3a6c3bd7a047e'></img>

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
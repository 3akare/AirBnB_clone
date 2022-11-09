# AirBnB - Console

This console is a command interpreter similar to [hsh](https://github.com/3akare/simple_shell), but limited to a specific use-case.

## Functionalities of the console:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

This console is the first step towards building a full web application: the [AirBnB](airbnb.com) clone. The console allows us to understand what works in the storage engine and what doesn't

<img src='README.png' width=70%></img>

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
# Installation
Clone this repository
```
git clone "https://github.com/3akare/AirBnB_clone.git"
```
Access AirBnb directory
```shell
cd AirBnB_clone
```
Run hbnb(interactively)
```shell
 ./console.py
```
Run hbnb (non-interactively)
```shell
echo "<command>" | ./console.py
```
# Usage
## Available Classes
- BaseModel
- User - Inherits from `BaseModel`
- State - Inherits from `BaseModel`
- Review - Inherits from `BaseModel`
- Amenity - Inherits from `BaseModel`
- Place - Inherits from `BaseModel`
- City - Inherits from `BaseModel`

Note: instances are saved in json format located at `file.json`

## Console Commands
- ### create
    usage: `create <class>`

    creates a new instance of the class and prints the id of the instance on success
```shell
$ ./console.py
(hbnb) create User
eea3c738-1842-4afe-a47c-a6efa0d4db41
```
- ### show
    usage: `show <classname> <instance id>`
    
    prints out a string representation of a class instance based on the given id
```shell
$./console.py
(hbnb) create BaseModel
333852b9-1e07-4776-bd9f-4bda55faa7e7
(hbnb) show BaseModel 333852b9-1e07-4776-bd9f-4bda55faa7e7
[BaseModel] (333852b9-1e07-4776-bd9f-4bda55faa7e7) {'id': '333852b9-1e07-4776-bd9f-4bda55faa7e7', 'created_at': datetime.datetime(2022, 11, 9, 15, 5, 44, 858267), 'updated_at': datetime.datetime(2022, 11, 9, 15, 5, 44, 858306)}
(hbnb)
```
- ### destroy
    usage: `destory <classname> <id>`

    deletes an instance based on the given id
```shell
$ ./console.py
(hbnb) create Place
a91a3ef0-7605-4954-8ead-f96d846f4f7f
(hbnb) show Place a91a3ef0-7605-4954-8ead-f96d846f4f7f
[Place] (a91a3ef0-7605-4954-8ead-f96d846f4f7f) {'id': 'a91a3ef0-7605-4954-8ead-f96d846f4f7f', 'created_at': datetime.datetime(2022, 11, 9, 15, 9, 13, 224981), 'updated_at': datetime.datetime(2022, 11, 9, 15, 9, 13, 225019)}
(hbnb) destroy Place a91a3ef0-7605-4954-8ead-f96d846f4f7f
(hbnb) show Place a91a3ef0-7605-4954-8ead-f96d846f4f7f
** no instance found **
```

- ### all
    usage: `all <classname>`

    prints out available instances of the given class
```shell
$ console.py
(hbnb) all Amenity
[]
(hbnb) create Amenity
1a6400cd-5d5a-42b8-93b6-552736553ca4
(hbnb) create Amenity
aa282422-3d7e-471a-bf2b-0ebb15b53d32
(hbnb) all Amenity
["[Amenity] (1a6400cd-5d5a-42b8-93b6-552736553ca4) {'id': '1a6400cd-5d5a-42b8-93b6-552736553ca4', 'created_at': datetime.datetime(2022, 11, 9, 15, 13, 56, 598305), 'updated_at': datetime.datetime(2022, 11, 9, 15, 13, 56, 598360)}", "[Amenity] (aa282422-3d7e-471a-bf2b-0ebb15b53d32) {'id': 'aa282422-3d7e-471a-bf2b-0ebb15b53d32', 'created_at': datetime.datetime(2022, 11, 9, 15, 13, 57, 562213), 'updated_at': datetime.datetime(2022, 11, 9, 15, 13, 57, 562232)}"]
(hbnb)
```
- ### update
    usage: `update <classname> <instance id> <attribute name> <attribute value>`

    Adds and update an attribute (key, value pair) to an instance depending on the class name and instance id given
```shell
$ ./console.py
(hbnb) create City
c0bf82cb-4112-43a8-8f35-8c27bf305c35
(hbnb) show City c0bf82cb-4112-43a8-8f35-8c27bf305c35
[City] (c0bf82cb-4112-43a8-8f35-8c27bf305c35) {'id': 'c0bf82cb-4112-43a8-8f35-8c27bf305c35', 'created_at': datetime.datetime(2022, 11, 9, 15, 18, 8, 952082), 'updated_at': datetime.datetime(2022, 11, 9, 15, 18, 8, 952119)}
(hbnb) update City c0bf82cb-4112-43a8-8f35-8c27bf305c35 name Abuja
(hbnb) show City c0bf82cb-4112-43a8-8f35-8c27bf305c35
[City] (c0bf82cb-4112-43a8-8f35-8c27bf305c35) {'id': 'c0bf82cb-4112-43a8-8f35-8c27bf305c35', 'created_at': datetime.datetime(2022, 11, 9, 15, 18, 8, 952082), 'updated_at': datetime.datetime(2022, 11, 9, 15, 18, 8, 952119), 'name': 'Abuja'}
```
# Authors
- [David Bakare](https://github.com/3akare)

# Acknowledgements
This project was written as part of the curriculum for Holberton School.
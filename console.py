#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models import storage
import os


class HBNBCommand(cmd.Cmd):
    '''Console Class'''

    prompt = "(hbnb) "
    __classes = [
        'BaseModel'
    ]

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''CTRl + D command to exit the program'''
        return True

    def emptyline(self):
        '''an empty line + ENTER doesn't execute anything'''
        pass

    def do_create(self, line):
        ''' Creates a new instance of BaseModel'''
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(line)().id)
            storage.save()

    def do_show(self, line):
        '''Prints the string representation of an instance
        based on the class name and id'''
        line = line.split(' ')
        objdict = storage.all()
        if line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line) == 0:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif f"{line[0]}.{line[1]}" not in objdict:
            print("** no instance found **")
        else:
            print(objdict[f"{line[0]}.{line[1]}"])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        line = line.split(' ')
        objdict = storage.all()
        if line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line) == 0:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif f'{line[0]}.{line[1]}' not in objdict:
            print("** not instance found **")
        else:
            del objdict[f"{line[0]}.{line[1]}"]
            storage.save()

    def do_all(self, line):
        '''Print all string representation of all
        instances based or no the classname'''
        line = line.split(' ')
        if len(line) > 0 and line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objlist = []
            for obj in storage.all().values():
                if len(line) > 0 and line[0] == obj.__class__.__name__:
                    objlist.append(obj.__str__())
                elif len(line) == 0:
                    obji.append(obj.__str__())
            print(objlist)

    def do_clear(self, line):
        '''clears the screen'''
        os.system('clear')

    def do_remove(self, line):
        '''remove json file'''
        os.remove('file.json')

    def do_update(self, line):
        '''Update an instance based in the class name and
        the id by adding or updating attribute'''
        line = line.split(' ')
        objdict = storage.all()
        try:
            if not line[0]:
                print("** class name missing **")
                return False
            if len(line) == 1:
                print("** instance id missing **")
                return False
            if len(line) == 2:
                print("** attribute name missing **")
                return False
            if f'{line[0]}.{line[1]}' not in objdict.keys():
                print("** no instance found **")
                return False
            if line[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return False
            if len(line) == 3:
                try:
                    type(eval(line[2])) != dict
                except Exception:
                    print("** value missing **")
                    return False
            if len(line) == 4:
                obj = objdict["{}.{}".format(line[0], line[1])]
                if line[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[line[2]])
                    obj.__dict__[line[2]] = valtype(line[3])
                else:
                    obj.__dict__[line[2]] = line[3]
            elif type(eval(line[2])) == dict:
                obj = objdict["{}.{}".format(line[0], line[1])]
                for k, v in eval(line[2]).items():
                    obj_keys = obj.__class__.__dict__.keys()
                    obj_dict = obj.__class__.__dict__[k]
                    if (k in obj_keys and type(obj_dict) in {str, int, float}):
                        valtype = type(obj.__class__.__dict__[k])
                        obj.__dict__[k] = valtype(v)
                    else:
                        obj.__dict__[k] = v
            storage.save()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

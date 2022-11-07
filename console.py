#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    '''Console Class'''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''CTRl + D command to exit the program'''
        return True

    def emptyline(self):
        '''an empty line + ENTER doesn't execute anything'''
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

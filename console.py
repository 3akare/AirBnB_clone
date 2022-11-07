#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    '''Console Class'''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Exit Program.'''
        return True

    def do_EOF(self, line):
        '''EOF to exit the program.'''
        return True

    def emptyline(self):
        '''Doesn't Execute anything'''
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
import cmd

class HBNBCOMMAND(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        '''Exits console\n'''
        return True
    def do_quit(self, arg):
        '''Quit command to exit the program\n'''
        return True
    def emptyline(self):
        '''Overwrites the emptyline command'''
        return False


if __name__ == '__main__':
    HBNBCOMMAND().cmdloop()

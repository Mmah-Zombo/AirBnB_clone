#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


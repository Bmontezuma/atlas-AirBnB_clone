#!/usr/bin/python3
"""Module for console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        print()
        return True

    def do_help(self, arg):
        """Help command to display available commands."""
        cmd.Cmd.do_help(self, arg)

    def do_emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

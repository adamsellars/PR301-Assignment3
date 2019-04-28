"""
# ---------------------------------------------Created by Adam----------------------------------
# Testing greeting and help messages work as expected
>>> controller = InterpreterController(ClassFinder(), ConsoleView())
>>> cmd = CommandLineInterpreter(controller)
>>> cmd.do_greet("line")
==================================================
Welcome to the command line interpreter.
Type help to view available commands
==================================================
<BLANKLINE>

# Test 2
>>> cmd.do_help("")
<BLANKLINE>
Documented commands (type help <topic>):
========================================
greet  help  load_file  print_file  quit  write_file
<BLANKLINE>

# Test 3
>>> cmd.do_help("greet")
==================================================
greet command help
==================================================
Description: A Greeting message
Syntax: greet
Parameter: none
Example: greet
<BLANKLINE>

# Test 4
>>> cmd.do_help("help")
List available commands with "help" or detailed help with "help cmd".

# Test 5
>>> cmd.do_help("load_file")
==================================================
load_file command help
==================================================
Description: Load a .txt file into the program
Syntax: load_file [path]
Parameter: [path] = full path name of the file starting from the root directory of this program
Example: load_file test4(myowncode).txt
<BLANKLINE>

# Test 6
>>> cmd.do_help("quit")
==================================================
quit command help
==================================================
Description: terminate the command line interpreter
Syntax: quit
Parameter: none
Example: quit
<BLANKLINE>

# Test 7
# surprise.txt doesn't exist should get an error message
>>> cmd.do_load_file("surprise.txt")
Error, file does not exist!

# Test 8
# this file does exist should get a success message
>>> cmd.do_load_file("test4.txt")
<BLANKLINE>
file loaded...
<BLANKLINE>

# Test 9
>>> cmd.do_quit("")
Goodbye thank you for using the command line interpreter
True

# ---------------------------------------------Created by Leroi---------------------------------
# Test 10
>>> cmd.help_print_file()
==================================================
print_file command help
==================================================
Description: Print a PEP8 format text into the interpreter
Syntax: print_file
Example: print_file test4.txt
<BLANKLINE>

# Test 11
>>> cmd.help_write_file()
==================================================
write_file command help
==================================================
Description: write a PEP8 format .txt file into path chosen
Syntax: write_file [path]
Parameter: [path] = full path name of the file starting from the root directory of this program
Example: write_file test4(myowncode).txt
<BLANKLINE>

# Test 12 try to read protected file should get permission error message
# Need to create a file with no write or read permission called no_permission.txt
# >>> cmd.do_load_file("no_permission.txt")
# Error, you do not have permission to access this file!

# tests for view
>>> view = ConsoleView()

# Test 13
>>> view.print_menu()
<BLANKLINE>
------------------------------------------------------
Press 1 to load your text file
------------------------------------------------------
Press 2 to write from plantuml text to python code
------------------------------------------------------
Press 3 to run the command line interpreter
------------------------------------------------------
Press 4 to write file to database
------------------------------------------------------
Press 5 to print class names from database to screen
------------------------------------------------------
Press 6 to load text file, convert data to PEP8 python
        format then convert file to pickle format in
        same directory
------------------------------------------------------
Press 7 to load data from pickle file
------------------------------------------------------
Press 8 to exit
------------------------------------------------------
<BLANKLINE>
<BLANKLINE>

# Test 14
>>> view.file_empty_warning()
File must not be empty

# Test 15
>>> view.file_not_loaded_warning()
Must load a file first

# Test 16
>>> view.file_type_warning()
File must be a .txt file type
"""

from view.console_view import ConsoleView
from model.class_finder import ClassFinder
from controller.interpreter_controller import InterpreterController
from controller.interpreter_controller import CommandLineInterpreter
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)

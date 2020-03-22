# Project 0x00 Shell, basics

What is the Shell, Navigation, Looking Around, Manipulating Files, Working with Commands, Reading Man Pages, Keyboard Shortcuts for Bash, LTS.

Concepts:
General

    What does RTFM mean?
    What is a Shebang

What is the Shell

    What is the shell
    What is the difference between a terminal and a shell
    What is the shell prompt
    How to use the history (the basics)

Navigation

    What do the commands or built-ins cd, pwd, ls do
    How to navigate the filesystem
    What are the . and .. directories
    What is the working directory, how to print it and how to change it
    What is the root directory
    What is the home directory, and how to go there
    What is the difference between the root directory and the home directory of the user root
    What are the characteristics of hidden files and how to list them
    What does the command cd - do

Looking Around

    What do the commands ls, less, file do
    How do you use options and arguments with commands
    Understand the ls long format and how to display it
    A Guided Tour
    What does the ln command do
    What do you find in the most common/important directories
    What is a symbolic link
    What is a hard link
    What is the difference between a hard link and a symbolic link

Manipulating Files

    What do the commands cp, mv, rm, mkdir do
    What are wildcards and how do they work
    How to use wildcards

Working with Commands

    What do type, which, help, man commands do
    What are the different kinds of commands
    What is an alias
    When do you use the command help instead of man

Reading Man Pages

    How to read a man page
    What are man page sections
    What are the section numbers for User commands, System calls and Library functions

Keyboard Shortcuts for Bash

    Common shortcuts for Bash

LTS

    What does LTS mean?


Describing each script:

0-current_working_directory is a script that will print the absolute path name of the current working directory.

1-listit is a script that will display the contents list of your current directory.

2-bring_me_home is a script that will change the working directory to the user's home directory.

3-listfiles is a script that will display current directory contents in a long format.

4-listmorefile is a script that will display current contents, including hidden files.

5-listfilesdigitonly is a script that will display current directory contents.

6-firstdirectory is a script that will creates a directory named holberton in the /tmp/ directory.

7-movethatfile is a script that will move the file betty from /tmp/ to /tmp/holberton

8-firstdelete is a script that will delete the file betty that is located in /tmp/holberton

9-firstdirdeletion is a script that will delete the directory holberton located in /tmp directory.

10-back is a script that will change the working directory to the previous one.

11-lists is a script that will list all files in the current directory and the parent of the working directory and the /boot directory in long format.

12-file_type is a script that will print the type of the file named iamafile located in /tmp.

13-symbolic_link is a script that will create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

14-copy_html is a script that will copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer that the versions in the parent of the working directory.

15-lets_move is a script that will move all files beginning with an uppercase letter to the directory.

16-clean_emacs is a script that will delete all files in the current working directory that end with the caracter ~

17-tree is a script that will create the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.

18-commas is a script that will list all the files and direcotries of the current directory, separated by commas.

holberton.mgc is a magic file, that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.

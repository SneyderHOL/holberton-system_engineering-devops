# Project 0x04-Loops, conditions, and parsing

Bash Scripts using Variables, Expansions, Shell Arithmetic, Loops, Conditions and Parsing.

Concepts:

    How to create SSH keys
    What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
    How to use while, until and for loops
    How to use if, else, elif and case condition statements
    How to use the cut command
    What are files and other comparison operators, and how to use them


Describing each script:

0-RSA_public_key.pub is a public ssh key

1-for_holberton_school is a Bash script that displays Holberton School 10 times using the for loop.

2-while_holberton_school is a Bash script that displays Holberton School 10 times using the while loop.

3-until_holberton_school is a Bash script that displays Holberton School 10 times using the until loop

4-if_9_say_hi is a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line using the while loop.

5-4_bad_luck_8_is_your_chance is a Bash script that loops from 1 to 10, and:

    displays bad luck for the 4th loop iteration
    displays good luck for the 8th loop iteration
    displays Holberton School for the other iterations

using the while loop.

6-superstitious_numbers is a Bash script that displays numbers form 1 to 20 and:

    displays 4 and then bad luck from China for the 4th loop iteration
    displays 9 and then bad luck from Japan for the 9th loop iteration
    displays 17 and then bad luck from Italy for the 17th loop iteration

using the while loop.

7-clock is a Bash script that displays the time for 12 hours and 59 minutes:

    display hours from 0 to 12
    display minutes from 1 to 59

using the while loop.

8-for_ls is a Bash script that displays:

    The content of the current directory
    In a list format
    Where only the part of the name after the first dash is displayed

using the for loop.

9-to_file_or_not_to_file is a Bash script that gives you information about the holbertonschool file.

    You must use if and, else (case is forbidden)
    Your Bash script should check if the file exists and print:
        if the file exists: holbertonschool file exists
        if the file does not exist: holbertonschool file does not exist
    If the file exists, print:
        if the file is empty: holbertonschool file is empty
        if the file is not empty: holbertonschool file is not empty
        if the file is a regular file: holbertonschool is a regular file
        if the file is not a regular file: (nothing)

10-fizzbuzz is a Bash script that displays numbers from 1 to 100.

    Displays FizzBuzz when the number is a multiple of 3 and 5
    Displays Fizz when the number is multiple of 3
    Displays Buzz when the number is a multiple of 5
    Otherwise, displays the number
    In a list format

100-read_and_cut is a Bash Script that displays the content of the file /etc/passwd.

101-tell_the_story_of_passwd is a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.

102-lets_parse_apache_logs is a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.

103-dig_the-data is a Bash script that groups visitors by IP and HTTP status code, and displays this data.

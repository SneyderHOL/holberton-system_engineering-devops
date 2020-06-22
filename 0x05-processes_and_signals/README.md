# Project 0x05 Processes and signals

Bash Scripts using Process and Signals.

Concepts:

    What is a PID
    What is a process
    How to find a process’ PID
    How to kill a process
    What is a signal
    What are the 2 signals that cannot be ignored


Describing each script:

0-what-is-my-pid is a Bash script that displays its own PID.

1-list_your_processes is a Bash script that displays a list of currently running processes.

2-show_your_bash_pid is a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

3-show_your_bash_pid_made_easy is a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

4-to_infinity_and_beyond is a Bash script that displays To infinity and beyond indefinitely.

5-kill_me_now is a Bash script that kills 4-to_infinity_and_beyond process.

6-kill_me_now_made_easy is a Bash script that kills 4-to_infinity_and_beyond process.

7-highlander is a Bash script that displays:

    To infinity and beyond indefinitely
    With a sleep 2 in between each iteration
    I am invincible!!! when receiving a SIGTERM signal

Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

8-beheaded_process is a Bash script that kills the process 7-highlander.

100-process_and_pid_file is a Bash script that:

    Creates the file /var/run/holbertonscript.pid containing its PID
    Displays To infinity and beyond indefinitely
    Displays I hate the kill command when receiving a SIGTERM signal
    Displays Y U no love me?! when receiving a SIGINT signal
    Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

101-manage_my_process is a Bash (init) script that manages manage_my_process.

    When passing the argument start:
        Starts manage_my_process
        Creates a file containing its PID in /var/run/my_process.pid
        Displays manage_my_process started
    When passing the argument stop:
        Stops manage_my_process
        Deletes the file /var/run/my_process.pid
        Displays manage_my_process stopped
    When passing the argument restart
        Stops manage_my_process
        Deletes the file /var/run/my_process.pid
        Starts manage_my_process
        Creates a file containing its PID in /var/run/my_process.pid
        Displays manage_my_process restarted
    Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed

manage_my_process is a Bash script that:

    Indefinitely writes I am alive! to the file /tmp/my_process
    In between every I am alive! message, the program should pause for 2 seconds

102-zombie.c is a C program that creates 5 zombies processes.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - function that has an infinite while
 *
 * Return: Always 0 if the loops ends
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
	pid_t child, pid;
	int i = 0;

	pid = fork();
	if (pid == -1)
	{
		perror("Error creating parent");
		return (1);
	}
	if (pid == 0)
	{
		for (i = 0; i < 5; i++)
		{
			child = fork();
			if (child == -1)
			{
				perror("Error creating child");
				return (1);
			}
			if (child == 0)
			{
				printf("Zombie process created, PID: %u\n", getpid());
				exit(0);
			}
			else
			{
				sleep(1);
				continue;
			}
			infinite_while();
		}
	}
	return (0);
}

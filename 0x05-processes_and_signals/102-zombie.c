#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Infinite while for manage zombie process
 * Void: No entry parameters
 * Return: exit 0 success
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
 * main - Main function zombie process
 * Void: No entry parameters
 * Return: Exit 0 success
 */

int main(void)
{
	int index = 0;
	pid_t zombie = 0;

	for (index = 0; index < 5; index++)
	{
		zombie = fork();

		if (zombie > 0)
			printf("Zombie process created, PID: %d\n", zombie);
		else
			exit(0);

	}

	return (infinite_while());
}

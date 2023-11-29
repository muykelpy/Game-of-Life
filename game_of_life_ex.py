## NAME

## EMAIL ADDRESS

## netID

## DUE: Thursday, Nov. 30 by 11:59pm

## GAME OF LIFE - STEP ONE ##

#Exercise 10.1: To represent the 5x5 grid at Step 1 for Conway's Game of Life,
#you need to update the grid based on the initial state and the
#rules of the Game of Life. The rules are as follows:

#1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#2. Any live cell with two or three live neighbors lives on to the next generation.
#3. Any live cell with more than three live neighbors dies, as if by overpopulation.
#4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

#Given the initial grid:

#grid = [[' ','*',' ',' ',' '],
#        ['*','*','*',' ','*'],
#        [' ',' ','*',' ',' '],
#        ['*',' ',' ',' ','*'],
 #       [' ',' ','*','*',' ']]

#We need to apply these rules to each cell to determine the next state.
#For each cell, count the number of live ('*') neighbors and apply the rules
#accordingly to determine if the cell will be alive or dead in the next step.

#Calculate the state of each cell for Step 1,
#the first step after the initial state. In this grid, use '*'
#to represent a live cell and ' ' to represent
#a dead cell. Write the next step of the game below.

#Answer:

#Explicitly writing out the value of every element in the 5×5 grid would
#be extremely tedious. What if we wanted to work with a 50×50 grid?
#This would require writing out 2,500 values—no easy task! It would be helpful
#to have a function that creates this two-dimensional list for us.
#More generally, it would be helpful to have a function that creates a
#two-dimensional list of any given dimension.

#Exercise 10.2: Write a function called create_row that takes
#an integer, n, as input and returns a list of n space characters.

#Hint: Write a function that will create a single row of the grid with n columns,
#each initialized with a space character (' '), which represents a dead cell in the
#context of Conway's Game of Life. Use a list comprehension to create a
#list containing n space characters. When you call create_row(n),
#it will return a list with n spaces. For example, create_row(5)
#will return [' ', ' ', ' ', ' ', ' ']. This is a basic building block for
#creating larger two-dimensional grids.

#Answer:

#10.2.1: In order to use the create_row function with a specific value of n,
#you need to call the function and pass the desired value of n as its argument. 
#Create a row with 10 space characters. Write the function call as create_row(10).
#The resulting output should look like this: 
#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
 
#Answer:
		 	 						
#Exercise 10.3: Write a function called create_grid that takes two integers,
#rows and cols, as inputs and returns a two-dimensional list of space
#characters with rows and cols as its dimensions (where rows represents
#the number of rows and cols represents the number of columns).
#You should use the create_row function defined in the previous exercise. 
#Hint: To create the create_grid function, you will use the create_row
#function defined earlier. This function will create a two-dimensional
#list (a grid) with the specified number of rows and columns. Each row will
#be created by calling create_row(cols), ensuring that each row has the
#correct number of columns filled with space characters.

#Answer:

#10.3.1: Create a grid with 5 rows and 10 columns, where each cell in the
#grid is initialized to a space character (' '). This grid represents a 5x10
#Game of Life board in its initial state, with all cells "dead."

#Answer:

#As an initial state for your Game of Life grid, however, a grid full of
#dead cells would be rather boring.
#Nothing will ever happen in this world. What we would want is a grid
#of cells that had a reasonable distribution of live and dead cells.
#One way of creating such a grid would be to manually code in the values.
#With a 5×5 grid, manually coding in the values of every cell is manageable (barely).
#But what if we wanted to work with a 50×50 grid? This will require up to 2,500
#manually coded cells! One alternative, if we are not interested in a particular
#starting state, would be to randomly populate the cells in a grid with live and dead cells.

#See pgs. 129-30 for a discussion of the random library and the function random.random().

#Exercise 10.4: Write a function called flip that has no input or output values.
#When it is executed, it will print 'heads' or 'tails'
#where each string is displayed with 50% probability.

#Answer:

#Hint: To create the “flip” function that randomly prints "heads" or "tails"
#with a 50% probability for each, you can utilize the random module from Python's
#standard library. This module provides a function random() that generates a
#random float number between 0 and 1. You can use this function to decide
#whether to print "heads" or "tails".

#In the function you create, random.random() generates a random number
#between 0 and 1. If this number is less than 0.5, the function prints "heads";
#otherwise, it prints "tails". Since the random() function generates numbers in a
#uniform distribution, each outcome ("heads" or "tails") has approximately a 50% chance
#of occurring each time the flip function is called.

import random

#Answer:


#Exercise 10.5: Write a function called roll that has no input value.
#This function will model what it’s like to roll a six-sided die.
#The percentage of times it will land on any given number
#between 1 and 6 is 16.66%. This function should return a number between 1 and 6.

#Hint: To create a function roll that simulates rolling a six-sided die,
#you can use the randint function from Python's random module.
#This function can generate a random integer between two specified values, inclusive.
#Since a six-sided die has numbers from 1 to 6, you would use randint(1, 6) to simulate a die roll.

#Answer:

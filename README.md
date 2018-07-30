# Terminal Overlord
## A terminal(ly) awesome task manager

## Screenshots
Running iTerm2 with Gruvbox colorscheme

![alt-text](https://github.com/Orbtial/terminal-overlord/blob/master/Screenshots/terminal-overlord%20screenshot(1).png "Task list screen")

![alt-text](https://github.com/Orbtial/terminal-overlord/blob/master/Screenshots/terminal-overlord%20screenshot(2).png "Operator menu screen")

## Features
* Color coded deadlines
	* Red: <= 1 day
	* Yellow: <= 5 days
	* Green: > 5 days
* Customisable flags for organisation
* Ability to add, remove and edit all parts of todos
* Smooth deadline system
	* Just type in "5" to set the deadline in 5 days
	* Just type in "mon" to set it for the next occuring Monday
	* You can type "next" or "following" before a day like "mon" to shift the date accordingly!
	
## Prerequisites
* Mac OSX 10.13 High Sierra (not tested on Windows/Linux as of time of writing)
* Python 3
* [brickscript](https://pypi.org/project/brickscript/) (comes with the download)

## Usage
To start, move to the folder and type (in a terminal) :
```bash
python3 overlord.py
```

To navigate the menu in terminal, key in the option's index then hit [ENTER]

For example, to add a task (TODO)
1. Hit [ENTER] to go past the task list screen
2. Enter [1] and then hit [ENTER] again
3. Key in the flag, task and date.

## FAQs
Q1: Where's the delete task button? How do I delete a task?

Answer: Just use the "Mark as complete" menu option

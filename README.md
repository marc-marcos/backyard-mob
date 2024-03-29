# Backyard Mob 

Introducing a game inspired by John Conway's Game of Life, but with all of its rules changed. In this game, there are two teams at the start of each round. Each cell can be dead or can be alive and belonging to a team. They all follow a set of specific rules:

- If the number of cells belonging to the enemy team is double the number of cells belonging to the own team, a cell will convert to the enemy team.
- If there are more cells belonging to the enemy team than the own team, a cell will die.
- A dead cell will become part of the team that has a higher number of surrounding cells.
Additionally, each cell has a 10% chance of randomly dying.

## Getting Started

### Dependencies

#### Python version
* Python 3
* Ubuntu (or any other Unix system) 
* Pygame

#### C++ version
* C++
* g++
* sfml

It may work without this requirements but it hasn't been tested


### Installing


* Clone the repository
* ``pip install -r requirements.txt`` (Python version)
* ``sudo apt-get install libsfml-dev`` (C++ version)

### Executing program

#### Python version
* ``python3 python_version/index.py``

#### C++ version
* ``cd c++ version``
* ``make``
* ``./sfml-app``


## Help

This script at the moment only runs in Unix, running it in Windows might result in errors.

## Authors
[@marc-marcos](https://github.com/marc-marcos)

## Version History

* 0.1
    * Python version, runs well with relatively low row count but gets very laggy with more than 200 rows.
* 0.2 
    * Improved logic, now it make some sense and it happens what should happen in a real "conflict" or whatever.
    * C++ performance improved a lot (by a factor of 5.5 times versus Python version).

## License

This project is licensed under the GPL License - see the LICENSE.md file for details
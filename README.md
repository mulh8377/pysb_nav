# pysb_nav

## Description

A project management tool aimed at helping beginners set-up consistent python projects quickly and easily.


## Makefile


### Setup commands
1. make build
        Creates the folder layout that is used during the project.
2. make clean
        Clears the folder layout back to its original condition.

### Run Commands

3. make window

4. make cli

5. make web

## GUI

Includes a graphical user-interface that helps beginners plan & design their program before they begin implementation.


## WEB
Includes a useful module for surfing the web to gather helpful resources before beginning the project.

Input: URL | Algorithm | Topic | Question

Output: Downloads content that best matches user-input.

EXPORT:
docs/web/*.txt

Log: 
log/web/activity.txt

#### Design Goals:
    * search github
    * search stackoverflow
    * search google
    * ability to save resources to temp/
    * ability to ask question to stackoverflow from the terminal

### CLI
Intended for batch processing of various directories and other useful command-line operations that are not included in a typical shell environment.

#### Commands
* setup
    *
* create
    *
* remove
    *
* copy
    *
* move
    *
* compare
    *
* edit
    *
* merge
    *
* web
    *
* export
    *

INPUT:
pysb >= <command> [arguments]

All possible Exports will be listed.

OUTPUT:
bin/
config/
data/
docs/
temp/
tests/

LOG:
log/cli/activity.txt


#### Design Goals:
    * Simple Tool for beginners to use
    * Easy viewing of data and documents
    * Able to compare two resources from the web.
    * Able to have similar outcomes to the GUI
    * Should extend typical shell environment, but keeps commands that enable moving, copying, or editing files.

# NAV

Intuitive and fast way to browse files and folders in bash shell. Implemented with python curses.

![gif](doc/nav2.gif)

#### Features
- Use arrow keys and enter to browse files.
- Modern and easy-to-use search functionality for folders: just start typing the name of the folder and folders are filtered by their name.

## Usage
1. Clone the repository
2. Add following lines to .bashrc:
```bash
export NAV_HOME='PATH_TO_CLONED_REPOSITORY'
alias nav='source $NAV_HOME/bin/nav.sh'
```
Remember to replace `PATH_TO_CLONED_REPOSITORY` with absolute path to the cloned repository.

3. Refresh .bashrc file with restarting terminal or executing `source .bashrc`.
4. Type nav and start browsing files and folders.
5. Press f1 to quit nav.

## Contribution

Although there are no formal quidelines for contribution yet, it is warmly welcomed! If you are interested in contributing to the project, please make a new issue before writing any code where you describe at least the following:

- What kind of change are you planning to do?
- Why is it needed and how does it improve the project?
- Describe the actual code and file level changes: what classes need to be edited and how?
- If any exisiting behaviour of the program needs to be changed, please describe it as accurately as possibly.

The smaller the scope of the change is the more likely the issue will be accepted.

If the issue is accepted, you can proceed with making the change and creating a pull request.

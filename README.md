

# NAV

This project exists because I felt that typing multiple `cd`, `dir`/`ls` commands and striking the tab-key is not very fast or pleasant way to navigate in shell. As developers often need to work in multiple environments, nav supports bash shell, Windows Command Prompt and PowerShell. The core component of the project is implemented with python and uses curses module. Windows version uses [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) module. 

![gif](doc/nav2.gif)

#### Features
- Use arrow keys and enter to browse files.
- Modern and easy-to-use search functionality for folders: just start typing the name of the folder and folders are filtered by their name.
- Supports bash shell, Windows Command Prompt and PowerShell

## Usage - Bash
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

## Usage - Windows Command Prompt

1. Clone the repository.
2. Install [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) with `pip install windows-curses`.
3. Add absolute path to `\bin` folder in cloned project to PATH-environment variable.
4. Add new environment variable `NAV_HOME` that contains absolute path to the root of the cloned project.
5. Type nav and start browsing files and folders.
6. Press f1 to quit nav.

## Contribution

Although there are no formal quidelines for contribution yet, it is warmly welcomed! Please use issues to discuss about changes/features you would like to make before implementing them.

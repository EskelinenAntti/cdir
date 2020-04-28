

# CDIR

This project exists because I felt that typing multiple `cd`, `dir`/`ls` commands and striking the tab-key is not very fast or pleasant way to navigate in shell. As developers often need to work in multiple environments, cdir supports bash shell, Windows Command Prompt and PowerShell. The core component of the project is implemented with python and uses curses module. Windows version uses [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) module.

![gif](doc/nav2.gif)

#### Features
- Use arrow keys and enter to browse files.
- Modern and easy-to-use search functionality for folders: just start typing the name of the folder and folders are filtered by their name.
- Supports bash shell, Windows Command Prompt and PowerShell

## Usage - Bash
1. Install with `pip install cdir`
2. Add following line to .bashrc:
```bash
alias cdir='source nav.sh'
```
3. Type nav and start browsing files and folders.
4. Press f1 to quit nav.

## Usage - Windows Command Prompt

1. Install with `pip install cdir`
2. Type nav and start browsing files and folders.
3. Press f1 to quit nav.

## Contribution

Although there are no formal quidelines for contribution yet, it is warmly welcomed! Please use issues to discuss about changes/features you would like to make before implementing them.

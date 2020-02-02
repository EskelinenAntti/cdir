

# NAV

This project exists because I felt that typing multiple `cd`, `dir`/`ls` commands and striking the tab-key is not very fast or pleasant way to navigate in shell. As developers often need to work in multiple environments, nav supports bash shell, Windows Command Prompt and PowerShell. The core component of the project is implemented with python and uses curses module. Windows version uses [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) module.

![gif](doc/nav2.gif)

#### Features
- Use arrow keys and enter to browse files.
- Modern and easy-to-use search functionality for folders: just start typing the name of the folder and folders are filtered by their name.
- Supports bash shell, Windows Command Prompt and PowerShell

## Usage - Bash
1. Clone the repository
2. In the root folder of the cloned repository run `pip install .` to install nav.
3. Add bin folder to path variable, i.e. add following line to ~/.profile (or ~/.bash_profile):
```bash
PATH=[PATH_TO_CLONED_REPOSITORY]/linux/bin:$PATH
```
4. Type nav and start browsing files and folders.
5. Press f1 to quit nav.

## Usage - Windows Command Prompt

1. Clone the repository.
2. In the root folder of the cloned repository run `pip install .` to install nav.
3. Install [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) with `pip install windows-curses`.
4. Add absolute path to `bin\windows\` folder in cloned repository to PATH-environment variable.
5. Type nav and start browsing files and folders.
6. Press f1 to quit nav.

## Contribution

Although there are no formal quidelines for contribution yet, it is warmly welcomed! Please use issues to discuss about changes/features you would like to make before implementing them.

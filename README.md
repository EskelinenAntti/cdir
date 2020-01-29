# NAV

Intuitive and fast way to browse files and folders. Supports bash shell, Windows Command Prompt and PowerShell. Implemented with python curses. Windows version uses [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) module.

![gif](doc/nav2.gif)

#### Features
- Use arrow keys and enter to browse files.
- Modern and easy-to-use search functionality for folders: just start typing the name of the folder and folders are filtered by their name.
- Supports both bash shell and Windows Command Prompt

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

Although there are no formal quidelines for contribution yet, it is warmly welcomed! If you are interested in contributing to the project, please make a new issue before writing any code where you describe at least the following:

- What kind of change are you planning to do?
- Why is it needed and how does it improve the project?
- Describe the actual code and file level changes: what classes need to be edited and how?
- If any exisiting behaviour of the program needs to be changed, please describe it as accurately as possibly.

The smaller the scope of a single issue is the more likely the issue will be accepted. It is better to make multiple small issues than one big issue.

If the issue is accepted, you can proceed with making the change and creating a pull request.

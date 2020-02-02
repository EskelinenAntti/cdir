# NAV

Intuitive and fast way to browse files and folders. Supports bash shell and Windows Command Prompt. Implemented with python curses. Windows version uses [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) module.

![gif](doc/nav2.gif)

#### Features
- Use arrow keys and enter to browse files.
- Modern and easy-to-use search functionality for folders: just start typing the name of the folder and folders are filtered by their name.
- Supports both bash shell and Windows Command Prompt

## Usage - Bash
1. Clone the repository
2. In the root folder of the cloned repository run `pip install .` to install nav.
3. Add following line to .bashrc:
```bash
alias nav='source $NAV_HOME/bin/nav.sh'
```
4. Refresh .bashrc file with restarting terminal or executing `source .bashrc`.
5. Type nav and start browsing files and folders.
6. Press f1 to quit nav.

## Usage - Windows Command Prompt

1. Clone the repository.
2. In the root folder of the cloned repository run `pip install .` to install nav.
3. Install [windows-curses](https://github.com/zephyrproject-rtos/windows-curses) with `pip install windows-curses`.
4. Add absolute path to `\bin` folder in cloned project to PATH-environment variable.
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

# Welcome to DS-2002 Windows User Setup Guide!

If you are a Windows User, you are in the right place! If you are a MacOS user, please click [here](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/macOS_Users.md) to follow the MacOS User Setup Guide.

In this Setup Guide, you will find easy to navigate instructions for downloading and installing the tools you will need this semester:
- Environments ⛰️
- Languages 🗣️
- Packages 📦
- Tools 🛠️
- Etc. 🤷‍♀️

<br>

# Early Semester Must Haves

### Git Bash 💻
Git Bash is a command-line interface (CLI) for Windows that emulates a Unix-like shell environment. It provides essential Unix commands like `ls`, `cd`, `grep`, and a robust environment for using Git. Git Bash is important because it allows Windows users to work with the same commands and workflows as developers on macOS and Linux, which is crucial for consistency in software development and data science.

Please follow these steps and read each step carefully:
1. Download the Git Bash setup from the official website: https://git-scm.com/
2. Download the installer by clicking on "**Download for Windows**" for the **Latest Source Release**
3. Run the .exe file you just downloaded and follow the instructions in the installer.​
4. Open Git Bash by doing one of the following:
  - Open the Start menu, type "Git Bash", and the either click it to open it normally or right click and select "Run as administrator" if you need administrator privileges.
  - Open by right-clicking on any directory (folder in your file system) and selecting the **Git Bash Here** option from the context menu (i.e. right-click menu).

<br>

### Chocolatey 🍫
**Chocolatey** is a package manager for Windows. Think of it as an "app store" for the command line. It's important because it automates the process of installing, updating, and removing software from the command line. Instead of manually downloading an installer, you can use a single command like `choco install make` to automatically download and set up a program. This saves time and ensures your tools are consistently managed.

Please follow these steps and read each step carefully:
1. Open the Start menu, type "PowerShell," and right-click on it to select "Run as administrator."
2. Copy and paste the Chocolatey installation command:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
3. Press Enter. This command will download and install the Chocolatey package manager. Once it finishes, you can close the PowerShell window.
4. Open Powershell back up and run:
```
choco
```
  - If everything has installed properly, you should see an output like this: `Chocolatey v2.5.1`

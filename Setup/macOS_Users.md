# Welcome to DS-2002 macOS User Setup Guide!

If you are a macOs User, you are in the right place! If you are a Windows user, please click [here](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/Windows_Users.md) to follow the Windows User Setup Guide.

In this Setup Guide, you will find easy to navigate instructions for downloading and installing the tools you will need this semester:
- Environments ⛰️
- Languages 🗣️
- Packages 📦
- Tools 🛠️
- Etc. 🤷‍♀️

<br>

# Early Semester Must Haves

### Terminal 💻
The **Terminal** (or `Terminal.app` on macOS) is the default command-line interface (CLI) for macOS. It provides a Unix-like environment that allows users to interact directly with the operating system using commands. The Terminal is important because it's the standard tool for developers, system administrators, and data scientists to manage files, run scripts, and automate tasks. Since macOS is built on a Unix foundation, the Terminal is a native and powerful tool that doesn't require any special emulation.

Please follow these steps and read each step carefully:
1. You're done! It comes with your Mac by default!

<br>

### Homebrew 🍺
**Homebrew** is a package manager for macOS. It simplifies the process of installing software that isn't included with macOS by default, such as `jq`, `make`, and other command-line tools. Homebrew is important because it provides a centralized and reliable way to install and manage these applications without needing to download them manually or deal with complex installation processes. It's often referred to as "the missing package manager for macOS."

Please follow these steps and read each step carefully:
1. Open the **Terminal** application.
2. Copy and paste the following command and press Enter:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. The script will prompt you to confirm the installation and may ask for your administrator password. Follow the on-screen instructions.

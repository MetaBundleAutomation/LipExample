# 🤖 Path of Misfortune

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Getting Started](#getting-started)

<br>

## ⚡ Introduction
"Path of Misfortune" is a whimsically application designed for Path of Exile players who seek a refreshing twist in their gaming routine. It generates random builds by spinning a series of "wheels of misfortune," selecting an ascendancy and a set of skill gems for you and your friends to challenge yourselves with. Perfect for those adventurous souls who think they've seen it all in Wraeclast and groups looking to add a hefty dose of meme-building fun to their BroSSF league launches.

<br>

## 💻 Requirements

Before starting, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Taskfiles](https://taskfile.dev/installation/)
- [Python (3.10+)](https://www.python.org/downloads/)

<br>

## 🚀 Getting Started
To get started with "Path of Misfortune," clone the repository to your local machine and navigate into the project directory:

### Cloning the Repository
To get started with "Path of Misfortune," clone the repository to your local machine and navigate into the project directory:
```zsh
git clone https://github.com/MetaBundleAutomation/LipExample.git
cd path-of-misfortune
```

### Setting up the Environment
Install the project dependencies. This will create a virtual environment and install everything needed:

```bash
# Intialise a virtual env.
$ python -m venv .venv

# Activate a virtual env.
$ .venv\Scripts\activate

# Resolves the dependencies, and installs them
$ pip install -r requirements.txt
```

#### Updating module dependencies
```bash
# Freeze a new set of requirements if you've added a library
$ pip freeze > requirements.txt
```

### Running the Application
To launch the "Path of Misfortune" app, use Task to start the Streamlit server. This custom command simplifies the process and ensures consistency across environments:

```zsh
task streamlit:start 
# Alternatively: streamlit run app/main.py
```

### Running Code Quality Checks
Run the following command to perform all code quality checks:

```zsh
task code_quality:all
# Alternatively: ruff --check
```

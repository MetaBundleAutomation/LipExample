# 🤖 LipNet

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Getting Started](#getting-started)

<br>

## ⚡ Introduction
...

<br>

## 💻 Requirements

Before starting, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Taskfiles](https://taskfile.dev/installation/)
- [Python (3.10+)](https://www.python.org/downloads/)

<br>


## 🚀 Getting Started
Follow these instructions to get your Streamlit application up and running on your local machine for development and testing purposes.

### Cloning the Repository
First, clone the repository to your local machine and navigate into the project directory:
```zsh
git clone https://github.com/MetaBundleAutomation/LipExample.git
cd LipExample
```

### Setting up the Environment
Next, set up your Python environment and install the project dependencies in a virtual environment. 
```bash
# Intialise a virtual env.
$ python -m venv .venv

# Activate a virtual env.
$ .venv\Scripts\activate

# Resolves the dependencies, and installs them
$ pip install -r requirements.txt
```

### Running the Application
To launch the Streamlit app locally, you have two options. You can either use a Task command (if Task runner is configured) or directly through Poetry within your virtual environment. Use one of the following commands based on your setup:
```zsh
# Using Task
task streamlit:start 
```
```zsh
# Alternatively, use the venv directly
streamlit run app/app.py
```

### Running Code Quality Checks
To ensure your code adheres to quality standards, run the following command. This will execute a series of code quality checks including linting and static type checking:
```zsh
# Using Task to run all checks
task code_quality:all
```
```zsh
# Alternatively, running individual checks using the venv
ruff --check
isort . 
black .
mypy .
```

#### Updating module dependencies
Freeze a new set of requirements if you've added a library
```bash
$ pip freeze > requirements.txt
```

### Building and Running with Docker
For containerization and easy deployment, you can build and run your Streamlit application using Docker. The following command builds the Docker image and runs it as a container:
```zsh
# This will make your Streamlit app accessible at http://localhost:8000 on your machine.
docker build -f Dockerfile -t streamlit . && docker run -d -p 8000:8080 --name streamlit streamlit
```

### Using Docker Compose
Alternatively, you can use Docker Compose to build and run your application. This is especially useful for more complex applications that might depend on other services like databases:
```zsh
# This will make your Streamlit app accessible at http://localhost:8000 on your machine.
docker-compose up -d --build
```

# Project Manager

Description's project: **Implementation of a simple project manager.**

## Features

- Team management
- Tasks ( using checklists )
- Time management
- Reports

## Requirements

- Python 3.6
- [Pipenv](https://docs.pipenv.org/)

## Building the development environment


```bash
# Install dependence's and environment's library
sudo pip install pipenv
```

```bash
# Clone the repository 
git clone https://github.com/Marlysson/Project-Manager.git

# Enter the project
cd Project-Manager

# Install dependences
pipenv install

# Create and load environment variables
python contrib/env_gen.py

# Activate environment's project
pipenv shell

# Run migrations
python manage.py migrate
```

## How synchonize your fork

Read [how_to](how_to.md)

## Inicial class diagram's project

![Projeto de classes](https://github.com/Marlysson/Project-Manager/blob/master/Documenta%C3%A7%C3%A3o/Diagrama.png)
---

# AirBnB Clone

This project is a simplified clone of the AirBnB website, built as part of the Holberton School curriculum. The goal is to deploy a basic version of the platform on your own server, complete with a working backend, front-end interface, and a command-line interpreter.

## Project Overview

The AirBnB Clone is designed to help understand and build the full stack of a web application — from command-line data management to dynamic web pages and API interaction.

## Features

* **Command Interpreter**: A custom shell for creating, updating, and managing application data. Ideal for development and debugging.
* **Website (Front-end)**: A user-friendly interface displaying both static and dynamic content.
* **Storage**: A system for persisting data — using either a database or file-based storage.
* **RESTful API**: An interface for communication between the front-end and data layer, supporting CRUD operations (Create, Read, Update, Delete).

---

## Command Interpreter

### Description

The command interpreter is a text-based interface for managing the data model. It supports a range of commands to create, retrieve, update, and delete objects in the system.

### Starting the Interpreter

To launch the console, run:

```bash
$ ./console.py
```

This will start an interactive shell where you can type commands directly.

### Usage

Once in the console, you can use the following syntax:

```bash
create <class name>
show <class name> <id>
destroy <class name> <id>
all [<class name>]
update <class name> <id> <attribute name> "<attribute value>"
```

### Examples

```bash
(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) all
(hbnb) destroy User 1234-1234-1234
(hbnb) update User 1234-1234-1234 email "user@example.com"
```

---

## Project Structure

```
.
├── console.py         # Command-line interpreter
├── models/            # Data models (User, Place, State, etc.)
├── web_static/        # Static HTML, CSS, JS
├── web_dynamic/       # Dynamic web content using Flask
├── api/               # RESTful API
├── tests/             # Unit tests
└── README.md          # Project documentation
```

---

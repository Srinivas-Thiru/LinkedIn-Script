# LinkedIn Automation

A Python script using Selenium to automate LinkedIn connection requests and messages.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)

## Features

- Automates LinkedIn login.
- Searches for people based on a given query.
- Sends connection requests and custom messages to search results.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Chrome WebDriver
- Chrome Browser
- [Selenium](https://selenium-python.readthedocs.io/) Python library
- [dotenv](https://pypi.org/project/python-dotenv/) Python library

## Getting Started

You can install Python dependencies using `pip`:

    pip install selenium
    pip install dotenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Srinivas-Thiru/LinkedIn-Script.git
   cd linkedin-automation-bot

3. Set up your environment variables in a .env file:

    ```bash
    USER_NAME=your_username
    PASSWORD=your_password
    SEARCH_QUERY=your_search_query
    MESSAGE=your_custom_message
    NUMBER_OF_REQUESTS=5

4. Run the LinkedIn automation bot:

    ```bash
    python3 run_script.py

5. Sit back and relax while the script automates connection requests and messages on LinkedIn!

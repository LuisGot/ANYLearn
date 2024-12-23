# Description

This Python script utilizes the [Groq AI](https://groq.com) API to divide a topic into subtopics and generates complete courses for each subtopic.

![](/res/Images/ANYLearn-banner.png)

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)

## Features

- Interactive topic input and selection process.
- Dynamic generation of subtopics based on user's interest and knowledge.
- Generation of detailed courses with exercises for chosen subtopics.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [requests library](https://pypi.org/project/requests/)
- [python-dotenv library](https://pypi.org/project/python-dotenv/)
- [An API key from Groq](https://console.groq.com/keys)

## Installation

##### 1. Clone the repository

```bash
git clone https://github.com/LuisGot/ANYLearn.git
```

##### 2. Install required Python packages

```bash
pip install -r requirements.txt
```

##### 3. Setup environment variables

3.1 Rename .env.example file into .env.

```bash
mv .env.example .env
```

3.2 Generate an API key of a openai compatible llm provider and insert them in `.env` File.

3.3 Set the provider url in `.env` file.

##### 4. Run the script

```bash
python main.py
```

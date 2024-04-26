# Description

This Python script utilizes the [Groq AI](https://groq.com) API to divide a topic into subtopics and generates complete courses for each subtopic. The program then leverages a Discord webhook to send the generated courses to a Discord server, making it easy to share and collaborate on educational content.

![](/res/Images/ANYLearn-banner.png)

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)

## Features

-   Interactive topic input and selection process.
-   Dynamic generation of subtopics based on user's interest and knowledge.
-   Generation of detailed courses with exercises for chosen subtopics.
-   Sending course information directly to Discord server via Webhook.

## Prerequisites

-   [Python 3.x](https://www.python.org/downloads/)
-   [requests library](https://pypi.org/project/requests/)
-   [python-dotenv library](https://pypi.org/project/python-dotenv/)
-   [An API key from Groq](https://console.groq.com/keys)
-   [A Discord webhook URL](https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks)

## Installation

##### 1. Clone the repository

```
git clone https://github.com/LuisGot/ANYLearn.git
```

##### 2. Install required Python packages

```
pip install -r requirements.txt
```

##### 3. Setup environment variables

3.1 Rename .env.example file into .env.

```
mv .env.example .env
```

3.2 [Generate a Groq API Key](https://console.groq.com/keys) and [Create a Discord Webhook](https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks) and insert them in `.env` File

##### 4. Run the script

```
python main.py
```

# YouTube Link Checker Bot

This is a Python bot created in 2022 and designed to search for a specified number of BASE64 encoded YouTube links and check if they exist. The project was created out of curiosity to see how many videos can be published on the YouTube platform and to find out how many videos you can discover when trying a certain number of URLs.

## About

The bot generates YouTube video links by encoding random strings in BASE64 format and then decodes them to form valid YouTube URLs. It then checks if these URLs correspond to existing videos on the YouTube platform.

## Features

- **Generate BASE64 Encoded YouTube Links**: Creates a specified number of BASE64 encoded YouTube video links.
- **Check Video Existence**: Verifies if the generated YouTube links correspond to existing videos.
- **Report Results**: Provides a summary of how many of the generated links point to existing videos.

## Technologies Used

- Python
- `requests` library for HTTP requests
- `base64` library for encoding and decoding

## Setup

This project does not include a venv. You have to make sure to install the imported packages on your own
To set up and run the project locally, follow these steps:

1. Clone the project:
   ```bash
   git clone https://github.com/patrickeidencodes/Youtube-Videos-Checker-Python-Bot.git
   ```
2. Run the bot:
   ```bash
   python base.py
   ```
   

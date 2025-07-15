# reddit-user-persona-generator
A Python-based project that uses Natural Language Processing (NLP) and machine learning to generate a persona for a given Reddit user based on their comments and submissions.
## Table of Contents
* [Project Overview](#project-overview)
* [Setup](#setup)
* [Usage](#usage)
* [Output](#output)
* [Requirements](#requirements)
* [Contributing](#contributing)
* [License](#license)

## Project Overview
This project uses Natural Language Processing (NLP) and machine learning to generate a persona for a given Reddit user based on their comments and submissions.

## Setup
1. Clone the repository: `git clone https://github.com/your-username/reddit-user-persona-generator.git`
2. Install the required dependencies: `pip install praw transformers torch`
3. Create a Reddit app and obtain the client ID and client secret.
4. Update the `reddit_scraper.py` script with your client ID and client secret.

## Usage
1. Run the script: `python reddit_scraper.py`
2. Enter the Reddit user profile URL when prompted.
3. The generated persona will be saved to a `.txt` file.

## Output
The generated persona will be saved to a `.txt` file with the following format:

* Interests: [list of interests]
* Personality traits: [list of personality traits]
* Values: [list of values]

## Requirements
* Python 3.x
* PRAW API
* Transformers library
* Torch library

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

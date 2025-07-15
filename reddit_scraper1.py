import praw
from transformers import pipeline
import torch

# Reddit API credentials
reddit = praw.Reddit(client_id='OGWPyWACgeYxNdSa8bP-Lw',
                     client_secret='Iympmw-uvS-doen6E3774y4x3xps7Q',
                     user_agent='ScraperBot:v1.0 (by /u/GovernmentFederal825)')

def scrape_reddit_data(url):
    username = url.split('/')[-2]
    user = reddit.redditor(username)

    comments = []
    submissions = []

    for _ in range(10):  # Limit to 10 comments and submissions
        try:
            comment = next(user.comments.new(limit=None))
            comments.append(comment.body)
        except StopIteration:
            break

    for _ in range(10):  # Limit to 10 comments and submissions
        try:
            submission = next(user.submissions.new(limit=None))
            submissions.append(submission.selftext)
        except StopIteration:
            break

    return comments, submissions

def build_user_persona(comments, submissions):
    llm = pipeline('text-generation', model="openai-community/gpt2")

    persona = {}

    # Generate interests
    prompt = "Based on the following text, what are the user's interests? "
    text = ' '.join(comments + submissions)[:500]  # Truncate the text to 500 characters
    response = llm(prompt + text, max_new_tokens=100, truncation=True)
    persona['interests'] = response[0]['generated_text']

    # Generate personality traits
    prompt = "Based on the following text, what are the user's personality traits? "
    text = ' '.join(comments + submissions)[:500]  # Truncate the text to 500 characters
    response = llm(prompt + text, max_new_tokens=100, truncation=True)
    persona['personality_traits'] = response[0]['generated_text']

    # Generate values
    prompt = "Based on the following text, what are the user's values? "
    text = ' '.join(comments + submissions)[:500]  # Truncate the text to 500 characters
    response = llm(prompt + text, max_new_tokens=100, truncation=True)
    persona['values'] = response[0]['generated_text']

    return persona

def output_user_persona(persona, filename):
    with open(filename, 'w') as f:
        for characteristic, value in persona.items():
            f.write(f"{characteristic.capitalize()}: {value}\n\n")

url = input("Enter Reddit user profile URL: ")
comments, submissions = scrape_reddit_data(url)
persona = build_user_persona(comments, submissions)
output_user_persona(persona, 'user_persona.txt') 

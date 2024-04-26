import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


systemPrompt = """
You are an AI that creates perfect and detailed courses on a specific subtopic.
You always go into great detail, giving examples and exercises that the user can do.
Always make sure that your information is correct.

In your answer, always pay attention to the following structured sequence:
1. Create a short introduction and explain the topic in 1 to 3 sentences
2. Create a full course on the mentioned topic
3. give the user an exercise to put what they have learnt directly into practice

Always pay attention to the following:
- Your information is always correct
- You are only talking about the above-mentioned topic
- Explain the topic to the user as precisely as possible
- Give examples to explain the topic as well as possible
- do not start a conversation just give the course
- Use Markdown format to make the course more readable
- Use Markdown Headings to Format the course into a more readable format (You can do that by writing a '#' and the heading sperated by a space, eg. '# Heading', write multiple #'s for subheadings)
"""


def get_client():
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API key is not set")
    return Groq(api_key=api_key)

def generate_course(maintopic, subtopic):
    prompt = (
        systemPrompt
        + "\Maintopic:"
        + maintopic
        + "\nSubtopic:"
        + subtopic
    )
    client = get_client()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content

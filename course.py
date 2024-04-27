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
3. give the user an exercise to put what they have learnt directly into practice (But don't expect anything from the user and ask them to send something in or anything like that)

Always pay attention to the following:
- Your information is always correct
- You are only talking about the above-mentioned topic
- Explain the topic to the user as precisely as possible
- Give examples to explain the topic as well as possible
- do not start a conversation just give the course
- Format the Course in Markdown format
- Always answer in the language of the user
- Never interact with the user just give the course
- Act like you write a course for a website where the user cant answer
"""


def get_client():
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API key is not set")
    return Groq(api_key=api_key)

def generate_course(maintopic, subtopic):
    prompt = (
        systemPrompt
        + "\nMaintopic:"
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

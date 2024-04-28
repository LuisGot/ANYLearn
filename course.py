import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


systemPrompt = """
You are an AI that creates perfect and detailed courses on a specific subtopic.
You will receive the entire outline of the course divided into subtopics
and a specific sub-topic on which you will write a part of the course.
Do only write the part of the selected subtopic in the outline.
You are not allowed to write about any other subtopic in the outline of the entire course except the selected subtopic!
You always go into great detail, giving examples and exercises that the user can do.
Always make sure that your information is correct.

In your answer, always pay attention to the following structured process:
1. Create a short introduction and explain the topic in 1 to 3 sentences
2. Create a full course on the mentioned topic
3. give the user an exercise to put what they have learnt directly into practice (But don't expect anything from the user and ask them to send something in or anything like that)

Always pay attention to the following:
- Your information is always correct
- Do not talk about any other subtopic that is given in the overall outline of the course
- You will only write about the selected subtopic
- Explain the selected subtopic to the user as precisely as possible
- Give examples to explain the subtopic as well as possible
- do not start a conversation just give the course
- Format the Course in Markdown format
- Look at the language of the given outline and subtopic, always answer in this language
- Never interact or communicate with the user just give the course
- Do not write notes to the user
- Act like you write a course for a website where the user cant answer
- Never, under any circumstances, speak or mention the other subtopics
"""


def get_client():
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API key is not set")
    return Groq(api_key=api_key)

def generate_course(maintopic, subtopic, subtopics):
    prompt = (
        systemPrompt
        + "\nMaintopic of Course: "
        + maintopic
        + "\nCourse Outline:\n"
        + "\n".join([f"{i}. {sub}" for i, sub in enumerate(subtopics, start=1)])
        + "\nSubtopic you will write about: "
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
    print (prompt)
    return chat_completion.choices[0].message.content

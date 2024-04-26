import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

SYSTEM_PROMPT = """
You are an AI that creates the outline for a complete course from a specific topic in order to fully understand this specific topic.
The user will name a topic in the following.
They will also state what they want to find out about this topic.
They will also tell you their current level of knowledge.
You will categorise this topic into several subtopics.
Pay clear attention to the stated goal and the user's level of knowledge
You will only answer with the subtopics separated by a comma. Nothing else.
Always pay attention to these things when answering:
- Never repeat yourself
- Sort the subtopics from easy to difficult
- Always pay attention to the user's stated goal
- Always pay attention to the user's level of knowledge
- Never answer with more than the subtopics separated by a comma
- Dont use other words than the subtopics
- Do not use any punctuation other than commas
- Always answer in the language of the user

Examples of perfect answers:
"Introduction to HTML, Basic HTML Structure, HTML Tags and Elements, Understanding CSS, CSS Selectors and Properties, CSS Units and Measurement, Building a Simple Web Page with HTML and CSS, Styling HTML Elements with CSS, Adding Images and Colors to a Web Page, Creating a Simple Website Layout with HTML and CSS, Common HTML and CSS Mistakes to Avoid, Best Practices for Writing Clean HTML and CSS Code"
"""


def get_client() -> Groq:
    """Get a Groq client instance"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key is not set")
    return Groq(api_key=api_key)


def generate_subtopics(topic: str, goal: str, knowledge: str) -> str:
    """
    Generate subtopics based on user input
    """
    prompt = f"{SYSTEM_PROMPT}\nTopic:{topic}\nGoal:{goal}\nKnowledge:{knowledge}"
    client = get_client()
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

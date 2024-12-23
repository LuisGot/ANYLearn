from subtopics import generate_subtopics
from course import generate_course
import json

def get_user_input() -> tuple:
    """Get user input for topic, goal, and knowledge level"""
    topic = input("What topic do you want to learn about? ")
    goal = input("What do you want to learn about this topic? ")
    knowledge = input("What is your current level of knowledge about this topic? ")
    return topic, goal, knowledge

def display_subtopics(subtopics: list) -> None:
    """Display a list of subtopics with numbering"""
    print("\nSubtopics:")
    for i, subtopic in enumerate(subtopics, start=1):
        print(f"{i}. {subtopic}")

def get_subtopics(message: tuple) -> list:
    """Generate and parse subtopics based on user input"""
    json_response = generate_subtopics(message[0], message[1], message[2])
    try:
        data = json.loads(json_response)
        return data.get("subtopics", [])
    except json.JSONDecodeError:
        print("Error: Received invalid JSON from the LLM.")
        return []

def get_user_subtopic_choice(subtopics: list) -> str:
    """Get user's choice of subtopic"""
    while True:
        try:
            choice = int(input("\nWhich subtopic would you like to learn more about? "))
            if 1 <= choice <= len(subtopics):
                return subtopics[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")

def generate_subtopic_course(maintopic: str, subtopic: str, subtopics: list) -> str:
    """Generate a course for the selected subtopic"""
    return generate_course(maintopic, subtopic, subtopics)

def display_course(course: str) -> None:
    """Pretty display the course content"""
    print("\n" + "="*40)
    print("Course Content:")
    print("="*40)
    print(course)
    print("="*40 + "\n")

def main() -> None:
    """Main function to interact with the user and generate courses"""
    print(welcomeMessage)
    message = get_user_input()
    subtopics = get_subtopics(message)
    if not subtopics:
        print("No subtopics were generated. Exiting.")
        return
    while True:
        display_subtopics(subtopics)
        subtopic = get_user_subtopic_choice(subtopics)
        course = generate_subtopic_course(message[0], subtopic, subtopics)
        display_course(course)
        cont = input("Would you like to learn more about a different subtopic? (y/n): ")
        if cont.lower() != "y":
            break

welcomeMessage = r"""
     _    _   ___   ___                          
    / \  | \ | \ \ / / |    ___  __ _ _ __ _ __  
   / _ \ |  \| |\ V /| |   / _ \/ _` | '__| '_ \ 
  / ___ \| |\  | | | | |__|  __/ (_| | |  | | | |
 /_/   \_\_| \_| |_| |_____\___|\__,_|_|  |_| |_|

"""

if __name__ == "__main__":
    main()

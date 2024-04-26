from subtopics import generate_subtopics
from course import generate_course
from send import send_discord_message

def get_user_input():
    topic = input("Topic: ")
    goal = input("What do you want to learn about this topic? ")
    knowledge = input("What is your current level of knowledge about this topic? ")
    return topic, goal, knowledge


def display_subtopics(subtopics):
    print()
    for i, subtopic in enumerate(subtopics, start=1):
        print(f"{i}. {subtopic}")


def get_subtopics(message):
    subtopics = generate_subtopics(message[0], message[1], message[2])
    subtopics = subtopics.split(",")
    return subtopics


def get_user_subtopic_choice(subtopics):
    choice = int(input("Which subtopic would you like to learn more about? "))
    subtopic = subtopics[choice - 1]
    return subtopic


def generate_subtopic_course(maintopic, subtopic):
    course = generate_course(maintopic, subtopic)
    return course


def main():
    message = get_user_input()
    subtopics = get_subtopics(message)
    while True:
        display_subtopics(subtopics)
        subtopic = get_user_subtopic_choice(subtopics)
        course = generate_subtopic_course(message[0], subtopic)
        print(course)
        send_discord_message(course)
        cont = input("Would you like to learn more about a different subtopic? (y/n): ")
        if cont.lower() != "y":
            break




if __name__ == "__main__":
    main()




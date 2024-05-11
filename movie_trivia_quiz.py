import random

def select_difficulty():
    """Allows the user to choose a difficulty level for the trivia quiz."""
    print("Welcome to the Movie Trivia Quiz!")
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter a number between 1 and 3.")
        choice = input("Enter your choice (1-3): ")
    return int(choice)

def generate_question(difficulty):
    """Generates a random trivia question based on the selected difficulty level."""
    questions = {
        'easy': ["What movie features the line 'Here's looking at you, kid'?",
                 "Who played the lead role in the movie 'Forrest Gump'?",
                 "Which Disney movie features the song 'Let It Go'?"],
        'medium': ["Who directed the movie 'Inception'?",
                   "Which actor played the role of Tony Stark in the Marvel Cinematic Universe?",
                   "Which movie won the Academy Award for Best Picture in 2019?"],
        'hard': ["Which film won the first-ever Academy Award for Best Picture?",
                 "Who composed the soundtrack for the movie 'The Godfather'?",
                 "What was the name of the character played by Al Pacino in the movie 'Scarface'?"]
    }
    return random.choice(questions[difficulty])

def evaluate_answer(user_answer):
    """Evaluates user's answer to the current trivia question."""
    correct_answers = {
        "Casablanca": "What movie features the line 'Here's looking at you, kid'?",
        "Tom Hanks": "Who played the lead role in the movie 'Forrest Gump'?",
        "Frozen": "Which Disney movie features the song 'Let It Go'?",
        "Christopher Nolan": "Who directed the movie 'Inception'?",
        "Robert Downey Jr.": "Which actor played the role of Tony Stark in the Marvel Cinematic Universe?",
        "Parasite": "Which movie won the Academy Award for Best Picture in 2019?",
        "Wings": "Which film won the first-ever Academy Award for Best Picture?",
        "Nino Rota": "Who composed the soundtrack for the movie 'The Godfather'?",
        "Tony Montana": "What was the name of the character played by Al Pacino in the movie 'Scarface'?"
    }
    if user_answer in correct_answers:
        print("Correct! Well done!")
    else:
        print("Incorrect. Better luck next time!")

if __name__ == "__main__":
    difficulty_level = select_difficulty()
    question = generate_question(difficulty_level)
    print("\nTrivia Question:", question)
    user_answer = input("Your answer: ")
    evaluate_answer(user_answer)

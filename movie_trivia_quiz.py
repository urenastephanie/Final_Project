import random

def select_difficulty():
    """Allows the user to choose a difficulty level for the trivia quiz."""
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter a number between 1 and 3.")
        choice = input("Enter your choice (1-3): ")
    if choice == '1':
        return 'easy'
    elif choice == '2':
        return 'medium'
    else:
        return 'hard'

def generate_questions(difficulty):
    """Generates a list of trivia questions based on the selected difficulty level."""
    questions = {
        'easy': ["What movie features the line 'Here's looking at you, kid'?",
                 "Who played the lead role in the movie 'Forrest Gump'?",
                 "Which Disney movie features the song 'Let It Go'?",
                 "What is the name of the clownfish in the movie 'Finding Nemo'?",
                 "In which movie series does the character Harry Potter appear?",
                 "Who is the director of the movie 'Jurassic Park'?",
                 "Which actor portrays Iron Man in the Marvel Cinematic Universe?",
                 "What is the name of the character played by Johnny Depp in the 'Pirates of the Caribbean' movies?",
                 "Who is the main antagonist in the movie 'The Lion King'?",
                 "Which animated movie features the song 'Circle of Life'?"
                 ],
        'medium': ["Who directed the movie 'Inception'?",
                   "Which actor played the role of Tony Stark in the Marvel Cinematic Universe?",
                   "Which movie won the Academy Award for Best Picture in 2019?",
                   "Who is the actress known for her role as Katniss Everdeen in 'The Hunger Games' movies?",
                   "Which movie features the character Jack Dawson and Rose DeWitt Bukater?",
                   "What is the name of the protagonist in 'The Shawshank Redemption'?",
                   "Which actress won an Academy Award for her role in 'La La Land'?",
                   "What is the title of the movie that features a boy who goes on a quest to find a dragon in a fantasy world?",
                   "Who directed the movie 'The Dark Knight'?",
                   "Which movie won the Academy Award for Best Animated Feature in 2020?"
                   ],
        'hard': ["Which film won the first-ever Academy Award for Best Picture?",
                 "Who composed the soundtrack for the movie 'The Godfather'?",
                 "What was the name of the character played by Al Pacino in the movie 'Scarface'?",
                 "Which movie is considered to be the highest-grossing film of all time (not adjusted for inflation)?",
                 "Who won the Academy Award for Best Actor for his role in the movie 'The Revenant'?",
                 "What is the name of the fictional African nation ruled by T'Challa in the movie 'Black Panther'?",
                 "Which movie is based on the true story of the 1970 NASA mission to rescue astronauts stranded in space?",
                 "Who directed the movie 'The Lord of the Rings: The Return of the King'?",
                 "What is the name of the character played by Brad Pitt in the movie 'Fight Club'?",
                 "Which movie won the Academy Award for Best Original Screenplay in 2020?"
                 ]
    }
    return questions[difficulty]

def evaluate_answer(correct_answer, user_answer):
    """Evaluates user's answer to the current trivia question."""
    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    play_again = True
    while play_again:
        difficulty_level = select_difficulty()
        questions = generate_questions(difficulty_level)
        score = 0

        print("\nWelcome to the Movie Trivia Quiz!\n")

        # Dictionary containing correct answers for each question
        correct_answers = {
            "What movie features the line 'Here's looking at you, kid'?": "Casablanca",
            "Who played the lead role in the movie 'Forrest Gump'?": "Tom Hanks",
            "Which Disney movie features the song 'Let It Go'?": "Frozen",
            "What is the name of the clownfish in the movie 'Finding Nemo'?": "Nemo",
            "In which movie series does the character Harry Potter appear?": "Harry Potter",
            "Who is the director of the movie 'Jurassic Park'?": "Steven Spielberg",
            "Which actor portrays Iron Man in the Marvel Cinematic Universe?": "Robert Downey Jr.",
            "What is the name of the character played by Johnny Depp in the 'Pirates of the Caribbean' movies?": "Jack Sparrow",
            "Who is the main antagonist in the movie 'The Lion King'?": "Scar",
            "Which animated movie features the song 'Circle of Life'?": "The Lion King",
            "Who directed the movie 'Inception'?": "Christopher Nolan",
            "Which actor played the role of Tony Stark in the Marvel Cinematic Universe?": "Robert Downey Jr.",
            "Which movie won the Academy Award for Best Picture in 2019?": "Green Book",
            "Who is the actress known for her role as Katniss Everdeen in 'The Hunger Games' movies?": "Jennifer Lawrence",
            "Which movie features the character Jack Dawson and Rose DeWitt Bukater?": "Titanic",
            "What is the name of the protagonist in 'The Shawshank Redemption'?": "Andy Dufresne",
            "Which actress won an Academy Award for her role in 'La La Land'?": "Emma Stone",
            "What is the title of the movie that features a boy who goes on a quest to find a dragon in a fantasy world?": "How to Train Your Dragon",
            "Who directed the movie 'The Dark Knight'?": "Christopher Nolan",
            "Which movie won the Academy Award for Best Animated Feature in 2020?": "Toy Story 4",
            "Which film won the first-ever Academy Award for Best Picture?": "Wings",
            "Who composed the soundtrack for the movie 'The Godfather'?": "Nino Rota",
            "What was the name of the character played by Al Pacino in the movie 'Scarface'?": "Tony Montana",
            "Which movie is considered to be the highest-grossing film of all time (not adjusted for inflation)?": "Avatar",
            "Who won the Academy Award for Best Actor for his role in the movie 'The Revenant'?": "Leonardo DiCaprio",
            "What is the name of the fictional African nation ruled by T'Challa in the movie 'Black Panther'?": "Wakanda",
            "Which movie is based on the true story of the 1970 NASA mission to rescue astronauts stranded in space?": "Apollo 13",
            "Who directed the movie 'The Lord of the Rings: The Return of the King'?": "Peter Jackson",
            "What is the name of the character played by Brad Pitt in the movie 'Fight Club'?": "Tyler Durden",
            "Which movie won the Academy Award for Best Original Screenplay in 2020?": "Parasite"
        }

        for question in questions:
            print("\nQuestion:", question)
            user_answer = input("Your answer: ")
            if evaluate_answer(correct_answers[question], user_answer):
                print("Correct! Well done!")
                score += 1
            else:
                print("Incorrect. The correct answer is:", correct_answers[question])

        print("\nQuiz completed!")
        print("Your final score:", score, "/", len(questions))
        
        play_again_input = input("\nDo you want to play again? (yes/no): ")
        if play_again_input.lower() != 'yes':
            play_again = False

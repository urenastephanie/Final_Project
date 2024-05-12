import pytest
import movie_trivia_quiz

def test_select_difficulty():
    assert movie_trivia_quiz.select_difficulty() in ['easy', 'medium', 'hard']

def test_generate_questions():
    assert isinstance(movie_trivia_quiz.generate_questions('easy'), list)
    assert isinstance(movie_trivia_quiz.generate_questions('medium'), list)
    assert isinstance(movie_trivia_quiz.generate_questions('hard'), list)

def test_evaluate_answer():
    assert movie_trivia_quiz.evaluate_answer("correct_answer", "correct_answer") == True
    assert movie_trivia_quiz.evaluate_answer("correct_answer", "wrong_answer") == False

def test_provide_hint():
    assert isinstance(movie_trivia_quiz.provide_hint(), str)

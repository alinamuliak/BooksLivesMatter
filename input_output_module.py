"""
This module contains functions that print some messages
or asks user to input something.
"""

import time
import sys


def slow(text: str) -> str:
    """
    Function which displays characters one at a time and return an empty string.
    """
    for letters in text:
        print(letters, end="", flush=True)
        time.sleep(0.02)
    print()
    return ''


def send_welcome():
    """
    Print the congratulation in the start.
    """
    slow("Hi! I'm so glad you decided to use me! So, do you want to become a little wiser??")


def message_to_continue():
    """
    Ask user if he want to continue and return his answer.
    """
    message = str(
        input(slow("\nWrite 'yes' if you want to continue, and 'no' to exit: ")))
    return message


def request_to_continue1(message: str):
    """
    If (message) is 'yes', ask user to write a title of film and return that title.
    If (message) is 'no' end running programm.
    Otherwise, print info and return 'dk' (which means 'don't know').
    """
    if message == 'yes':
        film = str(input(slow(
            "Write me the title of the last movie you watched and liked: ")))
        return film
    if message == 'no':
        slow('Okay, then have a nice day! :*')
        sys.exit()
    else:
        slow("I don't understand what you mean. But I'll considef it as a 'yes') ")
        film = str(input(slow(
            "Write me the title of the last movie you watched and liked: ")))
        return film


def request_to_continue2() -> str:
    """
    Ask user to write another title of the movie and return it.
    """
    film = str(
        input(slow("Now give another one for better book recomendations:) ")))
    return film


def no_matching_film1():
    """
    Print message if there is no such film in database.
    """
    slow("Hmmm.. Please, check your input, because i didn't find that film.\
        \nYou know..i know every single film, so there's definitely your mistake there.\
        \nYou will have one more chance.")


def no_matching_film2():
    """
    Print message if there is no such film in database and end running the programm.
    """
    slow("Hmmm.. Please, check your input, because i didn't find that film.\
        \nYou know..i know every single film, so there's definitely your mistake there\
        \nMaybe try to start running me again")
    sys.exit()


def process_film_analysis_step(favourite_genre: str):
    """
    Print message about favourite genre.
    """
    slow(
        f"Wow, seems like you are really into {favourite_genre}!\
            \nSo, I'm sure you need to hear about these ones")


def print_info_about_book(list_of_book_info: list):
    """
    Print information about the book based on the given list.
    """
    if len(list_of_book_info) == 4:
        author, title, details, _ = list_of_book_info
        slow(f'{author} wrote really interesting book called {title}.\n')
        slow(f"This is some information about this book:\n{details}")
    else:
        slow("Somehing went wrong...\nPlease, try again")


def know_rating(list_of_book_info: list):
    """
    Ask if user wants to see rating of some book.
    Print messge with rating based on the given list.
    """
    decision = str(
        input(slow("\nDo you want what is the rating of this book?\nType yes or no: ")))

    if decision == 'yes':
        rating = list_of_book_info[3]
        slow(f"FYI, the rating of this book is {rating} out of 5!")
    elif decision == 'no':
        slow("Okay, let's move on!")
    else:
        slow("Well, not sure i understood, but i'll consider it as a 'no'")


def continue_searching() -> str:
    """
    Ask if user want to stop searching for books.
    If yes, then stop the programm, if no, return 'no'.
    Otherwise, return 'dk' (which means don't know)
    """
    slow('Sounds interestiong! Are you going to read one of \
those or want to continue searching for the better one?')
    user_decision = str(
        input(slow("Write 'yes' to stop searching and 'no' to continue: ")))
    if user_decision.lower() == 'yes':
        slow("I'm glad to hear that! Happy reading! Contact me when you finish reading, \
and i will pick up the next book for you!")
        sys.exit()
    if user_decision.lower() == 'no':
        return 'no'

    slow("I don't understand what you mean. Please try again: ")
    return 'dk'


def edward_recom() -> str:
    """
    Ask user if he wants to see information about some author.
    If the answer is no, end running the programme, otherwise, return 'continue'.
    """
    slow("Hmm, this week's author is Edward Ricardo Braithwaite! \
Maybe you'll like one of his books!")
    decision = str(input(slow("Want to know who is it? Type 'yes' or 'no': ")))
    if decision.lower() == 'no':
        slow("Okay, sorry, maybe try to вибрати щось tomorrow! We'll definitely find somethind!")
        sys.exit()
    if decision.lower() == 'yes':
        slow("\nHere will be several ideas below")
        return 'continue'
    slow("I don't understand what you mean, but i'll tell you anyway:))")
    return 'continue'


def print_edward_books(lst: list):
    """
    Print the information about Edward Ricardo Braithwaite's book based on the given list.
    """
    topic, title, date, genre = lst
    slow(
        f'Book called "{title}" was written in {date}. \
Its topic is {topic} and it is witten in {genre} genre.')


def continue_showing(edward_books_list: list):
    """
    Ask user if he wants to see more book information. If yes, print it based on the given list.
    Otherwise, breaks from the cicle.
    """
    for i in range(1, len(edward_books_list)):
        continue_show = str(
            input(slow("\nWant to see another book from Edward?: ")))
        if continue_show == "yes":
            print_edward_books(edward_books_list[i])
        else:
            break


def print_end():
    """
    Print the ending message.
    """
    slow("I was glad to help you! See you later :*")

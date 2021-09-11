"""
This module runs all the programm.
"""

import sys
import time
from bookslivesmatter import input_output_module as iom
from bookslivesmatter import read_and_analyze_module as ram


def slow(text: str) -> str:
    """
    Function which displays characters one at a time and return an empty string.
    """
    for letters in text:
        print(letters, end="", flush=True)
        time.sleep(0.03)
    print()
    return ''


def main_programm():
    """
    Function that starts and runs the programm.
    """
    iom.send_welcome()
    decision_to_continue = iom.message_to_continue()

    # ASKING TO WRITE THE TITLE OF SOME FILM
    film1 = iom.request_to_continue1(decision_to_continue)
    if film1 == 'dk':
        film1 = []
        iom.no_matching_film1()

    # DEFINES GENRES OF FILM1
    slow("searching . . .\n")
    genres_film1 = ram.user_input_film(film1)
    if genres_film1 == []:
        iom.no_matching_film1()

    # ASKING TO WRITE THE TITLE OF ANOTHER FILM
    film2 = iom.request_to_continue2()
    genres_film2 = ram.user_input_film(film2)
    if genres_film2 == [] and genres_film1 == []:
        iom.no_matching_film2()

    # DEFINES INTERSECTION BETWEEN GENRES OF TWO FILMS FOR FAVOURITE_GENRE
    favourite_genre = ram.most_favourite_genre([genres_film1, genres_film2])
    if not favourite_genre:
        slow("Well, something went wrong, starting over")
        sys.exit()
    iom.process_film_analysis_step(favourite_genre)

    # SEARCHING FOR BOOKS WITH MATCHING GENRE
    list_of_books = ram.search_for_books(favourite_genre)
    iom.print_info_about_book(list_of_books[0])
    iom.know_rating(list_of_books[0])

    # SHOWING MORE BOOKS IF USER ASKS FOR IT
    for i in range(1, len(list_of_books)):
        request_for_more = str(
            input(slow("Do you want to see another one? ('yes' or 'no'): ")))
        if request_for_more == "yes":
            iom.print_info_about_book(list_of_books[i])
            iom.know_rating(list_of_books[i])
        else:
            slow("Then no. Let's continue!")
            break

    # ASKING TO CONTINUE
    searching = iom.continue_searching()
    if searching == 'dk':
        searching = iom.continue_searching()
        if searching == 'dk':
            slow("I don't understand what you mean, but i'll consider it as a 'yes'")
            searching = 'yes'

    if searching == 'no':
        edward = iom.edward_recom()
        if edward == 'continue':
            edward_books = ram.read_data_topics()
            edward_books_list = ram.edward_books(edward_books)
            iom.print_edward_books(edward_books_list[0])
            iom.continue_showing(edward_books_list)
        # ENDING
        iom.print_end()

"""
This module reads data from certain files and do different operations with this data.
"""

import pandas as pd


def read_data_topics() -> object:
    """
    Return DataFrame based on 'topics.csv' file.
    """
    df = pd.read_csv('topics.csv')
    df_only_needed = df[['Topic', 'Name', 'Title',
                         'Date of creation/publication', 'Genre']]
    df_only_needed = df_only_needed.dropna()
    needed_novels = df_only_needed.loc[[2, 39, 45]]
    return needed_novels[['Topic', 'Title', 'Date of creation/publication', 'Genre']]


def read_data_tsv() -> object:
    """
    Return DataFrame based on 'data.tsv' file.
    """
    df = pd.read_table('data.tsv', low_memory=False)
    df_only_needed = df[(df['titleType'] == 'movie') |
                        (df['titleType'] == 'series')]
    df_only_needed = df_only_needed.dropna()
    return df_only_needed[['primaryTitle', 'originalTitle', 'isAdult', 'genres']]


def read_data_book() -> object:
    """
    Return DataFrame based on 'book_data.csv' file.
    """
    df = pd.read_csv('book_data.csv', low_memory=False)
    df_only_needed = df[['book_authors', 'book_title',
                         'genres', 'book_desc', 'book_rating']]
    df_only_needed = df_only_needed.dropna()
    return df_only_needed


def user_input_film(film: str) -> list:
    """
    Return a list of genres of this film or empty list if there is no such film.
    May work a little longer, because of going through a lot of information.
    """
    df = read_data_tsv()
    if film in df['primaryTitle'].values:
        genres = df.loc[df['primaryTitle'].isin([film])].iloc[0, 3]
        if genres != '':
            if ',' in genres:
                return genres.split(',')
            return [genres]
    return []


def most_favourite_genre(list_of_genres: list) -> str:
    """
    Return one element, that is the most frequent in 2 lists of list_of_genres,
    return the first element in first list if there is no intersection or
    if 2 lists in list_of_genres are empty.
    If one of lists is empty, return the first element of the another.
    >>> most_favourite_genre([['Romance', 'Drama'], []])
    'Romance'
    >>> most_favourite_genre([['Romance', 'Fiction'], ['Fiction', 'Family']])
    'Fiction'
    >>> most_favourite_genre([[], ['Fiction', 'Family']])
    'Fiction'
    >>> most_favourite_genre([[], []])
    []
    """
    if len(list_of_genres) == 1:
        return list_of_genres[0][0]

    lst1 = list_of_genres[0]
    lst2 = list_of_genres[1]
    if lst1 == [] and lst2 != []:
        return lst2[0]
    if lst1 != [] and lst2 == []:
        return lst1[0]
    if lst1 == [] and lst2 == []:
        return ''
    intersection = list(set(lst1) & set(lst2))
    if intersection:
        return intersection[0]
    return lst1[0]


def search_for_books(genre: str) -> list:
    """
    Return dataset with congruent books of given genre based on the information
    of 'book_data.csv' file.
    """
    df = read_data_book()
    df_filtered = df.loc[df['genres'] == genre]
    final_df_head = df_filtered.head(3)
    list_return = []

    for row in range(final_df_head.shape[0]):
        lst_inside = []
        for column in range(5):
            if column == 2:
                continue
            lst_inside.append(final_df_head.iat[row, column])
        list_return.append(lst_inside)
    return list_return


def edward_books(df: object) -> list:
    """
    Return list of lists with all the information in the given dataframe.
    """
    list_return = []
    for row in range(3):
        lst_inside = []
        for column in range(4):
            lst_inside.append(df.iat[row, column])
        list_return.append(lst_inside)
    return list_return

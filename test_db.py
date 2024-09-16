import sqlite_lib as sl
# Exercise 1


def test_check_rows_eurovision_winners():
    # Arrange
    sl.connect('hw.db');

    # Act
    result = sl.run_query_select('''
        SELECT count(*)
        FROM eurovision_winners 
    ''');

    # Assert
    assert result == [(68,)];


def test_check_rows_song_details():
    # Arrange
    sl.connect('hw.db');

    # Act
    result = sl.run_query_select('''
        SELECT count(*)
        FROM song_details
    ''');

    # Assert
    assert result == [(68,)];

# Exercise 4


def test_check_exist_song_winner():
    # Arrange
    sl.connect('hw.db');

    # Act
    result = sl.check_song_winner('israel', 2018);

    # Assert
    assert result == 'Toy';


def test_check_not_exist_song_winner():
    # Arrange
    sl.connect('hw.db');

    # Act
    result = sl.check_song_winner('israel', 2019);

    # Assert
    assert result.upper() == 'Wrong'.upper();


# Bonus
def test_check_song_winner_for_all_options():
    # Arrange
    sl.connect('hw.db');

    # Act
    table: list[tuple] = sl.run_query_select('''
                    SELECT country, year, song_name
                    FROM eurovision_winners;
                ''');

    for row in table:
        country, year, expected_song = row;
        result: str = sl.check_song_winner(country.lower(), year);

        # Assert
        assert result == expected_song;

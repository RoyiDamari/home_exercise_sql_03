import sqlite_lib as sl


def main():
    sl.connect('hw.db')
# Exercise 2
    answer: list[tuple] = sl.run_query_select('''
            SELECT *
            FROM eurovision_winners
            ORDER BY year desc LIMIT 10;
        ''');

    sl.print_song_details(answer);

# Exercise 3
    while True:
        # Validate the year input
        try:
            # Accept input from the user
            country: str = input("Enter the country name: ").lower();
            if any(char.isdigit() for char in country):
                raise ValueError("Country name can't be a number");

            year: int = int(input("Enter the year: "));
            break;

        except ValueError as e:
            print(e);

    # Call the function to check the winner
    winner_song: str = sl.check_song_winner(country, year)
    print(winner_song);

    winners_list: list[tuple] = sl.run_query_select('''
                    SELECT year, country, song_name
                    FROM eurovision_winners;
                ''');
    while True:
        # Validate the year input
        try:
            # Accept input from the user
            country: str = input("Enter the country name: ").lower();
            if any(char.isdigit() for char in country):
                raise ValueError("Country name can't be a number");

            year: int = int(input("Enter the year: "));
            break;

        except ValueError as e:
            print(e);

    # Call the function to check the song winner
    winner_song: str = sl.check_song_winner_by_filter(country, year, winners_list);
    print(winner_song);

# Exercise 5
    while True:
        # Validate the year input
        try:
            # Accept input from the user
            country: str = input("Enter the country name: ").lower();
            if any(char.isdigit() for char in country):
                raise ValueError("Country name can't be a number");

            year: int = int(input("Enter the year: "));
            genre: str = input("Enter the genre: ");
            if any(char.isdigit() for char in genre):
                raise ValueError("Genre name can't be a number");

            result: str = sl.check_song_winner_and_update(country, year, genre);
            if result == "enter different genre":
                print(result);
                continue;
            break;

        except ValueError as e:
            print(e);

    print(result);

    sl.close();


if __name__ == "__main__":
    main();
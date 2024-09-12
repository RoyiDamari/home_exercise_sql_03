import sqlite3;

conn: any = None
cursor: any = None


def connect(file_name: str) -> any:
    global conn, cursor
    conn = sqlite3.connect(file_name);
    conn.row_factory = sqlite3.Row;  # allow to use column names
    cursor = conn.cursor();  # Create cursor


def run_query_select(query: str) -> list[tuple]:
    cursor.execute(query);
    columns = cursor.fetchall();
    result = [tuple(row) for row in columns];
    return result;


def print_song_details(data: list[tuple]):
    # Print header
    print(f"{'Year':<6} {'Country':<15} {'Winner':<20} {'Host Country':<15} {'Song Name':<20}");
    print("=" * 80);

    # Print data rows with formatted alignment
    for row in data:
        print(f"{row[0]:<6} {row[1]:<15} {row[2]:<20} {row[3]:<15} {row[4]:<20}");


# Function to check if the song won for a given country and year
def check_song_winner(country: str, year: int) -> str:
    # Prepare the SQL query to find the song by country and year
    query = '''
           SELECT song_name
           FROM eurovision_winners
           WHERE LOWER(country) = ? AND year = ?;
       '''

    cursor.execute(query, (country, year));
    result = cursor.fetchone();

    if result:
        return result['song_name'];
    else:
        return "wrong";


# Function to check if the song won for a given country and year using the filter function
def check_song_winner_by_filter(country: str, year: int, winners_list: list[tuple]) -> str:
    result: list = list(filter(lambda winner: winner[1].lower() == country and winner[0] == year, winners_list));

    if result:
        return result[0][2];
    else:
        return "wrong";


# Function to check if the song won for a given country and year
def check_song_winner_and_update(country: str, year: int, genre: str) -> str:
    result: str = check_song_winner(country, year);
    answer: list[tuple] = run_query_select('''
                        SELECT DISTINCT genre
                        FROM song_details;
                    ''');

    # Extract the genres from the list of tuples
    genres: list[str] = [row[0] for row in answer];

    if result != "wrong":
        if genre in genres:
            return "enter different genre";
        else:
            run_query_update('''
                    UPDATE song_details
                    SET genre = ?
                    WHERE year = ?;
                ''', (genre, year));
            return "done";
    else:
        return "wrong";


def run_query_update(query: str,  params: tuple) -> None:
    cursor.execute(query, params);
    cursor.connection.commit();


def close():
    cursor.close();
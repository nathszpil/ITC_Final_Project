import csv
from spotify_api import *
from download_img import *

def fill_database_csv(artists):
    # Open CSV file in write mode with newline='' to prevent extra newlines
    with open('albums_database.csv', mode='w', newline='', encoding='utf-8') as file:
        # Define CSV writer
        writer = csv.writer(file)
        # Write header row
        writer.writerow(['id', 'name', 'artist_name', 'artist_genres', 'release_date', 'total_tracks'])

        # Iterate over each artist
        for artist_name in artists:
            # Get token and artist information
            token = get_token()
            artist_result = search_for_artist(token, artist_name)

            if artist_result:
                artist_id = artist_result["id"]
                artist_genres = artist_result.get("genres", [])
                # Get albums of the artist
                albums = get_albums_by_artist(token, artist_id)

                # Iterate over each album
                for album in albums:
                    album_id = album['id']
                    album_info = get_album_infos(token, album_id)
                    album_name = album_info['name']
                    release_date = album_info['release_date']
                    total_tracks = album_info['total_tracks']

                    # Write album information to CSV file
                    writer.writerow([album_id, album_name, artist_name, artist_genres, release_date, total_tracks])


# Example usage:
artists = ["Drake", "Ed Sheeran", "Mac Miller", "ACDC", "Kaytranada"]  # List of artists
fill_database_csv(artists)

from lyricsgenius import Genius

TOKEN = 'uuHF__pK3LtHS30aeHBiEG2xh1ciMvDoy_1zezSa2lX92lcEXSoVYXZMQI_HsMqX'

def get_lyrics(search_key):
    """
    Takes a string search_key representing a typical search request for a song [title][artist]
    Takes a string token representing the Genius API token
    Returns the lyrics of the song broken up by line into a list
    """
    genius = Genius(TOKEN)
    songs = genius.search_songs(search_key)
    url = songs['hits'][0]['result']['url']
    lyrics = genius.lyrics(song_url=url)
    return [line for line in lyrics.split('\n') if line.strip()]
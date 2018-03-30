from googleapiclient.discovery import build

"""
Helper function that connects to the YouTube API and returns the video ID for the first search result
"""

DEVELOPER_KEY = 'AIzaSyCJECT3j3AEKxxuNF2nZnn8QMnaTB1d1ec'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(query):
    """
    Returns top search result for the given query
    :param query: String (Artist Name + Track Name)
    :return: String (YouTube Video ID)
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=1
    ).execute()

    video = None

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video = search_result['id']['videoId']
            return video



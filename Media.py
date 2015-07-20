__author__ = 'Pri'

import webbrowser

"This class provides a way to store movies related information"

class Movie():
    def __init__(self, title, storyline, poster_image, video_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = video_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
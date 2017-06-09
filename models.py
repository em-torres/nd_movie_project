import webbrowser


class Video:
    def __init__(self, title, duration, poster_image, trailer_youtube):
        self.title = title
        self.duration = duration
        self.poster_image = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, duration, poster_image, storyline, title, trailer_youtube):
        Video.__init__(self, title, duration, poster_image, trailer_youtube)
        self.storyline = storyline


class TvShow(Video):
    def __init__(self, duration, episode, poster_image, title, season, tv_station, trailer_youtube):
        Video.__init__(self, title, duration, poster_image, trailer_youtube)
        self.episode = episode
        self.season = season
        self.tv_station = tv_station

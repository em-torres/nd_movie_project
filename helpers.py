import re
import requests
import constants as cnt
from config import Config
from models import Movie, TvShow


class TmdbApiConnection:
    def __init__(self):
        self.api_key = Config.TMDB_API_KEY
        self.now_playing_movies = self.get_now_playing_movies()
        self.popular_tvseries = self.get_popular_tv_series()

    def _get_youtube_trailer(self, movie_title):
        youtube_title_request = requests.get(cnt.YOUTUBE_SEARCH_URL.format(movie_title))
        youtube_trailer_id = re.findall('<a href="/watch\?v=?\'?([^"\'>]*)', youtube_title_request.text)[0]
        return youtube_trailer_id

    def _get_video_info(self, video_id, vid_type):
        if vid_type == 'm':
            info = requests.get(cnt.TMDB_MOVIE_API_INFO_URL.format(cnt.TMDB_API_PAGE, video_id, self.api_key)).json()
        else:
            info = requests.get(cnt.TMDB_TV_API_INFO_URL.format(cnt.TMDB_API_PAGE, video_id, self.api_key)).json()
        return info

    def get_now_playing_movies(self):
        movies = []
        now_playing_json = requests.get(cnt.TMDB_MOVIE_API_NP_URL.format(cnt.TMDB_API_PAGE, self.api_key)).json()
        for data in now_playing_json['results'][:9]:
            movie_info = self._get_video_info(data['id'], 'm')
            trailer_id = self._get_youtube_trailer(data['title'])
            movie_image_url = cnt.TMDB_IMAGE_API_URL.format(data['poster_path'])
            new_movie = Movie(movie_info['runtime'], movie_image_url, data['overview'], data['title'], trailer_id)
            movies.append(new_movie)
        return movies

    def get_popular_tv_series(self):
        tvseries = []
        popular_tvseries = requests.get(cnt.TMDB_TV_API_POPULAR_URL.format(cnt.TMDB_API_PAGE, self.api_key)).json()
        for data in popular_tvseries['results'][:9]:
            tvinfo = self._get_video_info(data['id'], 't')
            title = tvinfo['original_name']
            trailer_id = self._get_youtube_trailer(title)
            tvseries_image_url = cnt.TMDB_IMAGE_API_URL.format(data['poster_path'])
            duration = tvinfo['episode_run_time'][0]
            episodes = tvinfo['number_of_episodes']
            seasons = tvinfo['number_of_seasons']
            station = tvinfo['production_companies'][0]['name']
            new_tvseries = TvShow(duration, episodes, tvseries_image_url, title, seasons, station, trailer_id,)
            tvseries.append(new_tvseries)
        return tvseries

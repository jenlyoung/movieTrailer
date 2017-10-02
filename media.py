"""
media.py contains class Video and class Movie(Video). Both classes pull
specific information from the internet about videos/movies, including
opening the movie trailer.
"""
import webbrowser


class Video:

    """
    Parent class applies to movies and videos. Pulls info about the
    movie/video from the web.

    Args:
        :param1 title
        :param2 story_line
        :param3 duration
        :param4 category
        :param5 release_date
    """
    def __init__(self, title, story_line, duration, category, release_date):

        self.title = title
        self.story_line = story_line
        self.duration = duration
        self.category = category
        self.release_date = release_date


class Movie(Video):

    """
    Child class will apply to movies only. Inherits some information
    from Parent class Video--(title, story_line, duration, category,
    release_date).

    Args:
        :param1 title
        :param2 story_line
        :param3 duration
        :param4 category
        :param5 release_date
        :param6 poster_image
        :param7 trailer_youtube
        :param8 rating
    """
    VALID_RATINGS = ["G", "PG," "PG-13," "R"]

    def __init__(self, title, story_line, duration, category,
                 release_date, poster_image, trailer_youtube, rating):
        Video.__init__(self, title, story_line, duration, category,
                       release_date)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating

    def show_trailer(self):

        """
        Opens the youtube trailer from the web for the movie.

        :return: Youtube trailer for the movie
        """
        webbrowser.open(self.trailer_youtube_url)



class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, year: int, genres: list):
        # Initialize a new movie.
        self.title = title
        self.year = year
        self.genres = genres

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_genres(self):
        return self.genres

    def is_genre(self, string: str):
        """Returns true if the string parameter matches one of the movie’s genre."""
        return string in self.genres

    def __str__(self):
        return self.title

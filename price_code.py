from datetime import datetime
from enum import Enum

from movie import Movie


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days, "frp": lambda days: days}
    normal = {"price": lambda days: 1.50 * days, "frp": lambda days: 1}
    children = {"price": lambda days: 1.50 * days, "frp": lambda days: 1}

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]
        return pricing(days)

    def frequent_rental_points(self, days):
        """Return the rental points for a given number of days."""
        points = self.value["frp"]
        return points(days)

    @classmethod
    def for_movie(cls, movie: Movie):
        """Return movie price code."""
        if not isinstance(movie, Movie):
            raise TypeError('movie must be a Movie')

        this_year = int(datetime.now().strftime("%Y"))
        if movie.get_year() == this_year:
            return cls.new_release
        elif movie.is_genre('Children'):
            return cls.children
        else:
            return cls.normal

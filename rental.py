import logging

from movie import Movie
from price_code import PriceCode


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_title(self):
        return self.movie.get_title()

    def get_days_rented(self):
        return self.days_rented

    def get_charge(self):
        price_code = PriceCode.for_movie(self.movie)
        days = self.days_rented
        if price_code == PriceCode.normal:
            # Two days for $2, additional days 1.50 each.
            amount = 2.0
            if days > 2:
                amount += price_code.price(days - 2)
        elif price_code == PriceCode.children:
            # Three days for $1.50, additional days 1.50 each.
            amount = 1.5
            if days > 3:
                amount += price_code.price(days - 3)
        elif price_code == PriceCode.new_release:
            # Straight per day charge
            amount = price_code.price(days)
        else:
            log = logging.getLogger()
            log.error(f"Movie {self.movie()} has unrecognized priceCode {price_code}")
        return amount

    def get_rental_points(self):
        price_code = PriceCode.for_movie(self.movie)
        return price_code.frequent_rental_points(self.days_rented)

    # @classmethod
    # def get_rental(cls, movie: Movie, days_rented: int):
    #     return Rental(movie, days_rented)

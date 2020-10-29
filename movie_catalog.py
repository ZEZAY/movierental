import csv

from movie import Movie

FILENAME = 'movies.csv'


class MovieCatalog:

    def __init__(self):
        self.movies = self.load_data()

    def get_movie(self, title: str):
        for movie in self.movies:
            if movie.get_title() == title:
                return movie
        raise KeyError(f"Movie: {title} not found")

    def load_data(self):
        movies = []
        with open(FILENAME) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_zero = True
            for row in csv_reader:
                if line_zero:
                    line_zero = False
                else:
                    # id,title,year,genres
                    title, year, genres = row[1], int(row[2]), row[3].split('|')
                    movie = Movie(title, year, genres)
                    movies.append(movie)
        return movies

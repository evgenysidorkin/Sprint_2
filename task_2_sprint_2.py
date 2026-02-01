class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)    

class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драмы: {self.movies}'

class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Комедии: {self.movies}'


comedy = Comedy()
print(comedy.add_movie('Больщой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))
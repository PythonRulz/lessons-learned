class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling getter")
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        print("calling setter")
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Enter a valid rating.")


fav_movie = Movie("Titanic", 4.3)
print(fav_movie.rating)

fav_movie.rating = 5.1
print(fav_movie.rating)

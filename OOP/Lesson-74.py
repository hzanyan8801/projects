class Movie:

    def __init__(self, title, rating) -> None:
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("calling the getter...")
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        print("calling the setter...")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating")

favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = -5.6
print(favorite_movie.rating)
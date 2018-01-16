def two_exact_movies(flight_length, movie_lengths):
    movie_lengths_dict = {}

    for movie_length in movie_lengths:
        if (flight_length - movie_length) in movie_lengths_dict:
            return True
        else:
            movie_lengths_dict[movie_length] = True

    return False

flight_length = 20

movie_lengths = [10, 10]

print(two_exact_movies(flight_length, movie_lengths))
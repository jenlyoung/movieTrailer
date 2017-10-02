"""
entertainment_center.py contains the instance variables for
class Movie(Video). The class Movie(Video) will use this information to create
a movie trailer website.
"""

import fresh_tomatoes  # turns the information provided into a web page
import media  # contains class Video and class Movie(Video)

rogue_one = media.Movie("Rogue One",
                        ("The Rebel Alliance makes a risky move to steal the "
                         "plans for the Death Star, setting up the epic saga"
                         " to follow."),
                        "2h 13m",
                        "Action, Adventure, Sci-Fi",
                        "2014",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY",
                        "PG-13")

moulin_rouge = media.Movie("Moulin Rouge!",
                           ("A poet falls for a beautiful courtesan whom a "
                            "jealous duke covets."),
                           "2h 7m",
                           "Drama, Musical, Romance",
                           "2001",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/Moulin_rouge_poster.jpg",
                           "https://www.youtube.com/watch?v=dtEgAx80NC4",
                           "PG-13")

gog = media.Movie("Guardians of the Galaxy, Vol. 1",
                  ("A group of intergalactic criminals are forced to work "
                   "together to stop a fanatical warrior from taking "
                   "control of the universe."),
                  "2h 1m",
                  "Action, Adventure, Sci-Fi",
                  "2014",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                  "https://www.youtube.com/watch?v=2XltzyLcu0g",
                  "R")

lego_movie = media.Movie("The Lego Movie",
                         ("An ordinary Lego construction worker, thought to "
                          "be the prophesied 'Special', is recruited to join a"
                          " quest to stop an evil tyrant from gluing the Lego "
                          "universe into eternal stasis."),
                         "1h 40m",
                         "Animation, Action, Adventure",
                         "2014",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MDk1ODExN15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
                         "PG")

fault_in_our_stars = media.Movie("The Fault in Our Stars",
                                 ("Two teenage cancer patients begin a "
                                  "life-affirming journey to visit a reclusive"
                                  " author in Amsterdam."),
                                 "2h 6m",
                                 "Drama, Romance",
                                 "2014",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NzkxNzc5Ml5BMl5BanBnXkFtZTgwNzQ3OTMxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                 "https://www.youtube.com/watch?v=9ItBvH5J6ss",
                                 "PG-13")

the_night_before = media.Movie("The Night Before",
                               ("On Christmas eve, three lifelong friends "
                                "spend the night in New York City looking "
                                "for the Holy Grail of Christmas parties."),
                               "1h 41m",
                               "Comedy",
                               "2015",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyNDY1ODQwNV5BMl5BanBnXkFtZTgwNzA2MjUwNzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=kOBdxkhJvHQ",
                               "R")

movies = [rogue_one, moulin_rouge, gog, lego_movie, fault_in_our_stars,
          the_night_before]
fresh_tomatoes.open_movies_page(movies)

__author__ = 'Pri'

import json
import Media
import urllib2
import fresh_tomatoes

toy_story = Media.Movie("Toy Story",
                        "A Story of Boy",
                        "http://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Media.Movie("Avatar",
                     "A Marine on alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

shawshank = Media.Movie("The Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency",
                        "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

dark = Media.Movie("The Dark Knight",
                   "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham",
                   "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                   "https://www.youtube.com/watch?v=EXeTwQWrcwY")

fight = Media.Movie("Fight Club",
                    "An insomniac office worker looking for a way to change his life",
                    "http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=KVTNyXtW8rE")

gump = Media.Movie("Forrest Gump",
                   "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love,",
                   "http://ia.media-imdb.com/images/M/MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@._V1_SX214_AL_.jpg",
                   "https://www.youtube.com/watch?v=c_BsFNAraDQ")

movies = [toy_story, avatar, shawshank, dark, fight, gump]
print(Media.Movie.__doc__)

fresh_tomatoes.open_movies_page(movies)




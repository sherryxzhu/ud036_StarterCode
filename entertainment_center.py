import media
import fresh_tomatoes

blue_is_the_warmest_color = media.Movie("Blue Is the Warmest Colour", "https://images-na.ssl-images-amazon.com/images/M/MV5BMmYwZmVkZGItMjMyOS00OTkxLTg0MDEtZTM2Yzk0ZWEyNTQzXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_UY268_CR2,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=Y2OLRrocn3s" )

the_godfather = media.Movie("The Godfather", "http://abovethelaw.com/wp-content/uploads/2017/05/The-Godfather.jpg", "https://www.youtube.com/watch?v=8V2k2YQEQJ4")

moonlight = media.Movie("Moonlight", "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=2gCc6kGpXdw")


movies = [blue_is_the_warmest_color, the_godfather, moonlight]


fresh_tomatoes.open_movies_page(movies)
current_movies = {'Kireedam' : '11:00 AM',
                    'Chenkol' : '02:00 PM',
                    'Pingami' : '05:00 PM'}

print('We are showing following movies..')

for key in current_movies:
    print(key) 
movie = input('what movie you would like to show time for? \n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested show isn't playing")
else:
    print(movie, " is playing at ", showtime)

print(current_movies)


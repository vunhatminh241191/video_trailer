from media import Video
import fresh_tomatoes

list_movies = ['Avatar  http://oyster.ignimgs.com/mediawiki/apis.ign.com/avatar-3d/3/37/Avatar-movie-desktop-wallpaper.jpg  https://www.youtube.com/watch?v=d1_JBMrrYw8', 
	'Titanic  https://vincentloy.files.wordpress.com/2012/04/titanic-movie.jpg  https://www.youtube.com/watch?v=ZQ6klONCq4s',
	'Transformers: Age of Extinction  http://tfwiki.net/mediawiki/images2/7/7b/Transformers-_Age_of_ExtinctionOptimusPrimePoster.jpg  https://www.youtube.com/watch?v=dYDGqmxMZFI']

class Entertainment(object):
 	def __init__ (self, list_movies):
 		self.videos = []
 		for i in xrange(len(list_movies)):
	 		movie_title, posted_image, trailer_link = list_movies[i].split('  ')
	 		video = Video(movie_title, posted_image, trailer_link)
	 		self.videos.append(video)

if __name__ == '__main__':
	entertainment = Entertainment(list_movies)
	fresh_tomatoes.open_movies_page(entertainment.videos)
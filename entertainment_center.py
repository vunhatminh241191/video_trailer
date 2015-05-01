from media import Video
import fresh_tomatoes

list_movies = ['Avatar, http://oyster.ignimgs.com/mediawiki/apis.ign.com/avatar-3d/3/37/Avatar-movie-desktop-wallpaper.jpg, https://www.youtube.com/watch?v=d1_JBMrrYw8', 
	'Titanic, https://vincentloy.files.wordpress.com/2012/04/titanic-movie.jpg, https://www.youtube.com/watch?v=ZQ6klONCq4s',
	'Transformers: Age of Extinction, http://tfwiki.net/mediawiki/images2/7/7b/Transformers-_Age_of_ExtinctionOptimusPrimePoster.jpg, https://www.youtube.com/watch?v=dYDGqmxMZFI',
	'The amazing spider man 2, http://cdn.collider.com/wp-content/uploads/the-amazing-spider-man-2-international-poster-1.jpg, https://www.youtube.com/watch?v=DlM2CWNTQ84',
	'Despicable me 2, http://hillviewchristian.com/wp-content/uploads/2014/06/despicable-me-2-wallpaper.jpg, https://www.youtube.com/watch?v=TlbnGSMJQbQ',
	'Harry Potter and Deathly Hallows, http://3.bp.blogspot.com/_2fdwksuATNA/TMzcpsNK5GI/AAAAAAAAAT0/dxllm3YDvgg/s1600/HP+7+Part+1.png, https://www.youtube.com/watch?v=YzfEH0UPEBo']


''' Class Entertainment is the object to store every single movie that I love 
It contains movie's title, posted image and trailer link of this movie'''
class Entertainment(object):
 	def __init__ (self, list_movies):
 		self.videos = []
 		for i in xrange(len(list_movies)):
	 		movie_title, posted_image, trailer_link = list_movies[i].split(', ')
	 		video = Video(movie_title, posted_image, trailer_link)
	 		self.videos.append(video)

if __name__ == '__main__':
	entertainment = Entertainment(list_movies)
	# Using fresh tomatoes file to open web pages
	fresh_tomatoes.open_movies_page(entertainment.videos)
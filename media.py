''' Video class is the abstract data type of object video.
It contains every information about the video'''

class Video(object):
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	# get and set movie title
	def show_title(self):
		return self.title

	def set_title(self, title):
		self.title = title
		
	# get and set posted image
	def show_poster_image_url(self):
		return self.poster_image_url

	def set_poster_image_url(self, poster_image_url):
		self.poster_image_url = poster_image_url

	# get and set trailer
	def show_trailer(self):
		return self.trailer_youtube_url

	# changing the initial trailer of this film trailer
	def change_link_trailer(self, trailer_youtube_url):
		self.trailer_youtube_url = trailer_youtube_url

	# compare 2 video if this already exists
	def __eq__(self, video):
		if (self.title == video.title) and (self.poster_image_url
			== video.poster_image_url) and (self.trailer_youtube_url == video.trailer_youtube_url):
			return "This movie is duplicated"
		else:
			return

	# print information about this movie 
	def __str__(self):
		return 'This is a %s with url link %s' %(self.title, self.trailer_youtube_url)
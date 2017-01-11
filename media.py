import webbrowser
class Movie():
	"""This program displys a list of favorite movies and its related information"""
	
	def __init__(self, movie_title, movie_story_line, poster_image_url, trailer_youtube_link):
		self.title = movie_title
		self.story_line = movie_story_line
		self.poster_image_url = poster_image_url
		self.trailer_youtube_link = trailer_youtube_link


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_link)

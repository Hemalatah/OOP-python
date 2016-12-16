import media
import fresh_tomatoes

Alaipayuthey = media.Movie("Alaipayuthey", "Love after marrriage", "http://ap1.alchetron.com/cdn/Alaipayuthey-images-b4898282-6933-453a-a687-bec8cf025e4.jpg?op=OPEN", "https://youtu.be/BRFdGc3ku-k")

Harry_potter = media.Movie("Harry potter", "Rescued a young boy from the outrageous neglect of his aunt and uncle", "http://mystic-tom.com/tom_bio_page/sorcerers_stone_pic.jpg", "https://www.youtube.com/watch?v=VyHV0BRtdxo")

Kahaani = media.Movie("Kahaani", "A pregnant woman's efforts to find her missing husband", "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/KahaaniPoster.jpg/220px-KahaaniPoster.jpg", "https://www.youtube.com/watch?v=j1wEeuAosNM")

#Alaipayuthey.show_trailer()

movies = [Alaipayuthey, Harry_potter, Kahaani]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__) displays the documentation of the class
#print(media.Movie.__name__) displays the name of the class
#print(media.Movie.__module__) displays the module in which the class is defined
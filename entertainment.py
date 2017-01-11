import media
import fresh_tomatoes

Alaipayuthey = media.Movie("Alaipayuthey", "Love after marrriage", "images/Alaipayuthey.jpg", "https://youtu.be/BRFdGc3ku-k")

Harry_potter = media.Movie("Harry potter", "Rescued a young boy from the outrageous neglect of his aunt and uncle", "images/Harry_potter.jpg", "https://www.youtube.com/watch?v=VyHV0BRtdxo")

Kahaani = media.Movie("Kahaani", "A pregnant woman's efforts to find her missing husband", "images/Kahaani.jpg", "https://www.youtube.com/watch?v=j1wEeuAosNM")

The_Da_Vinci_Code = media.Movie("The Da Vinci Code", "A murder inside the Louvre and clues in Da Vinci paintings lead to the discovery of a religious mystery protected by a secret society for two thousand years", "images/The_Da_Vinci_Code.jpg", "https://www.youtube.com/watch?v=ZjRPTyazKds")

Forrest_Gump = media.Movie("Forrest Gump", "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him", "images/Forrest_Gump.jpg", "https://www.youtube.com/watch?v=uPIEn0M8su0")

House_of_Cards = media.Movie("House of Cards", "A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.", "images/House_of_Cards.jpg", "https://www.youtube.com/watch?v=ULwUzF1q5w4")

How_I_Met_Your_Mother = media.Movie("How I Met Your Mother", "A father recounts to his children, through a series of flashbacks, the journey he and his four best friends took leading up to him meeting their mother.", "images/How_I_Met_Your_Mother.jpg", "https://www.youtube.com/watch?v=apRiP2h-O5o")

Silicon_Valley = media.Movie("Silicon Valley", "In the high-tech gold rush of modern Silicon Valley, A comedy inspired by Mike Judge's experiences as a Silicon Valley engineer in the late 1980s.", "images/Silicon_Valley.jpg", "https://www.youtube.com/watch?v=69V__a49xtw")

Like_Stars_on_Earth = media.Movie("Like Stars on Earth", "An eight-year-old boy is thought to be lazy trouble-maker, until the new art teacher discover the real problem behind his struggles in school.", "images/Like_Stars_on_Earth.jpg", "https://www.youtube.com/watch?v=XOcX16f1KX4")

#Harry_potter.show_trailer() # show the trailer on the youtube website

movies = [Alaipayuthey, Kahaani, The_Da_Vinci_Code, Forrest_Gump, House_of_Cards, How_I_Met_Your_Mother, Silicon_Valley, Like_Stars_on_Earth, Harry_potter]

fresh_tomatoes.open_movies_page(movies)

#fresh_tomatoes.open_movies_summary_page(movies[1])

print(media.Movie.__doc__) # displays the documentation of the class
print(media.Movie.__name__) # displays the name of the class
print(media.Movie.__module__) # displays the module in which the class is defined

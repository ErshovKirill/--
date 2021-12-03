class HomeLibrary():

    def __init__(self,author, publication,genre):
        self.author = author
        self.publication = publication
        self.genre = genre
        print("Книга выбрана")


my_book = HomeLibrary("Robert Louis ",2018,"Treasure Island")
my_preferences = HomeLibrary("William Golding",2020,"Lord of the Flies")
print(my_book.publication)
print(my_preferences.author)
print(my_preferences.genre)
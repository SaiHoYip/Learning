class Music:
    def __init__(self, name, genre, year ):
        self.name = name
        self.genre = genre
        self.year = int(year)

    def Old(self):
        #if older then 20 years
        if self.year < 2000:
            return True
        else:
            return False

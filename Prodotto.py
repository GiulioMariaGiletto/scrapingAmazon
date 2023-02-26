class Prodotto:
    def __init__(self, titolo, prezzo, url, rating, nReview):
        self.titolo = titolo
        self.prezzo = prezzo
        self.url = url
        self.rating = rating
        self.nReview = nReview

    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self) -> str:
        return super().__str__()










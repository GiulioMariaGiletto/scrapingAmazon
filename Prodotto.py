class Prodotto :

    def __init__(self, titolo, prezzo, url, rating, nReview):
        self.titolo = titolo
        self.prezzo = prezzo
        self.url = url
        self.rating = rating
        self.nReview = nReview
        self.punteggio = (prezzo*10+rating*8+nReview*6)/24

    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self) -> str:
        return self.titolo+' '+self.prezzo+' '+self.url+' '+self.rating+' '+self.nReview

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)
















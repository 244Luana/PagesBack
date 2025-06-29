class Review:

    def __init__(self, id: str, book_id: str, user_id: str, rate: str, review: str):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.rate = rate
        self.review = review

#book_id → conecta a review ao livro certo
#user_id → conecta ao usuário que escreveu
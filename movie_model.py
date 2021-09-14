# movies에 쓸데없는 데이터를 넘기지 않기 위해 생성
class MovieModel:
    def __init__(self, title, rating, small_cover_image, summary):
        self.title = title
        self.rating = rating
        self.small_cover_image = small_cover_image
        self.summary = summary

class Book:
    def __init__(self, title, author_id, published_year):
        self.title = title
        self.author_id = author_id
        self.published_year = published_year

    def to_dict(self):
        return {
            "title": self.title,
            "author_id": self.author_id,
            "published_year": self.published_year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get('title'),
            author_id=data.get('author_id'),
            published_year=data.get('published_year')
        )

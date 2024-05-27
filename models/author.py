class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def to_dict(self):
        return {
            "name": self.name,
            "birth_year": self.birth_year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            birth_year=data.get('birth_year')
        )

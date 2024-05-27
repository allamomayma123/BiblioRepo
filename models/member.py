class Member:
    def __init__(self, name, email, membership_date):
        self.name = name
        self.email = email
        self.membership_date = membership_date

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "membership_date": self.membership_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            email=data.get('email'),
            membership_date=data.get('membership_date')
        )

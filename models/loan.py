class Loan:
    def __init__(self, book_id, member_id, loan_date, return_date=None):
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.return_date = return_date

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "member_id": self.member_id,
            "loan_date": self.loan_date,
            "return_date": self.return_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            book_id=data.get('book_id'),
            member_id=data.get('member_id'),
            loan_date=data.get('loan_date'),
            return_date=data.get('return_date')
        )

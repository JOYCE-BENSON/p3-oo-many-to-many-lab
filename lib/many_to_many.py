class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        """Returns all contracts for this author"""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Returns all books by this author through contracts"""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Creates a new contract between this author and the specified book"""
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Returns the total royalties earned by this author"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        """Returns all contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Returns all authors of this book through contracts"""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        self.author = author
        
        # Validate book
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        self.book = book
        
        # Validate date
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        self.date = date
        
        # Validate royalties
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.royalties = royalties
        
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts with the specified date"""
        return [contract for contract in cls.all if contract.date == date]
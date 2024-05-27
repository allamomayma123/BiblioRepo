from config.mongo_config import get_mongo_client
from config.neo4j_config import get_neo4j_driver
from models.book import Book


def add_book(book: Book):
    client = get_mongo_client()
    db = client.library
    books_collection = db.books
    books_collection.insert_one(book.to_dict())

    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run(
            "CREATE (b:Book {title: $title, author_id: $author_id, published_year: $published_year})",
            title=book.title, author_id=book.author_id, published_year=book.published_year
        )

def get_books():
    client = get_mongo_client()
    db = client.library
    books_collection = db.books
    return [Book.from_dict(book) for book in books_collection.find()]

def get_book_by_id(book_id):
    client = get_mongo_client()
    db = client.library
    books_collection = db.books
    book_data = books_collection.find_one({"_id": book_id})
    return Book.from_dict(book_data) if book_data else None


def update_book(book_id, data):
    client = get_mongo_client()
    db = client.library
    books_collection = db.books
    books_collection.update_one({"_id": book_id}, {"set": data})

def delete_book(book_id):
    client = get_mongo_client()
    db = client.library
    books_collection = db.books
    books_collection.delete_one({"_id": book_id})

# Neo4j Operations
def sync_book_to_neo4j(book: Book):
    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run("""
            MERGE (b:Book {title: $title})
            SET b.author_id = $author_id, b.published_year = $published_year
            """, title=book.title, author_id=book.author_id, published_year=book.published_year)

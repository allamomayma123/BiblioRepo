from config.mongo_config import get_mongo_client
from config.neo4j_config import get_neo4j_driver
from models.book import Book


def sync_books():
    client = get_mongo_client()
    db = client.library
    books_collection = db.books
    driver = get_neo4j_driver()

    with driver.session() as session:
        for book_data in books_collection.find():
            book = Book.from_dict(book_data)
            session.run("""
                MERGE (b:Book {title: $title})
                SET b.author_id = $author_id, b.published_year = $published_year
                """, title=book.title, author_id=book.author_id, published_year=book.published_year)

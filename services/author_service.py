from config.neo4j_config import get_neo4j_driver
from models.author import Author


def add_author(author: Author):
    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run(
            "CREATE (a:Author {name: $name, birth_year: $birth_year})",
            name=author.name, birth_year=author.birth_year
        )

def get_authors():
    driver = get_neo4j_driver()
    with driver.session() as session:
        result = session.run("MATCH (a:Author) RETURN a.name AS name, a.birth_year AS birth_year")
        return [Author(name=record["name"], birth_year=record["birth_year"]) for record in result]

def get_author_by_id(author_id):
    driver = get_neo4j_driver()
    with driver.session() as session:
        result = session.run(
            "MATCH (a:Author) WHERE ID(a) = $id RETURN a.name AS name, a.birth_year AS birth_year",
            id=author_id
        )
        record = result.single()
        return Author(name=record["name"], birth_year=record["birth_year"]) if record else None
def update_author(name, data):
    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run("""
            MATCH (a:Author {name: $name})
            SET a.birth_year = $birth_year
            """, name=name, birth_year=data["birth_year"])

def delete_author(name):
    driver = get_neo4j_driver()
    with driver.session() as session:
        session.run("MATCH (a:Author {name: $name}) DETACH DELETE a", name=name)
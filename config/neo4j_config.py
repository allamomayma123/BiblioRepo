from neo4j import GraphDatabase

def get_neo4j_driver():
    uri = "bolt://localhost:7687"
    return GraphDatabase.driver(uri, auth=("neo4j", "password"))

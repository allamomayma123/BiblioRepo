from .. import get_db, get_graph

def synchroniser_livres():
    db = get_db()
    graph = get_graph()
    livres = db.livres.find()
    for livre in livres:
        if not graph.nodes.match("Livre", ISBN=livre["ISBN"]).first():
            auteur = graph.nodes.match("Auteur", nom=livre["auteur"]).first()
            if not auteur:
                auteur = Node("Auteur", nom=livre["auteur"])
                graph.create(auteur)
            livre_node = Node("Livre", titre=livre["titre"], ISBN=livre["ISBN"], genre=livre["genre"], annee_publication=livre["annee_publication"])
            graph.create(livre_node)
            graph.create(Relationship(auteur, "A ÉCRIT", livre_node))

from flask import Flask
from routes.routes_book import book_bp
from routes.routes_author import author_bp
from routes.routes_member import member_bp
from routes.loan_routes import loan_bp

app = Flask(__name__)

app.register_blueprint(book_bp, url_prefix='/api')
app.register_blueprint(author_bp, url_prefix='/api')
app.register_blueprint(member_bp, url_prefix='/api')
app.register_blueprint(loan_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

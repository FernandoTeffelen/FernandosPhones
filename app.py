from flask import Flask, render_template, request
from productsData import products


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/produto/<int:id>')
def produtos(id):
    produto = next((item for item in products if item["id"] == id), None)

    cores = produto["colors"].split(', ')

    if not produto:
        return "Produto não encontrado", 404

    return render_template('produto.html', produto=produto, cores=cores)

if __name__ == '__main__':
    app.run(debug=True)
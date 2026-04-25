from flask import Flask, render_template, request, redirect, url_for
import couchdb

app = Flask(__name__)

# ── CouchDB connection ────────────────────────────────────────────
couch = couchdb.Server('http://admin:admin123@localhost:5984/')
db = couch['ecommerce']


# ── READ — List all orders ────────────────────────────────────────
@app.route('/')
def index():
    docs = [db[doc_id] for doc_id in db]
    return render_template('index.html', docs=docs)


# ── CREATE — Add a new order ──────────────────────────────────────
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        doc = {
            'order_id':      request.form['order_id'],
            'customer_id':   request.form['customer_id'],
            'order_status':  request.form['order_status'],
            'customer_city': request.form['customer_city'],
            'customer_state':request.form['customer_state'],
            'price':         float(request.form['price']),
            'product_id':    request.form['product_id'],
        }
        db.save(doc)
        return redirect(url_for('index'))
    return render_template('add.html')


# ── UPDATE — Edit an existing order ──────────────────────────────
@app.route('/edit/<doc_id>', methods=['GET', 'POST'])
def edit(doc_id):
    doc = db[doc_id]
    if request.method == 'POST':
        doc['order_status']  = request.form['order_status']
        doc['price']         = float(request.form['price'])
        doc['customer_city'] = request.form['customer_city']
        db.save(doc)
        return redirect(url_for('index'))
    return render_template('edit.html', doc=doc)


# ── DELETE — Remove an order ──────────────────────────────────────
@app.route('/delete/<doc_id>')
def delete(doc_id):
    doc = db[doc_id]
    db.delete(doc)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

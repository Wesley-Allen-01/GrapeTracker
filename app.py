from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wines.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tannin_level = db.Column(db.Integer, nullable=False)  # 1-10 scale
    sweetness = db.Column(db.Integer, nullable=False)  # 1-10 scale
    overall_appeal = db.Column(db.Integer, nullable=False)  # 1-10 scale
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'tannin_level': self.tannin_level,
            'sweetness': self.sweetness,
            'overall_appeal': self.overall_appeal,
            'price': self.price,
            'description': self.description,
            'date_added': self.date_added.strftime('%Y-%m-%d')
        }


@app.route('/')
def index():
    wines = Wine.query.order_by(Wine.date_added.desc()).all()
    return render_template('index.html', wines=wines)


@app.route('/add_wine', methods=['POST'])
def add_wine():
    try:
        wine = Wine(
            name=request.form['name'],
            tannin_level=int(request.form['tannin_level']),
            sweetness=int(request.form['sweetness']),
            overall_appeal=int(request.form['overall_appeal']),
            price=float(request.form['price']),
            description=request.form['description']
        )
        db.session.add(wine)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/delete_wine/<int:wine_id>', methods=['POST'])
def delete_wine(wine_id):
    wine = Wine.query.get_or_404(wine_id)
    db.session.delete(wine)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

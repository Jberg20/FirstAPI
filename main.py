from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class Band(db.Model):
    band_ID = db.Column(db.Integer, primary_key=True)
    band_Name = db.Column(db.String(80), unique=True, nullable=False)
    band_Genre = db.Column(db.String(80), unique=True, nullable=False)
    band_Gigs = db.Column(db.Integer, nullable=False)
    band_Rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
                'band_ID': self.band_ID,
                'band_Name': self.band_Name,
                'band_Genre': self.band_Genre,
                'band_Gigs': self.band_Gigs,
                'band_Rating': self.band_Rating
        }
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

@app.route('/bands/<int:band_ID>', methods=['GET'])
def get_band(band_ID):
    band = Band.query.get(band_ID)
    if band:
        return jsonify(band.to_dict())
    else:
        return jsonify({"message": "Band not found"}), 404

@app.route('/bands', methods=['POST'])
def make_band():
    data = request.get_json()
    if not all(key in data for key in ('band_Name', 'band_Genre', 'band_Gigs', 'band_Rating')):
            return {"message": "Missing data"}, 400
    band = Band(band_Name=data['band_Name'], band_Genre=data['band_Genre'], band_Gigs=data['band_Gigs'], band_Rating=data['band_Rating'])
    db.session.add(band)
    db.session.commit()
    return {"message": "Success"}, 201


if __name__ == "__main__":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)


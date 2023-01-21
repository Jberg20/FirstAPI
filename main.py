from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
api = Api(app)
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

@app.route('/bands/<int:band_ID>', methods=['GET'])
def get_band(band_ID):
    band = Band.query.get(band_ID)
    if band:
        return jsonify(band.to_dict())
    else:
        return jsonify({"message": "Band not found"}), 404

    


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

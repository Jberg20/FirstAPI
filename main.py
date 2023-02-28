from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

class BandList(Resource):
    print("BandList loaded")
    def get(self):
        print("running getall")
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bands")
        result = c.fetchall()
        if result:
            return {"message": result}
        else:
            return {"message": "No bands found"}

    def post(self):
        print("running post method")
        data = request.get_json()
        if not all(key in data for key in ('band_name', 'band_genre', 'gigs', 'rating')):
            return {"message": "Missing data"}
        band_name = data['band_name']
        band_genre = data['band_genre']
        gigs = data['gigs']
        rating = data['rating']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO bands (band_name,band_genre,gigs,rating) VALUES (?,?,?,?)", (band_name,band_genre,gigs,rating))
        conn.commit()
        return {"message": "Success"}

    def delete(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DELETE FROM bands")
        conn.commit()
        return {"message": "All bands has been deleted"}


class Band(Resource):
    print("Band loaded")
    def get(self, band_id):
        print("running get method")
        print(band_id)
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bands WHERE band_id=?", (band_id,))
        result = c.fetchone()
        if result:
            return {"message": result}
        else:
            return {"message": "Band not found"}
    
    def put(self, band_id):
        print("running put method")
        data = request.get_json()
        if not data or not all(key in data for key in ('band_name', 'band_genre', 'gigs', 'rating')):
            return {"message": "Missing data"}
        band_name = data['band_name']
        band_genre = data['band_genre']
        gigs = data['gigs']
        rating = data['rating']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE bands SET band_name=?, band_genre=?, gigs=?, rating=? WHERE band_id=?", (band_name, band_genre, gigs, rating, band_id))
        conn.commit()
        return {"message": f"Band {band_id} updated"}
    
    def delete(self, band_id):
        print("running delete method")
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DELETE FROM bands WHERE band_id=?", (band_id,))
        conn.commit()
        return {"message":f"Band {band_id} deleted"}




    

api.add_resource(BandList, '/bands')
api.add_resource(Band, '/bands/<int:band_id>')


if __name__ == "__main__":
    print("API is active")
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS bands")
    c.execute("""CREATE TABLE IF NOT EXISTS bands (
                band_id INTEGER PRIMARY KEY,
                band_name TEXT,
                band_genre TEXT,
                gigs INTEGER,
                rating INTEGER
                )""")
    conn.commit()
    app.run(debug=True)

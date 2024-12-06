import requests
import json
from sqlalchemy.orm import Session
from backend.app import models, database

def fetch_geojson(url: str):
    response = requests.get(url)
    return response.json()

def ingest_data(db: Session, data):
    for feature in data['features']:
        db_feature = models.Feature(
            name=feature['properties'].get('name', 'Unnamed'),
            latitude=feature['geometry']['coordinates'][1],
            longitude=feature['geometry']['coordinates'][0]
        )
        db.add(db_feature)
    db.commit()

def main():
    db = database.SessionLocal()
    geojson_data = fetch_geojson("https://example.com/karnataka.geojson")
    ingest_data(db, geojson_data)

if __name__ == "__main__":
    main()
import requests
import csv

import sqlalchemy as db

engine = db.create_engine('mysql+pymysql://admin:BigChungus@database-1.ceytofxkbh8r.eu-west-1.rds.amazonaws.com/cloud')

csv_url = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-csv.csv"

with requests.Session() as s:
    download = s.get(csv_url)
    decoded_content = download.content.decode('utf-8')


def create_table():
    with engine.connect() as connection:
        engine.execute('drop table if exists itsyaboi')
        engine.execute('create table itsyaboi ( nom varchar(20), age smallint )')


def update_db():
    with engine.connect() as connection:
        engine.execute('insert into itsyaboi values ("jack", 21), ("suffered", 22), ("greatly", 23), ("while", 24), ("making", 25), ("this", 26), ("cloudapp", 27)')

create_table()
update_db()

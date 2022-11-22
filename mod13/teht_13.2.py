from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='admin',
    password='admin1',
    autocommit=True
)
app = Flask(__name__)
@app.route('/kentta/<icao>')

def kentta(icao):
    try:
        icao = str(icao)
        sql ="SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            name = i[0]
            city = i[1]
        statusCode = 200
        answer = {
            "ICAO": icao,
            "Name": name,
            "Municipality": city,
        }

    except ValueError:
        statusCode = 400
        answer = {
            "status": statusCode,
            "text": "Virheellinen yhteenlaskettava"
        }

    jsonAnswer = json.dumps(answer)
    return Response(response=jsonAnswer, status=statusCode, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(errorCode):
    answer = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonAnswer = json.dumps(answer)
    return Response(response=jsonAnswer, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

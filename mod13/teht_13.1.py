from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(num):
    try:
        num = int(num)
        for i in range(2, num):
            if num % i == 0:
                result = False
                break
            else:
                result = True
        statusCode = 200
        answer = {
            "Number": num,
            "isPrime": result,
        }

    except ValueError:
        tilakoodi = 400
        answer = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
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
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
import json
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator", static_folder="static")

@app.route("/englishToFrench", methods=["GET"])
def englishToFrench():
    textToTranslate = request.args.get('Hello')
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish", methods=["GET"])
def frenchToEnglish():
    textToTranslate = request.args.get('Bonjour')
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text

@app.route("/", methods=["POST"])
def renderIndexPage():
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

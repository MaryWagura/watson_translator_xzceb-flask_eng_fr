from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract the translated text from the API response
    french_text = translation['translations'][0]['translation']

    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
   translation = language_translator.translate(
    # Extract the translated text from the API response
    english_text = translation['translations'][0]['translation']
    return "Translated text to English"

@app.route("/index.html")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from flask import Flask, request, render_template
from markupsafe import escape
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")


@app.route("/")
def home():
    """
    Returns index.htmml
    :return:
    """
    return render_template("index.html")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = english_to_french(textToTranslate)
    return "Translated text to French: {}".format(translation)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = french_to_english(textToTranslate)
    return "Translated text to English : {}".format(translation)


@app.route("/")
def renderIndexPage():
    pass
    # Write the code to render template


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

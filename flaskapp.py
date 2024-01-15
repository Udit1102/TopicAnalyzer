from text_analysis_lib import text_analyzer
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def analyzer():
    article1 = str(request.form.get("article1"))
    article2 = str(request.form.get("article2"))
    article3 = (request.form.get("article3"))
    result = text_analyzer(article1, article2, article3)
    return "News articles analyzed topics are:\n"+result

if __name__ == "__main__":
	app.run(debug=True)
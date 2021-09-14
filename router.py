from flask import Flask
from flask.templating import render_template
import movie_api as ma
import naver_temperature as nt

app = Flask(__name__)

@app.route("/")
def hello():                             # 키 값
    return render_template("index.html", movies=ma.callMovieApi(), temperature=nt.callTemperature()) # 파일 리턴

if __name__ == "__main__":
    app.run(debug=True) # 저장 시 리로드
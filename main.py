from model.index import GA
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/api/getData", methods=["POST"])
def getData():
    try:
        data = request.get_json()
        n = int(data["n"])
        p = int(data["p"])
        t = int(data["t"])
        k = int(data["k"])
        r = int(data["r"])
        b = int(data["b"])
        m_min = int(data["m_min"])
        m_max = int(data["m_max"])
        h_min = int(data["h_min"])
        h_max = int(data["h_max"])
        d_min = int(data["d_min"])
        d_max = int(data["d_max"])
        f_min = int(data["f_min"])
        f_max = int(data["f_max"])
        seed = int(data["seed"])
        result = GA(
            n,
            t,
            p,
            r,
            k,
            b,
            m_min,
            m_max,
            h_min,
            h_max,
            d_min,
            d_max,
            f_min,
            f_max,
            seed,
        )
        response = {"data": result}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)

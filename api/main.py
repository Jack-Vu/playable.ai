from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
import ai_agent


app = Flask(__name__)
cors = CORS(app)


@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No image file found"}), 400
    image = request.files["image"]
    image_to_process = Image.open(image)
    result = ai_agent.nameGames(image_to_process)
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)

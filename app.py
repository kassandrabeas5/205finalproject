# CST 205 - Summer 2025
# Project: Virtual Travel Gallery
# Authors: Kassandra Beas
# Date: July 15, 2025
# Description: Flask app for viewing world travel destinations.

from flask import Flask, render_template, request
import random
from image_info import image_data

app = Flask(__name__)

@app.route('/')
def index():
    region = request.args.get('region', 'All')
    all_regions = sorted({info["region"] for info in image_data.values()})

    if region == 'All':
        filtered_images = list(image_data.keys())
    else:
        filtered_images = [img for img, info in image_data.items() if info["region"] == region]

    random.shuffle(filtered_images)
    return render_template("index.html", images=filtered_images, image_data=image_data,
                           region=region, all_regions=all_regions)

@app.route('/detail/<image_name>')
def detail(image_name):
    info = image_data.get(image_name, {})
    return render_template("detail.html", image_name=image_name, info=info)
    
if __name__ == '__main__':
    app.run(debug=True)


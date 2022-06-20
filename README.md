# SnekRay
![example branch parameter](https://github.com/vextor22/snekray/actions/workflows/python-package.yml/badge.svg?branch=main)


Python implementation of "The Ray Tracer Challenge"

For testing:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
dotenv run -- python example.py
```
---
## Convert
To convert the PPM image output to PNG for display in this readme, I've used ImageMagick:
```
cd scenes
magick mogrify -format png *.ppm
```
---
## Examples

Chapter 2


<img src="./scenes/output.png?raw=true" height="300">

---
Chapter 4


<img src="./scenes/clock.png?raw=true" height="300">

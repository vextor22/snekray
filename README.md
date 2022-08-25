# SnekRay
![example branch parameter](https://github.com/vextor22/snekray/actions/workflows/python-package.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/vextor22/snekray/branch/main/graph/badge.svg?token=BB26TPRNPO)](https://codecov.io/gh/vextor22/snekray)

## Coverage
# <img src="https://codecov.io/gh/vextor22/snekray/branch/main/graphs/tree.svg?token=BB26TPRNPO"/>


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

---
Chapter 5


<img src="./scenes/sphere.png?raw=true" height="300">

---
Chapter 6

Phong lighting with a scaled and sheared sphere.

<img src="./scenes/sphere_with_light.png?raw=true" height="300">
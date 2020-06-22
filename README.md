# auto-cat-namer

Automagically write names right after detecting cat's faces using OpenCV Haar Cascades. It consumes data from a CSV in form of (filename, name), there's an example in `./data`

I was curious about how to detect animal's faces on images so I wrote this. If I keep studying I may use some sort of algorithm with Keras/TensorFlow later.

Install with:

```bash
python setup.py install
```

And:

```
cd data && auto-cat-namer --input-csv=./filename_names.csv --output-path=./
```

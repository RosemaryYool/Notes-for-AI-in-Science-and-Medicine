Here's the Markdown format for your `README.md` file:

```markdown
# Counter Demo

This is a simple web application that demonstrates a counter. It allows you to increment or decrement the counter value.

## Requirements

- Python 3.x
- `microdot` library

## Installation

1. Clone the repository.
2. Install the required library: `pip install microdot`.

## Usage

1. Run the following code:

```python
from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc(counter):
    return '''
        <html>
            <head>
                <title>Counter Demo</title>
            </head>
            <body>
                <div>
                    <h1>Counter: {counter}</h1>
                    <a href="/change/{counter}/1"><button>Increment</button></a>
                    <a href="/change/{counter}/-1"><button>Decrement</button></a>
                </div>
            </body>
        </html>
        '''

@app.route('/')
def home(request):
    return htmldoc(0)

@app.route('/change/<current_counter>/<step>')
def change(request, current_counter, step):
    counter = int(current_counter) + int(step)
    return htmldoc(counter)

app.run(debug=True, port=8008)
```

2. Open your web browser and go to `http://localhost:8008` to see the counter demo.

Note: Make sure you have the required dependencies installed before running the code.

Feel free to modify the installation and usage instructions according to your needs.

---

# Data Points Scatter Plot

This is a simple web application that generates a scatter plot of random data points using Matplotlib.

## Requirements

- Python 3.x
- `microdot` library
- `numpy` library
- `matplotlib` library

## Installation

1. Clone the repository.
2. Install the required libraries: `pip install microdot numpy matplotlib`.

## Usage

1. Run the following code:

```python
import base64
import io
from io import BytesIO
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from microdot import Microdot, Response
app = Microdot()
Response.default_content_type = 'text/html'


@app.route("/")
@app.route("/<points>")
def hello(request,points = "10"):

    points = int(points)

    data = np.random.rand(points, 2)

    fig = Figure()
    FigureCanvas(fig)

    ax = fig.add_subplot(111)

    ax.scatter(data[:,0], data[:,1])

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'There are {points} data points!')
    ax.grid(True)

    img = io.StringIO()
    fig.savefig(img, format='svg')
    #clip off the xml headers from the image
    svg_img = '<svg' + img.getvalue().split('<svg')[1]
    
    return svg_img
    
    
app.run(host="0.0.0.0",port=5000,debug = True)
```

2. Open your web browser and go to `http://localhost:5000` to see the scatter plot.

Note: Make sure you have the required dependencies installed before running the code.

Feel free to modify the installation and usage instructions according to your needs.
```

Make sure to save the respective content in separate sections of your `README.md` file.

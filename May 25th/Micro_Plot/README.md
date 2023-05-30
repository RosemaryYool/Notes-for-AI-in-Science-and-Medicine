Here's the README.md file for the code you provided:

```markdown
# SVG Image Generator

This is a Python application that generates an SVG image with random colors and displays it in a web browser.

## Dependencies

- microdot
- matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install microdot matplotlib
   ```

## Usage

1. Import the necessary modules:

   ```python
   import base64
   import io
   from io import BytesIO
   import numpy as np
   from microdot import Microdot, Response
   from matplotlib.figure import Figure
   from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
   ```

2. Create an instance of the Microdot application:

   ```python
   app = Microdot()
   ```

3. Define a route handler function:

   ```python
   @app.route('/')
   @app.route('/<points>')
   def hello(request, points="10"):
       # ...
   ```

4. Parse the `points` parameter and convert it to an integer:

   ```python
   points = int(points)
   ```

5. Create a `Figure` object and a `FigureCanvas`:

   ```python
   fig = Figure()
   FigureCanvas(fig)
   ```

6. Add a subplot to the figure and generate random RGB data:

   ```python
   ax = fig.add_subplot(111)
   RGB_data = np.random.rand(points, points, 3)
   ax.imshow(RGB_data)
   ```

7. Set the title of the plot:

   ```python
   ax.set_title(f'There are {points**2} pixels!')
   ```

8. Save the figure as an SVG image:

   ```python
   img = io.StringIO()
   fig.savefig(img, format='svg')
   svg_img = '<svg' + img.getvalue().split('<svg')[1]
   ```

9. Return the SVG image as the response:

   ```python
   return Response(svg_img, headers={'Content-Type': 'image/svg+xml'})
   ```

10. Run the application:

    ```python
    app.run(host="0.0.0.0", port=8008, debug=True)
    ```

11. Access the application by navigating to `http://localhost:8008` in your web browser.

## Image Generation

The application generates an SVG image with a grid of pixels. Each pixel has a random RGB color.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace `<repository-url>` with the actual URL of your repository.

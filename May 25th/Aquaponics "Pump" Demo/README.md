Here's the README.md file for the code you provided:

```markdown
# Aquaponics System Control

This is a Python application that allows you to control an aquaponics system by toggling the water pump and air pump on or off.

## Dependencies

- microdot_asyncio

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install microdot_asyncio
   ```

## Usage

1. Import the necessary modules:

   ```python
   from microdot_asyncio import Microdot, Response
   ```

2. Create an instance of the Microdot application:

   ```python
   app = Microdot()
   ```

3. Set the default content type of the response to 'text/html':

   ```python
   Response.default_content_type = 'text/html'
   ```

4. Define a function to generate the HTML document:

   ```python
   def htmldoc(water_pump_status, air_pump_status):
       # ...
   ```

5. Define the route for the control page:

   ```python
   @app.route('/')
   def control(request):
       # ...
   ```

6. Define the route for toggling the components:

   ```python
   @app.route('/toggle/<component>')
   def toggle(request, component):
       # ...
   ```

7. Run the application:

   ```python
   app.run(debug=True, port=8008)
   ```

8. Access the application by navigating to `http://localhost:8008` in your web browser.

## HTML and CSS Styling

The application generates HTML with CSS styling to display buttons for controlling the water pump and air pump. The buttons are styled based on their status (ON or OFF).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace `<repository-url>` with the actual URL of your repository.

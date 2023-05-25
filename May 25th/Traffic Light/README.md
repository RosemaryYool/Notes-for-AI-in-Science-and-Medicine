Certainly! Here's the code converted into Markdown format for a README.md file:

```markdown
# Traffic Light Web Application

This is a Python script that creates a web application for a traffic light using the Microdot library.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/traffic-light-web-app.git
   ```

2. Install the required dependencies:

   ```shell
   pip install microdot
   ```

## Usage

1. Import the necessary modules:

   ```python
   from microdot import Microdot, Response
   ```

2. Set up the Microdot application:

   ```python
   app = Microdot()
   Response.default_content_type = 'text/html'
   ```

3. Define the HTML document generation function:

   ```python
   def htmldoc():
       # ... (code omitted for brevity)
       return html_code
   ```

4. Define the root route:

   ```python
   @app.route('/')
   def hello(request):
       return htmldoc()
   ```

5. Define the toggle_light route:

   ```python
   @app.route('/toggle/<light_index>')
   def toggle_light(request, light_index):
       # ... (code omitted for brevity)
       return htmldoc()
   ```

6. Start the application:

   ```python
   app.run(debug=True, port=8009)
   ```

7. Access the web application:

   Open your web browser and navigate to `http://localhost:8009` to view the traffic light page. Click on the circles representing the traffic lights to toggle their colors.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Save the above code as `README.md` in the root directory of your project, and it will serve as the README file for your traffic light web application.

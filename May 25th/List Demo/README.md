Here's the README.md file for the code you provided:

```markdown
# To-Do List

This is a Python application that allows you to manage a to-do list. You can add tasks, mark them as complete or uncomplete, and delete tasks from the list.

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
   def htmldoc():
       # ...
   ```

5. Define the route for the home page:

   ```python
   @app.route('/', methods=['GET', 'POST'])
   async def home(request):
       # ...
   ```

6. Define the route for adding a task:

   ```python
   @app.route('/add', methods=['POST'])
   async def add(request):
       # ...
   ```

7. Define the route for toggling a task's completion status:

   ```python
   @app.route('/toggle/<index>')
   async def toggle(request, index):
       # ...
   ```

8. Define the route for deleting a task:

   ```python
   @app.route('/delete/<index>')
   async def delete(request, index):
       # ...
   ```

9. Run the application:

   ```python
   app.run(debug=True, port=8008)
   ```

10. Access the application by navigating to `http://localhost:8008` in your web browser.

## HTML and Form Handling

The application generates HTML with a form for adding new tasks. Tasks are displayed as a list, and each task has options to mark it as complete or uncomplete and to delete it from the list.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace `<repository-url>` with the actual URL of your repository.

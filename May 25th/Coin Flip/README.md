Here's the code in Markdown format:

```markdown
# Coin Flip Game

This is a simple web application that allows you to play a coin flip game. When you click the coin, it will randomly show either "Heads" or "Tails".

## Requirements

- Python 3.x
- `numpy` library
- `microdot` library

## Installation

1. Clone the repository.
2. Install the required libraries: `pip install numpy microdot`.

## Usage

1. Run the following code:

```python
import numpy as np
from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = "text/html"

def htmldoc():
    global coin_state
    coin_text = "Heads" if coin_state == 0 else "Tails"

    html = '''
        <html>
        <head>
            <title>Coin Flip Game</title>
        </head>
        <body>
            <div>
                <h1>Click the Coin to Flip</h1>
                <svg width="400" height="400" viewBox="0 0 400 400">
                    <a href="/toggle">
                        <circle style="fill:#0000FF" cx="60" cy="100" r="50"/>
                        <circle style="fill:#FFFF00"  cx="160" cy="90" r="50"/>
                        <circle style="fill:#FFC0CB" cx="260" cy="120" r="50"/>
                        <text x="60%" y="60%" font-size="30" text-anchor="middle" dy=".3em">{coin_text}</text>
                    </a>
                </svg>
            </div>
        </body>
        </html>
        '''
    return html

@app.route("/")
def home(request):
    global coin_state
    coin_state = np.random.randint(2)
    return htmldoc()

@app.route("/toggle")
def toggle_coin(request):
    global coin_state
    coin_state = np.random.randint(2)
    return htmldoc()

app.run(debug=True, port=8010)
```

2. Open your web browser and go to `http://localhost:8010` to play the coin flip game.

Note: Make sure you have the required dependencies installed before running the code.
```

You can save this content in a file named `README.md` in your project directory. Feel free to modify the installation and usage instructions according to your needs.

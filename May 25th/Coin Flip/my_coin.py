import numpy as np
from microdot import Microdot, Response
app = Microdot()
Response.default_content_type = "text/html"

def htmldoc():
    global coin_state
    coin_text = "Heads" if coin_state == 0 else "Tails"
    
    html = f'''
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

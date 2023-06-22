from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc():
    doc = f'''
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Dashboard CSS - Demo</title>
            <link rel="stylesheet" href="https://williamedwardhahn.github.io/AI_Science_Medicine/dashboard.css">
        </head>
        <body style="background-color: #77afbd;"> 
            <header>
                <h1>Welcome to the Dashboard!</h1>
            </header>
            <nav>
                <input type="checkbox" id="nav-menu-btn" />
                <label for="nav-menu-btn"></label>
                <ul>
                    <li><a href="#">My Profile</a></li>
                    <li><a href="#">My Projects</a></li>
                    <li><a href="#">Color Selections</a></li>
                    <li><a href="#">System Calibration</a></li>
                </ul>
            </nav>
            <main class="container-fluid">
              <div class="row">

                <div class="col-xs-12 col-sm-6 col-md-3">
                  <div class="panel">
                    <header>
                      <h2>Temperature</h2>
                    </header>
                    <main>
                      <h3>23.5<sub>&deg;C</sub></h3>
                    </main>
                    <footer>
                      <time>2016_04_01 12:21 UTC</time>
                    </footer>
                  </div>
                </div>

        <div class="col-xs-12 col-sm-12 col-md-6">
          <div class="panel info">
            <header>
              <h2>About</h2>
            </header>
            <main>
              <p>In this dashboard, you will be able to capture your images, 
              which will be used to train a Convolutional Neural Network (CNN)
              model. The intended purpose of this training is to later be able 
              to use designated hand gestures to turn the volume of sound up or 
              down. 
              </p>
            </main>
            <footer>
            </footer>
          </div>
        </div>

      </div>

      <div class="row">

        <div class="col-xs-12 col-sm-12 col-md-6">
          <div class="panel double success">
            <header>
              <h2>Hand Gestures to Adjust Volume</h2>
            </header>
            <main>
              <img src="Users/rosemaryyool/Desktop/Microscope/one_and_two_hands.png" alt="hand gestures" />
              <p>In order to run this program correctly, please begin by taking images of your 
              own hand gestures. The hand gestures used will be the hand gesture for the number 
              "1" and "2". The program is designed to capture 20 images in 1 second intervals. 
              Please pose your hands for approximately 10 images for each gesture, providing 
              each gesture with a slight variation. For example, for the number "2", turn your
              hands palms towards the camera as well as away. 
              </p>
            </main>
            <footer>
            </footer>
          </div>
        </div>

        <div class="col-xs-12 col-sm-12 col-md-6">
          <div class="panel double">
            <header>
              <h2>Motor Control</h2>
            </header>
            <main>
              <form>
                <div class="row">
                  <div class="col-md-3">
                    <label>Motor TL</label>
                    <input type="number" value="210" />
                  </div>
                  <div class="col-md-3">
                    <label>Motor TR</label>
                    <input type="number" value="0" />
                  </div>
                  <div class="col-md-3">
                    <label>Motor BL</label>
                    <input type="number" value="405" />
                  </div>
                  <div class="col-md-3">
                    <label>Motor BR</label>
                    <input type="number" value="313" />
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-3">
                    <label>Trim TL</label>
                    <input type="number" value="14" />
                  </div>
                  <div class="col-md-3">
                    <label>Trim TR</label>
                    <input type="number" value="0" />
                  </div>
                  <div class="col-md-3">
                    <label>Trim BL</label>
                    <input type="number" value="0" />
                  </div>
                  <div class="col-md-3">
                    <label>Trim BR</label>
                    <input type="number" value="-10" />
                  </div>
                </div>

                <button class="info">Apply</button>
                <button class="warning">Execute</button>
                <button class="danger">Halt</button>
              </form>
            </main>
          </div>
        </div>

      </div>

    </main>
    <footer>
      <p>
        <small>
        MPCR Lab
        </small>
      </p>
    </footer>
  </body>
</html>
'''
    return doc


@app.route('/')
def serve_html(request):
    return htmldoc()

app.run(debug=True, port=8011)

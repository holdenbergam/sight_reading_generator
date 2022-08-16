import os
from flask import Flask, render_template, request, url_for, flash, redirect
from .processing import make_random_music
from flask_caching import Cache
import time

# ...

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_url_path="", static_folder="static",instance_relative_config=True)
    #app.config["CACHE_TYPE"] = "null"
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        #CACHE_TYPE='SimpleCache'
    )

    #cache = Cache(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def home():
        return render_template('index.html')


    @app.route('/result', methods=['GET', 'POST'])
    #@cache.cached(timeout=20000)
    def shortenurl():
        if request.method == 'POST':
            time_ = request.form['time']
            key = request.form['key']
            instrument = request.form['instrument']
            measures = request.form['measures']
            level = request.form['level']
            image_name = "image.pdf?" + str(time.time())
            music_name = "music_output.mid?" + str(time.time())

            make_random_music(time_,key,measures,instrument,level,save_to='static/image.pdf')

            #music = make_random_music(time, key, instrument)
            #image = make_image(music)

            return render_template('result.html', time=time_, key=key, measures=measures, instrument=instrument, level=level, image_name=image_name, music_name=music_name)
        elif request.method == 'GET':
            return 'A GET request was made'
        else:
            return 'Not a valid request method for this route'

    return app

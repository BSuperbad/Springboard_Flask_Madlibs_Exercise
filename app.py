from flask import Flask, request, render_template
from stories import stories
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Shows home and dropdown menu for each story option"""
    print(stories)
    return render_template('dropdown.html', stories=stories.values())


@app.route('/madlib-v2')
def create_madlib():
    """Shows form to ask prompts"""
    story_title = request.args["story_title"]
    story = stories[story_title]
    words = story.prompts
    return render_template('madlib_v2.html', story_title=story_title, words=words)


@app.route('/story_v2')
def show_story():
    """Plugs in the words to create story"""
    story_title = request.args["story_title"]
    story = stories[story_title]
    text = story.generate(request.args)
    return render_template('story_v2.html', title=story_title, text=text)

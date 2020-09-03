from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
def index():
    user_stories = data_handler.get_all_user_story()

    return render_template('index.html', user_stories=user_stories)


@app.route('/story')
@app.route('/story/<int:id_story>')
def story(id_story=None):
    return render_template('story.html', id_story=id_story)


if __name__ == '__main__':
    app.run()

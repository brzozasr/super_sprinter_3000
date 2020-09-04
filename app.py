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
    if id_story is not None:
        data_to_update = data_handler.get_by_id_user_story(id_story)
        print(data_to_update, "TEST")
    else:
        data_to_update = None
    return render_template('story.html', id_story=id_story, statusies=data_handler.STATUSES,
                           data_update=data_to_update)


@app.route('/add', methods=['GET', 'POST'])
@app.route('/update/<int:id_story>', methods=['GET', 'POST'])
def add_update_story(id_story=None):
    if request.method == 'POST' and id_story is None:
        first_status = 0
        id_us = data_handler.get_id_for_user_story()
        title = request.form['title']
        user_story = request.form['story']
        criteria = request.form['criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = data_handler.STATUSES[first_status]
        story_to_add = {'id': id_us, 'title': title, 'user_story': user_story, 'acceptance_criteria': criteria,
                        'business_value': business_value, 'estimation': estimation, 'status': status}
        data_handler.add_user_story_to_file(story_to_add)
        return redirect('/')
    elif request.method == 'POST' and id_story is not None:
        id_us = id_story
        title = request.form['title']
        user_story = request.form['story']
        criteria = request.form['criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        story_to_update = {'id': id_us, 'title': title, 'user_story': user_story, 'acceptance_criteria': criteria,
                           'business_value': business_value, 'estimation': estimation, 'status': status}
        data_handler.update_user_story_to_file(story_to_update)
        return redirect('/')
    else:
        return redirect('/')


@app.route('/delete/<int:id_story>')
def delete_story(id_story):
    data_handler.delete_user_story_to_file(id_story)
    return redirect('/')


if __name__ == '__main__':
    app.run()

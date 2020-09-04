import csv
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
csv_file = os.path.join(current_dir, "data.csv")
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']

highest_id = 1


def get_all_user_story():
    with open(csv_file, 'r') as csv_data:
        stories_list = []
        reader = csv.DictReader(csv_data)
        for row in reader:
            stories_list.append(row)
    return stories_list


def get_by_id_user_story(id_story):
    with open(csv_file, 'r') as csv_data:
        reader = csv.DictReader(csv_data)
        for row in reader:
            if row['id'] == str(id_story):
                return row
        return None


def get_highest_id():
    stories_list = get_all_user_story()
    tmp_id = 0
    for story in stories_list:
        if int(story['id']) > tmp_id:
            tmp_id = int(story['id'])
    return tmp_id


def set_highest_id(value):
    global highest_id
    highest_id = value


set_highest_id(get_highest_id())


def get_id_for_user_story():
    """Generate ID for adding User Story."""
    tmp_id = highest_id + 1
    set_highest_id(tmp_id)
    return tmp_id


def add_user_story_to_file(story_dict):
    with open(csv_file, 'a') as csv_data:
        writer = csv.DictWriter(csv_data, fieldnames=DATA_HEADER)
        writer.writerow(story_dict)


def write_to_file_all_user_story(stories_list_of_dict):
    with open(csv_file, 'w') as csv_data:
        writer = csv.DictWriter(csv_data, fieldnames=DATA_HEADER)
        writer.writeheader()
        writer.writerows(stories_list_of_dict)


def update_user_story_to_file(story_dict):
    stories_list = get_all_user_story()
    count = 0
    for story in stories_list:
        if story['id'] == str(story_dict['id']):
            stories_list.pop(count)
            stories_list.insert(count, story_dict)
            break
        count += 1
    write_to_file_all_user_story(stories_list)


def delete_user_story_to_file(id_story):
    stories_list = get_all_user_story()
    count = 0
    for story in stories_list:
        if story['id'] == str(id_story):
            stories_list.pop(count)
            break
        count += 1
    write_to_file_all_user_story(stories_list)

import csv
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
csv_file = os.path.join(current_dir, "data.csv")
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    with open(csv_file, 'r') as csv_data:
        story_list = []
        reader = csv.DictReader(csv_data)
        for row in reader:
            story_list.append(row)
    return story_list

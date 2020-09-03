# Super Sprinter 3000

## Story

In this assignment you'll build a simple web application that might help
teams to track their progress during a project. You'll learn about agile
development later so let us summarize some concepts here:

- **User story description**: a natural language description/story from
  the perspective of a user of the system. Example: "As a \<persona\>, I
  want \<what?\> so that \<why?\>"
- **Acceptance Criteria**: a set of statements, each with a clear
  pass/fail result, that specify both functional and non-functional
  requirements.
- **Business value**: a numerical value to represent the importance of
  the User Story for the so called business (actually the customer).
- **Estimation**: Summary of the expected amount of work in all tasks
  collected to achieve User Story.
- **Status**: Current state of the User Story's development cycle.

Your system should be able to list, create, and update User Stories.

## What are you going to learn?

You will learn and practice how to do the following things:

 - create a Flask project
 - use routes with Flask
 - use HTML and the Jinja templating engine.

## Tasks

1. List all User Stories on the opening page.
    - The opening page of the website (`/`) shows all data of the saved user stories.
    - The page has an HTML `<table>` element containing all the data.
    - The columns are: "Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", "Estimation", "Status".
    - The column titles are proper table headers.
    - There is an "Add a new User Story" link on the top of the page, pointing to the `/story` page.
    - The Story titles are links, pointing to the `/story/<id>` page where the User Story can be updated.
    - The page follows this basic design: ![Super Sprinter 3000 - List.png](https://learn.code.cool/media/web-python/super-sprinter-3000-list.png)

2. It is possible to add a new User Story through a web form on page `/story`.
    - Page `/story` shows an empty web form.
    - The form has an input field for all the User Story fields except for `id` and `status`.
    - The following form validation rules are applied:
- Story Title: single line text input, required, minimum 5 characters
- User Story: multiline text input, required
- Acceptance Criteria: multiline text input, required
- Business value: single line number input, allow values only dividable by 100, between 100 and 1500
- Estimation: single line number input, allow values only dividable by 0.5, between 0.5 and 40.

    - By clicking the "Add new User Story" button, the form submits the data that gets saved.
    - When a new User Story is saved, a unique `id` is generated for it.
    - The page follows this basic design: ![Super Sprinter 3000 - Add.png](https://learn.code.cool/media/web-python/super-sprinter-3000-add.png)

3. It is possible to update an existing User Story through a web form on page `/story/<id>`.
    - Page `/story/<id>` shows the same web form as on the "Add new" page but filled in with data of the given User Story.
    - The form has an input field for all the User Story fields except `id`.
    - The following form validation rules are applied (same as at addition):
- Story Title: single line text input, required, minimum 5 characters
- User Story: multiline text input, required
- Acceptance Criteria: multiline text input, required
- Business value: single line number input, allow values only dividable by 100, between 100 and 1500
- Estimation: single line number input, allow values only dividable by 0.5, between 0.5 and 40.

    - The "Status" field also appears as a dropdown value list, with options `planning`, `todo`, `in progress`, `review`, `done`.
 The current status of the User Story should be selected by default.
    - Clicking the "Update User Story" button updates the existing entry and does not create a new one.
    - The page follows this basic design: ![Super Sprinter 3000 - Add.png](https://learn.code.cool/media/web-python/super-sprinter-3000-update.png)

4. The application persists data using a `.csv` file.
    - The User Story list and the form data upon update is loaded from a `.csv` file.
    - Form data is saved to a `.csv` file.

## General requirements

None

## Hints

- You **don't** have to use CSS!
- Use template inheritance to avoid code duplication: <http://flask.pocoo.org/docs/0.12/patterns/templateinheritance/>.
- Use the same form template file for both adding and updating the User Stories.
- We suggest you to use the `csv` module of Python. It has a
  `DictReader` and a `DictWriter` function: use them and work with
  dictionaries instead of lists accordingly.

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/solo/blueprint/super-sprinter-3000/python).

## Background materials

- <i class="far fa-exclamation"></i> [A web-framework for Python: Flask](https://learn.code.cool/full-stack/#/../pages/python/python-flask)
- <i class="far fa-open_book"></i> [Flask documentation](http://flask.palletsprojects.com/) (the Quickstart gives a good overview)
- <i class="far fa-open_book"></i> [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- [Tips & Tricks](https://learn.code.cool/full-stack/#/../pages/web/web-with-python-tips.md)
- [About unique identifiers](https://learn.code.cool/full-stack/#/../pages/general/unique-id.md)

from flask import Flask, request, render_template
import unittest

app = Flask(__name__)

tasks = []

def add_task(task):
    tasks.append(task)

def get_tasks():
    return tasks

@app.route('/')
def index():
    return render_template('index.html', tasks=get_tasks())

@app.route('/add-task', methods=['POST'])
def add_task_route():
    task = request.form.get('task')
    if task:
        add_task(task)
    return render_template('index.html', tasks=get_tasks())

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_task(self):
        add_task("Test Task")
        self.assertIn("Test Task", tasks)

    def test_get_tasks(self):
        tasks.clear()
        add_task("Task 1")
        add_task("Task 2")
        self.assertEqual(get_tasks(), ["Task 1", "Task 2"])

    def test_add_task_route(self):
        tasks.clear()
        response = self.app.post('/add-task', data={"task": "Task via Route"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task via Route", response.data)
        self.assertIn("Task via Route", tasks)

if __name__ == "__main__":
    app.run(debug=True)

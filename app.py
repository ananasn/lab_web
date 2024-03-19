from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('meow_task')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# tasks = [
#     {'todo': 'Поспать',
#      'deadline': '12.12.2025',
#      'ready': False,
#      'id': 0},
#     {'todo': 'Погулять',
#      'deadline': '12.12.2025',
#      'ready': True,
#      'id': 1},
#     {'todo': 'Поесть',
#      'deadline': '12.12.2025',
#      'ready': False,
#      'id': 2}
#     ]


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(500))
    deadline = db.Column(db.String(20))
    ready = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id} / {self.deadline}> {self.todo}'


@app.route('/')
def main():
    tasks = Task.query.all()
    print(tasks)
    return render_template('index.html',
                            tasks_list=tasks)


@app.route('/ready/<int:task_id>', methods=['PATCH'])
def modify_task(task_id):
    task = Task.query.get(task_id)
    task.ready = request.json['ready']
    db.session.commit()
    # global tasks
    # ready = request.json['ready']
    # for task in tasks:
    #     if task['id'] == task_id:
    #         task.update({'ready': ready})
    return 'Ok'


@app.route('/task', methods=['POST'])
def  create_task():
    data = request.json
    task = Task(**data)
    db.session.add(task)
    db.session.commit()
    # last_id = tasks[-1]['id']
    # new_id = last_id + 1
    # data['id'] = new_id
    # tasks.append(data)
    return 'Ok'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
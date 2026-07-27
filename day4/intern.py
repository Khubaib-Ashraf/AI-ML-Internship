class Intern:

    def __init__(self, intern_id, name, email, cnic):

        self.intern_id = intern_id
        self.name = name
        self.email = email
        self.cnic = cnic
        self.tasks = []

    def add_task(self, task_name):

        task = {
            "task": task_name,
            "status": "Pending"
        }

        self.tasks.append(task)

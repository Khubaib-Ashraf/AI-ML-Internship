from intern import Intern
from filehandler import FileHandler


class InternshipSystem:

    def __init__(self):

        self.interns = {}

        self.load_records()

def generate_id(self):

        number = len(self.interns) + 1

        return f"INT-2026-{number:03}"
def register_intern(self):

        name = input("Enter Name : ")

        email = input("Enter Email : ")

        cnic = input("Enter CNIC : ")

        for intern in self.interns.values():

            if intern.email == email or intern.cnic == cnic:

                print("Duplicate Intern Found.")

                return

        intern_id = self.generate_id()

        intern = Intern(intern_id, name, email, cnic)

        self.interns[intern_id] = intern

        print("Intern Registered Successfully.")
def assign_task(self):

        intern_id = input("Enter Intern ID : ")

        if intern_id not in self.interns:

            print("Intern Not Found.")

            return

        task = input("Enter Task : ")

        self.interns[intern_id].add_task(task)

        print("Task Assigned.")
def update_task(self):

        intern_id = input("Enter Intern ID : ")

        if intern_id not in self.interns:

            print("Intern Not Found.")

            return

        intern = self.interns[intern_id]

        for i, task in enumerate(intern.tasks):

            print(i + 1, task["task"], task["status"])

        choice = int(input("Select Task : ")) - 1

        status = input("Pending / In Progress / Completed : ")

        intern.tasks[choice]["status"] = status

        print("Status Updated.")
def search(self):

        value = input("Enter Name or ID : ").lower()

        for intern in self.interns.values():

            if value == intern.intern_id.lower() or value == intern.name.lower():

                print()

                print(intern.intern_id)

                print(intern.name)

                print(intern.email)

                print(intern.cnic)

                return

        print("Intern Not Found.")
def pending_tasks(self):

        for intern in self.interns.values():

            for task in intern.tasks:

                if task["status"] == "Pending":

                    print(intern.name, ":", task["task"])
def completed_tasks(self):

        for intern in self.interns.values():

            for task in intern.tasks:

                if task["status"] == "Completed":

                    print(intern.name, ":", task["task"])
def calculate_score(self, intern):

        score = 0

        for task in intern.tasks:

            if task["status"] == "Completed":

                score += 10

            elif task["status"] == "In Progress":

                score += 5

        return score
def rank(self, score):

        if score >= 80:

            return "Gold"

        elif score >= 40:

            return "Silver"

        else:

            return "Bronze"
def top_performer(self):

        best = None

        highest = -1

        for intern in self.interns.values():

            score = self.calculate_score(intern)

            if score > highest:

                highest = score

                best = intern

        if best:

            print(best.name)

            print(highest)
def save_records(self):

        data = []

        for intern in self.interns.values():

            data.append({

                "id": intern.intern_id,

                "name": intern.name,

                "email": intern.email,

                "cnic": intern.cnic,

                "tasks": intern.tasks

            })

        FileHandler.save_data(data)
def load_records(self):

        data = FileHandler.load_data()

        for item in data:

            intern = Intern(

                item["id"],

                item["name"],

                item["email"],

                item["cnic"]

            )

            intern.tasks = item["tasks"]

            self.interns[item["id"]] = intern

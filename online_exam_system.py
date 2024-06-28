import webbrowser

# User authentication
def login(username, password):
    # authenticate the user by checking if the username and password are valid
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Exam creation
class Exam:
    def __init__(self, name, duration, num_questions):
        self.name = name
        self.duration = duration
        self.num_questions = num_questions

    def create_exam(self):
        # create an exam with the specified name, duration, and number of questions
        exam_details = {"name": self.name, "duration": self.duration, "num_questions": self.num_questions}
        return exam_details

    def register_exam(self):
        # open a Google form to register for the exam
        registration_link = "https://docs.google.com/forms/d/e/1FAIpQLSecoumNX6KoipeNC1M4dAdotaYftGHGHZ4HcRQV63E1cufCkw/viewform?vc=0&c=0&w=1&flr=0"
        webbrowser.open(registration_link)

    def take_exam(self):
        # open a Google form to take the exam
        exam_link = "https://docs.google.com/forms/d/e/1FAIpQLSfdKz1FmYP1Sg8-fgz7ZP36Q0mYcCugAT2tJ0Ft_JLJlxQUvA/viewform"
        webbrowser.open(exam_link)

# Example usage
# Authenticate the user
if login("admin", "password"):
    # Create a new exam
    exam = Exam("Math Test", 60, 20)
    exam_details = exam.create_exam()
    print(exam_details)

    # Register for the exam
    exam.register_exam()

    # Take the exam
    exam.take_exam()

else:
    print("Invalid username or password.")

class Lesson:
    def __init__(self, t, m, l):
        self.lessonTitle = t
        self.durationMinutes = m
        self.requiresLab = l

    def outputLessonDetails(self):
        print("Lesson Title: ", self.lessonTitle)
        print("Duration: ", self.durationMinutes)
        print("Requires Lab: ", self.requiresLab)

class Assessment:
    def __init__(self, a, b):
        self.assessmentTitle = a
        self.maxMarks = b

    def outputAssessmentDetails(self):
        print("Assessment Title: ", self.assessmentTitle)
        print("Max Marks: ", self.maxMarks)

class Course:
    def __init__(self, q, w, e):
        self.courseTitle = q
        self.maxStudents = w
        self.numberOfLessons = e
        self.courseLessons = []
        self.courseAssessments = Assessment

    def addLesson(self):
        
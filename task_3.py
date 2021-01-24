# this project is solved using OOP features such as Class, Object, Methods, Inheritance ect.


class School:
    def __init__(self):
        self.subject_teacher = {"English Grammar": "John Smith", "Mathematics": "Lara Gilbert",
                                "Physics": "Johanna Kabir",
                                "Chemistry": "Danniel Robertson", "Biology": " Larry Cooper"}
        self.routine = []

    def class_routine(self):
        print(" 1. English Grammar\n", "2. Mathematics\n", "3. Physics\n", "4. Chemistry\n", "5. Biology\n")
        row = 4

        # taking input for routine
        for x in range(0, row):
            self.routine.append([int(j) for j in input().split()])
        # print(self.routine)

        # making routine
        for x in self.routine:
            # print("in for")
            if x[2] == 0:
                x[2] = "English Grammar"
            elif x[2] == 1:
                x[2] = "Mathematics"
            elif x[2] == 2:
                x[2] = "Physics"
            elif x[2] == 3:
                x[2] = "Chemistry"
            elif x[2] == 4:
                x[2] = "Biology"
        # print(self.routine)

    def show_routine(self):
        print("Class routine for this week")
        print("----------------------------")
        for v in self.routine:
            print(v[0], v[1], v[2], "\n")

    def list_courses_with_teachers_name(self):
        print("List of Courses with Teachers Name")
        print("-----------------------------------")
        for k, v in self.subject_teacher.items():
            print(k + ",", v)


# Inheritance
class Result(School):
    def input_taking(self):
        print("Chose your option:")
        print("---------------------")
        print(" A. Class Routine\n", "B. Show Routine\n", "C. List_Courses_with_Teachers_Name")
        n = input().upper()
        if n == 'A':
            self.class_routine()
        elif n == 'B':
            self.show_routine()
        else:
            self.list_courses_with_teachers_name()  # This function is "inherited" from class School.
        return


obj2 = Result()
while True:
    print("\n")
    obj2.input_taking()
    print("\nDo you want to check other options? (y/n)")
    t = input()
    if t is 'n':
        break

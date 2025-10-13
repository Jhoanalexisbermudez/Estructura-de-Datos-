class Student:
    def __init__(self, first_name, last_name, id_number, semester, program):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.semester = semester
        self.program = program
        self.next = None

    def __str__(self):
        return f"[{self.id_number}] {self.first_name} {self.last_name} - Sem: {self.semester} - Programa: {self.program}"


class ClassCourse:
    def __init__(self, course_id, name, credits):
        if credits <= 0:
            raise ValueError("Los créditos deben ser un número positivo.")
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.head = None

    def add_student(self, first_name, last_name, id_number, semester, program):
        if self.find_student(id_number) is not None:
            print(f"El alumno con ID {id_number} ya está inscrito.")
            return
        new_student = Student(first_name, last_name, id_number, semester, program)
        new_student.next = self.head
        self.head = new_student
        print(f"Alumno inscrito correctamente: {first_name} {last_name}")

    def find_student(self, id_number):
        current = self.head
        while current is not None:
            if current.id_number == id_number:
                return current
            current = current.next
        return None

    def update_student(self, id_number, new_program, new_semester):
        student = self.find_student(id_number)
        if student is None:
            print(f"No se encontró ningún alumno con el ID {id_number}.")
            return
        student.program = new_program
        student.semester = new_semester
        print(f"Datos del alumno {id_number} actualizados correctamente.")

    def remove_student(self, id_number):
        if self.head is None:
            print("No hay alumnos en esta clase.")
            return
        if self.head.id_number == id_number:
            self.head = self.head.next
            print(f"Alumno con ID {id_number} eliminado (era el primero).")
            return
        current = self.head
        while current.next is not None and current.next.id_number != id_number:
            current = current.next
        if current.next is None:
            print(f"No se encontró ningún alumno con el ID {id_number}.")
        else:
            current.next = current.next.next
            print(f"Alumno con ID {id_number} eliminado correctamente.")

    def list_students(self):
        if self.head is None:
            print(f"No hay alumnos inscritos en la clase '{self.name}'.")
            return
        print(f"Alumnos inscritos en '{self.name}':")
        current = self.head
        while current is not None:
            print("  -", current)
            current = current.next

    def clear_students(self):
        self.head = None
        print(f"Todos los alumnos han sido eliminados de la clase '{self.name}'.")


class UniversitySystem:
    def __init__(self):
        self.classes = []

    def create_class(self, course_id, name, credits):
        for c in self.classes:
            if c.course_id == course_id:
                print(f"Ya existe una clase con el ID {course_id}.")
                return
        new_class = ClassCourse(course_id, name, credits)
        self.classes.append(new_class)
        print(f"Clase '{name}' creada con éxito.")

    def find_class(self, course_id):
        for c in self.classes:
            if c.course_id == course_id:
                return c
        return None

    def update_class(self, course_id, new_name=None, new_credits=None):
        course = self.find_class(course_id)
        if not course:
            print(f"Clase con ID {course_id} no encontrada.")
            return
        if new_name:
            course.name = new_name
        if new_credits is not None and new_credits > 0:
            course.credits = new_credits
        print(f"Clase {course_id} actualizada correctamente.")

    def delete_class(self, course_id):
        for i, c in enumerate(self.classes):
            if c.course_id == course_id:
                c.clear_students()
                del self.classes[i]
                print(f"Clase con ID {course_id} eliminada correctamente.")
                return
        print(f"Clase con ID {course_id} no encontrada.")

    def list_classes(self):
        if not self.classes:
            print("No hay clases registradas en el sistema.")
            return
        print("Clases registradas:")
        for c in self.classes:
            print(f" - [{c.course_id}] {c.name} ({c.credits} créditos)")


def main():
    system = UniversitySystem()
    system.create_class(101, "Programación I", 3)
    system.create_class(102, "Estructuras de Datos", 4)
    system.list_classes()
    course = system.find_class(101)
    course.add_student("Laura", "García", 1001, 2, "Ingeniería de Software")
    course.add_student("Carlos", "Pérez", 1002, 1, "Ingeniería de Sistemas")
    course.add_student("Ana", "Torres", 1003, 3, "Informática")
    course.list_students()
    s = course.find_student(1002)
    print("Alumno encontrado:", s if s else "No encontrado")
    course.update_student(1003, "Ingeniería de Software", 4)
    course.remove_student(1001)
    course.list_students()
    system.delete_class(101)
    system.list_classes()


if __name__ == "__main__":
    main()

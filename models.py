class Person:
    def __init__(self, id: str, name: str, email: str):
        self._id = id
        self._name = name
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def __repr__(self):
        return f"<Person {self._id}: {self._name}>"

class Student(Person):
    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

class Professor(Person):
    def __init__(self, id: str, name: str, email: str, department: str):
        super().__init__(id, name, email)
        self._department = department

    @property
    def department(self):
        return self._department

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "email": self.email, "department": self.department}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

class Course:
    def __init__(self, code: str, title: str, credits: int, professor: str):
        self._code = code
        self._title = title
        self._credits = credits
        self._professor = professor

    @property
    def code(self):
        return self._code

    @property
    def title(self):
        return self._title

    @property
    def credits(self):
        return self._credits

    @property
    def professor(self):
        return self._professor

    def to_dict(self) -> dict:
        return {"code": self.code, "title": self.title, "credits": self.credits, "professor": self.professor}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
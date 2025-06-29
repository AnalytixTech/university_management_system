class Person:
    def __init__(self, id: str, name: str, email: str):
        self._id    = id
        self._name  = name
        self._email = email

    @property
    def id(self):    return self._id
    @property
    def name(self):  return self._name
    @property
    def email(self): return self._email

class Student(Person):
    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["id"], d["name"], d["email"])

class Professor(Person):
    def __init__(self, id: str, name: str, email: str, department: str):
        super().__init__(id, name, email)
        self._department = department

    @property
    def department(self): return self._department

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "email": self.email, "department": self.department}

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["id"], d["name"], d["email"], d["department"])

class Course:
    def __init__(self, code: str, title: str, credits: int, professor: str,
                 enrolled=None, applications=None):
        self._code         = code
        self._title        = title
        self._credits      = credits
        self._professor    = professor
        self._enrolled     = enrolled or []
        self._applications = applications or []

    @property
    def code(self):      return self._code
    @property
    def title(self):     return self._title
    @property
    def credits(self):   return self._credits
    @property
    def professor(self): return self._professor
    @property
    def enrolled(self):  return self._enrolled
    @property
    def applications(self): return self._applications

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "title": self.title,
            "credits": self.credits,
            "professor": self.professor,
            "enrolled": self.enrolled,
            "applications": self.applications,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["code"], d["title"], d["credits"], d["professor"],
                   enrolled=d.get("enrolled", []), applications=d.get("applications", []))
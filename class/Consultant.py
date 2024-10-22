class Consultant:
    def __init__(self, id_consultant=None, name=None, employee_id=None, level_consultant=None):
        self.id_consultant = id_consultant  # id mặc định của hệ thống
        self.name = name
        self.employee_id = employee_id    # id facebook của nhân viên đó
        self.level_consultant = level_consultant

    # Getter method cho id_consultant
    def get_id_consultant(self):
        return self.id_consultant

    # Setter method cho id_consultant
    def set_id_consultant(self, id_consultant):
        self.id_consultant = id_consultant

    # Getter method cho name
    def get_name(self):
        return self.name

    # Setter method cho name
    def set_name(self, name):
        self.name = name

    # Getter method cho employee_id
    def get_employee_id(self):
        return self.employee_id

    # Setter method cho employee_id
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    # Getter method cho level_consultant
    def get_level_consultant(self):
        return self.level_consultant

    # Setter method cho level_consultant
    def set_level_consultant(self, level_consultant):
        self.level_consultant = level_consultant

#######


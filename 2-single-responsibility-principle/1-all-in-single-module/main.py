class Employee:
    xml_filename = "emp.xml"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, factor):
        return self.salary * factor

    def save_as_xml(self):
        with open(self.xml_filename, "w") as file:
            file.write(f"<xml><name>{self.name}</name><salary>{self.salary}</salary></xml>")

e = Employee("Vera", 2000)
e.save_as_xml()

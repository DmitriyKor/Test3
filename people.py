class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender=gender
        self.age=age
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender[0].lower()})"

    def __eq__(self, other):
            return (self.first_name==other.first_name) and (self.last_name==other.last_name)

    #def __ne__(self, other):
    #    return not self.__eq__(other)

    def __hash__(self):
        return hash(self.last_name)

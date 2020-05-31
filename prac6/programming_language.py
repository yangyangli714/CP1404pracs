"""CP1404/CP5632 Practical - Programming Language"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        if self.reflection:
            return self.name

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name,
                                                                             self.typing, self.reflection, self.year)
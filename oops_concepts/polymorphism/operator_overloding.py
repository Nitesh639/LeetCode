class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        total_student = Student(m1, m2)
        return total_student

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(23, 56)
s2 = Student(23, 65)
s3 = Student(23, 65)
s4 = s1 + s2 + s3
print(s4.m2)
print(s1 < s2)
print(s2)
# when we use "+" operator than behind the seen here other functions or methods are working
# For ex: "+" = __add__(self, other) like this
# when we add int than there is int is the object where we have method __add__, __sub__ and other
# method for help us mathematical operations.

# But in our case, the object don't have these things, so we need to create those stuffs.
# As we created here __add__ method for + operator.

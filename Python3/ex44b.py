class Parent(object):

    def override(self):
        print("PARENT override()")

class CHild(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = CHild()

dad.override()
son.override()

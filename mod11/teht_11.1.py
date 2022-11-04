class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi: {self.name}")

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.editor}")

class Book(Publication):
    def __init__(self):
        self.author = ""
        self.pageCount = 0
    #todo make this work

pub1 = Magazine("Aku Ankka", "Aki Hyyppä")
pub1.print_info()

pub2 = Book("Hytti nro 6", "Rosa Likson", 220)
pub2.print_info()

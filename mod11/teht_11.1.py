class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Publication: {self.name}")

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    def print_info(self):
        super().print_info()
        print(f"Chief editor: {self.editor}")

class Book(Publication):
    def __init__(self, name, author, pageCount):
        self.author = author
        self.pageCount = pageCount
        super().__init__(name)
    def print_info(self):
        super().print_info()
        print(f"Author: {self.author}, Page count: {self.pageCount}")

pub1 = Magazine("Donald Duck", "Aki Hyyppä")
pub1.print_info()

pub2 = Book("Compartment No. 6", "Rosa Liksom", 192)
pub2.print_info()


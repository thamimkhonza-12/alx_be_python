# -----------------------------
# Library System using OOP
# Inheritance + Composition
# -----------------------------

class LibraryItem:
    """Base class for all items in the library."""

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"


class Book(LibraryItem):
    """Book inherits from LibraryItem."""

    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def __str__(self):
        return f"Book: '{self.title}' by {self.author} ({self.year})"


class Member:
    """Represents a library member. Uses composition to hold borrowed items."""

    def __init__(self, name):
        self.name = name
        self.borrowed_items = []  # composition: list of LibraryItem objects

    def borrow(self, item):
        self.borrowed_items.append(item)

    def __str__(self):
        if not self.borrowed_items:
            return f"{self.name} has borrowed no items."

        borrowed_list = ", ".join(str(item) for item in self.borrowed_items)
        return f"{self.name} has borrowed: {borrowed_list}"


class LibrarySystem:
    """Main system that manages members and items."""

    def __init__(self):
        self.members = []
        self.items = []

    def add_member(self, member):
        self.members.append(member)

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        members_str = ", ".join(member.name for member in self.members) or "No members"
        items_str = ", ".join(item.title for item in self.items) or "No items"
        return f"Library Members: {members_str}\nLibrary Items: {items_str}"


# -----------------------------
# Example usage (optional)
# -----------------------------
if __name__ == "__main__":
    book1 = Book("1984", 1949, "George Orwell")
    member1 = Member("Thami")

    library = LibrarySystem()
    library.add_item(book1)
    library.add_member(member1)

    member1.borrow(book1)

    print(book1)       # calls __str__
    print(member1)     # calls __str__
    print(library)     # calls __str__

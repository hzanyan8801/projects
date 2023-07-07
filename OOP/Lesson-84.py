class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print("This item is not in the backpack.")
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)


my_backpack = Backpack()
print(my_backpack.items)

my_backpack.add_multiple_items(["party", "school", "college"])
print(my_backpack.items)

my_backpack.add_item("Water bottle")
my_backpack.add_item("Sleeping bag")
my_backpack.add_item("Candy")

print("Not sorted")
print(my_backpack.items)

print("Sorted")
my_backpack.show_items(True)
print(my_backpack.items)

my_backpack.add_item("Water bottle")
print(my_backpack.items)

my_backpack.add_item("Sleeping bag")
print(my_backpack.items)

has_water = my_backpack.has_item("Water bottle")
print(has_water)

my_backpack.remove_item("Water bottle")
print(my_backpack.items)

my_backpack.remove_item("Sleeping bag")
print(my_backpack.items)

my_backpack.remove_item("phone")
print(my_backpack.items)
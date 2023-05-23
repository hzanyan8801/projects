class Backpack:

    def __init__(self) -> None:
        self._items = []

    @property
    def items(self):
        print("calling the getter...")
        return self._items
    
    @items.setter
    def items(self, new_items):
        print("calling the setter...")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")

my_backpack = Backpack()

print(my_backpack.items)
my_backpack.items = ["Water Bottle", "Sleeping Bag"]
print(my_backpack.items)
import random

class Grocery_Items:
    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.bought = False
    def buy_items(self):
        self.bought = True
    def __str__(self):
        if self.bought:
            status = 'Purchased'
        else:
            status = 'Pending'
        return f'{self.name}, {self.quantity} - {self.category} [{status}]'

class Items_List:
    def __init__(self):
        self.items = []
    def add_item(self, name, quantity, category):
        self.items.append(Grocery_Items(name, quantity, category))
    def remove_item(self, name, quantity, category):
        self.items.remove(Grocery_Items(name, quantity, category))
    def mark_item(self, name):
        for item in self.items:
            if item.name.upper() == name.upper():
                item.buy_items()
                print(f"{item.name} marked as 'Purchased'")
                return
        print("Item not found")
    def view_items(self):
        if len(self.items) == 0:
            print("No items found")
            return
        print("\nGrocery Items:")
        for item in self.items:
            print(f" - {item}")

    def view_items_by_category(self):
        if len(self.items) == 0:
            print("No items found")
            return
        categories = set(item.category for item in self.items)
        print("\nAvailable Categories:")
        for category in categories:
            print(f" - {category}")
        selected = input("Enter a category to view items: ")
        found = False
        print(f"\nItems in category '{selected}':")
        for item in self.items:
            if item.category.upper() == selected.upper():
                print(f" - {item}")
                found = True
        if not found:
            print("No items found in this category")

    def export_to_file(self, filename):
        if len(self.items) == 0:
            print("No items to export.")
            return

        if filename.strip() == "":
            random_number = random.randint(1000, 9999)
            filename = "grocery_list_" + str(random_number) + ".txt"

        try:
            f = open(filename, 'w')
            for item in self.items:
                line = item.name + "," + item.quantity + "," + item.category
                if item.bought:
                    line = line + ",Bought\n"
                else:
                    line = line + ",Pending\n"
                f.write(line)
            f.close()
            print("Grocery list saved to '" + filename + "'.")
        except:
            print("Something went wrong")
def main():
    grocery_list = Items_List()
    while True:
        print("\nGrocery List Organizer")
        print("1. Add Items")
        print("2. Mark Items as 'Purchased'")
        print("3. View Items")
        print("4. View Items by Category")
        print("5. Export List")
        print("6. Exit")

        user_choice = input("Choose an option: ")

        if user_choice == "1":
            name = input("Enter item name: ")
            quantity = input("Enter quantity: ")

            categories_list = ["Fruits", "Vegetables", "Dairy", "Grains", "Beverages"]
            print("\nPlease choose a category from the list below:")
            for index in range(len(categories_list)):
                number = index + 1
                category_name = categories_list[index]
                print(str(number) + ". " + category_name)

            other_option_number = len(categories_list) + 1
            print(str(other_option_number) + ". Other (If your category is not listed above)")

            while True:
                selected = input("Choose an option by number: ")
                if selected == "1":
                    category = "Fruits"
                    break
                elif selected == "2":
                    category = "Vegetables"
                    break
                elif selected == "3":
                    category = "Dairy"
                    break
                elif selected == "4":
                    category = "Grains"
                    break
                elif selected == "5":
                    category = "Beverages"
                    break
                elif selected == "6":
                    category = input("Enter your category name: ")
                    break
                else:
                    print("Invalid choice. Please try again.")

            grocery_list.add_item(name, quantity, category)
            print("'" + name + "' added to the list.")
            print("\nWhat would you like to do next?")
            print("1. Return to Main Menu")
            print("2. Exit")
            next_choice = input("Choose an option: ")
            if next_choice == "2":
                print("Thank you for using Grocery List Organizer. Have a nice day!")
                break

        elif user_choice == "2":
            name = input("Enter item name to mark as purchased: ")
            grocery_list.mark_item(name)
            print("\nWhat would you like to do next?")
            print("1. Return to Main Menu")
            print("2. Exit")
            next_choice = input("Choose an option: ")
            if next_choice == "2":
                print("Thank you for using Grocery List Organizer. Have a nice day!")
                break

        elif user_choice == "3":
            grocery_list.view_items()
            print("\nWhat would you like to do next?")
            print("1. Return to Main Menu")
            print("2. Exit")
            next_choice = input("Choose an option: ")
            if next_choice == "2":
                print("Thank you for using Grocery List Organizer. Have a nice day!")
                break

        elif user_choice == "4":
            grocery_list.view_items_by_category()
            print("\nWhat would you like to do next?")
            print("1. Return to Main Menu")
            print("2. Exit")
            next_choice = input("Choose an option: ")
            if next_choice == "2":
                print("Thank you for using Grocery List Organizer. Have a nice day!")
                break

        elif user_choice == "5":
            filename = input("Enter filename to export (or press 'Enter' for random name): ")
            grocery_list.export_to_file(filename)
            print("\nWhat would you like to do next?")
            print("1. Return to Main Menu")
            print("2. Exit")
            next_choice = input("Choose an option: ")
            if next_choice == "2":
                print("Thank you for using Grocery List Organizer. Have a nice day!")
                break

        elif user_choice == "6":
            print("Thank you for using Grocery List Organizer. Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()






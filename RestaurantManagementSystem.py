# import matplotlib.pyplot as plt

class RestaurantManagementSystem:
    
    def __init__(self):
        self.gujarati_menu = {
            "Chapati      ": 10,
            "Milk         ": 30,
            "sev tameta   ": 70,
            "undhyu       ": 150,
        }

        self.punjabi_menu = {
            "nan          ": 10,
            "batter-nan   ": 20,
            "kaju kari    ": 150,
            "kaju masala  ": 120,
        }

        self.chinese_menu= {
            "manchurain     ": 110,
            "noodles        ": 80,
            "chines bhel    ": 100,
            "manchurain rice": 50,
        }

        self.ordered_gujarati_items = {}
        self.ordered_punjabi_items = {}
        self.ordered_chinese_items = {}



    def display_menu(self):
        print("|--------------------------------------------------------------|")
        print("|                  Select a cuisine:                           |")
        print("|                                                              |")
        print("|              1. Gujarati Cuisine                             |")
        print("|              2. Punjabi Cuisine                              |")
        print("|              3. Chinese Cuisine                              |")
        print("|              4. Payment                                      |")
        print("|--------------------------------------------------------------|")
        print("                                                                ")

    def handle_input(self):
        print(" ")
        choice = input("Enter your choice: ")
        print(" ")

        if choice == "1":
            self.display_cuisine_menus(self.gujarati_menu, self.ordered_gujarati_items)
        elif choice == "2":
            self.display_cuisine_menus(self.punjabi_menu, self.ordered_punjabi_items)
        elif choice == "3":
            self.display_cuisine_menus(self.chinese_menu, self.ordered_chinese_items)
        elif choice == "4":
            print(" ")
            self.view_and_process_payment()
            print(" ")
            self.display_menu()
            self.handle_input()  # After payment, display the menu again
        else:
            print("Invalid choice. Please try again.")
            self.handle_input()


    def display_cuisine_menus(self, menu, ordered_items):
        print("-----------------------------------------")
        print("                 Menu                    ")
        print("-----------------------------------------")
        for index, (item, price) in enumerate(menu.items(), start=1):
            print(f"{index}. {item} - rs :{price}")
        print(f"{len(menu) + 1}. Main menu")

        while True:
            print("")
            choice = input("Enter your choice: ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(menu):
                    item = list(menu.keys())[choice - 1]
                    quantity = int(input("Enter the quantity of item: "))
                    total_cost = quantity * price
                    if item in ordered_items:
                        ordered_items[item] += quantity
                    else:
                        ordered_items[item] = quantity
                    total_cost = quantity * menu[item]
                    print(f"Total cost for {item}: rs :{total_cost}")
                elif choice == len(menu) + 1:
                    self.display_menu()
                    self.handle_input()
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid choice. Please try again.")

    def view_total_bill(self):
        total_bill = self.calculate_total_bill()
        print("*******************  total bill  ***********************")
        print(" ")
        print("               Total Bill: rs :", total_bill)
        print("********************************************************")

    def calculate_total_bill(self):
        total_bill = 0

        # Calculate total bill for Gujarati cuisine
        total_bill += sum(self.ordered_gujarati_items[item] * self.gujarati_menu[item] for item in self.ordered_gujarati_items)

        # Calculate total bill for Punjabi cuisine
        total_bill += sum(self.ordered_punjabi_items[item] * self.punjabi_menu[item] for item in self.ordered_punjabi_items)

        # Calculate total bill for Chinese cuisine
        total_bill += sum(self.ordered_chinese_items[item] * self.chinese_menu[item] for item in self.ordered_chinese_items)

        return total_bill

    def process_payment(self):
        print("Payment processed successfully.")

        # Reset ordered items after payment
        self.ordered_gujarati_items.clear()
        self.ordered_punjabi_items.clear()
        self.ordered_chinese_items.clear()

    def view_and_process_payment(self):
        self.view_total_bill()
        self.process_payment()

    def main(self):
        self.display_menu()
        self.handle_input()

# Instantiate the class and run the restaurant management system
if __name__ == "__main__":
    rms = RestaurantManagementSystem()
    rms.main()

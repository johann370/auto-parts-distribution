
from Order import Order
#currently, Database is the Inventory Manager; an Order Processor database needs to be made
from Database import Database
from UI import UI
from Payment import Payment

class OrderProcessor:
    def __init__(self, ui: UI, orders: Database) -> None:
        self.orders = orders
        self.ui = ui


    def processOrder(self):
      
        account_number = 0
        account_number += 1
        self.transaction(account_number)
        self.addOrder()


    def add_order(self, account_number):
        order_info = self.ui.get_order_info()
        new_order = Order([order_info], account_number)



    def transaction(self, account_number):
        payment = Payment()
        payment.processPayment(account_number)

    def delete_order(self):
        id_to_delete = self.ui.get_order_to_delete()

        self.inventory.delete_order(id_to_delete)

   
    def display_orders(self):
        print(self.inventory)


   
   def setOrderStatus(self):
            
        parts_received = input("Enter the part received: ")
        full_parts_list = full_parts_list + parts_received

   def addOrderToDatabase(self):
        pass
        #add order by calling self.orders

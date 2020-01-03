from pizzapi import *

customer = Customer("Sunset", "Superman", "sunsetsuperman@gmail.com", "8005550123")
address = Address("1158 Yo Mama St", "Columbus", "OH", "43210")
store = address.closest_store()

order = Order(store, customer, address)
order.add_item('P12IPAZA')
order.add_item('20BDCOKE')

card = PaymentObject("1234567890123456", "1234", "777", "43210")

def order_pizza(order, card):
    order.place(card)

command = input("Your usual order, sir?")

if command == "yes":
    print("Of course, sir.")
    order_pizza(order)
else:
    print("Of course, sir. Shutting down.")
    exit()

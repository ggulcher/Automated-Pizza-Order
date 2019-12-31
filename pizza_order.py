from pizzapi import *

def pizza_order(pizzapi):
    customer = Customer("Sunset", "Superman", "sunsetsuperman@gmail.com", "8005550123")
    address = Address("1158 Yo Mama St", "Columbus", "OH", "43210")

    store = address.closest_store()

    menu = store.get_menu()

    order = Order(store, customer, address)
    order.add_item('P12IPAZA')
    order.add_item('20BDCOKE')

    card = PaymentObject("1234567890123456", "1234", "777", "43210")

    order.place(card)

command = input("Your usual order, sir?")

if command == "yes":
    print("Of course, sir.")
    pizza_order(pizzapi)
else:
    print("Of course, sir. Shutting down.")
    exit()

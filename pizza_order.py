from pizzapi import *

customer = Customer("Sunset", "Superman", "sunsetsuperman@gmail.com", "8005550123")
address = Address("1158 Yo Mama St", "Columbus", "OH", "43210")

store = address.closest_store()

menu = store.get_menu()

order = Order(store, customer, address)
order.add_item('P12IPAZA')
order.add_item('20BDCOKE')

card = PaymentObject("1234567890123456", "1234", "777", "43210")

# To place order
# order.place(card)

# To test
# order.pay_with(card) 

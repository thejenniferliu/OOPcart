class Cart():
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_cart(self):
        item = input('What would you like to add? ')
        self.cart.append(item)
        pass
    
    def remove_cart(self):
        item = input('What would you like to remove?')
        try:
            self.cart.remove(item)
            print('item removed')
        except:
            print('the item you typed is not here ya dingus')
       
    def show_cart(self):
        print(self.cart) 
        pass
    
    def quit_cart(self):
        print(f"ok you bought {self.cart} byeeeee")

def run():
    my_cart = Cart('Jennifer')
    while True:
        ask = input('what do you wanna do? add/remove/show/quit')
        if ask == 'add':
            my_cart.add_cart()
        if ask == 'remove':
            my_cart.remove_cart()
        if ask == 'show':
            my_cart.show_cart()
        elif ask == 'quit':
            my_cart.quit_cart()
            break
run()



class Animal(): 
    energy = 5
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
       
    def play(self, play):
        self.energy -= play
        print(self.energy)
    def sleep(self, sleep):
        self.energy += sleep
        print(self.energy)
        
animal1=Animal('Buddy', 10)

animal2=Animal('Latte', 15)


animal2.sleep(45)
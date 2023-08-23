class Chest:
    def __init__(self, password: str):
        self.password = password
        self.close = False
        self.content = self.read_txt_file()

    def read_txt_file(self):
        return str(open("chest.txt", "r")).rstrip().split()

    def is_close(self):
        return self.close

    def items(self):
        if self.is_close():
            print("The Chest is Closed")
        else: 
            print(self.content) 

    def open_chest(self, password: str):
        if password == self.password:
            self.close = True
            print(f"Chest is Now Open")
        else:
            print(f"You Entered The Wrong Password")

    def add_item(self, item: str):
        if self.is_close():
            print("The Chest is Closed")
        else: 
            self.content.append(item)
            str_ = str(i +" " for i in self.content)
            open("chest.txt", "w").write(str_)

    def remove_item(self, item: str):
        if self.is_close:
            print("The Chest is Closed")
        else:
            if item in self.content:
                self.content.remove(item)
                str_ = str(i +" " for i in self.content)
                open("chest.txt", "w").write(str_)
                print(f"{item} successfully removed from chest")
            else:
                print(f"{item} Does not Exist in Your Chest")

    def close_chest(self):
        self.close = False

chest = Chest('m2007m')

chest.items()
chest.open_chest('m2006m')
chest.open_chest('m2007m')
chest.add_item("tnt")
chest.add_item("skull")
chest.remove_item("tnt")
chest.remove_item("bomb")
chest.close_chest()
chest.add_item("axe")
chest.open_chest('m2007m')
chest.add_item("axe")
chest.close_chest()


# ! CODE DOES NOT WORK !
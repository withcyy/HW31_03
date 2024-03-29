class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user_contacts(self, username, contacts):
        if username not in self.data:
            self.data[username] = contacts
        else:
            self.data[username].extend(contacts)

info_system = InformationSystem()
info_system.add_user_contacts("Bob", ["kilo@gmail.com", "+133141542"])
info_system.add_user_contacts("Mark", ["gram@gmail.com", "+134515412"])
print(info_system.data)
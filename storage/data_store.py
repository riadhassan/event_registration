class TicketHandler:
    tickets = {}

    def get(self, key):
        return self.tickets[key]

    def get_all(self):
        return self.tickets

    def add(self, ticket: "Ticket"):
        if not len(self.tickets) == 0:
            new_key = max(self.tickets.keys()) + 1
        else:
            new_key = 1
        self.tickets[new_key] = ticket
        self.tickets[new_key].ticket_id = new_key


class Ticket:
    ticket_id: int = None
    name: str
    email: str
    phone: str

    handler = TicketHandler()

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        if not self.ticket_id:
            self.handler.add(self)
        else:
            raise NotImplementedError("Update is not implemented")
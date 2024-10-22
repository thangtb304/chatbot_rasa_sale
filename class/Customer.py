class Customer:
    def __init__(self, id_customer=None, name=None, phone=None, address=None):
        self.id_customer = id_customer # id fbook của khách hàng
        self.name = name
        self.phone = phone
        self.address = address

    # Getter method cho id_customer
    def get_id_customer(self):
        return self.id_customer

    # Setter method cho id_customer
    def set_id_customer(self, id_customer):
        self.id_customer = id_customer

    # Getter method cho name
    def get_name(self):
        return self.name

    # Setter method cho name
    def set_name(self, name):
        self.name = name

    # Getter method cho phone
    def get_phone(self):
        return self.phone

    # Setter method cho phone
    def set_phone(self, phone):
        self.phone = phone

    # Getter method cho address
    def get_address(self):
        return self.address

    # Setter method cho address
    def set_address(self, address):
        self.address = address



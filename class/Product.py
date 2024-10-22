class Product:
    def __init__(self, id_product=None, name_product=None, price=None, features=None,
                 usage_instructions=None, promotions=None, warranty=None):
        self.id_product = id_product
        self.name_product = name_product
        self.price = price
        self.features = features
        self.usage_instructions = usage_instructions
        self.promotions = promotions
        self.warranty = warranty

    # Getter và setter cho id_product
    def get_id_product(self):
        return self.id_product

    def set_id_product(self, id_product):
        self.id_product = id_product

    # Getter và setter cho name_product
    def get_name_product(self):
        return self.name_product

    def set_name_product(self, name_product):
        self.name_product = name_product

    # Getter và setter cho price
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    # Getter và setter cho key_features (Key Features and Functions)
    def get_features(self):
        return self.features

    def set_features(self, features):
        self.features = features

    # Getter và setter cho usage_instructions (Usage Instructions)
    def get_usage_instructions(self):
        return self.usage_instructions

    def set_usage_instructions(self, usage_instructions):
        self.usage_instructions = usage_instructions

    # Getter và setter cho promotions (Promotions)
    def get_promotions(self):
        return self.promotions

    def set_promotions(self, promotions):
        self.promotions = promotions

    # Getter và setter cho warranty (Warranty and After-Sales Service)
    def get_warranty(self):
        return self.warranty

    def set_warranty(self, warranty):
        self.warranty = warranty

# # Ví dụ sử dụng class Product
# product = Product()
# product.set_name_product("Smartphone XYZ")
# product.set_price(699.99)
# product.set_features("High-resolution camera, 5G support, long battery life")
# product.set_usage_instructions("Charge fully before first use, avoid extreme temperatures")
# product.set_promotions("10% off for the first 100 customers")
# product.set_warranty("2-year warranty, 24/7 customer support")

# print(product.get_name_product())            # Output: Smartphone XYZ
# print(product.get_price())                   # Output: 699.99
# print(product.get_features())                # Output: High-resolution camera, 5G support, long battery life
# print(product.get_usage_instructions())      # Output: Charge fully before first use, avoid extreme temperatures
# print(product.get_promotions())              # Output: 10% off for the first 100 customers
# print(product.get_warranty())                # Output: 2-year warranty, 24/7 customer support



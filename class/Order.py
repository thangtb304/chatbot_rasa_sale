class Order:
    def __init__(self, id_order=None, employee_id=None, time_order=None, ship=None):
        self.id_order = id_order
        self.employee_id = employee_id  # id facebook của nhân viên đó
        self.products = []  # Danh sách chứa các sản phẩm
        self.price = [] # Danh sách chứa giá các sản phẩm
        self.quantities = []  # Danh sách chứa số lượng của từng sản phẩm
        self.time_order = time_order
        self.total_amount = 0.0
        self.ship=ship

    def add_product(self, product, quantity):
        self.products.append(product)  # Thêm sản phẩm vào danh sách
        self.quantities.append(quantity)  # Thêm số lượng tương ứng
        self.total_amount += product.get_price() * quantity  # Cập nhật total_amount
        
    # Getter cho id_order
    def get_id_order(self):
        return self.id_order

    # Getter cho idfb_consultant
    def get_employee_id(self):
        return self.employee_id

    # Getter cho products
    def get_products(self):
        return self.products

    # Getter cho time_order
    def get_time_order(self):
        return self.time_order
    
    # Setter và getter cho ship
    def set_ship(self,ship):
        self.ship=ship

    def get_ship(self):
        return self.ship

    # Getter cho total_amount
    def get_total_amount(self):
        self.total_amount += self.ship
        return self.total_amount


########################

# # Ví dụ sử dụng class Order với nhiều sản phẩm
# # Đầu tiên, định nghĩa một số sản phẩm
# product1 = Product(id_product=1, name_product="Smartphone XYZ", price=699.99)
# product2 = Product(id_product=2, name_product="Laptop ABC", price=1299.99)

# # Tạo một đơn hàng
# order = Order(id_order=1, idfb_consultant="fb_12345", time_order="2024-10-20")

# # Thêm sản phẩm vào đơn hàng
# order.add_product(product1, quantity=2)  # Thêm 2 sản phẩm Smartphone XYZ
# order.add_product(product2, quantity=1)  # Thêm 1 sản phẩm Laptop ABC

# # In thông tin đơn hàng
# print(f"Order ID: {order.get_id_order()}")                     # Output: Order ID: 1
# print(f"Consultant ID: {order.get_idfb_consultant()}")        # Output: Consultant ID: fb_12345
# print(f"Time Order: {order.get_time_order()}")                 # Output: Time Order: 2024-10-20

# # In ra thông tin sản phẩm trong đơn hàng
# for i, product in enumerate(order.get_products()):
#     print(f"Product: {product.get_name_product()}, Price: {product.get_price()}, Quantity: {order.quantities[i]}, Amount: {product.get_price() * order.quantities[i]}")

# print(f"Total Amount: {order.get_total_amount()}")             # Output: Total Amount: 2699.97

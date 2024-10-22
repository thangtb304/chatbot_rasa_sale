class FanPage:
    def __init__(self, name=None, id_page=None, content_type=None, products=None, followers_count=0, engagement_rate=0.0):
        """
        Khởi tạo một đối tượng FanPage.
        
        :param name: Tên của fanpage.
        :param id_page: ID của fanpage.
        :param content_type: Loại nội dung mà fanpage chia sẻ (ví dụ: bán hàng, tư vấn, thông tin).
        :param products: Danh sách các sản phẩm mà fanpage đang bán.
        :param followers_count: Số lượng người theo dõi fanpage.
        :param engagement_rate: Tỉ lệ tương tác (engagement rate) của fanpage.
        """
        self.name = name
        self.id_page = id_page
        self.content_type = content_type
        self.products = products if products is not None else []
        self.followers_count = followers_count
        self.engagement_rate = engagement_rate

    # Getter và setter cho name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter và setter cho id_page
    def get_id_page(self):
        return self.id_page

    def set_id_page(self, id_page):
        self.id_page = id_page

    # Getter và setter cho content_type
    def get_content_type(self):
        return self.content_type

    def set_content_type(self, content_type):
        self.content_type = content_type

    # Getter và setter cho products
    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    # Getter và setter cho followers_count
    def get_followers_count(self):
        return self.followers_count

    def set_followers_count(self, followers_count):
        self.followers_count = followers_count

    # Getter và setter cho engagement_rate
    def get_engagement_rate(self):
        return self.engagement_rate

    def set_engagement_rate(self, engagement_rate):
        self.engagement_rate = engagement_rate

    # Phương thức thêm sản phẩm
    def add_product(self, product):
        self.products.append(product)

    # Phương thức tính toán hiệu quả
    def calculate_effectiveness(self):
        """
        Tính toán hiệu quả của fanpage dựa trên số lượng người theo dõi và tỷ lệ tương tác.
        Trả về một giá trị số.
        """
        if self.followers_count == 0:
            return 0
        return (self.engagement_rate * self.followers_count) / 100  # Công thức đơn giản để tính hiệu quả

# # Ví dụ sử dụng class FanPage
# fanpage = FanPage(name="Tech Support", id_page="fb_tech_support", content_type="Bán hàng và tư vấn", followers_count=1500, engagement_rate=5.5)

# # Thêm sản phẩm vào fanpage
# fanpage.add_product("Laptop XYZ")
# fanpage.add_product("Smartphone ABC")

# # In thông tin fanpage
# print(f"FanPage Name: {fanpage.get_name()}")
# print(f"ID Page: {fanpage.get_id_page()}")
# print(f"Content Type: {fanpage.get_content_type()}")
# print(f"Products: {fanpage.get_products()}")
# print(f"Followers Count: {fanpage.get_followers_count()}")
# print(f"Engagement Rate: {fanpage.get_engagement_rate()}%")
# print(f"Effectiveness: {fanpage.calculate_effectiveness()}")

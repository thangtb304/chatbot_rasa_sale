from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
import json

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import logging
logger = logging.getLogger(__name__)

from search.search import search_info_product

# Form để xử lý thông tin đơn hàng
class ValidateOrderForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_order_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "customer_name",
            "customer_address",
            "customer_phone",
            "product_name",
            "product_quantity"
        ]

    # Validate các slot khi người dùng nhập thông tin
    async def extract_customer_name(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        customer_name = tracker.get_slot("customer_name")
        if customer_name:
            return {"customer_name": customer_name}
        else:
            dispatcher.utter_message(text="Vui lòng nhập tên của bạn.")
            return {"customer_name": None}

    async def extract_customer_address(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        customer_address = tracker.get_slot("customer_address")
        if customer_address:
            return {"customer_address": customer_address}
        else:
            dispatcher.utter_message(text="Vui lòng nhập địa chỉ của bạn.")
            return {"customer_address": None}

    async def extract_customer_phone(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        customer_phone = tracker.get_slot("customer_phone")
        if customer_phone:
            return {"customer_phone": customer_phone}
        else:
            dispatcher.utter_message(text="Vui lòng nhập số điện thoại của bạn.")
            return {"customer_phone": None}

    # Submit order
    async def submit(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict]:
        # Lấy giá trị từ các slot
        customer_name = tracker.get_slot("customer_name")
        customer_address = tracker.get_slot("customer_address")
        customer_phone = tracker.get_slot("customer_phone")
        product_name = tracker.get_slot("product_name")
        product_quantity = int(tracker.get_slot("product_quantity"))

        # Giá trị cố định
        ship_fee = 30000  # VND
        product_price = 100000  # Giá tạm placeholder, bạn có thể thay bằng giá từ JSON
        total_price = ship_fee + (product_price * product_quantity)

        # Đặt các giá trị vào slot
        dispatcher.utter_message(text=f"Cảm ơn {customer_name}! Đơn hàng của bạn đã được gửi đi.")
        return [
            SlotSet("ship_fee", ship_fee),
            SlotSet("total_price", total_price),
        ]

# Action để hiển thị thông tin đơn hàng
class ActionSubmitOrder(Action):
    def name(self) -> Text:
        return "action_submit_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        customer_name = tracker.get_slot("customer_name")
        customer_address = tracker.get_slot("customer_address")
        customer_phone = tracker.get_slot("customer_phone")
        product_name = tracker.get_slot("product_name")
        product_quantity = tracker.get_slot("product_quantity")
        ship_fee = tracker.get_slot("ship_fee")
        total_price = tracker.get_slot("total_price")

        dispatcher.utter_message(text=f"Thông tin đơn hàng của bạn:\n"
                                      f"Tên: {customer_name}\n"
                                      f"Địa chỉ: {customer_address}\n"
                                      f"Số điện thoại: {customer_phone}\n"
                                      f"Sản phẩm: {product_name}\n"
                                      f"Số lượng: {product_quantity}\n"
                                      f"Phí vận chuyển: {ship_fee} VND\n"
                                      f"Tổng giá trị đơn hàng: {total_price} VND\n"
                                      "Cảm ơn bạn đã đặt hàng!")
        return []


###
class ActionStoreProductName(Action):
    def name(self) -> Text:
        return "action_store_product_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product_name")
        logger.debug(f"Product Name Slot: {product_name}")  # Log giá trị slot
        return [SlotSet("product_name", product_name)]
    

### detail sản phẩm
# Action để cung cấp thông tin giá sản phẩm và lưu vào slot
class ActionProvideProductPrice(Action):
    def name(self) -> str:
        return "action_provide_product_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        #Lấy tên sản phẩm từ tracker
        product_name = tracker.get_slot("product_name")
        product_price = search_info_product(product_name)['price']  # Giá trị giá sản phẩm

        #Gửi thông báo cho người dùng
        dispatcher.utter_message(text=f"Giá của phẩm là {product_price}")

        #Đặt giá trị cho slot product_price
        return [SlotSet("product_price", product_price)]
    
# Action để cung cấp thông tin tính năng sản phẩm
class ActionProvideProductFeatures(Action):
    def name(self) -> str:
        return "action_provide_product_features"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Lấy tên sản phẩm từ tracker
        product_name = tracker.get_slot("product_name")       
        product_features = search_info_product(product_name)['features']  # Giá trị giá sản phẩm
        # Gửi phản hồi về thông tin sản phẩm
        if product_name:
            product_features = search_info_product(product_name)['features']
            dispatcher.utter_message(text=f"Sản phẩm {product_name} có các tính năng: {product_features}.")
            # Lưu giá vào slot featuré
            return [SlotSet("product_features", product_features)]
        else:
            dispatcher.utter_message(text=f"Xin lỗi, chúng tôi không tìm thấy thông tin cho sản phẩm {product_name}.")
            return []
        

############ KHAB123
# # lựa chọn action A nếu KH ở Hn và action B nếu KH ở tphcm
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionHandleLocation(Action):
#     def name(self) -> Text:
#         return "action_handle_location"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Lấy location từ entity hoặc slot đã lưu
#         location = next(tracker.get_latest_entity_values("location"), None)
        
#         if location and location.lower() in ["tphcm", "hcm", "ho chi minh"]:
#             # Nếu là TPHCM
#             dispatcher.utter_message(text="Bạn đang ở TPHCM.")
#             return [{"next_action": "action_A"}]
#         else:
#             # Nếu không phải TPHCM
#             dispatcher.utter_message(text=f"Bạn đang ở {location}.")
#             return [{"next_action": "action_B"}]

# class ActionA(Action):
#     def name(self) -> Text:
#         return "action_A"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Logic xử lý cho TPHCM
#         dispatcher.utter_message(text="Thực hiện action A cho TPHCM")
#         return []

# class ActionB(Action):
#     def name(self) -> Text:
#         return "action_B"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Logic xử lý cho các tỉnh khác
#         dispatcher.utter_message(text="Thực hiện action B cho tỉnh khác")
#         return []
    

# # # stories.yml
# # stories:
# # - story: handle location TPHCM
# #   steps:
# #   - intent: ask_location
# #   - slot_was_set:
# #       - location: "tphcm"
# #   - action: action_handle_location 
# #   - action: action_A

# # - story: handle location other
# #   steps:
# #   - intent: ask_location  
# #   - slot_was_set:
# #       - location: "other"
# #   - action: action_handle_location
# #   - action: action_B
# ######## /KHAB123

# #   KHAB124   
# #from rasa import Action
# from rasa.events import SlotSet

# class ActionHandleLocation(Action):
#     def name(self) -> str:
#         return "action_handle_location"

#     def run(self, dispatcher, tracker, domain):
#         customer_location = tracker.get_slot("customer_location")

#         if customer_location == "Hà Nội":
#             # Thực hiện hành động A
#             return [SlotSet("some_slot", "value_for_A"), ActionA()]
        
#         elif customer_location == "TPHCM":
#             # Thực hiện hành động B
#             return [SlotSet("some_slot", "value_for_B"), ActionB()]
        
#         else:
#             dispatcher.utter_message(text="Xin lỗi, vị trí không được xác định.")
#             return []

# #   KHAB124     
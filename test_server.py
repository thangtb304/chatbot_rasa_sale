import requests

# URL của Rasa server đang chạy với REST webhook
url = "http://localhost:5005/webhooks/rest/webhook"

# Payload là tin nhắn từ người dùng gửi đến bot
payload = {
    "sender": "user214",  # Tên của người gửi
    #"message": "hi"  # Tin nhắn từ người dùng
    #"message": "Bạn có Đồng hồ thông minh ABC không"  # Tin nhắn từ người dùng
    #"message": "Giá của cái này là bao nhiêu"
    "message": "Đồng hồ này có tính năng gì nổi bật?"
    #"message": "Có chương trình khuyến mãi nào không" ##
    
}

# Gửi request POST tới Rasa server với payload JSON
response = requests.post(url, json=payload)

# Kiểm tra phản hồi từ server
if response.status_code == 200:
    print(response.json())  # In ra phản hồi của bot
else:
    print(f"Error: {response.status_code}, {response.text}")

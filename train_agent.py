import rasa
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def train_agent():
    # Đường dẫn tới các file cần thiết
    training_files = 'data/'  # Thư mục chứa nlu.yml, stories.yml, domain.yml
    config_file = 'config.yml'
    #model_path = 'models/agent'  # Thư mục để lưu mô hình sau khi train
    model_path = 'models'  # Thư mục để lưu mô hình sau khi train

    # Huấn luyện agent
    rasa.train(
        domain=os.path.join(training_files, 'domain.yml'),  # Chỉ định rõ file domain
        config=config_file,
        training_files=[os.path.join(training_files, 'nlu.yml'), os.path.join(training_files, 'stories.yml')],
        output=model_path
    )

if __name__ == "__main__":
    train_agent()


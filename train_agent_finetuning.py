import rasa
import os
from typing import Text, Optional

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def finetune_agent(
    base_model_path: Text,
    new_training_files: Text,
    output_path: Text,
    config_file: Optional[Text] = 'config.yml'
):
    """
    Fine-tune một model RASA có sẵn với dữ liệu mới
    
    Args:
        base_model_path: Đường dẫn tới model gốc muốn fine-tune
        new_training_files: Thư mục chứa dữ liệu training mới
        output_path: Thư mục lưu model sau khi fine-tune
        config_file: File config.yml (optional)
    """
    # Kiểm tra model gốc tồn tại
    if not os.path.exists(base_model_path):
        raise FileNotFoundError(f"Không tìm thấy model gốc tại: {base_model_path}")

    # Đường dẫn tới các file training mới
    new_domain = os.path.join(new_training_files, 'domain.yml')
    new_nlu = os.path.join(new_training_files, 'nlu.yml')
    new_stories = os.path.join(new_training_files, 'stories.yml')

    # Kiểm tra các file training mới
    for file_path in [new_domain, new_nlu, new_stories]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Không tìm thấy file training: {file_path}")

    try:
        # Fine-tune model với dữ liệu mới
        rasa.train(
            domain=new_domain,
            config=config_file,
            training_files=[new_nlu, new_stories],
            output=output_path,
            force_training=True,  # Bắt buộc training lại
            model_to_finetune=base_model_path  # Chỉ định model gốc để fine-tune
        )
        print(f"Fine-tuning hoàn tất. Model mới được lưu tại: {output_path}")
        
    except Exception as e:
        print(f"Lỗi trong quá trình fine-tune: {str(e)}")
        raise

def train_base_agent():
    """Train model gốc ban đầu"""
    training_files = 'data/'
    config_file = 'config.yml'
    model_path = 'models'

    rasa.train(
        domain=os.path.join(training_files, 'domain.yml'),
        config=config_file,
        training_files=[
            os.path.join(training_files, 'nlu.yml'),
            os.path.join(training_files, 'stories.yml')
        ],
        output=model_path
    )
    return os.path.join(model_path, max(os.listdir(model_path)))  # Trả về đường dẫn của model mới nhất

if __name__ == "__main__":
    # 1. Train model gốc
    base_model = train_base_agent()
    print(f"Đã train xong model gốc: {base_model}")

    # 2. Fine-tune với dữ liệu mới
    # Giả sử bạn có thư mục data2/, data3/, ... chứa dữ liệu mới
    new_data_folders = ['data2', 'data3', 'data4', 'data5', 'data6']
    
    current_model = base_model
    for i, data_folder in enumerate(new_data_folders, 1):
        output_path = f'models/model_finetuned_{i}'
        try:
            finetune_agent(
                base_model_path=current_model,
                new_training_files=data_folder,
                output_path=output_path
            )
            # Cập nhật model hiện tại để fine-tune tiếp
            current_model = os.path.join(output_path, max(os.listdir(output_path)))
            print(f"Hoàn thành fine-tune với {data_folder}")
        except Exception as e:
            print(f"Lỗi khi fine-tune với {data_folder}: {str(e)}")
            break
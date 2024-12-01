import pandas as pd
import requests
from io import StringIO
import create
import read
import update
import delete
from datetime import datetime, timedelta
import os

# API URLs và đường dẫn file
ROW_DATA_API = 'https://andyanh.id.vn/index.php/s/p7XMy828G8NKiZp/download'
UPDATED_FILE_PATH = 'C:/Users/admin/Nextcloud4/andyanh/Data-Project-Student-Manager/Update Data/Updated_Data.csv'

def fetch_csv_from_api(api_url):
    """
    Tải dữ liệu từ API và lưu cache
    """
    cache_file = 'row_data_cache.csv'
    cache_timeout = timedelta(hours=24)
    
    if os.path.exists(cache_file):
        modified_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if datetime.now() - modified_time < cache_timeout:
            print(f"Đang tải dữ liệu từ cache {cache_file}...")
            return pd.read_csv(cache_file)
    
    print(f"Đang tải dữ liệu từ API {api_url}...")
    response = requests.get(api_url)
    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(cache_file, index=False)
        return df
    else:
        raise Exception(f"Không thể tải dữ liệu: {response.status_code}")

def load_data():
    """
    Tải dữ liệu ban đầu
    """
    try:
        df = fetch_csv_from_api(ROW_DATA_API)
        print("Đã tải dữ liệu thành công từ API")
        return df
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu từ API: {e}")
        print("Không thể tải dữ liệu. Vui lòng kiểm tra kết nối internet và thử lại.")
        exit()

def show_menu():
    """
    Hiển thị menu chức năng
    """
    print("\n=== QUẢN LÝ THÔNG TIN THÍ SINH ===")
    print("1. Thêm thí sinh mới")
    print("2. Xem thông tin thí sinh") 
    print("3. Cập nhật thông tin thí sinh")
    print("4. Xóa thông tin thí sinh")
    print("5. Lưu và thoát")

def List_manager():
    """
    Hàm chính quản lý luồng chương trình
    """
    df = load_data()
    
    while True:
        show_menu()
        choice = input("\nChọn chức năng (1-5): ")
        
        if choice == '1':
            df = create.create_student(df)
        elif choice == '2':
            read.read_student(df)
        elif choice == '3':
            df = update.update_student(df)
        elif choice == '4':
            df = delete.delete_student(df)
        elif choice == '5':
            df.to_csv(UPDATED_FILE_PATH, index=False)
            print("Đã lưu thay đổi và thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    List_manager()

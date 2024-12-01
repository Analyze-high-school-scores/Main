import pandas as pd
from pathlib import Path

def convert_cache_to_csv(cache_file, csv_file):
    """
    Chuyển đổi file cache sang file CSV
    
    Args:
        cache_file (str): Đường dẫn đến file cache
        csv_file (str): Đường dẫn đến file CSV đầu ra
    """
    try:
        # Đọc file cache dưới dạng DataFrame
        df = pd.read_pickle(cache_file)
        
        # Lưu DataFrame thành file CSV
        df.to_csv(csv_file, index=False, encoding='utf-8')
        
        print(f"Đã chuyển đổi thành công file {cache_file} sang {csv_file}")
        
    except Exception as e:
        print(f"Lỗi khi chuyển đổi file: {str(e)}")

if __name__ == "__main__":
    # Đường dẫn file
    cache_file = "data.cache"
    csv_file = "data.csv"
    
    # Kiểm tra file cache có tồn tại không
    if not Path(cache_file).exists():
        print(f"Không tìm thấy file {cache_file}")
    else:
        convert_cache_to_csv(cache_file, csv_file)

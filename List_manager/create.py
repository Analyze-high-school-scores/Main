import pandas as pd

def create_student(df):
    num_students = int(input("Bạn muốn nhập bao nhiêu thí sinh?: "))
    
    for i in range(num_students):
        print(f"\nNhập thông tin cho thí sinh thứ {i+1}:")
        sbd = int(input("Nhập SBD: "))
        year = int(input("Năm: "))
        
        # Kiểm tra xem SBD đã tồn tại trong năm đó chưa
        if not df[(df['SBD'] == sbd) & (df['Year'] == year)].empty:
            print(f"Lỗi: SBD {sbd} đã tồn tại trong năm {year}!")
            continue
            
        new_student_data = {
            'SBD': sbd,
            'Toan': float(input("Điểm Toán (hoặc để trống): ") or 'NaN'),
            'Van': float(input("Điểm Văn (hoặc để trống): ") or 'NaN'), 
            'Ly': float(input("Điểm Lý (hoặc để trống): ") or 'NaN'),
            'Sinh': float(input("Điểm Sinh (hoặc để trống): ") or 'NaN'),
            'Ngoai ngu': float(input("Điểm Ngoại Ngữ (hoặc để trống): ") or 'NaN'),
            'Year': year,
            'Hoa': float(input("Điểm Hóa (hoặc để trống): ") or 'NaN'),
            'Lich su': float(input("Điểm Lịch Sử (hoặc để trống): ") or 'NaN'),
            'Dia ly': float(input("Điểm Địa Lý (hoặc để trống): ") or 'NaN'),
            'GDCD': float(input("Điểm GDCD (hoặc để trống): ") or 'NaN'),
            'MaTinh': int(input("Mã Tỉnh: "))
        }
        filtered_student_data = {k: v for k, v in new_student_data.items() if pd.notnull(v)}
        new_student_df = pd.DataFrame([filtered_student_data])
        df = pd.concat([df, new_student_df], ignore_index=True)
        print(f"Đã thêm thí sinh thứ {i+1}.")
    
    print(f"\nĐã thêm thành công {num_students} thí sinh.")
    return df

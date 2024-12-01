import pandas as pd

def update_student(df):
    sbd = int(input("Nhập SBD của thí sinh cần cập nhật: "))
    year = int(input("Nhập năm thi: "))
    
    # Kiểm tra xem SBD có tồn tại không
    if sbd not in df['SBD'].values:
        print("Không tìm thấy thí sinh với SBD này.")
        return df
        
    # Kiểm tra xem thí sinh đã có điểm thi năm đó chưa
    student_mask = (df['SBD'] == sbd) & (df['Year'] == year)
    if student_mask.any():
        print("Thí sinh này đã có điểm thi năm", year)
        return df
    
    # Kiểm tra năm thi có hợp lệ không    
    if year not in df['Year'].values:
        print("Không tìm thấy thí sinh thi năm", year)
        return df
            
    # Nhập thông tin cần cập nhật
    column = input("Nhập tên cột cần cập nhật (Toan, Van, Ly, ...): ")
    if column not in df.columns:
        print("Tên cột không hợp lệ")
        return df
        
    new_value = input("Nhập giá trị mới (hoặc để trống): ")
    try:
        new_value = float(new_value) if new_value else 'NaN'
    except ValueError:
        print("Giá trị không hợp lệ")
        return df
        
    # Cập nhật thông tin
    df.loc[df['SBD'] == sbd, 'Year'] = year
    df.loc[df['SBD'] == sbd, column] = new_value
    print("Đã cập nhật thông tin thí sinh.")
    
    return df

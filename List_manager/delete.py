def delete_student(df):
    num_students = int(input("Bạn muốn xóa bao nhiêu thí sinh?: "))
    
    for i in range(num_students):
        print(f"\nNhập thông tin cho thí sinh thứ {i+1} cần xóa:")
        sbd = int(input("Nhập SBD: "))
        year = int(input("Năm thi: "))
        
        if not df[(df['SBD'] == sbd) & (df['Year'] == year)].empty:
            df = df[~((df['SBD'] == sbd) & (df['Year'] == year))]
            print(f"Đã xóa thí sinh có SBD {sbd} năm {year}.")
        else:
            print(f"Không tìm thấy thí sinh có SBD {sbd} trong năm {year}.")
    
    print(f"\nĐã hoàn tất xóa {num_students} thí sinh.")
    return df

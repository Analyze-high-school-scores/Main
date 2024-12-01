def read_student(df):
    sbd = int(input("Nhập SBD của thí sinh cần xem: "))
    student = df[df['SBD'] == sbd]
    if student.empty:
        print("Không tìm thấy thí sinh với SBD này.")
    else:
        print(student)

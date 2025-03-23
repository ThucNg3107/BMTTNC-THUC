from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
    
while (1==1):
        print("\nChương trình quản lý sinh viên")
        print("***************MENU***************")
        print("**  1.Thêm sinh viên  **")
        print("**  2.Cập nhật thông tin sinh viên bởi ID  **")
        print("**  3.Xoá sinh viên bởi ID  **")
        print("**  4.Tìm kiếm sinh viên theo tên  **")
        print("**  5.Sắp xếp sinh viên theo điểm trung bình  **")
        print("**  6.Sắp xếp sinh viên theo tên chuyên ngành  **")
        print("**  7.Hiển thị danh sách sinh viên  **")
        print("**  0.Thoát  **")
        print("**********************************")
        
        key = int(input("Nhập tuỳ chọn: "))
        
        if key == 1:
            print("\n1.Thêm sinh viên")
            qlsv.nhapSV()
            print("\nThêm sinh viên thành công!")
        
        elif key == 2:
            if qlsv.soluongSinhVien() > 0:
                print("\n2.Cập nhật thông tin sinh viên")
                ID = int(input("Nhập ID sinh viên cần cập nhật: "))
                qlsv.updateSinhVien(ID)
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 3:
            if qlsv.soluongSinhVien() > 0:
                print("\n3.Xoá sinh viên")
                ID = int(input("Nhập ID sinh viên cần xoá: "))
                if qlsv.deleteByID(ID):
                    print(f"\nSinh viên có ID = {ID} đã bị xoá.")
                else:
                    print(f"\nSinh viên có ID = {ID} không tồn tại.")
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 4:
            if qlsv.soluongSinhVien() > 0:
                print("\n4.Tìm kiếm sinh viên theo tên")
                name = input("Nhập tên sinh viên cần tìm: ")
                searchResult = qlsv.findByName(name)
                if searchResult:
                    qlsv.ShowSV(searchResult)
                else:
                    print("Không tìm thấy sinh viên với tên này.")
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 5:
            if qlsv.soluongSinhVien() > 0:
                print("\n5.Sắp xếp sinh viên theo điểm trung bình")
                qlsv.sortByDiemTB()
                qlsv.ShowSV(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 6:
            if qlsv.soluongSinhVien() > 0:
                print("\n6.Sắp xếp sinh viên theo tên")
                qlsv.sortByName()
                qlsv.ShowSV(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 7:
            if qlsv.soluongSinhVien() > 0:
                print("\n7.Hiển thị danh sách sinh viên")
                qlsv.ShowSV(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 0:
            print("\nThoát chương trình.")
            break
        
        else:
            print("\nKhông có chức năng này!")    
            print("\nVui lòng chọn lại!")
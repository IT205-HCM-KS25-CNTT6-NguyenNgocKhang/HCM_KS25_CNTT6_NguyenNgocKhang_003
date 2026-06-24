class CourseRegistration:
    def __init__(self, id, student_name, course_name, tuition_fee, discount, extra_fee):
        self.id = id
        self.student_name = student_name
        self.course_name = course_name
        self.tuition_fee = tuition_fee
        self.discount = discount
        self.extra_fee = extra_fee
        self.total_fee = 0
        self.fee_type = ""

    def calculate_total_fee(self):
        self.total_fee = self.tuition_fee - self.discount + self.extra_fee
        if self.total_fee < 0:
            self.total_fee = 0

    def classify_fee(self):
        if self.total_fee >= 15000000:
            self.fee_type = "Rất cao"
        elif self.total_fee >= 7000000:
            self.fee_type = "Cao"
        elif self.total_fee >= 3000000:
            self.fee_type = "Trung bình"
        else:
            self.fee_type = "Thấp"
        
class CourseRegistrationManager:
    def __init__(self):
        self.registrations : list[CourseRegistration] = [] 

    def add_registration(self):
        while True:
            add_id = input("Nhập mã đăng ký: ").strip().upper()
            if not add_id:
                print("Mã đăng ký không được trống!")
                continue
            for res in self.registrations:
                if add_id == res.id:
                    print("Mã đăng ký đã tồn tại!")
                    break
            else:
                break

        while True:
            add_student_name = input("Nhập họ tên học viên: ").strip().title()
            if not add_student_name:
                print("Họ tên học viên không được bỏ trống!")
                continue
            break

        while True:
            add_course_name = input("Nhập tên khóa học: ").strip().title()
            if not add_course_name:
                print("Tên khóa học không được bỏ trống!")
                continue
            break

        while True:
            add_tuition_fee = input("Nhập học phí gốc: ")
            if not add_tuition_fee:
                print("Học phí gốc không được bỏ trống!")
                continue
            try:
                add_tuition_fee = float(add_tuition_fee)

                if add_tuition_fee < 0:
                    print("Học phí gốc không được âm!")
                    continue

                break
            except ValueError:
                print("Học phí gốc không hợp lệ!")
                continue

        while True:
            add_discount = input("Nhập giảm giá: ")
            if not add_discount:
                print("Giảm giá không được bỏ trống!")
                continue
            try:
                add_discount = float(add_discount)

                if add_discount < 0:
                    print("Giảm giá không được âm!")
                    continue

                if add_discount > add_tuition_fee:
                    print("Giám giá không được lớn hơn học phí gốc!")
                    continue

                break
            except ValueError:
                print("Giảm giá không hợp lệ!")
                continue

        while True:
            add_extra_fee = input("Nhập phụ phí: ")
            if not add_extra_fee:
                print("Phụ phí không được bỏ trống!")
                continue
            try:
                add_extra_fee = float(add_extra_fee)

                if add_extra_fee < 0:
                    print("Phụ phí không được âm!")
                    continue

                break
            except ValueError:
                print("Phụ phí không hợp lệ!")
                continue

        new_registration = CourseRegistration(add_id, add_student_name, add_course_name, add_tuition_fee, add_discount, add_extra_fee)
        new_registration.calculate_total_fee()
        new_registration.classify_fee()

        self.registrations.append(new_registration)
        print("Thêm đăng ký khóa học thành công!")


    def show_all(self):
        if not self.registrations:
            print("Danh sách quản lý khóa học đang rỗng!")
            return
        
        print("---- Danh Sách Đăng Ký Khóa Học ----")
        print(f"{'Mã đăng ký':<10} | {'Họ tên học viên':<20} | {'Tên khóa học':<20} | {'Học phí gốc':<15} | {'Giảm giá':<15} | {'Phụ phí':<15} | {'Tổng học phí':<15} | {'Phân loại học phí':<5}")
        for res in self.registrations:
            print(f"{res.id:<10} | {res.student_name:<20} | {res.course_name:<20} | {res.tuition_fee:<15} | {res.discount:<15} | {res.extra_fee:<15} | {res.total_fee:<15} | {res.fee_type:<5}")

    def update_registration(self):
        while True:
            update_id = input("Nhập mã đăng ký: ").strip().upper()
            if not update_id:
                print("Mã đăng ký không được trống!")
                continue
            for res in self.registrations:
                if update_id == res.id:
                    
                    while True:
                        update_tuition_fee = input("Nhập học phí gốc: ")
                        if not update_tuition_fee:
                            print("Học phí gốc không được bỏ trống!")
                            continue
                        try:
                            update_tuition_fee = float(update_tuition_fee)

                            if update_tuition_fee < 0:
                                print("Học phí gốc không được âm!")
                                continue

                            break
                        except ValueError:
                            print("Học phí gốc không hợp lệ!")
                            continue

                    while True:
                        update_discount = input("Nhập giảm giá: ")
                        if not update_discount:
                            print("Giảm giá không được bỏ trống!")
                            continue
                        try:
                            update_discount = float(update_discount)

                            if update_discount < 0:
                                print("Giảm giá không được âm!")
                                continue

                            if update_discount > update_tuition_fee:
                                print("Giám giá không được lớn hơn học phí gốc!")
                                continue

                            break
                        except ValueError:
                            print("Giảm giá không hợp lệ!")
                            continue

                    while True:
                        update_extra_fee = input("Nhập phụ phí: ")
                        if not update_extra_fee:
                            print("Phụ phí không được bỏ trống!")
                            continue
                        try:
                            update_extra_fee = float(update_extra_fee)

                            if update_extra_fee < 0:
                                print("Phụ phí không được âm!")
                                continue

                            break
                        except ValueError:
                            print("Phụ phí không hợp lệ!")
                            continue

                    
                    res.tuition_fee = update_tuition_fee
                    res.discount = update_discount
                    res.extra_fee = update_extra_fee
                    res.calculate_total_fee()
                    res.classify_fee()

                    print("Cập nhật học phí thành công!")
                    return
            else:
                print("Không tìm thấy đăng ký khóa học cần cập nhật!")
                break
    
    def delete_registration(self):
        while True:
            delete_id = input("Nhập mã đăng ký: ").strip().upper()
            if not delete_id:
                print("Mã đăng ký không được trống!")
                continue
            for res in self.registrations:
                if delete_id == res.id:
                    accept = input("Bạn có chắc muốn xóa đăng ký khóa học này không (Y/N): ").upper()

                    match accept:
                        case "Y":
                            self.registrations.remove(res)
                            print("Xóa đăng ký khóa học thành công!")
                            return
                        case "N":
                            print("Đã hủy thao tác xóa!")
                            return
                        case _:
                            print("Lựa chọn không hợp lệ!")
                            return

                    break
            else:
                print("Không tìm thấy khóa học cần xóa!")
                break

    def search_registration(self):
        while True:
            search_value = input("Nhập họ tên học viên hoặc tên khóa học cần tìm: ").strip().lower()
            if not search_value:
                print("Họ tên học viên hoặc tên khóa học không được bỏ trống!")
                continue
            break

        found_list = []
        for res in self.registrations:
            if ( search_value in res.student_name.lower() ) or ( search_value in res.course_name.lower() ):
                found_list.append(res)
        
        if not found_list:
            print("Không tìm thấy đăng ký khóa học phù hợp!")
            return
        else:
            print("---- Danh Sách Khóa Học Cần Tìm ----")
            print(f"{'Mã đăng ký':<10} | {'Họ tên học viên':<20} | {'Tên khóa học':<20} | {'Học phí gốc':<15} | {'Giảm giá':<15} | {'Phụ phí':<15} | {'Tổng học phí':<15} | {'Phân loại học phí':<5}")
            for res in found_list:
                print(f"{res.id:<10} | {res.student_name:<20} | {res.course_name:<20} | {res.tuition_fee:<15} | {res.discount:<15} | {res.extra_fee:<15} | {res.total_fee:<15} | {res.fee_type:<5}")

def menu():
    print(""" 
============= MENU ================
1. Hiển thị khóa học
2. Thêm đăng ký khóa học mới
3. Cập nhật học phí
4. Xóa đăng ký khóa học
5. Tìm kiếm đăng ký
6. Thoát
===================================
     """)
    
def main():
    course_registration_manager = CourseRegistrationManager()
    course_registration_manager.registrations = [
        CourseRegistration("RE01", "Nguyễn Văn A", "Lập Trình Python", 3000000, 500000, 200000),
        CourseRegistration("RE02", "Nguyễn Văn B", "JavaStript", 2500000, 200000, 200000),
    ]
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                course_registration_manager.show_all()
            case "2":
                course_registration_manager.add_registration()
            case "3":
                course_registration_manager.update_registration()
            case "4":
                course_registration_manager.delete_registration()
            case "5":
                course_registration_manager.search_registration()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý khóa học!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
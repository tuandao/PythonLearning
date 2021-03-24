import functools as FT

#####################################################################
## Dữ liệu mẫu
#####################################################################
'''
Danh sách môn học
mỗi môn: một tuple: (tên môn, điểm, hệ số)
'''
courses_tuple = [('Toán', 8.5, 2),
                 ('Văn', 6.5, 2),
                 ('Ngoại ngữ', 9.5, 2),
                 ('Lý', 8.0, 1),
                 ('Hóa', 9.5, 1),
                 ('Sinh', 6.0, 1)]
'''
Danh sách môn học
mỗi môn: một dict: {'name': xxx, 'grade':xxx, 'coef':xxx}
'''
courses_dict = [
    {'name': 'Toán', 'grade': 8.5, 'coef': 2},
    {'name': 'Văn', 'grade': 6.5, 'coef': 2},
    {'name': 'Ngoại ngữ', 'grade': 9.5, 'coef': 2},
    {'name': 'Lý', 'grade': 8.0, 'coef': 1},
    {'name': 'Hóa', 'grade': 9.5, 'coef': 1},
    {'name': 'Sinh', 'grade': 6.0, 'coef': 1},
]

'''
Bảng ánh xạ: Tiếng việt - Tiếng Anh 
'''
vn2en_map = {
    'Toán': 'Mathematics',
    'Văn': 'Literature',
    'Ngoại ngữ': 'Foreign Language',
    'Lý': 'Physics',
    'Hóa': 'Chemistry',
    'Sinh': 'Biology',
}


#####################################################################
## Các hàm chức năng
#####################################################################
'''
en2vn_map:
Chuyển từ điển VN-to-EN sang từ điển EN-2-VN

Ví dụ:
vn2en_map:
    {
    'Toán': 'Mathematics', 
    'Văn': 'Literature', 
    'Ngoại ngữ': 'Foreign Language', 
    'Lý': 'Physics', 
    'Hóa': 'Chemistry', 
    'Sinh': 'Biology'
    }
=>
    {
    'Mathematics': 'Toán', 
    'Literature': 'Văn', 
    'Foreign Language': 'Ngoại ngữ',
    'Physics': 'Lý', 
    'Chemistry': 'Hóa',
    'Biology': 'Sinh'
    }
'''

def en2vn_map(vn2en_map: dict):
    inv_map = dict(map(reversed, vn2en_map.items()))
    print(inv_map)

en2vn_map(vn2en_map)


'''
sort_courses_tuple:
sort_course_dict:
    Sắp xếp môn học trong danh sách tăng dần theo điểm
Ví dụ:
[('Toán', 8.5, 2), ('Văn', 6.5, 2), ('Ngoại ngữ', 9.5, 2)]
=>
[('Văn', 6.5, 2), ('Toán', 8.5, 2), ('Ngoại ngữ', 9.5, 2)]
'''
def sort_courses_tuple(courses: list):
    sorted_courses = sorted(courses,key=lambda tup:tup[1])
    print(sorted_courses)

sort_courses_tuple(courses_tuple)


'''
[
    {'name': 'Toán', 'grade': 8.5, 'coef': 2},
    {'name': 'Văn', 'grade': 6.5, 'coef': 2},
    {'name': 'Ngoại ngữ', 'grade': 9.5, 'coef': 2}
]
=>
[
    {'name': 'Văn', 'grade': 6.5, 'coef': 2},
    {'name': 'Toán', 'grade': 8.5, 'coef': 2},
    {'name': 'Ngoại ngữ', 'grade': 9.5, 'coef': 2}
]
'''
def sort_courses_dict(courses: dict):
    sorted_dict = sorted(courses, key=lambda dict: dict['grade'])
    print(sorted_dict)

sort_courses_dict(courses_dict)


'''
average_tuple:
average_dict:
    Tính điểm trung bình có hệ số của các môn học trong danh sách
Ví dụ:
[('Toán', 8.5, 2), ('Văn', 6.5, 2), ('Sinh', 9.5, 1)]
=>
(8.5x2 + 6.5x2 + 9.5x1)/5
'''

def average_tuple(courses: list):
    score_map = list(map(lambda x: x[1]*x[2],courses))
    coef_map = list(map(lambda x:x[2],courses))
    print(sum(score_map)/sum(coef_map))

average_tuple(courses_tuple)

def average_dict(courses: list):
    score_map = list(map(lambda x: x['grade']*x['coef'],courses))
    coef_map = list(map(lambda x:x['coef'],courses))
    print(sum(score_map)/sum(coef_map))

average_dict(courses_dict)

'''
course_hscore_tuple:
Tìm và trả về môn học có điểm số lớn nhất; trả về môn đầu tiên nếu có từ hai môn có cùng điểm lớn nhất
[('Toán', 8.5, 2), ('Văn', 6.5, 2), ('Ngoại ngữ', 9.5, 2)]
=>
('Ngoại ngữ', 9.5, 2)
'''
def course_hscore_tuple(courses: list):
    max_rec = max(courses)
    print(max_rec)
course_hscore_tuple(courses_tuple)
#
#
# '''
# [
#     {'name': 'Toán', 'grade': 8.5, 'coef': 2},
#     {'name': 'Văn', 'grade': 6.5, 'coef': 2},
#     {'name': 'Ngoại ngữ', 'grade': 9.5, 'coef': 2}
# ]
# =>
#     {'name': 'Ngoại ngữ', 'grade': 9.5, 'coef': 2}
# '''
# def course_hscore_dict(courses: list):
#     #YOUR CODE HERE
#
#
# '''
# select_courses_tuple:
# select_courses_dict:
# Trả trả về danh sách các môn học có điểm >= 'from_score'
#
# Ví dụ:
# courses: [('Toán', 8.5, 2), ('Văn', 6.5, 2), ('Ngoại ngữ', 9.5, 2)]
# from_score: 7.0
# =>
# [('Toán', 8.5, 2), ('Ngoại ngữ', 9.5, 2)]
# '''
#
# def select_courses_tuple(courses: list, from_score: int=5):
#     #YOUR CODE HERE
#
# def select_courses_dict(courses: list, from_score: int=5):
#     #YOUR CODE HERE
#
# '''
# course_eng:
# Chuyển danh sách môn học có tên Tiếng việt sang Tiếng Anh, sử dụng bảng bộ từ điển trong vn2eng_map
#
# Ví dụ:
# courses:
# [
#     {'name': 'Toán', 'grade': 8.5, 'coef': 2},
#     {'name': 'Văn', 'grade': 6.5, 'coef': 2},
#     {'name': 'Ngoại ngữ', 'grade': 9.5, 'coef': 2}
# ]
# vn2eng_map:
# vn_to_eng = {
#     'Toán': 'Mathematics',
#     'Văn': 'Literature',
#     'Ngoại ngữ': 'Foreign Language',
#     'Lý': 'Physics',
#     'Hóa': 'Chemistry',
#     'Sinh': 'Biology',
# }
# =>
# [
#     {'name': 'Mathematics', 'grade': 8.5, 'coef': 2},
#     {'name': 'Literature', 'grade': 6.5, 'coef': 2},
#     {'name': 'Foreign Language', 'grade': 9.5, 'coef': 2}
# ]
# '''
# def course_eng(courses: list, vn2eng_map):
#     #YOUR CODE HERE
#
#
# '''
# update_course_tuple:
# Cập nhật điểm mới cho môn học trong danh sách.
#
# Ví dụ:
# courses: [('Toán', 8.5, 2), ('Văn', 6.5, 2), ('Ngoại ngữ', 9.5, 2)]
# updated_course: ('Văn', 8.5)
# =>
# [('Toán', 8.5, 2), ('Văn', .5, 2), ('Ngoại ngữ', 9.5, 2)]
#
# '''
# def update_course_tuple(courses: list, updated_course):
#     #YOUR CODE HERE
#
#
# '''
# update_course_dict:
# Cập nhật điểm mới cho môn học trong danh sách.
#
# Ví dụ:
# courses: [
#     {
#     'name': 'Toán',
#     'grade': 8.5,
#     'coef': 2
#     },
#     {
#     'name': 'Văn',
#     'grade': 6.5,
#     'coef': 2
#     },
#     {
#     'name': 'Ngoại ngữ',
#     'grade': 9.5,
#     'coef': 2
#     }
#     ]
# updated_course: ('Văn', 8.5)
# =>
# courses: [
#     {
#     'name': 'Toán',
#     'grade': 8.5,
#     'coef': 2
#     },
#     {
#     'name': 'Văn',
#     'grade': 8.5,
#     'coef': 2
#     },
#     {
#     'name': 'Ngoại ngữ',
#     'grade': 9.5,
#     'coef': 2
#     }
#     ]
#
# '''
# def update_course_dict(courses: list, updated_course):
#     #YOUR CODE HERE

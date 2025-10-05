from guizero import App, Picture, Text, Box
app=App(title='Bao Lao Dong', width=1000, height=940)
box=Box(app,align='top', width='fill')

text=Text(box, text='Lao động sang Đức lái tàu điện, xe buýt\n nhận lương 100 triệu đồng', font='Times new roman', size=37)
text1=Text(box, text='Người lao động Việt Nam sang Đức học nghề lái tàu điện, xe buýt trong 2,5 năm,\n'
                     ' sau đó làm việc tại TP Leipzig với mức lương 3.000-3.500 euro mỗi tháng (92-108\n'
                     ' triệu đồng).Thông tin được TS Fabian Magerl, Tổng giám đốc Phòng Công nghiệp và\n'
                     ' Thương mại Leipzig, chia sẻ tại hội thảo Du học nghề lái tàu điện và xe buýt tổ\n'
                     ' chức chiều 3/10, do chính quyền TP Leipzig, Công ty Vận tải giao thông Leipzig \n'
                     '(LVB) và 4WIN Recruiting phối hợp thực hiện.Theo ông Burkhard Jung, Thị trưởng TP\n'
                     ' Leipzig, thành phố có tỷ lệ người sử dụng phương tiện công cộng cao thứ hai ở Đức\n'
                     ', chỉ sau Berlin. Mỗi năm, LVB phục vụ 167 triệu lượt khách, vận hành 271 tàu điện\n'
                     ' và 166 xe buýt. Do nhu cầu đi lại công cộng, kéo theo nhu cầu lớn về tài xế. Hiện\n'
                     ' LVB có hơn 1.400 tài xế, trong đó 10% đến từ các quốc gia khác.', font='Courier new', align='left', size=14)
hinhanh=Picture(app,image='1_1_.png',width=900,height=500)
app.display()

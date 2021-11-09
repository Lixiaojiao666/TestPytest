import allure

def test_attach_test():
    # 给测试报告中添加文本，这种方法可以用来添加日志
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)
    # 给测试报告中添加网页，
def test_attach_html():
    allure.attach('''<body>这是一段"htmlbody“</body>''',"html测试块",attachment_type=allure.attachment_type.HTML)
    # 给测试报告中添加图片，可以添加报错截图，
def test_attach_photo():
    allure.attach.file("/Users/Administrator/PycharmProjects/TestPytest/123.jpg",name="这是一个图片",attachment_type=allure.attachment_type.JPG)
    # 给测试报告中添加视频，可以添加执行过程，
def test_attach_video():
    allure.attach.file("/Users/Administrator/PycharmProjects/TestPytest/456.mp4",name="这是一个视频",attachment_type=allure.attachment_type.MP4)
# -- coding: utf-8 --   #注意这里不能写成 coding = utf-8，不然会报错，要写成   -- coding: utf-8 --
'''
 2 cnblog的登录测试，分下面几种情况：
 3 (1)用户名、密码正确
 4 (2)用户名正确、密码不正确
 5 (3)用户名正确、密码为空
 6 (4)用户名错误、密码正确
 7 (5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
 8 '''

import unittest
from selenium import webdriver
from time import sleep
import unittest
import sys

#reload(sys)
from imp import reload


#sys.setdefaultencoding('utf-8')
#以上红色部门为设置断言必须导入的四个依赖包


class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('https://demo.qjylw.com/admin/index/login.html')  # cnblog登录页面
        self.dr.find_element_by_id('loginform-username').send_keys(username)
        self.dr.find_element_by_id('loginform-password').send_keys(password)
        self.dr.find_element_by_class_name('col-xs-4').click()

    def test_login_pwd_error(self):
        '''用户名正确、密码正确'''
        self.login('admin', 'qj@admin')  # 正确用户名，错误密码
        sleep(2)
        link = self.dr.find_element_by_id('header-nav-list')
        self.assertTrue('TV播库' in link.text)
        print("找到了元素")  # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
       # self.dr.get_screenshot_as_file("C:\Users\Administrator\Desktop\\login_success.png")  # 截图  将登陆成功的截图保存到桌面

    def test_login_success(self):
        '''用户名正确、密码不正确'''
        self.login('admin', 'qjadmin')  # 正确用户名和密码
        sleep(3)
        error_message = self.dr.find_element_by_id('login-form').text
        #self.assertIn('用户名或密码不正确', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        #self.dr.get_screenshot_as_file("C:\Users\Administrator\Desktop\\login_pwd_error.png")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('admin', '')  # 密码为空
        error_message = self.dr.find_element_by_id('login-form').text
        #self.assertEqual('error_message', '密码不能为空。')  # 用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
        #self.dr.get_screenshot_as_file("C:\Users\Administrator\Desktop\\login_pwd_null.png")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('ad', 'qj@admin')  # 密码正确，用户名错误
        sleep(2)
        error_message = self.dr.find_element_by_id('login-form').text
        #self.assertIn('用户名或密码不正确', error_message)  # 用assertIn(a,b)方法来断言 a in b
        #self.dr.get_screenshot_as_file("C:\Users\Administrator\Desktop\\login_user_error.png")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login("", 'qj@admin')  # 用户名为空，密码正确
        error_message = self.dr.find_element_by_id('login-form').text
        #self.assertEqual(error_message,
                        # '用户名不能为空。')  # 用assertEqual(a,b)方法来断言  a == b         self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_null.jpg")
        #self.dr.get_screenshot_as_file("C:\Users\Administrator\Desktop\\login_user_error.png")

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()


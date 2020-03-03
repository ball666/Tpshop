# 使用unittest搭建登录的接口用例的框架
# 1.导包
import requests,unittest
# 2.定义测试类,继承unittest.TestCase
class TestTpshopLogin(unittest.TestCase):

    # 3.定义setup和teardown
    def setUp(self) -> None:
        # 初始化session
        self.session = requests.Session()
        self.verify_code_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
    def tearDown(self) -> None:
        # 关闭session
        self.session.close()
    # 4.设置登录的测试方法
    """
     获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
     登录：http://localhost/index.php?m=Home&c=User&a=do_login
     我的订单：http://localhost/Home/Order/order_list.html
     data = {"username": "18088888888",
             "password": "123456",
             "verify_code": "8888"})
     """
    def test01_login_success(self):
        # 调用获取验证码接口
        response_verify = self.session.get(self.verify_code_url)
        #打印验证码接口的响应体
        # print(response_verify.headers)
        # 断言验证码响应体中Content-Type的值是否是image/png
        self.assertEqual("image/png",response_verify.headers.get("Content-Type"))
        # 调用登录接口
        response_login = self.session.post(self.login_url,
                                      data={"username": "18088888888",
                                            "password": "123456",
                                            "verify_code": "8888"})
        # 打印登录接口返回的相应数据
        jsonData = response_login.json() # type:dict
        # 断言响应状态码,和响应的json数据中的status的值和msg的值
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(1,jsonData.get("status"))
        self.assertEqual("登陆成功",jsonData.get("msg"))
    def test_login_no_exists(self):
        # 调用获取验证码接口
        response_verify = self.session.get(self.verify_code_url)
        #打印验证码接口的响应体
        print(response_verify.headers)
        # 断言验证码响应体中Content-Type的值是否是image/png
        self.assertEqual("image/png",response_verify.headers.get("Content-Type"))
        # 调用登录接口
        response_login = self.session.post(self.login_url,
                                      data={"username": "18088888866",
                                            "password": "123456",
                                            "verify_code": "8888"})
        # 打印登录接口返回的相应数据
        jsonData = response_login.json() # type:dict
        # 断言响应状态码,和响应的json数据中的status的值和msg的值
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(-1,jsonData.get("status"))
        self.assertIn("账号不存在",jsonData.get("msg"))

    def test_login_password_error(self):
        # 调用获取验证码接口
        response_verify = self.session.get(self.verify_code_url)
        #打印验证码接口的响应体
        print(response_verify.headers)
        # 断言验证码响应体中Content-Type的值是否是image/png
        self.assertEqual("image/png",response_verify.headers.get("Content-Type"))
        # 调用登录接口
        response_login = self.session.post(self.login_url,
                                      data={"username": "18088888888",
                                            "password": "ddddd",
                                            "verify_code": "8888"})
        # 打印登录接口返回的相应数据
        jsonData = response_login.json() # type:dict
        # 断言响应状态码,和响应的json数据中的status的值和msg的值
        self.assertEqual(200,response_login.status_code)
        self.assertEqual(-2,jsonData.get("status"))
        self.assertIn("密码错误",jsonData.get("msg"))
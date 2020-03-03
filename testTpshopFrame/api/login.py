# 定义tpshop登录的接口
class Login():
    def __init__(self):
        self.verify_code_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
    def get_verify_code(self,session):
        return session.get(self.verify_code_url)
        
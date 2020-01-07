# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_add_plan(self):
        driver = self.driver
        driver.maximize_window()
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin5/configure/admission")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div/div/div/div[2]/span", "xpath",
                            "校验进入招生计划管理")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th",
            "xpath", "校验表单“序号”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[2]/span/div/span",
            "xpath", "校验表单“招生计划名称”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[3]/span/div/span",
            "xpath", "校验表单“班型”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[4]/span/div/span",
            "xpath", "校验表单“招生开始时间”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[5]/span/div/span",
            "xpath", "校验表单“招生结束时间”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[6]/span/div/span",
            "xpath", "校验表单“是否付费”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[7]/span/div/span",
            "xpath", "校验表单“当前状态”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[8]/span/div/span",
            "xpath", "校验表单“操作")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/button", "xpath",
                            "校验“新建”")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li/a",
                            "xpath", "校验“分页-上一页”")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li[2]/a",
                            "xpath", "校验“分页第一页”")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li[3]/a",
                            "xpath", "校验“分页-下一页”")
        # 点击新建按钮
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/button").click()
        # 班级类型选择免费版
        driver.find_element_by_xpath("//*[@id=\"classType\"]/div/div").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[7]").click()
        # 是否付费选择否
        driver.find_element_by_xpath("//input[@value='0']").click()
        # 输入招生计划名称
        t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        driver.find_element_by_xpath("//input[@placeholder='请输入有效的招生计划名称']").send_keys(
            "自动化测试" + t1)
        # 输入招生开始时间
        driver.find_element_by_xpath("//*[@id=\"startTime\"]/div/input").click()
        t2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div/input").send_keys(
            t2)
        driver.find_element_by_xpath("//body").click()
        # 输入招生结束时间
        driver.find_element_by_xpath("//*[@id=\"endTime\"]/div/input").click()
        t3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").send_keys(
            t3)
        driver.find_element_by_xpath("//body").click()
        # 选择平均分班
        driver.find_element_by_xpath("//*[@id=\"classRules\"]/div/div").click()
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/ul/li[2]").click()
        # 关联招生主页1
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span").click()
        driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        # 保存
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[8]/div/div/span/button[1]").click()

        def check_save_istrue(driver, t1, t2, t3):
            '''判断新建招生计划三个时间是否存在页面中'''
            pro_status = driver.page_source
            if t1 in pro_status and t2 in pro_status and t3 in pro_status:
                return True
            else:
                return False

        # 断言数据添加是否成功
        assert_equal(check_save_istrue(driver, t1, t2, t3), True, '通用断言：验证添加数据是否成功')

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

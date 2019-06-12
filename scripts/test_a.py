import pytest, allure
class Test_a(object):
    # def setup_class(self):
    #     print(">>>>>>>>>>>>>>setup_class")
    # def teardown_class(self):
    #     print(">>>>>>>>>>>>>>teardown_class")
    #

    @pytest.allure.step("我是test_001第一个测试")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach("描述","这是一个描述-打印测试内容")
        print(">>>>>>>>>>>>>>test_001")
        assert True
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_002(self):
        allure.attach("这是一个描述","试一下")
        print(">>>>>>>>>>>>>>>>>>>>>>test_002")
        assert 1
    @allure.testcase("http://www.baidu.com/test_003")
    def test_003(self):
        print(">>>>>>>>>>>>>>>>test_003")
        assert True
    @allure.issue('http://www.163.com')
    def test_004(self):
        print(">>>>>>>>>>>>test_004>>>>zwf>>>>>>>>>>>>>>zwj")
        assert True


# if __name__ == '__main__':
    # pytest.main("-s allure generate/ report -o report/xml")

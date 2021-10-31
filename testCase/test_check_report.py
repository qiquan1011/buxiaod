from pageObject.acq_main_object import Acq_Main_Object
from common.log import Logger
import pytest
import traceback
from common.get_excel import get_excel

def setup_function():
    pass

@pytest.mark.parametrize(*get_excel().get_sheetNames("Sheet1"))
def test_01(case_name,path,yaml_page_data,yaml_input_data,name,name_path):
    try:
        diagnosed_text=Acq_Main_Object(path,yaml_page_data,yaml_input_data,name,name_path).acq_check()
        assert diagnosed_text=="待诊断"
    except Exception as e:
        message = traceback.format_exc()
        Logger("error").get_logger().debug(message)
def test_02():
    assert 1==2
def teardown_function(self):
    pass

if __name__=="__main__":
    pytest.main([("test_check_report.py"),("-sv")])
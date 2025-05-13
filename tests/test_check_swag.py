from pages.swag_labs import SwagLabs
import time

def test_check_swag(browser):

    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    time.sleep(3)
    assert demo_qa_page.exist_icon()
    time.sleep(3)
    assert demo_qa_page.exist_username()
    time.sleep(3)
    assert demo_qa_page.exist_password()


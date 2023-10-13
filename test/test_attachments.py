import json

import allure
from allure import attachment_type


def test_attachments():
    allure.attach("Text conten", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Text conten</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({'first': 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)

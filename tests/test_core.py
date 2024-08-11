from fh_frankenui.core import *

class TestH:
    def test_single_enum(self):
        assert C(H.h1) == 'uk-h1'
    def test_multiple_enums(self):
        assert C(H.h1, H.h2) == 'uk-h1 uk-h2'
    def test_string_and_enum(self):
        assert C(H.h1, 'abc', H.h2) == 'uk-h1 abc uk-h2'

class TestButton:
    def test_base_attr(self):
        assert C(Button.base) == 'uk-button'
    def test_base_attr_and_enum(self):
        assert C(Button.base, Button.style.primary) == 'uk-button uk-button-primary'

from pytest import raises
from fh_frankenui.foundations import BaseEnum, CoreEnum, C

class TextCOLOR(BaseEnum):
    red = 'red'
    blue = 'blue'
    
class TextSIZE(BaseEnum):
    small = 'small'
    large = 'large'

class TestBaseEnum:
    def test_single_enum(self):
        assert C(TextCOLOR.red) == 'uk-text-red', C(TextCOLOR.red)
    def test_multiple_enums(self):
        assert C(TextCOLOR.red, TextSIZE.small) == 'uk-text-red uk-text-small', C(TextCOLOR.red, TextSIZE.small)
    def test_string_and_enum(self):
        assert C(TextCOLOR.red, 'abc', TextSIZE.small) == 'uk-text-red abc uk-text-small', C(TextCOLOR.red, 'abc', TextSIZE.small)

class Text(CoreEnum):
    test = ''
    color = TextCOLOR
    size = TextSIZE

class TestNestedEnum:
    def test_single_enum(self):
        assert C(Text.color.red) == 'uk-text-red'
    def test_multiple_enums(self):
        assert C(Text.color.red, Text.size.small) == 'uk-text-red uk-text-small'
    def test_string_and_enum(self):
        assert C(Text.color.red, 'abc', Text.size.small) == 'uk-text-red abc uk-text-small'
    def test_enum_and_base_attr(self):
        assert C(Text.color.red, Text.test, Text.size.small) == 'uk-text-red uk-text uk-text-small'
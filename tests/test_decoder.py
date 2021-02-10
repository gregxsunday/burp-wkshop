import pytest
import unittest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

from app.core.views import encode_flag
from base64 import b64decode
from urllib.parse import unquote_plus

class DecoderTest(unittest.TestCase):
    def test_encoding(self):
        testflag = 'msfi{flag_decoding_unittest}'
        flag = encode_flag(testflag)
        flag = b64decode(flag)
        flag = ''.join([chr(int(flag[i:i+2], 16)) for i in range(0, len(flag), 2)])
        flag = b64decode(flag).decode('utf8')
        flag = unquote_plus(flag)
        assert testflag == flag


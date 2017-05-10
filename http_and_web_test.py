from unittest import TestCase
from http_and_web import get_name


class TestGetName(TestCase):
    """Test the user input to make sure the name meets a certain criteria;
    that it is only a string.
    """
    def test_artist_name_is_int(self):
        getname = get_name(20)
        self.assertEqual(getname, 'Enter a valid artist_name: ')

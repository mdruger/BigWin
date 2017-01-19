import unittest2
from mock import patch

from programs.BigWin.BigWin.gambler import TicketHolder
from programs.BigWin.BigWin.validator_name import ValidNameEntry


class NameValidatorTestCase(unittest2.TestCase):
    """Tests for names.py."""
    
    @classmethod
    def setUp(cls):
        cls.valid_name = ValidNameEntry()
    
    def test_show_valid_name(self):
        """Is 'Jones, Wendy' a valid name?"""
        self.assertTrue(('Jones', 'Wendy') == self.valid_name('Jones, Wendy'))

    def test_show_invalid_name_with_no_entry(self):
        """Is 'Jones, Wendy,' a valid name with two commas?"""
        self.assertFalse(self.valid_name(''))     
        
    def test_show_invalid_name_with_two_commas(self):
        """Is 'Jones, Wendy,' a valid name with two commas?"""
        self.assertFalse(self.valid_name('Jones, Wendy,'))        

    def test_show_invalid_name_with_two_commas_and_third_name(self):
        """Is 'Jones, Wendy,' a valid name with two commas and third name?"""
        self.assertFalse(self.valid_name('Jones, Wendy, liz'))    
        
    def test_show_invalid_name_with_numbers_as_name(self):
        """Do not accept a number as a name."""
        self.assertFalse(self.valid_name('1'))    

    def test_show_invalid_name_with_numbers_as_name(self):
        """Do not accept a comma separated list of numbers as a name."""
        self.assertFalse(self.valid_name('1, 2'))    

        
class TicketHolderTestCase(unittest2.TestCase):
    
    @patch('programs.BigWin.BigWin.gambler.ValidNameEntry')
    def test_validated_name_is_called(self, mock):
        """Verify that ValidNameEntry is called from GetName."""
        self.get_name = TicketHolder()
        assert mock.called
                
if __name__ == '__main__':
    unittest2.main()
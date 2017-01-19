import unittest2
from mock import patch

from programs.BigWin.BigWin.game import LotteryTicket
from programs.BigWin.BigWin.validator_numbers import LotteryNumbersValidator


class NumberValidatorTestCase(unittest2.TestCase):
    """Tests for LotteryNumbers.py."""
    
    @classmethod
    def setUp(cls):
        cls.valid_lottery_number = LotteryNumbersValidator()
        cls.non_powerball_min = cls.valid_lottery_number.non_powerball_min_number
        cls.non_powerball_max = cls.valid_lottery_number.non_powerball_max_number
        
        cls.powerball_min = cls.valid_lottery_number.powerball_min_number
        cls.powerball_max = cls.valid_lottery_number.powerball_max_number

    def test_valid_number_matches_minimum_number(self):
        """Is a number equal to minimum lottery number a valid number?"""
        self.assertTrue(self.valid_lottery_number(1, str(self.non_powerball_min)))
        
    def test_valid_number_matches_maximum_number(self):
        """Is a number equal to minimum lottery number a valid number?"""
        self.assertTrue(self.valid_lottery_number(1, str(self.non_powerball_max)))
        
    def test_invalid_number_less_than_minimum_number(self):
        """Is a number equal to minimum lottery number a valid number?"""
        self.assertFalse(self.valid_lottery_number(1, str(self.non_powerball_min-1)))
        
    def test_invalid_number_greater_than_maximum_number(self):
        """Is a number equal to minimum lottery number a valid number?"""
        self.assertFalse(self.valid_lottery_number(1, str(self.non_powerball_max+1)))
        
    def test_valid_powerball_number_at_minimum_value(self):
        self.assertTrue(self.valid_lottery_number(6, str(self.powerball_min)))
    
    def test_valid_powerball_number_at_minimum_value(self):
        self.assertTrue(self.valid_lottery_number(6, str(self.powerball_max)))

    def test_invalid_powerball_number_less_than_minimum_number(self):
        """Is a number equal to minimum lottery number a valid number?"""
        self.assertFalse(self.valid_lottery_number(6, str(self.powerball_min-1)))
        
    def test_invalid_powerball_number_greater_than_maximum_number(self):
        """Is a number equal to minimum lottery number a valid number?"""
        self.assertFalse(self.valid_lottery_number(6, str(self.powerball_max+1)))  

class LotteryTicketTestCase(unittest2.TestCase):
    
    @patch('programs.BigWin.BigWin.game.LotteryNumbersValidator')
    def test_validated_name_is_called(self, mock):
        """Verify that ValidNameEntry is called from GetName."""
        self.ticket = LotteryTicket(('test', 'test'))
        assert mock.called
        
if __name__ == '__main__':
    unittest2.main()
from collections import OrderedDict
from pprint import pprint

from programs.BigWin.BigWin.validator_numbers import LotteryNumbersValidator


class LotteryTicket(object):
    """A single lottery ticket."""
    
    _figures = ['st', 'nd', 'rd', 'th']
    
    def __init__(self, ticket_holder_name):
        self.ticket_holder = ticket_holder_name
        self.lottery_numbers = OrderedDict()
        self.valid_lottery_number = LotteryNumbersValidator()
        
    def __call__(self):
        return self._request_number()
    
    def _write_number_figure(self, i):
        if i > 4:
            return "{0}{1}".format(i, self._figures[-1])
        else:
            return "{0}{1}".format(i, self._figures[i-1])
    
    def _excluded_numbers(self):
        if len(self.lottery_numbers) == 0:
            return "): "

        if len(self.lottery_numbers) == 1:
            _exclude_numbers = " excluding {0}): ".format(
                ' '.join(sorted([str(v) for k,v in self.lottery_numbers.items() if k != 6], key=lambda numb: int(numb))))
            return _exclude_numbers
                    
        _exclude_numbers = " excluding {0} and {1}): ".format(
            ' '.join(
                sorted([
                    str(v) for k,v 
                    in self.lottery_numbers.items()
                ][0:len(self.lottery_numbers)-1], key=lambda numb: int(numb))),
            ''.join([str(v) for k,v in self.lottery_numbers.items()][-1])
        )
        
        return _exclude_numbers
    
    def _make_request_msg(self, i):
        if i < self.valid_lottery_number.powerball_pos-1:
            _msg = 'select {0} # ({1} thru {2}{3}'.format(
                self._write_number_figure(i+1),
                self.valid_lottery_number.non_powerball_min_number, 
                self.valid_lottery_number.non_powerball_max_number,
                self._excluded_numbers()
            )
        else:
            _msg = 'select Power Ball # ({1} thru {2}): '.format(
                self._write_number_figure(i),
                self.valid_lottery_number.powerball_min_number, 
                self.valid_lottery_number.powerball_max_number,
            )
        
        _lottery_number_entry = input(_msg)
        
        return _lottery_number_entry
    
    def _data_entry_reminder(self, pos):
        _min, _max = \
            self.valid_lottery_number._get_range_by_number_pos(pos)
        print("\nPlease enter a number between {0} and {1}.\n".format(
            _min, _max))
    
    def _duplicate_number_entries(self, pos, _lottery_number_entry):    
        if pos == self.valid_lottery_number.powerball_pos:
            return False
            
        return any(
            [
                x for x 
                in self.lottery_numbers 
                if self.lottery_numbers[x] == int(_lottery_number_entry)                    
            ]
        )
        
    def _request_number(self):
        lottery_number_entry = False
        i = 0
        while lottery_number_entry is False:
            if not lottery_number_entry:                
                _lottery_number_entry = self._make_request_msg(i)                
                if self.valid_lottery_number(i, _lottery_number_entry):
                    i += 1
                    if not self._duplicate_number_entries(i, _lottery_number_entry):
                        self.lottery_numbers[i] = int(_lottery_number_entry)

                    else:
                        self._data_entry_reminder(i)
                        i -= 1
                                            
                    if i == self.valid_lottery_number.powerball_pos:
                        lottery_number_entry = True              
                        
                else:
                    self._data_entry_reminder(i)
                    i -= 1
            
        return self.lottery_numbers
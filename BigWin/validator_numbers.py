class LotteryRules(object):
    
    def __init__(
            self,
            nonpb_min_value=1,
            nonpb_max_value=69,
            pb_min_value=1,
            pb_max_value=26,
            pb_pos=6
        ):
        self.non_powerball_min_number = nonpb_min_value
        self.non_powerball_max_number = nonpb_max_value
        
        self.powerball_min_number = pb_min_value
        self.powerball_max_number = pb_max_value
        self.powerball_pos = pb_pos

class LotteryNumbersValidator(LotteryRules):
    """Validate number entry."""
    def __init__(self):
        super().__init__()
        
    def _clamp(self, n, minn, maxn):
        return max(min(maxn, n), minn)
    
    def __call__(self, pos, number_entry):
        """Execute the name validated method."""
        self.number = self.validated_number(pos, number_entry)
        if self.number:
            
            return self.number
        
        return False
        
    def _valid_number(self, number_entry):
        if number_entry.isdigit():
            return True
            
        return False
    
    def _get_range_by_number_pos(self, pos):
        _min = self.non_powerball_min_number
        _max = self.non_powerball_max_number
        if pos > self.powerball_pos:
            _min = self.powerball_min_number
            _max = self.powerball_max_number
    
        return _min, _max
    
    def _valid_range(self, pos, entry):
        if int(entry) > 0:
            _min, _max = self._get_range_by_number_pos(pos)
            
            if int(entry) <= self._clamp(int(entry), _min, _max) <= _max:
                return True
            
        return False
        
    def validated_number(self, pos, number_entry):
        if not self._valid_number(number_entry):
            return False
        
        if self._valid_range(pos, number_entry):
            return True

        return False
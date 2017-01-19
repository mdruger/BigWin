from collections import Counter, OrderedDict
import random


class Drawing(object):

    def __init__(self, action):
        self.action = action
        
    def __call__(self, lottery_tickets):
        return self.draw_winning_numbers(lottery_tickets)
        
    def _count_numbers(self, lottery_tickets):
        counts = Counter(
            item for dct in lottery_tickets for item in dct.items())
        
        return counts

    def _count_powerballs(self, lottery_tickets):    
        counts = Counter(
            item for dct in lottery_tickets for item in dct.items())
        
        return counts
    
    def _drawing(self, drawing_type='pb'):
        _min = self.action.valid_lottery_number.non_powerball_min_number
        _max = self.action.valid_lottery_number.non_powerball_max_number
        
        if drawing_type == 'pb':
            _min = self.action.valid_lottery_number.powerball_min_number
            _max = self.action.valid_lottery_number.powerball_max_number
            
        return random.randint(_min, _max)
        
    def _replace_most_frequent_dupes(self, lottery_tickets, winning_ticket):
        _all_action = [i['action'] for i in lottery_tickets]
        _selection_counts = self._count_numbers(_all_action)        
        _dupes = [i for i in _selection_counts.most_common() if i[1] > 1]

        for item in _dupes:
            winning_ticket[item[0][0]] = item[0][1]
            
        return winning_ticket
    
    def draw_winning_numbers(self, lottery_tickets):        
        _winning_ticket = OrderedDict()

        for draw in range(0, 5):
            _winning_ticket[draw + 1] = self._drawing('number')        
        _winning_ticket[6] = self._drawing('pb')

        _winning_ticket = self._replace_most_frequent_dupes(
            lottery_tickets, _winning_ticket)
        
        _draw = "{0} Powerball: {1}".format(' '.join([str(i) for i in _winning_ticket.values()][:5]), _winning_ticket[6])
        
        return _draw
        
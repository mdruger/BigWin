from programs.BigWin.BigWin.speculator import LotteryTicketSpeculator


class PowerBallSpeculator(object):
    def __init__(self):
        self._continue = True
        self.lottery_tickets = []
    
    def __call__(self):
        return self.speculate()
    
    def speculate(self):
        with LotteryTicketSpeculator() as speculate:
            while self._continue:
                lottery_ticket = speculate.get_action()   
                self.lottery_tickets.append(lottery_ticket.copy())

                speculate.show_action(self.lottery_tickets)
                                                      
                _continued = input("\nEnter a new ticket? [Y]/N: ") or 'Y'
                if _continued != 'Y':                
                    print("\nPowerball winning number:\n")
                    print(speculate.winning_lottery_numbers(self.lottery_tickets))
                    self._continue = False  
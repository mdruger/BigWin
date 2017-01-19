from programs.BigWin.BigWin.gambler import TicketHolder
from programs.BigWin.BigWin.game import LotteryTicket
from programs.BigWin.BigWin.powerball import Drawing


class TicketReader:
    
    tickets = []
    
    def __init__(self, context):
        self.ticket = {}
        # print('TicketReader.__init__({})'.format(context))

    def get_action(self):
        self.ticket_holder = TicketHolder()
        gambler = self.ticket_holder()
        
        self.action = LotteryTicket(gambler)
        self.winning_lottery_numbers = Drawing(self.action)
        numbers = self.action()
        
        self.ticket['gambler'] = gambler
        self.ticket['action'] = numbers
        
        self.tickets.append(self.ticket)
        
        return self.ticket
    
    def show_action(self, lottery_tickets):
        print('\nEntered Lottery Tickets:')
        print(
            '\n'.join(
                [
                    "{0:<20s} {1:<15s} Powerball: {2}".format(
                        "{0} {1}".format(
                            i['gambler'][1],
                            i['gambler'][0]
                        ), 
                        ' '.join(
                            [
                                str(v) for k,v 
                                in i['action'].items() 
                                if k != 6
                            ]
                        ), 
                        i['action'][6]
                    ) 
                    for i in lottery_tickets
                ]
            )
        )
    
    def __del__(self):
        pass


class LotteryTicketSpeculator:

    def __init__(self):
        pass

    def __enter__(self):
        return TicketReader(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
from programs.BigWin.BigWin.validator_name import ValidNameEntry


class TicketHolder(object):
    """Command line input for ticket holder name."""

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.valid_name = ValidNameEntry()

    def __call__(self):
        return self.request_name()
    
    def request_name(self):
        name = False
        while name is False:
            if not name:
                name_entry = input('\nEnter your name. last name, first name with a single comma: ')
                name = self.validated_name(name_entry)
                
        return name
      
    def validated_name(self, name):
        """use ValidNameEntry to validate ticket holder name."""        
        names = self.valid_name(name)
        if names:
            self.last_name = names[0]
            self.first_name = names[1]
            return (self.last_name, self.first_name)
        
        print("\nPlease enter last name, first name separated by a single comma.\n")
        return False
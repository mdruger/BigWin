class ValidNameEntry(object):
    """Validate Name entry."""

    def __init__(self):
        self.last_name = None
        self.first_name = None

    def __call__(self, name_entry):
        """Execute the name validated method."""
        self.name = name_entry            
        names = self.validated_name(self.name)
        if names:
            self.last_name = names[0]
            self.first_name = names[1]
            
            return self.last_name, self.first_name
        
        return False

    def _valid_name(self, name):
        """.Return a valid name."""
        names = name.split(',')
        self.last_name = names[0].title().strip()
        self.first_name = names[1].title().strip()
        
        return self.last_name, self.first_name
    
    def _valid_entry_format(self, entry):
        """check for comma."""
        try:
            if ',' not in self.name:
                raise ValueError('comma not found')
              
            return True
            
        except ValueError:
            return False
            
    def _valid_string_entry(self, entry):
        """Check if entry is string."""
        try:
            if any([i for i in entry.split(',') if i.isdigit()]):                
                raise ValueError('entry is not string')  
              
            return True
            
        except ValueError:
            return False

    def _valid_last_first_names(self, entry):
        """check for two names."""
        try:
            if not 1 < len(self.name.split(',')) == 2:
                raise ValueError('comma error')  
              
            return True
            
        except ValueError:
            return False
            
    def _valid_entry(self, entry):
        """Determine if entry is a valid name."""
        try:           
            # check for comma
            if not self._valid_entry_format(entry):
                return False

            # check if entry is string
            if not self._valid_string_entry(entry):
                return False
                
            # check for two names
            if not self._valid_last_first_names(entry):
                return False
                    
        except ValueError:
            return False

        return True
                    
    def validated_name(self, name_entry):
        """Validate the name entry."""
        self.name = name_entry
        if self._valid_entry(self.name):              
            self.last_name, self.first_name = self._valid_name(self.name)
            
            return (self.last_name, self.first_name)
            
        return False
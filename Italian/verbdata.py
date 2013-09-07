from abc import ABCMeta, abstractmethod
 
# Abstract class for verbData
class VerbDataAbstract(metaclass=ABCMeta):
    @abstractmethod
    def setSuffix(self, *args):
        pass

class VerbData(VerbDataAbstract):
    """
    This class stores the suffix-endings for a 1st/2nd/3rd-form conjugation ...
    The 3 conjugations, in no particular order are "are", "ire", "ere"
    """ 
    # Preset class members
    forms  = ('io', 'tu', 'lui/lei/Lei', 'noi', 'voi', 'loro')
    tenses = ('Present', 'Imperfect', 'Future',
              'Present Conditional', 'Past Historic',
              'Present Subjunctive', 'Imperfect Subjunctive')
    
    # Preset instance members 
    def __init__(self, verbType):
        # Which conjugation
        self.verbType = verbType
        # Dictionary of dictionaries (a bit over the top ... so sue me)
        self.suffix = {}
    
    # Load a set of suffix value for a tense
    def setSuffix(self, tense, suffixset):
        # Create dictionary entry that is a dictionary
        self.suffix[tense] = dict(zip(VerbData.forms, suffixset))
    
    # Override the "to string" capability
    def __str__(self):
        # Return value, must be string
        result = ''
        # Cycle through the suffix dictionary-of-dictionaries
        for tenseName in self.suffix.keys():
            # Display current tense
            result += 'Processing tense %s:\n' % tenseName
            # Print the values for each tense
            for formName in self.suffix[tenseName].keys():
                # Print the form/suffix pair
                result += ' ' * 4
                result += '{0} : {1}\n'.format(formName, self.suffix[tenseName][formName])
        return result
    
    # Expand a passed base into conjugated verb
    def printVerb(self, base):
        # Return value, must be string
        result = ''
        # Cycle through the yield-return function for tenses
        for tenseName in VerbData.yieldTenses(self):
            # Display current tense
            result += 'Printing tense %s:\n' % tenseName
            # Print the values for each tense
            for formName in VerbData.forms:
                # Print the base+suffix pair
                result += ' ' * 4
                result += '{0}{1}\n'.format(base, self.suffix[tenseName][formName])
        return result
    
    #Generator function to "yield" used tenses in proper order
    def yieldTenses(self):
        # Cycle through the suffix dictionary-of-dictionaries
        for tenseName in VerbData.tenses:
            # if the tense is defined
            if tenseName in self.suffix.keys():
                # Return current tense
                yield tenseName


if __name__ == '__main__':
    x = VerbData('ire')
    x.setSuffix(x.tenses[0],('a','b','c','d','e','f'))
    x.setSuffix(x.tenses[2],('a','b','c','d','e','f'))
    print(x.printVerb('cour'))
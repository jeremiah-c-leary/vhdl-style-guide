

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.description = None
        self.violations = None

    def report_violations(self,filename):
        if self.violations:
            for violation in self.violations:
                print filename + ":" + str(violation) + ":" + self.name + "_" + self.identifier + ": " + self.description


import rule_whitespace

class list():
    ''' Contains a list of all rules to be checked.  It also contains methods to check the rules.'''

    def __init__(self):
        self.rules = []
        self.rules.append(rule_whitespace.rule_001())
        self.rules.append(rule_whitespace.rule_002())

    def check_rules(self, lines):
        dRuleViolations = {}
        for oRule in self.rules:
            oRule.analyze(lines)

    def report_violations(self, filename):
        for oRule in self.rules:
            oRule.report_violations(filename)

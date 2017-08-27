
import rule_whitespace
import rule_library
import rule_entity

class list():
    ''' Contains a list of all rules to be checked.  It also contains methods to check the rules.'''

    def __init__(self):
        self.rules = []
        self.rules.append(rule_whitespace.rule_001())
        self.rules.append(rule_whitespace.rule_002())
        self.rules.append(rule_whitespace.rule_003())
        self.rules.append(rule_whitespace.rule_004())
        self.rules.append(rule_library.rule_001())
        self.rules.append(rule_library.rule_002())
        self.rules.append(rule_library.rule_003())
        self.rules.append(rule_library.rule_004())
        self.rules.append(rule_library.rule_005())
        self.rules.append(rule_library.rule_006())
        self.rules.append(rule_library.rule_007())
        self.rules.append(rule_library.rule_008())
        self.rules.append(rule_entity.rule_001())
        self.rules.append(rule_entity.rule_002())
        self.rules.append(rule_entity.rule_003())
        self.rules.append(rule_entity.rule_004())
        self.rules.append(rule_entity.rule_005())
        self.rules.append(rule_entity.rule_006())
        self.rules.append(rule_entity.rule_007())
        self.rules.append(rule_entity.rule_008())
        self.rules.append(rule_entity.rule_009())
        self.rules.append(rule_entity.rule_010())
        self.rules.append(rule_entity.rule_011())
        self.rules.append(rule_entity.rule_012())
        self.rules.append(rule_entity.rule_013())
        self.rules.append(rule_entity.rule_014())
        self.rules.append(rule_entity.rule_015())
        self.rules.append(rule_entity.rule_016())
        self.rules.append(rule_entity.rule_017())
        self.rules.append(rule_entity.rule_018())
        self.rules.append(rule_entity.rule_019())
        self.rules.append(rule_entity.rule_020())
        self.rules.append(rule_entity.rule_021())
        self.rules.append(rule_entity.rule_022())
        self.rules.append(rule_entity.rule_023())
        self.rules.append(rule_entity.rule_024())
        self.rules.append(rule_entity.rule_025())
        self.rules.append(rule_entity.rule_026())
        self.rules.append(rule_entity.rule_027())
        self.rules.append(rule_entity.rule_028())
        self.rules.append(rule_entity.rule_029())
        self.rules.append(rule_entity.rule_030())
        self.rules.append(rule_entity.rule_031())
        self.rules.append(rule_entity.rule_032())
        self.rules.append(rule_entity.rule_033())
        self.rules.append(rule_entity.rule_034())
        self.rules.append(rule_entity.rule_035())
        self.rules.append(rule_entity.rule_036())

    def check_rules(self, lines):
        dRuleViolations = {}
        for oRule in self.rules:
            oRule.analyze(lines)

    def report_violations(self, filename):
        for oRule in self.rules:
            oRule.report_violations(filename)

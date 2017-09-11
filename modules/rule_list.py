
import rule_whitespace
import rule_library
import rule_entity
import rule_architecture
import rule_signal
import rule_constant
import rule_concurrent
import rule_process
import rule_port
import rule_generic

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

        self.rules.append(rule_port.rule_001())
        self.rules.append(rule_port.rule_002())
        self.rules.append(rule_port.rule_003())
        self.rules.append(rule_port.rule_004())
        self.rules.append(rule_port.rule_005())
        self.rules.append(rule_port.rule_006())
        self.rules.append(rule_port.rule_007())
        self.rules.append(rule_port.rule_008())
        self.rules.append(rule_port.rule_009())
        self.rules.append(rule_port.rule_010())
        self.rules.append(rule_port.rule_011())
        self.rules.append(rule_port.rule_012())
        self.rules.append(rule_port.rule_013())
        self.rules.append(rule_port.rule_014())
        self.rules.append(rule_port.rule_015())

        self.rules.append(rule_generic.rule_001())
        self.rules.append(rule_generic.rule_002())
        self.rules.append(rule_generic.rule_003())
        self.rules.append(rule_generic.rule_004())
        self.rules.append(rule_generic.rule_005())
        self.rules.append(rule_generic.rule_006())
        self.rules.append(rule_generic.rule_007())
        self.rules.append(rule_generic.rule_008())
        self.rules.append(rule_generic.rule_009())
        self.rules.append(rule_generic.rule_010())
        self.rules.append(rule_generic.rule_011())

        self.rules.append(rule_architecture.rule_001())
        self.rules.append(rule_architecture.rule_002())
        self.rules.append(rule_architecture.rule_003())
        self.rules.append(rule_architecture.rule_004())
        self.rules.append(rule_architecture.rule_005())
        self.rules.append(rule_architecture.rule_006())
        self.rules.append(rule_architecture.rule_007())
        self.rules.append(rule_architecture.rule_008())
        self.rules.append(rule_architecture.rule_009())
        self.rules.append(rule_architecture.rule_010())
        self.rules.append(rule_architecture.rule_011())
        self.rules.append(rule_architecture.rule_012())
        self.rules.append(rule_architecture.rule_013())
        self.rules.append(rule_architecture.rule_014())
        self.rules.append(rule_architecture.rule_015())
        self.rules.append(rule_architecture.rule_016())
        self.rules.append(rule_architecture.rule_017())
        self.rules.append(rule_architecture.rule_018())

        self.rules.append(rule_signal.rule_001())
        self.rules.append(rule_signal.rule_002())
        self.rules.append(rule_signal.rule_003())
        self.rules.append(rule_signal.rule_004())
        self.rules.append(rule_signal.rule_005())
        self.rules.append(rule_signal.rule_006())
        self.rules.append(rule_signal.rule_007())
        self.rules.append(rule_signal.rule_008())
        self.rules.append(rule_signal.rule_009())

        self.rules.append(rule_constant.rule_001())
        self.rules.append(rule_constant.rule_002())
        self.rules.append(rule_constant.rule_003())
        self.rules.append(rule_constant.rule_004())
        self.rules.append(rule_constant.rule_005())
        self.rules.append(rule_constant.rule_006())
        self.rules.append(rule_constant.rule_007())
        self.rules.append(rule_constant.rule_008())
        self.rules.append(rule_constant.rule_009())

        self.rules.append(rule_concurrent.rule_001())
        self.rules.append(rule_concurrent.rule_002())
        self.rules.append(rule_concurrent.rule_003())
        self.rules.append(rule_concurrent.rule_004())
        self.rules.append(rule_concurrent.rule_005())

        self.rules.append(rule_process.rule_001())
        self.rules.append(rule_process.rule_002())
        self.rules.append(rule_process.rule_003())
        self.rules.append(rule_process.rule_004())
        self.rules.append(rule_process.rule_005())
        self.rules.append(rule_process.rule_006())
        self.rules.append(rule_process.rule_007())
        self.rules.append(rule_process.rule_008())
        self.rules.append(rule_process.rule_009())
        self.rules.append(rule_process.rule_010())
        self.rules.append(rule_process.rule_011())


    def check_rules(self, oFile):
        dRuleViolations = {}
        for oRule in self.rules:
            oRule.analyze(oFile)

    def report_violations(self, filename):
        for oRule in self.rules:
            oRule.report_violations(filename)


import unittest
from vsg import rule


class testRuleMethods(unittest.TestCase):

    def test_rule_exists(self):
        oRule = rule.rule()
        self.assertTrue(oRule)

    def test_rule_name(self):
        oRule = rule.rule()
        self.assertFalse(oRule.name)
        oRule.name = 'sName'
        self.assertEqual(oRule.name, 'sName')

    def test_rule_id(self):
        oRule = rule.rule()
        self.assertFalse(oRule.identifier)
        oRule.id = 'rule id 001'
        self.assertEqual(oRule.id, 'rule id 001')

    def test_rule_solution(self):
        oRule = rule.rule()
        self.assertFalse(oRule.solution)
        oRule.solution = 'rule solution'
        self.assertEqual(oRule.solution, 'rule solution')

    def test_add_violations_method(self):
        oRule = rule.rule()
        self.assertEqual(oRule.violations, [])
        oRule.add_violation(1)
        self.assertEqual(oRule.violations, [1])
        oRule.add_violation(10)
        oRule.add_violation(33)
        self.assertEqual(oRule.violations, [1,10,33])

    def test_rule_configure(self):
        oRule = rule.rule()
        oRule.name = 'xyz'
        oRule.identifier = '001'
        oRule.solution = 'This is my solution'
        self.assertEqual(oRule.name,'xyz')
        self.assertEqual(oRule.identifier,'001')
        self.assertEqual(oRule.solution,'This is my solution')
        self.assertEqual(oRule.disable,False)
        self.assertEqual(oRule.indentSize,2)

        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['xyz_001'] = {}
        dConfiguration['rule']['xyz_001']['disable'] = True

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.disable,True)


        dConfiguration['rule']['xyz_002'] = {}
        dConfiguration['rule']['xyz_002']['disable'] = False

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.disable,True)

        dConfiguration['rule']['xyz_001']['solution'] = 'This is the new solution'

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.solution,'This is the new solution')

        dConfiguration['rule']['global'] = {}
        dConfiguration['rule']['global']['indentSize'] = 4

        oRule.configure(dConfiguration)

        self.assertEqual(oRule.indentSize,4)

        # Check for attributes that do not exist
        dConfiguration['rule']['xyz_001']['invalidAttribute'] = False
        oRule.configure(dConfiguration)
        self.assertEqual(oRule.disable,True)
        self.assertEqual(oRule.solution,'This is the new solution')
        self.assertEqual(oRule.indentSize,4)

    def test_report_violations(self):
        oRule = rule.rule()
        oRule.name = 'xyz'
        oRule.identifier = '001'
        oRule.solution = 'This is my solution'
        self.assertEqual(oRule.name,'xyz')
        self.assertEqual(oRule.identifier,'001')
        self.assertEqual(oRule.solution,'This is my solution')
        self.assertEqual(oRule.disable,False)
        self.assertEqual(oRule.indentSize,2)

        self.assertEqual(oRule.report_violations(1, 'vsg', 'filename', True), 0)
        oRule.add_violation(1)
        self.assertEqual(oRule.report_violations(1, 'vsg', 'filename', True), 1)

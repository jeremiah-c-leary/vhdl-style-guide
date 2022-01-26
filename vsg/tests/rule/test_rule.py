
import unittest
from unittest import mock

from vsg import config
from vsg import deprecated_rule
from vsg import parser
from vsg import rule
from vsg import violation
from vsg.vhdlFile.extract import tokens


class command_line_args():
    ''' This is used as an input into the version command.'''
    def __init__(self, version=False):
        self.version = version
        self.style = 'indent_only'
        self.configuration = []
        self.debug = False
        self.fix_only = False


class testRuleMethods(unittest.TestCase):

    def test_rule_exists(self):
        oRule = rule.Rule()
        self.assertTrue(oRule)

    def test_rule_name(self):
        oRule = rule.Rule()
        self.assertFalse(oRule.name)
        oRule.name = 'sName'
        self.assertEqual(oRule.name, 'sName')

    def test_rule_id(self):
        oRule = rule.Rule()
        self.assertFalse(oRule.identifier)
        oRule.id = 'rule id 001'
        self.assertEqual(oRule.id, 'rule id 001')

    def test_rule_solution(self):
        oRule = rule.Rule()
        self.assertFalse(oRule.solution)
        oRule.solution = 'rule solution'
        self.assertEqual(oRule.solution, 'rule solution')

    def test_add_violations_method(self):
        oRule = rule.Rule()
        self.assertEqual(oRule.violations, [])

        oTokens = tokens.New(0, 0, [])
        oViolation = violation.New(0, oTokens, '')

        oRule.add_violation(oViolation)
        self.assertEqual(len(oRule.violations), 1)
        oRule.add_violation(oViolation)
        oRule.add_violation(oViolation)
        self.assertEqual(len(oRule.violations), 3)

    def test_fix_violation(self):
        oRule = rule.Rule()
        oTokens = tokens.New(0, 0, [])
        oViolation = violation.New(0, oTokens, '')

        self.assertIsNone(oRule._fix_violation(oViolation))

    @mock.patch('sys.stdout')
    def test_print_debug_message(self, mock_stdout):
        oRule = rule.Rule()
        oRule.set_debug()
        sString = 'This is a debug message'

        lExpected = []
        lExpected.append(mock.call('INFO: This is a debug message'))
        
        oRule._print_debug_message(sString)

        mock_stdout.write.assert_has_calls(lExpected)

    @unittest.skip('Waiting for full refactor of configuration')
    def test_rule_configure(self):
        oRule = rule.Rule()
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

    def test_get_configuration(self):
        oRule = rule.Rule()
        oRule.name = 'xyz'
        oRule.identifier = '010'
        oRule.phase = 3
        dExpected = {}
        dExpected['disable'] = False
        dExpected['fixable'] = True
        dExpected['indentSize'] = 2
        dExpected['phase'] = 3
        dExpected['severity'] = 'Error'
        dActual = oRule.get_configuration()
        for sKey in dExpected.keys():
            self.assertEqual(dActual[sKey], dExpected[sKey])
        for sKey in dActual.keys():
            self.assertEqual(dActual[sKey], dExpected[sKey])

    def test_get_solution(self):
        oRule = rule.Rule()

        oTokens = tokens.New(0, 0, [])
        oViolation = violation.New(0, oTokens, 'Solution Line 0')

        oRule.add_violation(oViolation)

        oViolation = violation.New(1, oTokens, 'Solution Line 1')
        oRule.add_violation(oViolation)

        self.assertEqual(oRule._get_solution(0), 'Solution Line 0')
        self.assertEqual(oRule._get_solution(1), 'Solution Line 1')

    @unittest.skip('Waiting for full refactor of configuration')
    def test_configure_rule_attributes_method(self):
        oRule = rule.Rule()
        oRule.name = 'xyz'
        oRule.identifier = '001'
        
        oConfig = config.New(command_line_args())

        oConfig.dConfig = {}

        oRule.configure(oConfig)

        self.assertEqual(oRule.indentSize, 2)
        self.assertEqual(oRule.phase, None)
        self.assertEqual(oRule.disable, False)
        self.assertEqual(oRule.fixable, True)
        self.assertEqual(oRule.configuration, ['indentSize', 'phase', 'disable', 'fixable', 'severity'])

        dConfiguration = {}
        dConfiguration['rule'] = {}
        dConfiguration['rule']['xyz_001'] = {}
        dConfiguration['rule']['xyz_001']['indentSize'] = 4
        dConfiguration['rule']['xyz_001']['phase'] = 10
        dConfiguration['rule']['xyz_001']['disable'] = True
        dConfiguration['rule']['xyz_001']['fixable'] = False
        dConfiguration['rule']['xyz_001']['unknown'] = 'New'

        oConfig.dConfig = dConfiguration

        oRule.configure(oConfig)

        self.assertEqual(oRule.indentSize, 4)
        self.assertEqual(oRule.phase, 10)
        self.assertEqual(oRule.disable, True)
        self.assertEqual(oRule.fixable, False)
        self.assertEqual(oRule.configuration, ['indentSize', 'phase', 'disable', 'fixable', 'severity'])

        oRule.configuration.append('unknown')
        oRule.unknown = None
        oRule.configure(oConfig)

        self.assertEqual(oRule.indentSize, 4)
        self.assertEqual(oRule.phase, 10)
        self.assertEqual(oRule.disable, True)
        self.assertEqual(oRule.fixable, False)
        self.assertEqual(oRule.unknown, 'New')
        self.assertEqual(oRule.configuration, ['indentSize', 'phase', 'disable', 'fixable', 'severity', 'unknown'])

    def test_get_violations_w_vsg_output_method(self):
        oRule = rule.Rule('xyz', '001')
        oRule.solution = 'Solution'

        self.assertFalse(oRule.has_violations())

        oToken = parser.item('first')
        oTokens = tokens.New(0, 1, [oToken])

        oViolation = violation.New(1, oTokens, 'First')
        oRule.add_violation(oViolation)

        oToken = parser.item('second')
        oTokens = tokens.New(1, 2, [oToken])

        oViolation = violation.New(2, oTokens, 'Second')
        oRule.add_violation(oViolation)

        oToken = parser.item('third')
        oTokens = tokens.New(2, 3, [oToken])

        oViolation = violation.New(3, oTokens, 'Third')
        oRule.add_violation(oViolation)

        dActual = oRule.get_violations_at_linenumber(1)
        self.assertEqual('First', dActual[0]['solution'])

        dActual = oRule.get_violations_at_linenumber(2)
        self.assertEqual('Second', dActual[0]['solution'])


    def test_has_violations_method(self):
        oRule = rule.Rule()

        self.assertFalse(oRule.has_violations())

        oTokens = tokens.New(0, 0, [])

        oViolation = violation.New(0, oTokens, '')
        oRule.add_violation(oViolation)
        self.assertTrue(oRule.has_violations())


    def test_deprecated_rule(self):
        oRule = deprecated_rule.Rule('some_rule', '001')
        oRule.message = ['This has been deprecated.']

        oConfig = config.New(command_line_args())

        dConfig = {}
        dConfig['rule'] = {}
        dConfig['rule']['some_rule_001'] = {}
        dConfig['rule']['some_rule_001']['disable'] = True

        oConfig.dConfig = dConfig

        lExpected = []
        lExpected.append('ERROR [config-001] Rule some_rule_001 has been deprecated.')
        lExpected.append('  ' + oRule.message[0])

        lActual = oRule.configure(oConfig)

        self.assertEqual(lExpected, lActual)

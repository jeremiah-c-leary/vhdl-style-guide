import unittest
import subprocess

class command_line_args():
    ''' This is used as an input into the version command.'''
    def __init__(self, version=False):
        self.version = version


class testVsg(unittest.TestCase):

#    def test_rc_command_line_argument(self):
#        lExpected = []
#        lExpected.append('{')
#        lExpected.append('  "rule": {')
#        lExpected.append('    "after_002": {')
#        lExpected.append('      "phase": 5,')
#        lExpected.append('      "fixable": true,')
#        lExpected.append('      "disable": true,')
#        lExpected.append('      "indentSize": 2')
#        lExpected.append('    }')
#        lExpected.append('  }')
#        lExpected.append('}')
#        lExpected.append('')
#
#        lActual = subprocess.check_output(['bin/vsg','-rc','after_002'])
#        lActual = str(lActual.decode('utf-8')).split('\n')
#        self.assertEqual(lActual, lExpected)
#
#    def test_rc_command_line_argument_w_configuration(self):
#        lExpected = []
#        lExpected.append('{')
#        lExpected.append('  "rule": {')
#        lExpected.append('    "after_002": {')
#        lExpected.append('      "phase": 5,')
#        lExpected.append('      "fixable": false,')
#        lExpected.append('      "disable": true,')
#        lExpected.append('      "indentSize": 4')
#        lExpected.append('    }')
#        lExpected.append('  }')
#        lExpected.append('}')
#        lExpected.append('')
#
#        lActual = subprocess.check_output(['bin/vsg','-rc','after_002', '-c', 'vsg/tests/vsg/rc_config.json'])
#        lActual = str(lActual.decode('utf-8')).split('\n')
#        self.assertEqual(lActual, lExpected)
#
#    def test_rc_command_line_argument_w_global(self):
#        lExpected = []
#        lExpected.append('{')
#        lExpected.append('  "rule": {')
#        lExpected.append('    "after_002": {')
#        lExpected.append('      "phase": 5,')
#        lExpected.append('      "fixable": true,')
#        lExpected.append('      "disable": true,')
#        lExpected.append('      "indentSize": 3')
#        lExpected.append('    }')
#        lExpected.append('  }')
#        lExpected.append('}')
#        lExpected.append('')
#
#        lActual = subprocess.check_output(['bin/vsg','-rc','after_002', '-c', 'vsg/tests/vsg/rc_global_config.json'])
#        lActual = str(lActual.decode('utf-8')).split('\n')
#        self.assertEqual(lActual, lExpected)

    def test_rc_command_line_argument_w_invalid_rule(self):
        lExpected = []
        lExpected.append('ERROR: rule unknown_rule_001 was not found.')
        lExpected.append('')
        iExitStatus = -1

        try:
            subprocess.check_output(['bin/vsg','-rc','unknown_rule_001'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)


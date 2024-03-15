
import unittest

from vsg import severity

class testMethods(unittest.TestCase):

    def test_error_class_exists(self):
        oSeverity = severity.error('Error')
        self.assertTrue(oSeverity)
        self.assertEqual(oSeverity.name, 'Error')
        self.assertEqual(oSeverity.type, 'error')

    def test_warning_class_exists(self):
        oSeverity = severity.warning('Warning')
        self.assertTrue(oSeverity)
        self.assertEqual(oSeverity.name, 'Warning')
        self.assertEqual(oSeverity.type, 'warning')

    def test_create_list(self):
        oSeverityList = severity.create_list({})
        self.assertEqual(len(oSeverityList.lSeverities), 2)

        self.assertEqual(oSeverityList.get_severity_named('Error').name, 'Error')
        self.assertEqual(oSeverityList.get_severity_named('Warning').name, 'Warning')
        self.assertIsNone(oSeverityList.get_severity_named('Mine'))

    def test_extract_severities_from_configuration(self):
        dConfiguration = {}
        dConfiguration['severity'] = {}
        dSeverity = {}
        dSeverity['type'] = 'warning'
        dSeverity = {}
        dSeverity['type'] = 'error'
        dConfiguration['severity']['Todo'] = dSeverity

        lExpected = []
        lExpected.append(severity.error('Todo'))


        lActual = severity._extract_severities_from_configuration(dConfiguration)

        self.assertEqual(len(lActual), len(lExpected))

        for iIndex, oExpected in enumerate(lExpected):
            self.assertEqual(lActual[iIndex].name, oExpected.name)
            self.assertEqual(lActual[iIndex].type, oExpected.type)

    def test_create_list_add_severity_method(self):
        oSeverityList = severity.create_list({})
        self.assertEqual(len(oSeverityList.lSeverities), 2)

        oSeverity = severity.warning('Guideline')
        oSeverityList.add_severity(oSeverity)

        self.assertEqual(len(oSeverityList.lSeverities), 3)

        self.assertEqual(oSeverityList.get_severity_named('Error').name, 'Error')
        self.assertEqual(oSeverityList.get_severity_named('Warning').name, 'Warning')
        self.assertEqual(oSeverityList.get_severity_named('Guideline').name, 'Guideline')
        self.assertEqual(oSeverityList.get_severity_named('Guideline').type, 'warning')

    def test_create_list_with_configuration(self):
        dConfiguration = {}
        dConfiguration['severity'] = {}
        dSeverity = {}
        dSeverity['type'] = 'warning'
        dConfiguration['severity']['Guideline'] = dSeverity
        dSeverity = {}
        dSeverity['type'] = 'error'
        dConfiguration['severity']['Todo'] = dSeverity

        oSeverityList = severity.create_list(dConfiguration)

        lExpected = []
        lExpected.append(severity.error('Error'))
        lExpected.append(severity.warning('Warning'))
        lExpected.append(severity.warning('Guideline'))
        lExpected.append(severity.error('Todo'))

        lActual = oSeverityList.lSeverities

        self.assertEqual(len(lActual), len(lExpected))

        for iIndex, oExpected in enumerate(lExpected):
            self.assertEqual(lActual[iIndex].name, oExpected.name)
            self.assertEqual(lActual[iIndex].type, oExpected.type)


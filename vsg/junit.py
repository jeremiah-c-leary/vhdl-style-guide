import platform
import datetime


class failure():
    '''
    This class holds failure type attributes.
    '''

    def __init__(self, sType):
        self.type = sType
        self.text = None

    def add_text(self, sText):
        try:
            self.text.append(sText)
        except AttributeError:
            self.text = [sText]

    def build_junit(self):
        '''
        Return a formatted failure as a list of strings.
        '''
        lJunit = ['    <failure type="' + self.type + '">']
        for sText in self.text:
            lJunit.append('      ' + escape_xml_characters(sText))
        lJunit.append('    </failure>')

        return lJunit


class testcase():
    '''
    This class holds testcase attributes.
    '''

    def __init__(self, sName=None, sTime=None, sClassName=None):
        self.name = sName
        self.time = sTime
        self.classname = sClassName
        self.failures = None

    def add_failure(self, oFailure):
        try:
            self.failures.append(oFailure)
        except AttributeError:
            self.failures = [oFailure]

    def build_junit(self):
        '''
        Return formatted testcase as a list of strings.
        '''

        lJunit = ['  <testcase name="' + self.name + '" time="' + self.time + '" classname="' + self.classname + '">']

        if self.failures:
            for oFailure in self.failures:
                try:
                    lJunit.extend(oFailure.build_junit())
                except TypeError:
                    pass

        lJunit.append('  </testcase>')

        return lJunit


class testsuite():
    '''
    This class holds testsuite attributes.
    '''

    def __init__(self, sName, sTime):
        self.name = sName
        self.time = sTime
        self.testcases = None
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%S")

    def add_testcase(self, oTestcase):
        try:
            self.testcases.append(oTestcase)
        except AttributeError:
            self.testcases = [oTestcase]

    def build_junit(self):
        '''
        Return a formatted testsuite as a list of strings.
        '''
        sHeader = '<testsuite'
        sHeader += ' errors="0"'
        sHeader += ' hostname="' + platform.uname()[1] + '"'
        iFailures = 0
        for oTestcase in self.testcases:
            if oTestcase.failures:
                iFailures += len(oTestcase.failures)
        sHeader += ' failures="' + str(iFailures) + '"'
        sHeader += ' timestamp="' + self.timestamp + '"'
        sHeader += ' tests="' + str(len(self.testcases)) + '"'
        sHeader += ' time="' + self.time + '"'
        sHeader += ' name="' + self.name + '"'
        sHeader += '>'
        lJunit = [sHeader]
        lJunit.append('  <properties>')
        lJunit.append('  </properties>')
        for oTestcase in self.testcases:
            lJunit.extend(oTestcase.build_junit())
        lJunit.append('  <system-out>')
        lJunit.append('  </system-out>')
        lJunit.append('  <system-err>')
        lJunit.append('  </system-err>')
        lJunit.append('</testsuite>')

        return lJunit


class xmlfile():
    '''
    This class holds testsuites.
    '''

    def __init__(self, sFileName):
        self.filename = sFileName
        self.testsuites = None

    def add_testsuite(self, oTestsuite):
        try:
            self.testsuites.append(oTestsuite)
        except AttributeError:
            self.testsuites = [oTestsuite]

    def build_junit(self):
        '''
        Return a JUnit XML file formatted as a list of strings.
        '''
        lJunit = ['<?xml version="1.0" ?>']
        for oTestsuite in self.testsuites:
            lJunit.extend(oTestsuite.build_junit())

        return lJunit


def escape_xml_characters(sString):
    '''
    Replaces the following characters in a string:

      &  with &amp;
      "  with &quot;
      '  with &apos;
      <  with &lt;
      >  with &gt;

    Parameters:

        sString : (string)

    Returns: (string)
    '''
    sReturn = sString.replace('&', '&amp;')
    sReturn = sReturn.replace('"', '&quot;')
    sReturn = sReturn.replace('\'', '&apos;')
    sReturn = sReturn.replace('<', '&lt;')
    sReturn = sReturn.replace('>', '&gt;')
    return sReturn

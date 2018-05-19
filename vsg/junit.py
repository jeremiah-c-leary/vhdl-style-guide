
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
      except:
          self.text = [sText]

  def build_junit(self):
      '''
      Returns a list of strings of a formatted failure.
      '''

      lJunit = ['      <failure type="' + self.type + '">']
      for sText in self.text:
          lJunit.append('        ' + sText)
      lJunit.append('      </failure>')

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
      except:
          self.failures = [oFailure]

  def build_junit(self):
      '''
      Return a list of strings of a formatted testcase.
      '''

      lJunit = ['    <testcase name="' + self.name + '" time="' + self.time + '" classname="' + self.classname + '">']
      for oFailure in self.failures:
          lJunit.extend(oFailure.build_junit())
      lJunit.append('    </testcase>')
     
      return lJunit


class testsuite():
  '''
  This class holds testsuite attributes.
  '''

  def __init__(self, sName, sTime):
      self.name = sName
      self.time = sTime
      self.testcases = None

  def add_testcase(self, oTestcase):
      try:
          self.testcases.append(oTestcase)
      except:
          self.testcases = [oTestcase]

  def build_junit(self):
      '''
      Return a list of strings of a formatted testsuite.
      '''

      lJunit = ['  <testsuite>']
      lJunit.append('    <properties>')
      lJunit.append('    </properties>')
      for oTestcase in self.testcases:
          lJunit.extend(oTestcase.build_junit())
      lJunit.append('    <system-out>')
      lJunit.append('    </system-out>')
      lJunit.append('    <system-err>')
      lJunit.append('    </system-err>')
      lJunit.append('  </testsuite>')

      return lJunit

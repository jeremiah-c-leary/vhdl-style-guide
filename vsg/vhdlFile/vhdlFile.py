import re
from vsg import line
from vsg.vhdlFile import update
from vsg.vhdlFile import classify


class vhdlFile():

    def __init__(self, filename):
        self.filename = filename
        self.lines = [line.line('')]
        self.hasArchitecture = False
        self.hasEntity = False
        self._processFile()

    def _processFile(self):

        dVars = {}
        dVars['fFoundProcessBegin'] = False
        dVars['SensitivityListFound'] = False
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        dVars['iCurrentIndentLevel'] = 0

        with open(self.filename) as oFile:
            for sLine in oFile:
                oLine = line.line(sLine.replace('\t', '  ').rstrip())
                update.inside_attributes(self.lines[-1], oLine)

                classify.blank(oLine)
                classify.comment(dVars, oLine)
                classify.library(oLine)
                classify.entity(self, dVars, oLine)
                classify.assert_statement(dVars, oLine)

                if oLine.insideEntity or oLine.insideComponent:
                    classify.port(dVars, oLine)
                    classify.generic(dVars, oLine)

                classify.architecture(self, dVars, oLine)
                classify.packageBody(dVars, oLine)
                classify.package(dVars, oLine)
                classify.component(dVars, oLine)
                classify.signal(dVars, oLine)
                classify.constant(dVars, oLine)
                classify.variable(dVars, oLine)
                classify.process(dVars, oLine)
                classify.generate(dVars, oLine)

                # Check concurrent declarations
                if oLine.insideArchitecture and not oLine.insideProcess:
                    classify.concurrent(dVars, oLine)

                classify.forLoop(dVars, oLine)

                # Check if statements
                if oLine.insideProcess or oLine.insideFunction:
                    classify.ifStatement(dVars, oLine)

                classify.case(self, dVars, oLine)
                classify.function(dVars, oLine)
                classify.type(dVars, oLine)
                # Check sequential statements
                if oLine.insideProcess:
                    classify.sequential(dVars, oLine)
                    classify.variable_assignment(dVars, oLine)

                # Check instantiation statements
                if oLine.insideArchitecture and not oLine.insideProcess and \
                   not oLine.isConcurrentBegin and \
                   not oLine.insideComponent and \
                   not oLine.isGenerateKeyword and \
                   not oLine.insideFunction:
                    classify.instantiation(dVars, oLine)

                # Add line to file
                self.lines.append(oLine)

        oFile.close()

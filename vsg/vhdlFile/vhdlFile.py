
from vsg import line
from vsg.vhdlFile import update
from vsg.vhdlFile import classify


class vhdlFile():
    '''
    Holds contents of a VHDL file.
    When a vhdlFile object is created, the filename passed to it is opened.
    A line object is created for each line read in.
    Then the line object attributes are updated.

    Parameters:

       filename: (string)
    '''
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
        dVars['fProcedureParameterEndDetected'] = False
        dVars['fProcedureIsDetected'] = False
        dVars['fProcedureBeginDetected'] = False
        dVars['fFunctionParameterEndDetected'] = False
        dVars['fFunctionIsDetected'] = False
        dVars['fFunctionBeginDetected'] = False
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        dVars['iCurrentIndentLevel'] = 0
        dVars['iGenerateLevel'] = 0

        try:
            with open(self.filename) as oFile:
                for sLine in oFile:
                    oLine = line.line(sLine.replace('\t', '  ').rstrip())
                    update.inside_attributes(dVars, self.lines[-1], oLine)
    
                    classify.blank(oLine)
                    classify.comment(dVars, oLine)
                    classify.library(oLine)
                    classify.entity(self, dVars, oLine)
                    classify.assert_statement(dVars, oLine)
    
                    classify.port(dVars, oLine)
                    classify.generic(dVars, oLine)
    
                    classify.architecture(self, dVars, oLine)
                    classify.package_body(dVars, oLine)
                    classify.block(self, dVars, oLine)
                    classify.package(dVars, oLine)
                    classify.component(dVars, oLine)
                    classify.signal(dVars, oLine)
                    classify.constant(dVars, oLine)
                    classify.variable(dVars, oLine)
                    classify.process(dVars, oLine)
                    classify.generate(dVars, oLine)
                    classify.attribute(dVars, oLine)
                    classify.file_statement(dVars, oLine)
    
                    classify.concurrent(dVars, oLine)
    
                    classify.with_statement(dVars, oLine)
                    classify.for_loop(dVars, oLine)
                    classify.while_loop(dVars, oLine)
    
                    classify.if_statement(dVars, oLine)
    
                    classify.case(self, dVars, oLine)
                    classify.function(dVars, oLine)
                    classify.procedure(dVars, oLine)
                    classify.type_definition(dVars, oLine)
                    classify.subtype(dVars, oLine)
    
                    classify.sequential(dVars, oLine)
                    classify.variable_assignment(dVars, oLine)
    
                    # Check instantiation statements
                    if oLine.insideArchitecture and not oLine.insideProcess and \
                       not oLine.isConcurrentBegin and \
                       not oLine.insideComponent and \
                       not oLine.isGenerateKeyword and \
                       not oLine.insideFunction and \
                       not oLine.insideProcedure:
                        classify.instantiation(dVars, oLine)
    
                    # Add line to file
                    self.lines.append(oLine)

            oFile.close()

        except IOError:
            pass

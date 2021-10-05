import os
import unittest

from vsg import vhdlFile
from vsg import rule_list
from vsg import severity
from vsg.tests import utils

sSourceDir = os.path.join(os.path.dirname(__file__),'..','..','code_examples','graphicsaccelerator')

dIndentMap = utils.read_indent_file()

lBresenhamer, eBresenhamerError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'Bresenhamer.vhd'))
oBresenhamer = vhdlFile.vhdlFile(lBresenhamer)
oBresenhamer.set_indent_map(dIndentMap)

lDebouncer, eDebouncerError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'Debouncer.vhd'))
oDebouncer = vhdlFile.vhdlFile(lDebouncer)
oDebouncer.set_indent_map(dIndentMap)

lVgatop, eVgatopError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'VGA_Top.vhd'))
oVgatop = vhdlFile.vhdlFile(lVgatop)
oVgatop.set_indent_map(dIndentMap)

lPointer, ePointerError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'Pointer.vhd'))
oPointer = vhdlFile.vhdlFile(lPointer)
oPointer.set_indent_map(dIndentMap)

lFreqDiv, eFreqDivError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'FreqDiv.vhd'))
oFreqDiv = vhdlFile.vhdlFile(lFreqDiv)
oFreqDiv.set_indent_map(dIndentMap)

lSynchronizer, eSynchronizerError = vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'Synchronizer.vhd'))
oSynchronizer = vhdlFile.vhdlFile(lSynchronizer)
oSynchronizer.set_indent_map(dIndentMap)

lFrameBuffer, eFrameBufferError =  vhdlFile.utils.read_vhdlfile(os.path.join(sSourceDir,'FrameBuffer2.vhd'))
oFrameBuffer =  vhdlFile.vhdlFile(lFrameBuffer)
oFrameBuffer.set_indent_map(dIndentMap)

oConfig = utils.read_configuration(os.path.join(os.path.dirname(__file__),'..','..','..','..','styles', 'indent_only.yaml'))

oSeverityList = severity.create_list({})


class testCodeExample(unittest.TestCase):

    def setUp(self):
        self.assertIsNone(eDebouncerError)
        self.assertIsNone(eBresenhamerError)
        self.assertIsNone(eVgatopError)
        self.assertIsNone(ePointerError)
        self.assertIsNone(eFreqDivError)
        self.assertIsNone(eSynchronizerError)
        self.assertIsNone(eFrameBufferError)

    def test_bresenhamer(self):
        oRuleList = rule_list.rule_list(oBresenhamer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Bresenhamer.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oBresenhamer.get_lines())

    def test_debouncer(self):
        oRuleList = rule_list.rule_list(oDebouncer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Debouncer.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oDebouncer.get_lines())

    def test_vga_top(self):
        oRuleList = rule_list.rule_list(oVgatop, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'VGA_Top.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oVgatop.get_lines())

    def test_pointer(self):
        oRuleList = rule_list.rule_list(oPointer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Pointer.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oPointer.get_lines())

    def test_freqdiv(self):
        oRuleList = rule_list.rule_list(oFreqDiv, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'FreqDiv.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oFreqDiv.get_lines())

    def test_synchronizer(self):
        oRuleList = rule_list.rule_list(oSynchronizer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'Synchronizer.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oSynchronizer.get_lines())

    def test_framebuffer(self):
        oRuleList = rule_list.rule_list(oFrameBuffer, oSeverityList)
        oRuleList.configure(oConfig)
        oRuleList.fix(7, oConfig.dConfig['skip_phase'])
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'FrameBuffer2.vhd'), lExpected, bStrip=False)
        self.assertEqual(lExpected, oFrameBuffer.get_lines())

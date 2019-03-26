
import unittest

from vsg import utils


class testUtilsProcedures(unittest.TestCase):

    def test_extract_keywords(self):
        sString = 'This, is a colon : CLK\'event end entity architecture begin -- this is a comment'
        lExpected = ['This','a','colon','CLK']
        self.assertEqual(lExpected, utils.extract_keywords(sString))

        sString = '  U_PROC:process(param_1,param_2)is--Comment  '
        lExpected = ['U_PROC', 'param_1', 'param_2']
        self.assertEqual(lExpected, utils.extract_keywords(sString))

        sString = '  signal sig1, sig2 : std_logic_vector(31 downto 0) := (others => \'0\');'
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_keywords(sString))

        sString = '  Gr3th <= \'0\' when signal1 = X"000_000" else--Comment  '
        lExpected = ['Gr3th', 'signal1']
        self.assertEqual(lExpected, utils.extract_keywords(sString))



import unittest

from vsg import utils
from vsg import line


class testUtilsProcedures(unittest.TestCase):

    def test_extract_non_keywords(self):
        sString = 'This, is a colon : CLK\'event end entity architecture begin -- this is a comment'
        lExpected = ['This','a','colon','CLK']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = '  U_PROC:process(param_1,param_2)is--Comment  '
        lExpected = ['U_PROC', 'param_1', 'param_2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = '  signal sig1, sig2 : std_logic_vector(31 downto 0) := (others => \'0\');'
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = '  Gr3th <= \'0\' when signal1 = X"000_000" else--Comment  '
        lExpected = ['Gr3th', 'signal1']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = '  sig1 x"000_000" sig2 when x"1100_0000"--Comment  '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = '  port map sig1 generic sig2 map (); '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 abs  downto  library  sig2 postponed   srl '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 access   else  linkage sig2  procedure  subtype '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 after   elsif  literal sig2  process  then '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 alias   end  loop  pure  sig2  to '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 all   entity  map  range sig2  transport '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 and  exit  mod  record sig2  type '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 architecture  file   nand sig2 register   unaffected '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 array  for  new   reject sig2  units '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 assert   function  next sig2 rem  until '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 attribute  generate  nor sig2  report   use '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 begin  generic  not  return sig2 variable '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 block  group   null sig2  rol   wait '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 body  guarded   of sig2  ror   when '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 buffer  if  on   select sig2  while '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 bus   impure sig2  open   severity   with '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 case  in  or sig2 shared   xnor '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 component  inertial sig2 others  signal  xor '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 configuration  inout sig2 out  sla '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 constant  is  package sig2 sll '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 disconnect  label sig2  port  sra '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

        sString = ' sig1 * & sig2 ** - + / '
        lExpected = ['sig1', 'sig2']
        self.assertEqual(lExpected, utils.extract_non_keywords(sString))

    def test_change_word(self):
        oLine = line.blank_line()
        oLine.update_line('red blue green yellow')
        sExpected = 'blue blue green yellow'
        utils.change_word(oLine, 'red', 'blue', 1)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue green greenyellow')
        sExpected = 'red blue blue greenyellow'
        utils.change_word(oLine, 'green', 'blue', 1)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue green green,')
        sExpected = 'red blue blue green,'
        utils.change_word(oLine, 'green', 'blue', 1)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue green yellow,')
        sExpected = 'red blue green blue,'
        utils.change_word(oLine, 'yellow', 'blue', 1)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue (green) yellow,')
        sExpected = 'red blue (red) yellow,'
        utils.change_word(oLine, 'green', 'red', 1)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue (green) green,')
        sExpected = 'red blue (red) red,'
        utils.change_word(oLine, 'green', 'red', 2)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue (green) yellow')
        sExpected = 'red blue (green) red'
        utils.change_word(oLine, 'yellow', 'red', 1)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('red blue (green) green;')
        sExpected = 'red blue (red) red;'
        utils.change_word(oLine, 'green', 'red', 2)
        sActual = oLine.line
        self.assertEqual(sExpected, sActual)

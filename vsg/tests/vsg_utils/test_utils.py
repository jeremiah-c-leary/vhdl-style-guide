
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

class testExtractFunctions(unittest.TestCase):

    def test_extract_class_name(self):
        oLine = line.blank_line()
        oLine.update_line('signal s1, s2, s3 : std_logic := \'1\';')
        sExpected = ['signal']
        sActual = utils.extract_class_name(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('CONSTANT C_MY_CONST : integer := -24;')
        sExpected = ['CONSTANT']
        sActual = utils.extract_class_name(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_class_identifier_list(self):
        oLine = line.blank_line()
        oLine.update_line('signal s1, s2, s3 : std_logic := \'1\';')
        sExpected = ['s1', 's2', 's3']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('signal s1, s2, s3')
        sExpected = ['s1', 's2', 's3']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('signal s_x: std_logic;')
        sExpected = ['s_x']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('s1, s2, s3;')
        sExpected = ['s1', 's2', 's3']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('sig;')
        sExpected = ['sig']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('constant C_VALUE : integer;')
        sExpected = ['C_VALUE']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('variable var1, var2 : integer := -32;')
        sExpected = ['var1', 'var2']
        sActual = utils.extract_class_identifier_list(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_generics(self):
        oLine = line.blank_line()
        oLine.update_line('generic( MY_GENERIC: std_logic_vector )')
        sExpected = ['MY_GENERIC']
        sActual = utils.extract_generics(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('generic(GEN1,GEN2: integer )')
        sExpected = ['GEN1', 'GEN2']
        sActual = utils.extract_generics(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_type_name(self):
        oLine = line.blank_line()
        oLine.update_line('variable var1, var2 : integer := -32;')
        sExpected = ['integer']
        sActual = utils.extract_type_name(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('constant con1 : integer;')
        sExpected = ['integer']
        sActual = utils.extract_type_name(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('type fbuffer is array (0 to 524288 / 16 - 1) of std_logic_vector(2 downto 0);')
        sExpected = ['std_logic_vector']
        sActual = utils.extract_type_name(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('signal a,')
        sExpected = []
        sActual = utils.extract_type_name(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_type_name_vhdl_only(self):
        oLine = line.blank_line()
        oLine.update_line('variable var1, var2 : integer := -32;')
        sExpected = ['integer']
        sActual = utils.extract_type_name_vhdl_only(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('variable var1, var2 : my_type := -32;')
        sExpected = []
        sActual = utils.extract_type_name_vhdl_only(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_label(self):
        oLine = line.blank_line()
        oLine.update_line('  cp: CPU')
        sExpected = ['cp']
        sActual = utils.extract_label(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('  cp : CPU')
        sExpected = ['cp']
        sActual = utils.extract_label(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_first_keyword(self):
        oLine = line.blank_line()
        oLine.update_line('MY_LABEL: case (boolean) is')
        sExpected = ['case']
        sActual = utils.extract_first_keyword(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('if rising_edge(clk) then')
        sExpected = ['if']
        sActual = utils.extract_first_keyword(oLine)
        self.assertEqual(sExpected, sActual)

    def test_extract_port_names_from_port_map(self):
        oLine = line.blank_line()
        oLine.update_line('port map( some_port=>sig,')
        sExpected = ['some_port']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('port map (p => s,')
        sExpected = ['p']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('map(p100=>s100,')
        sExpected = ['p100']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('P1 => S1,')
        sExpected = ['P1']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

        oLine = line.blank_line()
        oLine.update_line('port1 => S1,')
        sExpected = ['port1']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)
        oLine = line.blank_line()

        oLine.update_line('p1 => s1, p2 => s2)')
        sExpected = ['p1', 'p2']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

        oLine.update_line(' port_2 (3 downto 0) => w_port_2')
        sExpected = ['port_2']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

        oLine.update_line("PORT_2 => (others => (a => (others => '0'), b => (others => '1')))")
        sExpected = ['PORT_2', 'b']
        sActual = utils.extract_port_names_from_port_map(oLine)
        self.assertEqual(sExpected, sActual)

    def test_is_number(self):
        self.assertTrue(utils.is_number('34'))
        self.assertTrue(utils.is_number('-34'))
        self.assertTrue(utils.is_number('3.4'))
        self.assertTrue(utils.is_number('-3.4'))
        self.assertTrue(utils.is_number('3400'))
        self.assertTrue(utils.is_number('-4034'))
        self.assertFalse(utils.is_number('3.4c'))
        self.assertFalse(utils.is_number('abc'))
        self.assertFalse(utils.is_number('a-b'))
        self.assertFalse(utils.is_number('1-2'))
        self.assertFalse(utils.is_number('c_constant_344'))
        self.assertFalse(utils.is_number('34_c-great'))

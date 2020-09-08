import os

import unittest

from vsg.vhdlFile import vhdlFile_new
from vsg.tests import utils

try:
    sLrmUnit = os.environ['vsg_element']
    
    lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..',sLrmUnit,'classification_test_input.vhd'))
    oFile = vhdlFile_new.vhdlFile(lFile)
    
    
    class test_token(unittest.TestCase):
    
    
        def test_debug(self):
            utils.print_objects(oFile,True)

except KeyError:
  pass

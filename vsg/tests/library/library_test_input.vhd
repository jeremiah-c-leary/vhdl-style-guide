

library lib1;
  use lib1.comp.all;
  use lib1.comp2.all;

 library lib2;

  Library lib3;
  use lib3.comp.all;


library  lib4;
use lib4.comp.all;

use lib4.comp2.all;



LIBRARY     lib5;
    library   lib6;

  use lib6.comp.all;
  use lib6.comp2.all;

USE lib6.comp3.all;   -- USE 
  Use   lib6.comp4.all;


    uSe   lib6.comp5.all;

library lib1
-- Comment 1
  use lib1.all

library lib1
  -- Comment 1
  use lib1.all

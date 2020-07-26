
-- These should pass

context c1 is

  context con1;

end context c1;

context con2;

-- These should fail

context c1 is

  CONTEXT con1;

end context c1;

CONTEXT con2;

CONtext c1 is

  conTEXT con1;

end conText c1;

CoNtExT con2;


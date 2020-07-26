
-- These should pass

context c1 is

  CONTEXT con1;

end context c1;

CONTEXT con2;

-- These should fail

context c1 is

  CONTEXT con1;

end context c1;

CONTEXT con2;

CONtext c1 is

  CONTEXT con1;

end conText c1;

CONTEXT con2;


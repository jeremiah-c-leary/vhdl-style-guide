
-- These should pass

context c1 is

  context con1;

end context c1;

context con2;

-- These should fail

context c1 is

  context con1;

end context c1;

context con2;

CONtext c1 is

  context con1;

end conText c1;

context con2;



--This should pass
context c1 is
  context con1, con2, con3;
end context c1;

--This should fail
context  c1 is
  context   con1, con2, con3;
end context c1;

context   c1 is
  library ieee; context  con1,
 con2, con3;
end context c1;


context   c1 is context  con1, con2,
  con3
;

end context c1;


--This should pass
context c1 is context con1, con2;

end context c1;

-- Split declaration across lines
context
c1
is

library
ieee
;
context --Some somment
con1
,
con2
;
end
context
c1
;

context   con1,
 con2;

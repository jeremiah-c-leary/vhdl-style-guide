
--This should pass
context con1 is

end context con1;

context con2 is

end context con2;

--This should fail
context con3 is

end con3;

context con4 is

end
 con4;

-- Split declaration across lines
context
con5
is

end
context
 con5;

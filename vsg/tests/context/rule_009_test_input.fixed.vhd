
--This should pass
context c1 is

end context c1;

--These should fail
context c1 is
end context
 c1;

context
c1 
is

end context

 -- Some comment
c1;

context

end context -- Some comment
 -- Some other comment
c1;

context c1  -- Yet another commet
  -- Some comment
is

end context
 -- Comment again

 c1;

-- Test with missing end context keyword

context c1 is

end;


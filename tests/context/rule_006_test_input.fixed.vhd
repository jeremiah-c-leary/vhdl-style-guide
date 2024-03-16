
--This should pass
context c1 is

end context c1;

--These should fail
context c1 is

end context c1;

context
c1 is


end context c1;

context
 c1 is  -- Some comment


end context c1;

context c1 is  -- Yet another comment, comment
  -- Some comment


end context c1;

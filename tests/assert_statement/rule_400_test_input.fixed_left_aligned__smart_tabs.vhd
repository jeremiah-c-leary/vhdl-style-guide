
architecture ARCH of ENTITY1 is

begin

  -- Passing wo default
  assert boolean
    report "Something something something" &
			"Something else and this other thing"
    severity FAILURE;

  assert boolean
    report "Something something something" &
			"Something else and this other thing";

  -- Passing w default
  assert boolean
    report "Something something something" &
			"Something else and this other thing"
    severity FAILURE;

  assert boolean
    report "Something something something" &
			"Something else and this other thing";

  -- Failing
  assert boolean
    report "Something something something" &
			"Something else and this other thing"
    severity FAILURE;

  assert boolean
    report "Something something something" &
			"Something else and this other thing";

end architecture ARCH;

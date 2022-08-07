
architecture ARCH of ENTITY1 is

begin

  -- Passing
	LABEL : assert boolean report "Something" severity FAILURE;

	LABEL : assert boolean
		report "Something" severity FAILURE;

	LABEL : assert boolean report "Something"
		severity FAILURE;

	LABEL : assert boolean
		report "Something"
		severity FAILURE;

	assert boolean report "Something" severity FAILURE;

	assert boolean
		report "Something" severity FAILURE;

	assert boolean report "Something"
		severity FAILURE;

	assert boolean
		report "Something"
		severity FAILURE;

  -- Failing
	LABEL : assert boolean report "Something" severity FAILURE;

	LABEL : assert boolean
		report "Something" severity FAILURE;

	LABEL : assert boolean report "Something"
		severity FAILURE;

	LABEL : assert boolean
		report "Something"
		severity FAILURE;

	assert boolean report "Something" severity FAILURE;

	assert boolean
		report "Something" severity FAILURE;

	assert boolean report "Something"
		severity FAILURE;

	assert boolean
		report "Something"
		severity FAILURE;

end architecture ARCH;

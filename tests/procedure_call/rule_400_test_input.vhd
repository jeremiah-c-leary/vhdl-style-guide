
architecture rtl of fifo is

begin

  procedure_call(first, second(2),
                 third(func_call(4, 5, 6)), fourth(7),
                 fifth(8));

  bare_procedure_call;

  process begin

    procedure_call(first, second(2),
                   third(func_call(4, 5, 6)), fourth(7),
                   fifth(8));

    bare_procedure_call;

  end process;

  -- Violations below

  procedure_call(first, second(2),
                        third(func_call(4, 5, 6)), fourth(7),
fifth(8));

  bare_procedure_call;

  process begin

    procedure_call(first, second(2),
 third(func_call(4, 5, 6)), fourth(7),
                          fifth(8));

    bare_procedure_call;

  end process;

end architecture rtl;

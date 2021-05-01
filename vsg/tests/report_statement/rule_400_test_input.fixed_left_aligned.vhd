
architecture rtl of fifo is

begin

  process begin

    report "Something" &
        "Something Else" &
        "Yet another thing"
      severity WARNING;

  end process;

end architecture rtl;

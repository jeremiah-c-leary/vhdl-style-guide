entity broken is
  port (
    x : in bit
  );
end entity broken;

architecture rtl of broken is
begin
  process
  begin
    if x = '1' then
  end process;
end architecture rtl;

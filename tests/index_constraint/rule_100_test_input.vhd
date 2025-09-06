
entity fifo is
  port (
    i_data : in  signed      (15 downto 0);
    i_data : in  signed (15 downto 0);
    i_data : in  signed(15 downto 0)
  );
end entity fifo;


architecture rtl of fifo is

  subtype t_my_array is t_array(open)     (t_range);
  subtype t_my_array is t_array(open) (t_range);
  subtype t_my_array is t_array(open)(t_range);

begin

end architecture rtl;

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tt_um_pe_simonbju is
    port (
        ui_in   : in  std_logic_vector(7 downto 0);
        uo_out  : out std_logic_vector(7 downto 0);
        uio_in  : in  std_logic_vector(7 downto 0);
        uio_out : out std_logic_vector(7 downto 0);
        uio_oe  : out std_logic_vector(7 downto 0);
        ena     : in  std_logic;
        clk     : in  std_logic;
        rst_n   : in  std_logic
    );
end tt_um_pe_simonbju;

architecture Behavioral of tt_um_pe_simonbju is
    signal a, b : unsigned(3 downto 0);
    signal op : std_logic_vector(2 downto 0);
    signal r : unsigned(3 downto 0);
begin

    pipeline: process(clk) is
    begin
        if rising_edge(clk) then
            if ena = '1' then
                a <= unsigned(ui_in(3 downto 0));
                b <= unsigned(ui_in(7 downto 4));
                op <= uio_in(2 downto 0);
                uo_out <= "0000" & std_logic_vector(r);
            end if;
        end if;
    end process;


    with op select
        r <=
            a + b when "000",
            a - b when "001",
            a and b when "010",
            a or b when "011",
            a xor b when "100",
            not a when "101",
            (others => '0') when others;

    uio_out <= (others => '0');
    uio_oe <= (others => '0');

end Behavioral;
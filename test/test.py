# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 25, unit="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    await FallingEdge(dut.clk)

    dut._log.info("Test project behavior")

    assert dut.uo_out.value == 0b00000000
    dut.ui_in.value = 0b00010001
    dut.uio_in.value = 0b00000000 # ADD
    await FallingEdge(dut.clk)

    dut.ui_in.value = 0b00100011
    dut.uio_in.value = 0b00000001 # SUB
    await FallingEdge(dut.clk)

    assert dut.uo_out.value == 0b00000010
    dut.ui_in.value = 0b00110010
    dut.uio_in.value = 0b00000001 # SUB 2 3
    await FallingEdge(dut.clk)

    assert dut.uo_out.value == 0b00000001
    dut.ui_in.value = 0b11010110
    dut.uio_in.value = 0b00000010 # AND
    await FallingEdge(dut.clk)

    assert dut.uo_out.value == 0b00001111
    dut.ui_in.value = 0b10000011
    dut.uio_in.value = 0b00000011 # OR
    await FallingEdge(dut.clk)
    
    assert dut.uo_out.value == 0b00000100
    await FallingEdge(dut.clk)
    
    assert dut.uo_out.value == 0b00001011

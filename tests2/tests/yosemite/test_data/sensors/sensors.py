# ",/usr/bin/env python,
# ,
# Copyright 2018-present Facebook. All Rights Reserved.,
# ,
# This program file is free software; you can redistribute it and/or modify it,
# under the terms of the GNU General Public License as published by the,
# Free Software Foundation; version 2 of the License.,
# ,
# This program is distributed in the hope that it will be useful, but WITHOUT,
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or,
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License,
# for more details.,
# ,
# You should have received a copy of the GNU General Public License,
# along with this program in a file named COPYING; if not, write to the,
# Free Software Foundation, Inc.,,
# 51 Franklin Street, Fifth Floor,,
# Boston, MA 02110-1301 USA,
# ,

SENSORS_SLOT = [
    "MB Outlet Temp",
    "VCCIN VR Temp",
    "VCCGBE VR Temp",
    "1V05PCH VR Temp",
    "SOC Temp",
    "MB Inlet Temp",
    "PCH Temp",
    "SOC Therm Margin",
    "VDDR VR Temp",
    "VCCGBE VR Curr",
    "1V05PCH VR Curr",
    "VCCIN VR Pout",
    "VCCIN VR Curr",
    "VCCIN VR Vol",
    "INA230 Power",
    "INA230 Voltage",
    "SOC Package Pwr",
    "SOC Tjmax",
    "VDDR VR Pout",
    "VDDR VR Curr",
    "VDDR VR Vol",
    "VCCSCSUS VR Curr",
    "VCCSCSUS VR Vol",
    "VCCSCSUS VR Temp",
    "VCCSCSUS VR Pout",
    "VCCGBE VR Pout",
    "VCCGBE VR Vol",
    "1V05PCH VR Pout",
    "1V05PCH VR Vol",
    "SOC DIMMA0 Temp",
    "SOC DIMMA1 Temp",
    "SOC DIMMB0 Temp",
    "SOC DIMMB1 Temp",
    "P3V3_MB",
    "P12V_MB",
    "P1V05_PCH",
    "P3V3_STBY_MB",
    "P5V_STBY_MB",
    "PV_BAT",
    "PVDDR",
    "PVCCGBE",
]

SENSORS_SPB = [
    "SP_INLET_TEMP",
    "SP_OUTLET_TEMP",
    "SP_FAN0_TACH",
    "SP_FAN1_TACH",
    "SP_P5V",
    "SP_P12V",
    "SP_P3V3_STBY",
    "SP_P12V_SLOT1",
    "SP_P12V_SLOT2",
    "SP_P12V_SLOT3",
    "SP_P12V_SLOT4",
    "SP_P3V3",
    "SP_HSC_IN_VOLT",
    "SP_HSC_OUT_CURR",
    "SP_HSC_TEMP",
    "SP_HSC_IN_POWER",
]


SENSOR_NIC = ["MEZZ_SENSOR_TEMP"]

SENSORS = {
    "slot1": SENSORS_SLOT,
    "slot2": SENSORS_SLOT,
    "slot3": SENSORS_SLOT,
    "slot4": SENSORS_SLOT,
    "spb": SENSORS_SPB,
    "nic": SENSOR_NIC,
}

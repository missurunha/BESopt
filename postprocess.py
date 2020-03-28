# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:23:05 2020

@author: Antonio Carneiro
"""
import pickle

class OptimizationResults:
    """Class to process optimization output.

    Attributes
    ---------

    Methods
    -------
    """
    def __init__(self, res_x, res_y, res_z, res_x_tariff, res_x_gas, res_x_el,
                 res_power, res_heat, res_energy, res_p_grid, res_G,
                 res_G_total, res_El, res_El_total, res_soc, res_soc_init,
                 res_ch, res_dch, res_p_use, res_p_sell, res_p_hp, res_c_inv,
                 res_c_om, res_c_dem, res_c_fix, res_c_eeg, res_c_total,
                 res_rev, res_sub, res_emission, res_emission_max,
                 objVal, runtime, MIPGap, name=""):
        self.name = name
        self.x = res_x
        self.y = res_y
        self.z = res_z
        self.x_tariff = res_x_tariff
        self.x_gas = res_x_gas
        self.x_el = res_x_el
        self.power = res_power
        self.heat = res_heat
        self.energy = res_energy
        self.grid = res_p_grid
        self.g = res_G
        self.g_total = res_G_total
        self.el = res_El
        self.El_total = res_El_total
        self.SOC = res_soc
        self.SOC_init = res_soc_init
        self.ch = res_ch
        self.dch = res_dch
        self.p_use = res_p_use
        self.p_sell = res_p_sell
        self.p_HP = res_p_hp
        self.c_inv = res_c_inv
        self.c_om = res_c_om
        self.c_dem = res_c_dem
        self.c_fix = res_c_fix
        self.c_egg = res_c_eeg
        self.c_total = res_c_total
        self.rev = res_rev
        self.sub = res_sub
        self.emission = res_emission
        self.emission_max = res_emission_max
        self.objective = objVal
        self.runtime = runtime
        self.MIPGap = MIPGap

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
            return obj

    def save(self):
        fname = f"{self.name}_results.pkl"
        with open(fname, 'wb') as f:
            pickle.dump(self, f)

    def printDevices(self):
        """To be implemented.

        Generates a list of devices from the variables stored in the object."""
        pass

    def printSummary(self):
        """Print the optimization summary.


        Returns
        -------
        None.

        """
        print(f"Summary: {self.name}")
        print(f"Objective value: {self.objective:.2f}")
        print(f"Emissions: {self.emission:.2f}")
        print(f"MIP Gap: {self.MIPGap}")
        print("Subsidies:")
        for key in self.sub:
            print(f"\t {key}: {self.sub[key]}")

        print("Selected energy tarifs:")
        print("\tGas: {self.x_tariff['gas']}")
        print("\tElectricity:  {self.x_tariff['el']}")

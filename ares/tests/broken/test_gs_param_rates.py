"""

test_21cm_parameterized_rates.py

Author: Jordan Mirocha
Affiliation: University of Colorado at Boulder
Created on: Mon Nov 17 14:21:53 MST 2014

Description: 

"""

import ares
import numpy as np

def test():

    sim = ares.simulations.Global21cm(tanh_model=True,
        verbose=False, progress_bar=False)
    sim.run()
    
    zarr = sim.history['z'][sim.history['z'] < 40]
        
    # Parameterized evolution (const. in time)
    def Gamma_cgm_func(z, species=0, **kwargs):
        return np.interp(z, sim.history['z'][-1::-1], 
            sim.history['cgm_Gamma_h_1'][-1::-1])
        
    def eheat_func(z, species=0, **kwargs):
        return np.interp(z, sim.history['z'][-1::-1], 
            sim.history['igm_heat_h_1'][-1::-1])
    
    def Ja_func(z, **kwargs):
        return np.interp(z, sim.history['z'][-1::-1], 
            sim.history['Ja'][-1::-1])
    
    # Simulate it numerically! (parameterized everything)
    sim2 = ares.simulations.Global21cm(pop_k_ion_cgm=Gamma_cgm_func, 
        pop_k_heat_igm=eheat_func, pop_Ja=Ja_func, is_ion_src_igm=False,
        verbose=False, progress_bar=False, pop_model='user')
    sim2.run()
    
    # Make sure values agree
    sim1_ion_hist = np.interp(zarr, sim.history['z'][-1::-1], 
        sim.history['cgm_h_2'][-1::-1])
    sim2_ion_hist = np.interp(zarr, sim2.history['z'][-1::-1], 
            sim2.history['cgm_h_2'][-1::-1])
    
    ion_hist_ok = np.allclose(sim1_ion_hist, sim2_ion_hist)
            
    sim1_T_hist = np.interp(zarr, sim.history['z'][-1::-1], 
        sim.history['igm_Tk'][-1::-1])
    sim2_T_hist = np.interp(zarr, sim2.history['z'][-1::-1], 
            sim2.history['igm_Tk'][-1::-1])        
    
    T_hist_ok = np.allclose(sim1_T_hist, sim2_T_hist)
    
    assert ion_hist_ok and T_hist_ok

if __name__ == '__main__':
    test()    

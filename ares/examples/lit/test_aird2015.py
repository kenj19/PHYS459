"""
test_Lx(z)

Author: Jacob Jost
Affiliation: University of Colorado at Boulder
Created on: Thu June 4 09:00:00 MDT 2015

--- = spacing between different sections of a code
$$$ = spacing between different parts of codes

The redshift can be set so the same redshift is used for each plot or can be set 
for each individual plot. You either need to keep the top z for the overall or 
hash it out and unhash the other z's to set individually.
"""

import ares
import numpy as np
import matplotlib.pyplot as pl
from scipy import integrate

a15 = ares.util.read_lit('aird2015')

z = np.arange(0, 3)
L = np.logspace(41, 46)

fig1 = pl.figure(1); ax1 = fig1.add_subplot(111)

colors = 'k', 'b', 'g'
for i, redshift in enumerate(z):
    lf_ldde1 = a15.LuminosityFunction(L, redshift)
    
    ax1.loglog(L, lf_ldde1, color=colors[i], ls='-', 
        label=r'$z={}$'.format(redshift))
    
ax1.set_xlabel(r'$L_X$')    
ax1.set_ylabel(r'$\phi(L_X)$')
ax1.legend(loc='best')
pl.show()

import sys
sys.exit()

z = 1.0
#------------------------------------------------------------

#z = 5.0
L = np.logspace(41, 47, 100)

fig1 = pl.figure(1); ax1 = fig1.add_subplot(111)

models = []
for p, Lx in enumerate(L):
    model = a15.LuminosityFunction(Lx, z)
    models.append(model)
models = np.array(models)


pl.loglog(L, models, color = 'k', label = r'LDDE1-Hard Band')
#pl.title('2-7 KeV LDDE1 at z ~ {:.1f}'.format(z))
#pl.ylim(10**-9.1, 10**-2)
#ax1.set_xlabel(r'$L_X$')    
#ax1.set_ylabel(r'$\phi(L_X)$')
#ax1.legend(loc='best')
#pl.show()

#------------------------------------------------------------

#z = 5.0

for p, Lx in enumerate(L):
    model = a15.LuminosityFunction(Lx, z)
    models.append(model)
models = np.array(models)

pl.loglog(L, models, color = 'g', label = r'LDDE2-Hard Band')
#pl.title('2-7 KeV LDDE2 at z ~ {:.1f}'.format(z))
#pl.ylim(10**-9.1, 10**-2)
#ax1.set_xlabel(r'$L_X$')    
#ax1.set_ylabel(r'$\phi(L_X)$')
#ax1.legend(loc='best')
#pl.show()


import sys
sys.exit()


#------------------------------------------------------------

#z = 5.0
L = np.logspace(41, 47, 100)

fig1 = pl.figure(1); ax1 = fig1.add_subplot(111)

models = []
for p, Lx in enumerate(L):
    model = a15.LuminosityFunction(Lx, z, LDDE1 = True, **a15.qsolf_LDDE1_softpars)
    models.append(model)
models = np.array(models)


pl.loglog(L, models, color = 'r', label = r'LDDE1-Soft Band')
#pl.title('0.5-2 KeV LDDE1 at z ~ {:.1f}'.format(z))
#pl.ylim(10**-9.1, 10**-2)
#ax1.set_xlabel(r'$L_X$')    
#ax1.set_ylabel(r'$\phi(L_X)$')
#ax1.legend(loc='best')
#pl.show()

#------------------------------------------------------------

#z = 5.0
L = np.logspace(41, 47, 100)

fig1 = pl.figure(1); ax1 = fig1.add_subplot(111)

models = []
for p, Lx in enumerate(L):
    model = a15.LuminosityFunction(Lx, z, LDDE2 = True, **a15.qsolf_LDDE2_softpars)
    models.append(model)
models = np.array(models)


pl.loglog(L, models, color = 'b', label = r'LDDE2-Soft Band')
pl.title(r'Different models for $\phi(L_X)$ for soft and hard bands at $z$ ~ ${:.1f}$'.format(z))
pl.ylim(10**-9.1, 10**-2) 
ax1.set_xlabel(r'$L_X$')    
ax1.set_ylabel(r'$\phi(L_X)$')
ax1.legend(loc='best')
pl.show()


import sys
sys.exit()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
# -*- coding: utf-8 -*-

test_Lx(z)

Author: Jacob Jost
Affiliation: University of Colorado at Boulder (Undergraduate)
Created on: Thu June 12 11:00:00 MDT 2015


The redshift can be set so the same redshift is used for each plot or can be set 
for each individual plot. You either need to keep the top z for the overall or 
hash it out and unhash the other z's to set individually.

Models = # of models you want to run

NOTE: 
    
    This has not been vectorized so any more than 50 models will take quite some
    time to run. 

    If you want to look at a particular model, just use triple quotes to take the 
    section you dont need out. 
    
    To converte from the 2-10 KeV band to the 0.5-8 Kev Band divide integrand1 by 1.33.
    
    --- = spacing between different sections of code
    
    # of steps for random samples needs to match the steps of the redshift
    
    Need to combine the parameters dictionary and the err dictionarty to use the randomsamples function
"""

#------------------------------------------------------------

#a15 = ares.util.read_lit('aird2015')

Legend = ['Green = LDDE1 softband', 'Red = LDDE1 hardband', \
'Blue =  LDDE2 softband', 'Black = LDDE2 hardband']

z = np.linspace(0, 5, 100)
fig2 = pl.figure(2); ax2 = fig2.add_subplot(111)
#------------------------------------------------------------

#z = np.linspace(0, 5, 100)
#fig2 = pl.figure(2); ax2 = fig2.add_subplot(111)
#a15 = ares.util.read_lit('aird2015')

hardpars = a15.qsolf_LDDE1_hardpars #parameters dictionary
harderr = a15.qsolf_LDDE1_harderr #parameters error dictionary
hardall = hardpars.copy() #copying parameters dictionary
hardall.update(harderr) #combining parameters dictionary & parameters error dictionary

hardsamples = a15.randomsamples(100, **hardall)

models = 50
Legend1 = ['Red = LDDE1 hardband']
                
integrand1=[]
for i in range(models):
    
    integrand = [] 
    for j in range(len(z)):
       
        x = lambda Lx: a15.LuminosityFunction(Lx, z[j], LDDE1 = True,\
        **hardsamples[i])
        p, err = integrate.quad(x, 10**41, 10**46)
        integrand.append(p)
    integrand1.append(integrand)

#HEADS UP: this takes a while to run, use caution. 

for i in range(len(integrand1)):
    pl.semilogy(z, integrand1[i], alpha = 0.25, color = 'r')
    
#ax2.set_ylabel(r'$L_X(z)$')    
#ax2.set_xlabel(r'$z$')
#pl.legend((Legend1), loc='best')
#pl.show()

#------------------------------------------------------------

#z = np.linspace(0, 5, 100)
#fig2 = pl.figure(2); ax2 = fig2.add_subplot(111)
#a15 = ares.util.read_lit('aird2015')

softpars = a15.qsolf_LDDE1_softpars
softerr = a15.qsolf_LDDE1_softerr
softall = softpars.copy()
softall.update(softerr)

softsamples = a15.randomsamples(100, **softall)



models = 50
Legend2 = ['Green = LDDE1 Softband']
                
integrand1=[]
for i in range(models):
    
    integrand = [] 
    for j in range(len(z)):
        x = lambda Lx: a15.LuminosityFunction(Lx, z[j], LDDE1 = True,\
        **softsamples[i])
        p, err = integrate.quad(x, 10**41, 10**46)
        integrand.append(p)
    integrand1.append(integrand)

#HEADS UP: this takes a while to run, use caution. 

for i in range(len(integrand1)):
    pl.semilogy(z, integrand1[i], alpha = 0.25, color = 'g')
    

#ax2.set_ylabel(r'$L_X(z)$')    
#ax2.set_xlabel(r'$z$')
#pl.legend((Legend2), loc='best')
#pl.show()

#------------------------------------------------------------

#z = np.linspace(0, 5, 100)
#fig2 = pl.figure(2); ax2 = fig2.add_subplot(111)
#a15 = ares.util.read_lit('aird2015')

hardpars = a15.qsolf_LDDE2_hardpars
harderr = a15.qsolf_LDDE2_harderr
hardall = hardpars.copy()
hardall.update(harderr)

hardsamples = a15.randomsamples(100, **hardall)

models = 50
Legend3 = ['Black = LDDE2 hardband']
               
integrand1=[]
for i in range(models):
    
    integrand = [] 
    for j in range(len(z)):
        x = lambda Lx: a15.LuminosityFunction(Lx, z[j], LDDE2 = True,\
        **hardsamples[i])
        p, err = integrate.quad(x, 10**41, 10**46)
        integrand.append(p)
    integrand1.append(integrand)

#HEADS UP: this takes a while to run, use caution. 

for i in range(len(integrand1)):
    pl.semilogy(z, integrand1[i], alpha = 0.25, color = 'k')
    
#fig2 = pl.figure(2); ax2 = fig2.add_subplot(111)
#ax2.set_ylabel(r'$L_X(z)$')    
#ax2.set_xlabel(r'$z$')
#pl.legend((Legend3), loc='best')
#pl.show()

#------------------------------------------------------------

#z = np.linspace(0, 5, 100)
#fig2 = pl.figure(2); ax2 = fig2.add_subplot(111)
#a15 = ares.util.read_lit('aird2015')

softpars = a15.qsolf_LDDE2_softpars
softerr = a15.qsolf_LDDE2_softerr
softall = softpars.copy()
softall.update(softerr)

softsamples = a15.randomsamples(100, **softall)

models = 50
Legend4 = ['Blue = LDDE2 Softband']
               
integrand1=[]
for i in range(models):
    
    integrand = [] 
    for j in range(len(z)):
        x = lambda Lx: a15.LuminosityFunction(Lx, z[j], LDDE2 = True,\
        **softsamples[i])
        p, err = integrate.quad(x, 10**41, 10**46)
        integrand.append(p)
    integrand1.append(integrand)

#HEADS UP: this takes a while to run, use caution. 

for i in range(len(integrand1)):
    pl.semilogy(z, integrand1[i], alpha = 0.25, color = 'b')
    

ax2.set_ylabel(r'$L_X(z)$')    
ax2.set_xlabel(r'$z$')
#pl.legend((Legend4), loc='best')
pl.legend((Legend), loc='best')
pl.show()

#---------------------------------------------------------

"""
#z = np.linspace(0, 5, 50)
models = 50
Legend5 = ['Black = 0.5-8 KeV Band (LDDE2)']
               
integrand1=[]
for i in range(models):
    
    integrand = [] 
    for j in range(len(z)):
        x = lambda Lx: a15._LuminosityFunction_LDDE2_integrate(Lx, z[j],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[3], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[-2][i], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[2][i],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[1][i], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[9][i], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[6][i], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[7][i], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[-1][i], \
        list(a15.qsolf_LDDE2_hardpars_integration.values())[-3][i],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[-6][i],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[5][i],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[-4][i],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[4][i],\
        list(a15.qsolf_LDDE2_hardpars_integration.values())[0][i])
        p, err = integrate.quad(x, 10**41, 10**46)
        integrand.append(p)
    integrand1.append(integrand)
integrand1 = np.array(integrand1)

#HEADS UP: this takes a while to run, use caution. 

for i in range(len(integrand1)):
    pl.semilogy(z, integrand1[i], alpha = 0.25, color = 'k')
    

ax2.set_ylabel(r'$L_X(z)$')    
ax2.set_xlabel(r'$z$')
pl.legend((Legend), loc='best')
pl.show()
"""

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
test_Lx(z)

Author: Jacob Jost
Affiliation: University of Colorado at Boulder (Undergraduate)
Created on: Thu June 4 09:00:00 MDT 2015

--- = spacing between different sections of code

The redshift can be set so the same redshift is used for each plot or can be set 
for each individual plot. You either need to keep the top z for the overall or 
hash it out and unhash the other z's to set individually."""


#a15 = ares.util.read_lit('aird2015') 
fig3 = pl.figure(3); ax3 = fig3.add_subplot(111)
Legend = ['Green = LDDE1 softband', 'Red = LDDE1 hardband', 'Blue =  LDDE2 softband', 'Black = LDDE2 hardband']
z = 5.0
L = np.logspace(41, 47, 100)
m = 1000

#------------------------------------------------------------

#z = 5.0
#L = np.logspace(41, 47, 100)
#m = 100
#Legend1 = ['Red = LDDE1 hardband']
#fig3 = pl.figure(3); ax3 = fig3.add_subplot(111)

hardpars = a15.qsolf_LDDE1_hardpars
harderr = a15.qsolf_LDDE1_harderr
hardall = hardpars.copy()
hardall.update(harderr)
hardsamples = a15.randomsamples(1000, **hardall)

models = []
for t in range(m):
    model = []
    models.append(model)
    for Lx in L:
        model1 = a15.LuminosityFunction(Lx, z, LDDE1 = True, **hardsamples[t])
        model.append(model1)

for i, j in enumerate(models):
    pl.loglog(L, models[i], color = 'r', alpha = 0.1)
    
#pl.title('2-7 KeV LDDE1 at z ~ {:.1f}'.format(z))
#pl.ylim(10**-9.1, 10**-2)

#ax3.set_xlabel(r'$L_X$')    
#ax3.set_ylabel(r'$\phi(L_X)$')
#ax3.legend((Legend1), loc='best')
#pl.show()

#------------------------------------------------------------

#z = 5.0
#L = np.logspace(41, 47, 100)
#m = 100
#Legend2 = ['Green = LDDE1 softband']
#fig3 = pl.figure(3); ax3 = fig3.add_subplot(111)

softpars = a15.qsolf_LDDE1_softpars
softerr = a15.qsolf_LDDE1_softerr
softall = softpars.copy()
softall.update(softerr)
softsamples = a15.randomsamples(1000, **softall)

models = []
for t in range(m):
    model = []
    models.append(model)
    for Lx in L:
        model1 = a15.LuminosityFunction(Lx, z, LDDE1 = True, **softsamples[t])
        model.append(model1)

for i, j in enumerate(models):
    pl.loglog(L, models[i], color = 'g', alpha = 0.1)
    
#pl.title('2-7 KeV LDDE1 at z ~ {:.1f}'.format(z))
#pl.ylim(10**-9.1, 10**-2)
#ax3.set_xlabel(r'$L_X$')    
#ax3.set_ylabel(r'$\phi(L_X)$')
#ax3.legend((Legend2), loc='best')
#pl.show()

#------------------------------------------------------------

#z = 5.0
#L = np.logspace(41, 47, 1000)
#m = 100
#Legend3 = ['Black = LDDE2 hardband']
#fig3 = pl.figure(3); ax3 = fig3.add_subplot(111)

hardpars = a15.qsolf_LDDE2_hardpars
harderr = a15.qsolf_LDDE2_harderr
hardall = hardpars.copy()
hardall.update(harderr)
hardsamples = a15.randomsamples(1000, **hardall)

models = []
for t in range(m):
    model = []
    models.append(model)
    for Lx in L:
        model1 = a15.LuminosityFunction(Lx, z, LDDE2 = True, **hardsamples[t])
        model.append(model1)


for i, j in enumerate(models):
    
    pl.loglog(L, models[i], color = 'k', alpha = 0.1)
#pl.title('0.5-2 KeV LDDE1 at z ~ {:.1f}'.format(z))
#pl.ylim(10**-9.1, 10**-2)
#ax3.set_xlabel(r'$L_X$')    
#ax3.set_ylabel(r'$\phi(L_X)$')
#ax3.legend((Legend3), loc='best')
#pl.show()

#------------------------------------------------------------

#z = 5.0
#L = np.logspace(41, 47, 100)
#m = 100
#Legend4 = ['Blue = LDDE2 softband']
#fig3 = pl.figure(3); ax3 = fig3.add_subplot(111)

softpars = a15.qsolf_LDDE2_softpars
softerr = a15.qsolf_LDDE2_softerr
softall = softpars.copy()
softall.update(softerr)
softsamples = a15.randomsamples(1000, **softall)

models = []
for t in range(m):
    model = []
    models.append(model)
    for Lx in L:
        model1 = a15.LuminosityFunction(Lx, z, LDDE2 = True, **softsamples[t])
        model.append(model1)

for i, j in enumerate(models):
    
    pl.loglog(L, models[i], color = 'b', alpha = 0.1)
pl.title(r'Different models for $\phi(L_X)$ for soft and hard bands at $z$ ~ ${:.1f}$'.format(z))
pl.ylim(10**-9.1, 10**-2) 
ax3.set_xlabel(r'$L_X$')    
ax3.set_ylabel(r'$\phi(L_X)$')
#ax3.legend((Legend4), loc='best')
ax3.legend((Legend), loc='best')
pl.show()

#------------------------------------------------------------

import numpy as np
import fitsio
import os, sys
sys.path.insert(0, '/global/homes/q/qmxp55/DESI/omarlibs/bgstargets/py')

from io_ import get_sweep_whole, getBGSbits
from io_ import get_random, get_isdesi, get_dict, bgsmask, get_reg, get_svfields


desit_dr8_s = '/global/cscratch1/sd/qmxp55/desitarget_output/targets-dr8.0-south/targets/main/resolve/bright/targets-dr8-hp-X.fits'
desit_dr8_n = '/global/cscratch1/sd/qmxp55/desitarget_output/targets-dr8.0-north/targets/main/resolve/bright/targets-dr8-hp-X.fits'

catdt_s = fitsio.read(desit_dr8_s)
catdt_n = fitsio.read(desit_dr8_n)
print('DESITARGET cat DONE!')

maskdt_s = get_svfields(catdt_s['RA'],catdt_s['DEC'])
maskdt_n = get_svfields(catdt_n['RA'],catdt_n['DEC'])

catdt_s = catdt_s[maskdt_s]
catdt_n = catdt_n[maskdt_n]
print('In SVFIELD footprint...')

catmy = np.load('/global/cscratch1/sd/qmxp55/sweep_files/dr8_sweep_whole_r21.0_v2.0.npy')
print('MYCAT LOADED...')
maskmy = get_svfields(catmy['RA'],catmy['DEC'])
catmy = catmy[maskmy]
print('MYCAT in SVFIELD Done!')

# Took only data in DECaLS as we want to compare with DESITARGET above catalogue which is only in the south (aka DECaLS+DES)
catmy_s = catmy[catmy['DEC'] < 30]
catmy_n = catmy[catmy['DEC'] > 30]
print('MYCAT per regions DONE!')

#
bgsfdt_s = (catdt_s['BGS_TARGET'] & 2**(0)) != 0
bgsbdt_s = (catdt_s['BGS_TARGET'] & 2**(1)) != 0

bgsbmy_s = ((catmy_s['BGSBITS'] & 2**(21)) != 0)
bgsfmy_s = ((catmy_s['BGSBITS'] & 2**(22)) != 0)

#
bgsfdt_n = (catdt_n['BGS_TARGET'] & 2**(0)) != 0
bgsbdt_n = (catdt_n['BGS_TARGET'] & 2**(1)) != 0

bgsbmy_n = ((catmy_n['BGSBITS'] & 2**(21)) != 0)
bgsfmy_n = ((catmy_n['BGSBITS'] & 2**(22)) != 0)
           
#
print('====== Comparisons in SOUTH ======')
print('Targ. Dens. of BGS faint: %i (DESITARGET) \t %i (MYCODE)' %(np.sum(bgsfdt_s), np.sum(bgsfmy_s)))
print('Targ. Dens. of BGS faint: %i (DESITARGET) \t %i (MYCODE)' %(np.sum(bgsbdt_s), np.sum(bgsbmy_s)))

#
print('====== Comparisons in NORTH ======')
print('Targ. Dens. of BGS faint: %i (DESITARGET) \t %i (MYCODE)' %(np.sum(bgsfdt_n), np.sum(bgsfmy_n)))
print('Targ. Dens. of BGS faint: %i (DESITARGET) \t %i (MYCODE)' %(np.sum(bgsbdt_n), np.sum(bgsbmy_n)))
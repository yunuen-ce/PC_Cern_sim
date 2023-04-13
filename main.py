import numpy as np
import matplotlib.pyplot as plt

def calculate_zeff( Z1, f1, Z2, f2, Z3=0, f3=0, Z4=0, f4=0, Z5=0, f5=0):
    f = f1 + f2 + f3 + f4 + f5
    p=2.94
    if f == 1:
        Zeff = (f1 * Z1 **(p) + f2 * Z2 **(p) + f3 * Z3 **(p) + f4 * Z4 **(p)+ f5 * Z5 **(p))**(1/p)
       # Zeff = f1 * Z1 + f2 * Z2 + f3 * Z3 + f4 * Z4 + f5 * Z5
    else:
        print('fractions dont add to 1')
        Zeff = 0
    return Zeff

Zeff_pvt= calculate_zeff(6, 0.915, 1, 0.085)
Zeff_pvtpb= calculate_zeff(1, 0.07655, 6, 0.9095, 7, 0.0019, 8, 0.00405, 82, 0.0080)
Zeff_poly = calculate_zeff(1, 0.077418, 6, 0.922582)
Zeff_water = calculate_zeff(1, 0.111, 8, 0.889) # (1, 0.111894, 8, 0.888106)
print(Zeff_pvt, Zeff_pvtpb, Zeff_poly, Zeff_water)
line_color=['black', 'red']
# Results
# 9 MeV and 200 MeV
det_pvt = [[7.0457e-11, 0.165], [1.9710e-10, 0.103]]
det_bcf = [[6.9941e-11, 0.165], [1.9526e-10, 0.103]]
det_pb = [[6.9848e-11, 0.165], [1.9488e-10, 0.103]]
det_water = [[7.2379e-11, 0.150], [2.0204e-10, 0.094]]

detector = ['pvt', 'bcf', 'pb', 'water']
energy = ['9 MeV', '200 MeV']
symbol = ['s', 'd']

for e in range(len(energy)):
    plt.errorbar(0, det_water[e][0] / det_water[e][0], yerr= np.sqrt(
        (det_water[e][0] * det_water[e][1] / 100) ** 2 + (det_water[e][0] * det_water[e][1] / 100) ** 2), fmt=symbol[e],
                 color=line_color[e])
    plt.errorbar(1, det_pvt[e][0]/det_water[e][0], yerr=(det_pvt[e][0]/det_water[e][0])*np.sqrt((det_pvt[e][0]*det_pvt[e][1]/100)**2 + (det_water[e][0]*det_water[e][1]/100)**2), fmt=symbol[e], color=line_color[e])
    plt.errorbar(2, det_bcf[e][0]/det_water[e][0], yerr=(det_bcf[e][0]/det_water[e][0])*np.sqrt((det_bcf[e][0]*det_bcf[e][1]/100)**2 + (det_water[e][0]*det_water[e][1]/100)**2),  fmt=symbol[e],  color=line_color[e])
    plt.errorbar(3, det_pb[e][0]/det_water[e][0], yerr=(det_pb[e][0]/det_water[e][0])*np.sqrt((det_pb[e][0]*det_pb[e][1]/100)**2 + (det_water[e][0]*det_water[e][1]/100)**2), fmt=symbol[e],  color=line_color[e], label=energy[e])

plt.xticks([0, 1, 2, 3], ['water', 'pvt', 'bcf', 'pvt + pb'])
plt.ylabel('Dose[] /Dose[water]')
plt.legend()
plt.show()



'''
9 MeV
det_pvt_setup             7.0457e-11 +/- 0.165  % 
det_bcf_setup             6.9941e-11 +/- 0.165  % 
det_pb_setup              6.9848e-11 +/- 0.165  % 
Geometry 1           Geometry 2           Identifier               Dose ratio
det_bcf_setup        det_pvt_setup        -                        0.99268  +/- 0.00232
det_bcf_setup        det_pb_setup         -                        1.00133  +/- 0.00234
det_pvt_setup        det_pb_setup         -                        1.00871  +/- 0.00236

200 MeV
Geometry                        Cavity dose      
-----------------------------------------------
det_pvt_setup             1.9710e-10 +/- 0.103  % 
det_bcf_setup             1.9526e-10 +/- 0.103  % 
det_pb_setup              1.9488e-10 +/- 0.103  % 


Geometry 1           Geometry 2           Identifier               Dose ratio
det_bcf_setup        det_pvt_setup        -                        0.99067  +/- 0.00119
det_bcf_setup        det_pb_setup         -                        1.00197  +/- 0.00120
det_pvt_setup        det_pb_setup         -                        1.01141  +/- 0.00122
'''
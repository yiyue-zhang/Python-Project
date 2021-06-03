# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:37:55 2021

@author: Yi
"""

#Seasons\n",
Seasons = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]

#Free Throws
KobeBryant_FT = [696,667,623,483,439,483,381,525,18,196]
JoeJohnson_FT = [261,235,316,299,220,195,158,132,159,141]
LeBronJames_FT = [601,489,549,594,593,503,387,403,439,375]
CarmeloAnthony_FT = [573,459,464,371,508,507,295,425,459,189]
DwightHoward_FT = [356,390,529,504,483,546,281,355,349,143]
ChrisBosh_FT = [474,463,472,504,470,384,229,241,223,179]
ChrisPaul_FT = [394,292,332,455,161,337,260,286,295,289]
KevinDurant_FT = [209,209,391,452,756,594,431,679,703,146],
DerrickRose_FT = [146,146,146,197,259,476,194,0,27,152]
DwayneWade_FT = [629,432,354,590,534,494,235,308,189,284]

#Free Throw Attempts
KobeBryant_FTA = [819,768,742,564,541,583,451,626,21,241]
JoeJohnson_FTA = [330,314,379,362,269,243,186,161,195,176]
LeBronJames_FTA = [814,701,771,762,773,663,502,535,585,528]
CarmeloAnthony_FTA = [709,568,590,468,612,605,367,512,541,237]
DwightHoward_FTA = [598,666,897,849,816,916,572,721,638,271]
ChrisBosh_FTA = [581,590,559,617,590,471,279,302,272,232]
ChrisPaul_FTA = [465,357,390,524,190,384,302,323,345,321]
KevinDurant_FTA = [256,256,448,524,840,675,501,750,805,171]
DerrickRose_FTA = [205,205,205,250,338,555,239,0,32,187]
DwayneWade_FTA = [803,535,467,771,702,652,297,425,258,370]

import numpy as np
import matplotlib.pyplot as plt

#free throw attempts for each player #Kobe Bryan as an example
plt.plot(Seasons, KobeBryant_FT, color = "red", marker = "o")
plt.title("Kobe Bryant")
plt.xlabel('Year', fontsize=14)
plt.ylabel('Free throw points', fontsize=14)

#free throw accuracy for each player #Kobe Bryan as an example
KobeBryanta = []
for i in range(0, 10):
    KobeBryanta.append(round((KobeBryant_FT[i] / KobeBryant_FTA[i]) * 100))
plt.plot(Seasons, KobeBryanta, color = "black", marker = "^")
plt.title("Kobe Bryant")
plt.xlabel('Year', fontsize=14)
plt.ylabel('Free throw accuracy', fontsize=14)

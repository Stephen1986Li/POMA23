from __future__ import division
import jmp_score as jmp
from math import *
import numpy as np


""" ==================================================================
 Copyright(C) 2018 SAS Institute Inc.All rights reserved.
 
 Notice:
 The following permissions are granted provided that the
 above copyright and this notice appear in the score code and
 any related documentation. Permission to copy, modify
 and distribute the score code generated using
 JMP(R) software is limited to customers of SAS Institute Inc. ("SAS")
 and successive third parties, all without any warranty, express or
 implied, or any other obligation by SAS. SAS and all other SAS
 Institute Inc. product and service names are registered
 trademarks or trademarks of SAS Institute Inc. in the USA
 and other countries. Except as contained in this notice,
 the name of the SAS Institute Inc. and JMP shall not be used in
 the advertising or promotion of products or services without
 prior written authorization from SAS Institute Inc.
 ================================================================== """

""" Python code generated by JMP v16.2.0 """

def getModelMetadata():
	return {"creator": u"Discriminant", "modelName": u"", "predicted": u"itype1", "table": u"final-2022-11-18", "version": u"16.2.0", "timestamp": u"2023-02-13T04:50:32Z"}


def getInputMetadata():
    return {
        u"v455_fc": "float",
        u"v810_mm": "float",
        u"wavelethhl_glcm_correlation_mm": "float",
        u"wavelethhl_glcm_imc1_tc": "float",
        u"wavelethhl_gldm_smalldependencel_mm": "float",
        u"wavelethhl_glrlm_longrunhighgray_mm": "float",
        u"wavelethhl_glszm_graylevelvarian_mm": "float",
        u"wavelethhl_glszm_smallareaemphas_fc": "float",
        u"wavelethlh_firstorder_median_lm": "float",
        u"wavelethlh_glszm_largeareahighgr_tc": "float",
        u"wavelethlh_glszm_zoneentropy_tc": "float",
        u"waveletlhh_firstorder_median_lm": "float",
        u"waveletlhl_firstorder_skewness_tc": "float",
        u"waveletlhl_glszm_zoneentropy_lm": "float",
        u"waveletlll_glcm_clustershade_lm": "float",
        u"waveletlll_glcm_idn_fc": "float"
	}


def getOutputMetadata():
    return {
        u"Prob[Case]": "float",
        u"Prob[Control]": "float",
        u"Pred itype1_1": "str"
	}


def score(indata, outdata):

    # Original name was: 'SqDist[Case]_1'
    # Original name was: 'SqDist[Control]_1'

    _temp_1 = [0 for i in range(2)]
    _temp_2 = u""

    SqDist0_1 = (jmp.vec_quadratic(np.array([[174.259058204683, 107.141623137677, -6333.36298469195, -1.14478161570266, -1.38116996933128, -3.99007222031169, -71.005217045357, -249.527429122803, 0.000408547331600316, -11.7460075579233, 530.125556793215, -8.14104092759178, 0.0000003352592675865, -1.6068020437981, -45.0233155435341, 360.557857630178], [107.141623137677, 26683.5428128032, 74647.2655917397, 7.97517590181142, -38.8099203240908, 9.63230726019007, 1956.2808796327, 3463.76332195958, -0.0220373885071666, -58.1176914813899, 1115.97198453117, 256.20542853681, 0.0000027421665207077, -15.0624463022658, -2251.90586924546, 10764.6601806957], [-6333.36298469195, 74647.2655917397, 1457962.19951911, 154.439746151749, -156.773538302598, 283.559921293113, 9638.64865488973, -22557.7476028709, -0.621346352468847, 944.448042668002, -9612.04759882987, 298.268937119925, 0.0000153266882520226, 258.760352214186, -12232.2308550008, -245085.844316551], [-1.14478161570266, 7.97517590181142, 154.439746151749, 0.0235404564790525, -0.0136305907615965, 0.0174896457035781, 1.31829789015961, -2.97039535524019, -0.000113575695851236, 0.126276633304387, -0.251600211825856, 0.0676430116163292, 0.0000000005865213604, 0.00228183873630279, -1.47468831829, -31.6736581534702], [-1.38116996933128, -38.8099203240908, -156.773538302598, -0.0136305907615965, 37.2284304500024, -1.34090566159194, 41.2901115727424, 160.878647361124, -0.0247573777325132, 15.9363844992475, 183.968019697494, -0.302271562350129, 0.000000124481778447, -0.611863467599445, -44.882762561503, 13.6678381131196], [-3.99007222031169, 9.63230726019007, 283.559921293113, 0.0174896457035781, -1.34090566159194, 20.4030006720482, 108.116816929048, 106.015694988086, 0.00120857464177696, 4.51379565766121, 66.0967733578026, -0.725279821500084, -0.0000001481660576274, -0.693895531687771, -9.93222793914841, -193.597604973112], [-71.005217045357, 1956.2808796327, 9638.64865488973, 1.31829789015961, 41.2901115727424, 108.116816929048, 2999.27161039958, 62.1875493143935, 0.0384828382435018, 35.4485147707451, -956.859828737482, 3.8767463911349, 0.0000002162396786309, -7.47003694926677, 8.05770482750316, 5150.84580040768], [-249.527429122803, 3463.76332195958, -22557.7476028709, -2.97039535524019, 160.878647361124, 106.015694988086, 62.1875493143935, 40323.0119492187, -0.30279312245083, -86.0658074908714, -9423.41977629877, 64.7481152887642, -0.0000026300790638801, 150.010138512486, -978.487620754173, 32283.8246899453], [0.000408547331600316, -0.0220373885071666, -0.621346352468847, -0.000113575695851236, -0.0247573777325132, 0.00120857464177696, 0.0384828382435018, -0.30279312245083, 0.000114240085460467, 0.0278884040665645, -0.0845823569857615, -0.00571678593514649, 6.19510345322355e-11, -0.0122211935282895, -0.091856206324822, 0.120148741301615], [-11.7460075579233, -58.1176914813899, 944.448042668002, 0.126276633304387, 15.9363844992475, 4.51379565766121, 35.4485147707451, -86.0658074908714, 0.0278884040665645, 209.148947418744, 266.06631972102, 7.57058480194321, -0.0000001874669548082, 8.64287649865886, -103.055646064131, -1406.26642063327], [530.125556793215, 1115.97198453117, -9612.04759882987, -0.251600211825856, 183.968019697494, 66.0967733578026, -956.859828737482, -9423.41977629877, -0.0845823569857615, 266.06631972102, 42300.2314783844, -276.11128337127, -0.0000016474528874805, -4.66605651498569, 1152.01950964009, -44782.4871145077], [-8.14104092759178, 256.20542853681, 298.268937119925, 0.0676430116163292, -0.302271562350129, -0.725279821500084, 3.8767463911349, 64.7481152887642, -0.00571678593514649, 7.57058480194321, -276.11128337127, 78.8509434101974, -0.0000000400527821068, -1.20416344799482, -11.2451683905589, 846.349010402711], [0.0000003352592675865, 0.0000027421665207077, 0.0000153266882520226, 0.0000000005865213604, 0.000000124481778447, -0.0000001481660576274, 0.0000002162396786309, -0.0000026300790638801, 6.19510345322355e-11, -0.0000001874669548082, -0.0000016474528874805, -0.0000000400527821068, 1.90588060413055e-14, -0.0000000196291185839, 0.0000002939682637432, 0.0000323834684303796], [-1.6068020437981, -15.0624463022658, 258.760352214186, 0.00228183873630279, -0.611863467599445, -0.693895531687771, -7.47003694926677, 150.010138512486, -0.0122211935282895, 8.64287649865886, -4.66605651498569, -1.20416344799482, -0.0000000196291185839, 28.2533674513904, 41.680782323878, 227.991022858735], [-45.0233155435341, -2251.90586924546, -12232.2308550008, -1.47468831829, -44.882762561503, -9.93222793914841, 8.05770482750316, -978.487620754173, -0.091856206324822, -103.055646064131, 1152.01950964009, -11.2451683905589, 0.0000002939682637432, 41.680782323878, 2061.15478696427, -1251.1129172538], [360.557857630178, 10764.6601806957, -245085.844316551, -31.6736581534702, 13.6678381131196, -193.597604973112, 5150.84580040768, 32283.8246899453, 0.120148741301615, -1406.26642063327, -44782.4871145077, 846.349010402711, 0.0000323834684303796, 227.991022858735, -1251.1129172538, 605971.518357721]]),np.concatenate((np.array([[indata[u"wavelethhl_glszm_graylevelvarian_mm"]]]),np.array([[indata[u"wavelethhl_glcm_correlation_mm"]]]),np.array([[indata[u"wavelethhl_gldm_smalldependencel_mm"]]]),np.array([[indata[u"wavelethhl_glrlm_longrunhighgray_mm"]]]),np.array([[indata[u"waveletlhl_glszm_zoneentropy_lm"]]]),np.array([[indata[u"wavelethlh_glszm_zoneentropy_tc"]]]),np.array([[indata[u"wavelethhl_glszm_smallareaemphas_fc"]]]),np.array([[indata[u"waveletlll_glcm_idn_fc"]]]),np.array([[indata[u"waveletlll_glcm_clustershade_lm"]]]),np.array([[indata[u"wavelethlh_firstorder_median_lm"]]]),np.array([[indata[u"wavelethhl_glcm_imc1_tc"]]]),np.array([[indata[u"waveletlhl_firstorder_skewness_tc"]]]),np.array([[indata[u"wavelethlh_glszm_largeareahighgr_tc"]]]),np.array([[indata[u"waveletlhh_firstorder_median_lm"]]]),np.array([[indata[u"v810_mm"]]]),np.array([[indata[u"v455_fc"]]])))))[0][0]

    SqDist_Case__1 = 46518.2654533753 + SqDist0_1 + -140727.93296277 * indata[u"v455_fc"] + 1781.1180526132 * indata[u"v810_mm"] + -10677.7808817774 * indata[u"wavelethhl_glcm_correlation_mm"] + 21129.8337954755 * indata[u"wavelethhl_glcm_imc1_tc"] + 70467.0496898792 * indata[u"wavelethhl_gldm_smalldependencel_mm"] + 10.5269388379892 * indata[u"wavelethhl_glrlm_longrunhighgray_mm"] + -23.8456581287552 * indata[u"wavelethhl_glszm_graylevelvarian_mm"] + -6054.72028436839 * indata[u"wavelethhl_glszm_smallareaemphas_fc"] + 196.038744547905 * indata[u"wavelethlh_firstorder_median_lm"] + -0.0000024081994623117 * indata[u"wavelethlh_glszm_largeareahighgr_tc"] + -392.336186216467 * indata[u"wavelethlh_glszm_zoneentropy_tc"] + -299.434599890548 * indata[u"waveletlhh_firstorder_median_lm"] + -211.31077669668 * indata[u"waveletlhl_firstorder_skewness_tc"] + -743.183157980846 * indata[u"waveletlhl_glszm_zoneentropy_lm"] + 0.803382800994478 * indata[u"waveletlll_glcm_clustershade_lm"] + -80372.8306970031 * indata[u"waveletlll_glcm_idn_fc"]

    SqDist_Control__1 = 46353.7669430051 + SqDist0_1 + -140506.98376066 * indata[u"v455_fc"] + 1743.69821791699 * indata[u"v810_mm"] + -10581.7780401271 * indata[u"wavelethhl_glcm_correlation_mm"] + 21036.5633429013 * indata[u"wavelethhl_glcm_imc1_tc"] + 71465.2142195974 * indata[u"wavelethhl_gldm_smalldependencel_mm"] + 10.636922258777 * indata[u"wavelethhl_glrlm_longrunhighgray_mm"] + -32.0692331605877 * indata[u"wavelethhl_glszm_graylevelvarian_mm"] + -6018.10697052979 * indata[u"wavelethhl_glszm_smallareaemphas_fc"] + 202.352070357849 * indata[u"wavelethlh_firstorder_median_lm"] + -0.000002497737529154 * indata[u"wavelethlh_glszm_largeareahighgr_tc"] + -390.430291457254 * indata[u"wavelethlh_glszm_zoneentropy_tc"] + -296.79919177225 * indata[u"waveletlhh_firstorder_median_lm"] + -205.837340742549 * indata[u"waveletlhl_firstorder_skewness_tc"] + -740.347435077053 * indata[u"waveletlhl_glszm_zoneentropy_lm"] + 0.797873252077264 * indata[u"waveletlll_glcm_clustershade_lm"] + -80239.4291850222 * indata[u"waveletlll_glcm_idn_fc"]

    outdata[u"Prob[Case]"] = 1 / (1 + jmp.exp((0.5 * SqDist_Case__1 + -0.5 * SqDist_Control__1)))

    outdata[u"Prob[Control]"] = 1 / (1 + jmp.exp((-0.5 * SqDist_Case__1 + 0.5 * SqDist_Control__1)))

    _temp_1[0] = outdata[u"Prob[Case]"]
    _temp_1[1] = outdata[u"Prob[Control]"]
    _temp_0 = jmp.max_array(2, _temp_1)
    if jmp.mz(_temp_0 == 0):
        _temp_2 = u"Case"
    elif jmp.mz(_temp_0 == 1):
        _temp_2 = u"Control"
    else:
        _temp_2 = u""
    outdata[u"Pred itype1_1"] = _temp_2

    return outdata[u"Pred itype1_1"]


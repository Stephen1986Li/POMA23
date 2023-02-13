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
	return {"creator": u"Fit Generalized", "modelName": u"Lasso", "predicted": u"itype1", "table": u"final-2022-11-18", "version": u"16.2.0", "timestamp": u"2023-02-13T04:58:43Z"}


def getInputMetadata():
    return {
        u"original_firstorder_minimum_fc": "float",
        u"original_glszm_smallareaemphasis_fc": "float",
        u"original_shape_elongation_lm": "float",
        u"original_shape_sphericity_mm": "float",
        u"v455_fc": "float",
        u"v620_fc": "float",
        u"v810_mm": "float",
        u"wavelethhh_firstorder_minimum_fc": "float",
        u"wavelethhh_glcm_clustershade_mm": "float",
        u"wavelethhh_glcm_imc1_lm": "float",
        u"wavelethhh_glrlm_runvariance_mm": "float",
        u"wavelethhh_glszm_largeareahighgr_fc": "float",
        u"wavelethhl_firstorder_mean_mm": "float",
        u"wavelethhl_glcm_clusterprominenc_fc": "float",
        u"wavelethhl_glcm_correlation_mm": "float",
        u"wavelethhl_glcm_imc1_mm": "float",
        u"wavelethhl_glcm_imc1_tc": "float",
        u"wavelethhl_gldm_smalldependencel_fc": "float",
        u"wavelethhl_gldm_smalldependencel_mm": "float",
        u"wavelethhl_glrlm_longrunhighgray_mm": "float",
        u"wavelethhl_glszm_graylevelvarian_mm": "float",
        u"wavelethhl_glszm_largearealowgra_fc": "float",
        u"wavelethhl_glszm_smallareaemphas_fc": "float",
        u"wavelethlh_firstorder_median_lm": "float",
        u"wavelethlh_glszm_largeareahighgr_tc": "float",
        u"wavelethlh_glszm_zoneentropy_tc": "float",
        u"wavelethll_firstorder_kurtosis_mm": "float",
        u"wavelethll_firstorder_skewness_lm": "float",
        u"wavelethll_glszm_graylevelnonuni_fc": "float",
        u"wavelethll_glszm_largearealowgra_lm": "float",
        u"wavelethll_glszm_smallareaemphas_fc": "float",
        u"wavelethll_ngtdm_busyness_mm": "float",
        u"waveletlhh_firstorder_maximum_mm": "float",
        u"waveletlhh_firstorder_median_lm": "float",
        u"waveletlhh_glszm_smallareaemphas_mm": "float",
        u"waveletlhl_firstorder_minimum_tc": "float",
        u"waveletlhl_firstorder_skewness_fc": "float",
        u"waveletlhl_firstorder_skewness_tc": "float",
        u"waveletlhl_glcm_clustershade_fc": "float",
        u"waveletlhl_glszm_zoneentropy_lm": "float",
        u"waveletlhl_glszm_zoneentropy_mm": "float",
        u"waveletllh_firstorder_minimum_fc": "float",
        u"waveletllh_glcm_correlation_mm": "float",
        u"waveletllh_glcm_imc1_mm": "float",
        u"waveletllh_gldm_smalldependencel_mm": "float",
        u"waveletllh_glszm_zoneentropy_fc": "float",
        u"waveletlll_glcm_clustershade_lm": "float",
        u"waveletlll_glcm_idn_fc": "float",
        u"waveletlll_gldm_largedependenceh_lm": "float",
        u"waveletlll_glszm_graylevelnonuni_fc": "float",
        u"waveletlll_glszm_graylevelvarian_mm": "float",
        u"waveletlll_ngtdm_busyness_tc": "float",
        u"Probability( itype1=Control )": "float",
        u"Probability( itype1=Case )": "float"
	}


def getOutputMetadata():
    return {
        u"Probability( itype1=Control ),!Probability( itype1=Control )": "float",
        u"Probability( itype1=Case ),!Probability( itype1=Case )": "float",
        u"Most Likely itype1,!Most Likely itype1": "str"
	}


def score(indata, outdata):

    _temp_1 = [0 for i in range(2)]
    _temp_2 = u""

    outdata[u"Probability( itype1=Control ),!Probability( itype1=Control )"] = jmp.squish((138.906662284563 + -0.0374840613777587 * indata[u"original_firstorder_minimum_fc"] + 30.0851204984573 * indata[u"original_glszm_smallareaemphasis_fc"] + -5.16886931938608 * indata[u"original_shape_elongation_lm"] + -22.6027937197107 * indata[u"original_shape_sphericity_mm"] + -183.241411245849 * indata[u"v455_fc"] + -31.2864884900061 * indata[u"v620_fc"] + 13.0929184029347 * indata[u"v810_mm"] + -0.0449150326270933 * indata[u"wavelethhh_firstorder_minimum_fc"] + -80.5541121951956 * indata[u"wavelethhh_glcm_clustershade_mm"] + -175.513292031235 * indata[u"wavelethhh_glcm_imc1_lm"] + 14.1388520672465 * indata[u"wavelethhh_glrlm_runvariance_mm"] + -0.0000000065806757192 * indata[u"wavelethhh_glszm_largeareahighgr_fc"] + 8.44401662768123 * indata[u"wavelethhl_firstorder_mean_mm"] + -2.50698631344467 * indata[u"wavelethhl_glcm_clusterprominenc_fc"] + -70.4834404869617 * indata[u"wavelethhl_glcm_correlation_mm"] + 135.159288730406 * indata[u"wavelethhl_glcm_imc1_mm"] + 68.3596341150643 * indata[u"wavelethhl_glcm_imc1_tc"] + -580.872797304735 * indata[u"wavelethhl_gldm_smalldependencel_fc"] + -634.382491552537 * indata[u"wavelethhl_gldm_smalldependencel_mm"] + -0.0725533381359363 * indata[u"wavelethhl_glrlm_longrunhighgray_mm"] + 7.05678012366991 * indata[u"wavelethhl_glszm_graylevelvarian_mm"] + 0.0000034063862657645 * indata[u"wavelethhl_glszm_largearealowgra_fc"] + -23.7451543847941 * indata[u"wavelethhl_glszm_smallareaemphas_fc"] + -2.46711982513115 * indata[u"wavelethlh_firstorder_median_lm"] + 0.000000052516315218 * indata[u"wavelethlh_glszm_largeareahighgr_tc"] + -1.61594579730143 * indata[u"wavelethlh_glszm_zoneentropy_tc"] + -0.315597348534774 * indata[u"wavelethll_firstorder_kurtosis_mm"] + 2.72362187343286 * indata[u"wavelethll_firstorder_skewness_lm"] + -0.00363176200000953 * indata[u"wavelethll_glszm_graylevelnonuni_fc"] + -0.0000108750618386455 * indata[u"wavelethll_glszm_largearealowgra_lm"] + -34.6049578360473 * indata[u"wavelethll_glszm_smallareaemphas_fc"] + -0.00622267395786139 * indata[u"wavelethll_ngtdm_busyness_mm"] + 0.0125102964039785 * indata[u"waveletlhh_firstorder_maximum_mm"] + -1.63901757644153 * indata[u"waveletlhh_firstorder_median_lm"] + -5.4573283165394 * indata[u"waveletlhh_glszm_smallareaemphas_mm"] + -0.00913208687306463 * indata[u"waveletlhl_firstorder_minimum_tc"] + 3.82470924731225 * indata[u"waveletlhl_firstorder_skewness_fc"] + -2.44052577290932 * indata[u"waveletlhl_firstorder_skewness_tc"] + -0.271269630988434 * indata[u"waveletlhl_glcm_clustershade_fc"] + -2.22075325292815 * indata[u"waveletlhl_glszm_zoneentropy_lm"] + -1.73129068376673 * indata[u"waveletlhl_glszm_zoneentropy_mm"] + -0.0049465095877357 * indata[u"waveletllh_firstorder_minimum_fc"] + -22.7839150149442 * indata[u"waveletllh_glcm_correlation_mm"] + -49.4931066442567 * indata[u"waveletllh_glcm_imc1_mm"] + 508.07815254672 * indata[u"waveletllh_gldm_smalldependencel_mm"] + -4.27054091625983 * indata[u"waveletllh_glszm_zoneentropy_fc"] + 0.00258323341544075 * indata[u"waveletlll_glcm_clustershade_lm"] + -66.2396707106205 * indata[u"waveletlll_glcm_idn_fc"] + 0.0000154180694582632 * indata[u"waveletlll_gldm_largedependenceh_lm"] + 0.00278500701223195 * indata[u"waveletlll_glszm_graylevelnonuni_fc"] + 0.12855055853742 * indata[u"waveletlll_glszm_graylevelvarian_mm"] + -0.237040444584005 * indata[u"waveletlll_ngtdm_busyness_tc"]))

    outdata[u"Probability( itype1=Case ),!Probability( itype1=Case )"] = 1 + -1 * jmp.squish((138.906662284563 + -0.0374840613777587 * indata[u"original_firstorder_minimum_fc"] + 30.0851204984573 * indata[u"original_glszm_smallareaemphasis_fc"] + -5.16886931938608 * indata[u"original_shape_elongation_lm"] + -22.6027937197107 * indata[u"original_shape_sphericity_mm"] + -183.241411245849 * indata[u"v455_fc"] + -31.2864884900061 * indata[u"v620_fc"] + 13.0929184029347 * indata[u"v810_mm"] + -0.0449150326270933 * indata[u"wavelethhh_firstorder_minimum_fc"] + -80.5541121951956 * indata[u"wavelethhh_glcm_clustershade_mm"] + -175.513292031235 * indata[u"wavelethhh_glcm_imc1_lm"] + 14.1388520672465 * indata[u"wavelethhh_glrlm_runvariance_mm"] + -0.0000000065806757192 * indata[u"wavelethhh_glszm_largeareahighgr_fc"] + 8.44401662768123 * indata[u"wavelethhl_firstorder_mean_mm"] + -2.50698631344467 * indata[u"wavelethhl_glcm_clusterprominenc_fc"] + -70.4834404869617 * indata[u"wavelethhl_glcm_correlation_mm"] + 135.159288730406 * indata[u"wavelethhl_glcm_imc1_mm"] + 68.3596341150643 * indata[u"wavelethhl_glcm_imc1_tc"] + -580.872797304735 * indata[u"wavelethhl_gldm_smalldependencel_fc"] + -634.382491552537 * indata[u"wavelethhl_gldm_smalldependencel_mm"] + -0.0725533381359363 * indata[u"wavelethhl_glrlm_longrunhighgray_mm"] + 7.05678012366991 * indata[u"wavelethhl_glszm_graylevelvarian_mm"] + 0.0000034063862657645 * indata[u"wavelethhl_glszm_largearealowgra_fc"] + -23.7451543847941 * indata[u"wavelethhl_glszm_smallareaemphas_fc"] + -2.46711982513115 * indata[u"wavelethlh_firstorder_median_lm"] + 0.000000052516315218 * indata[u"wavelethlh_glszm_largeareahighgr_tc"] + -1.61594579730143 * indata[u"wavelethlh_glszm_zoneentropy_tc"] + -0.315597348534774 * indata[u"wavelethll_firstorder_kurtosis_mm"] + 2.72362187343286 * indata[u"wavelethll_firstorder_skewness_lm"] + -0.00363176200000953 * indata[u"wavelethll_glszm_graylevelnonuni_fc"] + -0.0000108750618386455 * indata[u"wavelethll_glszm_largearealowgra_lm"] + -34.6049578360473 * indata[u"wavelethll_glszm_smallareaemphas_fc"] + -0.00622267395786139 * indata[u"wavelethll_ngtdm_busyness_mm"] + 0.0125102964039785 * indata[u"waveletlhh_firstorder_maximum_mm"] + -1.63901757644153 * indata[u"waveletlhh_firstorder_median_lm"] + -5.4573283165394 * indata[u"waveletlhh_glszm_smallareaemphas_mm"] + -0.00913208687306463 * indata[u"waveletlhl_firstorder_minimum_tc"] + 3.82470924731225 * indata[u"waveletlhl_firstorder_skewness_fc"] + -2.44052577290932 * indata[u"waveletlhl_firstorder_skewness_tc"] + -0.271269630988434 * indata[u"waveletlhl_glcm_clustershade_fc"] + -2.22075325292815 * indata[u"waveletlhl_glszm_zoneentropy_lm"] + -1.73129068376673 * indata[u"waveletlhl_glszm_zoneentropy_mm"] + -0.0049465095877357 * indata[u"waveletllh_firstorder_minimum_fc"] + -22.7839150149442 * indata[u"waveletllh_glcm_correlation_mm"] + -49.4931066442567 * indata[u"waveletllh_glcm_imc1_mm"] + 508.07815254672 * indata[u"waveletllh_gldm_smalldependencel_mm"] + -4.27054091625983 * indata[u"waveletllh_glszm_zoneentropy_fc"] + 0.00258323341544075 * indata[u"waveletlll_glcm_clustershade_lm"] + -66.2396707106205 * indata[u"waveletlll_glcm_idn_fc"] + 0.0000154180694582632 * indata[u"waveletlll_gldm_largedependenceh_lm"] + 0.00278500701223195 * indata[u"waveletlll_glszm_graylevelnonuni_fc"] + 0.12855055853742 * indata[u"waveletlll_glszm_graylevelvarian_mm"] + -0.237040444584005 * indata[u"waveletlll_ngtdm_busyness_tc"]))

    _temp_1[0] = indata[u"Probability( itype1=Control )"]
    _temp_1[1] = indata[u"Probability( itype1=Case )"]
    _temp_0 = jmp.max_array(2, _temp_1)
    if jmp.mz(_temp_0 == 0):
        _temp_2 = u"Control"
    elif jmp.mz(_temp_0 == 1):
        _temp_2 = u"Case"
    else:
        _temp_2 = u""
    outdata[u"Most Likely itype1,!Most Likely itype1"] = _temp_2

    return outdata[u"Most Likely itype1,!Most Likely itype1"]


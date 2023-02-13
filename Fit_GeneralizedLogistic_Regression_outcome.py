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
	return {"creator": u"Fit Generalized", "modelName": u"Logistic Regression", "predicted": u"itype1", "table": u"final-2022-11-18", "version": u"16.2.0", "timestamp": u"2023-02-13T04:25:44Z"}


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
        u"Probability( itype1=Case )": "float",
        u"Probability( itype1=Control )": "float"
	}


def getOutputMetadata():
    return {
        u"Probability( itype1=Case ),!Probability( itype1=Case )": "float",
        u"Probability( itype1=Control ),!Probability( itype1=Control )": "float",
        u"Most Likely itype1,!Most Likely itype1": "str"
	}


def score(indata, outdata):

    _temp_1 = [0 for i in range(2)]
    _temp_2 = u""

    outdata[u"Probability( itype1=Case ),!Probability( itype1=Case )"] = jmp.squish((-172.775141372896 + 0.0700013881448006 * indata[u"original_firstorder_minimum_fc"] + -34.6341381687953 * indata[u"original_glszm_smallareaemphasis_fc"] + 7.54578689212087 * indata[u"original_shape_elongation_lm"] + 24.9071630447123 * indata[u"original_shape_sphericity_mm"] + 218.137837762385 * indata[u"v455_fc"] + 39.0624589184386 * indata[u"v620_fc"] + -14.8937736069372 * indata[u"v810_mm"] + 0.0604526564360081 * indata[u"wavelethhh_firstorder_minimum_fc"] + 89.5301013123465 * indata[u"wavelethhh_glcm_clustershade_mm"] + 214.358761675947 * indata[u"wavelethhh_glcm_imc1_lm"] + -17.6764276816312 * indata[u"wavelethhh_glrlm_runvariance_mm"] + 0.0000000080922643666 * indata[u"wavelethhh_glszm_largeareahighgr_fc"] + -8.40701742507882 * indata[u"wavelethhl_firstorder_mean_mm"] + 3.24586941507034 * indata[u"wavelethhl_glcm_clusterprominenc_fc"] + 82.0036396632976 * indata[u"wavelethhl_glcm_correlation_mm"] + -167.929146981831 * indata[u"wavelethhl_glcm_imc1_mm"] + -81.2591606535897 * indata[u"wavelethhl_glcm_imc1_tc"] + 623.8196279605 * indata[u"wavelethhl_gldm_smalldependencel_fc"] + 633.853678229485 * indata[u"wavelethhl_gldm_smalldependencel_mm"] + 0.0712579203802247 * indata[u"wavelethhl_glrlm_longrunhighgray_mm"] + -8.37242054133618 * indata[u"wavelethhl_glszm_graylevelvarian_mm"] + -0.0000040672567565978 * indata[u"wavelethhl_glszm_largearealowgra_fc"] + 27.028294011724 * indata[u"wavelethhl_glszm_smallareaemphas_fc"] + 2.68091328754982 * indata[u"wavelethlh_firstorder_median_lm"] + -0.0000000601367110805 * indata[u"wavelethlh_glszm_largeareahighgr_tc"] + 1.87372477941517 * indata[u"wavelethlh_glszm_zoneentropy_tc"] + 0.430843975535361 * indata[u"wavelethll_firstorder_kurtosis_mm"] + -3.33711473495706 * indata[u"wavelethll_firstorder_skewness_lm"] + 0.00320998251121829 * indata[u"wavelethll_glszm_graylevelnonuni_fc"] + 0.0000096730777206538 * indata[u"wavelethll_glszm_largearealowgra_lm"] + 36.6019335270319 * indata[u"wavelethll_glszm_smallareaemphas_fc"] + 0.0114474155576093 * indata[u"wavelethll_ngtdm_busyness_mm"] + -0.0142720476386511 * indata[u"waveletlhh_firstorder_maximum_mm"] + 1.8562871937663 * indata[u"waveletlhh_firstorder_median_lm"] + 5.62642810418155 * indata[u"waveletlhh_glszm_smallareaemphas_mm"] + 0.00855828593287416 * indata[u"waveletlhl_firstorder_minimum_tc"] + -4.62528411700657 * indata[u"waveletlhl_firstorder_skewness_fc"] + 2.78111477571768 * indata[u"waveletlhl_firstorder_skewness_tc"] + 0.436133710049468 * indata[u"waveletlhl_glcm_clustershade_fc"] + 2.38003617427814 * indata[u"waveletlhl_glszm_zoneentropy_lm"] + 2.19765939161489 * indata[u"waveletlhl_glszm_zoneentropy_mm"] + 0.00548500502818228 * indata[u"waveletllh_firstorder_minimum_fc"] + 23.7225356876432 * indata[u"waveletllh_glcm_correlation_mm"] + 60.070472306518 * indata[u"waveletllh_glcm_imc1_mm"] + -677.424891403618 * indata[u"waveletllh_gldm_smalldependencel_mm"] + 5.00353308692232 * indata[u"waveletllh_glszm_zoneentropy_fc"] + -0.0029503317107897 * indata[u"waveletlll_glcm_clustershade_lm"] + 91.8404517476474 * indata[u"waveletlll_glcm_idn_fc"] + -0.0000930711561240935 * indata[u"waveletlll_gldm_largedependenceh_lm"] + -0.00251842296463469 * indata[u"waveletlll_glszm_graylevelnonuni_fc"] + -0.127514568580581 * indata[u"waveletlll_glszm_graylevelvarian_mm"] + 0.242909639123736 * indata[u"waveletlll_ngtdm_busyness_tc"]))

    outdata[u"Probability( itype1=Control ),!Probability( itype1=Control )"] = 1 + -1 * jmp.squish((-172.775141372896 + 0.0700013881448006 * indata[u"original_firstorder_minimum_fc"] + -34.6341381687953 * indata[u"original_glszm_smallareaemphasis_fc"] + 7.54578689212087 * indata[u"original_shape_elongation_lm"] + 24.9071630447123 * indata[u"original_shape_sphericity_mm"] + 218.137837762385 * indata[u"v455_fc"] + 39.0624589184386 * indata[u"v620_fc"] + -14.8937736069372 * indata[u"v810_mm"] + 0.0604526564360081 * indata[u"wavelethhh_firstorder_minimum_fc"] + 89.5301013123465 * indata[u"wavelethhh_glcm_clustershade_mm"] + 214.358761675947 * indata[u"wavelethhh_glcm_imc1_lm"] + -17.6764276816312 * indata[u"wavelethhh_glrlm_runvariance_mm"] + 0.0000000080922643666 * indata[u"wavelethhh_glszm_largeareahighgr_fc"] + -8.40701742507882 * indata[u"wavelethhl_firstorder_mean_mm"] + 3.24586941507034 * indata[u"wavelethhl_glcm_clusterprominenc_fc"] + 82.0036396632976 * indata[u"wavelethhl_glcm_correlation_mm"] + -167.929146981831 * indata[u"wavelethhl_glcm_imc1_mm"] + -81.2591606535897 * indata[u"wavelethhl_glcm_imc1_tc"] + 623.8196279605 * indata[u"wavelethhl_gldm_smalldependencel_fc"] + 633.853678229485 * indata[u"wavelethhl_gldm_smalldependencel_mm"] + 0.0712579203802247 * indata[u"wavelethhl_glrlm_longrunhighgray_mm"] + -8.37242054133618 * indata[u"wavelethhl_glszm_graylevelvarian_mm"] + -0.0000040672567565978 * indata[u"wavelethhl_glszm_largearealowgra_fc"] + 27.028294011724 * indata[u"wavelethhl_glszm_smallareaemphas_fc"] + 2.68091328754982 * indata[u"wavelethlh_firstorder_median_lm"] + -0.0000000601367110805 * indata[u"wavelethlh_glszm_largeareahighgr_tc"] + 1.87372477941517 * indata[u"wavelethlh_glszm_zoneentropy_tc"] + 0.430843975535361 * indata[u"wavelethll_firstorder_kurtosis_mm"] + -3.33711473495706 * indata[u"wavelethll_firstorder_skewness_lm"] + 0.00320998251121829 * indata[u"wavelethll_glszm_graylevelnonuni_fc"] + 0.0000096730777206538 * indata[u"wavelethll_glszm_largearealowgra_lm"] + 36.6019335270319 * indata[u"wavelethll_glszm_smallareaemphas_fc"] + 0.0114474155576093 * indata[u"wavelethll_ngtdm_busyness_mm"] + -0.0142720476386511 * indata[u"waveletlhh_firstorder_maximum_mm"] + 1.8562871937663 * indata[u"waveletlhh_firstorder_median_lm"] + 5.62642810418155 * indata[u"waveletlhh_glszm_smallareaemphas_mm"] + 0.00855828593287416 * indata[u"waveletlhl_firstorder_minimum_tc"] + -4.62528411700657 * indata[u"waveletlhl_firstorder_skewness_fc"] + 2.78111477571768 * indata[u"waveletlhl_firstorder_skewness_tc"] + 0.436133710049468 * indata[u"waveletlhl_glcm_clustershade_fc"] + 2.38003617427814 * indata[u"waveletlhl_glszm_zoneentropy_lm"] + 2.19765939161489 * indata[u"waveletlhl_glszm_zoneentropy_mm"] + 0.00548500502818228 * indata[u"waveletllh_firstorder_minimum_fc"] + 23.7225356876432 * indata[u"waveletllh_glcm_correlation_mm"] + 60.070472306518 * indata[u"waveletllh_glcm_imc1_mm"] + -677.424891403618 * indata[u"waveletllh_gldm_smalldependencel_mm"] + 5.00353308692232 * indata[u"waveletllh_glszm_zoneentropy_fc"] + -0.0029503317107897 * indata[u"waveletlll_glcm_clustershade_lm"] + 91.8404517476474 * indata[u"waveletlll_glcm_idn_fc"] + -0.0000930711561240935 * indata[u"waveletlll_gldm_largedependenceh_lm"] + -0.00251842296463469 * indata[u"waveletlll_glszm_graylevelnonuni_fc"] + -0.127514568580581 * indata[u"waveletlll_glszm_graylevelvarian_mm"] + 0.242909639123736 * indata[u"waveletlll_ngtdm_busyness_tc"]))

    _temp_1[0] = indata[u"Probability( itype1=Case )"]
    _temp_1[1] = indata[u"Probability( itype1=Control )"]
    _temp_0 = jmp.max_array(2, _temp_1)
    if jmp.mz(_temp_0 == 0):
        _temp_2 = u"Case"
    elif jmp.mz(_temp_0 == 1):
        _temp_2 = u"Control"
    else:
        _temp_2 = u""
    outdata[u"Most Likely itype1,!Most Likely itype1"] = _temp_2

    return outdata[u"Most Likely itype1,!Most Likely itype1"]


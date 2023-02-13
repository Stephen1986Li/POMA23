﻿/* 
 * SAS code generated by JMP v16.2.0
 * From the following model(s): 
 *   拟合广义/自适应“双 Lasso” - itype1
 * Variable name mapping: 
 *   original_firstorder_minimum_fc => original_firstorder_minimum_fc
 *   original_glszm_smallareaemphasis_fc => original_glszm_smallareaemphasis
 *   original_shape_elongation_lm => original_shape_elongation_lm
 *   original_shape_sphericity_mm => original_shape_sphericity_mm
 *   v455_fc => v455_fc
 *   v620_fc => v620_fc
 *   v810_mm => v810_mm
 *   wavelethhh_firstorder_minimum_fc => wavelethhh_firstorder_minimum_fc
 *   wavelethhh_glcm_clustershade_mm => wavelethhh_glcm_clustershade_mm
 *   wavelethhh_glcm_imc1_lm => wavelethhh_glcm_imc1_lm
 *   wavelethhh_glrlm_runvariance_mm => wavelethhh_glrlm_runvariance_mm
 *   wavelethhh_glszm_largeareahighgr_fc => wavelethhh_glszm_largeareahighgr
 *   wavelethhl_firstorder_mean_mm => wavelethhl_firstorder_mean_mm
 *   wavelethhl_glcm_clusterprominenc_fc => wavelethhl_glcm_clusterprominenc
 *   wavelethhl_glcm_correlation_mm => wavelethhl_glcm_correlation_mm
 *   wavelethhl_glcm_imc1_mm => wavelethhl_glcm_imc1_mm
 *   wavelethhl_glcm_imc1_tc => wavelethhl_glcm_imc1_tc
 *   wavelethhl_gldm_smalldependencel_fc => wavelethhl_gldm_smalldependencel
 *   wavelethhl_gldm_smalldependencel_mm => wavelethhl_gldm_smalldependence2
 *   wavelethhl_glrlm_longrunhighgray_mm => wavelethhl_glrlm_longrunhighgray
 *   wavelethhl_glszm_graylevelvarian_mm => wavelethhl_glszm_graylevelvarian
 *   wavelethhl_glszm_largearealowgra_fc => wavelethhl_glszm_largearealowgra
 *   wavelethhl_glszm_smallareaemphas_fc => wavelethhl_glszm_smallareaemphas
 *   wavelethlh_firstorder_median_lm => wavelethlh_firstorder_median_lm
 *   wavelethlh_glszm_largeareahighgr_tc => wavelethlh_glszm_largeareahighgr
 *   wavelethlh_glszm_zoneentropy_tc => wavelethlh_glszm_zoneentropy_tc
 *   wavelethll_firstorder_kurtosis_mm => wavelethll_firstorder_kurtosis_m
 *   wavelethll_firstorder_skewness_lm => wavelethll_firstorder_skewness_l
 *   wavelethll_glszm_graylevelnonuni_fc => wavelethll_glszm_graylevelnonuni
 *   wavelethll_glszm_largearealowgra_lm => wavelethll_glszm_largearealowgra
 *   wavelethll_glszm_smallareaemphas_fc => wavelethll_glszm_smallareaemphas
 *   wavelethll_ngtdm_busyness_mm => wavelethll_ngtdm_busyness_mm
 *   waveletlhh_firstorder_maximum_mm => waveletlhh_firstorder_maximum_mm
 *   waveletlhh_firstorder_median_lm => waveletlhh_firstorder_median_lm
 *   waveletlhh_glszm_smallareaemphas_mm => waveletlhh_glszm_smallareaemphas
 *   waveletlhl_firstorder_minimum_tc => waveletlhl_firstorder_minimum_tc
 *   waveletlhl_firstorder_skewness_fc => waveletlhl_firstorder_skewness_f
 *   waveletlhl_firstorder_skewness_tc => waveletlhl_firstorder_skewness_t
 *   waveletlhl_glcm_clustershade_fc => waveletlhl_glcm_clustershade_fc
 *   waveletlhl_glszm_zoneentropy_lm => waveletlhl_glszm_zoneentropy_lm
 *   waveletlhl_glszm_zoneentropy_mm => waveletlhl_glszm_zoneentropy_mm
 *   waveletllh_firstorder_minimum_fc => waveletllh_firstorder_minimum_fc
 *   waveletllh_glcm_correlation_mm => waveletllh_glcm_correlation_mm
 *   waveletllh_glcm_imc1_mm => waveletllh_glcm_imc1_mm
 *   waveletllh_gldm_smalldependencel_mm => waveletllh_gldm_smalldependencel
 *   waveletllh_glszm_zoneentropy_fc => waveletllh_glszm_zoneentropy_fc
 *   waveletlll_glcm_clustershade_lm => waveletlll_glcm_clustershade_lm
 *   waveletlll_glcm_idn_fc => waveletlll_glcm_idn_fc
 *   waveletlll_gldm_largedependenceh_lm => waveletlll_gldm_largedependenceh
 *   waveletlll_glszm_graylevelnonuni_fc => waveletlll_glszm_graylevelnonuni
 *   waveletlll_glszm_graylevelvarian_mm => waveletlll_glszm_graylevelvarian
 *   waveletlll_ngtdm_busyness_tc => waveletlll_ngtdm_busyness_tc
 *   最可能的“itype1”_1 => __itype1__1
 *   概率 ( itype1=Case ) => __itype1_Case_
 *   概率 ( itype1=Control ) => __itype1_Control_
 */
DECLARE int idx_max;
DECLARE double val_max;
DECLARE double acc_max;
idx_max = 0;
acc_max = .;

__itype1_Case_ = (1/(1+exp(-((-172.314275759506 + 0.0698069198722904*original_firstorder_minimum_fc + -34.5287138545909*
  original_glszm_smallareaemphasis + 7.52847283555431*original_shape_elongation_lm + 24.8320833122873*original_shape_sphericity_mm + 
  217.495246919398*v455_fc + 38.9676918327534*v620_fc + -14.8691202157608*v810_mm + 0.0602888949136799*wavelethhh_firstorder_minimum_fc + 
  89.2495344791801*wavelethhh_glcm_clustershade_mm + 213.773098091994*wavelethhh_glcm_imc1_lm + -17.6276240728582*wavelethhh_glrlm_runvariance_mm + 
  0.0000000080719363555*wavelethhh_glszm_largeareahighgr + -8.38605622822001*wavelethhl_firstorder_mean_mm + 3.2364724806286*
  wavelethhl_glcm_clusterprominenc + 81.8360980927234*wavelethhl_glcm_correlation_mm + -167.384837720787*wavelethhl_glcm_imc1_mm + 
  -81.0820217266207*wavelethhl_glcm_imc1_tc + 621.763588160631*wavelethhl_gldm_smalldependencel + 632.411254057462*wavelethhl_gldm_smalldependence2 + 
  0.0710881207259484*wavelethhl_glrlm_longrunhighgray + -8.351738303974*wavelethhl_glszm_graylevelvarian + -0.0000040561045732148*
  wavelethhl_glszm_largearealowgra + 26.9670478158734*wavelethhl_glszm_smallareaemphas + 2.67589095757834*wavelethlh_firstorder_median_lm + 
  -0.0000000600164173229*wavelethlh_glszm_largeareahighgr + 1.86950561596052*wavelethlh_glszm_zoneentropy_tc + 0.429287840979061*
  wavelethll_firstorder_kurtosis_m + -3.3301283354265*wavelethll_firstorder_skewness_l + 0.00320049649204003*wavelethll_glszm_graylevelnonuni + 
  0.0000096137070879199*wavelethll_glszm_largearealowgra + 36.5045204583078*wavelethll_glszm_smallareaemphas + 0.0114133947661589*
  wavelethll_ngtdm_busyness_mm + -0.014209835899086*waveletlhh_firstorder_maximum_mm + 1.85250947419981*waveletlhh_firstorder_median_lm + 
  5.59512662546722*waveletlhh_glszm_smallareaemphas + 0.00854410262392001*waveletlhl_firstorder_minimum_tc + -4.60982515805346*
  waveletlhl_firstorder_skewness_f + 2.77392733677797*waveletlhl_firstorder_skewness_t + 0.434544097213904*waveletlhl_glcm_clustershade_fc + 
  2.37371532631983*waveletlhl_glszm_zoneentropy_lm + 2.19071943478082*waveletlhl_glszm_zoneentropy_mm + 0.00545600840256806*
  waveletllh_firstorder_minimum_fc + 23.6600207591023*waveletllh_glcm_correlation_mm + 59.9111630785163*waveletllh_glcm_imc1_mm + 
  -675.256556331641*waveletllh_gldm_smalldependencel + 4.98801409541456*waveletllh_glszm_zoneentropy_fc + -0.0029447507382415*
  waveletlll_glcm_clustershade_lm + 91.6163084067093*waveletlll_glcm_idn_fc + -0.0000923483577302275*waveletlll_gldm_largedependenceh + 
  -0.00251156764446676*waveletlll_glszm_graylevelnonuni + -0.127240045441525*waveletlll_glszm_graylevelvarian + 0.24205064244792*
  waveletlll_ngtdm_busyness_tc)))));
__itype1_Control_ = 1 + -1*(1/(1+exp(-((-172.314275759506 + 0.0698069198722904*original_firstorder_minimum_fc + 
  -34.5287138545909*original_glszm_smallareaemphasis + 7.52847283555431*original_shape_elongation_lm + 24.8320833122873*original_shape_sphericity_mm + 
  217.495246919398*v455_fc + 38.9676918327534*v620_fc + -14.8691202157608*v810_mm + 0.0602888949136799*wavelethhh_firstorder_minimum_fc + 
  89.2495344791801*wavelethhh_glcm_clustershade_mm + 213.773098091994*wavelethhh_glcm_imc1_lm + -17.6276240728582*wavelethhh_glrlm_runvariance_mm + 
  0.0000000080719363555*wavelethhh_glszm_largeareahighgr + -8.38605622822001*wavelethhl_firstorder_mean_mm + 3.2364724806286*
  wavelethhl_glcm_clusterprominenc + 81.8360980927234*wavelethhl_glcm_correlation_mm + -167.384837720787*wavelethhl_glcm_imc1_mm + 
  -81.0820217266207*wavelethhl_glcm_imc1_tc + 621.763588160631*wavelethhl_gldm_smalldependencel + 632.411254057462*wavelethhl_gldm_smalldependence2 + 
  0.0710881207259484*wavelethhl_glrlm_longrunhighgray + -8.351738303974*wavelethhl_glszm_graylevelvarian + -0.0000040561045732148*
  wavelethhl_glszm_largearealowgra + 26.9670478158734*wavelethhl_glszm_smallareaemphas + 2.67589095757834*wavelethlh_firstorder_median_lm + 
  -0.0000000600164173229*wavelethlh_glszm_largeareahighgr + 1.86950561596052*wavelethlh_glszm_zoneentropy_tc + 0.429287840979061*
  wavelethll_firstorder_kurtosis_m + -3.3301283354265*wavelethll_firstorder_skewness_l + 0.00320049649204003*wavelethll_glszm_graylevelnonuni + 
  0.0000096137070879199*wavelethll_glszm_largearealowgra + 36.5045204583078*wavelethll_glszm_smallareaemphas + 0.0114133947661589*
  wavelethll_ngtdm_busyness_mm + -0.014209835899086*waveletlhh_firstorder_maximum_mm + 1.85250947419981*waveletlhh_firstorder_median_lm + 
  5.59512662546722*waveletlhh_glszm_smallareaemphas + 0.00854410262392001*waveletlhl_firstorder_minimum_tc + -4.60982515805346*
  waveletlhl_firstorder_skewness_f + 2.77392733677797*waveletlhl_firstorder_skewness_t + 0.434544097213904*waveletlhl_glcm_clustershade_fc + 
  2.37371532631983*waveletlhl_glszm_zoneentropy_lm + 2.19071943478082*waveletlhl_glszm_zoneentropy_mm + 0.00545600840256806*
  waveletllh_firstorder_minimum_fc + 23.6600207591023*waveletllh_glcm_correlation_mm + 59.9111630785163*waveletllh_glcm_imc1_mm + 
  -675.256556331641*waveletllh_gldm_smalldependencel + 4.98801409541456*waveletllh_glszm_zoneentropy_fc + -0.0029447507382415*
  waveletlll_glcm_clustershade_lm + 91.6163084067093*waveletlll_glcm_idn_fc + -0.0000923483577302275*waveletlll_gldm_largedependenceh + 
  -0.00251156764446676*waveletlll_glszm_graylevelnonuni + -0.127240045441525*waveletlll_glszm_graylevelvarian + 0.24205064244792*
  waveletlll_ngtdm_busyness_tc)))));
val_max = __itype1_Case_;
IF (not missing(val_max) AND (missing(acc_max) OR val_max > acc_max)) THEN DO;
  idx_max = 1;
  acc_max = val_max;
END;
val_max = __itype1_Control_;
IF (not missing(val_max) AND (missing(acc_max) OR val_max > acc_max)) THEN DO;
  idx_max = 2;
  acc_max = val_max;
END;

__itype1__1 = 
 SELECT (idx_max)
  WHEN (1) 'Case'
  WHEN (2) 'Control'
  OTHERWISE ''
 END
;
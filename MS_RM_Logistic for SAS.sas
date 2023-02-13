﻿/* 
 * SAS code generated by JMP v16.2.0
 * From the following model(s): 
 *   拟合名义型 Logistic - itype1
 * Variable name mapping: 
 *   Lin[Control] => Lin_Control_
 *   Prob[Case] => Prob_Case_
 *   Prob[Control] => Prob_Control_
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
 */
DECLARE int idx_max;
DECLARE double val_max;
DECLARE double acc_max;
idx_max = 0;
acc_max = .;

Lin_Control_ = 139.063307307109 + -0.0375375058236927*original_firstorder_minimum_fc + 30.1305459902407*original_glszm_smallareaemphasis + 
  -5.17171374967425*original_shape_elongation_lm + -22.628924144954*original_shape_sphericity_mm + -183.420385655495*v455_fc + 
  -31.3312684285548*v620_fc + 13.0992317650441*v810_mm + -0.0449927285119966*wavelethhh_firstorder_minimum_fc + -80.6126275103369*
  wavelethhh_glcm_clustershade_mm + -175.668834756151*wavelethhh_glcm_imc1_lm + 14.1554437543005*wavelethhh_glrlm_runvariance_mm + 
  -0.0000000065902705011*wavelethhh_glszm_largeareahighgr + 8.45187008427271*wavelethhl_firstorder_mean_mm + -2.51117441608486*
  wavelethhl_glcm_clusterprominenc + -70.5459140508903*wavelethhl_glcm_correlation_mm + 135.331231912644*wavelethhl_glcm_imc1_mm + 
  68.4181502822914*wavelethhl_glcm_imc1_tc + -581.704233452415*wavelethhl_gldm_smalldependencel + -635.035033535392*wavelethhl_gldm_smalldependence2 + 
  -0.072635465822395*wavelethhl_glrlm_longrunhighgray + 7.06528813212184*wavelethhl_glszm_graylevelvarian + 0.0000034111631823944*
  wavelethhl_glszm_largearealowgra + -23.7669673323275*wavelethhl_glszm_smallareaemphas + -2.46793938305455*wavelethlh_firstorder_median_lm + 
  0.0000000525523637457*wavelethlh_glszm_largeareahighgr + -1.61723183048599*wavelethlh_glszm_zoneentropy_tc + -0.316146251951614*
  wavelethll_firstorder_kurtosis_m + 2.7258700982166*wavelethll_firstorder_skewness_l + -0.00363526522397216*wavelethll_glszm_graylevelnonuni + 
  -0.0000108940674123602*wavelethll_glszm_largearealowgra + -34.6530768983916*wavelethll_glszm_smallareaemphas + -0.00623430072694499*
  wavelethll_ngtdm_busyness_mm + 0.012526519001378*waveletlhh_firstorder_maximum_mm + -1.64028698105191*waveletlhh_firstorder_median_lm + 
  -5.46359479661979*waveletlhh_glszm_smallareaemphas + -0.00913903040109286*waveletlhl_firstorder_minimum_tc + 3.83169686327823*
  waveletlhl_firstorder_skewness_f + -2.44183012541404*waveletlhl_firstorder_skewness_t + -0.271943462270141*waveletlhl_glcm_clustershade_fc + 
  -2.22250066849681*waveletlhl_glszm_zoneentropy_lm + -1.7335082222592*waveletlhl_glszm_zoneentropy_mm + -0.00495276405350047*
  waveletllh_firstorder_minimum_fc + -22.8109063799044*waveletllh_glcm_correlation_mm + -49.5476168994885*waveletllh_glcm_imc1_mm + 
  508.787193443226*waveletllh_gldm_smalldependencel + -4.27604784138928*waveletllh_glszm_zoneentropy_fc + 0.00258474806649526*
  waveletlll_glcm_clustershade_lm + -66.3147077572225*waveletlll_glcm_idn_fc + 0.0000155238629072697*waveletlll_gldm_largedependenceh + 
  0.0027879963430726*waveletlll_glszm_graylevelnonuni + 0.128677844112411*waveletlll_glszm_graylevelvarian + -0.237313019002244*
  waveletlll_ngtdm_busyness_tc;
Prob_Control_ = 1/(1 + Exp((-Lin_Control_)));
Prob_Case_ = 1/(1 + Exp(Lin_Control_));
val_max = Prob_Control_;
IF (not missing(val_max) AND (missing(acc_max) OR val_max > acc_max)) THEN DO;
  idx_max = 1;
  acc_max = val_max;
END;
val_max = Prob_Case_;
IF (not missing(val_max) AND (missing(acc_max) OR val_max > acc_max)) THEN DO;
  idx_max = 2;
  acc_max = val_max;
END;

__itype1__1 = 
  
 SELECT (idx_max)
  WHEN (1) 'Control'
  WHEN (2) 'Case'
  OTHERWISE ''
 END
;
drop Lin_Control_;
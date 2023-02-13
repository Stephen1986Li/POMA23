/* 
 * SAS code generated by JMP v16.2.0
 * From the following model(s): 
 *   Discriminant - itype1
 * Variable name mapping: 
 *   Pred itype1_1 => Pred_itype1_1
 *   Prob[Case] => Prob_Case_
 *   Prob[Control] => Prob_Control_
 *   SqDist0_1 => SqDist0_1
 *   SqDist[Case]_1 => SqDist_Case__1
 *   SqDist[Control]_1 => SqDist_Control__1
 *   v455_fc => v455_fc
 *   v810_mm => v810_mm
 *   wavelethhl_glcm_correlation_mm => wavelethhl_glcm_correlation_mm
 *   wavelethhl_glcm_imc1_tc => wavelethhl_glcm_imc1_tc
 *   wavelethhl_gldm_smalldependencel_mm => wavelethhl_gldm_smalldependencel
 *   wavelethhl_glrlm_longrunhighgray_mm => wavelethhl_glrlm_longrunhighgray
 *   wavelethhl_glszm_graylevelvarian_mm => wavelethhl_glszm_graylevelvarian
 *   wavelethhl_glszm_smallareaemphas_fc => wavelethhl_glszm_smallareaemphas
 *   wavelethlh_firstorder_median_lm => wavelethlh_firstorder_median_lm
 *   wavelethlh_glszm_largeareahighgr_tc => wavelethlh_glszm_largeareahighgr
 *   wavelethlh_glszm_zoneentropy_tc => wavelethlh_glszm_zoneentropy_tc
 *   waveletlhh_firstorder_median_lm => waveletlhh_firstorder_median_lm
 *   waveletlhl_firstorder_skewness_tc => waveletlhl_firstorder_skewness_t
 *   waveletlhl_glszm_zoneentropy_lm => waveletlhl_glszm_zoneentropy_lm
 *   waveletlll_glcm_clustershade_lm => waveletlll_glcm_clustershade_lm
 *   waveletlll_glcm_idn_fc => waveletlll_glcm_idn_fc
 */
DECLARE int idx_max;
DECLARE double val_max;
DECLARE double acc_max;
idx_max = 0;
acc_max = .;

SqDist0_1 = Unhandled operator: Vec Quadratic;
SqDist_Case__1 = 46518.2654533753 + SqDist0_1 + -140727.93296277*v455_fc + 
  1781.1180526132*v810_mm + -10677.7808817774*wavelethhl_glcm_correlation_mm + 21129.8337954755*wavelethhl_glcm_imc1_tc + 70467.0496898792*
  wavelethhl_gldm_smalldependencel + 10.5269388379892*wavelethhl_glrlm_longrunhighgray + -23.8456581287552*wavelethhl_glszm_graylevelvarian + 
  -6054.72028436839*wavelethhl_glszm_smallareaemphas + 196.038744547905*wavelethlh_firstorder_median_lm + -0.0000024081994623117*
  wavelethlh_glszm_largeareahighgr + -392.336186216467*wavelethlh_glszm_zoneentropy_tc + -299.434599890548*waveletlhh_firstorder_median_lm + 
  -211.31077669668*waveletlhl_firstorder_skewness_t + -743.183157980846*waveletlhl_glszm_zoneentropy_lm + 0.803382800994478*
  waveletlll_glcm_clustershade_lm + -80372.8306970031*waveletlll_glcm_idn_fc;
SqDist_Control__1 = 46353.7669430051 + SqDist0_1 + 
  -140506.98376066*v455_fc + 1743.69821791699*v810_mm + -10581.7780401271*wavelethhl_glcm_correlation_mm + 21036.5633429013*
  wavelethhl_glcm_imc1_tc + 71465.2142195974*wavelethhl_gldm_smalldependencel + 10.636922258777*wavelethhl_glrlm_longrunhighgray + 
  -32.0692331605877*wavelethhl_glszm_graylevelvarian + -6018.10697052979*wavelethhl_glszm_smallareaemphas + 202.352070357849*
  wavelethlh_firstorder_median_lm + -0.000002497737529154*wavelethlh_glszm_largeareahighgr + -390.430291457254*wavelethlh_glszm_zoneentropy_tc + 
  -296.79919177225*waveletlhh_firstorder_median_lm + -205.837340742549*waveletlhl_firstorder_skewness_t + -740.347435077053*
  waveletlhl_glszm_zoneentropy_lm + 0.797873252077264*waveletlll_glcm_clustershade_lm + -80239.4291850222*waveletlll_glcm_idn_fc;
Prob_Case_ = 
  1/(1 + Exp((0.5*SqDist_Case__1 + -0.5*SqDist_Control__1)));
Prob_Control_ = 1/(1 + Exp((-0.5*SqDist_Case__1 + 0.5*SqDist_Control__1)));
val_max = Prob_Case_;
IF (not missing(val_max) AND (missing(acc_max) OR val_max > acc_max)) THEN DO;
  idx_max = 1;
  acc_max = val_max;
END;
val_max = Prob_Control_;
IF (not missing(val_max) AND (missing(acc_max) OR val_max > acc_max)) THEN DO;
  idx_max = 2;
  acc_max = val_max;
END;

Pred_itype1_1 = 
  
 SELECT (idx_max)
  WHEN (1) 'Case'
  WHEN (2) 'Control'
  OTHERWISE ''
 END
;
drop SqDist0_1 SqDist_Case__1 SqDist_Control__1;
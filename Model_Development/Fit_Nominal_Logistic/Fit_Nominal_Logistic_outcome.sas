/* 
 * SAS code generated by JMP v16.2.0
 * From the following model(s): 
 *   Fit Nominal Logistic - itype1
 * Variable name mapping: 
 *   Lin[Control]_1 => Lin_Control__1
 *   Most Likely itype1,!Most Likely itype1 => Most_Likely_itype1_Most_Likely_
 *   Prob[Case] => Prob_Case_
 *   Prob[Case],!Prob[Case] => Prob_Case_Prob_Case_
 *   Prob[Control] => Prob_Control_
 *   Prob[Control],!Prob[Control] => Prob_Control_Prob_Control_
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
 *   wavelethll_firstorder_skewness_lm => wavelethll_firstorder_skewness_l
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

Lin_Control__1 = 67.8225584206322 + 17.9139066181218*v810_mm + -44.4484024147687*wavelethhl_glcm_correlation_mm + 37.1611631286306*
  wavelethhl_glcm_imc1_tc + -543.08691361572*wavelethhl_gldm_smalldependencel + -0.0605076619251482*wavelethhl_glrlm_longrunhighgray + 
  4.23079348309421*wavelethhl_glszm_graylevelvarian + -17.427377971716*wavelethhl_glszm_smallareaemphas + -3.3401829838497*
  wavelethlh_firstorder_median_lm + 0.0000000600668512722*wavelethlh_glszm_largeareahighgr + -1.00398340579847*wavelethlh_glszm_zoneentropy_tc + 
  1.25412905444842*wavelethll_firstorder_skewness_l + -1.35301244832444*waveletlhh_firstorder_median_lm + -2.49611308125717*
  waveletlhl_firstorder_skewness_t + -1.29104858312071*waveletlhl_glszm_zoneentropy_lm + 0.00279307501761915*waveletlll_glcm_clustershade_lm + 
  -59.8246992075537*waveletlll_glcm_idn_fc;
Prob_Control_Prob_Control_ = 1/(1 + Exp((-Lin_Control__1)));
Prob_Case_Prob_Case_ = 
  1/(1 + Exp(Lin_Control__1));
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

Most_Likely_itype1_Most_Likely_ = 
 SELECT (idx_max)
  WHEN (1) 'Control'
  WHEN (2) 'Case'
  OTHERWISE ''
 END
;
drop Lin_Control__1;

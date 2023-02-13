#include "jmp_score.h"
#include "jmp_lib.h"


/* ==================================================================
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
 ================================================================== */

/* C code generated by JMP v16.2.0 */

JMP_SCORE_API void fillMetadataCounts(COUNTS *mc) {
	mc->creatorLen       = 21;
	mc->modelNameLen     = 1;
	mc->predictedLen     = 7;
	mc->tableNameLen     = 17;
	mc->versionLen       = 7;
	mc->timestampLen     = 21;
	mc->maxInputNameLen  = 36;
	mc->maxOutputNameLen = 39;
	mc->numInputs        = 18;
	mc->numOutputs       = 3;
}

JMP_SCORE_API void fillModelMetadata(MODELMD *mm) {
	strcpy_safe(mm->creator,   "Fit Nominal Logistic"); 
	strcpy_safe(mm->modelName, ""); 
	strcpy_safe(mm->predicted, "itype1"); 
	strcpy_safe(mm->tableName, "final-2022-11-18"); 
	strcpy_safe(mm->version,   "16.2.0");
    strcpy_safe(mm->timestamp, "2023-02-13T04:52:38Z");
}

JMP_SCORE_API void fillInputMetadata(FIELDMD *fd) {
    strcpy_safe(fd[0].name, "v810_mm");
    fd[0].type = fnum_type;
    fd[0].datalen = 0;        

    strcpy_safe(fd[1].name, "wavelethhl_glcm_correlation_mm");
    fd[1].type = fnum_type;
    fd[1].datalen = 0;        

    strcpy_safe(fd[2].name, "wavelethhl_glcm_imc1_tc");
    fd[2].type = fnum_type;
    fd[2].datalen = 0;        

    strcpy_safe(fd[3].name, "wavelethhl_gldm_smalldependencel_mm");
    fd[3].type = fnum_type;
    fd[3].datalen = 0;        

    strcpy_safe(fd[4].name, "wavelethhl_glrlm_longrunhighgray_mm");
    fd[4].type = fnum_type;
    fd[4].datalen = 0;        

    strcpy_safe(fd[5].name, "wavelethhl_glszm_graylevelvarian_mm");
    fd[5].type = fnum_type;
    fd[5].datalen = 0;        

    strcpy_safe(fd[6].name, "wavelethhl_glszm_smallareaemphas_fc");
    fd[6].type = fnum_type;
    fd[6].datalen = 0;        

    strcpy_safe(fd[7].name, "wavelethlh_firstorder_median_lm");
    fd[7].type = fnum_type;
    fd[7].datalen = 0;        

    strcpy_safe(fd[8].name, "wavelethlh_glszm_largeareahighgr_tc");
    fd[8].type = fnum_type;
    fd[8].datalen = 0;        

    strcpy_safe(fd[9].name, "wavelethlh_glszm_zoneentropy_tc");
    fd[9].type = fnum_type;
    fd[9].datalen = 0;        

    strcpy_safe(fd[10].name, "wavelethll_firstorder_skewness_lm");
    fd[10].type = fnum_type;
    fd[10].datalen = 0;        

    strcpy_safe(fd[11].name, "waveletlhh_firstorder_median_lm");
    fd[11].type = fnum_type;
    fd[11].datalen = 0;        

    strcpy_safe(fd[12].name, "waveletlhl_firstorder_skewness_tc");
    fd[12].type = fnum_type;
    fd[12].datalen = 0;        

    strcpy_safe(fd[13].name, "waveletlhl_glszm_zoneentropy_lm");
    fd[13].type = fnum_type;
    fd[13].datalen = 0;        

    strcpy_safe(fd[14].name, "waveletlll_glcm_clustershade_lm");
    fd[14].type = fnum_type;
    fd[14].datalen = 0;        

    strcpy_safe(fd[15].name, "waveletlll_glcm_idn_fc");
    fd[15].type = fnum_type;
    fd[15].datalen = 0;        

    strcpy_safe(fd[16].name, "Prob[Control]");
    fd[16].type = fnum_type;
    fd[16].datalen = 0;        

    strcpy_safe(fd[17].name, "Prob[Case]");
    fd[17].type = fnum_type;
    fd[17].datalen = 0;        
}

JMP_SCORE_API void fillOutputMetadata(FIELDMD *fd) {
    strcpy_safe(fd[0].name, "Prob[Control],!Prob[Control]");
    fd[0].type = fnum_type;
    fd[0].datalen = 0;        

    strcpy_safe(fd[1].name, "Prob[Case],!Prob[Case]");
    fd[1].type = fnum_type;
    fd[1].datalen = 0;        

    strcpy_safe(fd[2].name, "Most Likely itype1,!Most Likely itype1");
    fd[2].type = char_type;
    fd[2].datalen = 8;        
}

// Original name was: 'v810_mm'
#define V810_MM                             indata[0].data.fnum
// Original name was: 'wavelethhl_glcm_correlation_mm'
#define WAVELETHHL_GLCM_CORRELATION_MM      indata[1].data.fnum
// Original name was: 'wavelethhl_glcm_imc1_tc'
#define WAVELETHHL_GLCM_IMC1_TC             indata[2].data.fnum
// Original name was: 'wavelethhl_gldm_smalldependencel_mm'
#define WAVELETHHL_GLDM_SMALLDEPENDENCEL_MM indata[3].data.fnum
// Original name was: 'wavelethhl_glrlm_longrunhighgray_mm'
#define WAVELETHHL_GLRLM_LONGRUNHIGHGRAY_MM indata[4].data.fnum
// Original name was: 'wavelethhl_glszm_graylevelvarian_mm'
#define WAVELETHHL_GLSZM_GRAYLEVELVARIAN_MM indata[5].data.fnum
// Original name was: 'wavelethhl_glszm_smallareaemphas_fc'
#define WAVELETHHL_GLSZM_SMALLAREAEMPHAS_FC indata[6].data.fnum
// Original name was: 'wavelethlh_firstorder_median_lm'
#define WAVELETHLH_FIRSTORDER_MEDIAN_LM     indata[7].data.fnum
// Original name was: 'wavelethlh_glszm_largeareahighgr_tc'
#define WAVELETHLH_GLSZM_LARGEAREAHIGHGR_TC indata[8].data.fnum
// Original name was: 'wavelethlh_glszm_zoneentropy_tc'
#define WAVELETHLH_GLSZM_ZONEENTROPY_TC     indata[9].data.fnum
// Original name was: 'wavelethll_firstorder_skewness_lm'
#define WAVELETHLL_FIRSTORDER_SKEWNESS_LM   indata[10].data.fnum
// Original name was: 'waveletlhh_firstorder_median_lm'
#define WAVELETLHH_FIRSTORDER_MEDIAN_LM     indata[11].data.fnum
// Original name was: 'waveletlhl_firstorder_skewness_tc'
#define WAVELETLHL_FIRSTORDER_SKEWNESS_TC   indata[12].data.fnum
// Original name was: 'waveletlhl_glszm_zoneentropy_lm'
#define WAVELETLHL_GLSZM_ZONEENTROPY_LM     indata[13].data.fnum
// Original name was: 'waveletlll_glcm_clustershade_lm'
#define WAVELETLLL_GLCM_CLUSTERSHADE_LM     indata[14].data.fnum
// Original name was: 'waveletlll_glcm_idn_fc'
#define WAVELETLLL_GLCM_IDN_FC              indata[15].data.fnum
// Original name was: 'Prob[Control]'
#define PROB_CONTROL_                       indata[16].data.fnum
// Original name was: 'Prob[Case]'
#define PROB_CASE_                          indata[17].data.fnum

// Original name was: 'Prob[Control],!Prob[Control]'
#define PROB_CONTROL_PROB_CONTROL_             outdata[0].data.fnum
// Original name was: 'Prob[Case],!Prob[Case]'
#define PROB_CASE_PROB_CASE_                   outdata[1].data.fnum
// Original name was: 'Most Likely itype1,!Most Likely itype1'
#define MOST_LIKELY_ITYPE1_MOST_LIKELY_ITYPE1  outdata[2].data.str  // max string length: 7

JMP_SCORE_API void score(PARM *indata, PARM *outdata) {
    // Original name was: 'Lin[Control]_1'
    double Lin_Control__1;
    int _temp_0;
    double _temp_1[2];
    char * _temp_2 = "";

    Lin_Control__1 = 67.8225584206322 + 17.9139066181218 * V810_MM + -44.4484024147687 * WAVELETHHL_GLCM_CORRELATION_MM + 37.1611631286306 * WAVELETHHL_GLCM_IMC1_TC + -543.08691361572 * WAVELETHHL_GLDM_SMALLDEPENDENCEL_MM + -0.0605076619251482 * WAVELETHHL_GLRLM_LONGRUNHIGHGRAY_MM + 4.23079348309421 * WAVELETHHL_GLSZM_GRAYLEVELVARIAN_MM + -17.427377971716 * WAVELETHHL_GLSZM_SMALLAREAEMPHAS_FC + -3.3401829838497 * WAVELETHLH_FIRSTORDER_MEDIAN_LM + 0.0000000600668512722 * WAVELETHLH_GLSZM_LARGEAREAHIGHGR_TC + -1.00398340579847 * WAVELETHLH_GLSZM_ZONEENTROPY_TC + 1.25412905444842 * WAVELETHLL_FIRSTORDER_SKEWNESS_LM + -1.35301244832444 * WAVELETLHH_FIRSTORDER_MEDIAN_LM + -2.49611308125717 * WAVELETLHL_FIRSTORDER_SKEWNESS_TC + -1.29104858312071 * WAVELETLHL_GLSZM_ZONEENTROPY_LM + 0.00279307501761915 * WAVELETLLL_GLCM_CLUSTERSHADE_LM + -59.8246992075537 * WAVELETLLL_GLCM_IDN_FC;

    PROB_CONTROL_PROB_CONTROL_ = 1 / (1 + exp(-(Lin_Control__1)));

    PROB_CASE_PROB_CASE_ = 1 / (1 + exp(Lin_Control__1));

    _temp_1[0] = PROB_CONTROL_;
    _temp_1[1] = PROB_CASE_;
    _temp_0 = jmp_max_array(2, _temp_1);
    switch (_temp_0) {
        case 0: {
            _temp_2 = "Control";
        }
        break;
        case 1: {
            _temp_2 = "Case";
        }
        break;
        default: {
            _temp_2 = "";
        }
    }
    strcpy_safe(MOST_LIKELY_ITYPE1_MOST_LIKELY_ITYPE1, _temp_2);

}



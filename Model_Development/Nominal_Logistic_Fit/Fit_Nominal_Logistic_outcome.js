"use strict";

var jmp = require('./jmp_score.js');


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

/* JavaScript code generated by JMP v16.2.0 */
var getModelMetadata = function() {
	return {"creator": "Fit Nominal Logistic", "modelName": "", "predicted": "itype1", "table": "final-2022-11-18", "version": "16.2.0", "timestamp": "2023-02-13T04:54:50Z"};
};

var getInputMetadata = function() {
    return {
   "$schema": "http://json-schema.org/draft-04/schema#",
   "id": "/",
   "type": "object",
   "properties": {
     "original_firstorder_minimum_fc": {
       "id": "original_firstorder_minimum_fc",
       "type": "number"
     },
     "original_glszm_smallareaemphasis_fc": {
       "id": "original_glszm_smallareaemphasis_fc",
       "type": "number"
     },
     "original_shape_elongation_lm": {
       "id": "original_shape_elongation_lm",
       "type": "number"
     },
     "original_shape_sphericity_mm": {
       "id": "original_shape_sphericity_mm",
       "type": "number"
     },
     "v455_fc": {
       "id": "v455_fc",
       "type": "number"
     },
     "v620_fc": {
       "id": "v620_fc",
       "type": "number"
     },
     "v810_mm": {
       "id": "v810_mm",
       "type": "number"
     },
     "wavelethhh_firstorder_minimum_fc": {
       "id": "wavelethhh_firstorder_minimum_fc",
       "type": "number"
     },
     "wavelethhh_glcm_clustershade_mm": {
       "id": "wavelethhh_glcm_clustershade_mm",
       "type": "number"
     },
     "wavelethhh_glcm_imc1_lm": {
       "id": "wavelethhh_glcm_imc1_lm",
       "type": "number"
     },
     "wavelethhh_glrlm_runvariance_mm": {
       "id": "wavelethhh_glrlm_runvariance_mm",
       "type": "number"
     },
     "wavelethhh_glszm_largeareahighgr_fc": {
       "id": "wavelethhh_glszm_largeareahighgr_fc",
       "type": "number"
     },
     "wavelethhl_firstorder_mean_mm": {
       "id": "wavelethhl_firstorder_mean_mm",
       "type": "number"
     },
     "wavelethhl_glcm_clusterprominenc_fc": {
       "id": "wavelethhl_glcm_clusterprominenc_fc",
       "type": "number"
     },
     "wavelethhl_glcm_correlation_mm": {
       "id": "wavelethhl_glcm_correlation_mm",
       "type": "number"
     },
     "wavelethhl_glcm_imc1_mm": {
       "id": "wavelethhl_glcm_imc1_mm",
       "type": "number"
     },
     "wavelethhl_glcm_imc1_tc": {
       "id": "wavelethhl_glcm_imc1_tc",
       "type": "number"
     },
     "wavelethhl_gldm_smalldependencel_fc": {
       "id": "wavelethhl_gldm_smalldependencel_fc",
       "type": "number"
     },
     "wavelethhl_gldm_smalldependencel_mm": {
       "id": "wavelethhl_gldm_smalldependencel_mm",
       "type": "number"
     },
     "wavelethhl_glrlm_longrunhighgray_mm": {
       "id": "wavelethhl_glrlm_longrunhighgray_mm",
       "type": "number"
     },
     "wavelethhl_glszm_graylevelvarian_mm": {
       "id": "wavelethhl_glszm_graylevelvarian_mm",
       "type": "number"
     },
     "wavelethhl_glszm_largearealowgra_fc": {
       "id": "wavelethhl_glszm_largearealowgra_fc",
       "type": "number"
     },
     "wavelethhl_glszm_smallareaemphas_fc": {
       "id": "wavelethhl_glszm_smallareaemphas_fc",
       "type": "number"
     },
     "wavelethlh_firstorder_median_lm": {
       "id": "wavelethlh_firstorder_median_lm",
       "type": "number"
     },
     "wavelethlh_glszm_largeareahighgr_tc": {
       "id": "wavelethlh_glszm_largeareahighgr_tc",
       "type": "number"
     },
     "wavelethlh_glszm_zoneentropy_tc": {
       "id": "wavelethlh_glszm_zoneentropy_tc",
       "type": "number"
     },
     "wavelethll_firstorder_kurtosis_mm": {
       "id": "wavelethll_firstorder_kurtosis_mm",
       "type": "number"
     },
     "wavelethll_firstorder_skewness_lm": {
       "id": "wavelethll_firstorder_skewness_lm",
       "type": "number"
     },
     "wavelethll_glszm_graylevelnonuni_fc": {
       "id": "wavelethll_glszm_graylevelnonuni_fc",
       "type": "number"
     },
     "wavelethll_glszm_largearealowgra_lm": {
       "id": "wavelethll_glszm_largearealowgra_lm",
       "type": "number"
     },
     "wavelethll_glszm_smallareaemphas_fc": {
       "id": "wavelethll_glszm_smallareaemphas_fc",
       "type": "number"
     },
     "wavelethll_ngtdm_busyness_mm": {
       "id": "wavelethll_ngtdm_busyness_mm",
       "type": "number"
     },
     "waveletlhh_firstorder_maximum_mm": {
       "id": "waveletlhh_firstorder_maximum_mm",
       "type": "number"
     },
     "waveletlhh_firstorder_median_lm": {
       "id": "waveletlhh_firstorder_median_lm",
       "type": "number"
     },
     "waveletlhh_glszm_smallareaemphas_mm": {
       "id": "waveletlhh_glszm_smallareaemphas_mm",
       "type": "number"
     },
     "waveletlhl_firstorder_minimum_tc": {
       "id": "waveletlhl_firstorder_minimum_tc",
       "type": "number"
     },
     "waveletlhl_firstorder_skewness_fc": {
       "id": "waveletlhl_firstorder_skewness_fc",
       "type": "number"
     },
     "waveletlhl_firstorder_skewness_tc": {
       "id": "waveletlhl_firstorder_skewness_tc",
       "type": "number"
     },
     "waveletlhl_glcm_clustershade_fc": {
       "id": "waveletlhl_glcm_clustershade_fc",
       "type": "number"
     },
     "waveletlhl_glszm_zoneentropy_lm": {
       "id": "waveletlhl_glszm_zoneentropy_lm",
       "type": "number"
     },
     "waveletlhl_glszm_zoneentropy_mm": {
       "id": "waveletlhl_glszm_zoneentropy_mm",
       "type": "number"
     },
     "waveletllh_firstorder_minimum_fc": {
       "id": "waveletllh_firstorder_minimum_fc",
       "type": "number"
     },
     "waveletllh_glcm_correlation_mm": {
       "id": "waveletllh_glcm_correlation_mm",
       "type": "number"
     },
     "waveletllh_glcm_imc1_mm": {
       "id": "waveletllh_glcm_imc1_mm",
       "type": "number"
     },
     "waveletllh_gldm_smalldependencel_mm": {
       "id": "waveletllh_gldm_smalldependencel_mm",
       "type": "number"
     },
     "waveletllh_glszm_zoneentropy_fc": {
       "id": "waveletllh_glszm_zoneentropy_fc",
       "type": "number"
     },
     "waveletlll_glcm_clustershade_lm": {
       "id": "waveletlll_glcm_clustershade_lm",
       "type": "number"
     },
     "waveletlll_glcm_idn_fc": {
       "id": "waveletlll_glcm_idn_fc",
       "type": "number"
     },
     "waveletlll_gldm_largedependenceh_lm": {
       "id": "waveletlll_gldm_largedependenceh_lm",
       "type": "number"
     },
     "waveletlll_glszm_graylevelnonuni_fc": {
       "id": "waveletlll_glszm_graylevelnonuni_fc",
       "type": "number"
     },
     "waveletlll_glszm_graylevelvarian_mm": {
       "id": "waveletlll_glszm_graylevelvarian_mm",
       "type": "number"
     },
     "waveletlll_ngtdm_busyness_tc": {
       "id": "waveletlll_ngtdm_busyness_tc",
       "type": "number"
     },
     "Prob[Control]": {
       "id": "Prob[Control]",
       "type": "number"
     },
     "Prob[Case]": {
       "id": "Prob[Case]",
       "type": "number"
     }   },
   "additionalProperties": false,
  };
};

var getOutputMetadata = function() {
    return {
   "$schema": "http://json-schema.org/draft-04/schema#",
   "id": "/",
   "type": "object",
   "properties": {
     "Prob[Control],!Prob[Control]": {
       "id": "Prob[Control],!Prob[Control]",
       "type": "number"
     },
     "Prob[Case],!Prob[Case]": {
       "id": "Prob[Case],!Prob[Case]",
       "type": "number"
     },
     "Most Likely itype1,!Most Likely itype1": {
       "id": "Most Likely itype1,!Most Likely itype1",
       "type": "string"
     }   },
   "additionalProperties": false,
  };
};

var score = function(indata, outdata) {
    // Original name was: 'Lin[Control]_1'
    var Lin_Control__1;
    var _temp_0;
    var _temp_1 = [];
    var _temp_2 = "";

    Lin_Control__1 = 139.063307307109 + -0.0375375058236927 * indata["original_firstorder_minimum_fc"] + 30.1305459902407 * indata["original_glszm_smallareaemphasis_fc"] + -5.17171374967425 * indata["original_shape_elongation_lm"] + -22.628924144954 * indata["original_shape_sphericity_mm"] + -183.420385655495 * indata["v455_fc"] + -31.3312684285548 * indata["v620_fc"] + 13.0992317650441 * indata["v810_mm"] + -0.0449927285119966 * indata["wavelethhh_firstorder_minimum_fc"] + -80.6126275103369 * indata["wavelethhh_glcm_clustershade_mm"] + -175.668834756151 * indata["wavelethhh_glcm_imc1_lm"] + 14.1554437543005 * indata["wavelethhh_glrlm_runvariance_mm"] + -0.0000000065902705011 * indata["wavelethhh_glszm_largeareahighgr_fc"] + 8.45187008427271 * indata["wavelethhl_firstorder_mean_mm"] + -2.51117441608486 * indata["wavelethhl_glcm_clusterprominenc_fc"] + -70.5459140508903 * indata["wavelethhl_glcm_correlation_mm"] + 135.331231912644 * indata["wavelethhl_glcm_imc1_mm"] + 68.4181502822914 * indata["wavelethhl_glcm_imc1_tc"] + -581.704233452415 * indata["wavelethhl_gldm_smalldependencel_fc"] + -635.035033535392 * indata["wavelethhl_gldm_smalldependencel_mm"] + -0.072635465822395 * indata["wavelethhl_glrlm_longrunhighgray_mm"] + 7.06528813212184 * indata["wavelethhl_glszm_graylevelvarian_mm"] + 0.0000034111631823944 * indata["wavelethhl_glszm_largearealowgra_fc"] + -23.7669673323275 * indata["wavelethhl_glszm_smallareaemphas_fc"] + -2.46793938305455 * indata["wavelethlh_firstorder_median_lm"] + 0.0000000525523637457 * indata["wavelethlh_glszm_largeareahighgr_tc"] + -1.61723183048599 * indata["wavelethlh_glszm_zoneentropy_tc"] + -0.316146251951614 * indata["wavelethll_firstorder_kurtosis_mm"] + 2.7258700982166 * indata["wavelethll_firstorder_skewness_lm"] + -0.00363526522397216 * indata["wavelethll_glszm_graylevelnonuni_fc"] + -0.0000108940674123602 * indata["wavelethll_glszm_largearealowgra_lm"] + -34.6530768983916 * indata["wavelethll_glszm_smallareaemphas_fc"] + -0.00623430072694499 * indata["wavelethll_ngtdm_busyness_mm"] + 0.012526519001378 * indata["waveletlhh_firstorder_maximum_mm"] + -1.64028698105191 * indata["waveletlhh_firstorder_median_lm"] + -5.46359479661979 * indata["waveletlhh_glszm_smallareaemphas_mm"] + -0.00913903040109286 * indata["waveletlhl_firstorder_minimum_tc"] + 3.83169686327823 * indata["waveletlhl_firstorder_skewness_fc"] + -2.44183012541404 * indata["waveletlhl_firstorder_skewness_tc"] + -0.271943462270141 * indata["waveletlhl_glcm_clustershade_fc"] + -2.22250066849681 * indata["waveletlhl_glszm_zoneentropy_lm"] + -1.7335082222592 * indata["waveletlhl_glszm_zoneentropy_mm"] + -0.00495276405350047 * indata["waveletllh_firstorder_minimum_fc"] + -22.8109063799044 * indata["waveletllh_glcm_correlation_mm"] + -49.5476168994885 * indata["waveletllh_glcm_imc1_mm"] + 508.787193443226 * indata["waveletllh_gldm_smalldependencel_mm"] + -4.27604784138928 * indata["waveletllh_glszm_zoneentropy_fc"] + 0.00258474806649526 * indata["waveletlll_glcm_clustershade_lm"] + -66.3147077572225 * indata["waveletlll_glcm_idn_fc"] + 0.0000155238629072697 * indata["waveletlll_gldm_largedependenceh_lm"] + 0.0027879963430726 * indata["waveletlll_glszm_graylevelnonuni_fc"] + 0.128677844112411 * indata["waveletlll_glszm_graylevelvarian_mm"] + -0.237313019002244 * indata["waveletlll_ngtdm_busyness_tc"];

    outdata["Prob[Control],!Prob[Control]"] = 1 / (1 + Math.exp(-(Lin_Control__1)));

    outdata["Prob[Case],!Prob[Case]"] = 1 / (1 + Math.exp(Lin_Control__1));

    _temp_1[0] = indata["Prob[Control]"];
    _temp_1[1] = indata["Prob[Case]"];
    _temp_0 = jmp.max_array(2, _temp_1);
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
    outdata["Most Likely itype1,!Most Likely itype1"] = _temp_2;

    return outdata["Most Likely itype1,!Most Likely itype1"];
};


module.exports = {
  getInputMetadata: getInputMetadata,
  getOutputMetadata : getOutputMetadata,
  getModelMetadata : getModelMetadata,
  score : score
};




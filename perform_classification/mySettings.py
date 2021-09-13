#!/usr/bin/env pythonhttp://localhost:8888/edit/2020_MRI_Work/Radiogenomics/perform_classification/mySettings.py#
# coding: utf-8
import pandas as pd
import os

#========================================
# - "experiment_class": {"BraTS2021",  "TCGA_IDH",  "TCGA_MGMT"}, used to control different datasets for experiments.
# - "task_name_list": list some tasks in the specified "experiment_class", if it is a empty list, 
#                     then all the tasks in this experiment_class will be done!
# - "features_for_TCGA": {"extracted_features", "public_features"}, use public features from TCIA, or use features extracted by myself.
# - "feature_filter_dict": used to control the settings to filter the features for classification.
#                     - "modality_list": ["t1", "t1ce", "t1Gd", "t2", "flair"];
#                     - "imageType_list": ["original", "gradient", "log-sigma-1-0-mm-3D", "log-sigma-3-0-mm-3D",
#                         "square", "squareroot", "logarithm", "exponential", "lbp-3D-m2", "lbp-3D-m1", "lbp-3D-k"],
#                     - "tumor_subregion_list": ["NCR", "ED", "ET", "TC", "wholeTumor"]
# - "feature_selection_method": {"RFECV","RFE", AnovaTest, SelectFromModel}
#                     Note that: AnovaTest is very fast and effective.
# - "harmonization_method": {"withoutComBat", "parametric_ComBat", "nonParametric_ComBat, "noEB_ComBat"}
# - "harmonization_label": {"Tissue.source.site", "is_3T"}, column name of the setting label used to do the harmonization.
# - "random_seed": int number, used for reproducibility of the results.

'''
Basic Settings for the code
'''
global_basic_settings={
    "experiment_class": "TCGA_IDH",  
    "task_list": [], 
    "features_for_TCGA": "extracted_features",  
    "feature_filter_dict":{"modality_list": ["t1", "t1ce", "t1Gd", "t2", "flair"], 
                         "imageType_list": ["gradient"],      
                         "tumor_subregion_list": ["NCR", "ED", "ET", "TC", "wholeTumor"],
                        },
    "feature_selection_method":"AnovaTest",  
    "harmonization_method": "withoutComBat",  
    "harmonization_label": "is_3T",     
    "random_seed": 2021,
}


def get_basic_settings():
   
    return global_basic_settings



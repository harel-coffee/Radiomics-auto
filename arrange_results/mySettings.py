#!/usr/bin/env python
# coding: utf-8

import os

#=================  used for "main_arrange_results.ipynb" ==================
def get_arrange_results_settings_dict():
    """
    Settings used to arrange and plot the results;
    """
    basepath="G://PhDProjects/RadiogenomicsProjects/GliomasSubtypes/Results_randomseed2021"
    
    arrange_results_settings_dict={}

    #==================== 1: Compare the normalization method =====================
    arrange_results_settings_dict["compare_normalization_methods"]={
        "results_basepath": os.path.join(basepath, "1-compare_normalization_methods"),
        "groupby_column": "task",
        "plot_setting": {"x_column": "classifier", 
                         "hue_column": "normalization_method",
                         "rename_hue_values": {"no_normalization": "Without normalization", 
                                               "zscore": "With Z-Score"},
                         "ncol": 2,
                         "exclude_hue_value": ["fcm"]
                        }
    }
    
    
    #====================== 2: Compare different image feature extraction strategy ===================================
    arrange_results_settings_dict["compare_feature_strategy"]={
        "results_basepath": os.path.join(basepath, "2-compare_feature_strategy"),
        "groupby_column": "base_task",
        "plot_setting": {"x_column": "classifier", 
                         "hue_column": "task_additional_description",
                         "rename_hue_values": {"WT base": "WT base ", 
                                               "WT withSubregionInfo":"WT withIndicatorColumns ", 
                                               "NCR-TC-WT base":"NCR-TC-WT base", 
                                               "NCR-TC-WT withSubregionInfo": "NCR-TC-WT withIndicatorColumns", 
                                               "NCR-TC-WT-ED-ET base": "NCR-TC-WT-ED-ET base", 
                                               "NCR-TC-WT-ED-ET withSubregionInfo":"NCR-TC-WT-ED-ET withIndicatorColumns"},
                         "ncol": 3,
                         "exclude_hue_value": ["ShapeFeatureOnly base", "ShapeFeatureOnly withIndicatorColumns"]
                        }
    }
     
    #====================== 3: Compare different image filters ===================================
    arrange_results_settings_dict["compare_image_filter"]={
        "results_basepath": os.path.join(basepath, "3-compare_image_filter"),
        "groupby_column": "task",
        "plot_setting": {"x_column": "classifier", 
                         "hue_column": "image_filter",
                         "rename_hue_values": {"exponential": "Exponential", 
                                               "square": "Square", 
                                               "lbp-3D": "Local Binary Pattern",  
                                               "gradient": "Gradient", 
                                               "wavelet": "Wavelet", 
                                               "original": "Original", 
                                               "squareroot": "SquareRoot", 
                                               "logarithm": "Logarithm", 
                                               "log-sigma-1-0-mm-3D": "Laplacian of Gaussian"},
                         "ncol": 5,
                         "exclude_hue_value": ["log-sigma-3-0-mm-3D"]
                        }
    }
    
    #====================== 4: Compare whether to add clinical info (age and sex) ===================================
    arrange_results_settings_dict["compare_add_clinicalinfo"]={
        "results_basepath": os.path.join(basepath, "4-compare_add_clinicalinfo"),
        "groupby_column": "base_task",
        "plot_setting": {"x_column": "classifier", 
                         "hue_column": "task_additional_description",
                         "rename_hue_values":{" withSubregionInfo": "Without clinical info",
                                          " withAllInfo": "With clinical info"},
                         "ncol": 2,
                         "exclude_hue_value": []
                        }
    }
    return arrange_results_settings_dict





#================ used for "main_transform_binary-multiclass_classification.ipynb" ======================
"""
Settings for converting three binary classification results to one multiclass classification results;
"""
def get_convert_binary_to_multiclass_setting_dict():
    
    # base path
    base_dataPath="G://PhDProjects/RadiogenomicsProjects/GliomasSubtypes"
    image_filter="log-sigma-1-0-mm-3D"
    intensity_normalization="zscore"
    random_seed=0
    
    results_base_path= os.path.join(base_dataPath, "Results_randomseed"+str(random_seed), image_filter, "TCGA_IDH-extracted_features-"+intensity_normalization, "withoutComBat-IgnoreDataImbalance")
    
    convert_binary_to_multiclass_setting_dict={}
    
    convert_binary_to_multiclass_setting_dict["TCGA-IDH"]={
        # folders of the tasks.
        "binary_task_path_dict": {"is_GBM": os.path.join(results_base_path, "TCGA_1.103_isGBM_withSubregionInfo"),
                                  "is_IDH_mutant": os.path.join(results_base_path, "TCGA_2.103_isIDHMutant_withSubregionInfo"),
                                  "is_1p19q_codeleted": os.path.join(results_base_path, "TCGA_3.103_is1p19qCodeleted_withSubregionInfo")},
        # base path to save the results.
        "save_results_basepath": results_base_path, 
        # excel path which saves the ground truth labels;
        "ground_truth_target_excel_dict": {"train_data": os.path.join(base_dataPath, "Features", "final_metadata", intensity_normalization, "TCGA_extracted_features_IDH_train_resplited_randomseed_"+str(random_seed)+".xlsx"),
                                           "test_data": os.path.join(base_dataPath, "Features", "final_metadata", intensity_normalization, "TCGA_extracted_features_IDH_test_resplited_randomseed_"+str(random_seed)+".xlsx")
                                          }
                                           

    }
        
    return convert_binary_to_multiclass_setting_dict


# coding: utf-8

# IMPORTS
#import filecmp
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import XMLGenerator_Bandlist_core


# TESTS: XLSX_reader
# Bandlist Absorption & Raman: general info
def test_read_bandlist_general():
    # absorption
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/bandlist_general.xlsx", "ABS")  # all possible info is filled (the mega-full)
    # Bandlist
    assert verf_result[0]['BL_Import_mode'] == "first import"
    assert verf_result[1]['BL_Import_mode'] == ('C', 3, 3)
    assert verf_result[0]['BL_Type'] == "absorption"
    assert verf_result[1]['BL_Type'] == ('C', 4, 4)
    assert verf_result[0]['BL_Title'] == "C5"
    assert verf_result[1]['BL_Title'] == ('C', 5, 5)
    assert verf_result[0]['BL_Description'] == "C6"
    assert verf_result[1]['BL_Description'] == ('C', 6, 6)
    assert verf_result[0]['BL_Analysis'] == "C7"
    assert verf_result[1]['BL_Analysis'] == ('C', 7, 7)
    assert verf_result[0]['BL_Global_comments'] == "C8"
    assert verf_result[1]['BL_Global_comments'] == ('C', 8, 8)
    # files
    assert verf_result[0]['BL_Documentation_names'] == ['C9', 'C10', 'C11']
    assert verf_result[1]['BL_Documentation_names'] == ('C', 9, 11)
    assert verf_result[0]['BL_Documentation_files'] == ['E9', 'E10', 'E11']
    assert verf_result[1]['BL_Documentation_files'] == ('E', 9, 11)
    assert verf_result[0]['BL_Original_data_filename'] == 'bandlist_general.xlsx'
    assert verf_result[1]['BL_Original_data_filename'] == ('C', 12, 12)
    assert verf_result[0]['BL_Export_filename'] == 'C13'
    assert verf_result[1]['BL_Export_filename'] == ('C', 13, 13)
    # UID
    assert verf_result[0]['BL_UID'] == "A17"
    assert verf_result[1]['BL_UID'] == ('A', 17, 17)
    assert verf_result[0]['BL_Constituent_UID'] == "B17"
    assert verf_result[1]['BL_Constituent_UID'] == ('B', 17, 17)
    assert verf_result[0]['BL_Constituent_Primary_specie_UID'] == "C17"
    assert verf_result[1]['BL_Constituent_Primary_specie_UID'] == ('C', 17, 17)
    assert verf_result[0]['BL_Constituent_Comments'] == "D17"
    assert verf_result[1]['BL_Constituent_Comments'] == ('D', 17, 17)
    # Parents
    assert verf_result[0]['BL_Parents_Exp_UID'] == ['A25', 'A26', 'A27', 'A28']
    assert verf_result[1]['BL_Parents_Exp_UID'] == ('A', 25, 28)
    assert verf_result[0]['BL_Parents_Spectra_UID'] == ['B25', 'B26', 'B27', 'B28']
    assert verf_result[1]['BL_Parents_Spectra_UID'] == ('B', 25, 28)
    assert verf_result[0]['BL_Parents_Comments'] == "C25"
    assert verf_result[1]['BL_Parents_Comments'] == ('C', 25, 25)
    # Spectral
    assert verf_result[0]['BL_Spectral_Unit'] == "cm-1"
    assert verf_result[1]['BL_Spectral_Unit'] == ('A', 34, 34)
    assert verf_result[0]['BL_Spectral_Standard'] == "unknown"
    assert verf_result[1]['BL_Spectral_Standard'] == ('B', 34, 34)
    assert verf_result[0]['BL_Spectral_Range_types'] == ['FIR', 'MIR', 'soft X', 'hard X', 'UV', 'mm']
    assert verf_result[1]['BL_Spectral_Range_types'] == ('C', 34, 39)
    assert verf_result[0]['BL_Spectral_Range_min'] == ['50', '333', '555', '777']
    assert verf_result[1]['BL_Spectral_Range_min'] == ('D', 34, 37)
    assert verf_result[0]['BL_Spectral_Range_max'] == ['4600', '444', '666', '888']
    assert verf_result[1]['BL_Spectral_Range_max'] == ('E', 34, 37)
    assert verf_result[0]['BL_Spectral_Comments'] == "F34"
    assert verf_result[1]['BL_Spectral_Comments'] == ('F', 34, 34)
    assert verf_result[0]['BL_Spectral_Ref_pos_electronic'] == "111"
    assert verf_result[1]['BL_Spectral_Ref_pos_electronic'] == ('G', 34, 34)
    assert verf_result[0]['BL_Spectral_Ref_pos_absorption'] == "222"
    assert verf_result[1]['BL_Spectral_Ref_pos_absorption'] == ('H', 34, 34)
    # Validation
    assert verf_result[0]['BL_Validation_Quality'] == "5"
    assert verf_result[1]['BL_Validation_Quality'] == ('A', 44, 44)
    assert verf_result[0]['BL_Validation_Date_validated'] == "2021-08-16"
    assert verf_result[1]['BL_Validation_Date_validated'] == ('B', 44, 44)
    assert verf_result[0]['BL_Validation_Validators_UID'] == ['Bernard_Schmitt', 'B_S', 'B_F', 'F_B']
    assert verf_result[1]['BL_Validation_Validators_UID'] == ('C', 44, 47)
    # Versions
    assert verf_result[0]['BL_Versions_Current_version_history'] == "A53"
    assert verf_result[1]['BL_Versions_Current_version_history'] == ('A', 53, 53)
    assert verf_result[0]['BL_Versions_Previous_version_status'] == "partly invalidated version"
    assert verf_result[1]['BL_Versions_Previous_version_status'] == ('B', 53, 53)
    assert verf_result[0]['BL_Versions_Comments'] == "C53"
    assert verf_result[1]['BL_Versions_Comments'] == ('C', 53, 53)
    # Preview
    assert verf_result[0]['BL_Preview_x_Axis'] == "lin"
    assert verf_result[1]['BL_Preview_x_Axis'] == ('B', 57, 57)
    assert verf_result[0]['BL_Preview_x_Unit'] == "cm-1"
    assert verf_result[1]['BL_Preview_x_Unit'] == ('C', 57, 57)
    assert verf_result[0]['BL_Preview_x_Min'] == "0"
    assert verf_result[1]['BL_Preview_x_Min'] == ('D', 57, 57)
    assert verf_result[0]['BL_Preview_x_Max'] == "4700"
    assert verf_result[1]['BL_Preview_x_Max'] == ('E', 57, 57)
    assert verf_result[0]['BL_Preview_y_Axis'] == "log"
    assert verf_result[1]['BL_Preview_y_Axis'] == ('B', 58, 58)
    assert verf_result[0]['BL_Preview_y_Unit'] == "cm-1"
    assert verf_result[1]['BL_Preview_y_Unit'] == ('C', 58, 58)
    assert verf_result[0]['BL_Preview_y_Min'] == "11"
    assert verf_result[1]['BL_Preview_y_Min'] == ('D', 58, 58)
    assert verf_result[0]['BL_Preview_y_Max'] == "999"
    assert verf_result[1]['BL_Preview_y_Max'] == ('E', 58, 58)
    assert verf_result[0]['BL_Preview_y_rel_Axis'] == "lin"
    assert verf_result[1]['BL_Preview_y_rel_Axis'] == ('B', 59, 59)
    assert verf_result[0]['BL_Preview_y_rel_Min'] == "12"
    assert verf_result[1]['BL_Preview_y_rel_Min'] == ('D', 59, 59)
    assert verf_result[0]['BL_Preview_y_rel_Max'] == "457"
    assert verf_result[1]['BL_Preview_y_rel_Max'] == ('E', 59, 59)
    assert verf_result[0]['BL_Preview_Type'] == "relative"
    assert verf_result[1]['BL_Preview_Type'] == ('E', 60, 60)
    assert verf_result[0]['BL_Preview_Filename'] == "B60"
    assert verf_result[1]['BL_Preview_Filename'] == ('B', 60, 60)
    # Raman
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/bandlist_general.xlsx", "RAMAN")  # there are hols in data
    # Bandlist
    assert verf_result[0]['BL_Import_mode'] == "first import"
    assert verf_result[1]['BL_Import_mode'] == ('C', 3, 3)
    assert verf_result[0]['BL_Type'] == "Raman scattering"
    assert verf_result[1]['BL_Type'] == ('C', 4, 4)
    assert verf_result[0]['BL_Title'] == "C5"
    assert verf_result[1]['BL_Title'] == ('C', 5, 5)
    assert verf_result[0]['BL_Description'] == "C6"
    assert verf_result[1]['BL_Description'] == ('C', 6, 6)
    assert verf_result[0]['BL_Analysis'] == "C7"
    assert verf_result[1]['BL_Analysis'] == ('C', 7, 7)
    assert verf_result[0]['BL_Global_comments'] == "C8"
    assert verf_result[1]['BL_Global_comments'] == ('C', 8, 8)
    # files
    assert verf_result[0]['BL_Documentation_names'] == ['', 'C10', 'C11']
    assert verf_result[1]['BL_Documentation_names'] == ('C', 9, 11)
    assert verf_result[0]['BL_Documentation_files'] == ['E9', 'E10', '']
    assert verf_result[1]['BL_Documentation_files'] == ('E', 9, 11)
    assert verf_result[0]['BL_Original_data_filename'] == 'bandlist_general.xlsx'
    assert verf_result[1]['BL_Original_data_filename'] == ('C', 12, 12)
    assert verf_result[0]['BL_Export_filename'] == 'C13'
    assert verf_result[1]['BL_Export_filename'] == ('C', 13, 13)
    # UID
    assert verf_result[0]['BL_UID'] == "A17"
    assert verf_result[1]['BL_UID'] == ('A', 17, 17)
    assert verf_result[0]['BL_Constituent_UID'] == "B17"
    assert verf_result[1]['BL_Constituent_UID'] == ('B', 17, 17)
    assert verf_result[0]['BL_Constituent_Primary_specie_UID'] == "C17"
    assert verf_result[1]['BL_Constituent_Primary_specie_UID'] == ('C', 17, 17)
    assert verf_result[0]['BL_Constituent_Comments'] == "D17"
    assert verf_result[1]['BL_Constituent_Comments'] == ('D', 17, 17)
    # Parents
    assert verf_result[0]['BL_Parents_Exp_UID'] == ['', 'A26', 'A27', 'A28']
    assert verf_result[1]['BL_Parents_Exp_UID'] == ('A', 25, 28)
    assert verf_result[0]['BL_Parents_Spectra_UID'] == ['B25', 'B26', '', 'B28']
    assert verf_result[1]['BL_Parents_Spectra_UID'] == ('B', 25, 28)
    assert verf_result[0]['BL_Parents_Comments'] == "C25"
    assert verf_result[1]['BL_Parents_Comments'] == ('C', 25, 25)
    # Spectral
    assert verf_result[0]['BL_Spectral_Unit'] == "cm-1"
    assert verf_result[1]['BL_Spectral_Unit'] == ('A', 34, 34)
    assert verf_result[0]['BL_Spectral_Standard'] == "vacuum"
    assert verf_result[1]['BL_Spectral_Standard'] == ('B', 34, 34)
    assert verf_result[0]['BL_Spectral_Range_types'] == ['FIR', 'MIR']
    assert verf_result[1]['BL_Spectral_Range_types'] == ('C', 34, 39)
    assert verf_result[0]['BL_Spectral_Range_min'] == ['150', '', '13', '']
    assert verf_result[1]['BL_Spectral_Range_min'] == ('D', 34, 37)
    assert verf_result[0]['BL_Spectral_Range_max'] == ['3200', '', '5055', '']
    assert verf_result[1]['BL_Spectral_Range_max'] == ('E', 34, 37)
    assert verf_result[0]['BL_Spectral_Comments'] == "F34"
    assert verf_result[1]['BL_Spectral_Comments'] == ('F', 34, 34)
    assert verf_result[0]['BL_Spectral_Ref_pos_electronic'] == "111"
    assert verf_result[1]['BL_Spectral_Ref_pos_electronic'] == ('G', 34, 34)
    assert verf_result[0]['BL_Spectral_Ref_pos_absorption'] == "3203"
    assert verf_result[1]['BL_Spectral_Ref_pos_absorption'] == ('H', 34, 34)
    # Validation
    assert verf_result[0]['BL_Validation_Quality'] == "3"
    assert verf_result[1]['BL_Validation_Quality'] == ('A', 44, 44)
    assert verf_result[0]['BL_Validation_Date_validated'] == "2021-08-14"
    assert verf_result[1]['BL_Validation_Date_validated'] == ('B', 44, 44)
    assert verf_result[0]['BL_Validation_Validators_UID'] == ['Bernard_Schmitt']
    assert verf_result[1]['BL_Validation_Validators_UID'] == ('C', 44, 47)
    # Versions
    assert verf_result[0]['BL_Versions_Current_version_history'] == "A53"
    assert verf_result[1]['BL_Versions_Current_version_history'] == ('A', 53, 53)
    assert verf_result[0]['BL_Versions_Previous_version_status'] == "obsolete version"
    assert verf_result[1]['BL_Versions_Previous_version_status'] == ('B', 53, 53)
    assert verf_result[0]['BL_Versions_Comments'] == "C53"
    assert verf_result[1]['BL_Versions_Comments'] == ('C', 53, 53)
    # Preview
    assert verf_result[0]['BL_Preview_x_Axis'] == "lin"
    assert verf_result[1]['BL_Preview_x_Axis'] == ('B', 57, 57)
    assert verf_result[0]['BL_Preview_x_Unit'] == "cm-1"
    assert verf_result[1]['BL_Preview_x_Unit'] == ('C', 57, 57)
    assert verf_result[0]['BL_Preview_x_Min'] == "0"
    assert verf_result[1]['BL_Preview_x_Min'] == ('D', 57, 57)
    assert verf_result[0]['BL_Preview_x_Max'] == "3300"
    assert verf_result[1]['BL_Preview_x_Max'] == ('E', 57, 57)
    assert verf_result[0]['BL_Preview_y_Axis'] == "log"
    assert verf_result[1]['BL_Preview_y_Axis'] == ('B', 58, 58)
    assert verf_result[0]['BL_Preview_y_Unit'] == "cm-1"
    assert verf_result[1]['BL_Preview_y_Unit'] == ('C', 58, 58)
    assert verf_result[0]['BL_Preview_y_Min'] == "1"
    assert verf_result[1]['BL_Preview_y_Min'] == ('D', 58, 58)
    assert verf_result[0]['BL_Preview_y_Max'] == "5550"
    assert verf_result[1]['BL_Preview_y_Max'] == ('E', 58, 58)
    assert verf_result[0]['BL_Preview_y_rel_Axis'] == ""
    assert verf_result[1]['BL_Preview_y_rel_Axis'] == ('B', 59, 59)
    assert verf_result[0]['BL_Preview_y_rel_Min'] == ""
    assert verf_result[1]['BL_Preview_y_rel_Min'] == ('D', 59, 59)
    assert verf_result[0]['BL_Preview_y_rel_Max'] == ""
    assert verf_result[1]['BL_Preview_y_rel_Max'] == ('E', 59, 59)
    assert verf_result[0]['BL_Preview_Type'] == "abscoef"
    assert verf_result[1]['BL_Preview_Type'] == ('E', 60, 60)
    assert verf_result[0]['BL_Preview_Filename'] == "B60"
    assert verf_result[1]['BL_Preview_Filename'] == ('B', 60, 60)


# Bandlist Absorption & Raman: structure
def test_read_bandlist_structure():
    # absorption
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/bandlist_structure.xlsx", "ABS") # mega-full example
    # Structure
    assert verf_result[0]['BL_Sections_Var_param'] == "band transition category"
    assert verf_result[1]['BL_Sections_Var_param'] == ('C', 64, 64)
    assert verf_result[0]['BL_Sections_qty'] == 3
    # Section 1
    assert verf_result[0]['BL_Section_1_Var_param'] == "other"
    assert verf_result[1]['BL_Section_1_Var_param'] == ('C', 66, 66)
    assert verf_result[0]['BL_Section_1_Title'] == "B67"
    assert verf_result[1]['BL_Section_1_Title'] == ('B', 67, 67)
    assert verf_result[0]['BL_Section_1_Description'] == "B68"
    assert verf_result[1]['BL_Section_1_Description'] == ('B', 68, 68)
    assert verf_result[0]['BL_Section_1_Bands_UID'] == ["B69", "B70", "B71", "B72", "B73", "B74", "B75", "B76"]
    assert verf_result[1]['BL_Section_1_Bands_UID'] == ('B', 69, 76)
    assert verf_result[0]['BL_Section_1_Sub_sections_qty'] == 11
    # sub-section 1
    assert verf_result[0]['BL_Section_1_Sub_section_1_Title'] == "D67"
    assert verf_result[1]['BL_Section_1_Sub_section_1_Title'] == ('D', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_1_Description'] == "D68"
    assert verf_result[1]['BL_Section_1_Sub_section_1_Description'] == ('D', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_1_Bands_UID'] == ["D69", "D70", "D71", "D72", "D73", "D74", "D75", "D76"]
    assert verf_result[1]['BL_Section_1_Sub_section_1_Bands_UID'] == ('D', 69, 76)
    # sub-section 2
    assert verf_result[0]['BL_Section_1_Sub_section_2_Title'] == "E67"
    assert verf_result[1]['BL_Section_1_Sub_section_2_Title'] == ('E', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_2_Description'] == "E68"
    assert verf_result[1]['BL_Section_1_Sub_section_2_Description'] == ('E', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_2_Bands_UID'] == ["E69", "E70", "E71", "E72", "E73", "E74", "E75", "E76"]
    assert verf_result[1]['BL_Section_1_Sub_section_2_Bands_UID'] == ('E', 69, 76)
    # sub-section 3
    assert verf_result[0]['BL_Section_1_Sub_section_3_Title'] == "F67"
    assert verf_result[1]['BL_Section_1_Sub_section_3_Title'] == ('F', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_3_Description'] == "F68"
    assert verf_result[1]['BL_Section_1_Sub_section_3_Description'] == ('F', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_3_Bands_UID'] == ["F69", "F70", "F71", "F72", "F73", "F74", "F75", "F76"]
    assert verf_result[1]['BL_Section_1_Sub_section_3_Bands_UID'] == ('F', 69, 76)
    # sub-section 4
    assert verf_result[0]['BL_Section_1_Sub_section_4_Title'] == "G67"
    assert verf_result[1]['BL_Section_1_Sub_section_4_Title'] == ('G', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_4_Description'] == "G68"
    assert verf_result[1]['BL_Section_1_Sub_section_4_Description'] == ('G', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_4_Bands_UID'] == ["G69", "G70", "G71", "G72", "G73", "G74", "G75", "G76"]
    assert verf_result[1]['BL_Section_1_Sub_section_4_Bands_UID'] == ('G', 69, 76)
    # sub-section 5
    assert verf_result[0]['BL_Section_1_Sub_section_5_Title'] == "H67"
    assert verf_result[1]['BL_Section_1_Sub_section_5_Title'] == ('H', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_5_Description'] == "H68"
    assert verf_result[1]['BL_Section_1_Sub_section_5_Description'] == ('H', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_5_Bands_UID'] == ["H69", "H70", "H71", "H72", "H73", "H74", "H75", "H76"]
    assert verf_result[1]['BL_Section_1_Sub_section_5_Bands_UID'] == ('H', 69, 76)
    # sub-section 6
    assert verf_result[0]['BL_Section_1_Sub_section_6_Title'] == "I67"
    assert verf_result[1]['BL_Section_1_Sub_section_6_Title'] == ('I', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_6_Description'] == "I68"
    assert verf_result[1]['BL_Section_1_Sub_section_6_Description'] == ('I', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_6_Bands_UID'] == ["I69", "I70", "I71", "I72", "I73", "I74", "I75", "I76"]
    assert verf_result[1]['BL_Section_1_Sub_section_6_Bands_UID'] == ('I', 69, 76)
    # sub-section 7
    assert verf_result[0]['BL_Section_1_Sub_section_7_Title'] == "J67"
    assert verf_result[1]['BL_Section_1_Sub_section_7_Title'] == ('J', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_7_Description'] == "J68"
    assert verf_result[1]['BL_Section_1_Sub_section_7_Description'] == ('J', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_7_Bands_UID'] == ["J69", "J70", "J71", "J72", "J73", "J74", "J75", "J76"]
    assert verf_result[1]['BL_Section_1_Sub_section_7_Bands_UID'] == ('J', 69, 76)
    # sub-section 8
    assert verf_result[0]['BL_Section_1_Sub_section_8_Title'] == "K67"
    assert verf_result[1]['BL_Section_1_Sub_section_8_Title'] == ('K', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_8_Description'] == "K68"
    assert verf_result[1]['BL_Section_1_Sub_section_8_Description'] == ('K', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_8_Bands_UID'] == ["K69", "K70", "K71", "K72", "K73", "K74", "K75", "K76"]
    assert verf_result[1]['BL_Section_1_Sub_section_8_Bands_UID'] == ('K', 69, 76)
    # sub-section 9
    assert verf_result[0]['BL_Section_1_Sub_section_9_Title'] == "L67"
    assert verf_result[1]['BL_Section_1_Sub_section_9_Title'] == ('L', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_9_Description'] == "L68"
    assert verf_result[1]['BL_Section_1_Sub_section_9_Description'] == ('L', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_9_Bands_UID'] == ["L69", "L70", "L71", "L72", "L73", "L74", "L75", "L76"]
    assert verf_result[1]['BL_Section_1_Sub_section_9_Bands_UID'] == ('L', 69, 76)
    # sub-section 10
    assert verf_result[0]['BL_Section_1_Sub_section_10_Title'] == "M67"
    assert verf_result[1]['BL_Section_1_Sub_section_10_Title'] == ('M', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_10_Description'] == "M68"
    assert verf_result[1]['BL_Section_1_Sub_section_10_Description'] == ('M', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_10_Bands_UID'] == ["M69", "M70", "M71", "M72", "M73", "M74", "M75", "M76"]
    assert verf_result[1]['BL_Section_1_Sub_section_10_Bands_UID'] == ('M', 69, 76)
    # sub-section 11
    assert verf_result[0]['BL_Section_1_Sub_section_11_Title'] == "N67"
    assert verf_result[1]['BL_Section_1_Sub_section_11_Title'] == ('N', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_11_Description'] == "N68"
    assert verf_result[1]['BL_Section_1_Sub_section_11_Description'] == ('N', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_11_Bands_UID'] == ["N69", "N70", "N71", "N72", "N73", "N74", "N75", "N76"]
    assert verf_result[1]['BL_Section_1_Sub_section_11_Bands_UID'] == ('N', 69, 76)
    # Section 2
    assert verf_result[0]['BL_Section_2_Var_param'] == "no"
    assert verf_result[1]['BL_Section_2_Var_param'] == ('C', 78, 78)
    assert verf_result[0]['BL_Section_2_Title'] == "B67"
    assert verf_result[1]['BL_Section_2_Title'] == ('B', 79, 79)
    assert verf_result[0]['BL_Section_2_Description'] == "B68"
    assert verf_result[1]['BL_Section_2_Description'] == ('B', 80, 80)
    assert verf_result[0]['BL_Section_2_Bands_UID'] == ["B69", "B70", "B71", "B72", "B73", "B74", "B75", "B76"]
    assert verf_result[1]['BL_Section_2_Bands_UID'] == ('B', 81, 88)
    assert verf_result[0]['BL_Section_2_Sub_sections_qty'] == 0
    # Section 3
    assert verf_result[0]['BL_Section_3_Var_param'] == "isotope"
    assert verf_result[1]['BL_Section_3_Var_param'] == ('C', 92, 92)
    assert verf_result[0]['BL_Section_3_Title'] == "B67"
    assert verf_result[1]['BL_Section_3_Title'] == ('B', 93, 93)
    assert verf_result[0]['BL_Section_3_Description'] == "B68"
    assert verf_result[1]['BL_Section_3_Description'] == ('B', 94, 94)
    assert verf_result[0]['BL_Section_3_Bands_UID'] == ['']
    assert verf_result[1]['BL_Section_3_Bands_UID'] == ('', '', '')
    assert verf_result[0]['BL_Section_3_Sub_sections_qty'] == 3
    # sub-section 1
    assert verf_result[0]['BL_Section_3_Sub_section_1_Title'] == "D67"
    assert verf_result[1]['BL_Section_3_Sub_section_1_Title'] == ('D', 93, 93)
    assert verf_result[0]['BL_Section_3_Sub_section_1_Description'] == "D68"
    assert verf_result[1]['BL_Section_3_Sub_section_1_Description'] == ('D', 94, 94)
    assert verf_result[0]['BL_Section_3_Sub_section_1_Bands_UID'] == ["D69", "D70", "D71", "D72"]
    assert verf_result[1]['BL_Section_3_Sub_section_1_Bands_UID'] == ('D', 95, 98)
    # sub-section 2
    assert verf_result[0]['BL_Section_3_Sub_section_2_Title'] == "E67"
    assert verf_result[1]['BL_Section_3_Sub_section_2_Title'] == ('E', 93, 93)
    assert verf_result[0]['BL_Section_3_Sub_section_2_Description'] == "E68"
    assert verf_result[1]['BL_Section_3_Sub_section_2_Description'] == ('E', 94, 94)
    assert verf_result[0]['BL_Section_3_Sub_section_2_Bands_UID'] == ["E69", "E70", "E71", "E72", "E73"]
    assert verf_result[1]['BL_Section_3_Sub_section_2_Bands_UID'] == ('E', 95, 99)
    # sub-section 3
    assert verf_result[0]['BL_Section_3_Sub_section_3_Title'] == "F67"
    assert verf_result[1]['BL_Section_3_Sub_section_3_Title'] == ('F', 93, 93)
    assert verf_result[0]['BL_Section_3_Sub_section_3_Description'] == "F68"
    assert verf_result[1]['BL_Section_3_Sub_section_3_Description'] == ('F', 94, 94)
    assert verf_result[0]['BL_Section_3_Sub_section_3_Bands_UID'] == ["F69", "F70"]
    assert verf_result[1]['BL_Section_3_Sub_section_3_Bands_UID'] == ('F', 95, 96)
    # Raman
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/bandlist_structure.xlsx", "RAMAN")  # mega-full example
    # Structure
    assert verf_result[0]['BL_Sections_Var_param'] == "band transition category"
    assert verf_result[1]['BL_Sections_Var_param'] == ('C', 64, 64)
    assert verf_result[0]['BL_Sections_qty'] == 3
    # Section 1
    assert verf_result[0]['BL_Section_1_Var_param'] == "other"
    assert verf_result[1]['BL_Section_1_Var_param'] == ('C', 66, 66)
    assert verf_result[0]['BL_Section_1_Title'] == "B67"
    assert verf_result[1]['BL_Section_1_Title'] == ('B', 67, 67)
    assert verf_result[0]['BL_Section_1_Description'] == "B68"
    assert verf_result[1]['BL_Section_1_Description'] == ('B', 68, 68)
    assert verf_result[0]['BL_Section_1_Bands_UID'] == [""]
    assert verf_result[1]['BL_Section_1_Bands_UID'] == ('', '', '')
    assert verf_result[0]['BL_Section_1_Sub_sections_qty'] == 11
    # sub-section 1
    assert verf_result[0]['BL_Section_1_Sub_section_1_Title'] == "D67"
    assert verf_result[1]['BL_Section_1_Sub_section_1_Title'] == ('D', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_1_Description'] == "D68"
    assert verf_result[1]['BL_Section_1_Sub_section_1_Description'] == ('D', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_1_Bands_UID'] == ["D69", "D70", "D71", "D72", "D73", "D74", "D75", "D76"]
    assert verf_result[1]['BL_Section_1_Sub_section_1_Bands_UID'] == ('D', 69, 76)
    # sub-section 2
    assert verf_result[0]['BL_Section_1_Sub_section_2_Title'] == "E67"
    assert verf_result[1]['BL_Section_1_Sub_section_2_Title'] == ('E', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_2_Description'] == "E68"
    assert verf_result[1]['BL_Section_1_Sub_section_2_Description'] == ('E', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_2_Bands_UID'] == ["E69", "E70", "E71", "E72", "E73", "E74", "E75", "E76"]
    assert verf_result[1]['BL_Section_1_Sub_section_2_Bands_UID'] == ('E', 69, 76)
    # sub-section 3
    assert verf_result[0]['BL_Section_1_Sub_section_3_Title'] == "F67"
    assert verf_result[1]['BL_Section_1_Sub_section_3_Title'] == ('F', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_3_Description'] == "F68"
    assert verf_result[1]['BL_Section_1_Sub_section_3_Description'] == ('F', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_3_Bands_UID'] == ["F69", "F70", "F71", "F72", "F73", "F74", "F75", "F76"]
    assert verf_result[1]['BL_Section_1_Sub_section_3_Bands_UID'] == ('F', 69, 76)
    # sub-section 4
    assert verf_result[0]['BL_Section_1_Sub_section_4_Title'] == "G67"
    assert verf_result[1]['BL_Section_1_Sub_section_4_Title'] == ('G', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_4_Description'] == "G68"
    assert verf_result[1]['BL_Section_1_Sub_section_4_Description'] == ('G', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_4_Bands_UID'] == ["G69", "G70", "G71", "G72", "G73", "G74", "G75", "G76"]
    assert verf_result[1]['BL_Section_1_Sub_section_4_Bands_UID'] == ('G', 69, 76)
    # sub-section 5
    assert verf_result[0]['BL_Section_1_Sub_section_5_Title'] == "H67"
    assert verf_result[1]['BL_Section_1_Sub_section_5_Title'] == ('H', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_5_Description'] == "H68"
    assert verf_result[1]['BL_Section_1_Sub_section_5_Description'] == ('H', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_5_Bands_UID'] == ["H69", "H70", "H71", "H72", "H73", "H74", "H75", "H76"]
    assert verf_result[1]['BL_Section_1_Sub_section_5_Bands_UID'] == ('H', 69, 76)
    # sub-section 6
    assert verf_result[0]['BL_Section_1_Sub_section_6_Title'] == "I67"
    assert verf_result[1]['BL_Section_1_Sub_section_6_Title'] == ('I', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_6_Description'] == "I68"
    assert verf_result[1]['BL_Section_1_Sub_section_6_Description'] == ('I', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_6_Bands_UID'] == ["I69", "I70", "I71", "I72", "I73", "I74", "I75", "I76"]
    assert verf_result[1]['BL_Section_1_Sub_section_6_Bands_UID'] == ('I', 69, 76)
    # sub-section 7
    assert verf_result[0]['BL_Section_1_Sub_section_7_Title'] == "J67"
    assert verf_result[1]['BL_Section_1_Sub_section_7_Title'] == ('J', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_7_Description'] == "J68"
    assert verf_result[1]['BL_Section_1_Sub_section_7_Description'] == ('J', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_7_Bands_UID'] == ["J69", "J70", "J71", "J72", "J73", "J74", "J75", "J76"]
    assert verf_result[1]['BL_Section_1_Sub_section_7_Bands_UID'] == ('J', 69, 76)
    # sub-section 8
    assert verf_result[0]['BL_Section_1_Sub_section_8_Title'] == "K67"
    assert verf_result[1]['BL_Section_1_Sub_section_8_Title'] == ('K', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_8_Description'] == "K68"
    assert verf_result[1]['BL_Section_1_Sub_section_8_Description'] == ('K', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_8_Bands_UID'] == ["K69", "K70", "K71", "K72", "K73", "K74", "K75", "K76"]
    assert verf_result[1]['BL_Section_1_Sub_section_8_Bands_UID'] == ('K', 69, 76)
    # sub-section 9
    assert verf_result[0]['BL_Section_1_Sub_section_9_Title'] == "L67"
    assert verf_result[1]['BL_Section_1_Sub_section_9_Title'] == ('L', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_9_Description'] == "L68"
    assert verf_result[1]['BL_Section_1_Sub_section_9_Description'] == ('L', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_9_Bands_UID'] == ["L69", "L70", "L71", "L72", "L73", "L74", "L75", "L76"]
    assert verf_result[1]['BL_Section_1_Sub_section_9_Bands_UID'] == ('L', 69, 76)
    # sub-section 10
    assert verf_result[0]['BL_Section_1_Sub_section_10_Title'] == "M67"
    assert verf_result[1]['BL_Section_1_Sub_section_10_Title'] == ('M', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_10_Description'] == "M68"
    assert verf_result[1]['BL_Section_1_Sub_section_10_Description'] == ('M', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_10_Bands_UID'] == ["M69", "M70", "M71", "M72", "M73", "M74", "M75", "M76"]
    assert verf_result[1]['BL_Section_1_Sub_section_10_Bands_UID'] == ('M', 69, 76)
    # sub-section 11
    assert verf_result[0]['BL_Section_1_Sub_section_11_Title'] == "N67"
    assert verf_result[1]['BL_Section_1_Sub_section_11_Title'] == ('N', 67, 67)
    assert verf_result[0]['BL_Section_1_Sub_section_11_Description'] == "N68"
    assert verf_result[1]['BL_Section_1_Sub_section_11_Description'] == ('N', 68, 68)
    assert verf_result[0]['BL_Section_1_Sub_section_11_Bands_UID'] == ["N69", "N70", "N71", "N72", "N73", "N74", "N75", "N76"]
    assert verf_result[1]['BL_Section_1_Sub_section_11_Bands_UID'] == ('N', 69, 76)
    # Section 2
    assert verf_result[0]['BL_Section_2_Var_param'] == "no"
    assert verf_result[1]['BL_Section_2_Var_param'] == ('C', 78, 78)
    assert verf_result[0]['BL_Section_2_Title'] == "B67"
    assert verf_result[1]['BL_Section_2_Title'] == ('B', 79, 79)
    assert verf_result[0]['BL_Section_2_Description'] == "B68"
    assert verf_result[1]['BL_Section_2_Description'] == ('B', 80, 80)
    assert verf_result[0]['BL_Section_2_Bands_UID'] == ["B69", "B70", "B71", "B72", "B73", "B74", "B75", "B76"]
    assert verf_result[1]['BL_Section_2_Bands_UID'] == ('B', 81, 88)
    assert verf_result[0]['BL_Section_2_Sub_sections_qty'] == 0
    # Section 3
    assert verf_result[0]['BL_Section_3_Var_param'] == "isotope"
    assert verf_result[1]['BL_Section_3_Var_param'] == ('C', 92, 92)
    assert verf_result[0]['BL_Section_3_Title'] == "B67"
    assert verf_result[1]['BL_Section_3_Title'] == ('B', 93, 93)
    assert verf_result[0]['BL_Section_3_Description'] == "B68"
    assert verf_result[1]['BL_Section_3_Description'] == ('B', 94, 94)
    assert verf_result[0]['BL_Section_3_Bands_UID'] == ["B69", "B70", "B71", "B72", "B73", "B74", "B75", "B76"]
    assert verf_result[1]['BL_Section_3_Bands_UID'] == ('B', 95, 102)
    assert verf_result[0]['BL_Section_3_Sub_sections_qty'] == 3
    # sub-section 1
    assert verf_result[0]['BL_Section_3_Sub_section_1_Title'] == "D67"
    assert verf_result[1]['BL_Section_3_Sub_section_1_Title'] == ('D', 93, 93)
    assert verf_result[0]['BL_Section_3_Sub_section_1_Description'] == "D68"
    assert verf_result[1]['BL_Section_3_Sub_section_1_Description'] == ('D', 94, 94)
    assert verf_result[0]['BL_Section_3_Sub_section_1_Bands_UID'] == ["D69", "D70", "D71", "D72"]
    assert verf_result[1]['BL_Section_3_Sub_section_1_Bands_UID'] == ('D', 95, 98)
    # sub-section 2
    assert verf_result[0]['BL_Section_3_Sub_section_2_Title'] == "E67"
    assert verf_result[1]['BL_Section_3_Sub_section_2_Title'] == ('E', 93, 93)
    assert verf_result[0]['BL_Section_3_Sub_section_2_Description'] == "E68"
    assert verf_result[1]['BL_Section_3_Sub_section_2_Description'] == ('E', 94, 94)
    assert verf_result[0]['BL_Section_3_Sub_section_2_Bands_UID'] == ["E69", "E70", "E71", "E72", "E73"]
    assert verf_result[1]['BL_Section_3_Sub_section_2_Bands_UID'] == ('E', 95, 99)
    # sub-section 3
    assert verf_result[0]['BL_Section_3_Sub_section_3_Title'] == "F67"
    assert verf_result[1]['BL_Section_3_Sub_section_3_Title'] == ('F', 93, 93)
    assert verf_result[0]['BL_Section_3_Sub_section_3_Description'] == "F68"
    assert verf_result[1]['BL_Section_3_Sub_section_3_Description'] == ('F', 94, 94)
    assert verf_result[0]['BL_Section_3_Sub_section_3_Bands_UID'] == ["F69", "F70"]
    assert verf_result[1]['BL_Section_3_Sub_section_3_Bands_UID'] == ('F', 95, 96)

# Band general info
def test_read_band_general():
    # Raman
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_general.xlsx", "RAMAN") # mega-full example
    # Band general info
    assert verf_result[0]['B_qty'] == 8
    # band 1
    assert verf_result[0]['B_1_Index'] == "1"
    assert verf_result[1]['B_1_Index'] == ('A', 21, 21)
    assert verf_result[0]['B_1_Import_mode'] == "first import"
    assert verf_result[1]['B_1_Import_mode'] == ('B', 21, 21)
    assert verf_result[0]['B_1_UID'] == "94"
    assert verf_result[1]['B_1_UID'] == ('C', 21, 21)
    assert verf_result[0]['B_1_Comment'] == "E21"
    assert verf_result[1]['B_1_Comment'] == ('E', 21, 21)
    # band 2
    assert verf_result[0]['B_2_Index'] == "2"
    assert verf_result[1]['B_2_Index'] == ('A', 29, 29)
    assert verf_result[0]['B_2_Import_mode'] == "inherited"
    assert verf_result[1]['B_2_Import_mode'] == ('B', 29, 29)
    assert verf_result[0]['B_2_UID'] == "106"
    assert verf_result[1]['B_2_UID'] == ('C', 29, 29)
    assert verf_result[0]['B_2_Comment'] == "E29"
    assert verf_result[1]['B_2_Comment'] == ('E', 29, 29)
    # band 3
    assert verf_result[0]['B_3_Index'] == "3"
    assert verf_result[1]['B_3_Index'] == ('A', 43, 43)
    assert verf_result[0]['B_3_Import_mode'] == "no change"
    assert verf_result[1]['B_3_Import_mode'] == ('B', 43, 43)
    assert verf_result[0]['B_3_UID'] == "506"
    assert verf_result[1]['B_3_UID'] == ('C', 43, 43)
    assert verf_result[0]['B_3_Comment'] == "E43"
    assert verf_result[1]['B_3_Comment'] == ('E', 43, 43)
    # band 4
    assert verf_result[0]['B_4_Index'] == "4"
    assert verf_result[1]['B_4_Index'] == ('A', 36, 36)
    assert verf_result[0]['B_4_Import_mode'] == "correction"
    assert verf_result[1]['B_4_Import_mode'] == ('B', 36, 36)
    assert verf_result[0]['B_4_UID'] == "228"
    assert verf_result[1]['B_4_UID'] == ('C', 36, 36)
    assert verf_result[0]['B_4_Comment'] == "E36"
    assert verf_result[1]['B_4_Comment'] == ('E', 36, 36)
    # band 5
    assert verf_result[0]['B_5_Index'] == "5"
    assert verf_result[1]['B_5_Index'] == ('A', 49, 49)
    assert verf_result[0]['B_5_Import_mode'] == "ignore"
    assert verf_result[1]['B_5_Import_mode'] == ('B', 49, 49)
    assert verf_result[0]['B_5_UID'] == "760"
    assert verf_result[1]['B_5_UID'] == ('C', 49, 49)
    assert verf_result[0]['B_5_Comment'] == "E49"
    assert verf_result[1]['B_5_Comment'] == ('E', 49, 49)
    # band 6
    assert verf_result[0]['B_6_Index'] == "6"
    assert verf_result[1]['B_6_Index'] == ('A', 61, 61)
    assert verf_result[0]['B_6_Import_mode'] == "new version"
    assert verf_result[1]['B_6_Import_mode'] == ('B', 61, 61)
    assert verf_result[0]['B_6_UID'] == "999"
    assert verf_result[1]['B_6_UID'] == ('C', 61, 61)
    assert verf_result[0]['B_6_Comment'] == "E61"
    assert verf_result[1]['B_6_Comment'] == ('E', 61, 61)
    # band 7
    assert verf_result[0]['B_7_Index'] == "7"
    assert verf_result[1]['B_7_Index'] == ('A', 55, 55)
    assert verf_result[0]['B_7_Import_mode'] == "draft"
    assert verf_result[1]['B_7_Import_mode'] == ('B', 55, 55)
    assert verf_result[0]['B_7_UID'] == "883"
    assert verf_result[1]['B_7_UID'] == ('C', 55, 55)
    assert verf_result[0]['B_7_Comment'] == "E55"
    assert verf_result[1]['B_7_Comment'] == ('E', 55, 55)
    # band 8
    assert verf_result[0]['B_8_Index'] == "8"
    assert verf_result[1]['B_8_Index'] == ('A', 70, 70)
    assert verf_result[0]['B_8_Import_mode'] == "invalidate"
    assert verf_result[1]['B_8_Import_mode'] == ('B', 70, 70)
    assert verf_result[0]['B_8_UID'] == "1111"
    assert verf_result[1]['B_8_UID'] == ('C', 70, 70)
    assert verf_result[0]['B_8_Comment'] == "E70"
    assert verf_result[1]['B_8_Comment'] == ('E', 70, 70)
    # Absorption
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_general.xlsx", "ABS")  # mega-full example
    # Band general info
    assert verf_result[0]['B_qty'] == 8
    # band 1
    assert verf_result[0]['B_1_Index'] == "1"
    assert verf_result[1]['B_1_Index'] == ('A', 84, 84)
    assert verf_result[0]['B_1_Import_mode'] == "first import"
    assert verf_result[1]['B_1_Import_mode'] == ('B', 84, 84)
    assert verf_result[0]['B_1_UID'] == "94"
    assert verf_result[1]['B_1_UID'] == ('C', 84, 84)
    assert verf_result[0]['B_1_Comment'] == "E21"
    assert verf_result[1]['B_1_Comment'] == ('E', 84, 84)
    # band 2
    assert verf_result[0]['B_2_Index'] == "2"
    assert verf_result[1]['B_2_Index'] == ('A', 92, 92)
    assert verf_result[0]['B_2_Import_mode'] == "inherited"
    assert verf_result[1]['B_2_Import_mode'] == ('B', 92, 92)
    assert verf_result[0]['B_2_UID'] == "106"
    assert verf_result[1]['B_2_UID'] == ('C', 92, 92)
    assert verf_result[0]['B_2_Comment'] == "E29"
    assert verf_result[1]['B_2_Comment'] == ('E', 92, 92)
    # band 3
    assert verf_result[0]['B_3_Index'] == "3"
    assert verf_result[1]['B_3_Index'] == ('A', 106, 106)
    assert verf_result[0]['B_3_Import_mode'] == "no change"
    assert verf_result[1]['B_3_Import_mode'] == ('B', 106, 106)
    assert verf_result[0]['B_3_UID'] == "506"
    assert verf_result[1]['B_3_UID'] == ('C', 106, 106)
    assert verf_result[0]['B_3_Comment'] == "E43"
    assert verf_result[1]['B_3_Comment'] == ('E', 106, 106)
    # band 4
    assert verf_result[0]['B_4_Index'] == "4"
    assert verf_result[1]['B_4_Index'] == ('A', 99, 99)
    assert verf_result[0]['B_4_Import_mode'] == "correction"
    assert verf_result[1]['B_4_Import_mode'] == ('B', 99, 99)
    assert verf_result[0]['B_4_UID'] == "228"
    assert verf_result[1]['B_4_UID'] == ('C', 99, 99)
    assert verf_result[0]['B_4_Comment'] == "E36"
    assert verf_result[1]['B_4_Comment'] == ('E', 99, 99)
    # band 5
    assert verf_result[0]['B_5_Index'] == "5"
    assert verf_result[1]['B_5_Index'] == ('A', 112, 112)
    assert verf_result[0]['B_5_Import_mode'] == "ignore"
    assert verf_result[1]['B_5_Import_mode'] == ('B', 112, 112)
    assert verf_result[0]['B_5_UID'] == "760"
    assert verf_result[1]['B_5_UID'] == ('C', 112, 112)
    assert verf_result[0]['B_5_Comment'] == "E49"
    assert verf_result[1]['B_5_Comment'] == ('E', 112, 112)
    # band 6
    assert verf_result[0]['B_6_Index'] == "6"
    assert verf_result[1]['B_6_Index'] == ('A', 124, 124)
    assert verf_result[0]['B_6_Import_mode'] == "new version"
    assert verf_result[1]['B_6_Import_mode'] == ('B', 124, 124)
    assert verf_result[0]['B_6_UID'] == "999"
    assert verf_result[1]['B_6_UID'] == ('C', 124, 124)
    assert verf_result[0]['B_6_Comment'] == "E61"
    assert verf_result[1]['B_6_Comment'] == ('E', 124, 124)
    # band 7
    assert verf_result[0]['B_7_Index'] == "7"
    assert verf_result[1]['B_7_Index'] == ('A', 118, 118)
    assert verf_result[0]['B_7_Import_mode'] == "draft"
    assert verf_result[1]['B_7_Import_mode'] == ('B', 118, 118)
    assert verf_result[0]['B_7_UID'] == "883"
    assert verf_result[1]['B_7_UID'] == ('C', 118, 118)
    assert verf_result[0]['B_7_Comment'] == "E55"
    assert verf_result[1]['B_7_Comment'] == ('E', 118, 118)
    # band 8
    assert verf_result[0]['B_8_Index'] == "8"
    assert verf_result[1]['B_8_Index'] == ('A', 133, 133)
    assert verf_result[0]['B_8_Import_mode'] == "invalidate"
    assert verf_result[1]['B_8_Import_mode'] == ('B', 133, 133)
    assert verf_result[0]['B_8_UID'] == "1111"
    assert verf_result[1]['B_8_UID'] == ('C', 133, 133)
    assert verf_result[0]['B_8_Comment'] == "E70"
    assert verf_result[1]['B_8_Comment'] == ('E', 133, 133)


# Band Assignment
def test_read_band_assignment():
    # Raman
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_assignment_ram.xlsx", "RAMAN")
    # Band Assignment Qty
    assert verf_result[0]['B_1_Assignments_qty'] == 3
    assert verf_result[0]['B_2_Assignments_qty'] == 4
    assert verf_result[0]['B_3_Assignments_qty'] == 1
    # Band Assignment Number
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Number'] == '1'
    assert verf_result[1]['B_1_Assignment_1_Number'] == ('H', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Number'] == '2'
    assert verf_result[1]['B_1_Assignment_2_Number'] == ('H', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Number'] == '3'
    assert verf_result[1]['B_1_Assignment_3_Number'] == ('H', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Number'] == '1'
    assert verf_result[1]['B_2_Assignment_1_Number'] == ('H', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Number'] == '2'
    assert verf_result[1]['B_2_Assignment_2_Number'] == ('H', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Number'] == '3'
    assert verf_result[1]['B_2_Assignment_3_Number'] == ('H', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Number'] == '4'
    assert verf_result[1]['B_2_Assignment_4_Number'] == ('H', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Number'] == '1'
    assert verf_result[1]['B_3_Assignment_1_Number'] == ('H', 57, 57)
    # Band Assignment Label
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Label'] == 'I15'
    assert verf_result[1]['B_1_Assignment_1_Label'] == ('I', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Label'] == 'I27'
    assert verf_result[1]['B_1_Assignment_2_Label'] == ('I', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Label'] == 'I21'
    assert verf_result[1]['B_1_Assignment_3_Label'] == ('I', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Label'] == 'I51'
    assert verf_result[1]['B_2_Assignment_1_Label'] == ('I', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Label'] == 'I45'
    assert verf_result[1]['B_2_Assignment_2_Label'] == ('I', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Label'] == 'I39'
    assert verf_result[1]['B_2_Assignment_3_Label'] == ('I', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Label'] == 'I33'
    assert verf_result[1]['B_2_Assignment_4_Label'] == ('I', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Label'] == 'I57'
    assert verf_result[1]['B_3_Assignment_1_Label'] == ('I', 57, 57)
    # Band Assignment Symmetry
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Symmetry'] == 'E'
    assert verf_result[1]['B_1_Assignment_1_Symmetry'] == ('J', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Symmetry'] == 'E1'
    assert verf_result[1]['B_1_Assignment_2_Symmetry'] == ('J', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Symmetry'] == 'unknown'
    assert verf_result[1]['B_1_Assignment_3_Symmetry'] == ('J', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Symmetry'] == 'Au'
    assert verf_result[1]['B_2_Assignment_1_Symmetry'] == ('J', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Symmetry'] == 'A'
    assert verf_result[1]['B_2_Assignment_2_Symmetry'] == ('J', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Symmetry'] == 'NULL'
    assert verf_result[1]['B_2_Assignment_3_Symmetry'] == ('J', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Symmetry'] == 'Ag'
    assert verf_result[1]['B_2_Assignment_4_Symmetry'] == ('J', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Symmetry'] == 'A2g'
    assert verf_result[1]['B_3_Assignment_1_Symmetry'] == ('J', 57, 57)
    # Band Assignment Category
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Category'] == 'electronic transition'
    assert verf_result[1]['B_1_Assignment_1_Category'] == ('K', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Category'] == 'rotation'
    assert verf_result[1]['B_1_Assignment_2_Category'] == ('K', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Category'] == 'overtone vibration'
    assert verf_result[1]['B_1_Assignment_3_Category'] == ('K', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Category'] == 'combination'
    assert verf_result[1]['B_2_Assignment_1_Category'] == ('K', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Category'] == 'overtone rotation'
    assert verf_result[1]['B_2_Assignment_2_Category'] == ('K', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Category'] == 'unknown'
    assert verf_result[1]['B_2_Assignment_3_Category'] == ('K', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Category'] == 'other'
    assert verf_result[1]['B_2_Assignment_4_Category'] == ('K', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Category'] == 'phonon mode'
    assert verf_result[1]['B_3_Assignment_1_Category'] == ('K', 57, 57)
    # Band Assignment Method
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Method'] == 'L15'
    assert verf_result[1]['B_1_Assignment_1_Method'] == ('L', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Method'] == 'L27'
    assert verf_result[1]['B_1_Assignment_2_Method'] == ('L', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Method'] == 'L21'
    assert verf_result[1]['B_1_Assignment_3_Method'] == ('L', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Method'] == 'L51'
    assert verf_result[1]['B_2_Assignment_1_Method'] == ('L', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Method'] == 'L45'
    assert verf_result[1]['B_2_Assignment_2_Method'] == ('L', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Method'] == 'L39'
    assert verf_result[1]['B_2_Assignment_3_Method'] == ('L', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Method'] == 'L33'
    assert verf_result[1]['B_2_Assignment_4_Method'] == ('L', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Method'] == 'L57'
    assert verf_result[1]['B_3_Assignment_1_Method'] == ('L', 57, 57)
    # Band Assignment Level
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Level'] == 'fully assigned'
    assert verf_result[1]['B_1_Assignment_1_Level'] == ('M', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Level'] == 'partly assigned'
    assert verf_result[1]['B_1_Assignment_2_Level'] == ('M', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Level'] == ''
    assert verf_result[1]['B_1_Assignment_3_Level'] == ('M', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Level'] == 'NULL'
    assert verf_result[1]['B_2_Assignment_1_Level'] == ('M', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Level'] == 'uncertain assignment'
    assert verf_result[1]['B_2_Assignment_2_Level'] == ('M', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Level'] == 'species assigned'
    assert verf_result[1]['B_2_Assignment_3_Level'] == ('M', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Level'] == 'transition assigned'
    assert verf_result[1]['B_2_Assignment_4_Level'] == ('M', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Level'] == ''
    assert verf_result[1]['B_3_Assignment_1_Level'] == ('M', 57, 57)
    # Band Assignment Evaluation
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Evaluation'] == ''
    assert verf_result[1]['B_1_Assignment_1_Evaluation'] == ('N', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Assignment_2_Evaluation'] == ('N', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Assignment_3_Evaluation'] == ('N', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Evaluation'] == ''
    assert verf_result[1]['B_2_Assignment_1_Evaluation'] == ('N', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Evaluation'] == 'with caution'
    assert verf_result[1]['B_2_Assignment_2_Evaluation'] == ('N', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Assignment_3_Evaluation'] == ('N', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Evaluation'] == 'validated'
    assert verf_result[1]['B_2_Assignment_4_Evaluation'] == ('N', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Evaluation'] == 'NULL'
    assert verf_result[1]['B_3_Assignment_1_Evaluation'] == ('N', 57, 57)
    # Band Assignment Comment
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Comment'] == 'O15'
    assert verf_result[1]['B_1_Assignment_1_Comment'] == ('O', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Comment'] == 'O27'
    assert verf_result[1]['B_1_Assignment_2_Comment'] == ('O', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Comment'] == 'O21'
    assert verf_result[1]['B_1_Assignment_3_Comment'] == ('O', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Comment'] == 'O51'
    assert verf_result[1]['B_2_Assignment_1_Comment'] == ('O', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Comment'] == 'O45'
    assert verf_result[1]['B_2_Assignment_2_Comment'] == ('O', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Comment'] == 'O39'
    assert verf_result[1]['B_2_Assignment_3_Comment'] == ('O', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Comment'] == 'O33'
    assert verf_result[1]['B_2_Assignment_4_Comment'] == ('O', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Comment'] == 'O57'
    assert verf_result[1]['B_3_Assignment_1_Comment'] == ('O', 57, 57)
    # Band Assignment Multiplicity Types
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Multiplicity_Types'] == ['', 'no', 'mode degeneracy', 'site degeneracy', 'rotational structure', 'other']
    assert verf_result[1]['B_1_Assignment_1_Multiplicity_Types'] == ('R', 15, 20)
    assert verf_result[0]['B_1_Assignment_2_Multiplicity_Types'] == ['mode degeneracy', 'rotational structure', 'other', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Multiplicity_Types'] == ('R', 27, 32)
    assert verf_result[0]['B_1_Assignment_3_Multiplicity_Types'] == ['no', '', 'rotational structure', '', 'other constituent specie', '']
    assert verf_result[1]['B_1_Assignment_3_Multiplicity_Types'] == ('R', 21, 26)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Multiplicity_Types'] == ['other', '', 'other isotope specie', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Multiplicity_Types'] == ('R', 51, 56)
    assert verf_result[0]['B_2_Assignment_2_Multiplicity_Types'] == ['accidental degeneracy', '', 'other constituent specie', 'accidental degeneracy', '', '']
    assert verf_result[1]['B_2_Assignment_2_Multiplicity_Types'] == ('R', 45, 50)
    assert verf_result[0]['B_2_Assignment_3_Multiplicity_Types'] == ['rotational structure', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Multiplicity_Types'] == ('R', 39, 44)
    assert verf_result[0]['B_2_Assignment_4_Multiplicity_Types'] == ['site degeneracy', '', '', '', 'other isotope specie', 'no']
    assert verf_result[1]['B_2_Assignment_4_Multiplicity_Types'] == ('R', 33, 38)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Multiplicity_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Multiplicity_Types'] == ('R', 57, 63)
    # Band Assignment Multiplicity Degeneracy
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Multiplicity_Degeneracy'] == ['', 'no', 'double', 'triple', 'quadruple', 'accidental double']
    assert verf_result[1]['B_1_Assignment_1_Multiplicity_Degeneracy'] == ('S', 15, 20)
    assert verf_result[0]['B_1_Assignment_2_Multiplicity_Degeneracy'] == ['accidental double', 'accidental triple', 'other', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Multiplicity_Degeneracy'] == ('S', 27, 32)
    assert verf_result[0]['B_1_Assignment_3_Multiplicity_Degeneracy'] == ['NULL', 'triple site', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Multiplicity_Degeneracy'] == ('S', 21, 26)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Multiplicity_Degeneracy'] == ['triple', '', '', 'double', '', '']
    assert verf_result[1]['B_2_Assignment_1_Multiplicity_Degeneracy'] == ('S', 51, 56)
    assert verf_result[0]['B_2_Assignment_2_Multiplicity_Degeneracy'] == ['no', '', 'accidental double', '', '', 'unknown']
    assert verf_result[1]['B_2_Assignment_2_Multiplicity_Degeneracy'] == ('S', 45, 50)
    assert verf_result[0]['B_2_Assignment_3_Multiplicity_Degeneracy'] == ['triple', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Multiplicity_Degeneracy'] == ('S', 39, 44)
    assert verf_result[0]['B_2_Assignment_4_Multiplicity_Degeneracy'] == ['quadruple', '', 'other', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Multiplicity_Degeneracy'] == ('S', 33, 38)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Multiplicity_Degeneracy'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Multiplicity_Degeneracy'] == ('S', 57, 63)
    # Band Assignment Multiplicity Other band
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Multiplicity_Other_band'] == ['T15', 'T16', 'T17', 'T18', 'T19', 'T20']
    assert verf_result[1]['B_1_Assignment_1_Multiplicity_Other_band'] == ('T', 15, 20)
    assert verf_result[0]['B_1_Assignment_2_Multiplicity_Other_band'] == ['T27', 'T28', 'T29', '', 'T31', '']
    assert verf_result[1]['B_1_Assignment_2_Multiplicity_Other_band'] == ('T', 27, 32)
    assert verf_result[0]['B_1_Assignment_3_Multiplicity_Other_band'] == ['T21', '', 'T23', '', '', 'T26']
    assert verf_result[1]['B_1_Assignment_3_Multiplicity_Other_band'] == ('T', 21, 26)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Multiplicity_Other_band'] == ['T51', '', 'T53', 'T54', '', '']
    assert verf_result[1]['B_2_Assignment_1_Multiplicity_Other_band'] == ('T', 51, 56)
    assert verf_result[0]['B_2_Assignment_2_Multiplicity_Other_band'] == ['T45', '', 'T47', '', 'T49', '']
    assert verf_result[1]['B_2_Assignment_2_Multiplicity_Other_band'] == ('T', 45, 50)
    assert verf_result[0]['B_2_Assignment_3_Multiplicity_Other_band'] == ['T39', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Multiplicity_Other_band'] == ('T', 39, 44)
    assert verf_result[0]['B_2_Assignment_4_Multiplicity_Other_band'] == ['T33', 'T34', 'T35', '', '', 'T38']
    assert verf_result[1]['B_2_Assignment_4_Multiplicity_Other_band'] == ('T', 33, 38)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Multiplicity_Other_band'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Multiplicity_Other_band'] == ('T', 57, 63)
    # Band Assignment Multiplicity Level
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Contribution_Level'] == ''
    assert verf_result[1]['B_1_Assignment_1_Contribution_Level'] == ('U', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Contribution_Level'] == ''
    assert verf_result[1]['B_1_Assignment_2_Contribution_Level'] == ('U', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Contribution_Level'] == 'NULL'
    assert verf_result[1]['B_1_Assignment_3_Contribution_Level'] == ('U', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Contribution_Level'] == 'major'
    assert verf_result[1]['B_2_Assignment_1_Contribution_Level'] == ('U', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Contribution_Level'] == 'medium'
    assert verf_result[1]['B_2_Assignment_2_Contribution_Level'] == ('U', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Contribution_Level'] == 'minor'
    assert verf_result[1]['B_2_Assignment_3_Contribution_Level'] == ('U', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Contribution_Level'] == 'extracted'
    assert verf_result[1]['B_2_Assignment_4_Contribution_Level'] == ('U', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Contribution_Level'] == ''
    assert verf_result[1]['B_3_Assignment_1_Contribution_Level'] == ('U', 57, 57)
    # Band Assignment Multiplicity Comment
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Contribution_Comment'] == 'V15'
    assert verf_result[1]['B_1_Assignment_1_Contribution_Comment'] == ('V', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Contribution_Comment'] == 'V27'
    assert verf_result[1]['B_1_Assignment_2_Contribution_Comment'] == ('V', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Contribution_Comment'] == 'V21'
    assert verf_result[1]['B_1_Assignment_3_Contribution_Comment'] == ('V', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Contribution_Comment'] == 'V51'
    assert verf_result[1]['B_2_Assignment_1_Contribution_Comment'] == ('V', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Contribution_Comment'] == 'V45'
    assert verf_result[1]['B_2_Assignment_2_Contribution_Comment'] == ('V', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Contribution_Comment'] == 'V39'
    assert verf_result[1]['B_2_Assignment_3_Contribution_Comment'] == ('V', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Contribution_Comment'] == 'V33'
    assert verf_result[1]['B_2_Assignment_4_Contribution_Comment'] == ('V', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Contribution_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Contribution_Comment'] == ('V', 57, 57)
    # Band Assignment Transition Qty
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Transition_Species_qty'] == 6
    assert verf_result[0]['B_1_Assignment_2_Transition_Species_qty'] == 3
    assert verf_result[0]['B_1_Assignment_3_Transition_Species_qty'] == 2
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Transition_Species_qty'] == 2
    assert verf_result[0]['B_2_Assignment_2_Transition_Species_qty'] == 3
    assert verf_result[0]['B_2_Assignment_3_Transition_Species_qty'] == 2
    assert verf_result[0]['B_2_Assignment_4_Transition_Species_qty'] == 1
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Transition_Species_qty'] == 1
    # Band Assignment Transition Specie UID
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_1_UID'] == 'Y15'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_1_UID'] == ('Y', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_2_UID'] == 'Y16'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_2_UID'] == ('Y', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_3_UID'] == 'Y17'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_3_UID'] == ('Y', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_4_UID'] == 'Y18'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_4_UID'] == ('Y', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_5_UID'] == 'Y19'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_5_UID'] == ('Y', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_6_UID'] == 'Y20'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_6_UID'] == ('Y', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Transition_Specie_1_UID'] == 'Y27'
    assert verf_result[1]['B_1_Assignment_2_Transition_Specie_1_UID'] == ('Y', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Transition_Specie_2_UID'] == 'Y28'
    assert verf_result[1]['B_1_Assignment_2_Transition_Specie_2_UID'] == ('Y', 28, 28)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Transition_Specie_3_UID'] == 'Y31'
    assert verf_result[1]['B_1_Assignment_2_Transition_Specie_3_UID'] == ('Y', 31, 31)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Transition_Specie_1_UID'] == 'Y21'
    assert verf_result[1]['B_1_Assignment_3_Transition_Specie_1_UID'] == ('Y', 21, 21)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Transition_Specie_2_UID'] == 'Y23'
    assert verf_result[1]['B_1_Assignment_3_Transition_Specie_2_UID'] == ('Y', 23, 23)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Transition_Specie_1_UID'] == 'Y51'
    assert verf_result[1]['B_2_Assignment_1_Transition_Specie_1_UID'] == ('Y', 51, 51)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Transition_Specie_2_UID'] == 'Y53'
    assert verf_result[1]['B_2_Assignment_1_Transition_Specie_2_UID'] == ('Y', 53, 53)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Transition_Specie_1_UID'] == 'Y45'
    assert verf_result[1]['B_2_Assignment_2_Transition_Specie_1_UID'] == ('Y', 45, 45)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Transition_Specie_2_UID'] == 'Y48'
    assert verf_result[1]['B_2_Assignment_2_Transition_Specie_2_UID'] == ('Y', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Transition_Specie_3_UID'] == 'Y49'
    assert verf_result[1]['B_2_Assignment_2_Transition_Specie_3_UID'] == ('Y', 49, 49)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Transition_Specie_1_UID'] == 'Y39'
    assert verf_result[1]['B_2_Assignment_3_Transition_Specie_1_UID'] == ('Y', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Transition_Specie_2_UID'] == 'Y40'
    assert verf_result[1]['B_2_Assignment_3_Transition_Specie_2_UID'] == ('Y', 40, 40)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Transition_Specie_1_UID'] == 'Y33'
    assert verf_result[1]['B_2_Assignment_4_Transition_Specie_1_UID'] == ('Y', 33, 33)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Transition_Specie_1_UID'] == ''
    assert verf_result[1]['B_3_Assignment_1_Transition_Specie_1_UID'] == ('Y', 57, 57)
    # Band Assignment Transition Site Molecule labels
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Molecule_labels'] == ['Z15']
    assert verf_result[1]['B_1_Assignment_1_Site_1_Molecule_labels'] == ('Z', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Molecule_labels'] == ['Z16']
    assert verf_result[1]['B_1_Assignment_1_Site_2_Molecule_labels'] == ('Z', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Molecule_labels'] == ['Z17']
    assert verf_result[1]['B_1_Assignment_1_Site_3_Molecule_labels'] == ('Z', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Molecule_labels'] == ['Z18']
    assert verf_result[1]['B_1_Assignment_1_Site_4_Molecule_labels'] == ('Z', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Molecule_labels'] == ['Z19']
    assert verf_result[1]['B_1_Assignment_1_Site_5_Molecule_labels'] == ('Z', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Molecule_labels'] == ['Z20']
    assert verf_result[1]['B_1_Assignment_1_Site_6_Molecule_labels'] == ('Z', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Molecule_labels'] == ['Z27']
    assert verf_result[1]['B_1_Assignment_2_Site_1_Molecule_labels'] == ('Z', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Molecule_labels'] == ['Z28', 'Z29', '']
    assert verf_result[1]['B_1_Assignment_2_Site_2_Molecule_labels'] == ('Z', 28, 30)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Molecule_labels'] == ['Z31', 'Z32']
    assert verf_result[1]['B_1_Assignment_2_Site_3_Molecule_labels'] == ('Z', 31, 32)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Molecule_labels'] == ['Z21', '']
    assert verf_result[1]['B_1_Assignment_3_Site_1_Molecule_labels'] == ('Z', 21, 22)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Molecule_labels'] == ['Z23', 'Z24', '', '']
    assert verf_result[1]['B_1_Assignment_3_Site_2_Molecule_labels'] == ('Z', 23, 26)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Molecule_labels'] == ['Z51', 'Z52']
    assert verf_result[1]['B_2_Assignment_1_Site_1_Molecule_labels'] == ('Z', 51, 52)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Molecule_labels'] == ['Z53', '', 'Z55', 'Z56']
    assert verf_result[1]['B_2_Assignment_1_Site_2_Molecule_labels'] == ('Z', 53, 56)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Molecule_labels'] == ['Z45', 'Z46', '']
    assert verf_result[1]['B_2_Assignment_2_Site_1_Molecule_labels'] == ('Z', 45, 47)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Molecule_labels'] == ['Z48']
    assert verf_result[1]['B_2_Assignment_2_Site_2_Molecule_labels'] == ('Z', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Molecule_labels'] == ['Z49', 'Z50']
    assert verf_result[1]['B_2_Assignment_2_Site_3_Molecule_labels'] == ('Z', 49, 50)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Molecule_labels'] == ['Z39']
    assert verf_result[1]['B_2_Assignment_3_Site_1_Molecule_labels'] == ('Z', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Molecule_labels'] == ['Z40', '', 'Z42', '', '']
    assert verf_result[1]['B_2_Assignment_3_Site_2_Molecule_labels'] == ('Z', 40, 44)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Molecule_labels'] == ['Z33', '', 'Z35', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Site_1_Molecule_labels'] == ('Z', 33, 38)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Molecule_labels'] == ['']
    assert verf_result[1]['B_3_Assignment_1_Site_1_Molecule_labels'] == ('Z', 57, 57)
    # Band Assignment Transition Site Molecule Symm. labels
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Molecule_Symm_label'] == ['AA15']
    assert verf_result[1]['B_1_Assignment_1_Site_1_Molecule_Symm_label'] == ('AA', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Molecule_Symm_label'] == ['AA16']
    assert verf_result[1]['B_1_Assignment_1_Site_2_Molecule_Symm_label'] == ('AA', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Molecule_Symm_label'] == ['AA17']
    assert verf_result[1]['B_1_Assignment_1_Site_3_Molecule_Symm_label'] == ('AA', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Molecule_Symm_label'] == ['AA18']
    assert verf_result[1]['B_1_Assignment_1_Site_4_Molecule_Symm_label'] == ('AA', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Molecule_Symm_label'] == ['AA19']
    assert verf_result[1]['B_1_Assignment_1_Site_5_Molecule_Symm_label'] == ('AA', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Molecule_Symm_label'] == ['AA20']
    assert verf_result[1]['B_1_Assignment_1_Site_6_Molecule_Symm_label'] == ('AA', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Molecule_Symm_label'] == ['AA27']
    assert verf_result[1]['B_1_Assignment_2_Site_1_Molecule_Symm_label'] == ('AA', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Molecule_Symm_label'] == ['AA28', 'AA29', 'AA30']
    assert verf_result[1]['B_1_Assignment_2_Site_2_Molecule_Symm_label'] == ('AA', 28, 30)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Molecule_Symm_label'] == ['AA31', 'AA32']
    assert verf_result[1]['B_1_Assignment_2_Site_3_Molecule_Symm_label'] == ('AA', 31, 32)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Molecule_Symm_label'] == ['AA21', 'AA22']
    assert verf_result[1]['B_1_Assignment_3_Site_1_Molecule_Symm_label'] == ('AA', 21, 22)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Molecule_Symm_label'] == ['AA23', 'AA24', 'AA25', '']
    assert verf_result[1]['B_1_Assignment_3_Site_2_Molecule_Symm_label'] == ('AA', 23, 26)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Molecule_Symm_label'] == ['AA51', 'AA52']
    assert verf_result[1]['B_2_Assignment_1_Site_1_Molecule_Symm_label'] == ('AA', 51, 52)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Molecule_Symm_label'] == ['AA53', 'AA54', 'AA55', 'AA56']
    assert verf_result[1]['B_2_Assignment_1_Site_2_Molecule_Symm_label'] == ('AA', 53, 56)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Molecule_Symm_label'] == ['AA45', 'AA46', 'AA47']
    assert verf_result[1]['B_2_Assignment_2_Site_1_Molecule_Symm_label'] == ('AA', 45, 47)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Molecule_Symm_label'] == ['AA48']
    assert verf_result[1]['B_2_Assignment_2_Site_2_Molecule_Symm_label'] == ('AA', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Molecule_Symm_label'] == ['AA49', 'AA50']
    assert verf_result[1]['B_2_Assignment_2_Site_3_Molecule_Symm_label'] == ('AA', 49, 50)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Molecule_Symm_label'] == ['AA39']
    assert verf_result[1]['B_2_Assignment_3_Site_1_Molecule_Symm_label'] == ('AA', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Molecule_Symm_label'] == ['AA40', 'AA41', 'AA42', 'AA43', '']
    assert verf_result[1]['B_2_Assignment_3_Site_2_Molecule_Symm_label'] == ('AA', 40, 44)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Molecule_Symm_label'] == ['AA33', 'AA34', 'AA35', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Site_1_Molecule_Symm_label'] == ('AA', 33, 38)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Molecule_Symm_label'] == ['']
    assert verf_result[1]['B_3_Assignment_1_Site_1_Molecule_Symm_label'] == ('AA', 57, 57)
    # Band Assignment Transition Site Atom Labels
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Atom_Labels'] == ['AB15']
    assert verf_result[1]['B_1_Assignment_1_Site_1_Atom_Labels'] == ('AB', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Atom_Labels'] == ['AB16']
    assert verf_result[1]['B_1_Assignment_1_Site_2_Atom_Labels'] == ('AB', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Atom_Labels'] == ['AB17']
    assert verf_result[1]['B_1_Assignment_1_Site_3_Atom_Labels'] == ('AB', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Atom_Labels'] == ['AB18']
    assert verf_result[1]['B_1_Assignment_1_Site_4_Atom_Labels'] == ('AB', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Atom_Labels'] == ['AB19']
    assert verf_result[1]['B_1_Assignment_1_Site_5_Atom_Labels'] == ('AB', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Atom_Labels'] == ['AB20']
    assert verf_result[1]['B_1_Assignment_1_Site_6_Atom_Labels'] == ('AB', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Atom_Labels'] == ['AB27']
    assert verf_result[1]['B_1_Assignment_2_Site_1_Atom_Labels'] == ('AB', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Atom_Labels'] == ['AB28']
    assert verf_result[1]['B_1_Assignment_2_Site_2_Atom_Labels'] == ('AB', 28, 28)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Atom_Labels'] == ['AB31']
    assert verf_result[1]['B_1_Assignment_2_Site_3_Atom_Labels'] == ('AB', 31, 31)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Atom_Labels'] == ['AB21', 'AB22']
    assert verf_result[1]['B_1_Assignment_3_Site_1_Atom_Labels'] == ('AB', 21, 22)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Atom_Labels'] == ['AB23', 'AB24']
    assert verf_result[1]['B_1_Assignment_3_Site_2_Atom_Labels'] == ('AB', 23, 24)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Atom_Labels'] == ['AB51', 'AB52']
    assert verf_result[1]['B_2_Assignment_1_Site_1_Atom_Labels'] == ('AB', 51, 52)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Atom_Labels'] == ['AB53']
    assert verf_result[1]['B_2_Assignment_1_Site_2_Atom_Labels'] == ('AB', 53, 53)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Atom_Labels'] == ['AB45']
    assert verf_result[1]['B_2_Assignment_2_Site_1_Atom_Labels'] == ('AB', 45, 45)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Atom_Labels'] == ['AB48']
    assert verf_result[1]['B_2_Assignment_2_Site_2_Atom_Labels'] == ('AB', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Atom_Labels'] == ['AB49', 'AB50']
    assert verf_result[1]['B_2_Assignment_2_Site_3_Atom_Labels'] == ('AB', 49, 50)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Atom_Labels'] == ['AB39']
    assert verf_result[1]['B_2_Assignment_3_Site_1_Atom_Labels'] == ('AB', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Atom_Labels'] == ['AB40', 'AB41']
    assert verf_result[1]['B_2_Assignment_3_Site_2_Atom_Labels'] == ('AB', 40, 41)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Atom_Labels'] == ['AB33', 'AB34']
    assert verf_result[1]['B_2_Assignment_4_Site_1_Atom_Labels'] == ('AB', 33, 34)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Atom_Labels'] == ['']
    assert verf_result[1]['B_3_Assignment_1_Site_1_Atom_Labels'] == ('AB', 57, 57)
    # Band Assignment Transition Site Atom Comment
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Atom_Comment'] == 'AC15'
    assert verf_result[1]['B_1_Assignment_1_Site_1_Atom_Comment'] == ('AC', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Atom_Comment'] == 'AC16'
    assert verf_result[1]['B_1_Assignment_1_Site_2_Atom_Comment'] == ('AC', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Atom_Comment'] == 'AC17'
    assert verf_result[1]['B_1_Assignment_1_Site_3_Atom_Comment'] == ('AC', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Atom_Comment'] == 'AC18'
    assert verf_result[1]['B_1_Assignment_1_Site_4_Atom_Comment'] == ('AC', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Atom_Comment'] == 'AC19'
    assert verf_result[1]['B_1_Assignment_1_Site_5_Atom_Comment'] == ('AC', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Atom_Comment'] == 'AC20'
    assert verf_result[1]['B_1_Assignment_1_Site_6_Atom_Comment'] == ('AC', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Atom_Comment'] == 'AC27'
    assert verf_result[1]['B_1_Assignment_2_Site_1_Atom_Comment'] == ('AC', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Atom_Comment'] == 'AC28'
    assert verf_result[1]['B_1_Assignment_2_Site_2_Atom_Comment'] == ('AC', 28, 28)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Atom_Comment'] == 'AC31'
    assert verf_result[1]['B_1_Assignment_2_Site_3_Atom_Comment'] == ('AC', 31, 31)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Atom_Comment'] == 'AC21'
    assert verf_result[1]['B_1_Assignment_3_Site_1_Atom_Comment'] == ('AC', 21, 21)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Atom_Comment'] == 'AC23'
    assert verf_result[1]['B_1_Assignment_3_Site_2_Atom_Comment'] == ('AC', 23, 23)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Atom_Comment'] == 'AC51'
    assert verf_result[1]['B_2_Assignment_1_Site_1_Atom_Comment'] == ('AC', 51, 51)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Atom_Comment'] == 'AC53'
    assert verf_result[1]['B_2_Assignment_1_Site_2_Atom_Comment'] == ('AC', 53, 53)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Atom_Comment'] == 'AC45'
    assert verf_result[1]['B_2_Assignment_2_Site_1_Atom_Comment'] == ('AC', 45, 45)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Atom_Comment'] == 'AC48'
    assert verf_result[1]['B_2_Assignment_2_Site_2_Atom_Comment'] == ('AC', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Atom_Comment'] == 'AC49'
    assert verf_result[1]['B_2_Assignment_2_Site_3_Atom_Comment'] == ('AC', 49, 49)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Atom_Comment'] == 'AC39'
    assert verf_result[1]['B_2_Assignment_3_Site_1_Atom_Comment'] == ('AC', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Atom_Comment'] == 'AC40'
    assert verf_result[1]['B_2_Assignment_3_Site_2_Atom_Comment'] == ('AC', 40, 40)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Atom_Comment'] == 'AC33'
    assert verf_result[1]['B_2_Assignment_4_Site_1_Atom_Comment'] == ('AC', 33, 33)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Atom_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Site_1_Atom_Comment'] == ('AC', 57, 57)
    # Band Assignment Electronic Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Electronic_Types'] == ['crystal field', 'ligand-to-metal charge-transfer', 'intervalence charge transfer', 'double exciton', 'other', 'unknown']
    assert verf_result[1]['B_1_Assignment_1_Electronic_Types'] == ('AF', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Electronic_Types'] == ['', '', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Electronic_Types'] == ('AF', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Electronic_Types'] == ['NULL', '', 'intervalence charge transfer', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Electronic_Types'] == ('AF', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Electronic_Types'] == ['crystal field', 'intervalence charge transfer', 'unknown', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Electronic_Types'] == ('AF', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Electronic_Types'] == ['double exciton', 'unknown', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_2_Electronic_Types'] == ('AF', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Electronic_Types'] == ['other', 'double exciton', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Electronic_Types'] == ('AF', 39, 44)
    # Band 2 Assignment 4
    assert verf_result[0]['B_2_Assignment_4_Electronic_Types'] == ['', 'ligand-to-metal charge-transfer', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Electronic_Types'] == ('AF', 33, 38)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Electronic_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Electronic_Types'] == ('AF', 57, 63)
    # Band Assignment Electronic Labels
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Electronic_Labels'] == ['AG15', 'AG16', 'AG17', 'AG18', 'AG19', 'AG20']
    assert verf_result[1]['B_1_Assignment_1_Electronic_Labels'] == ('AG', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Electronic_Labels'] == ['', '', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Electronic_Labels'] == ('AG', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Electronic_Labels'] == ['AG21', 'AG22', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Electronic_Labels'] == ('AG', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Electronic_Labels'] == ['AG51', 'AG52', 'AG53', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Electronic_Labels'] == ('AG', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Electronic_Labels'] == ['', 'AG46', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_2_Electronic_Labels'] == ('AG', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Electronic_Labels'] == ['AG39', 'AG40', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Electronic_Labels'] == ('AG', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Electronic_Labels'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Electronic_Labels'] == ('AG', 57, 63)
    # Band Assignment Electronic Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Electronic_Comment'] == 'AH15'
    assert verf_result[1]['B_1_Assignment_1_Electronic_Comment'] == ('AH', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Electronic_Comment'] == ''
    assert verf_result[1]['B_1_Assignment_2_Electronic_Comment'] == ('AH', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Electronic_Comment'] == 'AH21'
    assert verf_result[1]['B_1_Assignment_3_Electronic_Comment'] == ('AH', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Electronic_Comment'] == 'AH51'
    assert verf_result[1]['B_2_Assignment_1_Electronic_Comment'] == ('AH', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Electronic_Comment'] == 'AH45'
    assert verf_result[1]['B_2_Assignment_2_Electronic_Comment'] == ('AH', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Electronic_Comment'] == 'AH39'
    assert verf_result[1]['B_2_Assignment_3_Electronic_Comment'] == ('AH', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Electronic_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Electronic_Comment'] == ('AH', 57, 57)
    # Band Assignment Vibrations qty
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Vibrations_qty'] == 6
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Vibrations_qty'] == 2
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Vibrations_qty'] == 4
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Vibrations_qty'] == 2
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Vibrations_qty'] == 2
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Vibrations_qty'] == 3
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Vibrations_qty'] == 1
    # Band Assignment Vibration Types
    # Band 1 Assignment 1 Vibration 1
    assert verf_result[0]['B_1_Assignment_1_Vibration_1_Types'] == 'stretching'
    assert verf_result[1]['B_1_Assignment_1_Vibration_1_Types'] == ('AK', 15, 15)
    # Band 1 Assignment 1 Vibration 2
    assert verf_result[0]['B_1_Assignment_1_Vibration_2_Types'] == 'stretching sym.'
    assert verf_result[1]['B_1_Assignment_1_Vibration_2_Types'] == ('AK', 16, 16)
    # Band 1 Assignment 1 Vibration 3
    assert verf_result[0]['B_1_Assignment_1_Vibration_3_Types'] == 'stretching asym.'
    assert verf_result[1]['B_1_Assignment_1_Vibration_3_Types'] == ('AK', 17, 17)
    # Band 1 Assignment 1 Vibration 4
    assert verf_result[0]['B_1_Assignment_1_Vibration_4_Types'] == 'bending'
    assert verf_result[1]['B_1_Assignment_1_Vibration_4_Types'] == ('AK', 18, 18)
    # Band 1 Assignment 1 Vibration 5
    assert verf_result[0]['B_1_Assignment_1_Vibration_5_Types'] == 'bending in-p'
    assert verf_result[1]['B_1_Assignment_1_Vibration_5_Types'] == ('AK', 19, 19)
    # Band 1 Assignment 1 Vibration 6
    assert verf_result[0]['B_1_Assignment_1_Vibration_6_Types'] == 'bending out-p'
    assert verf_result[1]['B_1_Assignment_1_Vibration_6_Types'] == ('AK', 20, 20)
    # Band 1 Assignment 2 Vibration 1
    assert verf_result[0]['B_1_Assignment_2_Vibration_1_Types'] == 'bending asym. in-p (rocking)'
    assert verf_result[1]['B_1_Assignment_2_Vibration_1_Types'] == ('AK', 27, 27)
    # Band 1 Assignment 2 Vibration 2
    assert verf_result[0]['B_1_Assignment_2_Vibration_2_Types'] == 'bending sym. out-p (wagging)'
    assert verf_result[1]['B_1_Assignment_2_Vibration_2_Types'] == ('AK', 29, 29)
    # Band 1 Assignment 3 Vibration 1
    assert verf_result[0]['B_1_Assignment_3_Vibration_1_Types'] == 'bending sym.'
    assert verf_result[1]['B_1_Assignment_3_Vibration_1_Types'] == ('AK', 21, 21)
    # Band 1 Assignment 3 Vibration 2
    assert verf_result[0]['B_1_Assignment_3_Vibration_2_Types'] == 'bending asym.'
    assert verf_result[1]['B_1_Assignment_3_Vibration_2_Types'] == ('AK', 22, 22)
    # Band 1 Assignment 3 Vibration 3
    assert verf_result[0]['B_1_Assignment_3_Vibration_3_Types'] == 'bending sym. in-p (scissoring)'
    assert verf_result[1]['B_1_Assignment_3_Vibration_3_Types'] == ('AK', 23, 23)
    # Band 1 Assignment 3 Vibration 4
    assert verf_result[0]['B_1_Assignment_3_Vibration_4_Types'] == ''
    assert verf_result[1]['B_1_Assignment_3_Vibration_4_Types'] == ('AK', 24, 24)
    # Band 2 Assignment 1 Vibration 1
    assert verf_result[0]['B_2_Assignment_1_Vibration_1_Types'] == 'unknown'
    assert verf_result[1]['B_2_Assignment_1_Vibration_1_Types'] == ('AK', 51, 51)
    # Band 2 Assignment 1 Vibration 2
    assert verf_result[0]['B_2_Assignment_1_Vibration_2_Types'] == 'stretching asym.'
    assert verf_result[1]['B_2_Assignment_1_Vibration_2_Types'] == ('AK', 52, 52)
    # Band 2 Assignment 2 Vibration 1
    assert verf_result[0]['B_2_Assignment_2_Vibration_1_Types'] == 'other'
    assert verf_result[1]['B_2_Assignment_2_Vibration_1_Types'] == ('AK', 45, 45)
    # Band 2 Assignment 2 Vibration 2
    assert verf_result[0]['B_2_Assignment_2_Vibration_2_Types'] == 'NULL'
    assert verf_result[1]['B_2_Assignment_2_Vibration_2_Types'] == ('AK', 46, 46)
    # Band 2 Assignment 3 Vibration 1
    assert verf_result[0]['B_2_Assignment_3_Vibration_1_Types'] == 'deformation in-p'
    assert verf_result[1]['B_2_Assignment_3_Vibration_1_Types'] == ('AK', 39, 39)
    # Band 2 Assignment 3 Vibration 2
    assert verf_result[0]['B_2_Assignment_3_Vibration_2_Types'] == 'deformation out-p'
    assert verf_result[1]['B_2_Assignment_3_Vibration_2_Types'] == ('AK', 40, 40)
    # Band 2 Assignment 3 Vibration 3
    assert verf_result[0]['B_2_Assignment_3_Vibration_3_Types'] == 'deformation sym'
    assert verf_result[1]['B_2_Assignment_3_Vibration_3_Types'] == ('AK', 41, 41)
    # Band 3 Assignment 1 Vibration 1
    assert verf_result[0]['B_3_Assignment_1_Vibration_1_Types'] == ''
    assert verf_result[1]['B_3_Assignment_1_Vibration_1_Types'] == ('AK', 57, 57)
    # Band Assignment Vibration Label
    # Band 1 Assignment 1 Vibration 1
    assert verf_result[0]['B_1_Assignment_1_Vibration_1_Label'] == 'AL15'
    assert verf_result[1]['B_1_Assignment_1_Vibration_1_Label'] == ('AL', 15, 15)
    # Band 1 Assignment 1 Vibration 2
    assert verf_result[0]['B_1_Assignment_1_Vibration_2_Label'] == 'AL16'
    assert verf_result[1]['B_1_Assignment_1_Vibration_2_Label'] == ('AL', 16, 16)
    # Band 1 Assignment 1 Vibration 3
    assert verf_result[0]['B_1_Assignment_1_Vibration_3_Label'] == 'AL17'
    assert verf_result[1]['B_1_Assignment_1_Vibration_3_Label'] == ('AL', 17, 17)
    # Band 1 Assignment 1 Vibration 4
    assert verf_result[0]['B_1_Assignment_1_Vibration_4_Label'] == 'AL18'
    assert verf_result[1]['B_1_Assignment_1_Vibration_4_Label'] == ('AL', 18, 18)
    # Band 1 Assignment 1 Vibration 5
    assert verf_result[0]['B_1_Assignment_1_Vibration_5_Label'] == 'AL19'
    assert verf_result[1]['B_1_Assignment_1_Vibration_5_Label'] == ('AL', 19, 19)
    # Band 1 Assignment 1 Vibration 6
    assert verf_result[0]['B_1_Assignment_1_Vibration_6_Label'] == 'AL20'
    assert verf_result[1]['B_1_Assignment_1_Vibration_6_Label'] == ('AL', 20, 20)
    # Band 1 Assignment 2 Vibration 1
    assert verf_result[0]['B_1_Assignment_2_Vibration_1_Label'] == 'AL27'
    assert verf_result[1]['B_1_Assignment_2_Vibration_1_Label'] == ('AL', 27, 27)
    # Band 1 Assignment 2 Vibration 2
    assert verf_result[0]['B_1_Assignment_2_Vibration_2_Label'] == 'AL29'
    assert verf_result[1]['B_1_Assignment_2_Vibration_2_Label'] == ('AL', 29, 29)
    # Band 1 Assignment 3 Vibration 1
    assert verf_result[0]['B_1_Assignment_3_Vibration_1_Label'] == 'AL21'
    assert verf_result[1]['B_1_Assignment_3_Vibration_1_Label'] == ('AL', 21, 21)
    # Band 1 Assignment 3 Vibration 2
    assert verf_result[0]['B_1_Assignment_3_Vibration_2_Label'] == ''
    assert verf_result[1]['B_1_Assignment_3_Vibration_2_Label'] == ('AL', 22, 22)
    # Band 1 Assignment 3 Vibration 3
    assert verf_result[0]['B_1_Assignment_3_Vibration_3_Label'] == 'AL23'
    assert verf_result[1]['B_1_Assignment_3_Vibration_3_Label'] == ('AL', 23, 23)
    # Band 1 Assignment 3 Vibration 4
    assert verf_result[0]['B_1_Assignment_3_Vibration_4_Label'] == 'AL24'
    assert verf_result[1]['B_1_Assignment_3_Vibration_4_Label'] == ('AL', 24, 24)
    # Band 2 Assignment 1 Vibration 1
    assert verf_result[0]['B_2_Assignment_1_Vibration_1_Label'] == 'AL51'
    assert verf_result[1]['B_2_Assignment_1_Vibration_1_Label'] == ('AL', 51, 51)
    # Band 2 Assignment 1 Vibration 2
    assert verf_result[0]['B_2_Assignment_1_Vibration_2_Label'] == 'AL52'
    assert verf_result[1]['B_2_Assignment_1_Vibration_2_Label'] == ('AL', 52, 52)
    # Band 2 Assignment 2 Vibration 1
    assert verf_result[0]['B_2_Assignment_2_Vibration_1_Label'] == 'AL45'
    assert verf_result[1]['B_2_Assignment_2_Vibration_1_Label'] == ('AL', 45, 45)
    # Band 2 Assignment 2 Vibration 2
    assert verf_result[0]['B_2_Assignment_2_Vibration_2_Label'] == 'AL46'
    assert verf_result[1]['B_2_Assignment_2_Vibration_2_Label'] == ('AL', 46, 46)
    # Band 2 Assignment 3 Vibration 1
    assert verf_result[0]['B_2_Assignment_3_Vibration_1_Label'] == 'AL39'
    assert verf_result[1]['B_2_Assignment_3_Vibration_1_Label'] == ('AL', 39, 39)
    # Band 2 Assignment 3 Vibration 2
    assert verf_result[0]['B_2_Assignment_3_Vibration_2_Label'] == 'AL40'
    assert verf_result[1]['B_2_Assignment_3_Vibration_2_Label'] == ('AL', 40, 40)
    # Band 2 Assignment 3 Vibration 3
    assert verf_result[0]['B_2_Assignment_3_Vibration_3_Label'] == 'AL41'
    assert verf_result[1]['B_2_Assignment_3_Vibration_3_Label'] == ('AL', 41, 41)
    # Band 3 Assignment 1 Vibration 1
    assert verf_result[0]['B_3_Assignment_1_Vibration_1_Label'] == ''
    assert verf_result[1]['B_3_Assignment_1_Vibration_1_Label'] == ('AL', 57, 57)
    # Band Assignment Vibration Bonds
    # Band 1 Assignment 1 Vibration 1
    assert verf_result[0]['B_1_Assignment_1_Vibration_1_Bonds'] == ['AM15']
    assert verf_result[1]['B_1_Assignment_1_Vibration_1_Bonds'] == ('AM', 15, 15)
    # Band 1 Assignment 1 Vibration 2
    assert verf_result[0]['B_1_Assignment_1_Vibration_2_Bonds'] == ['AM16']
    assert verf_result[1]['B_1_Assignment_1_Vibration_2_Bonds'] == ('AM', 16, 16)
    # Band 1 Assignment 1 Vibration 3
    assert verf_result[0]['B_1_Assignment_1_Vibration_3_Bonds'] == ['AM17']
    assert verf_result[1]['B_1_Assignment_1_Vibration_3_Bonds'] == ('AM', 17, 17)
    # Band 1 Assignment 1 Vibration 4
    assert verf_result[0]['B_1_Assignment_1_Vibration_4_Bonds'] == ['AM18']
    assert verf_result[1]['B_1_Assignment_1_Vibration_4_Bonds'] == ('AM', 18, 18)
    # Band 1 Assignment 1 Vibration 5
    assert verf_result[0]['B_1_Assignment_1_Vibration_5_Bonds'] == ['AM19']
    assert verf_result[1]['B_1_Assignment_1_Vibration_5_Bonds'] == ('AM', 19, 19)
    # Band 1 Assignment 1 Vibration 6
    assert verf_result[0]['B_1_Assignment_1_Vibration_6_Bonds'] == ['AM20']
    assert verf_result[1]['B_1_Assignment_1_Vibration_6_Bonds'] == ('AM', 20, 20)
    # Band 1 Assignment 2 Vibration 1
    assert verf_result[0]['B_1_Assignment_2_Vibration_1_Bonds'] == ['AM27', 'AM28']
    assert verf_result[1]['B_1_Assignment_2_Vibration_1_Bonds'] == ('AM', 27, 28)
    # Band 1 Assignment 2 Vibration 2
    assert verf_result[0]['B_1_Assignment_2_Vibration_2_Bonds'] == ['AM29', 'AM31']
    assert verf_result[1]['B_1_Assignment_2_Vibration_2_Bonds'] == ('AM', 29, 31)
    # Band 1 Assignment 3 Vibration 1
    assert verf_result[0]['B_1_Assignment_3_Vibration_1_Bonds'] == ['AM21']
    assert verf_result[1]['B_1_Assignment_3_Vibration_1_Bonds'] == ('AM', 21, 21)
    # Band 1 Assignment 3 Vibration 2
    assert verf_result[0]['B_1_Assignment_3_Vibration_2_Bonds'] == ['AM22']
    assert verf_result[1]['B_1_Assignment_3_Vibration_2_Bonds'] == ('AM', 22, 22)
    # Band 1 Assignment 3 Vibration 3
    assert verf_result[0]['B_1_Assignment_3_Vibration_3_Bonds'] == ['AM23']
    assert verf_result[1]['B_1_Assignment_3_Vibration_3_Bonds'] == ('AM', 23, 23)
    # Band 1 Assignment 3 Vibration 4
    assert verf_result[0]['B_1_Assignment_3_Vibration_4_Bonds'] == ['']
    assert verf_result[1]['B_1_Assignment_3_Vibration_4_Bonds'] == ('', '', '')
    # Band 2 Assignment 1 Vibration 1
    assert verf_result[0]['B_2_Assignment_1_Vibration_1_Bonds'] == ['']
    assert verf_result[1]['B_2_Assignment_1_Vibration_1_Bonds'] == ('', '', '')
    # Band 2 Assignment 1 Vibration 2
    assert verf_result[0]['B_2_Assignment_1_Vibration_2_Bonds'] == ['AM52', 'AM53']
    assert verf_result[1]['B_2_Assignment_1_Vibration_2_Bonds'] == ('AM', 52, 53)
    # Band 2 Assignment 2 Vibration 1
    assert verf_result[0]['B_2_Assignment_2_Vibration_1_Bonds'] == ['AM45']
    assert verf_result[1]['B_2_Assignment_2_Vibration_1_Bonds'] == ('AM', 45, 45)
    # Band 2 Assignment 2 Vibration 2
    assert verf_result[0]['B_2_Assignment_2_Vibration_2_Bonds'] == ['']
    assert verf_result[1]['B_2_Assignment_2_Vibration_2_Bonds'] == ('', '', '')
    # Band 2 Assignment 3 Vibration 1
    assert verf_result[0]['B_2_Assignment_3_Vibration_1_Bonds'] == ['AM39']
    assert verf_result[1]['B_2_Assignment_3_Vibration_1_Bonds'] == ('AM', 39, 39)
    # Band 2 Assignment 3 Vibration 2
    assert verf_result[0]['B_2_Assignment_3_Vibration_2_Bonds'] == ['']
    assert verf_result[1]['B_2_Assignment_3_Vibration_2_Bonds'] == ('', '', '')
    # Band 2 Assignment 3 Vibration 3
    assert verf_result[0]['B_2_Assignment_3_Vibration_3_Bonds'] == ['AM41']
    assert verf_result[1]['B_2_Assignment_3_Vibration_3_Bonds'] == ('AM', 41, 41)
    # Band 3 Assignment 1 Vibration 1
    assert verf_result[0]['B_3_Assignment_1_Vibration_1_Bonds'] == ['']
    assert verf_result[1]['B_3_Assignment_1_Vibration_1_Bonds'] == ('AM', 57, 57)
    # Band Assignment Vibration Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Vibrations_Comment'] == 'AN15'
    assert verf_result[1]['B_1_Assignment_1_Vibrations_Comment'] == ('AN', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Vibrations_Comment'] == ''
    assert verf_result[1]['B_1_Assignment_2_Vibrations_Comment'] == ('AN', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Vibrations_Comment'] == 'AN21'
    assert verf_result[1]['B_1_Assignment_3_Vibrations_Comment'] == ('AN', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Vibrations_Comment'] == 'AN51'
    assert verf_result[1]['B_2_Assignment_1_Vibrations_Comment'] == ('AN', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Vibrations_Comment'] == 'AN45'
    assert verf_result[1]['B_2_Assignment_2_Vibrations_Comment'] == ('AN', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Vibrations_Comment'] == 'AN39'
    assert verf_result[1]['B_2_Assignment_3_Vibrations_Comment'] == ('AN', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Vibrations_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Vibrations_Comment'] == ('AN', 57, 57)
    # Band Assignment Rotation Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Rotation_Types'] == ['free rotation', 'hindered rotation', 'libration', 'other', 'unknown', 'NULL']
    assert verf_result[1]['B_1_Assignment_1_Rotation_Types'] == ('AQ', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Rotation_Types'] == ['free rotation', 'libration', 'NULL', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Rotation_Types'] == ('AQ', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Rotation_Types'] == ['free rotation', 'unknown', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Rotation_Types'] == ('AQ', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Rotation_Types'] == ['NULL', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Rotation_Types'] == ('AQ', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Rotation_Types'] == ['free rotation', '', 'unknown', 'NULL', '', '']
    assert verf_result[1]['B_2_Assignment_2_Rotation_Types'] == ('AQ', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Rotation_Types'] == ['free rotation', 'hindered rotation', 'unknown', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Rotation_Types'] == ('AQ', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Rotation_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Rotation_Types'] == ('AQ', 57, 63)
    # Band Assignment Rotation Label
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Rotation_Label'] == ['AR15', 'AR16', 'AR17', 'AR18', 'AR19', 'AR20']
    assert verf_result[1]['B_1_Assignment_1_Rotation_Label'] == ('AR', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Rotation_Label'] == ['AR27', '', 'AR29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Rotation_Label'] == ('AR', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Rotation_Label'] == ['AR21', 'AR22', 'AR23', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Rotation_Label'] == ('AR', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Rotation_Label'] == ['AR51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Rotation_Label'] == ('AR', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Rotation_Label'] == ['AR45', 'AR46', 'AR47', 'AR48', '', '']
    assert verf_result[1]['B_2_Assignment_2_Rotation_Label'] == ('AR', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Rotation_Label'] == ['AR39', 'AR40', 'AR41', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Rotation_Label'] == ('AR', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Rotation_Label'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Rotation_Label'] == ('AR', 57, 63)
    # Band Assignment Rotation Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Rotation_Comment'] == 'AS15'
    assert verf_result[1]['B_1_Assignment_1_Rotation_Comment'] == ('AS', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Rotation_Comment'] == 'AS27'
    assert verf_result[1]['B_1_Assignment_2_Rotation_Comment'] == ('AS', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Rotation_Comment'] == 'AS21'
    assert verf_result[1]['B_1_Assignment_3_Rotation_Comment'] == ('AS', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Rotation_Comment'] == 'AS51'
    assert verf_result[1]['B_2_Assignment_1_Rotation_Comment'] == ('AS', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Rotation_Comment'] == 'AS45'
    assert verf_result[1]['B_2_Assignment_2_Rotation_Comment'] == ('AS', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Rotation_Comment'] == 'AS39'
    assert verf_result[1]['B_2_Assignment_3_Rotation_Comment'] == ('AS', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Rotation_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Rotation_Comment'] == ('AS', 57, 57)
    # Band Assignment Phonon Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Phonon_Types'] == ['translation', 'longitudinal optic translation', 'transverse optic translation', 'longitudinal acoustic translation', 'transverse acoustic translation', 'other']
    assert verf_result[1]['B_1_Assignment_1_Phonon_Types'] == ('AV', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Phonon_Types'] == ['longitudinal optic translation', 'transverse acoustic translation', 'NULL', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Phonon_Types'] == ('AV', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Phonon_Types'] == ['unknown', 'NULL', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Phonon_Types'] == ('AV', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Phonon_Types'] == ['NULL', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Phonon_Types'] == ('AV', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Phonon_Types'] == ['translation', '', 'unknown', 'NULL', '', '']
    assert verf_result[1]['B_2_Assignment_2_Phonon_Types'] == ('AV', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Phonon_Types'] == ['longitudinal optic translation', 'other', 'NULL', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Phonon_Types'] == ('AV', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Phonon_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Phonon_Types'] == ('AV', 57, 63)
    # Band Assignment Phonon Label
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Phonon_Label'] == ['AW15', 'AW16', 'AW17', 'AW18', 'AW19', 'AW20']
    assert verf_result[1]['B_1_Assignment_1_Phonon_Label'] == ('AW', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Phonon_Label'] == ['AW27', '', 'AW29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Phonon_Label'] == ('AW', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Phonon_Label'] == ['AW21', 'AW22', 'AW23', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Phonon_Label'] == ('AW', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Phonon_Label'] == ['AW51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Phonon_Label'] == ('AW', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Phonon_Label'] == ['AW45', 'AW46', 'AW47', 'AW48', '', '']
    assert verf_result[1]['B_2_Assignment_2_Phonon_Label'] == ('AW', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Phonon_Label'] == ['AW39', 'AW40', 'AW41', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Phonon_Label'] == ('AW', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Phonon_Label'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Phonon_Label'] == ('AW', 57, 63)
    # Band Assignment Phonon Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Phonon_Comment'] == 'AX15'
    assert verf_result[1]['B_1_Assignment_1_Phonon_Comment'] == ('AX', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Phonon_Comment'] == 'AX27'
    assert verf_result[1]['B_1_Assignment_2_Phonon_Comment'] == ('AX', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Phonon_Comment'] == 'AX21'
    assert verf_result[1]['B_1_Assignment_3_Phonon_Comment'] == ('AX', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Phonon_Comment'] == 'AX51'
    assert verf_result[1]['B_2_Assignment_1_Phonon_Comment'] == ('AX', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Phonon_Comment'] == 'AX45'
    assert verf_result[1]['B_2_Assignment_2_Phonon_Comment'] == ('AX', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Phonon_Comment'] == 'AX39'
    assert verf_result[1]['B_2_Assignment_3_Phonon_Comment'] == ('AX', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Phonon_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Phonon_Comment'] == ('AX', 57, 57)
    # Band Assignment Resonances Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Types'] == ['Fermi resonance', 'electron-phonon coupling', 'rotational-vibrational coupling', 'vibration-phonon coupling', 'other', 'NULL']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Types'] == ('BA', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Types'] == ['Fermi resonance', 'unknown', 'NULL', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Types'] == ('BA', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Types'] == ['vibration-phonon coupling', 'NULL', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Types'] == ('BA', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Types'] == ['NULL', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Types'] == ('BA', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Types'] == ['electron-phonon coupling', '', 'unknown', 'NULL', '', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Types'] == ('BA', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Types'] == ['Fermi resonance', 'unknown', 'NULL', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Types'] == ('BA', 39, 44)
    # Band 2 Assignment 4
    assert verf_result[0]['B_2_Assignment_4_Resonances_Types'] == ['vibration-phonon coupling', 'unknown', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Resonances_Types'] == ('BA', 33, 38)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Types'] == ('BA', 57, 63)
    # Band Assignment Resonances Band
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Band'] == ['BB15', 'BB16', 'BB17', 'BB18', 'BB19', 'BB20']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Band'] == ('BB', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Band'] == ['BB27', '', 'BB29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Band'] == ('BB', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Band'] == ['BB21', 'BB22', 'BB23', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Band'] == ('BB', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Band'] == ['BB51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Band'] == ('BB', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Band'] == ['BB45', 'BB46', '', '', 'BB49', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Band'] == ('BB', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Band'] == ['', 'BB40', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Band'] == ('BB', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Band'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Band'] == ('BB', 57, 63)
    # Band Assignment Resonances Nb
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Nb'] == ['1', '2', '3', '4', '5', '6']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Nb'] == ('BC', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Nb'] == ['1', '2', '3', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Nb'] == ('BC', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Nb'] == ['3', '1', '2', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Nb'] == ('BC', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Nb'] == ['1', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Nb'] == ('BC', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Nb'] == ['1', '5', '4', '2', '3', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Nb'] == ('BC', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Nb'] == ['1', '2', '3', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Nb'] == ('BC', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Nb'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Nb'] == ('BC', 57, 63)
    # Band Assignment Resonances Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Comment'] == ['BD15', 'BD16', 'BD17', 'BD18', 'BD19', 'BD20']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Comment'] == ('BD', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Comment'] == ['', 'BD28', 'BD29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Comment'] == ('BD', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Comment'] == ['BD21', 'BD22', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Comment'] == ('BD', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Comment'] == ['BD51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Comment'] == ('BD', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Comment'] == ['BD45', 'BD46', '', '', 'BD49', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Comment'] == ('BD', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Comment'] == ['BD39', 'BD40', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Comment'] == ('BD', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Comment'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Comment'] == ('BD', 57, 63)
    # Abs
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_assignment_abs.xlsx", "ABS")
    # Band Assignment Qty
    assert verf_result[0]['B_1_Assignments_qty'] == 3
    assert verf_result[0]['B_2_Assignments_qty'] == 4
    assert verf_result[0]['B_3_Assignments_qty'] == 1
    # Band Assignment Number
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Number'] == '1'
    assert verf_result[1]['B_1_Assignment_1_Number'] == ('H', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Number'] == '2'
    assert verf_result[1]['B_1_Assignment_2_Number'] == ('H', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Number'] == '3'
    assert verf_result[1]['B_1_Assignment_3_Number'] == ('H', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Number'] == '1'
    assert verf_result[1]['B_2_Assignment_1_Number'] == ('H', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Number'] == '2'
    assert verf_result[1]['B_2_Assignment_2_Number'] == ('H', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Number'] == '3'
    assert verf_result[1]['B_2_Assignment_3_Number'] == ('H', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Number'] == '4'
    assert verf_result[1]['B_2_Assignment_4_Number'] == ('H', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Number'] == '1'
    assert verf_result[1]['B_3_Assignment_1_Number'] == ('H', 57, 57)
    # Band Assignment Label
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Label'] == 'I15'
    assert verf_result[1]['B_1_Assignment_1_Label'] == ('I', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Label'] == 'I27'
    assert verf_result[1]['B_1_Assignment_2_Label'] == ('I', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Label'] == 'I21'
    assert verf_result[1]['B_1_Assignment_3_Label'] == ('I', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Label'] == 'I51'
    assert verf_result[1]['B_2_Assignment_1_Label'] == ('I', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Label'] == 'I45'
    assert verf_result[1]['B_2_Assignment_2_Label'] == ('I', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Label'] == 'I39'
    assert verf_result[1]['B_2_Assignment_3_Label'] == ('I', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Label'] == 'I33'
    assert verf_result[1]['B_2_Assignment_4_Label'] == ('I', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Label'] == 'I57'
    assert verf_result[1]['B_3_Assignment_1_Label'] == ('I', 57, 57)
    # Band Assignment Symmetry
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Symmetry'] == 'E'
    assert verf_result[1]['B_1_Assignment_1_Symmetry'] == ('J', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Symmetry'] == 'E1'
    assert verf_result[1]['B_1_Assignment_2_Symmetry'] == ('J', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Symmetry'] == 'unknown'
    assert verf_result[1]['B_1_Assignment_3_Symmetry'] == ('J', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Symmetry'] == 'Au'
    assert verf_result[1]['B_2_Assignment_1_Symmetry'] == ('J', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Symmetry'] == 'A'
    assert verf_result[1]['B_2_Assignment_2_Symmetry'] == ('J', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Symmetry'] == 'NULL'
    assert verf_result[1]['B_2_Assignment_3_Symmetry'] == ('J', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Symmetry'] == 'Ag'
    assert verf_result[1]['B_2_Assignment_4_Symmetry'] == ('J', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Symmetry'] == 'A2g'
    assert verf_result[1]['B_3_Assignment_1_Symmetry'] == ('J', 57, 57)
    # Band Assignment Category
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Category'] == 'electronic transition'
    assert verf_result[1]['B_1_Assignment_1_Category'] == ('K', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Category'] == 'rotation'
    assert verf_result[1]['B_1_Assignment_2_Category'] == ('K', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Category'] == 'overtone vibration'
    assert verf_result[1]['B_1_Assignment_3_Category'] == ('K', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Category'] == 'combination'
    assert verf_result[1]['B_2_Assignment_1_Category'] == ('K', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Category'] == 'overtone rotation'
    assert verf_result[1]['B_2_Assignment_2_Category'] == ('K', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Category'] == 'unknown'
    assert verf_result[1]['B_2_Assignment_3_Category'] == ('K', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Category'] == 'other'
    assert verf_result[1]['B_2_Assignment_4_Category'] == ('K', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Category'] == 'phonon mode'
    assert verf_result[1]['B_3_Assignment_1_Category'] == ('K', 57, 57)
    # Band Assignment Method
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Method'] == 'L15'
    assert verf_result[1]['B_1_Assignment_1_Method'] == ('L', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Method'] == 'L27'
    assert verf_result[1]['B_1_Assignment_2_Method'] == ('L', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Method'] == 'L21'
    assert verf_result[1]['B_1_Assignment_3_Method'] == ('L', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Method'] == 'L51'
    assert verf_result[1]['B_2_Assignment_1_Method'] == ('L', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Method'] == 'L45'
    assert verf_result[1]['B_2_Assignment_2_Method'] == ('L', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Method'] == 'L39'
    assert verf_result[1]['B_2_Assignment_3_Method'] == ('L', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Method'] == 'L33'
    assert verf_result[1]['B_2_Assignment_4_Method'] == ('L', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Method'] == 'L57'
    assert verf_result[1]['B_3_Assignment_1_Method'] == ('L', 57, 57)
    # Band Assignment Level
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Level'] == 'fully assigned'
    assert verf_result[1]['B_1_Assignment_1_Level'] == ('M', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Level'] == 'partly assigned'
    assert verf_result[1]['B_1_Assignment_2_Level'] == ('M', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Level'] == ''
    assert verf_result[1]['B_1_Assignment_3_Level'] == ('M', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Level'] == 'NULL'
    assert verf_result[1]['B_2_Assignment_1_Level'] == ('M', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Level'] == 'uncertain assignment'
    assert verf_result[1]['B_2_Assignment_2_Level'] == ('M', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Level'] == 'species assigned'
    assert verf_result[1]['B_2_Assignment_3_Level'] == ('M', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Level'] == 'transition assigned'
    assert verf_result[1]['B_2_Assignment_4_Level'] == ('M', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Level'] == ''
    assert verf_result[1]['B_3_Assignment_1_Level'] == ('M', 57, 57)
    # Band Assignment Evaluation
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Evaluation'] == ''
    assert verf_result[1]['B_1_Assignment_1_Evaluation'] == ('N', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Assignment_2_Evaluation'] == ('N', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Assignment_3_Evaluation'] == ('N', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Evaluation'] == ''
    assert verf_result[1]['B_2_Assignment_1_Evaluation'] == ('N', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Evaluation'] == 'with caution'
    assert verf_result[1]['B_2_Assignment_2_Evaluation'] == ('N', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Assignment_3_Evaluation'] == ('N', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Evaluation'] == 'validated'
    assert verf_result[1]['B_2_Assignment_4_Evaluation'] == ('N', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Evaluation'] == 'NULL'
    assert verf_result[1]['B_3_Assignment_1_Evaluation'] == ('N', 57, 57)
    # Band Assignment Comment
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Comment'] == 'O15'
    assert verf_result[1]['B_1_Assignment_1_Comment'] == ('O', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Comment'] == 'O27'
    assert verf_result[1]['B_1_Assignment_2_Comment'] == ('O', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Comment'] == 'O21'
    assert verf_result[1]['B_1_Assignment_3_Comment'] == ('O', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Comment'] == 'O51'
    assert verf_result[1]['B_2_Assignment_1_Comment'] == ('O', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Comment'] == 'O45'
    assert verf_result[1]['B_2_Assignment_2_Comment'] == ('O', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Comment'] == 'O39'
    assert verf_result[1]['B_2_Assignment_3_Comment'] == ('O', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Comment'] == 'O33'
    assert verf_result[1]['B_2_Assignment_4_Comment'] == ('O', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Comment'] == 'O57'
    assert verf_result[1]['B_3_Assignment_1_Comment'] == ('O', 57, 57)
    # Band Assignment Multiplicity Types
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Multiplicity_Types'] == ['', 'no', 'mode degeneracy', 'site degeneracy', 'rotational structure', 'other']
    assert verf_result[1]['B_1_Assignment_1_Multiplicity_Types'] == ('R', 15, 20)
    assert verf_result[0]['B_1_Assignment_2_Multiplicity_Types'] == ['mode degeneracy', 'rotational structure', 'other', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Multiplicity_Types'] == ('R', 27, 32)
    assert verf_result[0]['B_1_Assignment_3_Multiplicity_Types'] == ['no', '', 'rotational structure', '', 'other constituent specie', '']
    assert verf_result[1]['B_1_Assignment_3_Multiplicity_Types'] == ('R', 21, 26)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Multiplicity_Types'] == ['other', '', 'other isotope specie', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Multiplicity_Types'] == ('R', 51, 56)
    assert verf_result[0]['B_2_Assignment_2_Multiplicity_Types'] == ['accidental degeneracy', '', 'other constituent specie', 'accidental degeneracy', '', '']
    assert verf_result[1]['B_2_Assignment_2_Multiplicity_Types'] == ('R', 45, 50)
    assert verf_result[0]['B_2_Assignment_3_Multiplicity_Types'] == ['rotational structure', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Multiplicity_Types'] == ('R', 39, 44)
    assert verf_result[0]['B_2_Assignment_4_Multiplicity_Types'] == ['site degeneracy', '', '', '', 'other isotope specie', 'no']
    assert verf_result[1]['B_2_Assignment_4_Multiplicity_Types'] == ('R', 33, 38)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Multiplicity_Types'] == ['unknown', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Multiplicity_Types'] == ('R', 57, 63)
    # Band Assignment Multiplicity Degeneracy
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Multiplicity_Degeneracy'] == ['', 'no', 'double', 'triple', 'quadruple', 'accidental double']
    assert verf_result[1]['B_1_Assignment_1_Multiplicity_Degeneracy'] == ('S', 15, 20)
    assert verf_result[0]['B_1_Assignment_2_Multiplicity_Degeneracy'] == ['accidental double', 'accidental triple', 'other', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Multiplicity_Degeneracy'] == ('S', 27, 32)
    assert verf_result[0]['B_1_Assignment_3_Multiplicity_Degeneracy'] == ['NULL', 'triple site', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Multiplicity_Degeneracy'] == ('S', 21, 26)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Multiplicity_Degeneracy'] == ['triple', '', '', 'double', '', '']
    assert verf_result[1]['B_2_Assignment_1_Multiplicity_Degeneracy'] == ('S', 51, 56)
    assert verf_result[0]['B_2_Assignment_2_Multiplicity_Degeneracy'] == ['no', '', 'accidental double', '', '', 'unknown']
    assert verf_result[1]['B_2_Assignment_2_Multiplicity_Degeneracy'] == ('S', 45, 50)
    assert verf_result[0]['B_2_Assignment_3_Multiplicity_Degeneracy'] == ['triple', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Multiplicity_Degeneracy'] == ('S', 39, 44)
    assert verf_result[0]['B_2_Assignment_4_Multiplicity_Degeneracy'] == ['quadruple', '', 'other', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Multiplicity_Degeneracy'] == ('S', 33, 38)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Multiplicity_Degeneracy'] == ['unknown', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Multiplicity_Degeneracy'] == ('S', 57, 63)
    # Band Assignment Multiplicity Other band
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Multiplicity_Other_band'] == ['T15', 'T16', 'T17', 'T18', 'T19', 'T20']
    assert verf_result[1]['B_1_Assignment_1_Multiplicity_Other_band'] == ('T', 15, 20)
    assert verf_result[0]['B_1_Assignment_2_Multiplicity_Other_band'] == ['T27', 'T28', 'T29', '', 'T31', '']
    assert verf_result[1]['B_1_Assignment_2_Multiplicity_Other_band'] == ('T', 27, 32)
    assert verf_result[0]['B_1_Assignment_3_Multiplicity_Other_band'] == ['T21', '', 'T23', '', '', 'T26']
    assert verf_result[1]['B_1_Assignment_3_Multiplicity_Other_band'] == ('T', 21, 26)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Multiplicity_Other_band'] == ['T51', '', 'T53', 'T54', '', '']
    assert verf_result[1]['B_2_Assignment_1_Multiplicity_Other_band'] == ('T', 51, 56)
    assert verf_result[0]['B_2_Assignment_2_Multiplicity_Other_band'] == ['T45', '', 'T47', '', 'T49', '']
    assert verf_result[1]['B_2_Assignment_2_Multiplicity_Other_band'] == ('T', 45, 50)
    assert verf_result[0]['B_2_Assignment_3_Multiplicity_Other_band'] == ['T39', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Multiplicity_Other_band'] == ('T', 39, 44)
    assert verf_result[0]['B_2_Assignment_4_Multiplicity_Other_band'] == ['T33', 'T34', 'T35', '', '', 'T38']
    assert verf_result[1]['B_2_Assignment_4_Multiplicity_Other_band'] == ('T', 33, 38)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Multiplicity_Other_band'] == ['T57', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Multiplicity_Other_band'] == ('T', 57, 63)
    # Band Assignment Multiplicity Level
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Contribution_Level'] == ''
    assert verf_result[1]['B_1_Assignment_1_Contribution_Level'] == ('U', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Contribution_Level'] == ''
    assert verf_result[1]['B_1_Assignment_2_Contribution_Level'] == ('U', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Contribution_Level'] == 'NULL'
    assert verf_result[1]['B_1_Assignment_3_Contribution_Level'] == ('U', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Contribution_Level'] == 'major'
    assert verf_result[1]['B_2_Assignment_1_Contribution_Level'] == ('U', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Contribution_Level'] == 'medium'
    assert verf_result[1]['B_2_Assignment_2_Contribution_Level'] == ('U', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Contribution_Level'] == 'minor'
    assert verf_result[1]['B_2_Assignment_3_Contribution_Level'] == ('U', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Contribution_Level'] == 'extracted'
    assert verf_result[1]['B_2_Assignment_4_Contribution_Level'] == ('U', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Contribution_Level'] == 'unknown'
    assert verf_result[1]['B_3_Assignment_1_Contribution_Level'] == ('U', 57, 57)
    # Band Assignment Multiplicity Comment
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Contribution_Comment'] == 'V15'
    assert verf_result[1]['B_1_Assignment_1_Contribution_Comment'] == ('V', 15, 15)
    assert verf_result[0]['B_1_Assignment_2_Contribution_Comment'] == 'V27'
    assert verf_result[1]['B_1_Assignment_2_Contribution_Comment'] == ('V', 27, 27)
    assert verf_result[0]['B_1_Assignment_3_Contribution_Comment'] == 'V21'
    assert verf_result[1]['B_1_Assignment_3_Contribution_Comment'] == ('V', 21, 21)
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Contribution_Comment'] == 'V51'
    assert verf_result[1]['B_2_Assignment_1_Contribution_Comment'] == ('V', 51, 51)
    assert verf_result[0]['B_2_Assignment_2_Contribution_Comment'] == 'V45'
    assert verf_result[1]['B_2_Assignment_2_Contribution_Comment'] == ('V', 45, 45)
    assert verf_result[0]['B_2_Assignment_3_Contribution_Comment'] == 'V39'
    assert verf_result[1]['B_2_Assignment_3_Contribution_Comment'] == ('V', 39, 39)
    assert verf_result[0]['B_2_Assignment_4_Contribution_Comment'] == 'V33'
    assert verf_result[1]['B_2_Assignment_4_Contribution_Comment'] == ('V', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Contribution_Comment'] == 'V57'
    assert verf_result[1]['B_3_Assignment_1_Contribution_Comment'] == ('V', 57, 57)
    # Band Assignment Transition Qty
    # Band 1
    assert verf_result[0]['B_1_Assignment_1_Transition_Species_qty'] == 6
    assert verf_result[0]['B_1_Assignment_2_Transition_Species_qty'] == 3
    assert verf_result[0]['B_1_Assignment_3_Transition_Species_qty'] == 2
    # Band 2
    assert verf_result[0]['B_2_Assignment_1_Transition_Species_qty'] == 2
    assert verf_result[0]['B_2_Assignment_2_Transition_Species_qty'] == 3
    assert verf_result[0]['B_2_Assignment_3_Transition_Species_qty'] == 2
    assert verf_result[0]['B_2_Assignment_4_Transition_Species_qty'] == 1
    # Band 3
    assert verf_result[0]['B_3_Assignment_1_Transition_Species_qty'] == 1
    # Band Assignment Transition Specie UID
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_1_UID'] == 'Y15'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_1_UID'] == ('Y', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_2_UID'] == 'Y16'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_2_UID'] == ('Y', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_3_UID'] == 'Y17'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_3_UID'] == ('Y', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_4_UID'] == 'Y18'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_4_UID'] == ('Y', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_5_UID'] == 'Y19'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_5_UID'] == ('Y', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Transition_Specie_6_UID'] == 'Y20'
    assert verf_result[1]['B_1_Assignment_1_Transition_Specie_6_UID'] == ('Y', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Transition_Specie_1_UID'] == 'Y27'
    assert verf_result[1]['B_1_Assignment_2_Transition_Specie_1_UID'] == ('Y', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Transition_Specie_2_UID'] == 'Y28'
    assert verf_result[1]['B_1_Assignment_2_Transition_Specie_2_UID'] == ('Y', 28, 28)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Transition_Specie_3_UID'] == 'Y31'
    assert verf_result[1]['B_1_Assignment_2_Transition_Specie_3_UID'] == ('Y', 31, 31)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Transition_Specie_1_UID'] == 'Y21'
    assert verf_result[1]['B_1_Assignment_3_Transition_Specie_1_UID'] == ('Y', 21, 21)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Transition_Specie_2_UID'] == 'Y23'
    assert verf_result[1]['B_1_Assignment_3_Transition_Specie_2_UID'] == ('Y', 23, 23)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Transition_Specie_1_UID'] == 'Y51'
    assert verf_result[1]['B_2_Assignment_1_Transition_Specie_1_UID'] == ('Y', 51, 51)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Transition_Specie_2_UID'] == 'Y53'
    assert verf_result[1]['B_2_Assignment_1_Transition_Specie_2_UID'] == ('Y', 53, 53)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Transition_Specie_1_UID'] == 'Y45'
    assert verf_result[1]['B_2_Assignment_2_Transition_Specie_1_UID'] == ('Y', 45, 45)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Transition_Specie_2_UID'] == 'Y48'
    assert verf_result[1]['B_2_Assignment_2_Transition_Specie_2_UID'] == ('Y', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Transition_Specie_3_UID'] == 'Y49'
    assert verf_result[1]['B_2_Assignment_2_Transition_Specie_3_UID'] == ('Y', 49, 49)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Transition_Specie_1_UID'] == 'Y39'
    assert verf_result[1]['B_2_Assignment_3_Transition_Specie_1_UID'] == ('Y', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Transition_Specie_2_UID'] == 'Y40'
    assert verf_result[1]['B_2_Assignment_3_Transition_Specie_2_UID'] == ('Y', 40, 40)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Transition_Specie_1_UID'] == 'Y33'
    assert verf_result[1]['B_2_Assignment_4_Transition_Specie_1_UID'] == ('Y', 33, 33)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Transition_Specie_1_UID'] == 'Y57'
    assert verf_result[1]['B_3_Assignment_1_Transition_Specie_1_UID'] == ('Y', 57, 57)
    # Band Assignment Transition Site Molecule labels
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Molecule_labels'] == ['Z15']
    assert verf_result[1]['B_1_Assignment_1_Site_1_Molecule_labels'] == ('Z', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Molecule_labels'] == ['Z16']
    assert verf_result[1]['B_1_Assignment_1_Site_2_Molecule_labels'] == ('Z', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Molecule_labels'] == ['Z17']
    assert verf_result[1]['B_1_Assignment_1_Site_3_Molecule_labels'] == ('Z', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Molecule_labels'] == ['Z18']
    assert verf_result[1]['B_1_Assignment_1_Site_4_Molecule_labels'] == ('Z', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Molecule_labels'] == ['Z19']
    assert verf_result[1]['B_1_Assignment_1_Site_5_Molecule_labels'] == ('Z', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Molecule_labels'] == ['Z20']
    assert verf_result[1]['B_1_Assignment_1_Site_6_Molecule_labels'] == ('Z', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Molecule_labels'] == ['Z27']
    assert verf_result[1]['B_1_Assignment_2_Site_1_Molecule_labels'] == ('Z', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Molecule_labels'] == ['Z28', 'Z29', '']
    assert verf_result[1]['B_1_Assignment_2_Site_2_Molecule_labels'] == ('Z', 28, 30)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Molecule_labels'] == ['Z31', 'Z32']
    assert verf_result[1]['B_1_Assignment_2_Site_3_Molecule_labels'] == ('Z', 31, 32)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Molecule_labels'] == ['Z21', '']
    assert verf_result[1]['B_1_Assignment_3_Site_1_Molecule_labels'] == ('Z', 21, 22)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Molecule_labels'] == ['Z23', 'Z24', '', '']
    assert verf_result[1]['B_1_Assignment_3_Site_2_Molecule_labels'] == ('Z', 23, 26)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Molecule_labels'] == ['Z51', 'Z52']
    assert verf_result[1]['B_2_Assignment_1_Site_1_Molecule_labels'] == ('Z', 51, 52)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Molecule_labels'] == ['Z53', '', 'Z55', 'Z56']
    assert verf_result[1]['B_2_Assignment_1_Site_2_Molecule_labels'] == ('Z', 53, 56)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Molecule_labels'] == ['Z45', 'Z46', '']
    assert verf_result[1]['B_2_Assignment_2_Site_1_Molecule_labels'] == ('Z', 45, 47)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Molecule_labels'] == ['Z48']
    assert verf_result[1]['B_2_Assignment_2_Site_2_Molecule_labels'] == ('Z', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Molecule_labels'] == ['Z49', 'Z50']
    assert verf_result[1]['B_2_Assignment_2_Site_3_Molecule_labels'] == ('Z', 49, 50)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Molecule_labels'] == ['Z39']
    assert verf_result[1]['B_2_Assignment_3_Site_1_Molecule_labels'] == ('Z', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Molecule_labels'] == ['Z40', '', 'Z42', '', '']
    assert verf_result[1]['B_2_Assignment_3_Site_2_Molecule_labels'] == ('Z', 40, 44)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Molecule_labels'] == ['Z33', '', 'Z35', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Site_1_Molecule_labels'] == ('Z', 33, 38)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Molecule_labels'] == ['Z57', '', '', 'Z60', 'Z61', '', '']
    assert verf_result[1]['B_3_Assignment_1_Site_1_Molecule_labels'] == ('Z', 57, 63)
    # Band Assignment Transition Site Molecule Symm. labels
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Molecule_Symm_label'] == ['AA15']
    assert verf_result[1]['B_1_Assignment_1_Site_1_Molecule_Symm_label'] == ('AA', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Molecule_Symm_label'] == ['AA16']
    assert verf_result[1]['B_1_Assignment_1_Site_2_Molecule_Symm_label'] == ('AA', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Molecule_Symm_label'] == ['AA17']
    assert verf_result[1]['B_1_Assignment_1_Site_3_Molecule_Symm_label'] == ('AA', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Molecule_Symm_label'] == ['AA18']
    assert verf_result[1]['B_1_Assignment_1_Site_4_Molecule_Symm_label'] == ('AA', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Molecule_Symm_label'] == ['AA19']
    assert verf_result[1]['B_1_Assignment_1_Site_5_Molecule_Symm_label'] == ('AA', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Molecule_Symm_label'] == ['AA20']
    assert verf_result[1]['B_1_Assignment_1_Site_6_Molecule_Symm_label'] == ('AA', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Molecule_Symm_label'] == ['AA27']
    assert verf_result[1]['B_1_Assignment_2_Site_1_Molecule_Symm_label'] == ('AA', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Molecule_Symm_label'] == ['AA28', 'AA29', 'AA30']
    assert verf_result[1]['B_1_Assignment_2_Site_2_Molecule_Symm_label'] == ('AA', 28, 30)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Molecule_Symm_label'] == ['AA31', 'AA32']
    assert verf_result[1]['B_1_Assignment_2_Site_3_Molecule_Symm_label'] == ('AA', 31, 32)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Molecule_Symm_label'] == ['AA21', 'AA22']
    assert verf_result[1]['B_1_Assignment_3_Site_1_Molecule_Symm_label'] == ('AA', 21, 22)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Molecule_Symm_label'] == ['AA23', 'AA24', 'AA25', '']
    assert verf_result[1]['B_1_Assignment_3_Site_2_Molecule_Symm_label'] == ('AA', 23, 26)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Molecule_Symm_label'] == ['AA51', 'AA52']
    assert verf_result[1]['B_2_Assignment_1_Site_1_Molecule_Symm_label'] == ('AA', 51, 52)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Molecule_Symm_label'] == ['AA53', 'AA54', 'AA55', 'AA56']
    assert verf_result[1]['B_2_Assignment_1_Site_2_Molecule_Symm_label'] == ('AA', 53, 56)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Molecule_Symm_label'] == ['AA45', 'AA46', 'AA47']
    assert verf_result[1]['B_2_Assignment_2_Site_1_Molecule_Symm_label'] == ('AA', 45, 47)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Molecule_Symm_label'] == ['AA48']
    assert verf_result[1]['B_2_Assignment_2_Site_2_Molecule_Symm_label'] == ('AA', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Molecule_Symm_label'] == ['AA49', 'AA50']
    assert verf_result[1]['B_2_Assignment_2_Site_3_Molecule_Symm_label'] == ('AA', 49, 50)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Molecule_Symm_label'] == ['AA39']
    assert verf_result[1]['B_2_Assignment_3_Site_1_Molecule_Symm_label'] == ('AA', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Molecule_Symm_label'] == ['AA40', 'AA41', 'AA42', 'AA43', '']
    assert verf_result[1]['B_2_Assignment_3_Site_2_Molecule_Symm_label'] == ('AA', 40, 44)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Molecule_Symm_label'] == ['AA33', 'AA34', 'AA35', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Site_1_Molecule_Symm_label'] == ('AA', 33, 38)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Molecule_Symm_label'] == ['AA57', 'AA58', '', 'AA60', 'AA61', 'AA62', '']
    assert verf_result[1]['B_3_Assignment_1_Site_1_Molecule_Symm_label'] == ('AA', 57, 63)
    # Band Assignment Transition Site Atom Labels
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Atom_Labels'] == ['AB15']
    assert verf_result[1]['B_1_Assignment_1_Site_1_Atom_Labels'] == ('AB', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Atom_Labels'] == ['AB16']
    assert verf_result[1]['B_1_Assignment_1_Site_2_Atom_Labels'] == ('AB', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Atom_Labels'] == ['AB17']
    assert verf_result[1]['B_1_Assignment_1_Site_3_Atom_Labels'] == ('AB', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Atom_Labels'] == ['AB18']
    assert verf_result[1]['B_1_Assignment_1_Site_4_Atom_Labels'] == ('AB', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Atom_Labels'] == ['AB19']
    assert verf_result[1]['B_1_Assignment_1_Site_5_Atom_Labels'] == ('AB', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Atom_Labels'] == ['AB20']
    assert verf_result[1]['B_1_Assignment_1_Site_6_Atom_Labels'] == ('AB', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Atom_Labels'] == ['AB27']
    assert verf_result[1]['B_1_Assignment_2_Site_1_Atom_Labels'] == ('AB', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Atom_Labels'] == ['AB28']
    assert verf_result[1]['B_1_Assignment_2_Site_2_Atom_Labels'] == ('AB', 28, 28)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Atom_Labels'] == ['AB31']
    assert verf_result[1]['B_1_Assignment_2_Site_3_Atom_Labels'] == ('AB', 31, 31)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Atom_Labels'] == ['AB21', 'AB22']
    assert verf_result[1]['B_1_Assignment_3_Site_1_Atom_Labels'] == ('AB', 21, 22)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Atom_Labels'] == ['AB23', 'AB24']
    assert verf_result[1]['B_1_Assignment_3_Site_2_Atom_Labels'] == ('AB', 23, 24)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Atom_Labels'] == ['AB51', 'AB52']
    assert verf_result[1]['B_2_Assignment_1_Site_1_Atom_Labels'] == ('AB', 51, 52)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Atom_Labels'] == ['AB53']
    assert verf_result[1]['B_2_Assignment_1_Site_2_Atom_Labels'] == ('AB', 53, 53)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Atom_Labels'] == ['AB45']
    assert verf_result[1]['B_2_Assignment_2_Site_1_Atom_Labels'] == ('AB', 45, 45)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Atom_Labels'] == ['AB48']
    assert verf_result[1]['B_2_Assignment_2_Site_2_Atom_Labels'] == ('AB', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Atom_Labels'] == ['AB49', 'AB50']
    assert verf_result[1]['B_2_Assignment_2_Site_3_Atom_Labels'] == ('AB', 49, 50)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Atom_Labels'] == ['AB39']
    assert verf_result[1]['B_2_Assignment_3_Site_1_Atom_Labels'] == ('AB', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Atom_Labels'] == ['AB40', 'AB41']
    assert verf_result[1]['B_2_Assignment_3_Site_2_Atom_Labels'] == ('AB', 40, 41)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Atom_Labels'] == ['AB33', 'AB34']
    assert verf_result[1]['B_2_Assignment_4_Site_1_Atom_Labels'] == ('AB', 33, 34)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Atom_Labels'] == ['AB57', 'AB58', 'AB59', 'AB61']
    assert verf_result[1]['B_3_Assignment_1_Site_1_Atom_Labels'] == ('AB', 57, 61)
    # Band Assignment Transition Site Atom Comment
    # Band 1 Assignment 1 Specie 1
    assert verf_result[0]['B_1_Assignment_1_Site_1_Atom_Comment'] == 'AC15'
    assert verf_result[1]['B_1_Assignment_1_Site_1_Atom_Comment'] == ('AC', 15, 15)
    # Band 1 Assignment 1 Specie 2
    assert verf_result[0]['B_1_Assignment_1_Site_2_Atom_Comment'] == 'AC16'
    assert verf_result[1]['B_1_Assignment_1_Site_2_Atom_Comment'] == ('AC', 16, 16)
    # Band 1 Assignment 1 Specie 3
    assert verf_result[0]['B_1_Assignment_1_Site_3_Atom_Comment'] == 'AC17'
    assert verf_result[1]['B_1_Assignment_1_Site_3_Atom_Comment'] == ('AC', 17, 17)
    # Band 1 Assignment 1 Specie 4
    assert verf_result[0]['B_1_Assignment_1_Site_4_Atom_Comment'] == 'AC18'
    assert verf_result[1]['B_1_Assignment_1_Site_4_Atom_Comment'] == ('AC', 18, 18)
    # Band 1 Assignment 1 Specie 5
    assert verf_result[0]['B_1_Assignment_1_Site_5_Atom_Comment'] == 'AC19'
    assert verf_result[1]['B_1_Assignment_1_Site_5_Atom_Comment'] == ('AC', 19, 19)
    # Band 1 Assignment 1 Specie 6
    assert verf_result[0]['B_1_Assignment_1_Site_6_Atom_Comment'] == 'AC20'
    assert verf_result[1]['B_1_Assignment_1_Site_6_Atom_Comment'] == ('AC', 20, 20)
    # Band 1 Assignment 2 Specie 1
    assert verf_result[0]['B_1_Assignment_2_Site_1_Atom_Comment'] == 'AC27'
    assert verf_result[1]['B_1_Assignment_2_Site_1_Atom_Comment'] == ('AC', 27, 27)
    # Band 1 Assignment 2 Specie 2
    assert verf_result[0]['B_1_Assignment_2_Site_2_Atom_Comment'] == 'AC28'
    assert verf_result[1]['B_1_Assignment_2_Site_2_Atom_Comment'] == ('AC', 28, 28)
    # Band 1 Assignment 2 Specie 3
    assert verf_result[0]['B_1_Assignment_2_Site_3_Atom_Comment'] == 'AC31'
    assert verf_result[1]['B_1_Assignment_2_Site_3_Atom_Comment'] == ('AC', 31, 31)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_1_Atom_Comment'] == 'AC21'
    assert verf_result[1]['B_1_Assignment_3_Site_1_Atom_Comment'] == ('AC', 21, 21)
    # Band 1 Assignment 3 Specie 1
    assert verf_result[0]['B_1_Assignment_3_Site_2_Atom_Comment'] == 'AC23'
    assert verf_result[1]['B_1_Assignment_3_Site_2_Atom_Comment'] == ('AC', 23, 23)
    # Band 2 Assignment 1 Specie 1
    assert verf_result[0]['B_2_Assignment_1_Site_1_Atom_Comment'] == 'AC51'
    assert verf_result[1]['B_2_Assignment_1_Site_1_Atom_Comment'] == ('AC', 51, 51)
    # Band 2 Assignment 1 Specie 2
    assert verf_result[0]['B_2_Assignment_1_Site_2_Atom_Comment'] == 'AC53'
    assert verf_result[1]['B_2_Assignment_1_Site_2_Atom_Comment'] == ('AC', 53, 53)
    # Band 2 Assignment 2 Specie 1
    assert verf_result[0]['B_2_Assignment_2_Site_1_Atom_Comment'] == 'AC45'
    assert verf_result[1]['B_2_Assignment_2_Site_1_Atom_Comment'] == ('AC', 45, 45)
    # Band 2 Assignment 2 Specie 2
    assert verf_result[0]['B_2_Assignment_2_Site_2_Atom_Comment'] == 'AC48'
    assert verf_result[1]['B_2_Assignment_2_Site_2_Atom_Comment'] == ('AC', 48, 48)
    # Band 2 Assignment 2 Specie 3
    assert verf_result[0]['B_2_Assignment_2_Site_3_Atom_Comment'] == 'AC49'
    assert verf_result[1]['B_2_Assignment_2_Site_3_Atom_Comment'] == ('AC', 49, 49)
    # Band 2 Assignment 3 Specie 1
    assert verf_result[0]['B_2_Assignment_3_Site_1_Atom_Comment'] == 'AC39'
    assert verf_result[1]['B_2_Assignment_3_Site_1_Atom_Comment'] == ('AC', 39, 39)
    # Band 2 Assignment 3 Specie 2
    assert verf_result[0]['B_2_Assignment_3_Site_2_Atom_Comment'] == 'AC40'
    assert verf_result[1]['B_2_Assignment_3_Site_2_Atom_Comment'] == ('AC', 40, 40)
    # Band 2 Assignment 4 Specie 1
    assert verf_result[0]['B_2_Assignment_4_Site_1_Atom_Comment'] == 'AC33'
    assert verf_result[1]['B_2_Assignment_4_Site_1_Atom_Comment'] == ('AC', 33, 33)
    # Band 3 Assignment 1 Specie 1
    assert verf_result[0]['B_3_Assignment_1_Site_1_Atom_Comment'] == 'AC57'
    assert verf_result[1]['B_3_Assignment_1_Site_1_Atom_Comment'] == ('AC', 57, 57)
    # Band Assignment Electronic Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Electronic_Types'] == ['crystal field', 'ligand-to-metal charge-transfer', 'intervalence charge transfer', 'double exciton', 'other', 'unknown']
    assert verf_result[1]['B_1_Assignment_1_Electronic_Types'] == ('AF', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Electronic_Types'] == ['', '', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Electronic_Types'] == ('AF', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Electronic_Types'] == ['NULL', '', 'intervalence charge transfer', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Electronic_Types'] == ('AF', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Electronic_Types'] == ['crystal field', 'intervalence charge transfer', 'unknown', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Electronic_Types'] == ('AF', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Electronic_Types'] == ['double exciton', 'unknown', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_2_Electronic_Types'] == ('AF', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Electronic_Types'] == ['other', 'double exciton', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Electronic_Types'] == ('AF', 39, 44)
    # Band 2 Assignment 4
    assert verf_result[0]['B_2_Assignment_4_Electronic_Types'] == ['', 'ligand-to-metal charge-transfer', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Electronic_Types'] == ('AF', 33, 38)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Electronic_Types'] == ['intervalence charge transfer', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Electronic_Types'] == ('AF', 57, 63)
    # Band Assignment Electronic Labels
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Electronic_Labels'] == ['AG15', 'AG16', 'AG17', 'AG18', 'AG19', 'AG20']
    assert verf_result[1]['B_1_Assignment_1_Electronic_Labels'] == ('AG', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Electronic_Labels'] == ['', '', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Electronic_Labels'] == ('AG', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Electronic_Labels'] == ['AG21', 'AG22', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Electronic_Labels'] == ('AG', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Electronic_Labels'] == ['AG51', 'AG52', 'AG53', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Electronic_Labels'] == ('AG', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Electronic_Labels'] == ['', 'AG46', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_2_Electronic_Labels'] == ('AG', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Electronic_Labels'] == ['AG39', 'AG40', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Electronic_Labels'] == ('AG', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Electronic_Labels'] == ['AG57', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Electronic_Labels'] == ('AG', 57, 63)
    # Band Assignment Electronic Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Electronic_Comment'] == 'AH15'
    assert verf_result[1]['B_1_Assignment_1_Electronic_Comment'] == ('AH', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Electronic_Comment'] == ''
    assert verf_result[1]['B_1_Assignment_2_Electronic_Comment'] == ('AH', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Electronic_Comment'] == 'AH21'
    assert verf_result[1]['B_1_Assignment_3_Electronic_Comment'] == ('AH', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Electronic_Comment'] == 'AH51'
    assert verf_result[1]['B_2_Assignment_1_Electronic_Comment'] == ('AH', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Electronic_Comment'] == 'AH45'
    assert verf_result[1]['B_2_Assignment_2_Electronic_Comment'] == ('AH', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Electronic_Comment'] == 'AH39'
    assert verf_result[1]['B_2_Assignment_3_Electronic_Comment'] == ('AH', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Electronic_Comment'] == 'AH57'
    assert verf_result[1]['B_3_Assignment_1_Electronic_Comment'] == ('AH', 57, 57)
    # Band Assignment Vibrations qty
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Vibrations_qty'] == 6
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Vibrations_qty'] == 2
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Vibrations_qty'] == 4
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Vibrations_qty'] == 2
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Vibrations_qty'] == 2
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Vibrations_qty'] == 3
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Vibrations_qty'] == 1
    # Band Assignment Vibration Types
    # Band 1 Assignment 1 Vibration 1
    assert verf_result[0]['B_1_Assignment_1_Vibration_1_Types'] == 'stretching'
    assert verf_result[1]['B_1_Assignment_1_Vibration_1_Types'] == ('AK', 15, 15)
    # Band 1 Assignment 1 Vibration 2
    assert verf_result[0]['B_1_Assignment_1_Vibration_2_Types'] == 'stretching sym.'
    assert verf_result[1]['B_1_Assignment_1_Vibration_2_Types'] == ('AK', 16, 16)
    # Band 1 Assignment 1 Vibration 3
    assert verf_result[0]['B_1_Assignment_1_Vibration_3_Types'] == 'stretching asym.'
    assert verf_result[1]['B_1_Assignment_1_Vibration_3_Types'] == ('AK', 17, 17)
    # Band 1 Assignment 1 Vibration 4
    assert verf_result[0]['B_1_Assignment_1_Vibration_4_Types'] == 'bending'
    assert verf_result[1]['B_1_Assignment_1_Vibration_4_Types'] == ('AK', 18, 18)
    # Band 1 Assignment 1 Vibration 5
    assert verf_result[0]['B_1_Assignment_1_Vibration_5_Types'] == 'bending in-p'
    assert verf_result[1]['B_1_Assignment_1_Vibration_5_Types'] == ('AK', 19, 19)
    # Band 1 Assignment 1 Vibration 6
    assert verf_result[0]['B_1_Assignment_1_Vibration_6_Types'] == 'bending out-p'
    assert verf_result[1]['B_1_Assignment_1_Vibration_6_Types'] == ('AK', 20, 20)
    # Band 1 Assignment 2 Vibration 1
    assert verf_result[0]['B_1_Assignment_2_Vibration_1_Types'] == 'bending asym. in-p (rocking)'
    assert verf_result[1]['B_1_Assignment_2_Vibration_1_Types'] == ('AK', 27, 27)
    # Band 1 Assignment 2 Vibration 2
    assert verf_result[0]['B_1_Assignment_2_Vibration_2_Types'] == 'bending sym. out-p (wagging)'
    assert verf_result[1]['B_1_Assignment_2_Vibration_2_Types'] == ('AK', 29, 29)
    # Band 1 Assignment 3 Vibration 1
    assert verf_result[0]['B_1_Assignment_3_Vibration_1_Types'] == 'bending sym.'
    assert verf_result[1]['B_1_Assignment_3_Vibration_1_Types'] == ('AK', 21, 21)
    # Band 1 Assignment 3 Vibration 2
    assert verf_result[0]['B_1_Assignment_3_Vibration_2_Types'] == 'bending asym.'
    assert verf_result[1]['B_1_Assignment_3_Vibration_2_Types'] == ('AK', 22, 22)
    # Band 1 Assignment 3 Vibration 3
    assert verf_result[0]['B_1_Assignment_3_Vibration_3_Types'] == 'bending sym. in-p (scissoring)'
    assert verf_result[1]['B_1_Assignment_3_Vibration_3_Types'] == ('AK', 23, 23)
    # Band 1 Assignment 3 Vibration 4
    assert verf_result[0]['B_1_Assignment_3_Vibration_4_Types'] == ''
    assert verf_result[1]['B_1_Assignment_3_Vibration_4_Types'] == ('AK', 24, 24)
    # Band 2 Assignment 1 Vibration 1
    assert verf_result[0]['B_2_Assignment_1_Vibration_1_Types'] == 'unknown'
    assert verf_result[1]['B_2_Assignment_1_Vibration_1_Types'] == ('AK', 51, 51)
    # Band 2 Assignment 1 Vibration 2
    assert verf_result[0]['B_2_Assignment_1_Vibration_2_Types'] == 'stretching asym.'
    assert verf_result[1]['B_2_Assignment_1_Vibration_2_Types'] == ('AK', 52, 52)
    # Band 2 Assignment 2 Vibration 1
    assert verf_result[0]['B_2_Assignment_2_Vibration_1_Types'] == 'other'
    assert verf_result[1]['B_2_Assignment_2_Vibration_1_Types'] == ('AK', 45, 45)
    # Band 2 Assignment 2 Vibration 2
    assert verf_result[0]['B_2_Assignment_2_Vibration_2_Types'] == 'NULL'
    assert verf_result[1]['B_2_Assignment_2_Vibration_2_Types'] == ('AK', 46, 46)
    # Band 2 Assignment 3 Vibration 1
    assert verf_result[0]['B_2_Assignment_3_Vibration_1_Types'] == 'deformation in-p'
    assert verf_result[1]['B_2_Assignment_3_Vibration_1_Types'] == ('AK', 39, 39)
    # Band 2 Assignment 3 Vibration 2
    assert verf_result[0]['B_2_Assignment_3_Vibration_2_Types'] == 'deformation out-p'
    assert verf_result[1]['B_2_Assignment_3_Vibration_2_Types'] == ('AK', 40, 40)
    # Band 2 Assignment 3 Vibration 3
    assert verf_result[0]['B_2_Assignment_3_Vibration_3_Types'] == 'deformation sym'
    assert verf_result[1]['B_2_Assignment_3_Vibration_3_Types'] == ('AK', 41, 41)
    # Band 3 Assignment 1 Vibration 1
    assert verf_result[0]['B_3_Assignment_1_Vibration_1_Types'] == ''
    assert verf_result[1]['B_3_Assignment_1_Vibration_1_Types'] == ('AK', 57, 57)
    # Band Assignment Vibration Label
    # Band 1 Assignment 1 Vibration 1
    assert verf_result[0]['B_1_Assignment_1_Vibration_1_Label'] == 'AL15'
    assert verf_result[1]['B_1_Assignment_1_Vibration_1_Label'] == ('AL', 15, 15)
    # Band 1 Assignment 1 Vibration 2
    assert verf_result[0]['B_1_Assignment_1_Vibration_2_Label'] == 'AL16'
    assert verf_result[1]['B_1_Assignment_1_Vibration_2_Label'] == ('AL', 16, 16)
    # Band 1 Assignment 1 Vibration 3
    assert verf_result[0]['B_1_Assignment_1_Vibration_3_Label'] == 'AL17'
    assert verf_result[1]['B_1_Assignment_1_Vibration_3_Label'] == ('AL', 17, 17)
    # Band 1 Assignment 1 Vibration 4
    assert verf_result[0]['B_1_Assignment_1_Vibration_4_Label'] == 'AL18'
    assert verf_result[1]['B_1_Assignment_1_Vibration_4_Label'] == ('AL', 18, 18)
    # Band 1 Assignment 1 Vibration 5
    assert verf_result[0]['B_1_Assignment_1_Vibration_5_Label'] == 'AL19'
    assert verf_result[1]['B_1_Assignment_1_Vibration_5_Label'] == ('AL', 19, 19)
    # Band 1 Assignment 1 Vibration 6
    assert verf_result[0]['B_1_Assignment_1_Vibration_6_Label'] == 'AL20'
    assert verf_result[1]['B_1_Assignment_1_Vibration_6_Label'] == ('AL', 20, 20)
    # Band 1 Assignment 2 Vibration 1
    assert verf_result[0]['B_1_Assignment_2_Vibration_1_Label'] == 'AL27'
    assert verf_result[1]['B_1_Assignment_2_Vibration_1_Label'] == ('AL', 27, 27)
    # Band 1 Assignment 2 Vibration 2
    assert verf_result[0]['B_1_Assignment_2_Vibration_2_Label'] == 'AL29'
    assert verf_result[1]['B_1_Assignment_2_Vibration_2_Label'] == ('AL', 29, 29)
    # Band 1 Assignment 3 Vibration 1
    assert verf_result[0]['B_1_Assignment_3_Vibration_1_Label'] == 'AL21'
    assert verf_result[1]['B_1_Assignment_3_Vibration_1_Label'] == ('AL', 21, 21)
    # Band 1 Assignment 3 Vibration 2
    assert verf_result[0]['B_1_Assignment_3_Vibration_2_Label'] == ''
    assert verf_result[1]['B_1_Assignment_3_Vibration_2_Label'] == ('AL', 22, 22)
    # Band 1 Assignment 3 Vibration 3
    assert verf_result[0]['B_1_Assignment_3_Vibration_3_Label'] == 'AL23'
    assert verf_result[1]['B_1_Assignment_3_Vibration_3_Label'] == ('AL', 23, 23)
    # Band 1 Assignment 3 Vibration 4
    assert verf_result[0]['B_1_Assignment_3_Vibration_4_Label'] == 'AL24'
    assert verf_result[1]['B_1_Assignment_3_Vibration_4_Label'] == ('AL', 24, 24)
    # Band 2 Assignment 1 Vibration 1
    assert verf_result[0]['B_2_Assignment_1_Vibration_1_Label'] == 'AL51'
    assert verf_result[1]['B_2_Assignment_1_Vibration_1_Label'] == ('AL', 51, 51)
    # Band 2 Assignment 1 Vibration 2
    assert verf_result[0]['B_2_Assignment_1_Vibration_2_Label'] == 'AL52'
    assert verf_result[1]['B_2_Assignment_1_Vibration_2_Label'] == ('AL', 52, 52)
    # Band 2 Assignment 2 Vibration 1
    assert verf_result[0]['B_2_Assignment_2_Vibration_1_Label'] == 'AL45'
    assert verf_result[1]['B_2_Assignment_2_Vibration_1_Label'] == ('AL', 45, 45)
    # Band 2 Assignment 2 Vibration 2
    assert verf_result[0]['B_2_Assignment_2_Vibration_2_Label'] == 'AL46'
    assert verf_result[1]['B_2_Assignment_2_Vibration_2_Label'] == ('AL', 46, 46)
    # Band 2 Assignment 3 Vibration 1
    assert verf_result[0]['B_2_Assignment_3_Vibration_1_Label'] == 'AL39'
    assert verf_result[1]['B_2_Assignment_3_Vibration_1_Label'] == ('AL', 39, 39)
    # Band 2 Assignment 3 Vibration 2
    assert verf_result[0]['B_2_Assignment_3_Vibration_2_Label'] == 'AL40'
    assert verf_result[1]['B_2_Assignment_3_Vibration_2_Label'] == ('AL', 40, 40)
    # Band 2 Assignment 3 Vibration 3
    assert verf_result[0]['B_2_Assignment_3_Vibration_3_Label'] == 'AL41'
    assert verf_result[1]['B_2_Assignment_3_Vibration_3_Label'] == ('AL', 41, 41)
    # Band 3 Assignment 1 Vibration 1
    assert verf_result[0]['B_3_Assignment_1_Vibration_1_Label'] == ''
    assert verf_result[1]['B_3_Assignment_1_Vibration_1_Label'] == ('AL', 57, 57)
    # Band Assignment Vibration Bonds
    # Band 1 Assignment 1 Vibration 1
    assert verf_result[0]['B_1_Assignment_1_Vibration_1_Bonds'] == ['AM15']
    assert verf_result[1]['B_1_Assignment_1_Vibration_1_Bonds'] == ('AM', 15, 15)
    # Band 1 Assignment 1 Vibration 2
    assert verf_result[0]['B_1_Assignment_1_Vibration_2_Bonds'] == ['AM16']
    assert verf_result[1]['B_1_Assignment_1_Vibration_2_Bonds'] == ('AM', 16, 16)
    # Band 1 Assignment 1 Vibration 3
    assert verf_result[0]['B_1_Assignment_1_Vibration_3_Bonds'] == ['AM17']
    assert verf_result[1]['B_1_Assignment_1_Vibration_3_Bonds'] == ('AM', 17, 17)
    # Band 1 Assignment 1 Vibration 4
    assert verf_result[0]['B_1_Assignment_1_Vibration_4_Bonds'] == ['AM18']
    assert verf_result[1]['B_1_Assignment_1_Vibration_4_Bonds'] == ('AM', 18, 18)
    # Band 1 Assignment 1 Vibration 5
    assert verf_result[0]['B_1_Assignment_1_Vibration_5_Bonds'] == ['AM19']
    assert verf_result[1]['B_1_Assignment_1_Vibration_5_Bonds'] == ('AM', 19, 19)
    # Band 1 Assignment 1 Vibration 6
    assert verf_result[0]['B_1_Assignment_1_Vibration_6_Bonds'] == ['AM20']
    assert verf_result[1]['B_1_Assignment_1_Vibration_6_Bonds'] == ('AM', 20, 20)
    # Band 1 Assignment 2 Vibration 1
    assert verf_result[0]['B_1_Assignment_2_Vibration_1_Bonds'] == ['AM27', 'AM28']
    assert verf_result[1]['B_1_Assignment_2_Vibration_1_Bonds'] == ('AM', 27, 28)
    # Band 1 Assignment 2 Vibration 2
    assert verf_result[0]['B_1_Assignment_2_Vibration_2_Bonds'] == ['AM29', 'AM31']
    assert verf_result[1]['B_1_Assignment_2_Vibration_2_Bonds'] == ('AM', 29, 31)
    # Band 1 Assignment 3 Vibration 1
    assert verf_result[0]['B_1_Assignment_3_Vibration_1_Bonds'] == ['AM21']
    assert verf_result[1]['B_1_Assignment_3_Vibration_1_Bonds'] == ('AM', 21, 21)
    # Band 1 Assignment 3 Vibration 2
    assert verf_result[0]['B_1_Assignment_3_Vibration_2_Bonds'] == ['AM22']
    assert verf_result[1]['B_1_Assignment_3_Vibration_2_Bonds'] == ('AM', 22, 22)
    # Band 1 Assignment 3 Vibration 3
    assert verf_result[0]['B_1_Assignment_3_Vibration_3_Bonds'] == ['AM23']
    assert verf_result[1]['B_1_Assignment_3_Vibration_3_Bonds'] == ('AM', 23, 23)
    # Band 1 Assignment 3 Vibration 4
    assert verf_result[0]['B_1_Assignment_3_Vibration_4_Bonds'] == ['']
    assert verf_result[1]['B_1_Assignment_3_Vibration_4_Bonds'] == ('', '', '')
    # Band 2 Assignment 1 Vibration 1
    assert verf_result[0]['B_2_Assignment_1_Vibration_1_Bonds'] == ['']
    assert verf_result[1]['B_2_Assignment_1_Vibration_1_Bonds'] == ('', '', '')
    # Band 2 Assignment 1 Vibration 2
    assert verf_result[0]['B_2_Assignment_1_Vibration_2_Bonds'] == ['AM52', 'AM53']
    assert verf_result[1]['B_2_Assignment_1_Vibration_2_Bonds'] == ('AM', 52, 53)
    # Band 2 Assignment 2 Vibration 1
    assert verf_result[0]['B_2_Assignment_2_Vibration_1_Bonds'] == ['AM45']
    assert verf_result[1]['B_2_Assignment_2_Vibration_1_Bonds'] == ('AM', 45, 45)
    # Band 2 Assignment 2 Vibration 2
    assert verf_result[0]['B_2_Assignment_2_Vibration_2_Bonds'] == ['']
    assert verf_result[1]['B_2_Assignment_2_Vibration_2_Bonds'] == ('', '', '')
    # Band 2 Assignment 3 Vibration 1
    assert verf_result[0]['B_2_Assignment_3_Vibration_1_Bonds'] == ['AM39']
    assert verf_result[1]['B_2_Assignment_3_Vibration_1_Bonds'] == ('AM', 39, 39)
    # Band 2 Assignment 3 Vibration 2
    assert verf_result[0]['B_2_Assignment_3_Vibration_2_Bonds'] == ['']
    assert verf_result[1]['B_2_Assignment_3_Vibration_2_Bonds'] == ('', '', '')
    # Band 2 Assignment 3 Vibration 3
    assert verf_result[0]['B_2_Assignment_3_Vibration_3_Bonds'] == ['AM41']
    assert verf_result[1]['B_2_Assignment_3_Vibration_3_Bonds'] == ('AM', 41, 41)
    # Band 3 Assignment 1 Vibration 1
    assert verf_result[0]['B_3_Assignment_1_Vibration_1_Bonds'] == ['']
    assert verf_result[1]['B_3_Assignment_1_Vibration_1_Bonds'] == ('AM', 57, 57)
    # Band Assignment Vibration Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Vibrations_Comment'] == 'AN15'
    assert verf_result[1]['B_1_Assignment_1_Vibrations_Comment'] == ('AN', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Vibrations_Comment'] == ''
    assert verf_result[1]['B_1_Assignment_2_Vibrations_Comment'] == ('AN', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Vibrations_Comment'] == 'AN21'
    assert verf_result[1]['B_1_Assignment_3_Vibrations_Comment'] == ('AN', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Vibrations_Comment'] == 'AN51'
    assert verf_result[1]['B_2_Assignment_1_Vibrations_Comment'] == ('AN', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Vibrations_Comment'] == 'AN45'
    assert verf_result[1]['B_2_Assignment_2_Vibrations_Comment'] == ('AN', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Vibrations_Comment'] == 'AN39'
    assert verf_result[1]['B_2_Assignment_3_Vibrations_Comment'] == ('AN', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Vibrations_Comment'] == 'AN57'
    assert verf_result[1]['B_3_Assignment_1_Vibrations_Comment'] == ('AN', 57, 57)
    # Band Assignment Rotation Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Rotation_Types'] == ['free rotation', 'hindered rotation', 'libration', 'other', 'unknown', 'NULL']
    assert verf_result[1]['B_1_Assignment_1_Rotation_Types'] == ('AQ', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Rotation_Types'] == ['free rotation', 'libration', 'NULL', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Rotation_Types'] == ('AQ', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Rotation_Types'] == ['free rotation', 'unknown', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Rotation_Types'] == ('AQ', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Rotation_Types'] == ['NULL', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Rotation_Types'] == ('AQ', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Rotation_Types'] == ['free rotation', '', 'unknown', 'NULL', '', '']
    assert verf_result[1]['B_2_Assignment_2_Rotation_Types'] == ('AQ', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Rotation_Types'] == ['free rotation', 'hindered rotation', 'unknown', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Rotation_Types'] == ('AQ', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Rotation_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Rotation_Types'] == ('AQ', 57, 63)
    # Band Assignment Rotation Label
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Rotation_Label'] == ['AR15', 'AR16', 'AR17', 'AR18', 'AR19', 'AR20']
    assert verf_result[1]['B_1_Assignment_1_Rotation_Label'] == ('AR', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Rotation_Label'] == ['AR27', '', 'AR29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Rotation_Label'] == ('AR', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Rotation_Label'] == ['AR21', 'AR22', 'AR23', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Rotation_Label'] == ('AR', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Rotation_Label'] == ['AR51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Rotation_Label'] == ('AR', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Rotation_Label'] == ['AR45', 'AR46', 'AR47', 'AR48', '', '']
    assert verf_result[1]['B_2_Assignment_2_Rotation_Label'] == ('AR', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Rotation_Label'] == ['AR39', 'AR40', 'AR41', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Rotation_Label'] == ('AR', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Rotation_Label'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Rotation_Label'] == ('AR', 57, 63)
    # Band Assignment Rotation Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Rotation_Comment'] == 'AS15'
    assert verf_result[1]['B_1_Assignment_1_Rotation_Comment'] == ('AS', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Rotation_Comment'] == 'AS27'
    assert verf_result[1]['B_1_Assignment_2_Rotation_Comment'] == ('AS', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Rotation_Comment'] == 'AS21'
    assert verf_result[1]['B_1_Assignment_3_Rotation_Comment'] == ('AS', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Rotation_Comment'] == 'AS51'
    assert verf_result[1]['B_2_Assignment_1_Rotation_Comment'] == ('AS', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Rotation_Comment'] == 'AS45'
    assert verf_result[1]['B_2_Assignment_2_Rotation_Comment'] == ('AS', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Rotation_Comment'] == 'AS39'
    assert verf_result[1]['B_2_Assignment_3_Rotation_Comment'] == ('AS', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Rotation_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Rotation_Comment'] == ('AS', 57, 57)
    # Band Assignment Phonon Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Phonon_Types'] == ['translation', 'longitudinal optic translation', 'transverse optic translation', 'longitudinal acoustic translation', 'transverse acoustic translation', 'other']
    assert verf_result[1]['B_1_Assignment_1_Phonon_Types'] == ('AV', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Phonon_Types'] == ['longitudinal optic translation', 'transverse acoustic translation', 'NULL', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Phonon_Types'] == ('AV', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Phonon_Types'] == ['unknown', 'NULL', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Phonon_Types'] == ('AV', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Phonon_Types'] == ['NULL', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Phonon_Types'] == ('AV', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Phonon_Types'] == ['translation', '', 'unknown', 'NULL', '', '']
    assert verf_result[1]['B_2_Assignment_2_Phonon_Types'] == ('AV', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Phonon_Types'] == ['longitudinal optic translation', 'other', 'NULL', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Phonon_Types'] == ('AV', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Phonon_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Phonon_Types'] == ('AV', 57, 63)
    # Band Assignment Phonon Label
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Phonon_Label'] == ['AW15', 'AW16', 'AW17', 'AW18', 'AW19', 'AW20']
    assert verf_result[1]['B_1_Assignment_1_Phonon_Label'] == ('AW', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Phonon_Label'] == ['AW27', '', 'AW29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Phonon_Label'] == ('AW', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Phonon_Label'] == ['AW21', 'AW22', 'AW23', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Phonon_Label'] == ('AW', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Phonon_Label'] == ['AW51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Phonon_Label'] == ('AW', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Phonon_Label'] == ['AW45', 'AW46', 'AW47', 'AW48', '', '']
    assert verf_result[1]['B_2_Assignment_2_Phonon_Label'] == ('AW', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Phonon_Label'] == ['AW39', 'AW40', 'AW41', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Phonon_Label'] == ('AW', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Phonon_Label'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Phonon_Label'] == ('AW', 57, 63)
    # Band Assignment Phonon Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Phonon_Comment'] == 'AX15'
    assert verf_result[1]['B_1_Assignment_1_Phonon_Comment'] == ('AX', 15, 15)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Phonon_Comment'] == 'AX27'
    assert verf_result[1]['B_1_Assignment_2_Phonon_Comment'] == ('AX', 27, 27)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Phonon_Comment'] == 'AX21'
    assert verf_result[1]['B_1_Assignment_3_Phonon_Comment'] == ('AX', 21, 21)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Phonon_Comment'] == 'AX51'
    assert verf_result[1]['B_2_Assignment_1_Phonon_Comment'] == ('AX', 51, 51)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Phonon_Comment'] == 'AX45'
    assert verf_result[1]['B_2_Assignment_2_Phonon_Comment'] == ('AX', 45, 45)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Phonon_Comment'] == 'AX39'
    assert verf_result[1]['B_2_Assignment_3_Phonon_Comment'] == ('AX', 39, 39)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Phonon_Comment'] == ''
    assert verf_result[1]['B_3_Assignment_1_Phonon_Comment'] == ('AX', 57, 57)
    # Band Assignment Resonances Types
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Types'] == ['Fermi resonance', 'electron-phonon coupling', 'rotational-vibrational coupling', 'vibration-phonon coupling', 'other', 'NULL']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Types'] == ('BA', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Types'] == ['Fermi resonance', 'unknown', 'NULL', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Types'] == ('BA', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Types'] == ['vibration-phonon coupling', 'NULL', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Types'] == ('BA', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Types'] == ['NULL', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Types'] == ('BA', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Types'] == ['electron-phonon coupling', '', 'unknown', 'NULL', '', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Types'] == ('BA', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Types'] == ['Fermi resonance', 'unknown', 'NULL', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Types'] == ('BA', 39, 44)
    # Band 2 Assignment 4
    assert verf_result[0]['B_2_Assignment_4_Resonances_Types'] == ['vibration-phonon coupling', 'unknown', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_4_Resonances_Types'] == ('BA', 33, 38)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Types'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Types'] == ('BA', 57, 63)
    # Band Assignment Resonances Band
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Band'] == ['BB15', 'BB16', 'BB17', 'BB18', 'BB19', 'BB20']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Band'] == ('BB', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Band'] == ['BB27', '', 'BB29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Band'] == ('BB', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Band'] == ['BB21', 'BB22', 'BB23', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Band'] == ('BB', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Band'] == ['BB51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Band'] == ('BB', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Band'] == ['BB45', 'BB46', '', '', 'BB49', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Band'] == ('BB', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Band'] == ['', 'BB40', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Band'] == ('BB', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Band'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Band'] == ('BB', 57, 63)
    # Band Assignment Resonances Nb
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Nb'] == ['1', '2', '3', '4', '5', '6']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Nb'] == ('BC', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Nb'] == ['1', '2', '3', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Nb'] == ('BC', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Nb'] == ['3', '1', '2', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Nb'] == ('BC', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Nb'] == ['1', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Nb'] == ('BC', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Nb'] == ['1', '5', '4', '2', '3', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Nb'] == ('BC', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Nb'] == ['1', '2', '3', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Nb'] == ('BC', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Nb'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Nb'] == ('BC', 57, 63)
    # Band Assignment Resonances Comment
    # Band 1 Assignment 1
    assert verf_result[0]['B_1_Assignment_1_Resonances_Comment'] == ['BD15', 'BD16', 'BD17', 'BD18', 'BD19', 'BD20']
    assert verf_result[1]['B_1_Assignment_1_Resonances_Comment'] == ('BD', 15, 20)
    # Band 1 Assignment 2
    assert verf_result[0]['B_1_Assignment_2_Resonances_Comment'] == ['', 'BD28', 'BD29', '', '', '']
    assert verf_result[1]['B_1_Assignment_2_Resonances_Comment'] == ('BD', 27, 32)
    # Band 1 Assignment 3
    assert verf_result[0]['B_1_Assignment_3_Resonances_Comment'] == ['BD21', 'BD22', '', '', '', '']
    assert verf_result[1]['B_1_Assignment_3_Resonances_Comment'] == ('BD', 21, 26)
    # Band 2 Assignment 1
    assert verf_result[0]['B_2_Assignment_1_Resonances_Comment'] == ['BD51', '', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_1_Resonances_Comment'] == ('BD', 51, 56)
    # Band 2 Assignment 2
    assert verf_result[0]['B_2_Assignment_2_Resonances_Comment'] == ['BD45', 'BD46', '', '', 'BD49', '']
    assert verf_result[1]['B_2_Assignment_2_Resonances_Comment'] == ('BD', 45, 50)
    # Band 2 Assignment 3
    assert verf_result[0]['B_2_Assignment_3_Resonances_Comment'] == ['BD39', 'BD40', '', '', '', '']
    assert verf_result[1]['B_2_Assignment_3_Resonances_Comment'] == ('BD', 39, 44)
    # Band 3 Assignment 1
    assert verf_result[0]['B_3_Assignment_1_Resonances_Comment'] == ['', '', '', '', '', '', '']
    assert verf_result[1]['B_3_Assignment_1_Resonances_Comment'] == ('BD', 57, 63)


# Band Publication
def test_read_band_publication():
    # Raman
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_publication_ram.xlsx", "RAMAN")
    # Band Publications UID
    # Band 1
    assert verf_result[0]['B_1_Publications_UID'] == ['BH15', 'BH16', 'BH17', 'BH18', 'BH19', 'BH20', 'BH23', 'BH21', 'BH27', 'BH29', 'BH31']
    assert verf_result[1]['B_1_Publications_UID'] == ('BH', 15, 32)
    # Band 2
    assert verf_result[0]['B_2_Publications_UID'] == ['BH34', 'BH36', 'BH33', 'BH37', 'BH39', 'BH40', 'BH41', 'BH42', 'BH48', 'BH52', 'BH54']
    assert verf_result[1]['B_2_Publications_UID'] == ('BH', 33, 56)
    # Band 3
    assert verf_result[0]['B_3_Publications_UID'] == ['']
    assert verf_result[1]['B_3_Publications_UID'] == ('BH', 57, 62)
    # Band Publications SSHADE UID
    # Band 1
    assert verf_result[0]['B_1_Publications_SSHADE_UID'] == ['BJ15', 'BJ16', 'BJ17', 'BJ18', 'BJ19', 'BJ20', 'BJ21', 'BJ23', 'BJ29', 'BJ31', 'BJ27']
    assert verf_result[1]['B_1_Publications_SSHADE_UID'] == ('BJ', 15, 32)
    # Band 2
    assert verf_result[0]['B_2_Publications_SSHADE_UID'] == ['BJ33', 'BJ35', 'BJ39', 'BJ41', 'BJ47', 'BJ45', 'BJ55', 'BJ53', 'BJ51', 'BJ52']
    assert verf_result[1]['B_2_Publications_SSHADE_UID'] == ('BJ', 33, 56)
    # Band 3
    assert verf_result[0]['B_3_Publications_SSHADE_UID'] == ['']
    assert verf_result[1]['B_3_Publications_SSHADE_UID'] == ('BJ', 57, 62)
    # Band Publications Data URL
    # Band 1
    assert verf_result[0]['B_1_Publications_Data_URL'] == ['BL15', 'BL22', 'BL30']
    assert verf_result[1]['B_1_Publications_Data_URL'] == ('BL', 15, 32)
    # Band 2
    assert verf_result[0]['B_2_Publications_Data_URL'] == ['BL47', 'BL44', 'BL35']
    assert verf_result[1]['B_2_Publications_Data_URL'] == ('BL', 33, 56)
    # Band 3
    assert verf_result[0]['B_3_Publications_Data_URL'] == ['']
    assert verf_result[1]['B_3_Publications_Data_URL'] == ('BL', 57, 62)
    # Band Publications Comments
    # Band 1
    assert verf_result[0]['B_1_Publications_Comments'] == 'BM15'
    assert verf_result[1]['B_1_Publications_Comments'] == ('BM', 15, 15)
    # Band 2
    assert verf_result[0]['B_2_Publications_Comments'] == ''
    assert verf_result[1]['B_2_Publications_Comments'] == ('BM', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Publications_Comments'] == ''
    assert verf_result[1]['B_3_Publications_Comments'] == ('BM', 57, 57)
    # Abs
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_publication_abs.xlsx", "ABS")
    # Band Publications UID
    # Band 1
    assert verf_result[0]['B_1_Publications_UID'] == ['BH15', 'BH16', 'BH17', 'BH18', 'BH19', 'BH20', 'BH23', 'BH21', 'BH27', 'BH29', 'BH31']
    assert verf_result[1]['B_1_Publications_UID'] == ('BH', 15, 32)
    # Band 2
    assert verf_result[0]['B_2_Publications_UID'] == ['BH34', 'BH36', 'BH33', 'BH37', 'BH39', 'BH40', 'BH41', 'BH42', 'BH48', 'BH52', 'BH54']
    assert verf_result[1]['B_2_Publications_UID'] == ('BH', 33, 56)
    # Band 3
    assert verf_result[0]['B_3_Publications_UID'] == ['']
    assert verf_result[1]['B_3_Publications_UID'] == ('BH', 57, 62)
    # Band Publications SSHADE UID
    # Band 1
    assert verf_result[0]['B_1_Publications_SSHADE_UID'] == ['BJ15', 'BJ16', 'BJ17', 'BJ18', 'BJ19', 'BJ20', 'BJ21', 'BJ23', 'BJ29', 'BJ31', 'BJ27']
    assert verf_result[1]['B_1_Publications_SSHADE_UID'] == ('BJ', 15, 32)
    # Band 2
    assert verf_result[0]['B_2_Publications_SSHADE_UID'] == ['BJ33', 'BJ35', 'BJ39', 'BJ41', 'BJ47', 'BJ45', 'BJ55', 'BJ53', 'BJ51', 'BJ52']
    assert verf_result[1]['B_2_Publications_SSHADE_UID'] == ('BJ', 33, 56)
    # Band 3
    assert verf_result[0]['B_3_Publications_SSHADE_UID'] == ['']
    assert verf_result[1]['B_3_Publications_SSHADE_UID'] == ('BJ', 57, 62)
    # Band Publications Data URL
    # Band 1
    assert verf_result[0]['B_1_Publications_Data_URL'] == ['BL15', 'BL22', 'BL30']
    assert verf_result[1]['B_1_Publications_Data_URL'] == ('BL', 15, 32)
    # Band 2
    assert verf_result[0]['B_2_Publications_Data_URL'] == ['BL47', 'BL44', 'BL35']
    assert verf_result[1]['B_2_Publications_Data_URL'] == ('BL', 33, 56)
    # Band 3
    assert verf_result[0]['B_3_Publications_Data_URL'] == ['']
    assert verf_result[1]['B_3_Publications_Data_URL'] == ('BL', 57, 62)
    # Band Publications Comments
    # Band 1
    assert verf_result[0]['B_1_Publications_Comments'] == 'BM15'
    assert verf_result[1]['B_1_Publications_Comments'] == ('BM', 15, 15)
    # Band 2
    assert verf_result[0]['B_2_Publications_Comments'] == ''
    assert verf_result[1]['B_2_Publications_Comments'] == ('BM', 33, 33)
    # Band 3
    assert verf_result[0]['B_3_Publications_Comments'] == ''
    assert verf_result[1]['B_3_Publications_Comments'] == ('BM', 57, 57)


# Band Characteristics
def test_read_band_characteristics():
    # Raman
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_characteristic_ram.xlsx", "RAMAN")
    # Band Characteristics qty
    # Band 1
    assert verf_result[0]['B_1_Characteristics_qty'] == 10
    # Band 2
    assert verf_result[0]['B_2_Characteristics_qty'] == 5
    # Band 3
    assert verf_result[0]['B_3_Characteristics_qty'] == 1
    # Band Characteristic Nb
    # Band 1 Characteristic 1 Nb
    assert verf_result[0]['B_1_Characteristic_1_Nb'] == '1'
    assert verf_result[1]['B_1_Characteristic_1_Nb'] == ('BP', 15, 15)
    # Band 1 Characteristic 2 Nb
    assert verf_result[0]['B_1_Characteristic_2_Nb'] == '2'
    assert verf_result[1]['B_1_Characteristic_2_Nb'] == ('BP', 16, 16)
    # Band 1 Characteristic 3 Nb
    assert verf_result[0]['B_1_Characteristic_3_Nb'] == '3'
    assert verf_result[1]['B_1_Characteristic_3_Nb'] == ('BP', 17, 17)
    # Band 1 Characteristic 4 Nb
    assert verf_result[0]['B_1_Characteristic_4_Nb'] == '4'
    assert verf_result[1]['B_1_Characteristic_4_Nb'] == ('BP', 18, 18)
    # Band 1 Characteristic 5 Nb
    assert verf_result[0]['B_1_Characteristic_5_Nb'] == '5'
    assert verf_result[1]['B_1_Characteristic_5_Nb'] == ('BP', 19, 19)
    # Band 1 Characteristic 6 Nb
    assert verf_result[0]['B_1_Characteristic_6_Nb'] == '6'
    assert verf_result[1]['B_1_Characteristic_6_Nb'] == ('BP', 20, 20)
    # Band 1 Characteristic 7 Nb
    assert verf_result[0]['B_1_Characteristic_7_Nb'] == '7'
    assert verf_result[1]['B_1_Characteristic_7_Nb'] == ('BP', 25, 25)
    # Band 1 Characteristic 8 Nb
    assert verf_result[0]['B_1_Characteristic_8_Nb'] == '8'
    assert verf_result[1]['B_1_Characteristic_8_Nb'] == ('BP', 26, 26)
    # Band 1 Characteristic 9 Nb
    assert verf_result[0]['B_1_Characteristic_9_Nb'] == '9'
    assert verf_result[1]['B_1_Characteristic_9_Nb'] == ('BP', 31, 31)
    # Band 1 Characteristic 10 Nb
    assert verf_result[0]['B_1_Characteristic_10_Nb'] == '10'
    assert verf_result[1]['B_1_Characteristic_10_Nb'] == ('BP', 32, 32)
    # Band 2 Characteristic 1 Nb
    assert verf_result[0]['B_2_Characteristic_1_Nb'] == '1'
    assert verf_result[1]['B_2_Characteristic_1_Nb'] == ('BP', 37, 37)
    # Band 2 Characteristic 2 Nb
    assert verf_result[0]['B_2_Characteristic_2_Nb'] == '2'
    assert verf_result[1]['B_2_Characteristic_2_Nb'] == ('BP', 38, 38)
    # Band 2 Characteristic 3 Nb
    assert verf_result[0]['B_2_Characteristic_3_Nb'] == '3'
    assert verf_result[1]['B_2_Characteristic_3_Nb'] == ('BP', 41, 41)
    # Band 2 Characteristic 4 Nb
    assert verf_result[0]['B_2_Characteristic_4_Nb'] == '4'
    assert verf_result[1]['B_2_Characteristic_4_Nb'] == ('BP', 45, 45)
    # Band 2 Characteristic 5 Nb
    assert verf_result[0]['B_2_Characteristic_5_Nb'] == '5'
    assert verf_result[1]['B_2_Characteristic_5_Nb'] == ('BP', 53, 53)
    # Band 3 Characteristic 1 Nb
    assert verf_result[0]['B_3_Characteristic_1_Nb'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Nb'] == ('BP', 57, 57)
    # Band Characteristic Composition
    # Band 1 Characteristic 1 Composition
    assert verf_result[0]['B_1_Characteristic_1_Composition'] == 'BQ15'
    assert verf_result[1]['B_1_Characteristic_1_Composition'] == ('BQ', 15, 15)
    # Band 1 Characteristic 2 Composition
    assert verf_result[0]['B_1_Characteristic_2_Composition'] == 'BQ16'
    assert verf_result[1]['B_1_Characteristic_2_Composition'] == ('BQ', 16, 16)
    # Band 1 Characteristic 3 Composition
    assert verf_result[0]['B_1_Characteristic_3_Composition'] == 'BQ17'
    assert verf_result[1]['B_1_Characteristic_3_Composition'] == ('BQ', 17, 17)
    # Band 1 Characteristic 4 Composition
    assert verf_result[0]['B_1_Characteristic_4_Composition'] == 'BQ18'
    assert verf_result[1]['B_1_Characteristic_4_Composition'] == ('BQ', 18, 18)
    # Band 1 Characteristic 5 Composition
    assert verf_result[0]['B_1_Characteristic_5_Composition'] == 'BQ19'
    assert verf_result[1]['B_1_Characteristic_5_Composition'] == ('BQ', 19, 19)
    # Band 1 Characteristic 6 Composition
    assert verf_result[0]['B_1_Characteristic_6_Composition'] == 'BQ20'
    assert verf_result[1]['B_1_Characteristic_6_Composition'] == ('BQ', 20, 20)
    # Band 1 Characteristic 7 Composition
    assert verf_result[0]['B_1_Characteristic_7_Composition'] == 'BQ25'
    assert verf_result[1]['B_1_Characteristic_7_Composition'] == ('BQ', 25, 25)
    # Band 1 Characteristic 8 Composition
    assert verf_result[0]['B_1_Characteristic_8_Composition'] == 'BQ26'
    assert verf_result[1]['B_1_Characteristic_8_Composition'] == ('BQ', 26, 26)
    # Band 1 Characteristic 9 Composition
    assert verf_result[0]['B_1_Characteristic_9_Composition'] == 'BQ31'
    assert verf_result[1]['B_1_Characteristic_9_Composition'] == ('BQ', 31, 31)
    # Band 1 Characteristic 10 Composition
    assert verf_result[0]['B_1_Characteristic_10_Composition'] == 'BQ32'
    assert verf_result[1]['B_1_Characteristic_10_Composition'] == ('BQ', 32, 32)
    # Band 2 Characteristic 1 Composition
    assert verf_result[0]['B_2_Characteristic_1_Composition'] == 'BQ37'
    assert verf_result[1]['B_2_Characteristic_1_Composition'] == ('BQ', 37, 37)
    # Band 2 Characteristic 2 Composition
    assert verf_result[0]['B_2_Characteristic_2_Composition'] == 'BQ38'
    assert verf_result[1]['B_2_Characteristic_2_Composition'] == ('BQ', 38, 38)
    # Band 2 Characteristic 3 Composition
    assert verf_result[0]['B_2_Characteristic_3_Composition'] == 'BQ41'
    assert verf_result[1]['B_2_Characteristic_3_Composition'] == ('BQ', 41, 41)
    # Band 2 Characteristic 4 Composition
    assert verf_result[0]['B_2_Characteristic_4_Composition'] == 'BQ45'
    assert verf_result[1]['B_2_Characteristic_4_Composition'] == ('BQ', 45, 45)
    # Band 2 Characteristic 5 Composition
    assert verf_result[0]['B_2_Characteristic_5_Composition'] == 'BQ53'
    assert verf_result[1]['B_2_Characteristic_5_Composition'] == ('BQ', 53, 53)
    # Band 3 Characteristic 1 Composition
    assert verf_result[0]['B_3_Characteristic_1_Composition'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Composition'] == ('BQ', 57, 57)
    # Band Characteristic Texture
    # Band 1 Characteristic 1 Texture
    assert verf_result[0]['B_1_Characteristic_1_Texture'] == 'BR15'
    assert verf_result[1]['B_1_Characteristic_1_Texture'] == ('BR', 15, 15)
    # Band 1 Characteristic 2 Texture
    assert verf_result[0]['B_1_Characteristic_2_Texture'] == 'BR16'
    assert verf_result[1]['B_1_Characteristic_2_Texture'] == ('BR', 16, 16)
    # Band 1 Characteristic 3 Texture
    assert verf_result[0]['B_1_Characteristic_3_Texture'] == 'BR17'
    assert verf_result[1]['B_1_Characteristic_3_Texture'] == ('BR', 17, 17)
    # Band 1 Characteristic 4 Texture
    assert verf_result[0]['B_1_Characteristic_4_Texture'] == 'BR18'
    assert verf_result[1]['B_1_Characteristic_4_Texture'] == ('BR', 18, 18)
    # Band 1 Characteristic 5 Texture
    assert verf_result[0]['B_1_Characteristic_5_Texture'] == 'BR19'
    assert verf_result[1]['B_1_Characteristic_5_Texture'] == ('BR', 19, 19)
    # Band 1 Characteristic 6 Texture
    assert verf_result[0]['B_1_Characteristic_6_Texture'] == 'BR20'
    assert verf_result[1]['B_1_Characteristic_6_Texture'] == ('BR', 20, 20)
    # Band 1 Characteristic 7 Texture
    assert verf_result[0]['B_1_Characteristic_7_Texture'] == 'BR25'
    assert verf_result[1]['B_1_Characteristic_7_Texture'] == ('BR', 25, 25)
    # Band 1 Characteristic 8 Texture
    assert verf_result[0]['B_1_Characteristic_8_Texture'] == 'BR26'
    assert verf_result[1]['B_1_Characteristic_8_Texture'] == ('BR', 26, 26)
    # Band 1 Characteristic 9 Texture
    assert verf_result[0]['B_1_Characteristic_9_Texture'] == 'BR31'
    assert verf_result[1]['B_1_Characteristic_9_Texture'] == ('BR', 31, 31)
    # Band 1 Characteristic 10 Texture
    assert verf_result[0]['B_1_Characteristic_10_Texture'] == 'BR32'
    assert verf_result[1]['B_1_Characteristic_10_Texture'] == ('BR', 32, 32)
    # Band 2 Characteristic 1 Texture
    assert verf_result[0]['B_2_Characteristic_1_Texture'] == 'BR37'
    assert verf_result[1]['B_2_Characteristic_1_Texture'] == ('BR', 37, 37)
    # Band 2 Characteristic 2 Texture
    assert verf_result[0]['B_2_Characteristic_2_Texture'] == 'BR38'
    assert verf_result[1]['B_2_Characteristic_2_Texture'] == ('BR', 38, 38)
    # Band 2 Characteristic 3 Texture
    assert verf_result[0]['B_2_Characteristic_3_Texture'] == 'BR41'
    assert verf_result[1]['B_2_Characteristic_3_Texture'] == ('BR', 41, 41)
    # Band 2 Characteristic 4 Texture
    assert verf_result[0]['B_2_Characteristic_4_Texture'] == 'BR45'
    assert verf_result[1]['B_2_Characteristic_4_Texture'] == ('BR', 45, 45)
    # Band 2 Characteristic 5 Texture
    assert verf_result[0]['B_2_Characteristic_5_Texture'] == 'BR53'
    assert verf_result[1]['B_2_Characteristic_5_Texture'] == ('BR', 53, 53)
    # Band 3 Characteristic 1 Texture
    assert verf_result[0]['B_3_Characteristic_1_Texture'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Texture'] == ('BR', 57, 57)
    # Band Characteristic T_Unit
    # Band 1 Characteristic 1 T_Unit
    assert verf_result[0]['B_1_Characteristic_1_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_1_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 2 T_Unit
    assert verf_result[0]['B_1_Characteristic_2_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_2_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 3 T_Unit
    assert verf_result[0]['B_1_Characteristic_3_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_3_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 4 T_Unit
    assert verf_result[0]['B_1_Characteristic_4_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_4_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 5 T_Unit
    assert verf_result[0]['B_1_Characteristic_5_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_5_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 6 T_Unit
    assert verf_result[0]['B_1_Characteristic_6_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_6_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 7 T_Unit
    assert verf_result[0]['B_1_Characteristic_7_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_7_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 8 T_Unit
    assert verf_result[0]['B_1_Characteristic_8_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_8_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 9 T_Unit
    assert verf_result[0]['B_1_Characteristic_9_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_9_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 10 T_Unit
    assert verf_result[0]['B_1_Characteristic_10_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_10_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 1 T_Unit
    assert verf_result[0]['B_2_Characteristic_1_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_1_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 2 T_Unit
    assert verf_result[0]['B_2_Characteristic_2_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_2_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 3 T_Unit
    assert verf_result[0]['B_2_Characteristic_3_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_3_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 4 T_Unit
    assert verf_result[0]['B_2_Characteristic_4_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_4_T_Unit'] == ('BW', 8, 8)
    # Band 3 Characteristic 1 T_Unit
    assert verf_result[0]['B_3_Characteristic_1_T_Unit'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Unit'] == ('BW', 8, 8)
    # Band Characteristic T_Value
    # Band 1 Characteristic 1 T_Value
    assert verf_result[0]['B_1_Characteristic_1_T_Value'] == 'BT15'
    assert verf_result[1]['B_1_Characteristic_1_T_Value'] == ('BT', 15, 15)
    # Band 1 Characteristic 2 T_Value
    assert verf_result[0]['B_1_Characteristic_2_T_Value'] == 'BT16'
    assert verf_result[1]['B_1_Characteristic_2_T_Value'] == ('BT', 16, 16)
    # Band 1 Characteristic 3 T_Value
    assert verf_result[0]['B_1_Characteristic_3_T_Value'] == 'BT17'
    assert verf_result[1]['B_1_Characteristic_3_T_Value'] == ('BT', 17, 17)
    # Band 1 Characteristic 4 T_Value
    assert verf_result[0]['B_1_Characteristic_4_T_Value'] == 'BT18'
    assert verf_result[1]['B_1_Characteristic_4_T_Value'] == ('BT', 18, 18)
    # Band 1 Characteristic 5 T_Value
    assert verf_result[0]['B_1_Characteristic_5_T_Value'] == 'BT19'
    assert verf_result[1]['B_1_Characteristic_5_T_Value'] == ('BT', 19, 19)
    # Band 1 Characteristic 6 T_Value
    assert verf_result[0]['B_1_Characteristic_6_T_Value'] == 'BT20'
    assert verf_result[1]['B_1_Characteristic_6_T_Value'] == ('BT', 20, 20)
    # Band 1 Characteristic 7 T_Value
    assert verf_result[0]['B_1_Characteristic_7_T_Value'] == 'BT25'
    assert verf_result[1]['B_1_Characteristic_7_T_Value'] == ('BT', 25, 25)
    # Band 1 Characteristic 8 T_Value
    assert verf_result[0]['B_1_Characteristic_8_T_Value'] == 'BT26'
    assert verf_result[1]['B_1_Characteristic_8_T_Value'] == ('BT', 26, 26)
    # Band 1 Characteristic 9 T_Value
    assert verf_result[0]['B_1_Characteristic_9_T_Value'] == 'BT31'
    assert verf_result[1]['B_1_Characteristic_9_T_Value'] == ('BT', 31, 31)
    # Band 1 Characteristic 10 T_Value
    assert verf_result[0]['B_1_Characteristic_10_T_Value'] == 'BT32'
    assert verf_result[1]['B_1_Characteristic_10_T_Value'] == ('BT', 32, 32)
    # Band 2 Characteristic 1 T_Value
    assert verf_result[0]['B_2_Characteristic_1_T_Value'] == 'BT37'
    assert verf_result[1]['B_2_Characteristic_1_T_Value'] == ('BT', 37, 37)
    # Band 2 Characteristic 2 T_Value
    assert verf_result[0]['B_2_Characteristic_2_T_Value'] == 'BT38'
    assert verf_result[1]['B_2_Characteristic_2_T_Value'] == ('BT', 38, 38)
    # Band 2 Characteristic 3 T_Value
    assert verf_result[0]['B_2_Characteristic_3_T_Value'] == 'BT41'
    assert verf_result[1]['B_2_Characteristic_3_T_Value'] == ('BT', 41, 41)
    # Band 2 Characteristic 4 T_Value
    assert verf_result[0]['B_2_Characteristic_4_T_Value'] == 'BT45'
    assert verf_result[1]['B_2_Characteristic_4_T_Value'] == ('BT', 45, 45)
    # Band 2 Characteristic 5 T_Value
    assert verf_result[0]['B_2_Characteristic_5_T_Value'] == 'BT53'
    assert verf_result[1]['B_2_Characteristic_5_T_Value'] == ('BT', 53, 53)
    # Band 3 Characteristic 1 T_Value
    assert verf_result[0]['B_3_Characteristic_1_T_Value'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Value'] == ('BT', 57, 57)
    # Band Characteristic T_Error
    # Band 1 Characteristic 1 T_Error
    assert verf_result[0]['B_1_Characteristic_1_T_Error'] == 'BU15'
    assert verf_result[1]['B_1_Characteristic_1_T_Error'] == ('BU', 15, 15)
    # Band 1 Characteristic 2 T_Error
    assert verf_result[0]['B_1_Characteristic_2_T_Error'] == 'BU16'
    assert verf_result[1]['B_1_Characteristic_2_T_Error'] == ('BU', 16, 16)
    # Band 1 Characteristic 3 T_Error
    assert verf_result[0]['B_1_Characteristic_3_T_Error'] == 'BU17'
    assert verf_result[1]['B_1_Characteristic_3_T_Error'] == ('BU', 17, 17)
    # Band 1 Characteristic 4 T_Error
    assert verf_result[0]['B_1_Characteristic_4_T_Error'] == 'BU18'
    assert verf_result[1]['B_1_Characteristic_4_T_Error'] == ('BU', 18, 18)
    # Band 1 Characteristic 5 T_Error
    assert verf_result[0]['B_1_Characteristic_5_T_Error'] == 'BU19'
    assert verf_result[1]['B_1_Characteristic_5_T_Error'] == ('BU', 19, 19)
    # Band 1 Characteristic 6 T_Error
    assert verf_result[0]['B_1_Characteristic_6_T_Error'] == 'BU20'
    assert verf_result[1]['B_1_Characteristic_6_T_Error'] == ('BU', 20, 20)
    # Band 1 Characteristic 7 T_Error
    assert verf_result[0]['B_1_Characteristic_7_T_Error'] == 'BU25'
    assert verf_result[1]['B_1_Characteristic_7_T_Error'] == ('BU', 25, 25)
    # Band 1 Characteristic 8 T_Error
    assert verf_result[0]['B_1_Characteristic_8_T_Error'] == 'BU26'
    assert verf_result[1]['B_1_Characteristic_8_T_Error'] == ('BU', 26, 26)
    # Band 1 Characteristic 9 T_Error
    assert verf_result[0]['B_1_Characteristic_9_T_Error'] == 'BU31'
    assert verf_result[1]['B_1_Characteristic_9_T_Error'] == ('BU', 31, 31)
    # Band 1 Characteristic 10 T_Error
    assert verf_result[0]['B_1_Characteristic_10_T_Error'] == 'BU32'
    assert verf_result[1]['B_1_Characteristic_10_T_Error'] == ('BU', 32, 32)
    # Band 2 Characteristic 1 T_Error
    assert verf_result[0]['B_2_Characteristic_1_T_Error'] == 'BU37'
    assert verf_result[1]['B_2_Characteristic_1_T_Error'] == ('BU', 37, 37)
    # Band 2 Characteristic 2 T_Error
    assert verf_result[0]['B_2_Characteristic_2_T_Error'] == 'BU38'
    assert verf_result[1]['B_2_Characteristic_2_T_Error'] == ('BU', 38, 38)
    # Band 2 Characteristic 3 T_Error
    assert verf_result[0]['B_2_Characteristic_3_T_Error'] == 'BU41'
    assert verf_result[1]['B_2_Characteristic_3_T_Error'] == ('BU', 41, 41)
    # Band 2 Characteristic 4 T_Error
    assert verf_result[0]['B_2_Characteristic_4_T_Error'] == 'BU45'
    assert verf_result[1]['B_2_Characteristic_4_T_Error'] == ('BU', 45, 45)
    # Band 2 Characteristic 5 T_Error
    assert verf_result[0]['B_2_Characteristic_5_T_Error'] == 'BU53'
    assert verf_result[1]['B_2_Characteristic_5_T_Error'] == ('BU', 53, 53)
    # Band 3 Characteristic 1 T_Error
    assert verf_result[0]['B_3_Characteristic_1_T_Error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Error'] == ('BU', 57, 57)
    # Band Characteristic T_Formation
    # Band 1 Characteristic 1 T_Formation
    assert verf_result[0]['B_1_Characteristic_1_T_Formation'] == 'BV15'
    assert verf_result[1]['B_1_Characteristic_1_T_Formation'] == ('BV', 15, 15)
    # Band 1 Characteristic 2 T_Formation
    assert verf_result[0]['B_1_Characteristic_2_T_Formation'] == 'BV16'
    assert verf_result[1]['B_1_Characteristic_2_T_Formation'] == ('BV', 16, 16)
    # Band 1 Characteristic 3 T_Formation
    assert verf_result[0]['B_1_Characteristic_3_T_Formation'] == 'BV17'
    assert verf_result[1]['B_1_Characteristic_3_T_Formation'] == ('BV', 17, 17)
    # Band 1 Characteristic 4 T_Formation
    assert verf_result[0]['B_1_Characteristic_4_T_Formation'] == 'BV18'
    assert verf_result[1]['B_1_Characteristic_4_T_Formation'] == ('BV', 18, 18)
    # Band 1 Characteristic 5 T_Formation
    assert verf_result[0]['B_1_Characteristic_5_T_Formation'] == 'BV19'
    assert verf_result[1]['B_1_Characteristic_5_T_Formation'] == ('BV', 19, 19)
    # Band 1 Characteristic 6 T_Formation
    assert verf_result[0]['B_1_Characteristic_6_T_Formation'] == 'BV20'
    assert verf_result[1]['B_1_Characteristic_6_T_Formation'] == ('BV', 20, 20)
    # Band 1 Characteristic 7 T_Formation
    assert verf_result[0]['B_1_Characteristic_7_T_Formation'] == 'BV25'
    assert verf_result[1]['B_1_Characteristic_7_T_Formation'] == ('BV', 25, 25)
    # Band 1 Characteristic 8 T_Formation
    assert verf_result[0]['B_1_Characteristic_8_T_Formation'] == 'BV26'
    assert verf_result[1]['B_1_Characteristic_8_T_Formation'] == ('BV', 26, 26)
    # Band 1 Characteristic 9 T_Formation
    assert verf_result[0]['B_1_Characteristic_9_T_Formation'] == 'BV31'
    assert verf_result[1]['B_1_Characteristic_9_T_Formation'] == ('BV', 31, 31)
    # Band 1 Characteristic 10 T_Formation
    assert verf_result[0]['B_1_Characteristic_10_T_Formation'] == 'BV32'
    assert verf_result[1]['B_1_Characteristic_10_T_Formation'] == ('BV', 32, 32)
    # Band 2 Characteristic 1 T_Formation
    assert verf_result[0]['B_2_Characteristic_1_T_Formation'] == 'BV37'
    assert verf_result[1]['B_2_Characteristic_1_T_Formation'] == ('BV', 37, 37)
    # Band 2 Characteristic 2 T_Formation
    assert verf_result[0]['B_2_Characteristic_2_T_Formation'] == 'BV38'
    assert verf_result[1]['B_2_Characteristic_2_T_Formation'] == ('BV', 38, 38)
    # Band 2 Characteristic 3 T_Formation
    assert verf_result[0]['B_2_Characteristic_3_T_Formation'] == 'BV41'
    assert verf_result[1]['B_2_Characteristic_3_T_Formation'] == ('BV', 41, 41)
    # Band 2 Characteristic 4 T_Formation
    assert verf_result[0]['B_2_Characteristic_4_T_Formation'] == 'BV45'
    assert verf_result[1]['B_2_Characteristic_4_T_Formation'] == ('BV', 45, 45)
    # Band 2 Characteristic 5 T_Formation
    assert verf_result[0]['B_2_Characteristic_5_T_Formation'] == 'BV53'
    assert verf_result[1]['B_2_Characteristic_5_T_Formation'] == ('BV', 53, 53)
    # Band 3 Characteristic 1 T_Formation
    assert verf_result[0]['B_3_Characteristic_1_T_Formation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Formation'] == ('BV', 57, 57)
    # Band Characteristic T_Max
    # Band 1 Characteristic 1 T_Max
    assert verf_result[0]['B_1_Characteristic_1_T_Max'] == 'BW15'
    assert verf_result[1]['B_1_Characteristic_1_T_Max'] == ('BW', 15, 15)
    # Band 1 Characteristic 2 T_Max
    assert verf_result[0]['B_1_Characteristic_2_T_Max'] == 'BW16'
    assert verf_result[1]['B_1_Characteristic_2_T_Max'] == ('BW', 16, 16)
    # Band 1 Characteristic 3 T_Max
    assert verf_result[0]['B_1_Characteristic_3_T_Max'] == 'BW17'
    assert verf_result[1]['B_1_Characteristic_3_T_Max'] == ('BW', 17, 17)
    # Band 1 Characteristic 4 T_Max
    assert verf_result[0]['B_1_Characteristic_4_T_Max'] == 'BW18'
    assert verf_result[1]['B_1_Characteristic_4_T_Max'] == ('BW', 18, 18)
    # Band 1 Characteristic 5 T_Max
    assert verf_result[0]['B_1_Characteristic_5_T_Max'] == 'BW19'
    assert verf_result[1]['B_1_Characteristic_5_T_Max'] == ('BW', 19, 19)
    # Band 1 Characteristic 6 T_Max
    assert verf_result[0]['B_1_Characteristic_6_T_Max'] == 'BW20'
    assert verf_result[1]['B_1_Characteristic_6_T_Max'] == ('BW', 20, 20)
    # Band 1 Characteristic 7 T_Max
    assert verf_result[0]['B_1_Characteristic_7_T_Max'] == 'BW25'
    assert verf_result[1]['B_1_Characteristic_7_T_Max'] == ('BW', 25, 25)
    # Band 1 Characteristic 8 T_Max
    assert verf_result[0]['B_1_Characteristic_8_T_Max'] == 'BW26'
    assert verf_result[1]['B_1_Characteristic_8_T_Max'] == ('BW', 26, 26)
    # Band 1 Characteristic 9 T_Max
    assert verf_result[0]['B_1_Characteristic_9_T_Max'] == 'BW31'
    assert verf_result[1]['B_1_Characteristic_9_T_Max'] == ('BW', 31, 31)
    # Band 1 Characteristic 10 T_Max
    assert verf_result[0]['B_1_Characteristic_10_T_Max'] == 'BW32'
    assert verf_result[1]['B_1_Characteristic_10_T_Max'] == ('BW', 32, 32)
    # Band 2 Characteristic 1 T_Max
    assert verf_result[0]['B_2_Characteristic_1_T_Max'] == 'BW37'
    assert verf_result[1]['B_2_Characteristic_1_T_Max'] == ('BW', 37, 37)
    # Band 2 Characteristic 2 T_Max
    assert verf_result[0]['B_2_Characteristic_2_T_Max'] == 'BW38'
    assert verf_result[1]['B_2_Characteristic_2_T_Max'] == ('BW', 38, 38)
    # Band 2 Characteristic 3 T_Max
    assert verf_result[0]['B_2_Characteristic_3_T_Max'] == 'BW41'
    assert verf_result[1]['B_2_Characteristic_3_T_Max'] == ('BW', 41, 41)
    # Band 2 Characteristic 4 T_Max
    assert verf_result[0]['B_2_Characteristic_4_T_Max'] == 'BW45'
    assert verf_result[1]['B_2_Characteristic_4_T_Max'] == ('BW', 45, 45)
    # Band 2 Characteristic 5 T_Max
    assert verf_result[0]['B_2_Characteristic_5_T_Max'] == 'BW53'
    assert verf_result[1]['B_2_Characteristic_5_T_Max'] == ('BW', 53, 53)
    # Band 3 Characteristic 1 T_Max
    assert verf_result[0]['B_3_Characteristic_1_T_Max'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Max'] == ('BW', 57, 57)
    # Band Characteristic T_Comment
    # Band 1 Characteristic 1 T_Comment
    assert verf_result[0]['B_1_Characteristic_1_T_Comment'] == 'BX15'
    assert verf_result[1]['B_1_Characteristic_1_T_Comment'] == ('BX', 15, 15)
    # Band 1 Characteristic 2 T_Comment
    assert verf_result[0]['B_1_Characteristic_2_T_Comment'] == 'BX16'
    assert verf_result[1]['B_1_Characteristic_2_T_Comment'] == ('BX', 16, 16)
    # Band 1 Characteristic 3 T_Comment
    assert verf_result[0]['B_1_Characteristic_3_T_Comment'] == 'BX17'
    assert verf_result[1]['B_1_Characteristic_3_T_Comment'] == ('BX', 17, 17)
    # Band 1 Characteristic 4 T_Comment
    assert verf_result[0]['B_1_Characteristic_4_T_Comment'] == 'BX18'
    assert verf_result[1]['B_1_Characteristic_4_T_Comment'] == ('BX', 18, 18)
    # Band 1 Characteristic 5 T_Comment
    assert verf_result[0]['B_1_Characteristic_5_T_Comment'] == 'BX19'
    assert verf_result[1]['B_1_Characteristic_5_T_Comment'] == ('BX', 19, 19)
    # Band 1 Characteristic 6 T_Comment
    assert verf_result[0]['B_1_Characteristic_6_T_Comment'] == 'BX20'
    assert verf_result[1]['B_1_Characteristic_6_T_Comment'] == ('BX', 20, 20)
    # Band 1 Characteristic 7 T_Comment
    assert verf_result[0]['B_1_Characteristic_7_T_Comment'] == 'BX25'
    assert verf_result[1]['B_1_Characteristic_7_T_Comment'] == ('BX', 25, 25)
    # Band 1 Characteristic 8 T_Comment
    assert verf_result[0]['B_1_Characteristic_8_T_Comment'] == 'BX26'
    assert verf_result[1]['B_1_Characteristic_8_T_Comment'] == ('BX', 26, 26)
    # Band 1 Characteristic 9 T_Comment
    assert verf_result[0]['B_1_Characteristic_9_T_Comment'] == 'BX31'
    assert verf_result[1]['B_1_Characteristic_9_T_Comment'] == ('BX', 31, 31)
    # Band 1 Characteristic 10 T_Comment
    assert verf_result[0]['B_1_Characteristic_10_T_Comment'] == 'BX32'
    assert verf_result[1]['B_1_Characteristic_10_T_Comment'] == ('BX', 32, 32)
    # Band 2 Characteristic 1 T_Comment
    assert verf_result[0]['B_2_Characteristic_1_T_Comment'] == 'BX37'
    assert verf_result[1]['B_2_Characteristic_1_T_Comment'] == ('BX', 37, 37)
    # Band 2 Characteristic 2 T_Comment
    assert verf_result[0]['B_2_Characteristic_2_T_Comment'] == 'BX38'
    assert verf_result[1]['B_2_Characteristic_2_T_Comment'] == ('BX', 38, 38)
    # Band 2 Characteristic 3 T_Comment
    assert verf_result[0]['B_2_Characteristic_3_T_Comment'] == 'BX41'
    assert verf_result[1]['B_2_Characteristic_3_T_Comment'] == ('BX', 41, 41)
    # Band 2 Characteristic 4 T_Comment
    assert verf_result[0]['B_2_Characteristic_4_T_Comment'] == 'BX45'
    assert verf_result[1]['B_2_Characteristic_4_T_Comment'] == ('BX', 45, 45)
    # Band 2 Characteristic 5 T_Comment
    assert verf_result[0]['B_2_Characteristic_5_T_Comment'] == 'BX53'
    assert verf_result[1]['B_2_Characteristic_5_T_Comment'] == ('BX', 53, 53)
    # Band 3 Characteristic 1 T_Comment
    assert verf_result[0]['B_3_Characteristic_1_T_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Comment'] == ('BX', 57, 57)
    # Band Characteristic P_Unit
    # Band 1 Characteristic 1 P_Unit
    assert verf_result[0]['B_1_Characteristic_1_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_1_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 2 P_Unit
    assert verf_result[0]['B_1_Characteristic_2_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_2_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 3 P_Unit
    assert verf_result[0]['B_1_Characteristic_3_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_3_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 4 P_Unit
    assert verf_result[0]['B_1_Characteristic_4_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_4_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 5 P_Unit
    assert verf_result[0]['B_1_Characteristic_5_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_5_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 6 P_Unit
    assert verf_result[0]['B_1_Characteristic_6_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_6_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 7 P_Unit
    assert verf_result[0]['B_1_Characteristic_7_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_7_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 8 P_Unit
    assert verf_result[0]['B_1_Characteristic_8_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_8_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 9 P_Unit
    assert verf_result[0]['B_1_Characteristic_9_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_9_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 10 P_Unit
    assert verf_result[0]['B_1_Characteristic_10_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_10_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 1 P_Unit
    assert verf_result[0]['B_2_Characteristic_1_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_1_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 2 P_Unit
    assert verf_result[0]['B_2_Characteristic_2_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_2_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 3 P_Unit
    assert verf_result[0]['B_2_Characteristic_3_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_3_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 4 P_Unit
    assert verf_result[0]['B_2_Characteristic_4_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_4_P_Unit'] == ('CC', 8, 8)
    # Band 3 Characteristic 1 P_Unit
    assert verf_result[0]['B_3_Characteristic_1_P_Unit'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Unit'] == ('CC', 8, 8)
    # Band Characteristic P_Value
    # Band 1 Characteristic 1 P_Value
    assert verf_result[0]['B_1_Characteristic_1_P_Value'] == 'BZ15'
    assert verf_result[1]['B_1_Characteristic_1_P_Value'] == ('BZ', 15, 15)
    # Band 1 Characteristic 2 P_Value
    assert verf_result[0]['B_1_Characteristic_2_P_Value'] == 'BZ16'
    assert verf_result[1]['B_1_Characteristic_2_P_Value'] == ('BZ', 16, 16)
    # Band 1 Characteristic 3 P_Value
    assert verf_result[0]['B_1_Characteristic_3_P_Value'] == 'BZ17'
    assert verf_result[1]['B_1_Characteristic_3_P_Value'] == ('BZ', 17, 17)
    # Band 1 Characteristic 4 P_Value
    assert verf_result[0]['B_1_Characteristic_4_P_Value'] == 'BZ18'
    assert verf_result[1]['B_1_Characteristic_4_P_Value'] == ('BZ', 18, 18)
    # Band 1 Characteristic 5 P_Value
    assert verf_result[0]['B_1_Characteristic_5_P_Value'] == 'BZ19'
    assert verf_result[1]['B_1_Characteristic_5_P_Value'] == ('BZ', 19, 19)
    # Band 1 Characteristic 6 P_Value
    assert verf_result[0]['B_1_Characteristic_6_P_Value'] == 'BZ20'
    assert verf_result[1]['B_1_Characteristic_6_P_Value'] == ('BZ', 20, 20)
    # Band 1 Characteristic 7 P_Value
    assert verf_result[0]['B_1_Characteristic_7_P_Value'] == 'BZ25'
    assert verf_result[1]['B_1_Characteristic_7_P_Value'] == ('BZ', 25, 25)
    # Band 1 Characteristic 8 P_Value
    assert verf_result[0]['B_1_Characteristic_8_P_Value'] == 'BZ26'
    assert verf_result[1]['B_1_Characteristic_8_P_Value'] == ('BZ', 26, 26)
    # Band 1 Characteristic 9 P_Value
    assert verf_result[0]['B_1_Characteristic_9_P_Value'] == 'BZ31'
    assert verf_result[1]['B_1_Characteristic_9_P_Value'] == ('BZ', 31, 31)
    # Band 1 Characteristic 10 P_Value
    assert verf_result[0]['B_1_Characteristic_10_P_Value'] == 'BZ32'
    assert verf_result[1]['B_1_Characteristic_10_P_Value'] == ('BZ', 32, 32)
    # Band 2 Characteristic 1 P_Value
    assert verf_result[0]['B_2_Characteristic_1_P_Value'] == 'BZ37'
    assert verf_result[1]['B_2_Characteristic_1_P_Value'] == ('BZ', 37, 37)
    # Band 2 Characteristic 2 P_Value
    assert verf_result[0]['B_2_Characteristic_2_P_Value'] == 'BZ38'
    assert verf_result[1]['B_2_Characteristic_2_P_Value'] == ('BZ', 38, 38)
    # Band 2 Characteristic 3 P_Value
    assert verf_result[0]['B_2_Characteristic_3_P_Value'] == 'BZ41'
    assert verf_result[1]['B_2_Characteristic_3_P_Value'] == ('BZ', 41, 41)
    # Band 2 Characteristic 4 P_Value
    assert verf_result[0]['B_2_Characteristic_4_P_Value'] == 'BZ45'
    assert verf_result[1]['B_2_Characteristic_4_P_Value'] == ('BZ', 45, 45)
    # Band 2 Characteristic 5 P_Value
    assert verf_result[0]['B_2_Characteristic_5_P_Value'] == 'BZ53'
    assert verf_result[1]['B_2_Characteristic_5_P_Value'] == ('BZ', 53, 53)
    # Band 3 Characteristic 1 P_Value
    assert verf_result[0]['B_3_Characteristic_1_P_Value'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Value'] == ('BZ', 57, 57)
    # Band Characteristic P_Error
    # Band 1 Characteristic 1 P_Error
    assert verf_result[0]['B_1_Characteristic_1_P_Error'] == 'CA15'
    assert verf_result[1]['B_1_Characteristic_1_P_Error'] == ('CA', 15, 15)
    # Band 1 Characteristic 2 P_Error
    assert verf_result[0]['B_1_Characteristic_2_P_Error'] == 'CA16'
    assert verf_result[1]['B_1_Characteristic_2_P_Error'] == ('CA', 16, 16)
    # Band 1 Characteristic 3 P_Error
    assert verf_result[0]['B_1_Characteristic_3_P_Error'] == 'CA17'
    assert verf_result[1]['B_1_Characteristic_3_P_Error'] == ('CA', 17, 17)
    # Band 1 Characteristic 4 P_Error
    assert verf_result[0]['B_1_Characteristic_4_P_Error'] == 'CA18'
    assert verf_result[1]['B_1_Characteristic_4_P_Error'] == ('CA', 18, 18)
    # Band 1 Characteristic 5 P_Error
    assert verf_result[0]['B_1_Characteristic_5_P_Error'] == 'CA19'
    assert verf_result[1]['B_1_Characteristic_5_P_Error'] == ('CA', 19, 19)
    # Band 1 Characteristic 6 P_Error
    assert verf_result[0]['B_1_Characteristic_6_P_Error'] == 'CA20'
    assert verf_result[1]['B_1_Characteristic_6_P_Error'] == ('CA', 20, 20)
    # Band 1 Characteristic 7 P_Error
    assert verf_result[0]['B_1_Characteristic_7_P_Error'] == 'CA25'
    assert verf_result[1]['B_1_Characteristic_7_P_Error'] == ('CA', 25, 25)
    # Band 1 Characteristic 8 P_Error
    assert verf_result[0]['B_1_Characteristic_8_P_Error'] == 'CA26'
    assert verf_result[1]['B_1_Characteristic_8_P_Error'] == ('CA', 26, 26)
    # Band 1 Characteristic 9 P_Error
    assert verf_result[0]['B_1_Characteristic_9_P_Error'] == 'CA31'
    assert verf_result[1]['B_1_Characteristic_9_P_Error'] == ('CA', 31, 31)
    # Band 1 Characteristic 10 P_Error
    assert verf_result[0]['B_1_Characteristic_10_P_Error'] == 'CA32'
    assert verf_result[1]['B_1_Characteristic_10_P_Error'] == ('CA', 32, 32)
    # Band 2 Characteristic 1 P_Error
    assert verf_result[0]['B_2_Characteristic_1_P_Error'] == 'CA37'
    assert verf_result[1]['B_2_Characteristic_1_P_Error'] == ('CA', 37, 37)
    # Band 2 Characteristic 2 P_Error
    assert verf_result[0]['B_2_Characteristic_2_P_Error'] == 'CA38'
    assert verf_result[1]['B_2_Characteristic_2_P_Error'] == ('CA', 38, 38)
    # Band 2 Characteristic 3 P_Error
    assert verf_result[0]['B_2_Characteristic_3_P_Error'] == 'CA41'
    assert verf_result[1]['B_2_Characteristic_3_P_Error'] == ('CA', 41, 41)
    # Band 2 Characteristic 4 P_Error
    assert verf_result[0]['B_2_Characteristic_4_P_Error'] == 'CA45'
    assert verf_result[1]['B_2_Characteristic_4_P_Error'] == ('CA', 45, 45)
    # Band 2 Characteristic 5 P_Error
    assert verf_result[0]['B_2_Characteristic_5_P_Error'] == 'CA53'
    assert verf_result[1]['B_2_Characteristic_5_P_Error'] == ('CA', 53, 53)
    # Band 3 Characteristic 1 P_Error
    assert verf_result[0]['B_3_Characteristic_1_P_Error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Error'] == ('CA', 57, 57)
    # Band Characteristic P_Formation
    # Band 1 Characteristic 1 P_Formation
    assert verf_result[0]['B_1_Characteristic_1_P_Formation'] == 'CB15'
    assert verf_result[1]['B_1_Characteristic_1_P_Formation'] == ('CB', 15, 15)
    # Band 1 Characteristic 2 P_Formation
    assert verf_result[0]['B_1_Characteristic_2_P_Formation'] == 'CB16'
    assert verf_result[1]['B_1_Characteristic_2_P_Formation'] == ('CB', 16, 16)
    # Band 1 Characteristic 3 P_Formation
    assert verf_result[0]['B_1_Characteristic_3_P_Formation'] == 'CB17'
    assert verf_result[1]['B_1_Characteristic_3_P_Formation'] == ('CB', 17, 17)
    # Band 1 Characteristic 4 P_Formation
    assert verf_result[0]['B_1_Characteristic_4_P_Formation'] == 'CB18'
    assert verf_result[1]['B_1_Characteristic_4_P_Formation'] == ('CB', 18, 18)
    # Band 1 Characteristic 5 P_Formation
    assert verf_result[0]['B_1_Characteristic_5_P_Formation'] == 'CB19'
    assert verf_result[1]['B_1_Characteristic_5_P_Formation'] == ('CB', 19, 19)
    # Band 1 Characteristic 6 P_Formation
    assert verf_result[0]['B_1_Characteristic_6_P_Formation'] == 'CB20'
    assert verf_result[1]['B_1_Characteristic_6_P_Formation'] == ('CB', 20, 20)
    # Band 1 Characteristic 7 P_Formation
    assert verf_result[0]['B_1_Characteristic_7_P_Formation'] == 'CB25'
    assert verf_result[1]['B_1_Characteristic_7_P_Formation'] == ('CB', 25, 25)
    # Band 1 Characteristic 8 P_Formation
    assert verf_result[0]['B_1_Characteristic_8_P_Formation'] == 'CB26'
    assert verf_result[1]['B_1_Characteristic_8_P_Formation'] == ('CB', 26, 26)
    # Band 1 Characteristic 9 P_Formation
    assert verf_result[0]['B_1_Characteristic_9_P_Formation'] == 'CB31'
    assert verf_result[1]['B_1_Characteristic_9_P_Formation'] == ('CB', 31, 31)
    # Band 1 Characteristic 10 P_Formation
    assert verf_result[0]['B_1_Characteristic_10_P_Formation'] == 'CB32'
    assert verf_result[1]['B_1_Characteristic_10_P_Formation'] == ('CB', 32, 32)
    # Band 2 Characteristic 1 P_Formation
    assert verf_result[0]['B_2_Characteristic_1_P_Formation'] == 'CB37'
    assert verf_result[1]['B_2_Characteristic_1_P_Formation'] == ('CB', 37, 37)
    # Band 2 Characteristic 2 P_Formation
    assert verf_result[0]['B_2_Characteristic_2_P_Formation'] == 'CB38'
    assert verf_result[1]['B_2_Characteristic_2_P_Formation'] == ('CB', 38, 38)
    # Band 2 Characteristic 3 P_Formation
    assert verf_result[0]['B_2_Characteristic_3_P_Formation'] == 'CB41'
    assert verf_result[1]['B_2_Characteristic_3_P_Formation'] == ('CB', 41, 41)
    # Band 2 Characteristic 4 P_Formation
    assert verf_result[0]['B_2_Characteristic_4_P_Formation'] == 'CB45'
    assert verf_result[1]['B_2_Characteristic_4_P_Formation'] == ('CB', 45, 45)
    # Band 2 Characteristic 5 P_Formation
    assert verf_result[0]['B_2_Characteristic_5_P_Formation'] == 'CB53'
    assert verf_result[1]['B_2_Characteristic_5_P_Formation'] == ('CB', 53, 53)
    # Band 3 Characteristic 1 P_Formation
    assert verf_result[0]['B_3_Characteristic_1_P_Formation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Formation'] == ('CB', 57, 57)
    # Band Characteristic P_Max
    # Band 1 Characteristic 1 P_Max
    assert verf_result[0]['B_1_Characteristic_1_P_Max'] == 'CC15'
    assert verf_result[1]['B_1_Characteristic_1_P_Max'] == ('CC', 15, 15)
    # Band 1 Characteristic 2 P_Max
    assert verf_result[0]['B_1_Characteristic_2_P_Max'] == 'CC16'
    assert verf_result[1]['B_1_Characteristic_2_P_Max'] == ('CC', 16, 16)
    # Band 1 Characteristic 3 P_Max
    assert verf_result[0]['B_1_Characteristic_3_P_Max'] == 'CC17'
    assert verf_result[1]['B_1_Characteristic_3_P_Max'] == ('CC', 17, 17)
    # Band 1 Characteristic 4 P_Max
    assert verf_result[0]['B_1_Characteristic_4_P_Max'] == 'CC18'
    assert verf_result[1]['B_1_Characteristic_4_P_Max'] == ('CC', 18, 18)
    # Band 1 Characteristic 5 P_Max
    assert verf_result[0]['B_1_Characteristic_5_P_Max'] == 'CC19'
    assert verf_result[1]['B_1_Characteristic_5_P_Max'] == ('CC', 19, 19)
    # Band 1 Characteristic 6 P_Max
    assert verf_result[0]['B_1_Characteristic_6_P_Max'] == 'CC20'
    assert verf_result[1]['B_1_Characteristic_6_P_Max'] == ('CC', 20, 20)
    # Band 1 Characteristic 7 P_Max
    assert verf_result[0]['B_1_Characteristic_7_P_Max'] == 'CC25'
    assert verf_result[1]['B_1_Characteristic_7_P_Max'] == ('CC', 25, 25)
    # Band 1 Characteristic 8 P_Max
    assert verf_result[0]['B_1_Characteristic_8_P_Max'] == 'CC26'
    assert verf_result[1]['B_1_Characteristic_8_P_Max'] == ('CC', 26, 26)
    # Band 1 Characteristic 9 P_Max
    assert verf_result[0]['B_1_Characteristic_9_P_Max'] == 'CC31'
    assert verf_result[1]['B_1_Characteristic_9_P_Max'] == ('CC', 31, 31)
    # Band 1 Characteristic 10 P_Max
    assert verf_result[0]['B_1_Characteristic_10_P_Max'] == 'CC32'
    assert verf_result[1]['B_1_Characteristic_10_P_Max'] == ('CC', 32, 32)
    # Band 2 Characteristic 1 P_Max
    assert verf_result[0]['B_2_Characteristic_1_P_Max'] == 'CC37'
    assert verf_result[1]['B_2_Characteristic_1_P_Max'] == ('CC', 37, 37)
    # Band 2 Characteristic 2 P_Max
    assert verf_result[0]['B_2_Characteristic_2_P_Max'] == 'CC38'
    assert verf_result[1]['B_2_Characteristic_2_P_Max'] == ('CC', 38, 38)
    # Band 2 Characteristic 3 P_Max
    assert verf_result[0]['B_2_Characteristic_3_P_Max'] == 'CC41'
    assert verf_result[1]['B_2_Characteristic_3_P_Max'] == ('CC', 41, 41)
    # Band 2 Characteristic 4 P_Max
    assert verf_result[0]['B_2_Characteristic_4_P_Max'] == 'CC45'
    assert verf_result[1]['B_2_Characteristic_4_P_Max'] == ('CC', 45, 45)
    # Band 2 Characteristic 5 P_Max
    assert verf_result[0]['B_2_Characteristic_5_P_Max'] == 'CC53'
    assert verf_result[1]['B_2_Characteristic_5_P_Max'] == ('CC', 53, 53)
    # Band 3 Characteristic 1 P_Max
    assert verf_result[0]['B_3_Characteristic_1_P_Max'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Max'] == ('CC', 57, 57)
    # Band Characteristic P_Stress_type
    # Band 1 Characteristic 1 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_1_P_Stress_type'] == 'normal uniaxial tension'
    assert verf_result[1]['B_1_Characteristic_1_P_Stress_type'] == ('CD', 15, 15)
    # Band 1 Characteristic 2 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_2_P_Stress_type'] == 'normal uniaxial compression'
    assert verf_result[1]['B_1_Characteristic_2_P_Stress_type'] == ('CD', 16, 16)
    # Band 1 Characteristic 3 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_3_P_Stress_type'] == 'simple shear'
    assert verf_result[1]['B_1_Characteristic_3_P_Stress_type'] == ('CD', 17, 17)
    # Band 1 Characteristic 4 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_4_P_Stress_type'] == 'normal biaxial tension'
    assert verf_result[1]['B_1_Characteristic_4_P_Stress_type'] == ('CD', 18, 18)
    # Band 1 Characteristic 5 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_5_P_Stress_type'] == 'normal biaxial compression'
    assert verf_result[1]['B_1_Characteristic_5_P_Stress_type'] == ('CD', 19, 19)
    # Band 1 Characteristic 6 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_6_P_Stress_type'] == 'cylindrical normal tension'
    assert verf_result[1]['B_1_Characteristic_6_P_Stress_type'] == ('CD', 20, 20)
    # Band 1 Characteristic 7 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_7_P_Stress_type'] == ''
    assert verf_result[1]['B_1_Characteristic_7_P_Stress_type'] == ('CD', 25, 25)
    # Band 1 Characteristic 8 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_8_P_Stress_type'] == 'cylindrical normal compression'
    assert verf_result[1]['B_1_Characteristic_8_P_Stress_type'] == ('CD', 26, 26)
    # Band 1 Characteristic 9 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_9_P_Stress_type'] == 'isotropic normal tension'
    assert verf_result[1]['B_1_Characteristic_9_P_Stress_type'] == ('CD', 31, 31)
    # Band 1 Characteristic 10 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_10_P_Stress_type'] == 'isotropic normal compression'
    assert verf_result[1]['B_1_Characteristic_10_P_Stress_type'] == ('CD', 32, 32)
    # Band 2 Characteristic 1 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_1_P_Stress_type'] == 'combined biaxial'
    assert verf_result[1]['B_2_Characteristic_1_P_Stress_type'] == ('CD', 37, 37)
    # Band 2 Characteristic 2 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_2_P_Stress_type'] == 'combined triaxial'
    assert verf_result[1]['B_2_Characteristic_2_P_Stress_type'] == ('CD', 38, 38)
    # Band 2 Characteristic 3 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_3_P_Stress_type'] == 'other'
    assert verf_result[1]['B_2_Characteristic_3_P_Stress_type'] == ('CD', 41, 41)
    # Band 2 Characteristic 4 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_4_P_Stress_type'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_4_P_Stress_type'] == ('CD', 45, 45)
    # Band 2 Characteristic 5 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_5_P_Stress_type'] == ''
    assert verf_result[1]['B_2_Characteristic_5_P_Stress_type'] == ('CD', 53, 53)
    # Band 3 Characteristic 1 P_Stress_type
    assert verf_result[0]['B_3_Characteristic_1_P_Stress_type'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Stress_type'] == ('CD', 57, 57)
    # Band Characteristic P_Comment
    # Band 1 Characteristic 1 P_Comment
    assert verf_result[0]['B_1_Characteristic_1_P_Comment'] == 'CE15'
    assert verf_result[1]['B_1_Characteristic_1_P_Comment'] == ('CE', 15, 15)
    # Band 1 Characteristic 2 P_Comment
    assert verf_result[0]['B_1_Characteristic_2_P_Comment'] == 'CE16'
    assert verf_result[1]['B_1_Characteristic_2_P_Comment'] == ('CE', 16, 16)
    # Band 1 Characteristic 3 P_Comment
    assert verf_result[0]['B_1_Characteristic_3_P_Comment'] == 'CE17'
    assert verf_result[1]['B_1_Characteristic_3_P_Comment'] == ('CE', 17, 17)
    # Band 1 Characteristic 4 P_Comment
    assert verf_result[0]['B_1_Characteristic_4_P_Comment'] == 'CE18'
    assert verf_result[1]['B_1_Characteristic_4_P_Comment'] == ('CE', 18, 18)
    # Band 1 Characteristic 5 P_Comment
    assert verf_result[0]['B_1_Characteristic_5_P_Comment'] == 'CE19'
    assert verf_result[1]['B_1_Characteristic_5_P_Comment'] == ('CE', 19, 19)
    # Band 1 Characteristic 6 P_Comment
    assert verf_result[0]['B_1_Characteristic_6_P_Comment'] == 'CE20'
    assert verf_result[1]['B_1_Characteristic_6_P_Comment'] == ('CE', 20, 20)
    # Band 1 Characteristic 7 P_Comment
    assert verf_result[0]['B_1_Characteristic_7_P_Comment'] == 'CE25'
    assert verf_result[1]['B_1_Characteristic_7_P_Comment'] == ('CE', 25, 25)
    # Band 1 Characteristic 8 P_Comment
    assert verf_result[0]['B_1_Characteristic_8_P_Comment'] == 'CE26'
    assert verf_result[1]['B_1_Characteristic_8_P_Comment'] == ('CE', 26, 26)
    # Band 1 Characteristic 9 P_Comment
    assert verf_result[0]['B_1_Characteristic_9_P_Comment'] == 'CE31'
    assert verf_result[1]['B_1_Characteristic_9_P_Comment'] == ('CE', 31, 31)
    # Band 1 Characteristic 10 P_Comment
    assert verf_result[0]['B_1_Characteristic_10_P_Comment'] == 'CE32'
    assert verf_result[1]['B_1_Characteristic_10_P_Comment'] == ('CE', 32, 32)
    # Band 2 Characteristic 1 P_Comment
    assert verf_result[0]['B_2_Characteristic_1_P_Comment'] == 'CE37'
    assert verf_result[1]['B_2_Characteristic_1_P_Comment'] == ('CE', 37, 37)
    # Band 2 Characteristic 2 P_Comment
    assert verf_result[0]['B_2_Characteristic_2_P_Comment'] == 'CE38'
    assert verf_result[1]['B_2_Characteristic_2_P_Comment'] == ('CE', 38, 38)
    # Band 2 Characteristic 3 P_Comment
    assert verf_result[0]['B_2_Characteristic_3_P_Comment'] == 'CE41'
    assert verf_result[1]['B_2_Characteristic_3_P_Comment'] == ('CE', 41, 41)
    # Band 2 Characteristic 4 P_Comment
    assert verf_result[0]['B_2_Characteristic_4_P_Comment'] == 'CE45'
    assert verf_result[1]['B_2_Characteristic_4_P_Comment'] == ('CE', 45, 45)
    # Band 2 Characteristic 5 P_Comment
    assert verf_result[0]['B_2_Characteristic_5_P_Comment'] == 'CE53'
    assert verf_result[1]['B_2_Characteristic_5_P_Comment'] == ('CE', 53, 53)
    # Band 3 Characteristic 1 P_Comment
    assert verf_result[0]['B_3_Characteristic_1_P_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Comment'] == ('CE', 57, 57)
    # Band Characteristic Laser_excitation_Wavelength_Unit
    # Band 1 Characteristic 1 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_1_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 2 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_2_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_2_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 3 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_3_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_3_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 4 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_4_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_4_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 5 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_5_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_5_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 6 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_6_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_6_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 7 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_7_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_7_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 8 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_8_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_8_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 9 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_9_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_9_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 10 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_10_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_10_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 1 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_1_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 2 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_2_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_2_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 3 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_3_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_3_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 4 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_4_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_4_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 3 Characteristic 1 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_3_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band Characteristic Laser_excitation_Wavelength
    # Band 1 Characteristic 1 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_1_Laser_excitation_Wavelength'] == 'CG15'
    assert verf_result[1]['B_1_Characteristic_1_Laser_excitation_Wavelength'] == ('CG', 15, 15)
    # Band 1 Characteristic 2 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_2_Laser_excitation_Wavelength'] == 'CG16'
    assert verf_result[1]['B_1_Characteristic_2_Laser_excitation_Wavelength'] == ('CG', 16, 16)
    # Band 1 Characteristic 3 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_3_Laser_excitation_Wavelength'] == 'CG17'
    assert verf_result[1]['B_1_Characteristic_3_Laser_excitation_Wavelength'] == ('CG', 17, 17)
    # Band 1 Characteristic 4 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_4_Laser_excitation_Wavelength'] == 'CG18'
    assert verf_result[1]['B_1_Characteristic_4_Laser_excitation_Wavelength'] == ('CG', 18, 18)
    # Band 1 Characteristic 5 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_5_Laser_excitation_Wavelength'] == 'CG19'
    assert verf_result[1]['B_1_Characteristic_5_Laser_excitation_Wavelength'] == ('CG', 19, 19)
    # Band 1 Characteristic 6 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_6_Laser_excitation_Wavelength'] == 'CG20'
    assert verf_result[1]['B_1_Characteristic_6_Laser_excitation_Wavelength'] == ('CG', 20, 20)
    # Band 1 Characteristic 7 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_7_Laser_excitation_Wavelength'] == 'CG25'
    assert verf_result[1]['B_1_Characteristic_7_Laser_excitation_Wavelength'] == ('CG', 25, 25)
    # Band 1 Characteristic 8 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_8_Laser_excitation_Wavelength'] == 'CG26'
    assert verf_result[1]['B_1_Characteristic_8_Laser_excitation_Wavelength'] == ('CG', 26, 26)
    # Band 1 Characteristic 9 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_9_Laser_excitation_Wavelength'] == 'CG31'
    assert verf_result[1]['B_1_Characteristic_9_Laser_excitation_Wavelength'] == ('CG', 31, 31)
    # Band 1 Characteristic 10 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_10_Laser_excitation_Wavelength'] == 'CG32'
    assert verf_result[1]['B_1_Characteristic_10_Laser_excitation_Wavelength'] == ('CG', 32, 32)
    # Band 2 Characteristic 1 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_1_Laser_excitation_Wavelength'] == 'CG37'
    assert verf_result[1]['B_2_Characteristic_1_Laser_excitation_Wavelength'] == ('CG', 37, 37)
    # Band 2 Characteristic 2 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_2_Laser_excitation_Wavelength'] == 'CG38'
    assert verf_result[1]['B_2_Characteristic_2_Laser_excitation_Wavelength'] == ('CG', 38, 38)
    # Band 2 Characteristic 3 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_3_Laser_excitation_Wavelength'] == 'CG41'
    assert verf_result[1]['B_2_Characteristic_3_Laser_excitation_Wavelength'] == ('CG', 41, 41)
    # Band 2 Characteristic 4 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_4_Laser_excitation_Wavelength'] == 'CG45'
    assert verf_result[1]['B_2_Characteristic_4_Laser_excitation_Wavelength'] == ('CG', 45, 45)
    # Band 2 Characteristic 5 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_5_Laser_excitation_Wavelength'] == 'CG53'
    assert verf_result[1]['B_2_Characteristic_5_Laser_excitation_Wavelength'] == ('CG', 53, 53)
    # Band 3 Characteristic 1 Laser_excitation_Wavelength
    assert verf_result[0]['B_3_Characteristic_1_Laser_excitation_Wavelength'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Laser_excitation_Wavelength'] == ('CG', 57, 57)
    # Band Characteristic Sample_Orient_mode
    # Band 1 Characteristic 1 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_1_Sample_Orient_mode'] == 'oriented'
    assert verf_result[1]['B_1_Characteristic_1_Sample_Orient_mode'] == ('CH', 15, 15)
    # Band 1 Characteristic 2 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_2_Sample_Orient_mode'] == 'unoriented'
    assert verf_result[1]['B_1_Characteristic_2_Sample_Orient_mode'] == ('CH', 16, 16)
    # Band 1 Characteristic 3 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_3_Sample_Orient_mode'] == 'random'
    assert verf_result[1]['B_1_Characteristic_3_Sample_Orient_mode'] == ('CH', 17, 17)
    # Band 1 Characteristic 4 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_4_Sample_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_4_Sample_Orient_mode'] == ('CH', 18, 18)
    # Band 1 Characteristic 5 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_5_Sample_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_5_Sample_Orient_mode'] == ('CH', 19, 19)
    # Band 1 Characteristic 6 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_6_Sample_Orient_mode'] == 'oriented'
    assert verf_result[1]['B_1_Characteristic_6_Sample_Orient_mode'] == ('CH', 20, 20)
    # Band 1 Characteristic 7 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_7_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_7_Sample_Orient_mode'] == ('CH', 25, 25)
    # Band 1 Characteristic 8 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_8_Sample_Orient_mode'] == 'unoriented'
    assert verf_result[1]['B_1_Characteristic_8_Sample_Orient_mode'] == ('CH', 26, 26)
    # Band 1 Characteristic 9 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_9_Sample_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_9_Sample_Orient_mode'] == ('CH', 31, 31)
    # Band 1 Characteristic 10 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_10_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Sample_Orient_mode'] == ('CH', 32, 32)
    # Band 2 Characteristic 1 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_1_Sample_Orient_mode'] == 'unoriented'
    assert verf_result[1]['B_2_Characteristic_1_Sample_Orient_mode'] == ('CH', 37, 37)
    # Band 2 Characteristic 2 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_2_Sample_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Sample_Orient_mode'] == ('CH', 38, 38)
    # Band 2 Characteristic 3 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_3_Sample_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Sample_Orient_mode'] == ('CH', 41, 41)
    # Band 2 Characteristic 4 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_4_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Sample_Orient_mode'] == ('CH', 45, 45)
    # Band 2 Characteristic 5 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_5_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Sample_Orient_mode'] == ('CH', 53, 53)
    # Band 3 Characteristic 1 Sample_Orient_mode
    assert verf_result[0]['B_3_Characteristic_1_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Sample_Orient_mode'] == ('CH', 57, 57)
    # Band Characteristic Sample_Orient
    # Band 1 Characteristic 1 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_1_Sample_Orient'] == 'CI15'
    assert verf_result[1]['B_1_Characteristic_1_Sample_Orient'] == ('CI', 15, 15)
    # Band 1 Characteristic 2 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_2_Sample_Orient'] == 'CI16'
    assert verf_result[1]['B_1_Characteristic_2_Sample_Orient'] == ('CI', 16, 16)
    # Band 1 Characteristic 3 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_3_Sample_Orient'] == 'CI17'
    assert verf_result[1]['B_1_Characteristic_3_Sample_Orient'] == ('CI', 17, 17)
    # Band 1 Characteristic 4 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_4_Sample_Orient'] == 'CI18'
    assert verf_result[1]['B_1_Characteristic_4_Sample_Orient'] == ('CI', 18, 18)
    # Band 1 Characteristic 5 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_5_Sample_Orient'] == 'CI19'
    assert verf_result[1]['B_1_Characteristic_5_Sample_Orient'] == ('CI', 19, 19)
    # Band 1 Characteristic 6 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_6_Sample_Orient'] == 'CI20'
    assert verf_result[1]['B_1_Characteristic_6_Sample_Orient'] == ('CI', 20, 20)
    # Band 1 Characteristic 7 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_7_Sample_Orient'] == 'CI25'
    assert verf_result[1]['B_1_Characteristic_7_Sample_Orient'] == ('CI', 25, 25)
    # Band 1 Characteristic 8 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_8_Sample_Orient'] == 'CI26'
    assert verf_result[1]['B_1_Characteristic_8_Sample_Orient'] == ('CI', 26, 26)
    # Band 1 Characteristic 9 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_9_Sample_Orient'] == 'CI31'
    assert verf_result[1]['B_1_Characteristic_9_Sample_Orient'] == ('CI', 31, 31)
    # Band 1 Characteristic 10 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_10_Sample_Orient'] == 'CI32'
    assert verf_result[1]['B_1_Characteristic_10_Sample_Orient'] == ('CI', 32, 32)
    # Band 2 Characteristic 1 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_1_Sample_Orient'] == 'CI37'
    assert verf_result[1]['B_2_Characteristic_1_Sample_Orient'] == ('CI', 37, 37)
    # Band 2 Characteristic 2 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_2_Sample_Orient'] == 'CI38'
    assert verf_result[1]['B_2_Characteristic_2_Sample_Orient'] == ('CI', 38, 38)
    # Band 2 Characteristic 3 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_3_Sample_Orient'] == 'CI41'
    assert verf_result[1]['B_2_Characteristic_3_Sample_Orient'] == ('CI', 41, 41)
    # Band 2 Characteristic 4 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_4_Sample_Orient'] == 'CI45'
    assert verf_result[1]['B_2_Characteristic_4_Sample_Orient'] == ('CI', 45, 45)
    # Band 2 Characteristic 5 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_5_Sample_Orient'] == 'CI53'
    assert verf_result[1]['B_2_Characteristic_5_Sample_Orient'] == ('CI', 53, 53)
    # Band 3 Characteristic 1 Sample_Orient
    assert verf_result[0]['B_3_Characteristic_1_Sample_Orient'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Sample_Orient'] == ('CI', 57, 57)
    # Band Characteristic Polarization_Orient_mode
    # Band 1 Characteristic 1 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_1_Polarization_Orient_mode'] == 'depolarized'
    assert verf_result[1]['B_1_Characteristic_1_Polarization_Orient_mode'] == ('CJ', 15, 15)
    # Band 1 Characteristic 2 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_2_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_1_Characteristic_2_Polarization_Orient_mode'] == ('CJ', 16, 16)
    # Band 1 Characteristic 3 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_3_Polarization_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_3_Polarization_Orient_mode'] == ('CJ', 17, 17)
    # Band 1 Characteristic 4 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_4_Polarization_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_4_Polarization_Orient_mode'] == ('CJ', 18, 18)
    # Band 1 Characteristic 5 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_5_Polarization_Orient_mode'] == 'depolarized'
    assert verf_result[1]['B_1_Characteristic_5_Polarization_Orient_mode'] == ('CJ', 19, 19)
    # Band 1 Characteristic 6 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_6_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_1_Characteristic_6_Polarization_Orient_mode'] == ('CJ', 20, 20)
    # Band 1 Characteristic 7 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_7_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_7_Polarization_Orient_mode'] == ('CJ', 25, 25)
    # Band 1 Characteristic 8 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_8_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_1_Characteristic_8_Polarization_Orient_mode'] == ('CJ', 26, 26)
    # Band 1 Characteristic 9 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_9_Polarization_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_9_Polarization_Orient_mode'] == ('CJ', 31, 31)
    # Band 1 Characteristic 10 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_10_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Polarization_Orient_mode'] == ('CJ', 32, 32)
    # Band 2 Characteristic 1 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_1_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_2_Characteristic_1_Polarization_Orient_mode'] == ('CJ', 37, 37)
    # Band 2 Characteristic 2 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_2_Polarization_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Polarization_Orient_mode'] == ('CJ', 38, 38)
    # Band 2 Characteristic 3 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_3_Polarization_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Polarization_Orient_mode'] == ('CJ', 41, 41)
    # Band 2 Characteristic 4 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_4_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Polarization_Orient_mode'] == ('CJ', 45, 45)
    # Band 2 Characteristic 5 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_5_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Polarization_Orient_mode'] == ('CJ', 53, 53)
    # Band 3 Characteristic 1 Polarization_Orient_mode
    assert verf_result[0]['B_3_Characteristic_1_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Polarization_Orient_mode'] == ('CJ', 57, 57)
    # Band Characteristic Polarization_Orient
    # Band 1 Characteristic 1 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_1_Polarization_Orient'] == 'CK15'
    assert verf_result[1]['B_1_Characteristic_1_Polarization_Orient'] == ('CK', 15, 15)
    # Band 1 Characteristic 2 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_2_Polarization_Orient'] == 'CK16'
    assert verf_result[1]['B_1_Characteristic_2_Polarization_Orient'] == ('CK', 16, 16)
    # Band 1 Characteristic 3 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_3_Polarization_Orient'] == 'CK17'
    assert verf_result[1]['B_1_Characteristic_3_Polarization_Orient'] == ('CK', 17, 17)
    # Band 1 Characteristic 4 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_4_Polarization_Orient'] == 'CK18'
    assert verf_result[1]['B_1_Characteristic_4_Polarization_Orient'] == ('CK', 18, 18)
    # Band 1 Characteristic 5 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_5_Polarization_Orient'] == 'CK19'
    assert verf_result[1]['B_1_Characteristic_5_Polarization_Orient'] == ('CK', 19, 19)
    # Band 1 Characteristic 6 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_6_Polarization_Orient'] == 'CK20'
    assert verf_result[1]['B_1_Characteristic_6_Polarization_Orient'] == ('CK', 20, 20)
    # Band 1 Characteristic 7 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_7_Polarization_Orient'] == 'CK25'
    assert verf_result[1]['B_1_Characteristic_7_Polarization_Orient'] == ('CK', 25, 25)
    # Band 1 Characteristic 8 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_8_Polarization_Orient'] == 'CK26'
    assert verf_result[1]['B_1_Characteristic_8_Polarization_Orient'] == ('CK', 26, 26)
    # Band 1 Characteristic 9 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_9_Polarization_Orient'] == 'CK31'
    assert verf_result[1]['B_1_Characteristic_9_Polarization_Orient'] == ('CK', 31, 31)
    # Band 1 Characteristic 10 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_10_Polarization_Orient'] == 'CK32'
    assert verf_result[1]['B_1_Characteristic_10_Polarization_Orient'] == ('CK', 32, 32)
    # Band 2 Characteristic 1 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_1_Polarization_Orient'] == 'CK37'
    assert verf_result[1]['B_2_Characteristic_1_Polarization_Orient'] == ('CK', 37, 37)
    # Band 2 Characteristic 2 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_2_Polarization_Orient'] == 'CK38'
    assert verf_result[1]['B_2_Characteristic_2_Polarization_Orient'] == ('CK', 38, 38)
    # Band 2 Characteristic 3 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_3_Polarization_Orient'] == 'CK41'
    assert verf_result[1]['B_2_Characteristic_3_Polarization_Orient'] == ('CK', 41, 41)
    # Band 2 Characteristic 4 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_4_Polarization_Orient'] == 'CK45'
    assert verf_result[1]['B_2_Characteristic_4_Polarization_Orient'] == ('CK', 45, 45)
    # Band 2 Characteristic 5 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_5_Polarization_Orient'] == 'CK53'
    assert verf_result[1]['B_2_Characteristic_5_Polarization_Orient'] == ('CK', 53, 53)
    # Band 3 Characteristic 1 Polarization_Orient
    assert verf_result[0]['B_3_Characteristic_1_Polarization_Orient'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Polarization_Orient'] == ('CK', 57, 57)
    # Band Characteristic Excitation_Comment
    # Band 1 Characteristic 1 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_1_Excitation_Comment'] == 'CL15'
    assert verf_result[1]['B_1_Characteristic_1_Excitation_Comment'] == ('CL', 15, 15)
    # Band 1 Characteristic 2 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_2_Excitation_Comment'] == 'CL16'
    assert verf_result[1]['B_1_Characteristic_2_Excitation_Comment'] == ('CL', 16, 16)
    # Band 1 Characteristic 3 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_3_Excitation_Comment'] == 'CL17'
    assert verf_result[1]['B_1_Characteristic_3_Excitation_Comment'] == ('CL', 17, 17)
    # Band 1 Characteristic 4 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_4_Excitation_Comment'] == 'CL18'
    assert verf_result[1]['B_1_Characteristic_4_Excitation_Comment'] == ('CL', 18, 18)
    # Band 1 Characteristic 5 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_5_Excitation_Comment'] == 'CL19'
    assert verf_result[1]['B_1_Characteristic_5_Excitation_Comment'] == ('CL', 19, 19)
    # Band 1 Characteristic 6 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_6_Excitation_Comment'] == 'CL20'
    assert verf_result[1]['B_1_Characteristic_6_Excitation_Comment'] == ('CL', 20, 20)
    # Band 1 Characteristic 7 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_7_Excitation_Comment'] == 'CL25'
    assert verf_result[1]['B_1_Characteristic_7_Excitation_Comment'] == ('CL', 25, 25)
    # Band 1 Characteristic 8 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_8_Excitation_Comment'] == 'CL26'
    assert verf_result[1]['B_1_Characteristic_8_Excitation_Comment'] == ('CL', 26, 26)
    # Band 1 Characteristic 9 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_9_Excitation_Comment'] == 'CL31'
    assert verf_result[1]['B_1_Characteristic_9_Excitation_Comment'] == ('CL', 31, 31)
    # Band 1 Characteristic 10 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_10_Excitation_Comment'] == 'CL32'
    assert verf_result[1]['B_1_Characteristic_10_Excitation_Comment'] == ('CL', 32, 32)
    # Band 2 Characteristic 1 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_1_Excitation_Comment'] == 'CL37'
    assert verf_result[1]['B_2_Characteristic_1_Excitation_Comment'] == ('CL', 37, 37)
    # Band 2 Characteristic 2 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_2_Excitation_Comment'] == 'CL38'
    assert verf_result[1]['B_2_Characteristic_2_Excitation_Comment'] == ('CL', 38, 38)
    # Band 2 Characteristic 3 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_3_Excitation_Comment'] == 'CL41'
    assert verf_result[1]['B_2_Characteristic_3_Excitation_Comment'] == ('CL', 41, 41)
    # Band 2 Characteristic 4 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_4_Excitation_Comment'] == 'CL45'
    assert verf_result[1]['B_2_Characteristic_4_Excitation_Comment'] == ('CL', 45, 45)
    # Band 2 Characteristic 5 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_5_Excitation_Comment'] == 'CL53'
    assert verf_result[1]['B_2_Characteristic_5_Excitation_Comment'] == ('CL', 53, 53)
    # Band 3 Characteristic 1 Excitation_Comment
    assert verf_result[0]['B_3_Characteristic_1_Excitation_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Excitation_Comment'] == ('CL', 57, 57)
    # Band Characteristic Methods_qty
    # Band 1 Characteristic 1 Methods_qty
    assert verf_result[0]['B_1_Characteristic_1_Methods_qty'] == 1
    # Band 1 Characteristic 2 Methods_qty
    assert verf_result[0]['B_1_Characteristic_2_Methods_qty'] == 1
    # Band 1 Characteristic 3 Methods_qty
    assert verf_result[0]['B_1_Characteristic_3_Methods_qty'] == 1
    # Band 1 Characteristic 4 Methods_qty
    assert verf_result[0]['B_1_Characteristic_4_Methods_qty'] == 1
    # Band 1 Characteristic 5 Methods_qty
    assert verf_result[0]['B_1_Characteristic_5_Methods_qty'] == 1
    # Band 1 Characteristic 6 Methods_qty
    assert verf_result[0]['B_1_Characteristic_6_Methods_qty'] == 3
    # Band 1 Characteristic 7 Methods_qty
    assert verf_result[0]['B_1_Characteristic_7_Methods_qty'] == 1
    # Band 1 Characteristic 8 Methods_qty
    assert verf_result[0]['B_1_Characteristic_8_Methods_qty'] == 1
    # Band 1 Characteristic 9 Methods_qty
    assert verf_result[0]['B_1_Characteristic_9_Methods_qty'] == 1
    # Band 1 Characteristic 10 Methods_qty
    assert verf_result[0]['B_1_Characteristic_10_Methods_qty'] == 1
    # Band 2 Characteristic 1 Methods_qty
    assert verf_result[0]['B_2_Characteristic_1_Methods_qty'] == 1
    # Band 2 Characteristic 2 Methods_qty
    assert verf_result[0]['B_2_Characteristic_2_Methods_qty'] == 1
    # Band 2 Characteristic 3 Methods_qty
    assert verf_result[0]['B_2_Characteristic_3_Methods_qty'] == 3
    # Band 2 Characteristic 4 Methods_qty
    assert verf_result[0]['B_2_Characteristic_4_Methods_qty'] == 4
    # Band 2 Characteristic 5 Methods_qty
    assert verf_result[0]['B_2_Characteristic_5_Methods_qty'] == 1
    # Band 3 Characteristic 1 Methods_qty
    assert verf_result[0]['B_3_Characteristic_1_Methods_qty'] == 1
    # Band Characteristic Method Types
    # Band 1 Characteristic 1 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Types'] == 'spectrum measurement'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Types'] == ('CO', 15, 15)
    # Band 1 Characteristic 2 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Types'] == 'spectrum fit'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Types'] == ('CO', 16, 16)
    # Band 1 Characteristic 3 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Types'] == 'spectrum analysis'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Types'] == ('CO', 17, 17)
    # Band 1 Characteristic 4 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Types'] == 'data compilation'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Types'] == ('CO', 18, 18)
    # Band 1 Characteristic 5 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Types'] == 'data extrapolation'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Types'] == ('CO', 19, 19)
    # Band 1 Characteristic 6 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Types'] == 'theory'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Types'] == ('CO', 20, 20)
    # Band 1 Characteristic 6 Method_2_Types
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Types'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Types'] == ('CO', 22, 22)
    # Band 1 Characteristic 6 Method_3_Types
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Types'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Types'] == ('CO', 23, 23)
    # Band 1 Characteristic 7 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Types'] == 'estimation'
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Types'] == ('CO', 25, 25)
    # Band 1 Characteristic 8 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Types'] == 'various'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Types'] == ('CO', 26, 26)
    # Band 1 Characteristic 9 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Types'] == 'other'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Types'] == ('CO', 31, 31)
    # Band 1 Characteristic 10 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Types'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Types'] == ('CO', 32, 32)
    # Band 2 Characteristic 1 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Types'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Types'] == ('CO', 37, 37)
    # Band 2 Characteristic 2 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Types'] == 'spectrum measurement'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Types'] == ('CO', 38, 38)
    # Band 2 Characteristic 3 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Types'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Types'] == ('CO', 41, 41)
    # Band 2 Characteristic 3 Method_2_Types
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Types'] == 'spectrum analysis'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Types'] == ('CO', 42, 42)
    # Band 2 Characteristic 3 Method_3_Types
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Types'] == ('CO', 44, 44)
    # Band 2 Characteristic 4 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Types'] == ('CO', 45, 45)
    # Band 2 Characteristic 4 Method_2_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Types'] == ('CO', 46, 46)
    # Band 2 Characteristic 4 Method_3_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Types'] == 'data extrapolation'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Types'] == ('CO', 48, 48)
    # Band 2 Characteristic 4 Method_4_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Types'] == ('CO', 49, 49)
    # Band 2 Characteristic 5 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Types'] == ('CO', 53, 53)
    # Band 3 Characteristic 1 Method_1_Types
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Types'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Types'] == ('CO', 57, 57)
    # Band Characteristic Method Description
    # Band 1 Characteristic 1 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Description'] == 'CP15'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Description'] == ('CP', 15, 15)
    # Band 1 Characteristic 2 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Description'] == 'CP16'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Description'] == ('CP', 16, 16)
    # Band 1 Characteristic 3 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Description'] == 'CP17'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Description'] == ('CP', 17, 17)
    # Band 1 Characteristic 4 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Description'] == 'CP18'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Description'] == ('CP', 18, 18)
    # Band 1 Characteristic 5 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Description'] == 'CP19'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Description'] == ('CP', 19, 19)
    # Band 1 Characteristic 6 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Description'] == 'CP20'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Description'] == ('CP', 20, 20)
    # Band 1 Characteristic 6 Method_2_Description
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Description'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Description'] == ('CP', 22, 22)
    # Band 1 Characteristic 6 Method_2_Description
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Description'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Description'] == ('CP', 23, 23)
    # Band 1 Characteristic 7 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Description'] == 'CP25'
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Description'] == ('CP', 25, 25)
    # Band 1 Characteristic 8 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Description'] == 'CP26'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Description'] == ('CP', 26, 26)
    # Band 1 Characteristic 9 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Description'] == 'CP31'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Description'] == ('CP', 31, 31)
    # Band 1 Characteristic 10 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Description'] == 'CP32'
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Description'] == ('CP', 32, 32)
    # Band 2 Characteristic 1 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Description'] == 'CP37'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Description'] == ('CP', 37, 37)
    # Band 2 Characteristic 2 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Description'] == 'CP38'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Description'] == ('CP', 38, 38)
    # Band 2 Characteristic 3 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Description'] == 'CP41'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Description'] == ('CP', 41, 41)
    # Band 2 Characteristic 3 Method_2_Description
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Description'] == 'CP42'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Description'] == ('CP', 42, 42)
    # Band 2 Characteristic 3 Method_3_Description
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Description'] == 'CP44'
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Description'] == ('CP', 44, 44)
    # Band 2 Characteristic 4 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Description'] == 'CP45'
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Description'] == ('CP', 45, 45)
    # Band 2 Characteristic 4 Method_2_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Description'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Description'] == ('CP', 46, 46)
    # Band 2 Characteristic 4 Method_3_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Description'] == 'CP48'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Description'] == ('CP', 48, 48)
    # Band 2 Characteristic 4 Method_4_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Description'] == 'CP49'
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Description'] == ('CP', 49, 49)
    # Band 2 Characteristic 5 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Description'] == 'CP53'
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Description'] == ('CP', 53, 53)
    # Band 3 Characteristic 1 Method_1_Description
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Description'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Description'] == ('CP', 57, 57)
    # Band Characteristic Method Fit_Fct_type
    # Band 1 Characteristic 1 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Fit_Fct_type'] == 'Gaussian'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Fit_Fct_type'] == ('CQ', 15, 15)
    # Band 1 Characteristic 2 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Fit_Fct_type'] == 'Voigt'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Fit_Fct_type'] == ('CQ', 16, 16)
    # Band 1 Characteristic 3 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Fit_Fct_type'] == ('CQ', 17, 17)
    # Band 1 Characteristic 4 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Fit_Fct_type'] == 'BWF'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Fit_Fct_type'] == ('CQ', 18, 18)
    # Band 1 Characteristic 5 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Fit_Fct_type'] == ('CQ', 19, 19)
    # Band 1 Characteristic 6 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Fit_Fct_type'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Fit_Fct_type'] == ('CQ', 20, 20)
    # Band 1 Characteristic 6 Method_2_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Fit_Fct_type'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Fit_Fct_type'] == ('CQ', 22, 22)
    # Band 1 Characteristic 6 Method_3_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Fit_Fct_type'] == 'Voigt'
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Fit_Fct_type'] == ('CQ', 23, 23)
    # Band 1 Characteristic 7 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Fit_Fct_type'] == ('CQ', 25, 25)
    # Band 1 Characteristic 8 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Fit_Fct_type'] == ('CQ', 26, 26)
    # Band 1 Characteristic 9 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Fit_Fct_type'] == ('CQ', 31, 31)
    # Band 1 Characteristic 10 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Fit_Fct_type'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Fit_Fct_type'] == ('CQ', 32, 32)
    # Band 2 Characteristic 1 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Fit_Fct_type'] == ('CQ', 37, 37)
    # Band 2 Characteristic 2 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Fit_Fct_type'] == ('CQ', 38, 38)
    # Band 2 Characteristic 3 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Fit_Fct_type'] == ('CQ', 41, 41)
    # Band 2 Characteristic 3 Method_2_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Fit_Fct_type'] == ('CQ', 42, 42)
    # Band 2 Characteristic 3 Method_2_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Fit_Fct_type'] == ('CQ', 44, 44)
    # Band 2 Characteristic 4 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Fit_Fct_type'] == 'Voigt'
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Fit_Fct_type'] == ('CQ', 45, 45)
    # Band 2 Characteristic 4 Method_2_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Fit_Fct_type'] == ('CQ', 46, 46)
    # Band 2 Characteristic 4 Method_3_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Fit_Fct_type'] == ('CQ', 48, 48)
    # Band 2 Characteristic 4 Method_4_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Fit_Fct_type'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Fit_Fct_type'] == ('CQ', 49, 49)
    # Band 2 Characteristic 5 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Fit_Fct_type'] == ('CQ', 53, 53)
    # Band 3 Characteristic 1 Method_1_Fit_Fct_type
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Fit_Fct_type'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Fit_Fct_type'] == ('CQ', 57, 57)
    # Band Characteristic Method Fit_parameters
    # Band 1 Characteristic 1 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Fit_parameters'] == 'CR15'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Fit_parameters'] == ('CR', 15, 15)
    # Band 1 Characteristic 2 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Fit_parameters'] == 'CR16'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Fit_parameters'] == ('CR', 16, 16)
    # Band 1 Characteristic 3 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Fit_parameters'] == 'CR17'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Fit_parameters'] == ('CR', 17, 17)
    # Band 1 Characteristic 4 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Fit_parameters'] == 'CR18'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Fit_parameters'] == ('CR', 18, 18)
    # Band 1 Characteristic 5 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Fit_parameters'] == 'CR19'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Fit_parameters'] == ('CR', 19, 19)
    # Band 1 Characteristic 6 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Fit_parameters'] == 'CR20'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Fit_parameters'] == ('CR', 20, 20)
    # Band 1 Characteristic 6 Method_2_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Fit_parameters'] == 'CR22'
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Fit_parameters'] == ('CR', 22, 22)
    # Band 1 Characteristic 6 Method_3_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Fit_parameters'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Fit_parameters'] == ('CR', 23, 23)
    # Band 1 Characteristic 7 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Fit_parameters'] == ''
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Fit_parameters'] == ('CR', 25, 25)
    # Band 1 Characteristic 8 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Fit_parameters'] == 'CR26'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Fit_parameters'] == ('CR', 26, 26)
    # Band 1 Characteristic 9 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Fit_parameters'] == 'CR31'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Fit_parameters'] == ('CR', 31, 31)
    # Band 1 Characteristic 10 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Fit_parameters'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Fit_parameters'] == ('CR', 32, 32)
    # Band 2 Characteristic 1 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Fit_parameters'] == 'CR37'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Fit_parameters'] == ('CR', 37, 37)
    # Band 2 Characteristic 2 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Fit_parameters'] == 'CR38'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Fit_parameters'] == ('CR', 38, 38)
    # Band 2 Characteristic 3 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Fit_parameters'] == 'CR41'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Fit_parameters'] == ('CR', 41, 41)
    # Band 2 Characteristic 3 Method_2_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Fit_parameters'] == 'CR42'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Fit_parameters'] == ('CR', 42, 42)
    # Band 2 Characteristic 3 Method_2_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Fit_parameters'] == 'CR44'
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Fit_parameters'] == ('CR', 44, 44)
    # Band 2 Characteristic 4 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Fit_parameters'] == 'CR45'
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Fit_parameters'] == ('CR', 45, 45)
    # Band 2 Characteristic 4 Method_2_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Fit_parameters'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Fit_parameters'] == ('CR', 46, 46)
    # Band 2 Characteristic 4 Method_3_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Fit_parameters'] == 'CR48'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Fit_parameters'] == ('CR', 48, 48)
    # Band 2 Characteristic 4 Method_4_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Fit_parameters'] == 'CR49'
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Fit_parameters'] == ('CR', 49, 49)
    # Band 2 Characteristic 5 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Fit_parameters'] == 'CR53'
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Fit_parameters'] == ('CR', 53, 53)
    # Band 3 Characteristic 1 Method_1_Fit_parameters
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Fit_parameters'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Fit_parameters'] == ('CR', 57, 57)
    # Band Characteristic Methods_Overlap
    # Band 1 Characteristic 1 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_1_Methods_Overlap'] == 'extracted'
    assert verf_result[1]['B_1_Characteristic_1_Methods_Overlap'] == ('CU', 15, 15)
    # Band 1 Characteristic 2 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_2_Methods_Overlap'] == 'isolated'
    assert verf_result[1]['B_1_Characteristic_2_Methods_Overlap'] == ('CU', 16, 16)
    # Band 1 Characteristic 3 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_3_Methods_Overlap'] == 'slightly blended'
    assert verf_result[1]['B_1_Characteristic_3_Methods_Overlap'] == ('CU', 17, 17)
    # Band 1 Characteristic 4 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_4_Methods_Overlap'] == 'moderately blended'
    assert verf_result[1]['B_1_Characteristic_4_Methods_Overlap'] == ('CU', 18, 18)
    # Band 1 Characteristic 5 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_5_Methods_Overlap'] == 'strongly blended'
    assert verf_result[1]['B_1_Characteristic_5_Methods_Overlap'] == ('CU', 19, 19)
    # Band 1 Characteristic 6 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_6_Methods_Overlap'] == 'multiple'
    assert verf_result[1]['B_1_Characteristic_6_Methods_Overlap'] == ('CU', 20, 20)
    # Band 1 Characteristic 7 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_7_Methods_Overlap'] == 'other'
    assert verf_result[1]['B_1_Characteristic_7_Methods_Overlap'] == ('CU', 25, 25)
    # Band 1 Characteristic 8 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_8_Methods_Overlap'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_8_Methods_Overlap'] == ('CU', 26, 26)
    # Band 1 Characteristic 9 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_9_Methods_Overlap'] == ''
    assert verf_result[1]['B_1_Characteristic_9_Methods_Overlap'] == ('CU', 31, 31)
    # Band 1 Characteristic 10 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_10_Methods_Overlap'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_10_Methods_Overlap'] == ('CU', 32, 32)
    # Band 2 Characteristic 1 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_1_Methods_Overlap'] == 'isolated'
    assert verf_result[1]['B_2_Characteristic_1_Methods_Overlap'] == ('CU', 37, 37)
    # Band 2 Characteristic 2 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_2_Methods_Overlap'] == 'strongly blended'
    assert verf_result[1]['B_2_Characteristic_2_Methods_Overlap'] == ('CU', 38, 38)
    # Band 2 Characteristic 3 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_3_Methods_Overlap'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_3_Methods_Overlap'] == ('CU', 41, 41)
    # Band 2 Characteristic 4 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_4_Methods_Overlap'] == 'isolated'
    assert verf_result[1]['B_2_Characteristic_4_Methods_Overlap'] == ('CU', 45, 45)
    # Band 2 Characteristic 5 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_5_Methods_Overlap'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Methods_Overlap'] == ('CU', 53, 53)
    # Band 3 Characteristic 1 Methods_Overlap
    assert verf_result[0]['B_3_Characteristic_1_Methods_Overlap'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Methods_Overlap'] == ('CU', 57, 57)
    # Band Characteristic Position_Peak_method
    # Band 1 Characteristic 1 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_1_Position_Peak_method'] == 'peak'
    assert verf_result[1]['B_1_Characteristic_1_Position_Peak_method'] == ('CW', 15, 15)
    # Band 1 Characteristic 2 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_2_Position_Peak_method'] == 'fit peak'
    assert verf_result[1]['B_1_Characteristic_2_Position_Peak_method'] == ('CW', 16, 16)
    # Band 1 Characteristic 3 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_3_Position_Peak_method'] == '90%-max center'
    assert verf_result[1]['B_1_Characteristic_3_Position_Peak_method'] == ('CW', 17, 17)
    # Band 1 Characteristic 4 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_4_Position_Peak_method'] == 'first derivativee'
    assert verf_result[1]['B_1_Characteristic_4_Position_Peak_method'] == ('CW', 18, 18)
    # Band 1 Characteristic 5 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_5_Position_Peak_method'] == 'second derivative'
    assert verf_result[1]['B_1_Characteristic_5_Position_Peak_method'] == ('CW', 19, 19)
    # Band 1 Characteristic 6 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_6_Position_Peak_method'] == 'higher order derivative'
    assert verf_result[1]['B_1_Characteristic_6_Position_Peak_method'] == ('CW', 20, 20)
    # Band 1 Characteristic 7 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_7_Position_Peak_method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_7_Position_Peak_method'] == ('CW', 25, 25)
    # Band 1 Characteristic 8 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_8_Position_Peak_method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_8_Position_Peak_method'] == ('CW', 26, 26)
    # Band 1 Characteristic 9 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_9_Position_Peak_method'] == ''
    assert verf_result[1]['B_1_Characteristic_9_Position_Peak_method'] == ('CW', 31, 31)
    # Band 1 Characteristic 10 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_10_Position_Peak_method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_10_Position_Peak_method'] == ('CW', 32, 32)
    # Band 2 Characteristic 1 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_1_Position_Peak_method'] == 'calculated'
    assert verf_result[1]['B_2_Characteristic_1_Position_Peak_method'] == ('CW', 37, 37)
    # Band 2 Characteristic 2 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_2_Position_Peak_method'] == 'estimated'
    assert verf_result[1]['B_2_Characteristic_2_Position_Peak_method'] == ('CW', 38, 38)
    # Band 2 Characteristic 3 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_3_Position_Peak_method'] == 'various'
    assert verf_result[1]['B_2_Characteristic_3_Position_Peak_method'] == ('CW', 41, 41)
    # Band 2 Characteristic 4 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_4_Position_Peak_method'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_4_Position_Peak_method'] == ('CW', 45, 45)
    # Band 2 Characteristic 5 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_5_Position_Peak_method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Position_Peak_method'] == ('CW', 53, 53)
    # Band 3 Characteristic 1 Position_Peak_method
    assert verf_result[0]['B_3_Characteristic_1_Position_Peak_method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Peak_method'] == ('CW', 57, 57)
    # Band Characteristic Position_Peak
    # Band 1 Characteristic 1 Position_Peak
    assert verf_result[0]['B_1_Characteristic_1_Position_Peak'] == 'CX15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Peak'] == ('CX', 15, 15)
    # Band 1 Characteristic 2 Position_Peak
    assert verf_result[0]['B_1_Characteristic_2_Position_Peak'] == 'CX16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Peak'] == ('CX', 16, 16)
    # Band 1 Characteristic 3 Position_Peak
    assert verf_result[0]['B_1_Characteristic_3_Position_Peak'] == 'CX17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Peak'] == ('CX', 17, 17)
    # Band 1 Characteristic 4 Position_Peak
    assert verf_result[0]['B_1_Characteristic_4_Position_Peak'] == 'CX18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Peak'] == ('CX', 18, 18)
    # Band 1 Characteristic 5 Position_Peak
    assert verf_result[0]['B_1_Characteristic_5_Position_Peak'] == 'CX19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Peak'] == ('CX', 19, 19)
    # Band 1 Characteristic 6 Position_Peak
    assert verf_result[0]['B_1_Characteristic_6_Position_Peak'] == 'CX20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Peak'] == ('CX', 20, 20)
    # Band 1 Characteristic 7 Position_Peak
    assert verf_result[0]['B_1_Characteristic_7_Position_Peak'] == 'CX25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Peak'] == ('CX', 25, 25)
    # Band 1 Characteristic 8 Position_Peak
    assert verf_result[0]['B_1_Characteristic_8_Position_Peak'] == 'CX26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Peak'] == ('CX', 26, 26)
    # Band 1 Characteristic 9 Position_Peak
    assert verf_result[0]['B_1_Characteristic_9_Position_Peak'] == 'CX31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Peak'] == ('CX', 31, 31)
    # Band 1 Characteristic 10 Position_Peak
    assert verf_result[0]['B_1_Characteristic_10_Position_Peak'] == 'CX32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Peak'] == ('CX', 32, 32)
    # Band 2 Characteristic 1 Position_Peak
    assert verf_result[0]['B_2_Characteristic_1_Position_Peak'] == 'CX37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Peak'] == ('CX', 37, 37)
    # Band 2 Characteristic 2 Position_Peak
    assert verf_result[0]['B_2_Characteristic_2_Position_Peak'] == 'CX38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Peak'] == ('CX', 38, 38)
    # Band 2 Characteristic 3 Position_Peak
    assert verf_result[0]['B_2_Characteristic_3_Position_Peak'] == 'CX41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Peak'] == ('CX', 41, 41)
    # Band 2 Characteristic 4 Position_Peak
    assert verf_result[0]['B_2_Characteristic_4_Position_Peak'] == 'CX45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Peak'] == ('CX', 45, 45)
    # Band 2 Characteristic 5 Position_Peak
    assert verf_result[0]['B_2_Characteristic_5_Position_Peak'] == 'CX53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Peak'] == ('CX', 53, 53)
    # Band 3 Characteristic 1 Position_Peak
    assert verf_result[0]['B_3_Characteristic_1_Position_Peak'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Peak'] == ('CX', 57, 57)
    # Band Characteristic Position_Peak_error
    # Band 1 Characteristic 1 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_1_Position_Peak_error'] == 'CY15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Peak_error'] == ('CY', 15, 15)
    # Band 1 Characteristic 2 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_2_Position_Peak_error'] == 'CY16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Peak_error'] == ('CY', 16, 16)
    # Band 1 Characteristic 3 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_3_Position_Peak_error'] == 'CY17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Peak_error'] == ('CY', 17, 17)
    # Band 1 Characteristic 4 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_4_Position_Peak_error'] == 'CY18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Peak_error'] == ('CY', 18, 18)
    # Band 1 Characteristic 5 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_5_Position_Peak_error'] == 'CY19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Peak_error'] == ('CY', 19, 19)
    # Band 1 Characteristic 6 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_6_Position_Peak_error'] == 'CY20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Peak_error'] == ('CY', 20, 20)
    # Band 1 Characteristic 7 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_7_Position_Peak_error'] == 'CY25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Peak_error'] == ('CY', 25, 25)
    # Band 1 Characteristic 8 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_8_Position_Peak_error'] == 'CY26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Peak_error'] == ('CY', 26, 26)
    # Band 1 Characteristic 9 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_9_Position_Peak_error'] == 'CY31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Peak_error'] == ('CY', 31, 31)
    # Band 1 Characteristic 10 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_10_Position_Peak_error'] == 'CY32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Peak_error'] == ('CY', 32, 32)
    # Band 2 Characteristic 1 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_1_Position_Peak_error'] == 'CY37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Peak_error'] == ('CY', 37, 37)
    # Band 2 Characteristic 2 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_2_Position_Peak_error'] == 'CY38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Peak_error'] == ('CY', 38, 38)
    # Band 2 Characteristic 3 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_3_Position_Peak_error'] == 'CY41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Peak_error'] == ('CY', 41, 41)
    # Band 2 Characteristic 4 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_4_Position_Peak_error'] == 'CY45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Peak_error'] == ('CY', 45, 45)
    # Band 2 Characteristic 5 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_5_Position_Peak_error'] == 'CY53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Peak_error'] == ('CY', 53, 53)
    # Band 3 Characteristic 1 Position_Peak_error
    assert verf_result[0]['B_3_Characteristic_1_Position_Peak_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Peak_error'] == ('CY', 57, 57)
    # Band Characteristic Position_Center_method
    # Band 1 Characteristic 1 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_1_Position_Center_method'] == 'half-max center'
    assert verf_result[1]['B_1_Characteristic_1_Position_Center_method'] == ('CZ', 15, 15)
    # Band 1 Characteristic 2 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_2_Position_Center_method'] == 'fit center'
    assert verf_result[1]['B_1_Characteristic_2_Position_Center_method'] == ('CZ', 16, 16)
    # Band 1 Characteristic 3 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_3_Position_Center_method'] == 'second derivative'
    assert verf_result[1]['B_1_Characteristic_3_Position_Center_method'] == ('CZ', 17, 17)
    # Band 1 Characteristic 4 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_4_Position_Center_method'] == 'higher order derivative'
    assert verf_result[1]['B_1_Characteristic_4_Position_Center_method'] == ('CZ', 18, 18)
    # Band 1 Characteristic 5 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_5_Position_Center_method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_5_Position_Center_method'] == ('CZ', 19, 19)
    # Band 1 Characteristic 6 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_6_Position_Center_method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_6_Position_Center_method'] == ('CZ', 20, 20)
    # Band 1 Characteristic 7 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_7_Position_Center_method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_7_Position_Center_method'] == ('CZ', 25, 25)
    # Band 1 Characteristic 8 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_8_Position_Center_method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_8_Position_Center_method'] == ('CZ', 26, 26)
    # Band 1 Characteristic 9 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_9_Position_Center_method'] == ''
    assert verf_result[1]['B_1_Characteristic_9_Position_Center_method'] == ('CZ', 31, 31)
    # Band 1 Characteristic 10 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_10_Position_Center_method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_10_Position_Center_method'] == ('CZ', 32, 32)
    # Band 2 Characteristic 1 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_1_Position_Center_method'] == 'other'
    assert verf_result[1]['B_2_Characteristic_1_Position_Center_method'] == ('CZ', 37, 37)
    # Band 2 Characteristic 2 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_2_Position_Center_method'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Position_Center_method'] == ('CZ', 38, 38)
    # Band 2 Characteristic 3 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_3_Position_Center_method'] == 'fit center'
    assert verf_result[1]['B_2_Characteristic_3_Position_Center_method'] == ('CZ', 41, 41)
    # Band 2 Characteristic 4 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_4_Position_Center_method'] == 'extrapolated'
    assert verf_result[1]['B_2_Characteristic_4_Position_Center_method'] == ('CZ', 45, 45)
    # Band 2 Characteristic 5 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_5_Position_Center_method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Position_Center_method'] == ('CZ', 53, 53)
    # Band 3 Characteristic 1 Position_Center_method
    assert verf_result[0]['B_3_Characteristic_1_Position_Center_method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Center_method'] == ('CZ', 57, 57)
    # Band Characteristic Position_Center
    # Band 1 Characteristic 1 Position_Center
    assert verf_result[0]['B_1_Characteristic_1_Position_Center'] == 'DA15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Center'] == ('DA', 15, 15)
    # Band 1 Characteristic 2 Position_Center
    assert verf_result[0]['B_1_Characteristic_2_Position_Center'] == 'DA16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Center'] == ('DA', 16, 16)
    # Band 1 Characteristic 3 Position_Center
    assert verf_result[0]['B_1_Characteristic_3_Position_Center'] == 'DA17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Center'] == ('DA', 17, 17)
    # Band 1 Characteristic 4 Position_Center
    assert verf_result[0]['B_1_Characteristic_4_Position_Center'] == 'DA18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Center'] == ('DA', 18, 18)
    # Band 1 Characteristic 5 Position_Center
    assert verf_result[0]['B_1_Characteristic_5_Position_Center'] == 'DA19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Center'] == ('DA', 19, 19)
    # Band 1 Characteristic 6 Position_Center
    assert verf_result[0]['B_1_Characteristic_6_Position_Center'] == 'DA20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Center'] == ('DA', 20, 20)
    # Band 1 Characteristic 7 Position_Center
    assert verf_result[0]['B_1_Characteristic_7_Position_Center'] == 'DA25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Center'] == ('DA', 25, 25)
    # Band 1 Characteristic 8 Position_Center
    assert verf_result[0]['B_1_Characteristic_8_Position_Center'] == 'DA26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Center'] == ('DA', 26, 26)
    # Band 1 Characteristic 9 Position_Center
    assert verf_result[0]['B_1_Characteristic_9_Position_Center'] == 'DA31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Center'] == ('DA', 31, 31)
    # Band 1 Characteristic 10 Position_Center
    assert verf_result[0]['B_1_Characteristic_10_Position_Center'] == 'DA32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Center'] == ('DA', 32, 32)
    # Band 2 Characteristic 1 Position_Center
    assert verf_result[0]['B_2_Characteristic_1_Position_Center'] == 'DA37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Center'] == ('DA', 37, 37)
    # Band 2 Characteristic 2 Position_Center
    assert verf_result[0]['B_2_Characteristic_2_Position_Center'] == 'DA38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Center'] == ('DA', 38, 38)
    # Band 2 Characteristic 3 Position_Center
    assert verf_result[0]['B_2_Characteristic_3_Position_Center'] == 'DA41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Center'] == ('DA', 41, 41)
    # Band 2 Characteristic 4 Position_Center
    assert verf_result[0]['B_2_Characteristic_4_Position_Center'] == 'DA45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Center'] == ('DA', 45, 45)
    # Band 2 Characteristic 5 Position_Center
    assert verf_result[0]['B_2_Characteristic_5_Position_Center'] == 'DA53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Center'] == ('DA', 53, 53)
    # Band 3 Characteristic 1 Position_Center
    assert verf_result[0]['B_3_Characteristic_1_Position_Center'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Center'] == ('DA', 57, 57)
    # Band Characteristic Position_Center_error
    # Band 1 Characteristic 1 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_1_Position_Center_error'] == 'DB15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Center_error'] == ('DB', 15, 15)
    # Band 1 Characteristic 2 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_2_Position_Center_error'] == 'DB16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Center_error'] == ('DB', 16, 16)
    # Band 1 Characteristic 3 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_3_Position_Center_error'] == 'DB17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Center_error'] == ('DB', 17, 17)
    # Band 1 Characteristic 4 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_4_Position_Center_error'] == 'DB18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Center_error'] == ('DB', 18, 18)
    # Band 1 Characteristic 5 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_5_Position_Center_error'] == 'DB19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Center_error'] == ('DB', 19, 19)
    # Band 1 Characteristic 6 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_6_Position_Center_error'] == 'DB20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Center_error'] == ('DB', 20, 20)
    # Band 1 Characteristic 7 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_7_Position_Center_error'] == 'DB25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Center_error'] == ('DB', 25, 25)
    # Band 1 Characteristic 8 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_8_Position_Center_error'] == 'DB26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Center_error'] == ('DB', 26, 26)
    # Band 1 Characteristic 9 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_9_Position_Center_error'] == 'DB31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Center_error'] == ('DB', 31, 31)
    # Band 1 Characteristic 10 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_10_Position_Center_error'] == 'DB32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Center_error'] == ('DB', 32, 32)
    # Band 2 Characteristic 1 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_1_Position_Center_error'] == 'DB37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Center_error'] == ('DB', 37, 37)
    # Band 2 Characteristic 2 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_2_Position_Center_error'] == 'DB38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Center_error'] == ('DB', 38, 38)
    # Band 2 Characteristic 3 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_3_Position_Center_error'] == 'DB41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Center_error'] == ('DB', 41, 41)
    # Band 2 Characteristic 4 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_4_Position_Center_error'] == 'DB45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Center_error'] == ('DB', 45, 45)
    # Band 2 Characteristic 5 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_5_Position_Center_error'] == 'DB53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Center_error'] == ('DB', 53, 53)
    # Band 3 Characteristic 1 Position_Center_error
    assert verf_result[0]['B_3_Characteristic_1_Position_Center_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Center_error'] == ('DB', 57, 57)
    # Band Characteristic Position_Evaluation
    # Band 1 Characteristic 1 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Position_Evaluation'] == ('DC', 15, 15)
    # Band 1 Characteristic 2 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Position_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Position_Evaluation'] == ('DC', 16, 16)
    # Band 1 Characteristic 3 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Position_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Position_Evaluation'] == ('DC', 17, 17)
    # Band 1 Characteristic 4 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Position_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Position_Evaluation'] == ('DC', 18, 18)
    # Band 1 Characteristic 5 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Position_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Position_Evaluation'] == ('DC', 19, 19)
    # Band 1 Characteristic 6 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Position_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Position_Evaluation'] == ('DC', 20, 20)
    # Band 1 Characteristic 7 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_7_Position_Evaluation'] == ('DC', 25, 25)
    # Band 1 Characteristic 8 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Position_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_8_Position_Evaluation'] == ('DC', 26, 26)
    # Band 1 Characteristic 9 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_9_Position_Evaluation'] == ('DC', 31, 31)
    # Band 1 Characteristic 10 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Position_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Position_Evaluation'] == ('DC', 32, 32)
    # Band 2 Characteristic 1 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Position_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_1_Position_Evaluation'] == ('DC', 37, 37)
    # Band 2 Characteristic 2 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Position_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_2_Characteristic_2_Position_Evaluation'] == ('DC', 38, 38)
    # Band 2 Characteristic 3 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_2_Characteristic_3_Position_Evaluation'] == ('DC', 41, 41)
    # Band 2 Characteristic 4 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Position_Evaluation'] == 'with caution'
    assert verf_result[1]['B_2_Characteristic_4_Position_Evaluation'] == ('DC', 45, 45)
    # Band 2 Characteristic 5 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Position_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Position_Evaluation'] == ('DC', 53, 53)
    # Band 3 Characteristic 1 Position_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Position_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Evaluation'] == ('DC', 57, 57)
    # Band Characteristic Position_Comment
    # Band 1 Characteristic 1 Position_Comment
    assert verf_result[0]['B_1_Characteristic_1_Position_Comment'] == 'DD15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Comment'] == ('DD', 15, 15)
    # Band 1 Characteristic 2 Position_Comment
    assert verf_result[0]['B_1_Characteristic_2_Position_Comment'] == 'DD16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Comment'] == ('DD', 16, 16)
    # Band 1 Characteristic 3 Position_Comment
    assert verf_result[0]['B_1_Characteristic_3_Position_Comment'] == 'DD17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Comment'] == ('DD', 17, 17)
    # Band 1 Characteristic 4 Position_Comment
    assert verf_result[0]['B_1_Characteristic_4_Position_Comment'] == 'DD18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Comment'] == ('DD', 18, 18)
    # Band 1 Characteristic 5 Position_Comment
    assert verf_result[0]['B_1_Characteristic_5_Position_Comment'] == 'DD19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Comment'] == ('DD', 19, 19)
    # Band 1 Characteristic 6 Position_Comment
    assert verf_result[0]['B_1_Characteristic_6_Position_Comment'] == 'DD20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Comment'] == ('DD', 20, 20)
    # Band 1 Characteristic 7 Position_Comment
    assert verf_result[0]['B_1_Characteristic_7_Position_Comment'] == 'DD25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Comment'] == ('DD', 25, 25)
    # Band 1 Characteristic 8 Position_Comment
    assert verf_result[0]['B_1_Characteristic_8_Position_Comment'] == 'DD26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Comment'] == ('DD', 26, 26)
    # Band 1 Characteristic 9 Position_Comment
    assert verf_result[0]['B_1_Characteristic_9_Position_Comment'] == 'DD31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Comment'] == ('DD', 31, 31)
    # Band 1 Characteristic 10 Position_Comment
    assert verf_result[0]['B_1_Characteristic_10_Position_Comment'] == 'DD32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Comment'] == ('DD', 32, 32)
    # Band 2 Characteristic 1 Position_Comment
    assert verf_result[0]['B_2_Characteristic_1_Position_Comment'] == 'DD37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Comment'] == ('DD', 37, 37)
    # Band 2 Characteristic 2 Position_Comment
    assert verf_result[0]['B_2_Characteristic_2_Position_Comment'] == 'DD38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Comment'] == ('DD', 38, 38)
    # Band 2 Characteristic 3 Position_Comment
    assert verf_result[0]['B_2_Characteristic_3_Position_Comment'] == 'DD41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Comment'] == ('DD', 41, 41)
    # Band 2 Characteristic 4 Position_Comment
    assert verf_result[0]['B_2_Characteristic_4_Position_Comment'] == 'DD45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Comment'] == ('DD', 45, 45)
    # Band 2 Characteristic 5 Position_Comment
    assert verf_result[0]['B_2_Characteristic_5_Position_Comment'] == 'DD53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Comment'] == ('DD', 53, 53)
    # Band 3 Characteristic 1 Position_Comment
    assert verf_result[0]['B_3_Characteristic_1_Position_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Comment'] == ('DD', 57, 57)
    # Band Characteristic Width_Method
    # Band 1 Characteristic 1 Width_Method
    assert verf_result[0]['B_1_Characteristic_1_Width_Method'] == 'fwhm'
    assert verf_result[1]['B_1_Characteristic_1_Width_Method'] == ('DG', 15, 15)
    # Band 1 Characteristic 2 Width_Method
    assert verf_result[0]['B_1_Characteristic_2_Width_Method'] == 'fit fwhm'
    assert verf_result[1]['B_1_Characteristic_2_Width_Method'] == ('DG', 16, 16)
    # Band 1 Characteristic 3 Width_Method
    assert verf_result[0]['B_1_Characteristic_3_Width_Method'] == 'hwhm'
    assert verf_result[1]['B_1_Characteristic_3_Width_Method'] == ('DG', 17, 17)
    # Band 1 Characteristic 4 Width_Method
    assert verf_result[0]['B_1_Characteristic_4_Width_Method'] == 'first derivative'
    assert verf_result[1]['B_1_Characteristic_4_Width_Method'] == ('DG', 18, 18)
    # Band 1 Characteristic 5 Width_Method
    assert verf_result[0]['B_1_Characteristic_5_Width_Method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_5_Width_Method'] == ('DG', 19, 19)
    # Band 1 Characteristic 6 Width_Method
    assert verf_result[0]['B_1_Characteristic_6_Width_Method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_6_Width_Method'] == ('DG', 20, 20)
    # Band 1 Characteristic 7 Width_Method
    assert verf_result[0]['B_1_Characteristic_7_Width_Method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_7_Width_Method'] == ('DG', 25, 25)
    # Band 1 Characteristic 8 Width_Method
    assert verf_result[0]['B_1_Characteristic_8_Width_Method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_8_Width_Method'] == ('DG', 26, 26)
    # Band 1 Characteristic 9 Width_Method
    assert verf_result[0]['B_1_Characteristic_9_Width_Method'] == 'other'
    assert verf_result[1]['B_1_Characteristic_9_Width_Method'] == ('DG', 31, 31)
    # Band 1 Characteristic 10 Width_Method
    assert verf_result[0]['B_1_Characteristic_10_Width_Method'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_10_Width_Method'] == ('DG', 32, 32)
    # Band 2 Characteristic 1 Width_Method
    assert verf_result[0]['B_2_Characteristic_1_Width_Method'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_1_Width_Method'] == ('DG', 37, 37)
    # Band 2 Characteristic 2 Width_Method
    assert verf_result[0]['B_2_Characteristic_2_Width_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_2_Width_Method'] == ('DG', 38, 38)
    # Band 2 Characteristic 3 Width_Method
    assert verf_result[0]['B_2_Characteristic_3_Width_Method'] == 'first derivative'
    assert verf_result[1]['B_2_Characteristic_3_Width_Method'] == ('DG', 41, 41)
    # Band 2 Characteristic 4 Width_Method
    assert verf_result[0]['B_2_Characteristic_4_Width_Method'] == 'fit fwhm'
    assert verf_result[1]['B_2_Characteristic_4_Width_Method'] == ('DG', 45, 45)
    # Band 2 Characteristic 5 Width_Method
    assert verf_result[0]['B_2_Characteristic_5_Width_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Width_Method'] == ('DG', 53, 53)
    # Band 3 Characteristic 1 Width_Method
    assert verf_result[0]['B_3_Characteristic_1_Width_Method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Method'] == ('DG', 57, 57)
    # Band Characteristic Width_FWHM
    # Band 1 Characteristic 1 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_1_Width_FWHM'] == 'DH15'
    assert verf_result[1]['B_1_Characteristic_1_Width_FWHM'] == ('DH', 15, 15)
    # Band 1 Characteristic 2 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_2_Width_FWHM'] == 'DH16'
    assert verf_result[1]['B_1_Characteristic_2_Width_FWHM'] == ('DH', 16, 16)
    # Band 1 Characteristic 3 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_3_Width_FWHM'] == 'DH17'
    assert verf_result[1]['B_1_Characteristic_3_Width_FWHM'] == ('DH', 17, 17)
    # Band 1 Characteristic 4 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_4_Width_FWHM'] == 'DH18'
    assert verf_result[1]['B_1_Characteristic_4_Width_FWHM'] == ('DH', 18, 18)
    # Band 1 Characteristic 5 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_5_Width_FWHM'] == 'DH19'
    assert verf_result[1]['B_1_Characteristic_5_Width_FWHM'] == ('DH', 19, 19)
    # Band 1 Characteristic 6 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_6_Width_FWHM'] == 'DH20'
    assert verf_result[1]['B_1_Characteristic_6_Width_FWHM'] == ('DH', 20, 20)
    # Band 1 Characteristic 7 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_7_Width_FWHM'] == 'DH25'
    assert verf_result[1]['B_1_Characteristic_7_Width_FWHM'] == ('DH', 25, 25)
    # Band 1 Characteristic 8 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_8_Width_FWHM'] == 'DH26'
    assert verf_result[1]['B_1_Characteristic_8_Width_FWHM'] == ('DH', 26, 26)
    # Band 1 Characteristic 9 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_9_Width_FWHM'] == 'DH31'
    assert verf_result[1]['B_1_Characteristic_9_Width_FWHM'] == ('DH', 31, 31)
    # Band 1 Characteristic 10 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_10_Width_FWHM'] == 'DH32'
    assert verf_result[1]['B_1_Characteristic_10_Width_FWHM'] == ('DH', 32, 32)
    # Band 2 Characteristic 1 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_1_Width_FWHM'] == 'DH37'
    assert verf_result[1]['B_2_Characteristic_1_Width_FWHM'] == ('DH', 37, 37)
    # Band 2 Characteristic 2 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_2_Width_FWHM'] == 'DH38'
    assert verf_result[1]['B_2_Characteristic_2_Width_FWHM'] == ('DH', 38, 38)
    # Band 2 Characteristic 3 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_3_Width_FWHM'] == 'DH41'
    assert verf_result[1]['B_2_Characteristic_3_Width_FWHM'] == ('DH', 41, 41)
    # Band 2 Characteristic 4 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_4_Width_FWHM'] == 'DH45'
    assert verf_result[1]['B_2_Characteristic_4_Width_FWHM'] == ('DH', 45, 45)
    # Band 2 Characteristic 5 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_5_Width_FWHM'] == 'DH53'
    assert verf_result[1]['B_2_Characteristic_5_Width_FWHM'] == ('DH', 53, 53)
    # Band 3 Characteristic 1 Width_FWHM
    assert verf_result[0]['B_3_Characteristic_1_Width_FWHM'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_FWHM'] == ('DH', 57, 57)
    # Band Characteristic Width_FWHM_error
    # Band 1 Characteristic 1 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_1_Width_FWHM_error'] == 'DI15'
    assert verf_result[1]['B_1_Characteristic_1_Width_FWHM_error'] == ('DI', 15, 15)
    # Band 1 Characteristic 2 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_2_Width_FWHM_error'] == 'DI16'
    assert verf_result[1]['B_1_Characteristic_2_Width_FWHM_error'] == ('DI', 16, 16)
    # Band 1 Characteristic 3 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_3_Width_FWHM_error'] == 'DI17'
    assert verf_result[1]['B_1_Characteristic_3_Width_FWHM_error'] == ('DI', 17, 17)
    # Band 1 Characteristic 4 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_4_Width_FWHM_error'] == 'DI18'
    assert verf_result[1]['B_1_Characteristic_4_Width_FWHM_error'] == ('DI', 18, 18)
    # Band 1 Characteristic 5 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_5_Width_FWHM_error'] == 'DI19'
    assert verf_result[1]['B_1_Characteristic_5_Width_FWHM_error'] == ('DI', 19, 19)
    # Band 1 Characteristic 6 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_6_Width_FWHM_error'] == 'DI20'
    assert verf_result[1]['B_1_Characteristic_6_Width_FWHM_error'] == ('DI', 20, 20)
    # Band 1 Characteristic 7 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_7_Width_FWHM_error'] == 'DI25'
    assert verf_result[1]['B_1_Characteristic_7_Width_FWHM_error'] == ('DI', 25, 25)
    # Band 1 Characteristic 8 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_8_Width_FWHM_error'] == 'DI26'
    assert verf_result[1]['B_1_Characteristic_8_Width_FWHM_error'] == ('DI', 26, 26)
    # Band 1 Characteristic 9 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_9_Width_FWHM_error'] == 'DI31'
    assert verf_result[1]['B_1_Characteristic_9_Width_FWHM_error'] == ('DI', 31, 31)
    # Band 1 Characteristic 10 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_10_Width_FWHM_error'] == 'DI32'
    assert verf_result[1]['B_1_Characteristic_10_Width_FWHM_error'] == ('DI', 32, 32)
    # Band 2 Characteristic 1 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_1_Width_FWHM_error'] == 'DI37'
    assert verf_result[1]['B_2_Characteristic_1_Width_FWHM_error'] == ('DI', 37, 37)
    # Band 2 Characteristic 2 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_2_Width_FWHM_error'] == 'DI38'
    assert verf_result[1]['B_2_Characteristic_2_Width_FWHM_error'] == ('DI', 38, 38)
    # Band 2 Characteristic 3 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_3_Width_FWHM_error'] == 'DI41'
    assert verf_result[1]['B_2_Characteristic_3_Width_FWHM_error'] == ('DI', 41, 41)
    # Band 2 Characteristic 4 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_4_Width_FWHM_error'] == 'DI45'
    assert verf_result[1]['B_2_Characteristic_4_Width_FWHM_error'] == ('DI', 45, 45)
    # Band 2 Characteristic 5 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_5_Width_FWHM_error'] == 'DI53'
    assert verf_result[1]['B_2_Characteristic_5_Width_FWHM_error'] == ('DI', 53, 53)
    # Band 3 Characteristic 1 Width_FWHM_error
    assert verf_result[0]['B_3_Characteristic_1_Width_FWHM_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_FWHM_error'] == ('DI', 57, 57)
    # Band Characteristic Width_Shape
    # Band 1 Characteristic 1 Width_Shape
    assert verf_result[0]['B_1_Characteristic_1_Width_Shape'] == 'symmetric'
    assert verf_result[1]['B_1_Characteristic_1_Width_Shape'] == ('DJ', 15, 15)
    # Band 1 Characteristic 2 Width_Shape
    assert verf_result[0]['B_1_Characteristic_2_Width_Shape'] == 'gaussian'
    assert verf_result[1]['B_1_Characteristic_2_Width_Shape'] == ('DJ', 16, 16)
    # Band 1 Characteristic 3 Width_Shape
    assert verf_result[0]['B_1_Characteristic_3_Width_Shape'] == 'lorentzian'
    assert verf_result[1]['B_1_Characteristic_3_Width_Shape'] == ('DJ', 17, 17)
    # Band 1 Characteristic 4 Width_Shape
    assert verf_result[0]['B_1_Characteristic_4_Width_Shape'] == 'voigt'
    assert verf_result[1]['B_1_Characteristic_4_Width_Shape'] == ('DJ', 18, 18)
    # Band 1 Characteristic 5 Width_Shape
    assert verf_result[0]['B_1_Characteristic_5_Width_Shape'] == 'doppler'
    assert verf_result[1]['B_1_Characteristic_5_Width_Shape'] == ('DJ', 19, 19)
    # Band 1 Characteristic 6 Width_Shape
    assert verf_result[0]['B_1_Characteristic_6_Width_Shape'] == 'asymmetric'
    assert verf_result[1]['B_1_Characteristic_6_Width_Shape'] == ('DJ', 20, 20)
    # Band 1 Characteristic 7 Width_Shape
    assert verf_result[0]['B_1_Characteristic_7_Width_Shape'] == 'asymmetric low frequency wing'
    assert verf_result[1]['B_1_Characteristic_7_Width_Shape'] == ('DJ', 25, 25)
    # Band 1 Characteristic 8 Width_Shape
    assert verf_result[0]['B_1_Characteristic_8_Width_Shape'] == 'asymmetric high frequency wing'
    assert verf_result[1]['B_1_Characteristic_8_Width_Shape'] == ('DJ', 26, 26)
    # Band 1 Characteristic 9 Width_Shape
    assert verf_result[0]['B_1_Characteristic_9_Width_Shape'] == 'shoulder'
    assert verf_result[1]['B_1_Characteristic_9_Width_Shape'] == ('DJ', 31, 31)
    # Band 1 Characteristic 10 Width_Shape
    assert verf_result[0]['B_1_Characteristic_10_Width_Shape'] == 'sharp shoulder'
    assert verf_result[1]['B_1_Characteristic_10_Width_Shape'] == ('DJ', 32, 32)
    # Band 2 Characteristic 1 Width_Shape
    assert verf_result[0]['B_2_Characteristic_1_Width_Shape'] == 'broad shoulder'
    assert verf_result[1]['B_2_Characteristic_1_Width_Shape'] == ('DJ', 37, 37)
    # Band 2 Characteristic 2 Width_Shape
    assert verf_result[0]['B_2_Characteristic_2_Width_Shape'] == 'low frequency tail'
    assert verf_result[1]['B_2_Characteristic_2_Width_Shape'] == ('DJ', 38, 38)
    # Band 2 Characteristic 3 Width_Shape
    assert verf_result[0]['B_2_Characteristic_3_Width_Shape'] == 'undefined'
    assert verf_result[1]['B_2_Characteristic_3_Width_Shape'] == ('DJ', 41, 41)
    # Band 2 Characteristic 4 Width_Shape
    assert verf_result[0]['B_2_Characteristic_4_Width_Shape'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Width_Shape'] == ('DJ', 45, 45)
    # Band 2 Characteristic 5 Width_Shape
    assert verf_result[0]['B_2_Characteristic_5_Width_Shape'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Width_Shape'] == ('DJ', 53, 53)
    # Band 3 Characteristic 1 Width_Shape
    assert verf_result[0]['B_3_Characteristic_1_Width_Shape'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Shape'] == ('DJ', 57, 57)
    # Band Characteristic Width_Asymm_factor
    # Band 1 Characteristic 1 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_1_Width_Asymm_factor'] == 'DK15'
    assert verf_result[1]['B_1_Characteristic_1_Width_Asymm_factor'] == ('DK', 15, 15)
    # Band 1 Characteristic 2 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_2_Width_Asymm_factor'] == 'DK16'
    assert verf_result[1]['B_1_Characteristic_2_Width_Asymm_factor'] == ('DK', 16, 16)
    # Band 1 Characteristic 3 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_3_Width_Asymm_factor'] == 'DK17'
    assert verf_result[1]['B_1_Characteristic_3_Width_Asymm_factor'] == ('DK', 17, 17)
    # Band 1 Characteristic 4 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_4_Width_Asymm_factor'] == 'DK18'
    assert verf_result[1]['B_1_Characteristic_4_Width_Asymm_factor'] == ('DK', 18, 18)
    # Band 1 Characteristic 5 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_5_Width_Asymm_factor'] == 'DK19'
    assert verf_result[1]['B_1_Characteristic_5_Width_Asymm_factor'] == ('DK', 19, 19)
    # Band 1 Characteristic 6 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_6_Width_Asymm_factor'] == 'DK20'
    assert verf_result[1]['B_1_Characteristic_6_Width_Asymm_factor'] == ('DK', 20, 20)
    # Band 1 Characteristic 7 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_7_Width_Asymm_factor'] == 'DK25'
    assert verf_result[1]['B_1_Characteristic_7_Width_Asymm_factor'] == ('DK', 25, 25)
    # Band 1 Characteristic 8 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_8_Width_Asymm_factor'] == 'DK26'
    assert verf_result[1]['B_1_Characteristic_8_Width_Asymm_factor'] == ('DK', 26, 26)
    # Band 1 Characteristic 9 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_9_Width_Asymm_factor'] == 'DK31'
    assert verf_result[1]['B_1_Characteristic_9_Width_Asymm_factor'] == ('DK', 31, 31)
    # Band 1 Characteristic 10 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_10_Width_Asymm_factor'] == 'DK32'
    assert verf_result[1]['B_1_Characteristic_10_Width_Asymm_factor'] == ('DK', 32, 32)
    # Band 2 Characteristic 1 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_1_Width_Asymm_factor'] == 'DK37'
    assert verf_result[1]['B_2_Characteristic_1_Width_Asymm_factor'] == ('DK', 37, 37)
    # Band 2 Characteristic 2 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_2_Width_Asymm_factor'] == 'DK38'
    assert verf_result[1]['B_2_Characteristic_2_Width_Asymm_factor'] == ('DK', 38, 38)
    # Band 2 Characteristic 3 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_3_Width_Asymm_factor'] == 'DK41'
    assert verf_result[1]['B_2_Characteristic_3_Width_Asymm_factor'] == ('DK', 41, 41)
    # Band 2 Characteristic 4 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_4_Width_Asymm_factor'] == 'DK45'
    assert verf_result[1]['B_2_Characteristic_4_Width_Asymm_factor'] == ('DK', 45, 45)
    # Band 2 Characteristic 5 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_5_Width_Asymm_factor'] == 'DK53'
    assert verf_result[1]['B_2_Characteristic_5_Width_Asymm_factor'] == ('DK', 53, 53)
    # Band 3 Characteristic 1 Width_Asymm_factor
    assert verf_result[0]['B_3_Characteristic_1_Width_Asymm_factor'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Asymm_factor'] == ('DK', 57, 57)
    # Band Characteristic Width_Asymm_factor_error
    # Band 1 Characteristic 1 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_1_Width_Asymm_factor_error'] == 'DL15'
    assert verf_result[1]['B_1_Characteristic_1_Width_Asymm_factor_error'] == ('DL', 15, 15)
    # Band 1 Characteristic 2 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_2_Width_Asymm_factor_error'] == 'DL16'
    assert verf_result[1]['B_1_Characteristic_2_Width_Asymm_factor_error'] == ('DL', 16, 16)
    # Band 1 Characteristic 3 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_3_Width_Asymm_factor_error'] == 'DL17'
    assert verf_result[1]['B_1_Characteristic_3_Width_Asymm_factor_error'] == ('DL', 17, 17)
    # Band 1 Characteristic 4 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_4_Width_Asymm_factor_error'] == 'DL18'
    assert verf_result[1]['B_1_Characteristic_4_Width_Asymm_factor_error'] == ('DL', 18, 18)
    # Band 1 Characteristic 5 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_5_Width_Asymm_factor_error'] == 'DL19'
    assert verf_result[1]['B_1_Characteristic_5_Width_Asymm_factor_error'] == ('DL', 19, 19)
    # Band 1 Characteristic 6 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_6_Width_Asymm_factor_error'] == 'DL20'
    assert verf_result[1]['B_1_Characteristic_6_Width_Asymm_factor_error'] == ('DL', 20, 20)
    # Band 1 Characteristic 7 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_7_Width_Asymm_factor_error'] == 'DL25'
    assert verf_result[1]['B_1_Characteristic_7_Width_Asymm_factor_error'] == ('DL', 25, 25)
    # Band 1 Characteristic 8 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_8_Width_Asymm_factor_error'] == 'DL26'
    assert verf_result[1]['B_1_Characteristic_8_Width_Asymm_factor_error'] == ('DL', 26, 26)
    # Band 1 Characteristic 9 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_9_Width_Asymm_factor_error'] == 'DL31'
    assert verf_result[1]['B_1_Characteristic_9_Width_Asymm_factor_error'] == ('DL', 31, 31)
    # Band 1 Characteristic 10 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_10_Width_Asymm_factor_error'] == 'DL32'
    assert verf_result[1]['B_1_Characteristic_10_Width_Asymm_factor_error'] == ('DL', 32, 32)
    # Band 2 Characteristic 1 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_1_Width_Asymm_factor_error'] == 'DL37'
    assert verf_result[1]['B_2_Characteristic_1_Width_Asymm_factor_error'] == ('DL', 37, 37)
    # Band 2 Characteristic 2 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_2_Width_Asymm_factor_error'] == 'DL38'
    assert verf_result[1]['B_2_Characteristic_2_Width_Asymm_factor_error'] == ('DL', 38, 38)
    # Band 2 Characteristic 3 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_3_Width_Asymm_factor_error'] == 'DL41'
    assert verf_result[1]['B_2_Characteristic_3_Width_Asymm_factor_error'] == ('DL', 41, 41)
    # Band 2 Characteristic 4 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_4_Width_Asymm_factor_error'] == 'DL45'
    assert verf_result[1]['B_2_Characteristic_4_Width_Asymm_factor_error'] == ('DL', 45, 45)
    # Band 2 Characteristic 5 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_5_Width_Asymm_factor_error'] == 'DL53'
    assert verf_result[1]['B_2_Characteristic_5_Width_Asymm_factor_error'] == ('DL', 53, 53)
    # Band 3 Characteristic 1 Width_Asymm_factor_error
    assert verf_result[0]['B_3_Characteristic_1_Width_Asymm_factor_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Asymm_factor_error'] == ('DL', 57, 57)
    # Band Characteristic Width_Evaluation
    # Band 1 Characteristic 1 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Width_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Width_Evaluation'] == ('DM', 15, 15)
    # Band 1 Characteristic 2 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Width_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Width_Evaluation'] == ('DM', 16, 16)
    # Band 1 Characteristic 3 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Width_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Width_Evaluation'] == ('DM', 17, 17)
    # Band 1 Characteristic 4 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Width_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Width_Evaluation'] == ('DM', 18, 18)
    # Band 1 Characteristic 5 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Width_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Width_Evaluation'] == ('DM', 19, 19)
    # Band 1 Characteristic 6 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Width_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Width_Evaluation'] == ('DM', 20, 20)
    # Band 1 Characteristic 7 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Width_Evaluation'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_7_Width_Evaluation'] == ('DM', 25, 25)
    # Band 1 Characteristic 8 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Width_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_8_Width_Evaluation'] == ('DM', 26, 26)
    # Band 1 Characteristic 9 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Width_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_9_Width_Evaluation'] == ('DM', 31, 31)
    # Band 1 Characteristic 10 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Width_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Width_Evaluation'] == ('DM', 32, 32)
    # Band 2 Characteristic 1 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Width_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_1_Width_Evaluation'] == ('DM', 37, 37)
    # Band 2 Characteristic 2 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Width_Evaluation'] == 'with caution'
    assert verf_result[1]['B_2_Characteristic_2_Width_Evaluation'] == ('DM', 38, 38)
    # Band 2 Characteristic 3 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Width_Evaluation'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Width_Evaluation'] == ('DM', 41, 41)
    # Band 2 Characteristic 4 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Width_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_4_Width_Evaluation'] == ('DM', 45, 45)
    # Band 2 Characteristic 5 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Width_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Width_Evaluation'] == ('DM', 53, 53)
    # Band 3 Characteristic 1 Width_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Width_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Evaluation'] == ('DM', 57, 57)
    # Band Characteristic Width_Comments
    # Band 1 Characteristic 1 Width_Comments
    assert verf_result[0]['B_1_Characteristic_1_Width_Comments'] == 'DN15'
    assert verf_result[1]['B_1_Characteristic_1_Width_Comments'] == ('DN', 15, 15)
    # Band 1 Characteristic 2 Width_Comments
    assert verf_result[0]['B_1_Characteristic_2_Width_Comments'] == 'DN16'
    assert verf_result[1]['B_1_Characteristic_2_Width_Comments'] == ('DN', 16, 16)
    # Band 1 Characteristic 3 Width_Comments
    assert verf_result[0]['B_1_Characteristic_3_Width_Comments'] == 'DN17'
    assert verf_result[1]['B_1_Characteristic_3_Width_Comments'] == ('DN', 17, 17)
    # Band 1 Characteristic 4 Width_Comments
    assert verf_result[0]['B_1_Characteristic_4_Width_Comments'] == 'DN18'
    assert verf_result[1]['B_1_Characteristic_4_Width_Comments'] == ('DN', 18, 18)
    # Band 1 Characteristic 5 Width_Comments
    assert verf_result[0]['B_1_Characteristic_5_Width_Comments'] == 'DN19'
    assert verf_result[1]['B_1_Characteristic_5_Width_Comments'] == ('DN', 19, 19)
    # Band 1 Characteristic 6 Width_Comments
    assert verf_result[0]['B_1_Characteristic_6_Width_Comments'] == 'DN20'
    assert verf_result[1]['B_1_Characteristic_6_Width_Comments'] == ('DN', 20, 20)
    # Band 1 Characteristic 7 Width_Comments
    assert verf_result[0]['B_1_Characteristic_7_Width_Comments'] == 'DN25'
    assert verf_result[1]['B_1_Characteristic_7_Width_Comments'] == ('DN', 25, 25)
    # Band 1 Characteristic 8 Width_Comments
    assert verf_result[0]['B_1_Characteristic_8_Width_Comments'] == 'DN26'
    assert verf_result[1]['B_1_Characteristic_8_Width_Comments'] == ('DN', 26, 26)
    # Band 1 Characteristic 9 Width_Comments
    assert verf_result[0]['B_1_Characteristic_9_Width_Comments'] == 'DN31'
    assert verf_result[1]['B_1_Characteristic_9_Width_Comments'] == ('DN', 31, 31)
    # Band 1 Characteristic 10 Width_Comments
    assert verf_result[0]['B_1_Characteristic_10_Width_Comments'] == 'DN32'
    assert verf_result[1]['B_1_Characteristic_10_Width_Comments'] == ('DN', 32, 32)
    # Band 2 Characteristic 1 Width_Comments
    assert verf_result[0]['B_2_Characteristic_1_Width_Comments'] == 'DN37'
    assert verf_result[1]['B_2_Characteristic_1_Width_Comments'] == ('DN', 37, 37)
    # Band 2 Characteristic 2 Width_Comments
    assert verf_result[0]['B_2_Characteristic_2_Width_Comments'] == 'DN38'
    assert verf_result[1]['B_2_Characteristic_2_Width_Comments'] == ('DN', 38, 38)
    # Band 2 Characteristic 3 Width_Comments
    assert verf_result[0]['B_2_Characteristic_3_Width_Comments'] == 'DN41'
    assert verf_result[1]['B_2_Characteristic_3_Width_Comments'] == ('DN', 41, 41)
    # Band 2 Characteristic 4 Width_Comments
    assert verf_result[0]['B_2_Characteristic_4_Width_Comments'] == 'DN45'
    assert verf_result[1]['B_2_Characteristic_4_Width_Comments'] == ('DN', 45, 45)
    # Band 2 Characteristic 5 Width_Comments
    assert verf_result[0]['B_2_Characteristic_5_Width_Comments'] == 'DN53'
    assert verf_result[1]['B_2_Characteristic_5_Width_Comments'] == ('DN', 53, 53)
    # Band 3 Characteristic 1 Width_Comments
    assert verf_result[0]['B_3_Characteristic_1_Width_Comments'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Comments'] == ('DN', 57, 57)
    # Band Characteristic Peak_intensity_Method
    # Band 1 Characteristic 1 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Method'] == 'baseline corrected peak intensity'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Method'] == ('DQ', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Method'] == 'peak intensity'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Method'] == ('DQ', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Method'] == 'fit intensity'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Method'] == ('DQ', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Method'] == ('DQ', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Method'] == ('DQ', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Method'] == ('DQ', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Method'] == ('DQ', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Method'] == 'other'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Method'] == ('DQ', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Method'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Method'] == ('DQ', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Method'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Method'] == ('DQ', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Method'] == 'baseline corrected peak intensity'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Method'] == ('DQ', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Method'] == 'other'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Method'] == ('DQ', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Method'] == 'various'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Method'] == ('DQ', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Method'] == 'calculated'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Method'] == ('DQ', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Method'] == ('DQ', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Method
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Method'] == ('DQ', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef'] == 'DR15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef'] == ('DR', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef'] == 'DR16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef'] == ('DR', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef'] == 'DR17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef'] == ('DR', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef'] == 'DR18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef'] == ('DR', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef'] == 'DR19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef'] == ('DR', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef'] == 'DR20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef'] == ('DR', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef'] == 'DR25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef'] == ('DR', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef'] == 'DR26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef'] == ('DR', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef'] == 'DR31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef'] == ('DR', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef'] == 'DR32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef'] == ('DR', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef'] == 'DR37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef'] == ('DR', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef'] == 'DR38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef'] == ('DR', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef'] == 'DR41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef'] == ('DR', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef'] == 'DR45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef'] == ('DR', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef'] == 'DR53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef'] == ('DR', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef'] == ('DR', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef_error
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef_error'] == 'DS15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef_error'] == ('DS', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef_error'] == 'DS16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef_error'] == ('DS', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef_error'] == 'DS17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef_error'] == ('DS', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef_error'] == 'DS18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef_error'] == ('DS', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef_error'] == 'DS19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef_error'] == ('DS', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef_error'] == 'DS20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef_error'] == ('DS', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef_error'] == 'DS25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef_error'] == ('DS', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef_error'] == 'DS26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef_error'] == ('DS', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef_error'] == 'DS31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef_error'] == ('DS', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef_error'] == 'DS32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef_error'] == ('DS', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef_error'] == 'DS37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef_error'] == ('DS', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef_error'] == 'DS38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef_error'] == ('DS', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef_error'] == 'DS41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef_error'] == ('DS', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef_error'] == 'DS45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef_error'] == ('DS', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef_error'] == 'DS53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef_error'] == ('DS', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef_error'] == ('DS', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef_sp
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp'] == 'DT15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ('DT', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp'] == 'DT16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp'] == ('DT', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp'] == 'DT17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp'] == ('DT', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp'] == 'DT18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp'] == ('DT', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp'] == 'DT19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp'] == ('DT', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp'] == 'DT20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp'] == ('DT', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp'] == 'DT25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp'] == ('DT', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp'] == 'DT26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp'] == ('DT', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp'] == 'DT31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp'] == ('DT', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp'] == 'DT32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp'] == ('DT', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp'] == 'DT37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ('DT', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp'] == 'DT38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp'] == ('DT', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp'] == 'DT41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp'] == ('DT', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp'] == 'DT45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp'] == ('DT', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp'] == 'DT53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp'] == ('DT', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ('DT', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef_sp_error
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == 'DU15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ('DU', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == 'DU16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == ('DU', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == 'DU17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == ('DU', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == 'DU18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == ('DU', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == 'DU19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == ('DU', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp_error'] == 'DU20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp_error'] == ('DU', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp_error'] == 'DU25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp_error'] == ('DU', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp_error'] == 'DU26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp_error'] == ('DU', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp_error'] == 'DU31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp_error'] == ('DU', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp_error'] == 'DU32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp_error'] == ('DU', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == 'DU37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ('DU', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == 'DU38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == ('DU', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == 'DU41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == ('DU', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == 'DU45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == ('DU', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == 'DU53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == ('DU', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ('DU', 57, 57)
    # Band Characteristic Peak_intensity_Relative
    # Band 1 Characteristic 1 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Relative'] == 'DV15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Relative'] == ('DV', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Relative'] == 'DV16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Relative'] == ('DV', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Relative'] == 'DV17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Relative'] == ('DV', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Relative'] == 'DV18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Relative'] == ('DV', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Relative'] == 'DV19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Relative'] == ('DV', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Relative'] == 'DV20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Relative'] == ('DV', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Relative'] == 'DV25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Relative'] == ('DV', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Relative'] == 'DV26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Relative'] == ('DV', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Relative'] == 'DV31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Relative'] == ('DV', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Relative'] == 'DV32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Relative'] == ('DV', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Relative'] == 'DV37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Relative'] == ('DV', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Relative'] == 'DV38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Relative'] == ('DV', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Relative'] == 'DV41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Relative'] == ('DV', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Relative'] == 'DV45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Relative'] == ('DV', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Relative'] == 'DV53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Relative'] == ('DV', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Relative
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Relative'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Relative'] == ('DV', 57, 57)
    # Band Characteristic Peak_intensity_Relative_error
    # Band 1 Characteristic 1 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Relative_error'] == 'DW15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Relative_error'] == ('DW', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Relative_error'] == 'DW16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Relative_error'] == ('DW', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Relative_error'] == 'DW17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Relative_error'] == ('DW', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Relative_error'] == 'DW18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Relative_error'] == ('DW', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Relative_error'] == 'DW19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Relative_error'] == ('DW', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Relative_error'] == 'DW20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Relative_error'] == ('DW', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Relative_error'] == 'DW25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Relative_error'] == ('DW', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Relative_error'] == 'DW26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Relative_error'] == ('DW', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Relative_error'] == 'DW31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Relative_error'] == ('DW', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Relative_error'] == 'DW32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Relative_error'] == ('DW', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Relative_error'] == 'DW37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Relative_error'] == ('DW', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Relative_error'] == 'DW38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Relative_error'] == ('DW', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Relative_error'] == 'DW41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Relative_error'] == ('DW', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Relative_error'] == 'DW45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Relative_error'] == ('DW', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Relative_error'] == 'DW53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Relative_error'] == ('DW', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Relative_error
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Relative_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Relative_error'] == ('DW', 57, 57)
    # Band Characteristic Peak_intensity_Strength
    # Band 1 Characteristic 1 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Strength'] == 'ia'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Strength'] == ('DX', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Strength'] == 'ew'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Strength'] == ('DX', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Strength'] == 'vvw'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Strength'] == ('DX', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Strength'] == 'vw'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Strength'] == ('DX', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Strength'] == 'w'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Strength'] == ('DX', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Strength'] == 'm'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Strength'] == ('DX', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Strength'] == 's'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Strength'] == ('DX', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Strength'] == 'vs'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Strength'] == ('DX', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Strength'] == 'vvs'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Strength'] == ('DX', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Strength'] == 'es'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Strength'] == ('DX', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Strength'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Strength'] == ('DX', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Strength'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Strength'] == ('DX', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Strength'] == ('DX', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Strength'] == 'w'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Strength'] == ('DX', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Strength'] == ('DX', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Strength
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Strength'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Strength'] == ('DX', 57, 57)
    # Band Characteristic Peak_intensity_Evaluation
    # Band 1 Characteristic 1 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Evaluation'] == ('EA', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Evaluation'] == ('EA', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Evaluation'] == ('EA', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Evaluation'] == ('EA', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Evaluation'] == ('EA', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Evaluation'] == ('EA', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Evaluation'] == ('EA', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Evaluation'] == ('EA', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Evaluation'] == ('EA', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Evaluation'] == ('EA', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Evaluation'] == ('EA', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Evaluation'] == ('EA', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Evaluation'] == ('EA', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Evaluation'] == ('EA', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Evaluation'] == ('EA', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Evaluation'] == ('EA', 57, 57)
    # Band Characteristic Peak_intensity_Comment
    # Band 1 Characteristic 1 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Comment'] == 'EB15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Comment'] == ('EB', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Comment'] == 'EB16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Comment'] == ('EB', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Comment'] == 'EB17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Comment'] == ('EB', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Comment'] == 'EB18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Comment'] == ('EB', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Comment'] == 'EB19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Comment'] == ('EB', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Comment'] == 'EB20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Comment'] == ('EB', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Comment'] == 'EB25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Comment'] == ('EB', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Comment'] == 'EB26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Comment'] == ('EB', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Comment'] == 'EB31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Comment'] == ('EB', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Comment'] == 'EB32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Comment'] == ('EB', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Comment'] == 'EB37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Comment'] == ('EB', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Comment'] == 'EB38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Comment'] == ('EB', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Comment'] == 'EB41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Comment'] == ('EB', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Comment'] == 'EB45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Comment'] == ('EB', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Comment'] == 'EB53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Comment'] == ('EB', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Comment
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Comment'] == ('EB', 57, 57)
    # Band Characteristic Integrated_intensity_Method
    # Band 1 Characteristic 1 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Method'] == 'band integrated intensity'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Method'] == ('EE', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Method'] == 'width x peak intensity'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Method'] == ('EE', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Method'] == 'fit integrated intensity'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Method'] == ('EE', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Method'] == ('EE', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Method'] == ('EE', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Method'] == ('EE', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Method'] == ('EE', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Method'] == 'other'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Method'] == ('EE', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Method'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Method'] == ('EE', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Method'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Method'] == ('EE', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Method'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Method'] == ('EE', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Method'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Method'] == ('EE', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Method'] == 'band integrated intensity'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Method'] == ('EE', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Method'] == 'fit integrated intensity'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Method'] == ('EE', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Method'] == ('EE', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Method
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Method'] == ('EE', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef'] == 'EF15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef'] == ('EF', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef'] == 'EF16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef'] == ('EF', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef'] == 'EF17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef'] == ('EF', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef'] == 'EF18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef'] == ('EF', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef'] == 'EF19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef'] == ('EF', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef'] == 'EF20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef'] == ('EF', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef'] == 'EF25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef'] == ('EF', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef'] == 'EF26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef'] == ('EF', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef'] == 'EF31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef'] == ('EF', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef'] == 'EF32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef'] == ('EF', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef'] == 'EF37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef'] == ('EF', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef'] == 'EF38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef'] == ('EF', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef'] == 'EF41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef'] == ('EF', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef'] == 'EF45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef'] == ('EF', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef'] == 'EF53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef'] == ('EF', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef'] == ('EF', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef_error
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_error'] == 'EG15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ('EG', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_error'] == 'EG16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_error'] == ('EG', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_error'] == 'EG17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_error'] == ('EG', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_error'] == 'EG18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_error'] == ('EG', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_error'] == 'EG19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_error'] == ('EG', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_error'] == 'EG20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_error'] == ('EG', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_error'] == 'EG25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_error'] == ('EG', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_error'] == 'EG26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_error'] == ('EG', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_error'] == 'EG31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_error'] == ('EG', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_error'] == 'EG32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_error'] == ('EG', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_error'] == 'EG37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ('EG', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_error'] == 'EG38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_error'] == ('EG', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_error'] == 'EG41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_error'] == ('EG', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_error'] == 'EG45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_error'] == ('EG', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_error'] == 'EG53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_error'] == ('EG', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ('EG', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef_sp
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == 'EH15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ('EH', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == 'EH16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == ('EH', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == 'EH17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == ('EH', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == 'EH18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == ('EH', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == 'EH19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == ('EH', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp'] == 'EH20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp'] == ('EH', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp'] == 'EH25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp'] == ('EH', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp'] == 'EH26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp'] == ('EH', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp'] == 'EH31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp'] == ('EH', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp'] == 'EH32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp'] == ('EH', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == 'EH37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ('EH', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == 'EH38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == ('EH', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == 'EH41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == ('EH', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == 'EH45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == ('EH', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == 'EH53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == ('EH', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ('EH', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef_sp_error
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == 'EI15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == 'EI16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == 'EI17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == 'EI18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == 'EI19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp_error'] == 'EI20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp_error'] == 'EI25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp_error'] == 'EI26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp_error'] == 'EI31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp_error'] == 'EI32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == 'EI37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == 'EI38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == 'EI41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == 'EI45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == 'EI53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 57, 57)
    # Band Characteristic Integrated_intensity_Relative
    # Band 1 Characteristic 1 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Relative'] == 'EJ15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Relative'] == ('EJ', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Relative'] == 'EJ16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Relative'] == ('EJ', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Relative'] == 'EJ17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Relative'] == ('EJ', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Relative'] == 'EJ18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Relative'] == ('EJ', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Relative'] == 'EJ19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Relative'] == ('EJ', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Relative'] == 'EJ20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Relative'] == ('EJ', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Relative'] == 'EJ25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Relative'] == ('EJ', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Relative'] == 'EJ26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Relative'] == ('EJ', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Relative'] == 'EJ31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Relative'] == ('EJ', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Relative'] == 'EJ32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Relative'] == ('EJ', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Relative'] == 'EJ37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Relative'] == ('EJ', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Relative'] == 'EJ38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Relative'] == ('EJ', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Relative'] == 'EJ41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Relative'] == ('EJ', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Relative'] == 'EJ45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Relative'] == ('EJ', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Relative'] == 'EJ53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Relative'] == ('EJ', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Relative
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Relative'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Relative'] == ('EJ', 57, 57)
    # Band Characteristic Integrated_intensity_Relative_error
    # Band 1 Characteristic 1 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Relative_error'] == 'EK15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Relative_error'] == ('EK', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Relative_error'] == 'EK16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Relative_error'] == ('EK', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Relative_error'] == 'EK17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Relative_error'] == ('EK', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Relative_error'] == 'EK18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Relative_error'] == ('EK', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Relative_error'] == 'EK19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Relative_error'] == ('EK', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Relative_error'] == 'EK20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Relative_error'] == ('EK', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Relative_error'] == 'EK25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Relative_error'] == ('EK', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Relative_error'] == 'EK26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Relative_error'] == ('EK', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Relative_error'] == 'EK31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Relative_error'] == ('EK', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Relative_error'] == 'EK32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Relative_error'] == ('EK', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Relative_error'] == 'EK37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Relative_error'] == ('EK', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Relative_error'] == 'EK38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Relative_error'] == ('EK', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Relative_error'] == 'EK41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Relative_error'] == ('EK', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Relative_error'] == 'EK45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Relative_error'] == ('EK', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Relative_error'] == 'EK53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Relative_error'] == ('EK', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Relative_error
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Relative_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Relative_error'] == ('EK', 57, 57)
    # Band Characteristic Integrated_intensity_Strength
    # Band 1 Characteristic 1 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Strength'] == 'ia'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Strength'] == ('EL', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Strength'] == 'ew'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Strength'] == ('EL', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Strength'] == 'vvw'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Strength'] == ('EL', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Strength'] == 'vw'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Strength'] == ('EL', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Strength'] == 'w'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Strength'] == ('EL', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Strength'] == 'm'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Strength'] == ('EL', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Strength'] == 's'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Strength'] == ('EL', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Strength'] == 'vs'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Strength'] == ('EL', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Strength'] == 'vvs'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Strength'] == ('EL', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Strength'] == 'es'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Strength'] == ('EL', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Strength'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Strength'] == ('EL', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Strength'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Strength'] == ('EL', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Strength'] == ('EL', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Strength'] == 'w'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Strength'] == ('EL', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Strength'] == ('EL', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Strength
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Strength'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Strength'] == ('EL', 57, 57)
    # Band Characteristic Integrated_intensity_Evaluation
    # Band 1 Characteristic 1 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Evaluation'] == ('EO', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Evaluation'] == ('EO', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Evaluation'] == ('EO', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Evaluation'] == ('EO', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Evaluation'] == ('EO', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Evaluation'] == ('EO', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Evaluation'] == ('EO', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Evaluation'] == ('EO', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Evaluation'] == ('EO', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Evaluation'] == ('EO', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Evaluation'] == ('EO', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Evaluation'] == ('EO', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Evaluation'] == ('EO', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Evaluation'] == ('EO', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Evaluation'] == ('EO', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Evaluation'] == ('EO', 57, 57)
    # Band Characteristic Integrated_intensity_Comment
    # Band 1 Characteristic 1 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Comment'] == 'EP15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Comment'] == ('EP', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Comment'] == 'EP16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Comment'] == ('EP', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Comment'] == 'EP17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Comment'] == ('EP', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Comment'] == 'EP18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Comment'] == ('EP', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Comment'] == 'EP19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Comment'] == ('EP', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Comment'] == 'EP20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Comment'] == ('EP', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Comment'] == 'EP25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Comment'] == ('EP', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Comment'] == 'EP26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Comment'] == ('EP', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Comment'] == 'EP31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Comment'] == ('EP', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Comment'] == 'EP32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Comment'] == ('EP', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Comment'] == 'EP37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Comment'] == ('EP', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Comment'] == 'EP38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Comment'] == ('EP', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Comment'] == 'EP41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Comment'] == ('EP', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Comment'] == 'EP45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Comment'] == ('EP', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Comment'] == 'EP53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Comment'] == ('EP', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Comment
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Comment'] == ('EP', 57, 57)
    # Band Characteristic Bandlist_flag
    # Band 1 Characteristic 1 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_1_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_1_Bandlist_flag'] == ('ES', 15, 15)
    # Band 1 Characteristic 2 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_2_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_2_Bandlist_flag'] == ('ES', 16, 16)
    # Band 1 Characteristic 3 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_3_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_3_Bandlist_flag'] == ('ES', 17, 17)
    # Band 1 Characteristic 4 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_4_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_4_Bandlist_flag'] == ('ES', 18, 18)
    # Band 1 Characteristic 5 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_5_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_5_Bandlist_flag'] == ('ES', 19, 19)
    # Band 1 Characteristic 6 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_6_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_6_Bandlist_flag'] == ('ES', 20, 20)
    # Band 1 Characteristic 7 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_7_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_7_Bandlist_flag'] == ('ES', 25, 25)
    # Band 1 Characteristic 8 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_8_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_8_Bandlist_flag'] == ('ES', 26, 26)
    # Band 1 Characteristic 9 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_9_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_9_Bandlist_flag'] == ('ES', 31, 31)
    # Band 1 Characteristic 10 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_10_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_10_Bandlist_flag'] == ('ES', 32, 32)
    # Band 2 Characteristic 1 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_1_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_2_Characteristic_1_Bandlist_flag'] == ('ES', 37, 37)
    # Band 2 Characteristic 2 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_2_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_2_Characteristic_2_Bandlist_flag'] == ('ES', 38, 38)
    # Band 2 Characteristic 3 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_3_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_2_Characteristic_3_Bandlist_flag'] == ('ES', 41, 41)
    # Band 2 Characteristic 4 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_4_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_2_Characteristic_4_Bandlist_flag'] == ('ES', 45, 45)
    # Band 2 Characteristic 5 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_5_Bandlist_flag'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Bandlist_flag'] == ('ES', 53, 53)
    # Band 3 Characteristic 1 Bandlist_flag
    assert verf_result[0]['B_3_Characteristic_1_Bandlist_flag'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Bandlist_flag'] == ('ES', 57, 57)
    # Abs
    verf_result = XMLGenerator_Bandlist_core.XLSX_reader("xlsx/read/band_characteristic_abs.xlsx", "ABS")
    # Band Characteristics qty
    # Band 1
    assert verf_result[0]['B_1_Characteristics_qty'] == 10
    # Band 2
    assert verf_result[0]['B_2_Characteristics_qty'] == 5
    # Band 3
    assert verf_result[0]['B_3_Characteristics_qty'] == 1
    # Band Characteristic Nb
    # Band 1 Characteristic 1 Nb
    assert verf_result[0]['B_1_Characteristic_1_Nb'] == '1'
    assert verf_result[1]['B_1_Characteristic_1_Nb'] == ('BP', 15, 15)
    # Band 1 Characteristic 2 Nb
    assert verf_result[0]['B_1_Characteristic_2_Nb'] == '2'
    assert verf_result[1]['B_1_Characteristic_2_Nb'] == ('BP', 16, 16)
    # Band 1 Characteristic 3 Nb
    assert verf_result[0]['B_1_Characteristic_3_Nb'] == '3'
    assert verf_result[1]['B_1_Characteristic_3_Nb'] == ('BP', 17, 17)
    # Band 1 Characteristic 4 Nb
    assert verf_result[0]['B_1_Characteristic_4_Nb'] == '4'
    assert verf_result[1]['B_1_Characteristic_4_Nb'] == ('BP', 18, 18)
    # Band 1 Characteristic 5 Nb
    assert verf_result[0]['B_1_Characteristic_5_Nb'] == '5'
    assert verf_result[1]['B_1_Characteristic_5_Nb'] == ('BP', 19, 19)
    # Band 1 Characteristic 6 Nb
    assert verf_result[0]['B_1_Characteristic_6_Nb'] == '6'
    assert verf_result[1]['B_1_Characteristic_6_Nb'] == ('BP', 20, 20)
    # Band 1 Characteristic 7 Nb
    assert verf_result[0]['B_1_Characteristic_7_Nb'] == '7'
    assert verf_result[1]['B_1_Characteristic_7_Nb'] == ('BP', 25, 25)
    # Band 1 Characteristic 8 Nb
    assert verf_result[0]['B_1_Characteristic_8_Nb'] == '8'
    assert verf_result[1]['B_1_Characteristic_8_Nb'] == ('BP', 26, 26)
    # Band 1 Characteristic 9 Nb
    assert verf_result[0]['B_1_Characteristic_9_Nb'] == '9'
    assert verf_result[1]['B_1_Characteristic_9_Nb'] == ('BP', 31, 31)
    # Band 1 Characteristic 10 Nb
    assert verf_result[0]['B_1_Characteristic_10_Nb'] == '10'
    assert verf_result[1]['B_1_Characteristic_10_Nb'] == ('BP', 32, 32)
    # Band 2 Characteristic 1 Nb
    assert verf_result[0]['B_2_Characteristic_1_Nb'] == '1'
    assert verf_result[1]['B_2_Characteristic_1_Nb'] == ('BP', 37, 37)
    # Band 2 Characteristic 2 Nb
    assert verf_result[0]['B_2_Characteristic_2_Nb'] == '2'
    assert verf_result[1]['B_2_Characteristic_2_Nb'] == ('BP', 38, 38)
    # Band 2 Characteristic 3 Nb
    assert verf_result[0]['B_2_Characteristic_3_Nb'] == '3'
    assert verf_result[1]['B_2_Characteristic_3_Nb'] == ('BP', 41, 41)
    # Band 2 Characteristic 4 Nb
    assert verf_result[0]['B_2_Characteristic_4_Nb'] == '4'
    assert verf_result[1]['B_2_Characteristic_4_Nb'] == ('BP', 45, 45)
    # Band 2 Characteristic 5 Nb
    assert verf_result[0]['B_2_Characteristic_5_Nb'] == '5'
    assert verf_result[1]['B_2_Characteristic_5_Nb'] == ('BP', 53, 53)
    # Band 3 Characteristic 1 Nb
    assert verf_result[0]['B_3_Characteristic_1_Nb'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Nb'] == ('BP', 57, 57)
    # Band Characteristic Composition
    # Band 1 Characteristic 1 Composition
    assert verf_result[0]['B_1_Characteristic_1_Composition'] == 'BQ15'
    assert verf_result[1]['B_1_Characteristic_1_Composition'] == ('BQ', 15, 15)
    # Band 1 Characteristic 2 Composition
    assert verf_result[0]['B_1_Characteristic_2_Composition'] == 'BQ16'
    assert verf_result[1]['B_1_Characteristic_2_Composition'] == ('BQ', 16, 16)
    # Band 1 Characteristic 3 Composition
    assert verf_result[0]['B_1_Characteristic_3_Composition'] == 'BQ17'
    assert verf_result[1]['B_1_Characteristic_3_Composition'] == ('BQ', 17, 17)
    # Band 1 Characteristic 4 Composition
    assert verf_result[0]['B_1_Characteristic_4_Composition'] == 'BQ18'
    assert verf_result[1]['B_1_Characteristic_4_Composition'] == ('BQ', 18, 18)
    # Band 1 Characteristic 5 Composition
    assert verf_result[0]['B_1_Characteristic_5_Composition'] == 'BQ19'
    assert verf_result[1]['B_1_Characteristic_5_Composition'] == ('BQ', 19, 19)
    # Band 1 Characteristic 6 Composition
    assert verf_result[0]['B_1_Characteristic_6_Composition'] == 'BQ20'
    assert verf_result[1]['B_1_Characteristic_6_Composition'] == ('BQ', 20, 20)
    # Band 1 Characteristic 7 Composition
    assert verf_result[0]['B_1_Characteristic_7_Composition'] == 'BQ25'
    assert verf_result[1]['B_1_Characteristic_7_Composition'] == ('BQ', 25, 25)
    # Band 1 Characteristic 8 Composition
    assert verf_result[0]['B_1_Characteristic_8_Composition'] == 'BQ26'
    assert verf_result[1]['B_1_Characteristic_8_Composition'] == ('BQ', 26, 26)
    # Band 1 Characteristic 9 Composition
    assert verf_result[0]['B_1_Characteristic_9_Composition'] == 'BQ31'
    assert verf_result[1]['B_1_Characteristic_9_Composition'] == ('BQ', 31, 31)
    # Band 1 Characteristic 10 Composition
    assert verf_result[0]['B_1_Characteristic_10_Composition'] == 'BQ32'
    assert verf_result[1]['B_1_Characteristic_10_Composition'] == ('BQ', 32, 32)
    # Band 2 Characteristic 1 Composition
    assert verf_result[0]['B_2_Characteristic_1_Composition'] == 'BQ37'
    assert verf_result[1]['B_2_Characteristic_1_Composition'] == ('BQ', 37, 37)
    # Band 2 Characteristic 2 Composition
    assert verf_result[0]['B_2_Characteristic_2_Composition'] == 'BQ38'
    assert verf_result[1]['B_2_Characteristic_2_Composition'] == ('BQ', 38, 38)
    # Band 2 Characteristic 3 Composition
    assert verf_result[0]['B_2_Characteristic_3_Composition'] == 'BQ41'
    assert verf_result[1]['B_2_Characteristic_3_Composition'] == ('BQ', 41, 41)
    # Band 2 Characteristic 4 Composition
    assert verf_result[0]['B_2_Characteristic_4_Composition'] == 'BQ45'
    assert verf_result[1]['B_2_Characteristic_4_Composition'] == ('BQ', 45, 45)
    # Band 2 Characteristic 5 Composition
    assert verf_result[0]['B_2_Characteristic_5_Composition'] == 'BQ53'
    assert verf_result[1]['B_2_Characteristic_5_Composition'] == ('BQ', 53, 53)
    # Band 3 Characteristic 1 Composition
    assert verf_result[0]['B_3_Characteristic_1_Composition'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Composition'] == ('BQ', 57, 57)
    # Band Characteristic Texture
    # Band 1 Characteristic 1 Texture
    assert verf_result[0]['B_1_Characteristic_1_Texture'] == 'BR15'
    assert verf_result[1]['B_1_Characteristic_1_Texture'] == ('BR', 15, 15)
    # Band 1 Characteristic 2 Texture
    assert verf_result[0]['B_1_Characteristic_2_Texture'] == 'BR16'
    assert verf_result[1]['B_1_Characteristic_2_Texture'] == ('BR', 16, 16)
    # Band 1 Characteristic 3 Texture
    assert verf_result[0]['B_1_Characteristic_3_Texture'] == 'BR17'
    assert verf_result[1]['B_1_Characteristic_3_Texture'] == ('BR', 17, 17)
    # Band 1 Characteristic 4 Texture
    assert verf_result[0]['B_1_Characteristic_4_Texture'] == 'BR18'
    assert verf_result[1]['B_1_Characteristic_4_Texture'] == ('BR', 18, 18)
    # Band 1 Characteristic 5 Texture
    assert verf_result[0]['B_1_Characteristic_5_Texture'] == 'BR19'
    assert verf_result[1]['B_1_Characteristic_5_Texture'] == ('BR', 19, 19)
    # Band 1 Characteristic 6 Texture
    assert verf_result[0]['B_1_Characteristic_6_Texture'] == 'BR20'
    assert verf_result[1]['B_1_Characteristic_6_Texture'] == ('BR', 20, 20)
    # Band 1 Characteristic 7 Texture
    assert verf_result[0]['B_1_Characteristic_7_Texture'] == 'BR25'
    assert verf_result[1]['B_1_Characteristic_7_Texture'] == ('BR', 25, 25)
    # Band 1 Characteristic 8 Texture
    assert verf_result[0]['B_1_Characteristic_8_Texture'] == 'BR26'
    assert verf_result[1]['B_1_Characteristic_8_Texture'] == ('BR', 26, 26)
    # Band 1 Characteristic 9 Texture
    assert verf_result[0]['B_1_Characteristic_9_Texture'] == 'BR31'
    assert verf_result[1]['B_1_Characteristic_9_Texture'] == ('BR', 31, 31)
    # Band 1 Characteristic 10 Texture
    assert verf_result[0]['B_1_Characteristic_10_Texture'] == 'BR32'
    assert verf_result[1]['B_1_Characteristic_10_Texture'] == ('BR', 32, 32)
    # Band 2 Characteristic 1 Texture
    assert verf_result[0]['B_2_Characteristic_1_Texture'] == 'BR37'
    assert verf_result[1]['B_2_Characteristic_1_Texture'] == ('BR', 37, 37)
    # Band 2 Characteristic 2 Texture
    assert verf_result[0]['B_2_Characteristic_2_Texture'] == 'BR38'
    assert verf_result[1]['B_2_Characteristic_2_Texture'] == ('BR', 38, 38)
    # Band 2 Characteristic 3 Texture
    assert verf_result[0]['B_2_Characteristic_3_Texture'] == 'BR41'
    assert verf_result[1]['B_2_Characteristic_3_Texture'] == ('BR', 41, 41)
    # Band 2 Characteristic 4 Texture
    assert verf_result[0]['B_2_Characteristic_4_Texture'] == 'BR45'
    assert verf_result[1]['B_2_Characteristic_4_Texture'] == ('BR', 45, 45)
    # Band 2 Characteristic 5 Texture
    assert verf_result[0]['B_2_Characteristic_5_Texture'] == 'BR53'
    assert verf_result[1]['B_2_Characteristic_5_Texture'] == ('BR', 53, 53)
    # Band 3 Characteristic 1 Texture
    assert verf_result[0]['B_3_Characteristic_1_Texture'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Texture'] == ('BR', 57, 57)
    # Band Characteristic T_Unit
    # Band 1 Characteristic 1 T_Unit
    assert verf_result[0]['B_1_Characteristic_1_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_1_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 2 T_Unit
    assert verf_result[0]['B_1_Characteristic_2_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_2_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 3 T_Unit
    assert verf_result[0]['B_1_Characteristic_3_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_3_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 4 T_Unit
    assert verf_result[0]['B_1_Characteristic_4_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_4_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 5 T_Unit
    assert verf_result[0]['B_1_Characteristic_5_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_5_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 6 T_Unit
    assert verf_result[0]['B_1_Characteristic_6_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_6_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 7 T_Unit
    assert verf_result[0]['B_1_Characteristic_7_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_7_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 8 T_Unit
    assert verf_result[0]['B_1_Characteristic_8_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_8_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 9 T_Unit
    assert verf_result[0]['B_1_Characteristic_9_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_9_T_Unit'] == ('BW', 8, 8)
    # Band 1 Characteristic 10 T_Unit
    assert verf_result[0]['B_1_Characteristic_10_T_Unit'] == 'K'
    assert verf_result[1]['B_1_Characteristic_10_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 1 T_Unit
    assert verf_result[0]['B_2_Characteristic_1_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_1_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 2 T_Unit
    assert verf_result[0]['B_2_Characteristic_2_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_2_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 3 T_Unit
    assert verf_result[0]['B_2_Characteristic_3_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_3_T_Unit'] == ('BW', 8, 8)
    # Band 2 Characteristic 4 T_Unit
    assert verf_result[0]['B_2_Characteristic_4_T_Unit'] == 'K'
    assert verf_result[1]['B_2_Characteristic_4_T_Unit'] == ('BW', 8, 8)
    # Band 3 Characteristic 1 T_Unit
    assert verf_result[0]['B_3_Characteristic_1_T_Unit'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Unit'] == ('BW', 8, 8)
    # Band Characteristic T_Value
    # Band 1 Characteristic 1 T_Value
    assert verf_result[0]['B_1_Characteristic_1_T_Value'] == 'BT15'
    assert verf_result[1]['B_1_Characteristic_1_T_Value'] == ('BT', 15, 15)
    # Band 1 Characteristic 2 T_Value
    assert verf_result[0]['B_1_Characteristic_2_T_Value'] == 'BT16'
    assert verf_result[1]['B_1_Characteristic_2_T_Value'] == ('BT', 16, 16)
    # Band 1 Characteristic 3 T_Value
    assert verf_result[0]['B_1_Characteristic_3_T_Value'] == 'BT17'
    assert verf_result[1]['B_1_Characteristic_3_T_Value'] == ('BT', 17, 17)
    # Band 1 Characteristic 4 T_Value
    assert verf_result[0]['B_1_Characteristic_4_T_Value'] == 'BT18'
    assert verf_result[1]['B_1_Characteristic_4_T_Value'] == ('BT', 18, 18)
    # Band 1 Characteristic 5 T_Value
    assert verf_result[0]['B_1_Characteristic_5_T_Value'] == 'BT19'
    assert verf_result[1]['B_1_Characteristic_5_T_Value'] == ('BT', 19, 19)
    # Band 1 Characteristic 6 T_Value
    assert verf_result[0]['B_1_Characteristic_6_T_Value'] == 'BT20'
    assert verf_result[1]['B_1_Characteristic_6_T_Value'] == ('BT', 20, 20)
    # Band 1 Characteristic 7 T_Value
    assert verf_result[0]['B_1_Characteristic_7_T_Value'] == 'BT25'
    assert verf_result[1]['B_1_Characteristic_7_T_Value'] == ('BT', 25, 25)
    # Band 1 Characteristic 8 T_Value
    assert verf_result[0]['B_1_Characteristic_8_T_Value'] == 'BT26'
    assert verf_result[1]['B_1_Characteristic_8_T_Value'] == ('BT', 26, 26)
    # Band 1 Characteristic 9 T_Value
    assert verf_result[0]['B_1_Characteristic_9_T_Value'] == 'BT31'
    assert verf_result[1]['B_1_Characteristic_9_T_Value'] == ('BT', 31, 31)
    # Band 1 Characteristic 10 T_Value
    assert verf_result[0]['B_1_Characteristic_10_T_Value'] == 'BT32'
    assert verf_result[1]['B_1_Characteristic_10_T_Value'] == ('BT', 32, 32)
    # Band 2 Characteristic 1 T_Value
    assert verf_result[0]['B_2_Characteristic_1_T_Value'] == 'BT37'
    assert verf_result[1]['B_2_Characteristic_1_T_Value'] == ('BT', 37, 37)
    # Band 2 Characteristic 2 T_Value
    assert verf_result[0]['B_2_Characteristic_2_T_Value'] == 'BT38'
    assert verf_result[1]['B_2_Characteristic_2_T_Value'] == ('BT', 38, 38)
    # Band 2 Characteristic 3 T_Value
    assert verf_result[0]['B_2_Characteristic_3_T_Value'] == 'BT41'
    assert verf_result[1]['B_2_Characteristic_3_T_Value'] == ('BT', 41, 41)
    # Band 2 Characteristic 4 T_Value
    assert verf_result[0]['B_2_Characteristic_4_T_Value'] == 'BT45'
    assert verf_result[1]['B_2_Characteristic_4_T_Value'] == ('BT', 45, 45)
    # Band 2 Characteristic 5 T_Value
    assert verf_result[0]['B_2_Characteristic_5_T_Value'] == 'BT53'
    assert verf_result[1]['B_2_Characteristic_5_T_Value'] == ('BT', 53, 53)
    # Band 3 Characteristic 1 T_Value
    assert verf_result[0]['B_3_Characteristic_1_T_Value'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Value'] == ('BT', 57, 57)
    # Band Characteristic T_Error
    # Band 1 Characteristic 1 T_Error
    assert verf_result[0]['B_1_Characteristic_1_T_Error'] == 'BU15'
    assert verf_result[1]['B_1_Characteristic_1_T_Error'] == ('BU', 15, 15)
    # Band 1 Characteristic 2 T_Error
    assert verf_result[0]['B_1_Characteristic_2_T_Error'] == 'BU16'
    assert verf_result[1]['B_1_Characteristic_2_T_Error'] == ('BU', 16, 16)
    # Band 1 Characteristic 3 T_Error
    assert verf_result[0]['B_1_Characteristic_3_T_Error'] == 'BU17'
    assert verf_result[1]['B_1_Characteristic_3_T_Error'] == ('BU', 17, 17)
    # Band 1 Characteristic 4 T_Error
    assert verf_result[0]['B_1_Characteristic_4_T_Error'] == 'BU18'
    assert verf_result[1]['B_1_Characteristic_4_T_Error'] == ('BU', 18, 18)
    # Band 1 Characteristic 5 T_Error
    assert verf_result[0]['B_1_Characteristic_5_T_Error'] == 'BU19'
    assert verf_result[1]['B_1_Characteristic_5_T_Error'] == ('BU', 19, 19)
    # Band 1 Characteristic 6 T_Error
    assert verf_result[0]['B_1_Characteristic_6_T_Error'] == 'BU20'
    assert verf_result[1]['B_1_Characteristic_6_T_Error'] == ('BU', 20, 20)
    # Band 1 Characteristic 7 T_Error
    assert verf_result[0]['B_1_Characteristic_7_T_Error'] == 'BU25'
    assert verf_result[1]['B_1_Characteristic_7_T_Error'] == ('BU', 25, 25)
    # Band 1 Characteristic 8 T_Error
    assert verf_result[0]['B_1_Characteristic_8_T_Error'] == 'BU26'
    assert verf_result[1]['B_1_Characteristic_8_T_Error'] == ('BU', 26, 26)
    # Band 1 Characteristic 9 T_Error
    assert verf_result[0]['B_1_Characteristic_9_T_Error'] == 'BU31'
    assert verf_result[1]['B_1_Characteristic_9_T_Error'] == ('BU', 31, 31)
    # Band 1 Characteristic 10 T_Error
    assert verf_result[0]['B_1_Characteristic_10_T_Error'] == 'BU32'
    assert verf_result[1]['B_1_Characteristic_10_T_Error'] == ('BU', 32, 32)
    # Band 2 Characteristic 1 T_Error
    assert verf_result[0]['B_2_Characteristic_1_T_Error'] == 'BU37'
    assert verf_result[1]['B_2_Characteristic_1_T_Error'] == ('BU', 37, 37)
    # Band 2 Characteristic 2 T_Error
    assert verf_result[0]['B_2_Characteristic_2_T_Error'] == 'BU38'
    assert verf_result[1]['B_2_Characteristic_2_T_Error'] == ('BU', 38, 38)
    # Band 2 Characteristic 3 T_Error
    assert verf_result[0]['B_2_Characteristic_3_T_Error'] == 'BU41'
    assert verf_result[1]['B_2_Characteristic_3_T_Error'] == ('BU', 41, 41)
    # Band 2 Characteristic 4 T_Error
    assert verf_result[0]['B_2_Characteristic_4_T_Error'] == 'BU45'
    assert verf_result[1]['B_2_Characteristic_4_T_Error'] == ('BU', 45, 45)
    # Band 2 Characteristic 5 T_Error
    assert verf_result[0]['B_2_Characteristic_5_T_Error'] == 'BU53'
    assert verf_result[1]['B_2_Characteristic_5_T_Error'] == ('BU', 53, 53)
    # Band 3 Characteristic 1 T_Error
    assert verf_result[0]['B_3_Characteristic_1_T_Error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Error'] == ('BU', 57, 57)
    # Band Characteristic T_Formation
    # Band 1 Characteristic 1 T_Formation
    assert verf_result[0]['B_1_Characteristic_1_T_Formation'] == 'BV15'
    assert verf_result[1]['B_1_Characteristic_1_T_Formation'] == ('BV', 15, 15)
    # Band 1 Characteristic 2 T_Formation
    assert verf_result[0]['B_1_Characteristic_2_T_Formation'] == 'BV16'
    assert verf_result[1]['B_1_Characteristic_2_T_Formation'] == ('BV', 16, 16)
    # Band 1 Characteristic 3 T_Formation
    assert verf_result[0]['B_1_Characteristic_3_T_Formation'] == 'BV17'
    assert verf_result[1]['B_1_Characteristic_3_T_Formation'] == ('BV', 17, 17)
    # Band 1 Characteristic 4 T_Formation
    assert verf_result[0]['B_1_Characteristic_4_T_Formation'] == 'BV18'
    assert verf_result[1]['B_1_Characteristic_4_T_Formation'] == ('BV', 18, 18)
    # Band 1 Characteristic 5 T_Formation
    assert verf_result[0]['B_1_Characteristic_5_T_Formation'] == 'BV19'
    assert verf_result[1]['B_1_Characteristic_5_T_Formation'] == ('BV', 19, 19)
    # Band 1 Characteristic 6 T_Formation
    assert verf_result[0]['B_1_Characteristic_6_T_Formation'] == 'BV20'
    assert verf_result[1]['B_1_Characteristic_6_T_Formation'] == ('BV', 20, 20)
    # Band 1 Characteristic 7 T_Formation
    assert verf_result[0]['B_1_Characteristic_7_T_Formation'] == 'BV25'
    assert verf_result[1]['B_1_Characteristic_7_T_Formation'] == ('BV', 25, 25)
    # Band 1 Characteristic 8 T_Formation
    assert verf_result[0]['B_1_Characteristic_8_T_Formation'] == 'BV26'
    assert verf_result[1]['B_1_Characteristic_8_T_Formation'] == ('BV', 26, 26)
    # Band 1 Characteristic 9 T_Formation
    assert verf_result[0]['B_1_Characteristic_9_T_Formation'] == 'BV31'
    assert verf_result[1]['B_1_Characteristic_9_T_Formation'] == ('BV', 31, 31)
    # Band 1 Characteristic 10 T_Formation
    assert verf_result[0]['B_1_Characteristic_10_T_Formation'] == 'BV32'
    assert verf_result[1]['B_1_Characteristic_10_T_Formation'] == ('BV', 32, 32)
    # Band 2 Characteristic 1 T_Formation
    assert verf_result[0]['B_2_Characteristic_1_T_Formation'] == 'BV37'
    assert verf_result[1]['B_2_Characteristic_1_T_Formation'] == ('BV', 37, 37)
    # Band 2 Characteristic 2 T_Formation
    assert verf_result[0]['B_2_Characteristic_2_T_Formation'] == 'BV38'
    assert verf_result[1]['B_2_Characteristic_2_T_Formation'] == ('BV', 38, 38)
    # Band 2 Characteristic 3 T_Formation
    assert verf_result[0]['B_2_Characteristic_3_T_Formation'] == 'BV41'
    assert verf_result[1]['B_2_Characteristic_3_T_Formation'] == ('BV', 41, 41)
    # Band 2 Characteristic 4 T_Formation
    assert verf_result[0]['B_2_Characteristic_4_T_Formation'] == 'BV45'
    assert verf_result[1]['B_2_Characteristic_4_T_Formation'] == ('BV', 45, 45)
    # Band 2 Characteristic 5 T_Formation
    assert verf_result[0]['B_2_Characteristic_5_T_Formation'] == 'BV53'
    assert verf_result[1]['B_2_Characteristic_5_T_Formation'] == ('BV', 53, 53)
    # Band 3 Characteristic 1 T_Formation
    assert verf_result[0]['B_3_Characteristic_1_T_Formation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Formation'] == ('BV', 57, 57)
    # Band Characteristic T_Max
    # Band 1 Characteristic 1 T_Max
    assert verf_result[0]['B_1_Characteristic_1_T_Max'] == 'BW15'
    assert verf_result[1]['B_1_Characteristic_1_T_Max'] == ('BW', 15, 15)
    # Band 1 Characteristic 2 T_Max
    assert verf_result[0]['B_1_Characteristic_2_T_Max'] == 'BW16'
    assert verf_result[1]['B_1_Characteristic_2_T_Max'] == ('BW', 16, 16)
    # Band 1 Characteristic 3 T_Max
    assert verf_result[0]['B_1_Characteristic_3_T_Max'] == 'BW17'
    assert verf_result[1]['B_1_Characteristic_3_T_Max'] == ('BW', 17, 17)
    # Band 1 Characteristic 4 T_Max
    assert verf_result[0]['B_1_Characteristic_4_T_Max'] == 'BW18'
    assert verf_result[1]['B_1_Characteristic_4_T_Max'] == ('BW', 18, 18)
    # Band 1 Characteristic 5 T_Max
    assert verf_result[0]['B_1_Characteristic_5_T_Max'] == 'BW19'
    assert verf_result[1]['B_1_Characteristic_5_T_Max'] == ('BW', 19, 19)
    # Band 1 Characteristic 6 T_Max
    assert verf_result[0]['B_1_Characteristic_6_T_Max'] == 'BW20'
    assert verf_result[1]['B_1_Characteristic_6_T_Max'] == ('BW', 20, 20)
    # Band 1 Characteristic 7 T_Max
    assert verf_result[0]['B_1_Characteristic_7_T_Max'] == 'BW25'
    assert verf_result[1]['B_1_Characteristic_7_T_Max'] == ('BW', 25, 25)
    # Band 1 Characteristic 8 T_Max
    assert verf_result[0]['B_1_Characteristic_8_T_Max'] == 'BW26'
    assert verf_result[1]['B_1_Characteristic_8_T_Max'] == ('BW', 26, 26)
    # Band 1 Characteristic 9 T_Max
    assert verf_result[0]['B_1_Characteristic_9_T_Max'] == 'BW31'
    assert verf_result[1]['B_1_Characteristic_9_T_Max'] == ('BW', 31, 31)
    # Band 1 Characteristic 10 T_Max
    assert verf_result[0]['B_1_Characteristic_10_T_Max'] == 'BW32'
    assert verf_result[1]['B_1_Characteristic_10_T_Max'] == ('BW', 32, 32)
    # Band 2 Characteristic 1 T_Max
    assert verf_result[0]['B_2_Characteristic_1_T_Max'] == 'BW37'
    assert verf_result[1]['B_2_Characteristic_1_T_Max'] == ('BW', 37, 37)
    # Band 2 Characteristic 2 T_Max
    assert verf_result[0]['B_2_Characteristic_2_T_Max'] == 'BW38'
    assert verf_result[1]['B_2_Characteristic_2_T_Max'] == ('BW', 38, 38)
    # Band 2 Characteristic 3 T_Max
    assert verf_result[0]['B_2_Characteristic_3_T_Max'] == 'BW41'
    assert verf_result[1]['B_2_Characteristic_3_T_Max'] == ('BW', 41, 41)
    # Band 2 Characteristic 4 T_Max
    assert verf_result[0]['B_2_Characteristic_4_T_Max'] == 'BW45'
    assert verf_result[1]['B_2_Characteristic_4_T_Max'] == ('BW', 45, 45)
    # Band 2 Characteristic 5 T_Max
    assert verf_result[0]['B_2_Characteristic_5_T_Max'] == 'BW53'
    assert verf_result[1]['B_2_Characteristic_5_T_Max'] == ('BW', 53, 53)
    # Band 3 Characteristic 1 T_Max
    assert verf_result[0]['B_3_Characteristic_1_T_Max'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Max'] == ('BW', 57, 57)
    # Band Characteristic T_Comment
    # Band 1 Characteristic 1 T_Comment
    assert verf_result[0]['B_1_Characteristic_1_T_Comment'] == 'BX15'
    assert verf_result[1]['B_1_Characteristic_1_T_Comment'] == ('BX', 15, 15)
    # Band 1 Characteristic 2 T_Comment
    assert verf_result[0]['B_1_Characteristic_2_T_Comment'] == 'BX16'
    assert verf_result[1]['B_1_Characteristic_2_T_Comment'] == ('BX', 16, 16)
    # Band 1 Characteristic 3 T_Comment
    assert verf_result[0]['B_1_Characteristic_3_T_Comment'] == 'BX17'
    assert verf_result[1]['B_1_Characteristic_3_T_Comment'] == ('BX', 17, 17)
    # Band 1 Characteristic 4 T_Comment
    assert verf_result[0]['B_1_Characteristic_4_T_Comment'] == 'BX18'
    assert verf_result[1]['B_1_Characteristic_4_T_Comment'] == ('BX', 18, 18)
    # Band 1 Characteristic 5 T_Comment
    assert verf_result[0]['B_1_Characteristic_5_T_Comment'] == 'BX19'
    assert verf_result[1]['B_1_Characteristic_5_T_Comment'] == ('BX', 19, 19)
    # Band 1 Characteristic 6 T_Comment
    assert verf_result[0]['B_1_Characteristic_6_T_Comment'] == 'BX20'
    assert verf_result[1]['B_1_Characteristic_6_T_Comment'] == ('BX', 20, 20)
    # Band 1 Characteristic 7 T_Comment
    assert verf_result[0]['B_1_Characteristic_7_T_Comment'] == 'BX25'
    assert verf_result[1]['B_1_Characteristic_7_T_Comment'] == ('BX', 25, 25)
    # Band 1 Characteristic 8 T_Comment
    assert verf_result[0]['B_1_Characteristic_8_T_Comment'] == 'BX26'
    assert verf_result[1]['B_1_Characteristic_8_T_Comment'] == ('BX', 26, 26)
    # Band 1 Characteristic 9 T_Comment
    assert verf_result[0]['B_1_Characteristic_9_T_Comment'] == 'BX31'
    assert verf_result[1]['B_1_Characteristic_9_T_Comment'] == ('BX', 31, 31)
    # Band 1 Characteristic 10 T_Comment
    assert verf_result[0]['B_1_Characteristic_10_T_Comment'] == 'BX32'
    assert verf_result[1]['B_1_Characteristic_10_T_Comment'] == ('BX', 32, 32)
    # Band 2 Characteristic 1 T_Comment
    assert verf_result[0]['B_2_Characteristic_1_T_Comment'] == 'BX37'
    assert verf_result[1]['B_2_Characteristic_1_T_Comment'] == ('BX', 37, 37)
    # Band 2 Characteristic 2 T_Comment
    assert verf_result[0]['B_2_Characteristic_2_T_Comment'] == 'BX38'
    assert verf_result[1]['B_2_Characteristic_2_T_Comment'] == ('BX', 38, 38)
    # Band 2 Characteristic 3 T_Comment
    assert verf_result[0]['B_2_Characteristic_3_T_Comment'] == 'BX41'
    assert verf_result[1]['B_2_Characteristic_3_T_Comment'] == ('BX', 41, 41)
    # Band 2 Characteristic 4 T_Comment
    assert verf_result[0]['B_2_Characteristic_4_T_Comment'] == 'BX45'
    assert verf_result[1]['B_2_Characteristic_4_T_Comment'] == ('BX', 45, 45)
    # Band 2 Characteristic 5 T_Comment
    assert verf_result[0]['B_2_Characteristic_5_T_Comment'] == 'BX53'
    assert verf_result[1]['B_2_Characteristic_5_T_Comment'] == ('BX', 53, 53)
    # Band 3 Characteristic 1 T_Comment
    assert verf_result[0]['B_3_Characteristic_1_T_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_T_Comment'] == ('BX', 57, 57)
    # Band Characteristic P_Unit
    # Band 1 Characteristic 1 P_Unit
    assert verf_result[0]['B_1_Characteristic_1_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_1_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 2 P_Unit
    assert verf_result[0]['B_1_Characteristic_2_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_2_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 3 P_Unit
    assert verf_result[0]['B_1_Characteristic_3_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_3_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 4 P_Unit
    assert verf_result[0]['B_1_Characteristic_4_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_4_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 5 P_Unit
    assert verf_result[0]['B_1_Characteristic_5_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_5_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 6 P_Unit
    assert verf_result[0]['B_1_Characteristic_6_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_6_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 7 P_Unit
    assert verf_result[0]['B_1_Characteristic_7_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_7_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 8 P_Unit
    assert verf_result[0]['B_1_Characteristic_8_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_8_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 9 P_Unit
    assert verf_result[0]['B_1_Characteristic_9_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_9_P_Unit'] == ('CC', 8, 8)
    # Band 1 Characteristic 10 P_Unit
    assert verf_result[0]['B_1_Characteristic_10_P_Unit'] == 'bar'
    assert verf_result[1]['B_1_Characteristic_10_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 1 P_Unit
    assert verf_result[0]['B_2_Characteristic_1_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_1_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 2 P_Unit
    assert verf_result[0]['B_2_Characteristic_2_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_2_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 3 P_Unit
    assert verf_result[0]['B_2_Characteristic_3_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_3_P_Unit'] == ('CC', 8, 8)
    # Band 2 Characteristic 4 P_Unit
    assert verf_result[0]['B_2_Characteristic_4_P_Unit'] == 'bar'
    assert verf_result[1]['B_2_Characteristic_4_P_Unit'] == ('CC', 8, 8)
    # Band 3 Characteristic 1 P_Unit
    assert verf_result[0]['B_3_Characteristic_1_P_Unit'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Unit'] == ('CC', 8, 8)
    # Band Characteristic P_Value
    # Band 1 Characteristic 1 P_Value
    assert verf_result[0]['B_1_Characteristic_1_P_Value'] == 'BZ15'
    assert verf_result[1]['B_1_Characteristic_1_P_Value'] == ('BZ', 15, 15)
    # Band 1 Characteristic 2 P_Value
    assert verf_result[0]['B_1_Characteristic_2_P_Value'] == 'BZ16'
    assert verf_result[1]['B_1_Characteristic_2_P_Value'] == ('BZ', 16, 16)
    # Band 1 Characteristic 3 P_Value
    assert verf_result[0]['B_1_Characteristic_3_P_Value'] == 'BZ17'
    assert verf_result[1]['B_1_Characteristic_3_P_Value'] == ('BZ', 17, 17)
    # Band 1 Characteristic 4 P_Value
    assert verf_result[0]['B_1_Characteristic_4_P_Value'] == 'BZ18'
    assert verf_result[1]['B_1_Characteristic_4_P_Value'] == ('BZ', 18, 18)
    # Band 1 Characteristic 5 P_Value
    assert verf_result[0]['B_1_Characteristic_5_P_Value'] == 'BZ19'
    assert verf_result[1]['B_1_Characteristic_5_P_Value'] == ('BZ', 19, 19)
    # Band 1 Characteristic 6 P_Value
    assert verf_result[0]['B_1_Characteristic_6_P_Value'] == 'BZ20'
    assert verf_result[1]['B_1_Characteristic_6_P_Value'] == ('BZ', 20, 20)
    # Band 1 Characteristic 7 P_Value
    assert verf_result[0]['B_1_Characteristic_7_P_Value'] == 'BZ25'
    assert verf_result[1]['B_1_Characteristic_7_P_Value'] == ('BZ', 25, 25)
    # Band 1 Characteristic 8 P_Value
    assert verf_result[0]['B_1_Characteristic_8_P_Value'] == 'BZ26'
    assert verf_result[1]['B_1_Characteristic_8_P_Value'] == ('BZ', 26, 26)
    # Band 1 Characteristic 9 P_Value
    assert verf_result[0]['B_1_Characteristic_9_P_Value'] == 'BZ31'
    assert verf_result[1]['B_1_Characteristic_9_P_Value'] == ('BZ', 31, 31)
    # Band 1 Characteristic 10 P_Value
    assert verf_result[0]['B_1_Characteristic_10_P_Value'] == 'BZ32'
    assert verf_result[1]['B_1_Characteristic_10_P_Value'] == ('BZ', 32, 32)
    # Band 2 Characteristic 1 P_Value
    assert verf_result[0]['B_2_Characteristic_1_P_Value'] == 'BZ37'
    assert verf_result[1]['B_2_Characteristic_1_P_Value'] == ('BZ', 37, 37)
    # Band 2 Characteristic 2 P_Value
    assert verf_result[0]['B_2_Characteristic_2_P_Value'] == 'BZ38'
    assert verf_result[1]['B_2_Characteristic_2_P_Value'] == ('BZ', 38, 38)
    # Band 2 Characteristic 3 P_Value
    assert verf_result[0]['B_2_Characteristic_3_P_Value'] == 'BZ41'
    assert verf_result[1]['B_2_Characteristic_3_P_Value'] == ('BZ', 41, 41)
    # Band 2 Characteristic 4 P_Value
    assert verf_result[0]['B_2_Characteristic_4_P_Value'] == 'BZ45'
    assert verf_result[1]['B_2_Characteristic_4_P_Value'] == ('BZ', 45, 45)
    # Band 2 Characteristic 5 P_Value
    assert verf_result[0]['B_2_Characteristic_5_P_Value'] == 'BZ53'
    assert verf_result[1]['B_2_Characteristic_5_P_Value'] == ('BZ', 53, 53)
    # Band 3 Characteristic 1 P_Value
    assert verf_result[0]['B_3_Characteristic_1_P_Value'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Value'] == ('BZ', 57, 57)
    # Band Characteristic P_Error
    # Band 1 Characteristic 1 P_Error
    assert verf_result[0]['B_1_Characteristic_1_P_Error'] == 'CA15'
    assert verf_result[1]['B_1_Characteristic_1_P_Error'] == ('CA', 15, 15)
    # Band 1 Characteristic 2 P_Error
    assert verf_result[0]['B_1_Characteristic_2_P_Error'] == 'CA16'
    assert verf_result[1]['B_1_Characteristic_2_P_Error'] == ('CA', 16, 16)
    # Band 1 Characteristic 3 P_Error
    assert verf_result[0]['B_1_Characteristic_3_P_Error'] == 'CA17'
    assert verf_result[1]['B_1_Characteristic_3_P_Error'] == ('CA', 17, 17)
    # Band 1 Characteristic 4 P_Error
    assert verf_result[0]['B_1_Characteristic_4_P_Error'] == 'CA18'
    assert verf_result[1]['B_1_Characteristic_4_P_Error'] == ('CA', 18, 18)
    # Band 1 Characteristic 5 P_Error
    assert verf_result[0]['B_1_Characteristic_5_P_Error'] == 'CA19'
    assert verf_result[1]['B_1_Characteristic_5_P_Error'] == ('CA', 19, 19)
    # Band 1 Characteristic 6 P_Error
    assert verf_result[0]['B_1_Characteristic_6_P_Error'] == 'CA20'
    assert verf_result[1]['B_1_Characteristic_6_P_Error'] == ('CA', 20, 20)
    # Band 1 Characteristic 7 P_Error
    assert verf_result[0]['B_1_Characteristic_7_P_Error'] == 'CA25'
    assert verf_result[1]['B_1_Characteristic_7_P_Error'] == ('CA', 25, 25)
    # Band 1 Characteristic 8 P_Error
    assert verf_result[0]['B_1_Characteristic_8_P_Error'] == 'CA26'
    assert verf_result[1]['B_1_Characteristic_8_P_Error'] == ('CA', 26, 26)
    # Band 1 Characteristic 9 P_Error
    assert verf_result[0]['B_1_Characteristic_9_P_Error'] == 'CA31'
    assert verf_result[1]['B_1_Characteristic_9_P_Error'] == ('CA', 31, 31)
    # Band 1 Characteristic 10 P_Error
    assert verf_result[0]['B_1_Characteristic_10_P_Error'] == 'CA32'
    assert verf_result[1]['B_1_Characteristic_10_P_Error'] == ('CA', 32, 32)
    # Band 2 Characteristic 1 P_Error
    assert verf_result[0]['B_2_Characteristic_1_P_Error'] == 'CA37'
    assert verf_result[1]['B_2_Characteristic_1_P_Error'] == ('CA', 37, 37)
    # Band 2 Characteristic 2 P_Error
    assert verf_result[0]['B_2_Characteristic_2_P_Error'] == 'CA38'
    assert verf_result[1]['B_2_Characteristic_2_P_Error'] == ('CA', 38, 38)
    # Band 2 Characteristic 3 P_Error
    assert verf_result[0]['B_2_Characteristic_3_P_Error'] == 'CA41'
    assert verf_result[1]['B_2_Characteristic_3_P_Error'] == ('CA', 41, 41)
    # Band 2 Characteristic 4 P_Error
    assert verf_result[0]['B_2_Characteristic_4_P_Error'] == 'CA45'
    assert verf_result[1]['B_2_Characteristic_4_P_Error'] == ('CA', 45, 45)
    # Band 2 Characteristic 5 P_Error
    assert verf_result[0]['B_2_Characteristic_5_P_Error'] == 'CA53'
    assert verf_result[1]['B_2_Characteristic_5_P_Error'] == ('CA', 53, 53)
    # Band 3 Characteristic 1 P_Error
    assert verf_result[0]['B_3_Characteristic_1_P_Error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Error'] == ('CA', 57, 57)
    # Band Characteristic P_Formation
    # Band 1 Characteristic 1 P_Formation
    assert verf_result[0]['B_1_Characteristic_1_P_Formation'] == 'CB15'
    assert verf_result[1]['B_1_Characteristic_1_P_Formation'] == ('CB', 15, 15)
    # Band 1 Characteristic 2 P_Formation
    assert verf_result[0]['B_1_Characteristic_2_P_Formation'] == 'CB16'
    assert verf_result[1]['B_1_Characteristic_2_P_Formation'] == ('CB', 16, 16)
    # Band 1 Characteristic 3 P_Formation
    assert verf_result[0]['B_1_Characteristic_3_P_Formation'] == 'CB17'
    assert verf_result[1]['B_1_Characteristic_3_P_Formation'] == ('CB', 17, 17)
    # Band 1 Characteristic 4 P_Formation
    assert verf_result[0]['B_1_Characteristic_4_P_Formation'] == 'CB18'
    assert verf_result[1]['B_1_Characteristic_4_P_Formation'] == ('CB', 18, 18)
    # Band 1 Characteristic 5 P_Formation
    assert verf_result[0]['B_1_Characteristic_5_P_Formation'] == 'CB19'
    assert verf_result[1]['B_1_Characteristic_5_P_Formation'] == ('CB', 19, 19)
    # Band 1 Characteristic 6 P_Formation
    assert verf_result[0]['B_1_Characteristic_6_P_Formation'] == 'CB20'
    assert verf_result[1]['B_1_Characteristic_6_P_Formation'] == ('CB', 20, 20)
    # Band 1 Characteristic 7 P_Formation
    assert verf_result[0]['B_1_Characteristic_7_P_Formation'] == 'CB25'
    assert verf_result[1]['B_1_Characteristic_7_P_Formation'] == ('CB', 25, 25)
    # Band 1 Characteristic 8 P_Formation
    assert verf_result[0]['B_1_Characteristic_8_P_Formation'] == 'CB26'
    assert verf_result[1]['B_1_Characteristic_8_P_Formation'] == ('CB', 26, 26)
    # Band 1 Characteristic 9 P_Formation
    assert verf_result[0]['B_1_Characteristic_9_P_Formation'] == 'CB31'
    assert verf_result[1]['B_1_Characteristic_9_P_Formation'] == ('CB', 31, 31)
    # Band 1 Characteristic 10 P_Formation
    assert verf_result[0]['B_1_Characteristic_10_P_Formation'] == 'CB32'
    assert verf_result[1]['B_1_Characteristic_10_P_Formation'] == ('CB', 32, 32)
    # Band 2 Characteristic 1 P_Formation
    assert verf_result[0]['B_2_Characteristic_1_P_Formation'] == 'CB37'
    assert verf_result[1]['B_2_Characteristic_1_P_Formation'] == ('CB', 37, 37)
    # Band 2 Characteristic 2 P_Formation
    assert verf_result[0]['B_2_Characteristic_2_P_Formation'] == 'CB38'
    assert verf_result[1]['B_2_Characteristic_2_P_Formation'] == ('CB', 38, 38)
    # Band 2 Characteristic 3 P_Formation
    assert verf_result[0]['B_2_Characteristic_3_P_Formation'] == 'CB41'
    assert verf_result[1]['B_2_Characteristic_3_P_Formation'] == ('CB', 41, 41)
    # Band 2 Characteristic 4 P_Formation
    assert verf_result[0]['B_2_Characteristic_4_P_Formation'] == 'CB45'
    assert verf_result[1]['B_2_Characteristic_4_P_Formation'] == ('CB', 45, 45)
    # Band 2 Characteristic 5 P_Formation
    assert verf_result[0]['B_2_Characteristic_5_P_Formation'] == 'CB53'
    assert verf_result[1]['B_2_Characteristic_5_P_Formation'] == ('CB', 53, 53)
    # Band 3 Characteristic 1 P_Formation
    assert verf_result[0]['B_3_Characteristic_1_P_Formation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Formation'] == ('CB', 57, 57)
    # Band Characteristic P_Max
    # Band 1 Characteristic 1 P_Max
    assert verf_result[0]['B_1_Characteristic_1_P_Max'] == 'CC15'
    assert verf_result[1]['B_1_Characteristic_1_P_Max'] == ('CC', 15, 15)
    # Band 1 Characteristic 2 P_Max
    assert verf_result[0]['B_1_Characteristic_2_P_Max'] == 'CC16'
    assert verf_result[1]['B_1_Characteristic_2_P_Max'] == ('CC', 16, 16)
    # Band 1 Characteristic 3 P_Max
    assert verf_result[0]['B_1_Characteristic_3_P_Max'] == 'CC17'
    assert verf_result[1]['B_1_Characteristic_3_P_Max'] == ('CC', 17, 17)
    # Band 1 Characteristic 4 P_Max
    assert verf_result[0]['B_1_Characteristic_4_P_Max'] == 'CC18'
    assert verf_result[1]['B_1_Characteristic_4_P_Max'] == ('CC', 18, 18)
    # Band 1 Characteristic 5 P_Max
    assert verf_result[0]['B_1_Characteristic_5_P_Max'] == 'CC19'
    assert verf_result[1]['B_1_Characteristic_5_P_Max'] == ('CC', 19, 19)
    # Band 1 Characteristic 6 P_Max
    assert verf_result[0]['B_1_Characteristic_6_P_Max'] == 'CC20'
    assert verf_result[1]['B_1_Characteristic_6_P_Max'] == ('CC', 20, 20)
    # Band 1 Characteristic 7 P_Max
    assert verf_result[0]['B_1_Characteristic_7_P_Max'] == 'CC25'
    assert verf_result[1]['B_1_Characteristic_7_P_Max'] == ('CC', 25, 25)
    # Band 1 Characteristic 8 P_Max
    assert verf_result[0]['B_1_Characteristic_8_P_Max'] == 'CC26'
    assert verf_result[1]['B_1_Characteristic_8_P_Max'] == ('CC', 26, 26)
    # Band 1 Characteristic 9 P_Max
    assert verf_result[0]['B_1_Characteristic_9_P_Max'] == 'CC31'
    assert verf_result[1]['B_1_Characteristic_9_P_Max'] == ('CC', 31, 31)
    # Band 1 Characteristic 10 P_Max
    assert verf_result[0]['B_1_Characteristic_10_P_Max'] == 'CC32'
    assert verf_result[1]['B_1_Characteristic_10_P_Max'] == ('CC', 32, 32)
    # Band 2 Characteristic 1 P_Max
    assert verf_result[0]['B_2_Characteristic_1_P_Max'] == 'CC37'
    assert verf_result[1]['B_2_Characteristic_1_P_Max'] == ('CC', 37, 37)
    # Band 2 Characteristic 2 P_Max
    assert verf_result[0]['B_2_Characteristic_2_P_Max'] == 'CC38'
    assert verf_result[1]['B_2_Characteristic_2_P_Max'] == ('CC', 38, 38)
    # Band 2 Characteristic 3 P_Max
    assert verf_result[0]['B_2_Characteristic_3_P_Max'] == 'CC41'
    assert verf_result[1]['B_2_Characteristic_3_P_Max'] == ('CC', 41, 41)
    # Band 2 Characteristic 4 P_Max
    assert verf_result[0]['B_2_Characteristic_4_P_Max'] == 'CC45'
    assert verf_result[1]['B_2_Characteristic_4_P_Max'] == ('CC', 45, 45)
    # Band 2 Characteristic 5 P_Max
    assert verf_result[0]['B_2_Characteristic_5_P_Max'] == 'CC53'
    assert verf_result[1]['B_2_Characteristic_5_P_Max'] == ('CC', 53, 53)
    # Band 3 Characteristic 1 P_Max
    assert verf_result[0]['B_3_Characteristic_1_P_Max'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Max'] == ('CC', 57, 57)
    # Band Characteristic P_Stress_type
    # Band 1 Characteristic 1 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_1_P_Stress_type'] == 'normal uniaxial tension'
    assert verf_result[1]['B_1_Characteristic_1_P_Stress_type'] == ('CD', 15, 15)
    # Band 1 Characteristic 2 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_2_P_Stress_type'] == 'normal uniaxial compression'
    assert verf_result[1]['B_1_Characteristic_2_P_Stress_type'] == ('CD', 16, 16)
    # Band 1 Characteristic 3 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_3_P_Stress_type'] == 'simple shear'
    assert verf_result[1]['B_1_Characteristic_3_P_Stress_type'] == ('CD', 17, 17)
    # Band 1 Characteristic 4 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_4_P_Stress_type'] == 'normal biaxial tension'
    assert verf_result[1]['B_1_Characteristic_4_P_Stress_type'] == ('CD', 18, 18)
    # Band 1 Characteristic 5 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_5_P_Stress_type'] == 'normal biaxial compression'
    assert verf_result[1]['B_1_Characteristic_5_P_Stress_type'] == ('CD', 19, 19)
    # Band 1 Characteristic 6 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_6_P_Stress_type'] == 'cylindrical normal tension'
    assert verf_result[1]['B_1_Characteristic_6_P_Stress_type'] == ('CD', 20, 20)
    # Band 1 Characteristic 7 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_7_P_Stress_type'] == ''
    assert verf_result[1]['B_1_Characteristic_7_P_Stress_type'] == ('CD', 25, 25)
    # Band 1 Characteristic 8 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_8_P_Stress_type'] == 'cylindrical normal compression'
    assert verf_result[1]['B_1_Characteristic_8_P_Stress_type'] == ('CD', 26, 26)
    # Band 1 Characteristic 9 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_9_P_Stress_type'] == 'isotropic normal tension'
    assert verf_result[1]['B_1_Characteristic_9_P_Stress_type'] == ('CD', 31, 31)
    # Band 1 Characteristic 10 P_Stress_type
    assert verf_result[0]['B_1_Characteristic_10_P_Stress_type'] == 'isotropic normal compression'
    assert verf_result[1]['B_1_Characteristic_10_P_Stress_type'] == ('CD', 32, 32)
    # Band 2 Characteristic 1 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_1_P_Stress_type'] == 'combined biaxial'
    assert verf_result[1]['B_2_Characteristic_1_P_Stress_type'] == ('CD', 37, 37)
    # Band 2 Characteristic 2 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_2_P_Stress_type'] == 'combined triaxial'
    assert verf_result[1]['B_2_Characteristic_2_P_Stress_type'] == ('CD', 38, 38)
    # Band 2 Characteristic 3 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_3_P_Stress_type'] == 'other'
    assert verf_result[1]['B_2_Characteristic_3_P_Stress_type'] == ('CD', 41, 41)
    # Band 2 Characteristic 4 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_4_P_Stress_type'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_4_P_Stress_type'] == ('CD', 45, 45)
    # Band 2 Characteristic 5 P_Stress_type
    assert verf_result[0]['B_2_Characteristic_5_P_Stress_type'] == ''
    assert verf_result[1]['B_2_Characteristic_5_P_Stress_type'] == ('CD', 53, 53)
    # Band 3 Characteristic 1 P_Stress_type
    assert verf_result[0]['B_3_Characteristic_1_P_Stress_type'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Stress_type'] == ('CD', 57, 57)
    # Band Characteristic P_Comment
    # Band 1 Characteristic 1 P_Comment
    assert verf_result[0]['B_1_Characteristic_1_P_Comment'] == 'CE15'
    assert verf_result[1]['B_1_Characteristic_1_P_Comment'] == ('CE', 15, 15)
    # Band 1 Characteristic 2 P_Comment
    assert verf_result[0]['B_1_Characteristic_2_P_Comment'] == 'CE16'
    assert verf_result[1]['B_1_Characteristic_2_P_Comment'] == ('CE', 16, 16)
    # Band 1 Characteristic 3 P_Comment
    assert verf_result[0]['B_1_Characteristic_3_P_Comment'] == 'CE17'
    assert verf_result[1]['B_1_Characteristic_3_P_Comment'] == ('CE', 17, 17)
    # Band 1 Characteristic 4 P_Comment
    assert verf_result[0]['B_1_Characteristic_4_P_Comment'] == 'CE18'
    assert verf_result[1]['B_1_Characteristic_4_P_Comment'] == ('CE', 18, 18)
    # Band 1 Characteristic 5 P_Comment
    assert verf_result[0]['B_1_Characteristic_5_P_Comment'] == 'CE19'
    assert verf_result[1]['B_1_Characteristic_5_P_Comment'] == ('CE', 19, 19)
    # Band 1 Characteristic 6 P_Comment
    assert verf_result[0]['B_1_Characteristic_6_P_Comment'] == 'CE20'
    assert verf_result[1]['B_1_Characteristic_6_P_Comment'] == ('CE', 20, 20)
    # Band 1 Characteristic 7 P_Comment
    assert verf_result[0]['B_1_Characteristic_7_P_Comment'] == 'CE25'
    assert verf_result[1]['B_1_Characteristic_7_P_Comment'] == ('CE', 25, 25)
    # Band 1 Characteristic 8 P_Comment
    assert verf_result[0]['B_1_Characteristic_8_P_Comment'] == 'CE26'
    assert verf_result[1]['B_1_Characteristic_8_P_Comment'] == ('CE', 26, 26)
    # Band 1 Characteristic 9 P_Comment
    assert verf_result[0]['B_1_Characteristic_9_P_Comment'] == 'CE31'
    assert verf_result[1]['B_1_Characteristic_9_P_Comment'] == ('CE', 31, 31)
    # Band 1 Characteristic 10 P_Comment
    assert verf_result[0]['B_1_Characteristic_10_P_Comment'] == 'CE32'
    assert verf_result[1]['B_1_Characteristic_10_P_Comment'] == ('CE', 32, 32)
    # Band 2 Characteristic 1 P_Comment
    assert verf_result[0]['B_2_Characteristic_1_P_Comment'] == 'CE37'
    assert verf_result[1]['B_2_Characteristic_1_P_Comment'] == ('CE', 37, 37)
    # Band 2 Characteristic 2 P_Comment
    assert verf_result[0]['B_2_Characteristic_2_P_Comment'] == 'CE38'
    assert verf_result[1]['B_2_Characteristic_2_P_Comment'] == ('CE', 38, 38)
    # Band 2 Characteristic 3 P_Comment
    assert verf_result[0]['B_2_Characteristic_3_P_Comment'] == 'CE41'
    assert verf_result[1]['B_2_Characteristic_3_P_Comment'] == ('CE', 41, 41)
    # Band 2 Characteristic 4 P_Comment
    assert verf_result[0]['B_2_Characteristic_4_P_Comment'] == 'CE45'
    assert verf_result[1]['B_2_Characteristic_4_P_Comment'] == ('CE', 45, 45)
    # Band 2 Characteristic 5 P_Comment
    assert verf_result[0]['B_2_Characteristic_5_P_Comment'] == 'CE53'
    assert verf_result[1]['B_2_Characteristic_5_P_Comment'] == ('CE', 53, 53)
    # Band 3 Characteristic 1 P_Comment
    assert verf_result[0]['B_3_Characteristic_1_P_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_P_Comment'] == ('CE', 57, 57)
    # Band Characteristic Laser_excitation_Wavelength_Unit
    # Band 1 Characteristic 1 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_1_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 2 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_2_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_2_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 3 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_3_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_3_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 4 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_4_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_4_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 5 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_5_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_5_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 6 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_6_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_6_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 7 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_7_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_7_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 8 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_8_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_8_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 9 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_9_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_9_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 1 Characteristic 10 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_1_Characteristic_10_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_1_Characteristic_10_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 1 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_1_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 2 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_2_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_2_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 3 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_3_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_3_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 2 Characteristic 4 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_2_Characteristic_4_Laser_excitation_Wavelength_Unit'] == 'nm'
    assert verf_result[1]['B_2_Characteristic_4_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band 3 Characteristic 1 Laser_excitation_Wavelength_Unit
    assert verf_result[0]['B_3_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Laser_excitation_Wavelength_Unit'] == ('CH', 7, 7)
    # Band Characteristic Laser_excitation_Wavelength
    # Band 1 Characteristic 1 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_1_Laser_excitation_Wavelength'] == 'CG15'
    assert verf_result[1]['B_1_Characteristic_1_Laser_excitation_Wavelength'] == ('CG', 15, 15)
    # Band 1 Characteristic 2 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_2_Laser_excitation_Wavelength'] == 'CG16'
    assert verf_result[1]['B_1_Characteristic_2_Laser_excitation_Wavelength'] == ('CG', 16, 16)
    # Band 1 Characteristic 3 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_3_Laser_excitation_Wavelength'] == 'CG17'
    assert verf_result[1]['B_1_Characteristic_3_Laser_excitation_Wavelength'] == ('CG', 17, 17)
    # Band 1 Characteristic 4 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_4_Laser_excitation_Wavelength'] == 'CG18'
    assert verf_result[1]['B_1_Characteristic_4_Laser_excitation_Wavelength'] == ('CG', 18, 18)
    # Band 1 Characteristic 5 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_5_Laser_excitation_Wavelength'] == 'CG19'
    assert verf_result[1]['B_1_Characteristic_5_Laser_excitation_Wavelength'] == ('CG', 19, 19)
    # Band 1 Characteristic 6 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_6_Laser_excitation_Wavelength'] == 'CG20'
    assert verf_result[1]['B_1_Characteristic_6_Laser_excitation_Wavelength'] == ('CG', 20, 20)
    # Band 1 Characteristic 7 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_7_Laser_excitation_Wavelength'] == 'CG25'
    assert verf_result[1]['B_1_Characteristic_7_Laser_excitation_Wavelength'] == ('CG', 25, 25)
    # Band 1 Characteristic 8 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_8_Laser_excitation_Wavelength'] == 'CG26'
    assert verf_result[1]['B_1_Characteristic_8_Laser_excitation_Wavelength'] == ('CG', 26, 26)
    # Band 1 Characteristic 9 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_9_Laser_excitation_Wavelength'] == 'CG31'
    assert verf_result[1]['B_1_Characteristic_9_Laser_excitation_Wavelength'] == ('CG', 31, 31)
    # Band 1 Characteristic 10 Laser_excitation_Wavelength
    assert verf_result[0]['B_1_Characteristic_10_Laser_excitation_Wavelength'] == 'CG32'
    assert verf_result[1]['B_1_Characteristic_10_Laser_excitation_Wavelength'] == ('CG', 32, 32)
    # Band 2 Characteristic 1 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_1_Laser_excitation_Wavelength'] == 'CG37'
    assert verf_result[1]['B_2_Characteristic_1_Laser_excitation_Wavelength'] == ('CG', 37, 37)
    # Band 2 Characteristic 2 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_2_Laser_excitation_Wavelength'] == 'CG38'
    assert verf_result[1]['B_2_Characteristic_2_Laser_excitation_Wavelength'] == ('CG', 38, 38)
    # Band 2 Characteristic 3 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_3_Laser_excitation_Wavelength'] == 'CG41'
    assert verf_result[1]['B_2_Characteristic_3_Laser_excitation_Wavelength'] == ('CG', 41, 41)
    # Band 2 Characteristic 4 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_4_Laser_excitation_Wavelength'] == 'CG45'
    assert verf_result[1]['B_2_Characteristic_4_Laser_excitation_Wavelength'] == ('CG', 45, 45)
    # Band 2 Characteristic 5 Laser_excitation_Wavelength
    assert verf_result[0]['B_2_Characteristic_5_Laser_excitation_Wavelength'] == 'CG53'
    assert verf_result[1]['B_2_Characteristic_5_Laser_excitation_Wavelength'] == ('CG', 53, 53)
    # Band 3 Characteristic 1 Laser_excitation_Wavelength
    assert verf_result[0]['B_3_Characteristic_1_Laser_excitation_Wavelength'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Laser_excitation_Wavelength'] == ('CG', 57, 57)
    # Band Characteristic Sample_Orient_mode
    # Band 1 Characteristic 1 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_1_Sample_Orient_mode'] == 'oriented'
    assert verf_result[1]['B_1_Characteristic_1_Sample_Orient_mode'] == ('CH', 15, 15)
    # Band 1 Characteristic 2 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_2_Sample_Orient_mode'] == 'unoriented'
    assert verf_result[1]['B_1_Characteristic_2_Sample_Orient_mode'] == ('CH', 16, 16)
    # Band 1 Characteristic 3 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_3_Sample_Orient_mode'] == 'random'
    assert verf_result[1]['B_1_Characteristic_3_Sample_Orient_mode'] == ('CH', 17, 17)
    # Band 1 Characteristic 4 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_4_Sample_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_4_Sample_Orient_mode'] == ('CH', 18, 18)
    # Band 1 Characteristic 5 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_5_Sample_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_5_Sample_Orient_mode'] == ('CH', 19, 19)
    # Band 1 Characteristic 6 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_6_Sample_Orient_mode'] == 'oriented'
    assert verf_result[1]['B_1_Characteristic_6_Sample_Orient_mode'] == ('CH', 20, 20)
    # Band 1 Characteristic 7 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_7_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_7_Sample_Orient_mode'] == ('CH', 25, 25)
    # Band 1 Characteristic 8 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_8_Sample_Orient_mode'] == 'unoriented'
    assert verf_result[1]['B_1_Characteristic_8_Sample_Orient_mode'] == ('CH', 26, 26)
    # Band 1 Characteristic 9 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_9_Sample_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_9_Sample_Orient_mode'] == ('CH', 31, 31)
    # Band 1 Characteristic 10 Sample_Orient_mode
    assert verf_result[0]['B_1_Characteristic_10_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Sample_Orient_mode'] == ('CH', 32, 32)
    # Band 2 Characteristic 1 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_1_Sample_Orient_mode'] == 'unoriented'
    assert verf_result[1]['B_2_Characteristic_1_Sample_Orient_mode'] == ('CH', 37, 37)
    # Band 2 Characteristic 2 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_2_Sample_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Sample_Orient_mode'] == ('CH', 38, 38)
    # Band 2 Characteristic 3 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_3_Sample_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Sample_Orient_mode'] == ('CH', 41, 41)
    # Band 2 Characteristic 4 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_4_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Sample_Orient_mode'] == ('CH', 45, 45)
    # Band 2 Characteristic 5 Sample_Orient_mode
    assert verf_result[0]['B_2_Characteristic_5_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Sample_Orient_mode'] == ('CH', 53, 53)
    # Band 3 Characteristic 1 Sample_Orient_mode
    assert verf_result[0]['B_3_Characteristic_1_Sample_Orient_mode'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Sample_Orient_mode'] == ('CH', 57, 57)
    # Band Characteristic Sample_Orient
    # Band 1 Characteristic 1 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_1_Sample_Orient'] == 'CI15'
    assert verf_result[1]['B_1_Characteristic_1_Sample_Orient'] == ('CI', 15, 15)
    # Band 1 Characteristic 2 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_2_Sample_Orient'] == 'CI16'
    assert verf_result[1]['B_1_Characteristic_2_Sample_Orient'] == ('CI', 16, 16)
    # Band 1 Characteristic 3 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_3_Sample_Orient'] == 'CI17'
    assert verf_result[1]['B_1_Characteristic_3_Sample_Orient'] == ('CI', 17, 17)
    # Band 1 Characteristic 4 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_4_Sample_Orient'] == 'CI18'
    assert verf_result[1]['B_1_Characteristic_4_Sample_Orient'] == ('CI', 18, 18)
    # Band 1 Characteristic 5 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_5_Sample_Orient'] == 'CI19'
    assert verf_result[1]['B_1_Characteristic_5_Sample_Orient'] == ('CI', 19, 19)
    # Band 1 Characteristic 6 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_6_Sample_Orient'] == 'CI20'
    assert verf_result[1]['B_1_Characteristic_6_Sample_Orient'] == ('CI', 20, 20)
    # Band 1 Characteristic 7 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_7_Sample_Orient'] == 'CI25'
    assert verf_result[1]['B_1_Characteristic_7_Sample_Orient'] == ('CI', 25, 25)
    # Band 1 Characteristic 8 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_8_Sample_Orient'] == 'CI26'
    assert verf_result[1]['B_1_Characteristic_8_Sample_Orient'] == ('CI', 26, 26)
    # Band 1 Characteristic 9 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_9_Sample_Orient'] == 'CI31'
    assert verf_result[1]['B_1_Characteristic_9_Sample_Orient'] == ('CI', 31, 31)
    # Band 1 Characteristic 10 Sample_Orient
    assert verf_result[0]['B_1_Characteristic_10_Sample_Orient'] == 'CI32'
    assert verf_result[1]['B_1_Characteristic_10_Sample_Orient'] == ('CI', 32, 32)
    # Band 2 Characteristic 1 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_1_Sample_Orient'] == 'CI37'
    assert verf_result[1]['B_2_Characteristic_1_Sample_Orient'] == ('CI', 37, 37)
    # Band 2 Characteristic 2 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_2_Sample_Orient'] == 'CI38'
    assert verf_result[1]['B_2_Characteristic_2_Sample_Orient'] == ('CI', 38, 38)
    # Band 2 Characteristic 3 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_3_Sample_Orient'] == 'CI41'
    assert verf_result[1]['B_2_Characteristic_3_Sample_Orient'] == ('CI', 41, 41)
    # Band 2 Characteristic 4 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_4_Sample_Orient'] == 'CI45'
    assert verf_result[1]['B_2_Characteristic_4_Sample_Orient'] == ('CI', 45, 45)
    # Band 2 Characteristic 5 Sample_Orient
    assert verf_result[0]['B_2_Characteristic_5_Sample_Orient'] == 'CI53'
    assert verf_result[1]['B_2_Characteristic_5_Sample_Orient'] == ('CI', 53, 53)
    # Band 3 Characteristic 1 Sample_Orient
    assert verf_result[0]['B_3_Characteristic_1_Sample_Orient'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Sample_Orient'] == ('CI', 57, 57)
    # Band Characteristic Polarization_Orient_mode
    # Band 1 Characteristic 1 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_1_Polarization_Orient_mode'] == 'depolarized'
    assert verf_result[1]['B_1_Characteristic_1_Polarization_Orient_mode'] == ('CJ', 15, 15)
    # Band 1 Characteristic 2 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_2_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_1_Characteristic_2_Polarization_Orient_mode'] == ('CJ', 16, 16)
    # Band 1 Characteristic 3 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_3_Polarization_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_3_Polarization_Orient_mode'] == ('CJ', 17, 17)
    # Band 1 Characteristic 4 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_4_Polarization_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_4_Polarization_Orient_mode'] == ('CJ', 18, 18)
    # Band 1 Characteristic 5 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_5_Polarization_Orient_mode'] == 'depolarized'
    assert verf_result[1]['B_1_Characteristic_5_Polarization_Orient_mode'] == ('CJ', 19, 19)
    # Band 1 Characteristic 6 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_6_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_1_Characteristic_6_Polarization_Orient_mode'] == ('CJ', 20, 20)
    # Band 1 Characteristic 7 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_7_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_7_Polarization_Orient_mode'] == ('CJ', 25, 25)
    # Band 1 Characteristic 8 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_8_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_1_Characteristic_8_Polarization_Orient_mode'] == ('CJ', 26, 26)
    # Band 1 Characteristic 9 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_9_Polarization_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_9_Polarization_Orient_mode'] == ('CJ', 31, 31)
    # Band 1 Characteristic 10 Polarization_Orient_mode
    assert verf_result[0]['B_1_Characteristic_10_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Polarization_Orient_mode'] == ('CJ', 32, 32)
    # Band 2 Characteristic 1 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_1_Polarization_Orient_mode'] == 'polarized'
    assert verf_result[1]['B_2_Characteristic_1_Polarization_Orient_mode'] == ('CJ', 37, 37)
    # Band 2 Characteristic 2 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_2_Polarization_Orient_mode'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Polarization_Orient_mode'] == ('CJ', 38, 38)
    # Band 2 Characteristic 3 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_3_Polarization_Orient_mode'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Polarization_Orient_mode'] == ('CJ', 41, 41)
    # Band 2 Characteristic 4 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_4_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Polarization_Orient_mode'] == ('CJ', 45, 45)
    # Band 2 Characteristic 5 Polarization_Orient_mode
    assert verf_result[0]['B_2_Characteristic_5_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Polarization_Orient_mode'] == ('CJ', 53, 53)
    # Band 3 Characteristic 1 Polarization_Orient_mode
    assert verf_result[0]['B_3_Characteristic_1_Polarization_Orient_mode'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Polarization_Orient_mode'] == ('CJ', 57, 57)
    # Band Characteristic Polarization_Orient
    # Band 1 Characteristic 1 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_1_Polarization_Orient'] == 'CK15'
    assert verf_result[1]['B_1_Characteristic_1_Polarization_Orient'] == ('CK', 15, 15)
    # Band 1 Characteristic 2 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_2_Polarization_Orient'] == 'CK16'
    assert verf_result[1]['B_1_Characteristic_2_Polarization_Orient'] == ('CK', 16, 16)
    # Band 1 Characteristic 3 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_3_Polarization_Orient'] == 'CK17'
    assert verf_result[1]['B_1_Characteristic_3_Polarization_Orient'] == ('CK', 17, 17)
    # Band 1 Characteristic 4 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_4_Polarization_Orient'] == 'CK18'
    assert verf_result[1]['B_1_Characteristic_4_Polarization_Orient'] == ('CK', 18, 18)
    # Band 1 Characteristic 5 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_5_Polarization_Orient'] == 'CK19'
    assert verf_result[1]['B_1_Characteristic_5_Polarization_Orient'] == ('CK', 19, 19)
    # Band 1 Characteristic 6 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_6_Polarization_Orient'] == 'CK20'
    assert verf_result[1]['B_1_Characteristic_6_Polarization_Orient'] == ('CK', 20, 20)
    # Band 1 Characteristic 7 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_7_Polarization_Orient'] == 'CK25'
    assert verf_result[1]['B_1_Characteristic_7_Polarization_Orient'] == ('CK', 25, 25)
    # Band 1 Characteristic 8 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_8_Polarization_Orient'] == 'CK26'
    assert verf_result[1]['B_1_Characteristic_8_Polarization_Orient'] == ('CK', 26, 26)
    # Band 1 Characteristic 9 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_9_Polarization_Orient'] == 'CK31'
    assert verf_result[1]['B_1_Characteristic_9_Polarization_Orient'] == ('CK', 31, 31)
    # Band 1 Characteristic 10 Polarization_Orient
    assert verf_result[0]['B_1_Characteristic_10_Polarization_Orient'] == 'CK32'
    assert verf_result[1]['B_1_Characteristic_10_Polarization_Orient'] == ('CK', 32, 32)
    # Band 2 Characteristic 1 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_1_Polarization_Orient'] == 'CK37'
    assert verf_result[1]['B_2_Characteristic_1_Polarization_Orient'] == ('CK', 37, 37)
    # Band 2 Characteristic 2 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_2_Polarization_Orient'] == 'CK38'
    assert verf_result[1]['B_2_Characteristic_2_Polarization_Orient'] == ('CK', 38, 38)
    # Band 2 Characteristic 3 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_3_Polarization_Orient'] == 'CK41'
    assert verf_result[1]['B_2_Characteristic_3_Polarization_Orient'] == ('CK', 41, 41)
    # Band 2 Characteristic 4 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_4_Polarization_Orient'] == 'CK45'
    assert verf_result[1]['B_2_Characteristic_4_Polarization_Orient'] == ('CK', 45, 45)
    # Band 2 Characteristic 5 Polarization_Orient
    assert verf_result[0]['B_2_Characteristic_5_Polarization_Orient'] == 'CK53'
    assert verf_result[1]['B_2_Characteristic_5_Polarization_Orient'] == ('CK', 53, 53)
    # Band 3 Characteristic 1 Polarization_Orient
    assert verf_result[0]['B_3_Characteristic_1_Polarization_Orient'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Polarization_Orient'] == ('CK', 57, 57)
    # Band Characteristic Excitation_Comment
    # Band 1 Characteristic 1 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_1_Excitation_Comment'] == 'CL15'
    assert verf_result[1]['B_1_Characteristic_1_Excitation_Comment'] == ('CL', 15, 15)
    # Band 1 Characteristic 2 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_2_Excitation_Comment'] == 'CL16'
    assert verf_result[1]['B_1_Characteristic_2_Excitation_Comment'] == ('CL', 16, 16)
    # Band 1 Characteristic 3 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_3_Excitation_Comment'] == 'CL17'
    assert verf_result[1]['B_1_Characteristic_3_Excitation_Comment'] == ('CL', 17, 17)
    # Band 1 Characteristic 4 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_4_Excitation_Comment'] == 'CL18'
    assert verf_result[1]['B_1_Characteristic_4_Excitation_Comment'] == ('CL', 18, 18)
    # Band 1 Characteristic 5 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_5_Excitation_Comment'] == 'CL19'
    assert verf_result[1]['B_1_Characteristic_5_Excitation_Comment'] == ('CL', 19, 19)
    # Band 1 Characteristic 6 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_6_Excitation_Comment'] == 'CL20'
    assert verf_result[1]['B_1_Characteristic_6_Excitation_Comment'] == ('CL', 20, 20)
    # Band 1 Characteristic 7 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_7_Excitation_Comment'] == 'CL25'
    assert verf_result[1]['B_1_Characteristic_7_Excitation_Comment'] == ('CL', 25, 25)
    # Band 1 Characteristic 8 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_8_Excitation_Comment'] == 'CL26'
    assert verf_result[1]['B_1_Characteristic_8_Excitation_Comment'] == ('CL', 26, 26)
    # Band 1 Characteristic 9 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_9_Excitation_Comment'] == 'CL31'
    assert verf_result[1]['B_1_Characteristic_9_Excitation_Comment'] == ('CL', 31, 31)
    # Band 1 Characteristic 10 Excitation_Comment
    assert verf_result[0]['B_1_Characteristic_10_Excitation_Comment'] == 'CL32'
    assert verf_result[1]['B_1_Characteristic_10_Excitation_Comment'] == ('CL', 32, 32)
    # Band 2 Characteristic 1 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_1_Excitation_Comment'] == 'CL37'
    assert verf_result[1]['B_2_Characteristic_1_Excitation_Comment'] == ('CL', 37, 37)
    # Band 2 Characteristic 2 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_2_Excitation_Comment'] == 'CL38'
    assert verf_result[1]['B_2_Characteristic_2_Excitation_Comment'] == ('CL', 38, 38)
    # Band 2 Characteristic 3 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_3_Excitation_Comment'] == 'CL41'
    assert verf_result[1]['B_2_Characteristic_3_Excitation_Comment'] == ('CL', 41, 41)
    # Band 2 Characteristic 4 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_4_Excitation_Comment'] == 'CL45'
    assert verf_result[1]['B_2_Characteristic_4_Excitation_Comment'] == ('CL', 45, 45)
    # Band 2 Characteristic 5 Excitation_Comment
    assert verf_result[0]['B_2_Characteristic_5_Excitation_Comment'] == 'CL53'
    assert verf_result[1]['B_2_Characteristic_5_Excitation_Comment'] == ('CL', 53, 53)
    # Band 3 Characteristic 1 Excitation_Comment
    assert verf_result[0]['B_3_Characteristic_1_Excitation_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Excitation_Comment'] == ('CL', 57, 57)
    # Band Characteristic Methods_qty
    # Band 1 Characteristic 1 Methods_qty
    assert verf_result[0]['B_1_Characteristic_1_Methods_qty'] == 1
    # Band 1 Characteristic 2 Methods_qty
    assert verf_result[0]['B_1_Characteristic_2_Methods_qty'] == 1
    # Band 1 Characteristic 3 Methods_qty
    assert verf_result[0]['B_1_Characteristic_3_Methods_qty'] == 1
    # Band 1 Characteristic 4 Methods_qty
    assert verf_result[0]['B_1_Characteristic_4_Methods_qty'] == 1
    # Band 1 Characteristic 5 Methods_qty
    assert verf_result[0]['B_1_Characteristic_5_Methods_qty'] == 1
    # Band 1 Characteristic 6 Methods_qty
    assert verf_result[0]['B_1_Characteristic_6_Methods_qty'] == 3
    # Band 1 Characteristic 7 Methods_qty
    assert verf_result[0]['B_1_Characteristic_7_Methods_qty'] == 1
    # Band 1 Characteristic 8 Methods_qty
    assert verf_result[0]['B_1_Characteristic_8_Methods_qty'] == 1
    # Band 1 Characteristic 9 Methods_qty
    assert verf_result[0]['B_1_Characteristic_9_Methods_qty'] == 1
    # Band 1 Characteristic 10 Methods_qty
    assert verf_result[0]['B_1_Characteristic_10_Methods_qty'] == 1
    # Band 2 Characteristic 1 Methods_qty
    assert verf_result[0]['B_2_Characteristic_1_Methods_qty'] == 1
    # Band 2 Characteristic 2 Methods_qty
    assert verf_result[0]['B_2_Characteristic_2_Methods_qty'] == 1
    # Band 2 Characteristic 3 Methods_qty
    assert verf_result[0]['B_2_Characteristic_3_Methods_qty'] == 3
    # Band 2 Characteristic 4 Methods_qty
    assert verf_result[0]['B_2_Characteristic_4_Methods_qty'] == 4
    # Band 2 Characteristic 5 Methods_qty
    assert verf_result[0]['B_2_Characteristic_5_Methods_qty'] == 1
    # Band 3 Characteristic 1 Methods_qty
    assert verf_result[0]['B_3_Characteristic_1_Methods_qty'] == 1
    # Band Characteristic Method Types
    # Band 1 Characteristic 1 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Types'] == 'spectrum measurement'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Types'] == ('CO', 15, 15)
    # Band 1 Characteristic 2 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Types'] == 'spectrum fit'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Types'] == ('CO', 16, 16)
    # Band 1 Characteristic 3 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Types'] == 'spectrum analysis'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Types'] == ('CO', 17, 17)
    # Band 1 Characteristic 4 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Types'] == 'data compilation'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Types'] == ('CO', 18, 18)
    # Band 1 Characteristic 5 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Types'] == 'data extrapolation'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Types'] == ('CO', 19, 19)
    # Band 1 Characteristic 6 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Types'] == 'theory'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Types'] == ('CO', 20, 20)
    # Band 1 Characteristic 6 Method_2_Types
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Types'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Types'] == ('CO', 22, 22)
    # Band 1 Characteristic 6 Method_3_Types
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Types'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Types'] == ('CO', 23, 23)
    # Band 1 Characteristic 7 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Types'] == 'estimation'
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Types'] == ('CO', 25, 25)
    # Band 1 Characteristic 8 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Types'] == 'various'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Types'] == ('CO', 26, 26)
    # Band 1 Characteristic 9 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Types'] == 'other'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Types'] == ('CO', 31, 31)
    # Band 1 Characteristic 10 Method_1_Types
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Types'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Types'] == ('CO', 32, 32)
    # Band 2 Characteristic 1 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Types'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Types'] == ('CO', 37, 37)
    # Band 2 Characteristic 2 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Types'] == 'spectrum measurement'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Types'] == ('CO', 38, 38)
    # Band 2 Characteristic 3 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Types'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Types'] == ('CO', 41, 41)
    # Band 2 Characteristic 3 Method_2_Types
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Types'] == 'spectrum analysis'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Types'] == ('CO', 42, 42)
    # Band 2 Characteristic 3 Method_3_Types
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Types'] == ('CO', 44, 44)
    # Band 2 Characteristic 4 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Types'] == ('CO', 45, 45)
    # Band 2 Characteristic 4 Method_2_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Types'] == ('CO', 46, 46)
    # Band 2 Characteristic 4 Method_3_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Types'] == 'data extrapolation'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Types'] == ('CO', 48, 48)
    # Band 2 Characteristic 4 Method_4_Types
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Types'] == ('CO', 49, 49)
    # Band 2 Characteristic 5 Method_1_Types
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Types'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Types'] == ('CO', 53, 53)
    # Band 3 Characteristic 1 Method_1_Types
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Types'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Types'] == ('CO', 57, 57)
    # Band Characteristic Method Description
    # Band 1 Characteristic 1 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Description'] == 'CP15'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Description'] == ('CP', 15, 15)
    # Band 1 Characteristic 2 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Description'] == 'CP16'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Description'] == ('CP', 16, 16)
    # Band 1 Characteristic 3 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Description'] == 'CP17'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Description'] == ('CP', 17, 17)
    # Band 1 Characteristic 4 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Description'] == 'CP18'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Description'] == ('CP', 18, 18)
    # Band 1 Characteristic 5 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Description'] == 'CP19'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Description'] == ('CP', 19, 19)
    # Band 1 Characteristic 6 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Description'] == 'CP20'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Description'] == ('CP', 20, 20)
    # Band 1 Characteristic 6 Method_2_Description
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Description'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Description'] == ('CP', 22, 22)
    # Band 1 Characteristic 6 Method_2_Description
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Description'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Description'] == ('CP', 23, 23)
    # Band 1 Characteristic 7 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Description'] == 'CP25'
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Description'] == ('CP', 25, 25)
    # Band 1 Characteristic 8 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Description'] == 'CP26'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Description'] == ('CP', 26, 26)
    # Band 1 Characteristic 9 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Description'] == 'CP31'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Description'] == ('CP', 31, 31)
    # Band 1 Characteristic 10 Method_1_Description
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Description'] == 'CP32'
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Description'] == ('CP', 32, 32)
    # Band 2 Characteristic 1 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Description'] == 'CP37'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Description'] == ('CP', 37, 37)
    # Band 2 Characteristic 2 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Description'] == 'CP38'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Description'] == ('CP', 38, 38)
    # Band 2 Characteristic 3 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Description'] == 'CP41'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Description'] == ('CP', 41, 41)
    # Band 2 Characteristic 3 Method_2_Description
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Description'] == 'CP42'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Description'] == ('CP', 42, 42)
    # Band 2 Characteristic 3 Method_3_Description
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Description'] == 'CP44'
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Description'] == ('CP', 44, 44)
    # Band 2 Characteristic 4 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Description'] == 'CP45'
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Description'] == ('CP', 45, 45)
    # Band 2 Characteristic 4 Method_2_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Description'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Description'] == ('CP', 46, 46)
    # Band 2 Characteristic 4 Method_3_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Description'] == 'CP48'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Description'] == ('CP', 48, 48)
    # Band 2 Characteristic 4 Method_4_Description
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Description'] == 'CP49'
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Description'] == ('CP', 49, 49)
    # Band 2 Characteristic 5 Method_1_Description
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Description'] == 'CP53'
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Description'] == ('CP', 53, 53)
    # Band 3 Characteristic 1 Method_1_Description
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Description'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Description'] == ('CP', 57, 57)
    # Band Characteristic Method Fit_Fct_type
    # Band 1 Characteristic 1 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Fit_Fct_type'] == 'Gaussian'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Fit_Fct_type'] == ('CQ', 15, 15)
    # Band 1 Characteristic 2 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Fit_Fct_type'] == 'Voigt'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Fit_Fct_type'] == ('CQ', 16, 16)
    # Band 1 Characteristic 3 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Fit_Fct_type'] == ('CQ', 17, 17)
    # Band 1 Characteristic 4 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Fit_Fct_type'] == 'BWF'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Fit_Fct_type'] == ('CQ', 18, 18)
    # Band 1 Characteristic 5 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Fit_Fct_type'] == ('CQ', 19, 19)
    # Band 1 Characteristic 6 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Fit_Fct_type'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Fit_Fct_type'] == ('CQ', 20, 20)
    # Band 1 Characteristic 6 Method_2_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Fit_Fct_type'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Fit_Fct_type'] == ('CQ', 22, 22)
    # Band 1 Characteristic 6 Method_3_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Fit_Fct_type'] == 'Voigt'
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Fit_Fct_type'] == ('CQ', 23, 23)
    # Band 1 Characteristic 7 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Fit_Fct_type'] == ('CQ', 25, 25)
    # Band 1 Characteristic 8 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Fit_Fct_type'] == ('CQ', 26, 26)
    # Band 1 Characteristic 9 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Fit_Fct_type'] == ('CQ', 31, 31)
    # Band 1 Characteristic 10 Method_1_Fit_Fct_type
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Fit_Fct_type'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Fit_Fct_type'] == ('CQ', 32, 32)
    # Band 2 Characteristic 1 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Fit_Fct_type'] == ('CQ', 37, 37)
    # Band 2 Characteristic 2 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Fit_Fct_type'] == ('CQ', 38, 38)
    # Band 2 Characteristic 3 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Fit_Fct_type'] == ('CQ', 41, 41)
    # Band 2 Characteristic 3 Method_2_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Fit_Fct_type'] == ('CQ', 42, 42)
    # Band 2 Characteristic 3 Method_2_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Fit_Fct_type'] == ('CQ', 44, 44)
    # Band 2 Characteristic 4 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Fit_Fct_type'] == 'Voigt'
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Fit_Fct_type'] == ('CQ', 45, 45)
    # Band 2 Characteristic 4 Method_2_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Fit_Fct_type'] == 'Doppler'
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Fit_Fct_type'] == ('CQ', 46, 46)
    # Band 2 Characteristic 4 Method_3_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Fit_Fct_type'] == 'other'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Fit_Fct_type'] == ('CQ', 48, 48)
    # Band 2 Characteristic 4 Method_4_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Fit_Fct_type'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Fit_Fct_type'] == ('CQ', 49, 49)
    # Band 2 Characteristic 5 Method_1_Fit_Fct_type
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Fit_Fct_type'] == 'Lorentzian'
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Fit_Fct_type'] == ('CQ', 53, 53)
    # Band 3 Characteristic 1 Method_1_Fit_Fct_type
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Fit_Fct_type'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Fit_Fct_type'] == ('CQ', 57, 57)
    # Band Characteristic Method Fit_parameters
    # Band 1 Characteristic 1 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_1_Method_1_Fit_parameters'] == 'CR15'
    assert verf_result[1]['B_1_Characteristic_1_Method_1_Fit_parameters'] == ('CR', 15, 15)
    # Band 1 Characteristic 2 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_2_Method_1_Fit_parameters'] == 'CR16'
    assert verf_result[1]['B_1_Characteristic_2_Method_1_Fit_parameters'] == ('CR', 16, 16)
    # Band 1 Characteristic 3 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_3_Method_1_Fit_parameters'] == 'CR17'
    assert verf_result[1]['B_1_Characteristic_3_Method_1_Fit_parameters'] == ('CR', 17, 17)
    # Band 1 Characteristic 4 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_4_Method_1_Fit_parameters'] == 'CR18'
    assert verf_result[1]['B_1_Characteristic_4_Method_1_Fit_parameters'] == ('CR', 18, 18)
    # Band 1 Characteristic 5 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_5_Method_1_Fit_parameters'] == 'CR19'
    assert verf_result[1]['B_1_Characteristic_5_Method_1_Fit_parameters'] == ('CR', 19, 19)
    # Band 1 Characteristic 6 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_6_Method_1_Fit_parameters'] == 'CR20'
    assert verf_result[1]['B_1_Characteristic_6_Method_1_Fit_parameters'] == ('CR', 20, 20)
    # Band 1 Characteristic 6 Method_2_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_6_Method_2_Fit_parameters'] == 'CR22'
    assert verf_result[1]['B_1_Characteristic_6_Method_2_Fit_parameters'] == ('CR', 22, 22)
    # Band 1 Characteristic 6 Method_3_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_6_Method_3_Fit_parameters'] == ''
    assert verf_result[1]['B_1_Characteristic_6_Method_3_Fit_parameters'] == ('CR', 23, 23)
    # Band 1 Characteristic 7 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_7_Method_1_Fit_parameters'] == ''
    assert verf_result[1]['B_1_Characteristic_7_Method_1_Fit_parameters'] == ('CR', 25, 25)
    # Band 1 Characteristic 8 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_8_Method_1_Fit_parameters'] == 'CR26'
    assert verf_result[1]['B_1_Characteristic_8_Method_1_Fit_parameters'] == ('CR', 26, 26)
    # Band 1 Characteristic 9 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_9_Method_1_Fit_parameters'] == 'CR31'
    assert verf_result[1]['B_1_Characteristic_9_Method_1_Fit_parameters'] == ('CR', 31, 31)
    # Band 1 Characteristic 10 Method_1_Fit_parameters
    assert verf_result[0]['B_1_Characteristic_10_Method_1_Fit_parameters'] == ''
    assert verf_result[1]['B_1_Characteristic_10_Method_1_Fit_parameters'] == ('CR', 32, 32)
    # Band 2 Characteristic 1 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_1_Method_1_Fit_parameters'] == 'CR37'
    assert verf_result[1]['B_2_Characteristic_1_Method_1_Fit_parameters'] == ('CR', 37, 37)
    # Band 2 Characteristic 2 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_2_Method_1_Fit_parameters'] == 'CR38'
    assert verf_result[1]['B_2_Characteristic_2_Method_1_Fit_parameters'] == ('CR', 38, 38)
    # Band 2 Characteristic 3 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_3_Method_1_Fit_parameters'] == 'CR41'
    assert verf_result[1]['B_2_Characteristic_3_Method_1_Fit_parameters'] == ('CR', 41, 41)
    # Band 2 Characteristic 3 Method_2_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_3_Method_2_Fit_parameters'] == 'CR42'
    assert verf_result[1]['B_2_Characteristic_3_Method_2_Fit_parameters'] == ('CR', 42, 42)
    # Band 2 Characteristic 3 Method_2_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_3_Method_3_Fit_parameters'] == 'CR44'
    assert verf_result[1]['B_2_Characteristic_3_Method_3_Fit_parameters'] == ('CR', 44, 44)
    # Band 2 Characteristic 4 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_1_Fit_parameters'] == 'CR45'
    assert verf_result[1]['B_2_Characteristic_4_Method_1_Fit_parameters'] == ('CR', 45, 45)
    # Band 2 Characteristic 4 Method_2_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_2_Fit_parameters'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Method_2_Fit_parameters'] == ('CR', 46, 46)
    # Band 2 Characteristic 4 Method_3_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_3_Fit_parameters'] == 'CR48'
    assert verf_result[1]['B_2_Characteristic_4_Method_3_Fit_parameters'] == ('CR', 48, 48)
    # Band 2 Characteristic 4 Method_4_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_4_Method_4_Fit_parameters'] == 'CR49'
    assert verf_result[1]['B_2_Characteristic_4_Method_4_Fit_parameters'] == ('CR', 49, 49)
    # Band 2 Characteristic 5 Method_1_Fit_parameters
    assert verf_result[0]['B_2_Characteristic_5_Method_1_Fit_parameters'] == 'CR53'
    assert verf_result[1]['B_2_Characteristic_5_Method_1_Fit_parameters'] == ('CR', 53, 53)
    # Band 3 Characteristic 1 Method_1_Fit_parameters
    assert verf_result[0]['B_3_Characteristic_1_Method_1_Fit_parameters'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Method_1_Fit_parameters'] == ('CR', 57, 57)
    # Band Characteristic Methods_Overlap
    # Band 1 Characteristic 1 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_1_Methods_Overlap'] == 'extracted'
    assert verf_result[1]['B_1_Characteristic_1_Methods_Overlap'] == ('CU', 15, 15)
    # Band 1 Characteristic 2 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_2_Methods_Overlap'] == 'isolated'
    assert verf_result[1]['B_1_Characteristic_2_Methods_Overlap'] == ('CU', 16, 16)
    # Band 1 Characteristic 3 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_3_Methods_Overlap'] == 'slightly blended'
    assert verf_result[1]['B_1_Characteristic_3_Methods_Overlap'] == ('CU', 17, 17)
    # Band 1 Characteristic 4 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_4_Methods_Overlap'] == 'moderately blended'
    assert verf_result[1]['B_1_Characteristic_4_Methods_Overlap'] == ('CU', 18, 18)
    # Band 1 Characteristic 5 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_5_Methods_Overlap'] == 'strongly blended'
    assert verf_result[1]['B_1_Characteristic_5_Methods_Overlap'] == ('CU', 19, 19)
    # Band 1 Characteristic 6 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_6_Methods_Overlap'] == 'multiple'
    assert verf_result[1]['B_1_Characteristic_6_Methods_Overlap'] == ('CU', 20, 20)
    # Band 1 Characteristic 7 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_7_Methods_Overlap'] == 'other'
    assert verf_result[1]['B_1_Characteristic_7_Methods_Overlap'] == ('CU', 25, 25)
    # Band 1 Characteristic 8 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_8_Methods_Overlap'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_8_Methods_Overlap'] == ('CU', 26, 26)
    # Band 1 Characteristic 9 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_9_Methods_Overlap'] == ''
    assert verf_result[1]['B_1_Characteristic_9_Methods_Overlap'] == ('CU', 31, 31)
    # Band 1 Characteristic 10 Methods_Overlap
    assert verf_result[0]['B_1_Characteristic_10_Methods_Overlap'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_10_Methods_Overlap'] == ('CU', 32, 32)
    # Band 2 Characteristic 1 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_1_Methods_Overlap'] == 'isolated'
    assert verf_result[1]['B_2_Characteristic_1_Methods_Overlap'] == ('CU', 37, 37)
    # Band 2 Characteristic 2 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_2_Methods_Overlap'] == 'strongly blended'
    assert verf_result[1]['B_2_Characteristic_2_Methods_Overlap'] == ('CU', 38, 38)
    # Band 2 Characteristic 3 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_3_Methods_Overlap'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_3_Methods_Overlap'] == ('CU', 41, 41)
    # Band 2 Characteristic 4 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_4_Methods_Overlap'] == 'isolated'
    assert verf_result[1]['B_2_Characteristic_4_Methods_Overlap'] == ('CU', 45, 45)
    # Band 2 Characteristic 5 Methods_Overlap
    assert verf_result[0]['B_2_Characteristic_5_Methods_Overlap'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Methods_Overlap'] == ('CU', 53, 53)
    # Band 3 Characteristic 1 Methods_Overlap
    assert verf_result[0]['B_3_Characteristic_1_Methods_Overlap'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Methods_Overlap'] == ('CU', 57, 57)
    # Band Characteristic Position_Peak_method
    # Band 1 Characteristic 1 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_1_Position_Peak_method'] == 'peak'
    assert verf_result[1]['B_1_Characteristic_1_Position_Peak_method'] == ('CW', 15, 15)
    # Band 1 Characteristic 2 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_2_Position_Peak_method'] == 'fit peak'
    assert verf_result[1]['B_1_Characteristic_2_Position_Peak_method'] == ('CW', 16, 16)
    # Band 1 Characteristic 3 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_3_Position_Peak_method'] == '90%-max center'
    assert verf_result[1]['B_1_Characteristic_3_Position_Peak_method'] == ('CW', 17, 17)
    # Band 1 Characteristic 4 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_4_Position_Peak_method'] == 'first derivativee'
    assert verf_result[1]['B_1_Characteristic_4_Position_Peak_method'] == ('CW', 18, 18)
    # Band 1 Characteristic 5 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_5_Position_Peak_method'] == 'second derivative'
    assert verf_result[1]['B_1_Characteristic_5_Position_Peak_method'] == ('CW', 19, 19)
    # Band 1 Characteristic 6 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_6_Position_Peak_method'] == 'higher order derivative'
    assert verf_result[1]['B_1_Characteristic_6_Position_Peak_method'] == ('CW', 20, 20)
    # Band 1 Characteristic 7 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_7_Position_Peak_method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_7_Position_Peak_method'] == ('CW', 25, 25)
    # Band 1 Characteristic 8 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_8_Position_Peak_method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_8_Position_Peak_method'] == ('CW', 26, 26)
    # Band 1 Characteristic 9 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_9_Position_Peak_method'] == ''
    assert verf_result[1]['B_1_Characteristic_9_Position_Peak_method'] == ('CW', 31, 31)
    # Band 1 Characteristic 10 Position_Peak_method
    assert verf_result[0]['B_1_Characteristic_10_Position_Peak_method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_10_Position_Peak_method'] == ('CW', 32, 32)
    # Band 2 Characteristic 1 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_1_Position_Peak_method'] == 'calculated'
    assert verf_result[1]['B_2_Characteristic_1_Position_Peak_method'] == ('CW', 37, 37)
    # Band 2 Characteristic 2 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_2_Position_Peak_method'] == 'estimated'
    assert verf_result[1]['B_2_Characteristic_2_Position_Peak_method'] == ('CW', 38, 38)
    # Band 2 Characteristic 3 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_3_Position_Peak_method'] == 'various'
    assert verf_result[1]['B_2_Characteristic_3_Position_Peak_method'] == ('CW', 41, 41)
    # Band 2 Characteristic 4 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_4_Position_Peak_method'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_4_Position_Peak_method'] == ('CW', 45, 45)
    # Band 2 Characteristic 5 Position_Peak_method
    assert verf_result[0]['B_2_Characteristic_5_Position_Peak_method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Position_Peak_method'] == ('CW', 53, 53)
    # Band 3 Characteristic 1 Position_Peak_method
    assert verf_result[0]['B_3_Characteristic_1_Position_Peak_method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Peak_method'] == ('CW', 57, 57)
    # Band Characteristic Position_Peak
    # Band 1 Characteristic 1 Position_Peak
    assert verf_result[0]['B_1_Characteristic_1_Position_Peak'] == 'CX15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Peak'] == ('CX', 15, 15)
    # Band 1 Characteristic 2 Position_Peak
    assert verf_result[0]['B_1_Characteristic_2_Position_Peak'] == 'CX16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Peak'] == ('CX', 16, 16)
    # Band 1 Characteristic 3 Position_Peak
    assert verf_result[0]['B_1_Characteristic_3_Position_Peak'] == 'CX17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Peak'] == ('CX', 17, 17)
    # Band 1 Characteristic 4 Position_Peak
    assert verf_result[0]['B_1_Characteristic_4_Position_Peak'] == 'CX18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Peak'] == ('CX', 18, 18)
    # Band 1 Characteristic 5 Position_Peak
    assert verf_result[0]['B_1_Characteristic_5_Position_Peak'] == 'CX19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Peak'] == ('CX', 19, 19)
    # Band 1 Characteristic 6 Position_Peak
    assert verf_result[0]['B_1_Characteristic_6_Position_Peak'] == 'CX20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Peak'] == ('CX', 20, 20)
    # Band 1 Characteristic 7 Position_Peak
    assert verf_result[0]['B_1_Characteristic_7_Position_Peak'] == 'CX25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Peak'] == ('CX', 25, 25)
    # Band 1 Characteristic 8 Position_Peak
    assert verf_result[0]['B_1_Characteristic_8_Position_Peak'] == 'CX26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Peak'] == ('CX', 26, 26)
    # Band 1 Characteristic 9 Position_Peak
    assert verf_result[0]['B_1_Characteristic_9_Position_Peak'] == 'CX31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Peak'] == ('CX', 31, 31)
    # Band 1 Characteristic 10 Position_Peak
    assert verf_result[0]['B_1_Characteristic_10_Position_Peak'] == 'CX32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Peak'] == ('CX', 32, 32)
    # Band 2 Characteristic 1 Position_Peak
    assert verf_result[0]['B_2_Characteristic_1_Position_Peak'] == 'CX37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Peak'] == ('CX', 37, 37)
    # Band 2 Characteristic 2 Position_Peak
    assert verf_result[0]['B_2_Characteristic_2_Position_Peak'] == 'CX38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Peak'] == ('CX', 38, 38)
    # Band 2 Characteristic 3 Position_Peak
    assert verf_result[0]['B_2_Characteristic_3_Position_Peak'] == 'CX41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Peak'] == ('CX', 41, 41)
    # Band 2 Characteristic 4 Position_Peak
    assert verf_result[0]['B_2_Characteristic_4_Position_Peak'] == 'CX45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Peak'] == ('CX', 45, 45)
    # Band 2 Characteristic 5 Position_Peak
    assert verf_result[0]['B_2_Characteristic_5_Position_Peak'] == 'CX53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Peak'] == ('CX', 53, 53)
    # Band 3 Characteristic 1 Position_Peak
    assert verf_result[0]['B_3_Characteristic_1_Position_Peak'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Peak'] == ('CX', 57, 57)
    # Band Characteristic Position_Peak_error
    # Band 1 Characteristic 1 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_1_Position_Peak_error'] == 'CY15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Peak_error'] == ('CY', 15, 15)
    # Band 1 Characteristic 2 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_2_Position_Peak_error'] == 'CY16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Peak_error'] == ('CY', 16, 16)
    # Band 1 Characteristic 3 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_3_Position_Peak_error'] == 'CY17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Peak_error'] == ('CY', 17, 17)
    # Band 1 Characteristic 4 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_4_Position_Peak_error'] == 'CY18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Peak_error'] == ('CY', 18, 18)
    # Band 1 Characteristic 5 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_5_Position_Peak_error'] == 'CY19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Peak_error'] == ('CY', 19, 19)
    # Band 1 Characteristic 6 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_6_Position_Peak_error'] == 'CY20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Peak_error'] == ('CY', 20, 20)
    # Band 1 Characteristic 7 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_7_Position_Peak_error'] == 'CY25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Peak_error'] == ('CY', 25, 25)
    # Band 1 Characteristic 8 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_8_Position_Peak_error'] == 'CY26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Peak_error'] == ('CY', 26, 26)
    # Band 1 Characteristic 9 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_9_Position_Peak_error'] == 'CY31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Peak_error'] == ('CY', 31, 31)
    # Band 1 Characteristic 10 Position_Peak_error
    assert verf_result[0]['B_1_Characteristic_10_Position_Peak_error'] == 'CY32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Peak_error'] == ('CY', 32, 32)
    # Band 2 Characteristic 1 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_1_Position_Peak_error'] == 'CY37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Peak_error'] == ('CY', 37, 37)
    # Band 2 Characteristic 2 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_2_Position_Peak_error'] == 'CY38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Peak_error'] == ('CY', 38, 38)
    # Band 2 Characteristic 3 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_3_Position_Peak_error'] == 'CY41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Peak_error'] == ('CY', 41, 41)
    # Band 2 Characteristic 4 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_4_Position_Peak_error'] == 'CY45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Peak_error'] == ('CY', 45, 45)
    # Band 2 Characteristic 5 Position_Peak_error
    assert verf_result[0]['B_2_Characteristic_5_Position_Peak_error'] == 'CY53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Peak_error'] == ('CY', 53, 53)
    # Band 3 Characteristic 1 Position_Peak_error
    assert verf_result[0]['B_3_Characteristic_1_Position_Peak_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Peak_error'] == ('CY', 57, 57)
    # Band Characteristic Position_Center_method
    # Band 1 Characteristic 1 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_1_Position_Center_method'] == 'half-max center'
    assert verf_result[1]['B_1_Characteristic_1_Position_Center_method'] == ('CZ', 15, 15)
    # Band 1 Characteristic 2 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_2_Position_Center_method'] == 'fit center'
    assert verf_result[1]['B_1_Characteristic_2_Position_Center_method'] == ('CZ', 16, 16)
    # Band 1 Characteristic 3 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_3_Position_Center_method'] == 'second derivative'
    assert verf_result[1]['B_1_Characteristic_3_Position_Center_method'] == ('CZ', 17, 17)
    # Band 1 Characteristic 4 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_4_Position_Center_method'] == 'higher order derivative'
    assert verf_result[1]['B_1_Characteristic_4_Position_Center_method'] == ('CZ', 18, 18)
    # Band 1 Characteristic 5 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_5_Position_Center_method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_5_Position_Center_method'] == ('CZ', 19, 19)
    # Band 1 Characteristic 6 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_6_Position_Center_method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_6_Position_Center_method'] == ('CZ', 20, 20)
    # Band 1 Characteristic 7 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_7_Position_Center_method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_7_Position_Center_method'] == ('CZ', 25, 25)
    # Band 1 Characteristic 8 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_8_Position_Center_method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_8_Position_Center_method'] == ('CZ', 26, 26)
    # Band 1 Characteristic 9 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_9_Position_Center_method'] == ''
    assert verf_result[1]['B_1_Characteristic_9_Position_Center_method'] == ('CZ', 31, 31)
    # Band 1 Characteristic 10 Position_Center_method
    assert verf_result[0]['B_1_Characteristic_10_Position_Center_method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_10_Position_Center_method'] == ('CZ', 32, 32)
    # Band 2 Characteristic 1 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_1_Position_Center_method'] == 'other'
    assert verf_result[1]['B_2_Characteristic_1_Position_Center_method'] == ('CZ', 37, 37)
    # Band 2 Characteristic 2 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_2_Position_Center_method'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Position_Center_method'] == ('CZ', 38, 38)
    # Band 2 Characteristic 3 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_3_Position_Center_method'] == 'fit center'
    assert verf_result[1]['B_2_Characteristic_3_Position_Center_method'] == ('CZ', 41, 41)
    # Band 2 Characteristic 4 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_4_Position_Center_method'] == 'extrapolated'
    assert verf_result[1]['B_2_Characteristic_4_Position_Center_method'] == ('CZ', 45, 45)
    # Band 2 Characteristic 5 Position_Center_method
    assert verf_result[0]['B_2_Characteristic_5_Position_Center_method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Position_Center_method'] == ('CZ', 53, 53)
    # Band 3 Characteristic 1 Position_Center_method
    assert verf_result[0]['B_3_Characteristic_1_Position_Center_method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Center_method'] == ('CZ', 57, 57)
    # Band Characteristic Position_Center
    # Band 1 Characteristic 1 Position_Center
    assert verf_result[0]['B_1_Characteristic_1_Position_Center'] == 'DA15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Center'] == ('DA', 15, 15)
    # Band 1 Characteristic 2 Position_Center
    assert verf_result[0]['B_1_Characteristic_2_Position_Center'] == 'DA16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Center'] == ('DA', 16, 16)
    # Band 1 Characteristic 3 Position_Center
    assert verf_result[0]['B_1_Characteristic_3_Position_Center'] == 'DA17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Center'] == ('DA', 17, 17)
    # Band 1 Characteristic 4 Position_Center
    assert verf_result[0]['B_1_Characteristic_4_Position_Center'] == 'DA18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Center'] == ('DA', 18, 18)
    # Band 1 Characteristic 5 Position_Center
    assert verf_result[0]['B_1_Characteristic_5_Position_Center'] == 'DA19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Center'] == ('DA', 19, 19)
    # Band 1 Characteristic 6 Position_Center
    assert verf_result[0]['B_1_Characteristic_6_Position_Center'] == 'DA20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Center'] == ('DA', 20, 20)
    # Band 1 Characteristic 7 Position_Center
    assert verf_result[0]['B_1_Characteristic_7_Position_Center'] == 'DA25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Center'] == ('DA', 25, 25)
    # Band 1 Characteristic 8 Position_Center
    assert verf_result[0]['B_1_Characteristic_8_Position_Center'] == 'DA26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Center'] == ('DA', 26, 26)
    # Band 1 Characteristic 9 Position_Center
    assert verf_result[0]['B_1_Characteristic_9_Position_Center'] == 'DA31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Center'] == ('DA', 31, 31)
    # Band 1 Characteristic 10 Position_Center
    assert verf_result[0]['B_1_Characteristic_10_Position_Center'] == 'DA32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Center'] == ('DA', 32, 32)
    # Band 2 Characteristic 1 Position_Center
    assert verf_result[0]['B_2_Characteristic_1_Position_Center'] == 'DA37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Center'] == ('DA', 37, 37)
    # Band 2 Characteristic 2 Position_Center
    assert verf_result[0]['B_2_Characteristic_2_Position_Center'] == 'DA38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Center'] == ('DA', 38, 38)
    # Band 2 Characteristic 3 Position_Center
    assert verf_result[0]['B_2_Characteristic_3_Position_Center'] == 'DA41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Center'] == ('DA', 41, 41)
    # Band 2 Characteristic 4 Position_Center
    assert verf_result[0]['B_2_Characteristic_4_Position_Center'] == 'DA45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Center'] == ('DA', 45, 45)
    # Band 2 Characteristic 5 Position_Center
    assert verf_result[0]['B_2_Characteristic_5_Position_Center'] == 'DA53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Center'] == ('DA', 53, 53)
    # Band 3 Characteristic 1 Position_Center
    assert verf_result[0]['B_3_Characteristic_1_Position_Center'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Center'] == ('DA', 57, 57)
    # Band Characteristic Position_Center_error
    # Band 1 Characteristic 1 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_1_Position_Center_error'] == 'DB15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Center_error'] == ('DB', 15, 15)
    # Band 1 Characteristic 2 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_2_Position_Center_error'] == 'DB16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Center_error'] == ('DB', 16, 16)
    # Band 1 Characteristic 3 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_3_Position_Center_error'] == 'DB17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Center_error'] == ('DB', 17, 17)
    # Band 1 Characteristic 4 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_4_Position_Center_error'] == 'DB18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Center_error'] == ('DB', 18, 18)
    # Band 1 Characteristic 5 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_5_Position_Center_error'] == 'DB19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Center_error'] == ('DB', 19, 19)
    # Band 1 Characteristic 6 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_6_Position_Center_error'] == 'DB20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Center_error'] == ('DB', 20, 20)
    # Band 1 Characteristic 7 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_7_Position_Center_error'] == 'DB25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Center_error'] == ('DB', 25, 25)
    # Band 1 Characteristic 8 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_8_Position_Center_error'] == 'DB26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Center_error'] == ('DB', 26, 26)
    # Band 1 Characteristic 9 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_9_Position_Center_error'] == 'DB31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Center_error'] == ('DB', 31, 31)
    # Band 1 Characteristic 10 Position_Center_error
    assert verf_result[0]['B_1_Characteristic_10_Position_Center_error'] == 'DB32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Center_error'] == ('DB', 32, 32)
    # Band 2 Characteristic 1 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_1_Position_Center_error'] == 'DB37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Center_error'] == ('DB', 37, 37)
    # Band 2 Characteristic 2 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_2_Position_Center_error'] == 'DB38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Center_error'] == ('DB', 38, 38)
    # Band 2 Characteristic 3 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_3_Position_Center_error'] == 'DB41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Center_error'] == ('DB', 41, 41)
    # Band 2 Characteristic 4 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_4_Position_Center_error'] == 'DB45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Center_error'] == ('DB', 45, 45)
    # Band 2 Characteristic 5 Position_Center_error
    assert verf_result[0]['B_2_Characteristic_5_Position_Center_error'] == 'DB53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Center_error'] == ('DB', 53, 53)
    # Band 3 Characteristic 1 Position_Center_error
    assert verf_result[0]['B_3_Characteristic_1_Position_Center_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Center_error'] == ('DB', 57, 57)
    # Band Characteristic Position_Evaluation
    # Band 1 Characteristic 1 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Position_Evaluation'] == ('DC', 15, 15)
    # Band 1 Characteristic 2 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Position_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Position_Evaluation'] == ('DC', 16, 16)
    # Band 1 Characteristic 3 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Position_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Position_Evaluation'] == ('DC', 17, 17)
    # Band 1 Characteristic 4 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Position_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Position_Evaluation'] == ('DC', 18, 18)
    # Band 1 Characteristic 5 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Position_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Position_Evaluation'] == ('DC', 19, 19)
    # Band 1 Characteristic 6 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Position_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Position_Evaluation'] == ('DC', 20, 20)
    # Band 1 Characteristic 7 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_7_Position_Evaluation'] == ('DC', 25, 25)
    # Band 1 Characteristic 8 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Position_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_8_Position_Evaluation'] == ('DC', 26, 26)
    # Band 1 Characteristic 9 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_9_Position_Evaluation'] == ('DC', 31, 31)
    # Band 1 Characteristic 10 Position_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Position_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Position_Evaluation'] == ('DC', 32, 32)
    # Band 2 Characteristic 1 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Position_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_1_Position_Evaluation'] == ('DC', 37, 37)
    # Band 2 Characteristic 2 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Position_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_2_Characteristic_2_Position_Evaluation'] == ('DC', 38, 38)
    # Band 2 Characteristic 3 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Position_Evaluation'] == 'undefined'
    assert verf_result[1]['B_2_Characteristic_3_Position_Evaluation'] == ('DC', 41, 41)
    # Band 2 Characteristic 4 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Position_Evaluation'] == 'with caution'
    assert verf_result[1]['B_2_Characteristic_4_Position_Evaluation'] == ('DC', 45, 45)
    # Band 2 Characteristic 5 Position_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Position_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Position_Evaluation'] == ('DC', 53, 53)
    # Band 3 Characteristic 1 Position_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Position_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Evaluation'] == ('DC', 57, 57)
    # Band Characteristic Position_Comment
    # Band 1 Characteristic 1 Position_Comment
    assert verf_result[0]['B_1_Characteristic_1_Position_Comment'] == 'DD15'
    assert verf_result[1]['B_1_Characteristic_1_Position_Comment'] == ('DD', 15, 15)
    # Band 1 Characteristic 2 Position_Comment
    assert verf_result[0]['B_1_Characteristic_2_Position_Comment'] == 'DD16'
    assert verf_result[1]['B_1_Characteristic_2_Position_Comment'] == ('DD', 16, 16)
    # Band 1 Characteristic 3 Position_Comment
    assert verf_result[0]['B_1_Characteristic_3_Position_Comment'] == 'DD17'
    assert verf_result[1]['B_1_Characteristic_3_Position_Comment'] == ('DD', 17, 17)
    # Band 1 Characteristic 4 Position_Comment
    assert verf_result[0]['B_1_Characteristic_4_Position_Comment'] == 'DD18'
    assert verf_result[1]['B_1_Characteristic_4_Position_Comment'] == ('DD', 18, 18)
    # Band 1 Characteristic 5 Position_Comment
    assert verf_result[0]['B_1_Characteristic_5_Position_Comment'] == 'DD19'
    assert verf_result[1]['B_1_Characteristic_5_Position_Comment'] == ('DD', 19, 19)
    # Band 1 Characteristic 6 Position_Comment
    assert verf_result[0]['B_1_Characteristic_6_Position_Comment'] == 'DD20'
    assert verf_result[1]['B_1_Characteristic_6_Position_Comment'] == ('DD', 20, 20)
    # Band 1 Characteristic 7 Position_Comment
    assert verf_result[0]['B_1_Characteristic_7_Position_Comment'] == 'DD25'
    assert verf_result[1]['B_1_Characteristic_7_Position_Comment'] == ('DD', 25, 25)
    # Band 1 Characteristic 8 Position_Comment
    assert verf_result[0]['B_1_Characteristic_8_Position_Comment'] == 'DD26'
    assert verf_result[1]['B_1_Characteristic_8_Position_Comment'] == ('DD', 26, 26)
    # Band 1 Characteristic 9 Position_Comment
    assert verf_result[0]['B_1_Characteristic_9_Position_Comment'] == 'DD31'
    assert verf_result[1]['B_1_Characteristic_9_Position_Comment'] == ('DD', 31, 31)
    # Band 1 Characteristic 10 Position_Comment
    assert verf_result[0]['B_1_Characteristic_10_Position_Comment'] == 'DD32'
    assert verf_result[1]['B_1_Characteristic_10_Position_Comment'] == ('DD', 32, 32)
    # Band 2 Characteristic 1 Position_Comment
    assert verf_result[0]['B_2_Characteristic_1_Position_Comment'] == 'DD37'
    assert verf_result[1]['B_2_Characteristic_1_Position_Comment'] == ('DD', 37, 37)
    # Band 2 Characteristic 2 Position_Comment
    assert verf_result[0]['B_2_Characteristic_2_Position_Comment'] == 'DD38'
    assert verf_result[1]['B_2_Characteristic_2_Position_Comment'] == ('DD', 38, 38)
    # Band 2 Characteristic 3 Position_Comment
    assert verf_result[0]['B_2_Characteristic_3_Position_Comment'] == 'DD41'
    assert verf_result[1]['B_2_Characteristic_3_Position_Comment'] == ('DD', 41, 41)
    # Band 2 Characteristic 4 Position_Comment
    assert verf_result[0]['B_2_Characteristic_4_Position_Comment'] == 'DD45'
    assert verf_result[1]['B_2_Characteristic_4_Position_Comment'] == ('DD', 45, 45)
    # Band 2 Characteristic 5 Position_Comment
    assert verf_result[0]['B_2_Characteristic_5_Position_Comment'] == 'DD53'
    assert verf_result[1]['B_2_Characteristic_5_Position_Comment'] == ('DD', 53, 53)
    # Band 3 Characteristic 1 Position_Comment
    assert verf_result[0]['B_3_Characteristic_1_Position_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Position_Comment'] == ('DD', 57, 57)
    # Band Characteristic Width_Method
    # Band 1 Characteristic 1 Width_Method
    assert verf_result[0]['B_1_Characteristic_1_Width_Method'] == 'fwhm'
    assert verf_result[1]['B_1_Characteristic_1_Width_Method'] == ('DG', 15, 15)
    # Band 1 Characteristic 2 Width_Method
    assert verf_result[0]['B_1_Characteristic_2_Width_Method'] == 'fit fwhm'
    assert verf_result[1]['B_1_Characteristic_2_Width_Method'] == ('DG', 16, 16)
    # Band 1 Characteristic 3 Width_Method
    assert verf_result[0]['B_1_Characteristic_3_Width_Method'] == 'hwhm'
    assert verf_result[1]['B_1_Characteristic_3_Width_Method'] == ('DG', 17, 17)
    # Band 1 Characteristic 4 Width_Method
    assert verf_result[0]['B_1_Characteristic_4_Width_Method'] == 'first derivative'
    assert verf_result[1]['B_1_Characteristic_4_Width_Method'] == ('DG', 18, 18)
    # Band 1 Characteristic 5 Width_Method
    assert verf_result[0]['B_1_Characteristic_5_Width_Method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_5_Width_Method'] == ('DG', 19, 19)
    # Band 1 Characteristic 6 Width_Method
    assert verf_result[0]['B_1_Characteristic_6_Width_Method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_6_Width_Method'] == ('DG', 20, 20)
    # Band 1 Characteristic 7 Width_Method
    assert verf_result[0]['B_1_Characteristic_7_Width_Method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_7_Width_Method'] == ('DG', 25, 25)
    # Band 1 Characteristic 8 Width_Method
    assert verf_result[0]['B_1_Characteristic_8_Width_Method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_8_Width_Method'] == ('DG', 26, 26)
    # Band 1 Characteristic 9 Width_Method
    assert verf_result[0]['B_1_Characteristic_9_Width_Method'] == 'other'
    assert verf_result[1]['B_1_Characteristic_9_Width_Method'] == ('DG', 31, 31)
    # Band 1 Characteristic 10 Width_Method
    assert verf_result[0]['B_1_Characteristic_10_Width_Method'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_10_Width_Method'] == ('DG', 32, 32)
    # Band 2 Characteristic 1 Width_Method
    assert verf_result[0]['B_2_Characteristic_1_Width_Method'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_1_Width_Method'] == ('DG', 37, 37)
    # Band 2 Characteristic 2 Width_Method
    assert verf_result[0]['B_2_Characteristic_2_Width_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_2_Width_Method'] == ('DG', 38, 38)
    # Band 2 Characteristic 3 Width_Method
    assert verf_result[0]['B_2_Characteristic_3_Width_Method'] == 'first derivative'
    assert verf_result[1]['B_2_Characteristic_3_Width_Method'] == ('DG', 41, 41)
    # Band 2 Characteristic 4 Width_Method
    assert verf_result[0]['B_2_Characteristic_4_Width_Method'] == 'fit fwhm'
    assert verf_result[1]['B_2_Characteristic_4_Width_Method'] == ('DG', 45, 45)
    # Band 2 Characteristic 5 Width_Method
    assert verf_result[0]['B_2_Characteristic_5_Width_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Width_Method'] == ('DG', 53, 53)
    # Band 3 Characteristic 1 Width_Method
    assert verf_result[0]['B_3_Characteristic_1_Width_Method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Method'] == ('DG', 57, 57)
    # Band Characteristic Width_FWHM
    # Band 1 Characteristic 1 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_1_Width_FWHM'] == 'DH15'
    assert verf_result[1]['B_1_Characteristic_1_Width_FWHM'] == ('DH', 15, 15)
    # Band 1 Characteristic 2 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_2_Width_FWHM'] == 'DH16'
    assert verf_result[1]['B_1_Characteristic_2_Width_FWHM'] == ('DH', 16, 16)
    # Band 1 Characteristic 3 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_3_Width_FWHM'] == 'DH17'
    assert verf_result[1]['B_1_Characteristic_3_Width_FWHM'] == ('DH', 17, 17)
    # Band 1 Characteristic 4 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_4_Width_FWHM'] == 'DH18'
    assert verf_result[1]['B_1_Characteristic_4_Width_FWHM'] == ('DH', 18, 18)
    # Band 1 Characteristic 5 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_5_Width_FWHM'] == 'DH19'
    assert verf_result[1]['B_1_Characteristic_5_Width_FWHM'] == ('DH', 19, 19)
    # Band 1 Characteristic 6 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_6_Width_FWHM'] == 'DH20'
    assert verf_result[1]['B_1_Characteristic_6_Width_FWHM'] == ('DH', 20, 20)
    # Band 1 Characteristic 7 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_7_Width_FWHM'] == 'DH25'
    assert verf_result[1]['B_1_Characteristic_7_Width_FWHM'] == ('DH', 25, 25)
    # Band 1 Characteristic 8 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_8_Width_FWHM'] == 'DH26'
    assert verf_result[1]['B_1_Characteristic_8_Width_FWHM'] == ('DH', 26, 26)
    # Band 1 Characteristic 9 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_9_Width_FWHM'] == 'DH31'
    assert verf_result[1]['B_1_Characteristic_9_Width_FWHM'] == ('DH', 31, 31)
    # Band 1 Characteristic 10 Width_FWHM
    assert verf_result[0]['B_1_Characteristic_10_Width_FWHM'] == 'DH32'
    assert verf_result[1]['B_1_Characteristic_10_Width_FWHM'] == ('DH', 32, 32)
    # Band 2 Characteristic 1 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_1_Width_FWHM'] == 'DH37'
    assert verf_result[1]['B_2_Characteristic_1_Width_FWHM'] == ('DH', 37, 37)
    # Band 2 Characteristic 2 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_2_Width_FWHM'] == 'DH38'
    assert verf_result[1]['B_2_Characteristic_2_Width_FWHM'] == ('DH', 38, 38)
    # Band 2 Characteristic 3 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_3_Width_FWHM'] == 'DH41'
    assert verf_result[1]['B_2_Characteristic_3_Width_FWHM'] == ('DH', 41, 41)
    # Band 2 Characteristic 4 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_4_Width_FWHM'] == 'DH45'
    assert verf_result[1]['B_2_Characteristic_4_Width_FWHM'] == ('DH', 45, 45)
    # Band 2 Characteristic 5 Width_FWHM
    assert verf_result[0]['B_2_Characteristic_5_Width_FWHM'] == 'DH53'
    assert verf_result[1]['B_2_Characteristic_5_Width_FWHM'] == ('DH', 53, 53)
    # Band 3 Characteristic 1 Width_FWHM
    assert verf_result[0]['B_3_Characteristic_1_Width_FWHM'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_FWHM'] == ('DH', 57, 57)
    # Band Characteristic Width_FWHM_error
    # Band 1 Characteristic 1 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_1_Width_FWHM_error'] == 'DI15'
    assert verf_result[1]['B_1_Characteristic_1_Width_FWHM_error'] == ('DI', 15, 15)
    # Band 1 Characteristic 2 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_2_Width_FWHM_error'] == 'DI16'
    assert verf_result[1]['B_1_Characteristic_2_Width_FWHM_error'] == ('DI', 16, 16)
    # Band 1 Characteristic 3 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_3_Width_FWHM_error'] == 'DI17'
    assert verf_result[1]['B_1_Characteristic_3_Width_FWHM_error'] == ('DI', 17, 17)
    # Band 1 Characteristic 4 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_4_Width_FWHM_error'] == 'DI18'
    assert verf_result[1]['B_1_Characteristic_4_Width_FWHM_error'] == ('DI', 18, 18)
    # Band 1 Characteristic 5 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_5_Width_FWHM_error'] == 'DI19'
    assert verf_result[1]['B_1_Characteristic_5_Width_FWHM_error'] == ('DI', 19, 19)
    # Band 1 Characteristic 6 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_6_Width_FWHM_error'] == 'DI20'
    assert verf_result[1]['B_1_Characteristic_6_Width_FWHM_error'] == ('DI', 20, 20)
    # Band 1 Characteristic 7 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_7_Width_FWHM_error'] == 'DI25'
    assert verf_result[1]['B_1_Characteristic_7_Width_FWHM_error'] == ('DI', 25, 25)
    # Band 1 Characteristic 8 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_8_Width_FWHM_error'] == 'DI26'
    assert verf_result[1]['B_1_Characteristic_8_Width_FWHM_error'] == ('DI', 26, 26)
    # Band 1 Characteristic 9 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_9_Width_FWHM_error'] == 'DI31'
    assert verf_result[1]['B_1_Characteristic_9_Width_FWHM_error'] == ('DI', 31, 31)
    # Band 1 Characteristic 10 Width_FWHM_error
    assert verf_result[0]['B_1_Characteristic_10_Width_FWHM_error'] == 'DI32'
    assert verf_result[1]['B_1_Characteristic_10_Width_FWHM_error'] == ('DI', 32, 32)
    # Band 2 Characteristic 1 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_1_Width_FWHM_error'] == 'DI37'
    assert verf_result[1]['B_2_Characteristic_1_Width_FWHM_error'] == ('DI', 37, 37)
    # Band 2 Characteristic 2 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_2_Width_FWHM_error'] == 'DI38'
    assert verf_result[1]['B_2_Characteristic_2_Width_FWHM_error'] == ('DI', 38, 38)
    # Band 2 Characteristic 3 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_3_Width_FWHM_error'] == 'DI41'
    assert verf_result[1]['B_2_Characteristic_3_Width_FWHM_error'] == ('DI', 41, 41)
    # Band 2 Characteristic 4 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_4_Width_FWHM_error'] == 'DI45'
    assert verf_result[1]['B_2_Characteristic_4_Width_FWHM_error'] == ('DI', 45, 45)
    # Band 2 Characteristic 5 Width_FWHM_error
    assert verf_result[0]['B_2_Characteristic_5_Width_FWHM_error'] == 'DI53'
    assert verf_result[1]['B_2_Characteristic_5_Width_FWHM_error'] == ('DI', 53, 53)
    # Band 3 Characteristic 1 Width_FWHM_error
    assert verf_result[0]['B_3_Characteristic_1_Width_FWHM_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_FWHM_error'] == ('DI', 57, 57)
    # Band Characteristic Width_Shape
    # Band 1 Characteristic 1 Width_Shape
    assert verf_result[0]['B_1_Characteristic_1_Width_Shape'] == 'symmetric'
    assert verf_result[1]['B_1_Characteristic_1_Width_Shape'] == ('DJ', 15, 15)
    # Band 1 Characteristic 2 Width_Shape
    assert verf_result[0]['B_1_Characteristic_2_Width_Shape'] == 'gaussian'
    assert verf_result[1]['B_1_Characteristic_2_Width_Shape'] == ('DJ', 16, 16)
    # Band 1 Characteristic 3 Width_Shape
    assert verf_result[0]['B_1_Characteristic_3_Width_Shape'] == 'lorentzian'
    assert verf_result[1]['B_1_Characteristic_3_Width_Shape'] == ('DJ', 17, 17)
    # Band 1 Characteristic 4 Width_Shape
    assert verf_result[0]['B_1_Characteristic_4_Width_Shape'] == 'voigt'
    assert verf_result[1]['B_1_Characteristic_4_Width_Shape'] == ('DJ', 18, 18)
    # Band 1 Characteristic 5 Width_Shape
    assert verf_result[0]['B_1_Characteristic_5_Width_Shape'] == 'doppler'
    assert verf_result[1]['B_1_Characteristic_5_Width_Shape'] == ('DJ', 19, 19)
    # Band 1 Characteristic 6 Width_Shape
    assert verf_result[0]['B_1_Characteristic_6_Width_Shape'] == 'asymmetric'
    assert verf_result[1]['B_1_Characteristic_6_Width_Shape'] == ('DJ', 20, 20)
    # Band 1 Characteristic 7 Width_Shape
    assert verf_result[0]['B_1_Characteristic_7_Width_Shape'] == 'asymmetric low frequency wing'
    assert verf_result[1]['B_1_Characteristic_7_Width_Shape'] == ('DJ', 25, 25)
    # Band 1 Characteristic 8 Width_Shape
    assert verf_result[0]['B_1_Characteristic_8_Width_Shape'] == 'asymmetric high frequency wing'
    assert verf_result[1]['B_1_Characteristic_8_Width_Shape'] == ('DJ', 26, 26)
    # Band 1 Characteristic 9 Width_Shape
    assert verf_result[0]['B_1_Characteristic_9_Width_Shape'] == 'shoulder'
    assert verf_result[1]['B_1_Characteristic_9_Width_Shape'] == ('DJ', 31, 31)
    # Band 1 Characteristic 10 Width_Shape
    assert verf_result[0]['B_1_Characteristic_10_Width_Shape'] == 'sharp shoulder'
    assert verf_result[1]['B_1_Characteristic_10_Width_Shape'] == ('DJ', 32, 32)
    # Band 2 Characteristic 1 Width_Shape
    assert verf_result[0]['B_2_Characteristic_1_Width_Shape'] == 'broad shoulder'
    assert verf_result[1]['B_2_Characteristic_1_Width_Shape'] == ('DJ', 37, 37)
    # Band 2 Characteristic 2 Width_Shape
    assert verf_result[0]['B_2_Characteristic_2_Width_Shape'] == 'low frequency tail'
    assert verf_result[1]['B_2_Characteristic_2_Width_Shape'] == ('DJ', 38, 38)
    # Band 2 Characteristic 3 Width_Shape
    assert verf_result[0]['B_2_Characteristic_3_Width_Shape'] == 'undefined'
    assert verf_result[1]['B_2_Characteristic_3_Width_Shape'] == ('DJ', 41, 41)
    # Band 2 Characteristic 4 Width_Shape
    assert verf_result[0]['B_2_Characteristic_4_Width_Shape'] == ''
    assert verf_result[1]['B_2_Characteristic_4_Width_Shape'] == ('DJ', 45, 45)
    # Band 2 Characteristic 5 Width_Shape
    assert verf_result[0]['B_2_Characteristic_5_Width_Shape'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Width_Shape'] == ('DJ', 53, 53)
    # Band 3 Characteristic 1 Width_Shape
    assert verf_result[0]['B_3_Characteristic_1_Width_Shape'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Shape'] == ('DJ', 57, 57)
    # Band Characteristic Width_Asymm_factor
    # Band 1 Characteristic 1 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_1_Width_Asymm_factor'] == 'DK15'
    assert verf_result[1]['B_1_Characteristic_1_Width_Asymm_factor'] == ('DK', 15, 15)
    # Band 1 Characteristic 2 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_2_Width_Asymm_factor'] == 'DK16'
    assert verf_result[1]['B_1_Characteristic_2_Width_Asymm_factor'] == ('DK', 16, 16)
    # Band 1 Characteristic 3 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_3_Width_Asymm_factor'] == 'DK17'
    assert verf_result[1]['B_1_Characteristic_3_Width_Asymm_factor'] == ('DK', 17, 17)
    # Band 1 Characteristic 4 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_4_Width_Asymm_factor'] == 'DK18'
    assert verf_result[1]['B_1_Characteristic_4_Width_Asymm_factor'] == ('DK', 18, 18)
    # Band 1 Characteristic 5 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_5_Width_Asymm_factor'] == 'DK19'
    assert verf_result[1]['B_1_Characteristic_5_Width_Asymm_factor'] == ('DK', 19, 19)
    # Band 1 Characteristic 6 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_6_Width_Asymm_factor'] == 'DK20'
    assert verf_result[1]['B_1_Characteristic_6_Width_Asymm_factor'] == ('DK', 20, 20)
    # Band 1 Characteristic 7 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_7_Width_Asymm_factor'] == 'DK25'
    assert verf_result[1]['B_1_Characteristic_7_Width_Asymm_factor'] == ('DK', 25, 25)
    # Band 1 Characteristic 8 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_8_Width_Asymm_factor'] == 'DK26'
    assert verf_result[1]['B_1_Characteristic_8_Width_Asymm_factor'] == ('DK', 26, 26)
    # Band 1 Characteristic 9 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_9_Width_Asymm_factor'] == 'DK31'
    assert verf_result[1]['B_1_Characteristic_9_Width_Asymm_factor'] == ('DK', 31, 31)
    # Band 1 Characteristic 10 Width_Asymm_factor
    assert verf_result[0]['B_1_Characteristic_10_Width_Asymm_factor'] == 'DK32'
    assert verf_result[1]['B_1_Characteristic_10_Width_Asymm_factor'] == ('DK', 32, 32)
    # Band 2 Characteristic 1 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_1_Width_Asymm_factor'] == 'DK37'
    assert verf_result[1]['B_2_Characteristic_1_Width_Asymm_factor'] == ('DK', 37, 37)
    # Band 2 Characteristic 2 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_2_Width_Asymm_factor'] == 'DK38'
    assert verf_result[1]['B_2_Characteristic_2_Width_Asymm_factor'] == ('DK', 38, 38)
    # Band 2 Characteristic 3 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_3_Width_Asymm_factor'] == 'DK41'
    assert verf_result[1]['B_2_Characteristic_3_Width_Asymm_factor'] == ('DK', 41, 41)
    # Band 2 Characteristic 4 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_4_Width_Asymm_factor'] == 'DK45'
    assert verf_result[1]['B_2_Characteristic_4_Width_Asymm_factor'] == ('DK', 45, 45)
    # Band 2 Characteristic 5 Width_Asymm_factor
    assert verf_result[0]['B_2_Characteristic_5_Width_Asymm_factor'] == 'DK53'
    assert verf_result[1]['B_2_Characteristic_5_Width_Asymm_factor'] == ('DK', 53, 53)
    # Band 3 Characteristic 1 Width_Asymm_factor
    assert verf_result[0]['B_3_Characteristic_1_Width_Asymm_factor'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Asymm_factor'] == ('DK', 57, 57)
    # Band Characteristic Width_Asymm_factor_error
    # Band 1 Characteristic 1 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_1_Width_Asymm_factor_error'] == 'DL15'
    assert verf_result[1]['B_1_Characteristic_1_Width_Asymm_factor_error'] == ('DL', 15, 15)
    # Band 1 Characteristic 2 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_2_Width_Asymm_factor_error'] == 'DL16'
    assert verf_result[1]['B_1_Characteristic_2_Width_Asymm_factor_error'] == ('DL', 16, 16)
    # Band 1 Characteristic 3 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_3_Width_Asymm_factor_error'] == 'DL17'
    assert verf_result[1]['B_1_Characteristic_3_Width_Asymm_factor_error'] == ('DL', 17, 17)
    # Band 1 Characteristic 4 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_4_Width_Asymm_factor_error'] == 'DL18'
    assert verf_result[1]['B_1_Characteristic_4_Width_Asymm_factor_error'] == ('DL', 18, 18)
    # Band 1 Characteristic 5 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_5_Width_Asymm_factor_error'] == 'DL19'
    assert verf_result[1]['B_1_Characteristic_5_Width_Asymm_factor_error'] == ('DL', 19, 19)
    # Band 1 Characteristic 6 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_6_Width_Asymm_factor_error'] == 'DL20'
    assert verf_result[1]['B_1_Characteristic_6_Width_Asymm_factor_error'] == ('DL', 20, 20)
    # Band 1 Characteristic 7 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_7_Width_Asymm_factor_error'] == 'DL25'
    assert verf_result[1]['B_1_Characteristic_7_Width_Asymm_factor_error'] == ('DL', 25, 25)
    # Band 1 Characteristic 8 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_8_Width_Asymm_factor_error'] == 'DL26'
    assert verf_result[1]['B_1_Characteristic_8_Width_Asymm_factor_error'] == ('DL', 26, 26)
    # Band 1 Characteristic 9 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_9_Width_Asymm_factor_error'] == 'DL31'
    assert verf_result[1]['B_1_Characteristic_9_Width_Asymm_factor_error'] == ('DL', 31, 31)
    # Band 1 Characteristic 10 Width_Asymm_factor_error
    assert verf_result[0]['B_1_Characteristic_10_Width_Asymm_factor_error'] == 'DL32'
    assert verf_result[1]['B_1_Characteristic_10_Width_Asymm_factor_error'] == ('DL', 32, 32)
    # Band 2 Characteristic 1 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_1_Width_Asymm_factor_error'] == 'DL37'
    assert verf_result[1]['B_2_Characteristic_1_Width_Asymm_factor_error'] == ('DL', 37, 37)
    # Band 2 Characteristic 2 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_2_Width_Asymm_factor_error'] == 'DL38'
    assert verf_result[1]['B_2_Characteristic_2_Width_Asymm_factor_error'] == ('DL', 38, 38)
    # Band 2 Characteristic 3 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_3_Width_Asymm_factor_error'] == 'DL41'
    assert verf_result[1]['B_2_Characteristic_3_Width_Asymm_factor_error'] == ('DL', 41, 41)
    # Band 2 Characteristic 4 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_4_Width_Asymm_factor_error'] == 'DL45'
    assert verf_result[1]['B_2_Characteristic_4_Width_Asymm_factor_error'] == ('DL', 45, 45)
    # Band 2 Characteristic 5 Width_Asymm_factor_error
    assert verf_result[0]['B_2_Characteristic_5_Width_Asymm_factor_error'] == 'DL53'
    assert verf_result[1]['B_2_Characteristic_5_Width_Asymm_factor_error'] == ('DL', 53, 53)
    # Band 3 Characteristic 1 Width_Asymm_factor_error
    assert verf_result[0]['B_3_Characteristic_1_Width_Asymm_factor_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Asymm_factor_error'] == ('DL', 57, 57)
    # Band Characteristic Width_Evaluation
    # Band 1 Characteristic 1 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Width_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Width_Evaluation'] == ('DM', 15, 15)
    # Band 1 Characteristic 2 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Width_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Width_Evaluation'] == ('DM', 16, 16)
    # Band 1 Characteristic 3 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Width_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Width_Evaluation'] == ('DM', 17, 17)
    # Band 1 Characteristic 4 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Width_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Width_Evaluation'] == ('DM', 18, 18)
    # Band 1 Characteristic 5 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Width_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Width_Evaluation'] == ('DM', 19, 19)
    # Band 1 Characteristic 6 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Width_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Width_Evaluation'] == ('DM', 20, 20)
    # Band 1 Characteristic 7 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Width_Evaluation'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_7_Width_Evaluation'] == ('DM', 25, 25)
    # Band 1 Characteristic 8 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Width_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_8_Width_Evaluation'] == ('DM', 26, 26)
    # Band 1 Characteristic 9 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Width_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_9_Width_Evaluation'] == ('DM', 31, 31)
    # Band 1 Characteristic 10 Width_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Width_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Width_Evaluation'] == ('DM', 32, 32)
    # Band 2 Characteristic 1 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Width_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_1_Width_Evaluation'] == ('DM', 37, 37)
    # Band 2 Characteristic 2 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Width_Evaluation'] == 'with caution'
    assert verf_result[1]['B_2_Characteristic_2_Width_Evaluation'] == ('DM', 38, 38)
    # Band 2 Characteristic 3 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Width_Evaluation'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_3_Width_Evaluation'] == ('DM', 41, 41)
    # Band 2 Characteristic 4 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Width_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_4_Width_Evaluation'] == ('DM', 45, 45)
    # Band 2 Characteristic 5 Width_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Width_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Width_Evaluation'] == ('DM', 53, 53)
    # Band 3 Characteristic 1 Width_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Width_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Evaluation'] == ('DM', 57, 57)
    # Band Characteristic Width_Comments
    # Band 1 Characteristic 1 Width_Comments
    assert verf_result[0]['B_1_Characteristic_1_Width_Comments'] == 'DN15'
    assert verf_result[1]['B_1_Characteristic_1_Width_Comments'] == ('DN', 15, 15)
    # Band 1 Characteristic 2 Width_Comments
    assert verf_result[0]['B_1_Characteristic_2_Width_Comments'] == 'DN16'
    assert verf_result[1]['B_1_Characteristic_2_Width_Comments'] == ('DN', 16, 16)
    # Band 1 Characteristic 3 Width_Comments
    assert verf_result[0]['B_1_Characteristic_3_Width_Comments'] == 'DN17'
    assert verf_result[1]['B_1_Characteristic_3_Width_Comments'] == ('DN', 17, 17)
    # Band 1 Characteristic 4 Width_Comments
    assert verf_result[0]['B_1_Characteristic_4_Width_Comments'] == 'DN18'
    assert verf_result[1]['B_1_Characteristic_4_Width_Comments'] == ('DN', 18, 18)
    # Band 1 Characteristic 5 Width_Comments
    assert verf_result[0]['B_1_Characteristic_5_Width_Comments'] == 'DN19'
    assert verf_result[1]['B_1_Characteristic_5_Width_Comments'] == ('DN', 19, 19)
    # Band 1 Characteristic 6 Width_Comments
    assert verf_result[0]['B_1_Characteristic_6_Width_Comments'] == 'DN20'
    assert verf_result[1]['B_1_Characteristic_6_Width_Comments'] == ('DN', 20, 20)
    # Band 1 Characteristic 7 Width_Comments
    assert verf_result[0]['B_1_Characteristic_7_Width_Comments'] == 'DN25'
    assert verf_result[1]['B_1_Characteristic_7_Width_Comments'] == ('DN', 25, 25)
    # Band 1 Characteristic 8 Width_Comments
    assert verf_result[0]['B_1_Characteristic_8_Width_Comments'] == 'DN26'
    assert verf_result[1]['B_1_Characteristic_8_Width_Comments'] == ('DN', 26, 26)
    # Band 1 Characteristic 9 Width_Comments
    assert verf_result[0]['B_1_Characteristic_9_Width_Comments'] == 'DN31'
    assert verf_result[1]['B_1_Characteristic_9_Width_Comments'] == ('DN', 31, 31)
    # Band 1 Characteristic 10 Width_Comments
    assert verf_result[0]['B_1_Characteristic_10_Width_Comments'] == 'DN32'
    assert verf_result[1]['B_1_Characteristic_10_Width_Comments'] == ('DN', 32, 32)
    # Band 2 Characteristic 1 Width_Comments
    assert verf_result[0]['B_2_Characteristic_1_Width_Comments'] == 'DN37'
    assert verf_result[1]['B_2_Characteristic_1_Width_Comments'] == ('DN', 37, 37)
    # Band 2 Characteristic 2 Width_Comments
    assert verf_result[0]['B_2_Characteristic_2_Width_Comments'] == 'DN38'
    assert verf_result[1]['B_2_Characteristic_2_Width_Comments'] == ('DN', 38, 38)
    # Band 2 Characteristic 3 Width_Comments
    assert verf_result[0]['B_2_Characteristic_3_Width_Comments'] == 'DN41'
    assert verf_result[1]['B_2_Characteristic_3_Width_Comments'] == ('DN', 41, 41)
    # Band 2 Characteristic 4 Width_Comments
    assert verf_result[0]['B_2_Characteristic_4_Width_Comments'] == 'DN45'
    assert verf_result[1]['B_2_Characteristic_4_Width_Comments'] == ('DN', 45, 45)
    # Band 2 Characteristic 5 Width_Comments
    assert verf_result[0]['B_2_Characteristic_5_Width_Comments'] == 'DN53'
    assert verf_result[1]['B_2_Characteristic_5_Width_Comments'] == ('DN', 53, 53)
    # Band 3 Characteristic 1 Width_Comments
    assert verf_result[0]['B_3_Characteristic_1_Width_Comments'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Width_Comments'] == ('DN', 57, 57)
    # Band Characteristic Peak_intensity_Method
    # Band 1 Characteristic 1 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Method'] == 'baseline corrected peak intensity'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Method'] == ('DQ', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Method'] == 'peak intensity'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Method'] == ('DQ', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Method'] == 'fit intensity'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Method'] == ('DQ', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Method'] == ('DQ', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Method'] == ('DQ', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Method'] == ('DQ', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Method'] == ('DQ', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Method'] == 'other'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Method'] == ('DQ', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Method'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Method'] == ('DQ', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Method
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Method'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Method'] == ('DQ', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Method'] == 'baseline corrected peak intensity'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Method'] == ('DQ', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Method'] == 'other'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Method'] == ('DQ', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Method'] == 'various'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Method'] == ('DQ', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Method'] == 'calculated'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Method'] == ('DQ', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Method
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Method'] == ('DQ', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Method
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Method'] == ('DQ', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef'] == 'DR15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef'] == ('DR', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef'] == 'DR16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef'] == ('DR', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef'] == 'DR17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef'] == ('DR', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef'] == 'DR18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef'] == ('DR', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef'] == 'DR19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef'] == ('DR', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef'] == 'DR20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef'] == ('DR', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef'] == 'DR25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef'] == ('DR', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef'] == 'DR26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef'] == ('DR', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef'] == 'DR31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef'] == ('DR', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef'] == 'DR32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef'] == ('DR', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef'] == 'DR37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef'] == ('DR', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef'] == 'DR38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef'] == ('DR', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef'] == 'DR41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef'] == ('DR', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef'] == 'DR45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef'] == ('DR', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef'] == 'DR53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef'] == ('DR', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef'] == ('DR', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef_error
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef_error'] == 'DS15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef_error'] == ('DS', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef_error'] == 'DS16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef_error'] == ('DS', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef_error'] == 'DS17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef_error'] == ('DS', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef_error'] == 'DS18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef_error'] == ('DS', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef_error'] == 'DS19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef_error'] == ('DS', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef_error'] == 'DS20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef_error'] == ('DS', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef_error'] == 'DS25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef_error'] == ('DS', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef_error'] == 'DS26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef_error'] == ('DS', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef_error'] == 'DS31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef_error'] == ('DS', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef_error'] == 'DS32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef_error'] == ('DS', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef_error'] == 'DS37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef_error'] == ('DS', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef_error'] == 'DS38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef_error'] == ('DS', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef_error'] == 'DS41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef_error'] == ('DS', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef_error'] == 'DS45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef_error'] == ('DS', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef_error'] == 'DS53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef_error'] == ('DS', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef_error
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef_error'] == ('DS', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef_sp
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp'] == 'DT15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ('DT', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp'] == 'DT16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp'] == ('DT', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp'] == 'DT17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp'] == ('DT', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp'] == 'DT18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp'] == ('DT', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp'] == 'DT19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp'] == ('DT', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp'] == 'DT20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp'] == ('DT', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp'] == 'DT25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp'] == ('DT', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp'] == 'DT26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp'] == ('DT', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp'] == 'DT31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp'] == ('DT', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp'] == 'DT32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp'] == ('DT', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp'] == 'DT37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ('DT', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp'] == 'DT38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp'] == ('DT', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp'] == 'DT41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp'] == ('DT', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp'] == 'DT45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp'] == ('DT', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp'] == 'DT53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp'] == ('DT', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef_sp
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp'] == ('DT', 57, 57)
    # Band Characteristic Peak_intensity_Abs_coef_sp_error
    # Band 1 Characteristic 1 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == 'DU15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ('DU', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == 'DU16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == ('DU', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == 'DU17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == ('DU', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == 'DU18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == ('DU', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == 'DU19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == ('DU', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp_error'] == 'DU20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Abs_coef_sp_error'] == ('DU', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp_error'] == 'DU25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Abs_coef_sp_error'] == ('DU', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp_error'] == 'DU26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Abs_coef_sp_error'] == ('DU', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp_error'] == 'DU31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Abs_coef_sp_error'] == ('DU', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp_error'] == 'DU32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Abs_coef_sp_error'] == ('DU', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == 'DU37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ('DU', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == 'DU38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Abs_coef_sp_error'] == ('DU', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == 'DU41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Abs_coef_sp_error'] == ('DU', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == 'DU45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Abs_coef_sp_error'] == ('DU', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == 'DU53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Abs_coef_sp_error'] == ('DU', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Abs_coef_sp_error'] == ('DU', 57, 57)
    # Band Characteristic Peak_intensity_Relative
    # Band 1 Characteristic 1 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Relative'] == 'DV15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Relative'] == ('DV', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Relative'] == 'DV16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Relative'] == ('DV', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Relative'] == 'DV17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Relative'] == ('DV', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Relative'] == 'DV18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Relative'] == ('DV', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Relative'] == 'DV19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Relative'] == ('DV', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Relative'] == 'DV20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Relative'] == ('DV', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Relative'] == 'DV25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Relative'] == ('DV', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Relative'] == 'DV26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Relative'] == ('DV', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Relative'] == 'DV31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Relative'] == ('DV', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Relative'] == 'DV32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Relative'] == ('DV', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Relative'] == 'DV37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Relative'] == ('DV', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Relative'] == 'DV38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Relative'] == ('DV', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Relative'] == 'DV41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Relative'] == ('DV', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Relative'] == 'DV45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Relative'] == ('DV', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Relative'] == 'DV53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Relative'] == ('DV', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Relative
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Relative'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Relative'] == ('DV', 57, 57)
    # Band Characteristic Peak_intensity_Relative_error
    # Band 1 Characteristic 1 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Relative_error'] == 'DW15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Relative_error'] == ('DW', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Relative_error'] == 'DW16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Relative_error'] == ('DW', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Relative_error'] == 'DW17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Relative_error'] == ('DW', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Relative_error'] == 'DW18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Relative_error'] == ('DW', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Relative_error'] == 'DW19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Relative_error'] == ('DW', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Relative_error'] == 'DW20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Relative_error'] == ('DW', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Relative_error'] == 'DW25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Relative_error'] == ('DW', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Relative_error'] == 'DW26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Relative_error'] == ('DW', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Relative_error'] == 'DW31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Relative_error'] == ('DW', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Relative_error'] == 'DW32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Relative_error'] == ('DW', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Relative_error'] == 'DW37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Relative_error'] == ('DW', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Relative_error'] == 'DW38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Relative_error'] == ('DW', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Relative_error'] == 'DW41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Relative_error'] == ('DW', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Relative_error'] == 'DW45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Relative_error'] == ('DW', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Relative_error'] == 'DW53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Relative_error'] == ('DW', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Relative_error
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Relative_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Relative_error'] == ('DW', 57, 57)
    # Band Characteristic Peak_intensity_Strength
    # Band 1 Characteristic 1 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Strength'] == 'ia'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Strength'] == ('DX', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Strength'] == 'ew'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Strength'] == ('DX', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Strength'] == 'vvw'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Strength'] == ('DX', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Strength'] == 'vw'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Strength'] == ('DX', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Strength'] == 'w'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Strength'] == ('DX', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Strength'] == 'm'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Strength'] == ('DX', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Strength'] == 's'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Strength'] == ('DX', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Strength'] == 'vs'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Strength'] == ('DX', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Strength'] == 'vvs'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Strength'] == ('DX', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Strength'] == 'es'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Strength'] == ('DX', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Strength'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Strength'] == ('DX', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Strength'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Strength'] == ('DX', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Strength'] == ('DX', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Strength'] == 'w'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Strength'] == ('DX', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Strength'] == ('DX', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Strength
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Strength'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Strength'] == ('DX', 57, 57)
    # Band Characteristic Peak_intensity_Evaluation
    # Band 1 Characteristic 1 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Evaluation'] == ('EA', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Evaluation'] == ('EA', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Evaluation'] == ('EA', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Evaluation'] == ('EA', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Evaluation'] == ('EA', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Evaluation'] == ('EA', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Evaluation'] == ('EA', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Evaluation'] == ('EA', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Evaluation'] == ('EA', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Evaluation'] == ('EA', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Evaluation'] == ('EA', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Evaluation'] == ('EA', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Evaluation'] == ('EA', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Evaluation'] == ('EA', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Evaluation'] == ('EA', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Evaluation'] == ('EA', 57, 57)
    # Band Characteristic Peak_intensity_Comment
    # Band 1 Characteristic 1 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_1_Peak_intensity_Comment'] == 'EB15'
    assert verf_result[1]['B_1_Characteristic_1_Peak_intensity_Comment'] == ('EB', 15, 15)
    # Band 1 Characteristic 2 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_2_Peak_intensity_Comment'] == 'EB16'
    assert verf_result[1]['B_1_Characteristic_2_Peak_intensity_Comment'] == ('EB', 16, 16)
    # Band 1 Characteristic 3 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_3_Peak_intensity_Comment'] == 'EB17'
    assert verf_result[1]['B_1_Characteristic_3_Peak_intensity_Comment'] == ('EB', 17, 17)
    # Band 1 Characteristic 4 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_4_Peak_intensity_Comment'] == 'EB18'
    assert verf_result[1]['B_1_Characteristic_4_Peak_intensity_Comment'] == ('EB', 18, 18)
    # Band 1 Characteristic 5 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_5_Peak_intensity_Comment'] == 'EB19'
    assert verf_result[1]['B_1_Characteristic_5_Peak_intensity_Comment'] == ('EB', 19, 19)
    # Band 1 Characteristic 6 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_6_Peak_intensity_Comment'] == 'EB20'
    assert verf_result[1]['B_1_Characteristic_6_Peak_intensity_Comment'] == ('EB', 20, 20)
    # Band 1 Characteristic 7 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_7_Peak_intensity_Comment'] == 'EB25'
    assert verf_result[1]['B_1_Characteristic_7_Peak_intensity_Comment'] == ('EB', 25, 25)
    # Band 1 Characteristic 8 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_8_Peak_intensity_Comment'] == 'EB26'
    assert verf_result[1]['B_1_Characteristic_8_Peak_intensity_Comment'] == ('EB', 26, 26)
    # Band 1 Characteristic 9 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_9_Peak_intensity_Comment'] == 'EB31'
    assert verf_result[1]['B_1_Characteristic_9_Peak_intensity_Comment'] == ('EB', 31, 31)
    # Band 1 Characteristic 10 Peak_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_10_Peak_intensity_Comment'] == 'EB32'
    assert verf_result[1]['B_1_Characteristic_10_Peak_intensity_Comment'] == ('EB', 32, 32)
    # Band 2 Characteristic 1 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_1_Peak_intensity_Comment'] == 'EB37'
    assert verf_result[1]['B_2_Characteristic_1_Peak_intensity_Comment'] == ('EB', 37, 37)
    # Band 2 Characteristic 2 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_2_Peak_intensity_Comment'] == 'EB38'
    assert verf_result[1]['B_2_Characteristic_2_Peak_intensity_Comment'] == ('EB', 38, 38)
    # Band 2 Characteristic 3 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_3_Peak_intensity_Comment'] == 'EB41'
    assert verf_result[1]['B_2_Characteristic_3_Peak_intensity_Comment'] == ('EB', 41, 41)
    # Band 2 Characteristic 4 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_4_Peak_intensity_Comment'] == 'EB45'
    assert verf_result[1]['B_2_Characteristic_4_Peak_intensity_Comment'] == ('EB', 45, 45)
    # Band 2 Characteristic 5 Peak_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_5_Peak_intensity_Comment'] == 'EB53'
    assert verf_result[1]['B_2_Characteristic_5_Peak_intensity_Comment'] == ('EB', 53, 53)
    # Band 3 Characteristic 1 Peak_intensity_Comment
    assert verf_result[0]['B_3_Characteristic_1_Peak_intensity_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Peak_intensity_Comment'] == ('EB', 57, 57)
    # Band Characteristic Integrated_intensity_Method
    # Band 1 Characteristic 1 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Method'] == 'band integrated intensity'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Method'] == ('EE', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Method'] == 'width x peak intensity'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Method'] == ('EE', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Method'] == 'fit integrated intensity'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Method'] == ('EE', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Method'] == 'extrapolated'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Method'] == ('EE', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Method'] == 'calculated'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Method'] == ('EE', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Method'] == 'estimated'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Method'] == ('EE', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Method'] == 'various'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Method'] == ('EE', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Method'] == 'other'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Method'] == ('EE', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Method'] == 'unknown'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Method'] == ('EE', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Method
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Method'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Method'] == ('EE', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Method'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Method'] == ('EE', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Method'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Method'] == ('EE', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Method'] == 'band integrated intensity'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Method'] == ('EE', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Method'] == 'fit integrated intensity'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Method'] == ('EE', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Method
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Method'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Method'] == ('EE', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Method
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Method'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Method'] == ('EE', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef'] == 'EF15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef'] == ('EF', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef'] == 'EF16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef'] == ('EF', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef'] == 'EF17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef'] == ('EF', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef'] == 'EF18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef'] == ('EF', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef'] == 'EF19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef'] == ('EF', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef'] == 'EF20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef'] == ('EF', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef'] == 'EF25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef'] == ('EF', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef'] == 'EF26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef'] == ('EF', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef'] == 'EF31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef'] == ('EF', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef'] == 'EF32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef'] == ('EF', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef'] == 'EF37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef'] == ('EF', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef'] == 'EF38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef'] == ('EF', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef'] == 'EF41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef'] == ('EF', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef'] == 'EF45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef'] == ('EF', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef'] == 'EF53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef'] == ('EF', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef'] == ('EF', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef_error
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_error'] == 'EG15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ('EG', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_error'] == 'EG16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_error'] == ('EG', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_error'] == 'EG17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_error'] == ('EG', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_error'] == 'EG18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_error'] == ('EG', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_error'] == 'EG19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_error'] == ('EG', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_error'] == 'EG20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_error'] == ('EG', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_error'] == 'EG25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_error'] == ('EG', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_error'] == 'EG26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_error'] == ('EG', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_error'] == 'EG31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_error'] == ('EG', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_error'] == 'EG32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_error'] == ('EG', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_error'] == 'EG37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ('EG', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_error'] == 'EG38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_error'] == ('EG', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_error'] == 'EG41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_error'] == ('EG', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_error'] == 'EG45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_error'] == ('EG', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_error'] == 'EG53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_error'] == ('EG', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef_error
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_error'] == ('EG', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef_sp
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == 'EH15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ('EH', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == 'EH16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == ('EH', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == 'EH17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == ('EH', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == 'EH18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == ('EH', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == 'EH19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == ('EH', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp'] == 'EH20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp'] == ('EH', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp'] == 'EH25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp'] == ('EH', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp'] == 'EH26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp'] == ('EH', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp'] == 'EH31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp'] == ('EH', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp'] == 'EH32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp'] == ('EH', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == 'EH37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ('EH', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == 'EH38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp'] == ('EH', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == 'EH41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp'] == ('EH', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == 'EH45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp'] == ('EH', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == 'EH53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp'] == ('EH', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef_sp
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp'] == ('EH', 57, 57)
    # Band Characteristic Integrated_intensity_Abs_coef_sp_error
    # Band 1 Characteristic 1 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == 'EI15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == 'EI16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == 'EI17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == 'EI18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == 'EI19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp_error'] == 'EI20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp_error'] == 'EI25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp_error'] == 'EI26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp_error'] == 'EI31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp_error'] == 'EI32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == 'EI37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == 'EI38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == 'EI41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == 'EI45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == 'EI53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Abs_coef_sp_error
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Abs_coef_sp_error'] == ('EI', 57, 57)
    # Band Characteristic Integrated_intensity_Relative
    # Band 1 Characteristic 1 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Relative'] == 'EJ15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Relative'] == ('EJ', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Relative'] == 'EJ16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Relative'] == ('EJ', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Relative'] == 'EJ17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Relative'] == ('EJ', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Relative'] == 'EJ18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Relative'] == ('EJ', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Relative'] == 'EJ19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Relative'] == ('EJ', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Relative'] == 'EJ20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Relative'] == ('EJ', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Relative'] == 'EJ25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Relative'] == ('EJ', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Relative'] == 'EJ26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Relative'] == ('EJ', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Relative'] == 'EJ31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Relative'] == ('EJ', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Relative
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Relative'] == 'EJ32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Relative'] == ('EJ', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Relative'] == 'EJ37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Relative'] == ('EJ', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Relative'] == 'EJ38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Relative'] == ('EJ', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Relative'] == 'EJ41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Relative'] == ('EJ', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Relative'] == 'EJ45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Relative'] == ('EJ', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Relative
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Relative'] == 'EJ53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Relative'] == ('EJ', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Relative
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Relative'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Relative'] == ('EJ', 57, 57)
    # Band Characteristic Integrated_intensity_Relative_error
    # Band 1 Characteristic 1 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Relative_error'] == 'EK15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Relative_error'] == ('EK', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Relative_error'] == 'EK16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Relative_error'] == ('EK', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Relative_error'] == 'EK17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Relative_error'] == ('EK', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Relative_error'] == 'EK18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Relative_error'] == ('EK', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Relative_error'] == 'EK19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Relative_error'] == ('EK', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Relative_error'] == 'EK20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Relative_error'] == ('EK', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Relative_error'] == 'EK25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Relative_error'] == ('EK', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Relative_error'] == 'EK26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Relative_error'] == ('EK', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Relative_error'] == 'EK31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Relative_error'] == ('EK', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Relative_error
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Relative_error'] == 'EK32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Relative_error'] == ('EK', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Relative_error'] == 'EK37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Relative_error'] == ('EK', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Relative_error'] == 'EK38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Relative_error'] == ('EK', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Relative_error'] == 'EK41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Relative_error'] == ('EK', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Relative_error'] == 'EK45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Relative_error'] == ('EK', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Relative_error
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Relative_error'] == 'EK53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Relative_error'] == ('EK', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Relative_error
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Relative_error'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Relative_error'] == ('EK', 57, 57)
    # Band Characteristic Integrated_intensity_Strength
    # Band 1 Characteristic 1 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Strength'] == 'ia'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Strength'] == ('EL', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Strength'] == 'ew'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Strength'] == ('EL', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Strength'] == 'vvw'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Strength'] == ('EL', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Strength'] == 'vw'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Strength'] == ('EL', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Strength'] == 'w'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Strength'] == ('EL', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Strength'] == 'm'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Strength'] == ('EL', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Strength'] == 's'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Strength'] == ('EL', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Strength'] == 'vs'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Strength'] == ('EL', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Strength'] == 'vvs'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Strength'] == ('EL', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Strength
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Strength'] == 'es'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Strength'] == ('EL', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Strength'] == 'unknown'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Strength'] == ('EL', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Strength'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Strength'] == ('EL', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Strength'] == ('EL', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Strength'] == 'w'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Strength'] == ('EL', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Strength
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Strength'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Strength'] == ('EL', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Strength
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Strength'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Strength'] == ('EL', 57, 57)
    # Band Characteristic Integrated_intensity_Evaluation
    # Band 1 Characteristic 1 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Evaluation'] == 'undefined'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Evaluation'] == ('EO', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Evaluation'] == ('EO', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Evaluation'] == 'validated'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Evaluation'] == ('EO', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Evaluation'] == ('EO', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Evaluation'] == 'with caution'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Evaluation'] == ('EO', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Evaluation'] == ('EO', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Evaluation'] == ('EO', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Evaluation'] == ('EO', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Evaluation'] == ('EO', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Evaluation
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Evaluation'] == 'not recommended'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Evaluation'] == ('EO', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Evaluation'] == 'uncertain'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Evaluation'] == ('EO', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Evaluation'] == 'NULL'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Evaluation'] == ('EO', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Evaluation'] == ('EO', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Evaluation'] == 'recommended'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Evaluation'] == ('EO', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Evaluation
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Evaluation'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Evaluation'] == ('EO', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Evaluation
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Evaluation'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Evaluation'] == ('EO', 57, 57)
    # Band Characteristic Integrated_intensity_Comment
    # Band 1 Characteristic 1 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_1_Integrated_intensity_Comment'] == 'EP15'
    assert verf_result[1]['B_1_Characteristic_1_Integrated_intensity_Comment'] == ('EP', 15, 15)
    # Band 1 Characteristic 2 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_2_Integrated_intensity_Comment'] == 'EP16'
    assert verf_result[1]['B_1_Characteristic_2_Integrated_intensity_Comment'] == ('EP', 16, 16)
    # Band 1 Characteristic 3 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_3_Integrated_intensity_Comment'] == 'EP17'
    assert verf_result[1]['B_1_Characteristic_3_Integrated_intensity_Comment'] == ('EP', 17, 17)
    # Band 1 Characteristic 4 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_4_Integrated_intensity_Comment'] == 'EP18'
    assert verf_result[1]['B_1_Characteristic_4_Integrated_intensity_Comment'] == ('EP', 18, 18)
    # Band 1 Characteristic 5 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_5_Integrated_intensity_Comment'] == 'EP19'
    assert verf_result[1]['B_1_Characteristic_5_Integrated_intensity_Comment'] == ('EP', 19, 19)
    # Band 1 Characteristic 6 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_6_Integrated_intensity_Comment'] == 'EP20'
    assert verf_result[1]['B_1_Characteristic_6_Integrated_intensity_Comment'] == ('EP', 20, 20)
    # Band 1 Characteristic 7 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_7_Integrated_intensity_Comment'] == 'EP25'
    assert verf_result[1]['B_1_Characteristic_7_Integrated_intensity_Comment'] == ('EP', 25, 25)
    # Band 1 Characteristic 8 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_8_Integrated_intensity_Comment'] == 'EP26'
    assert verf_result[1]['B_1_Characteristic_8_Integrated_intensity_Comment'] == ('EP', 26, 26)
    # Band 1 Characteristic 9 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_9_Integrated_intensity_Comment'] == 'EP31'
    assert verf_result[1]['B_1_Characteristic_9_Integrated_intensity_Comment'] == ('EP', 31, 31)
    # Band 1 Characteristic 10 Integrated_intensity_Comment
    assert verf_result[0]['B_1_Characteristic_10_Integrated_intensity_Comment'] == 'EP32'
    assert verf_result[1]['B_1_Characteristic_10_Integrated_intensity_Comment'] == ('EP', 32, 32)
    # Band 2 Characteristic 1 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_1_Integrated_intensity_Comment'] == 'EP37'
    assert verf_result[1]['B_2_Characteristic_1_Integrated_intensity_Comment'] == ('EP', 37, 37)
    # Band 2 Characteristic 2 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_2_Integrated_intensity_Comment'] == 'EP38'
    assert verf_result[1]['B_2_Characteristic_2_Integrated_intensity_Comment'] == ('EP', 38, 38)
    # Band 2 Characteristic 3 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_3_Integrated_intensity_Comment'] == 'EP41'
    assert verf_result[1]['B_2_Characteristic_3_Integrated_intensity_Comment'] == ('EP', 41, 41)
    # Band 2 Characteristic 4 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_4_Integrated_intensity_Comment'] == 'EP45'
    assert verf_result[1]['B_2_Characteristic_4_Integrated_intensity_Comment'] == ('EP', 45, 45)
    # Band 2 Characteristic 5 Integrated_intensity_Comment
    assert verf_result[0]['B_2_Characteristic_5_Integrated_intensity_Comment'] == 'EP53'
    assert verf_result[1]['B_2_Characteristic_5_Integrated_intensity_Comment'] == ('EP', 53, 53)
    # Band 3 Characteristic 1 Integrated_intensity_Comment
    assert verf_result[0]['B_3_Characteristic_1_Integrated_intensity_Comment'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Integrated_intensity_Comment'] == ('EP', 57, 57)
    # Band Characteristic Bandlist_flag
    # Band 1 Characteristic 1 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_1_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_1_Bandlist_flag'] == ('ES', 15, 15)
    # Band 1 Characteristic 2 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_2_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_2_Bandlist_flag'] == ('ES', 16, 16)
    # Band 1 Characteristic 3 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_3_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_3_Bandlist_flag'] == ('ES', 17, 17)
    # Band 1 Characteristic 4 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_4_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_4_Bandlist_flag'] == ('ES', 18, 18)
    # Band 1 Characteristic 5 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_5_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_5_Bandlist_flag'] == ('ES', 19, 19)
    # Band 1 Characteristic 6 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_6_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_6_Bandlist_flag'] == ('ES', 20, 20)
    # Band 1 Characteristic 7 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_7_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_7_Bandlist_flag'] == ('ES', 25, 25)
    # Band 1 Characteristic 8 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_8_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_8_Bandlist_flag'] == ('ES', 26, 26)
    # Band 1 Characteristic 9 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_9_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_1_Characteristic_9_Bandlist_flag'] == ('ES', 31, 31)
    # Band 1 Characteristic 10 Bandlist_flag
    assert verf_result[0]['B_1_Characteristic_10_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_1_Characteristic_10_Bandlist_flag'] == ('ES', 32, 32)
    # Band 2 Characteristic 1 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_1_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_2_Characteristic_1_Bandlist_flag'] == ('ES', 37, 37)
    # Band 2 Characteristic 2 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_2_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_2_Characteristic_2_Bandlist_flag'] == ('ES', 38, 38)
    # Band 2 Characteristic 3 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_3_Bandlist_flag'] == 'yes'
    assert verf_result[1]['B_2_Characteristic_3_Bandlist_flag'] == ('ES', 41, 41)
    # Band 2 Characteristic 4 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_4_Bandlist_flag'] == 'no'
    assert verf_result[1]['B_2_Characteristic_4_Bandlist_flag'] == ('ES', 45, 45)
    # Band 2 Characteristic 5 Bandlist_flag
    assert verf_result[0]['B_2_Characteristic_5_Bandlist_flag'] == ''
    assert verf_result[1]['B_2_Characteristic_5_Bandlist_flag'] == ('ES', 53, 53)
    # Band 3 Characteristic 1 Bandlist_flag
    assert verf_result[0]['B_3_Characteristic_1_Bandlist_flag'] == ''
    assert verf_result[1]['B_3_Characteristic_1_Bandlist_flag'] == ('ES', 57, 57)


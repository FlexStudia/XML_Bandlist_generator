# coding: utf-8

# IMPORTS
import filecmp
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import XMLGenerator_Bandlist_core


# GLOBALS

# full-file tests: full files
# ABS
def test_ABS_test():
    # set_up
    xlsx_workbook = "xlsx/bandlist_ABS_test_v092a.xlsx"
    bandlist_type = "ABS"
    # verification
    verification_result = XMLGenerator_Bandlist_core.verification_F(xlsx_workbook, bandlist_type)
    assert verification_result == ""
    # fill
    str_to_upload = XMLGenerator_Bandlist_core.XML_filler(xlsx_workbook, bandlist_type)[0]
    # xml file saving
    file_name = f"bandlist.xml"
    if file_name:
        with open(file_name, 'wb') as file_output:
            file_output.write(str_to_upload)
    data_result = filecmp.cmp("bandlist.xml", "xml/bandlist_ABS_test_v092a.xml")
    assert data_result == True


def test_ABS_void():
    # set_up
    xlsx_workbook = "xlsx/bandlist_ABS_void_v092a.xlsx"
    bandlist_type = "ABS"
    # verification
    verification_result = XMLGenerator_Bandlist_core.verification_F(xlsx_workbook, bandlist_type)
    verification_result = verification_result.replace("ABS_MANDATORY list:", "")
    verification_result = verification_result.replace("- <bands><characteristics><position><peak_error>: Band_1, characteristic_1, NULL in ABS_M in CY21", "")
    verification_result = verification_result.replace("- <bands><characteristics><position><center_error>: Band_2, characteristic_1, NULL in ABS_M in DB23", "")
    verification_result = verification_result.replace("MANDATORY list:", "")
    verification_result = verification_result.replace("- <bands><characteristics><width><shape>: Band_1, characteristic_1, DJ21", "")
    verification_result = verification_result.replace("- <bands><characteristics><peak_intensity><abscoef>: Band_1, characteristic_1, DR21", "")
    verification_result = verification_result.replace("- <bands><publications>: Band_2, BH22-23", "")
    verification_result = verification_result.replace("- <bands><assignments><transition><rotation_modes><label>: Band_2, assignment_1: no label", "")
    verification_result = verification_result.replace("- <bands><characteristics><width><shape>: Band_2, characteristic_1, DJ23", "")
    verification_result = verification_result.replace("- <bands><characteristics><peak_intensity><abscoef>: Band_2, characteristic_1, DR23", "")
    verification_result = verification_result.replace("OUBLIETTES list:", "")
    verification_result = verification_result.replace("- <original_data_filename>: C12 value doesn't correspond to this xlsx file name", "")
    assert verification_result.strip() == ""
    # fill
    str_to_upload = XMLGenerator_Bandlist_core.XML_filler(xlsx_workbook, bandlist_type)[0]
    # xml file saving
    file_name = f"bandlist.xml"
    if file_name:
        with open(file_name, 'wb') as file_output:
            file_output.write(str_to_upload)
    data_result = filecmp.cmp("bandlist.xml", "xml/bandlist_ABS_void_v092a.xml")
    assert data_result == True


# RAMAN
def test_RAMAN_example():
    # set_up
    xlsx_workbook = "xlsx/bandlist_ABS_Raman_test_v092a.xlsx"
    bandlist_type = "RAMAN"
    # verification
    verification_result = XMLGenerator_Bandlist_core.verification_F(xlsx_workbook, bandlist_type)
    assert verification_result == ""
    # fill
    str_to_upload = XMLGenerator_Bandlist_core.XML_filler(xlsx_workbook, bandlist_type)[0]
    # xml file saving
    file_name = f"bandlist.xml"
    if file_name:
        with open(file_name, 'wb') as file_output:
            file_output.write(str_to_upload)
    data_result = filecmp.cmp("bandlist.xml", "xml/bandlist_ABS_Raman_test_v092a.xml")
    assert data_result == True


def test_RAMAN_full():
    # set_up
    xlsx_workbook = "xlsx/bandlist_ABS_Raman_full_v092a.xlsx"
    bandlist_type = "RAMAN"
    # verification
    verification_result = XMLGenerator_Bandlist_core.verification_F(xlsx_workbook, bandlist_type)
    assert verification_result == ""
    # fill
    str_to_upload = XMLGenerator_Bandlist_core.XML_filler(xlsx_workbook, bandlist_type)[0]
    # xml file saving
    file_name = f"bandlist.xml"
    if file_name:
        with open(file_name, 'wb') as file_output:
            file_output.write(str_to_upload)
    data_result = filecmp.cmp("bandlist.xml", "xml/bandlist_ABS_Raman_full_v092a.xml")
    assert data_result == True


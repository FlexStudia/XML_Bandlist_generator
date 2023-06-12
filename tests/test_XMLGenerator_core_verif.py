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


# GLOBALS

# TESTS: verification_F
# Bandlist
# <original_data_filename>  doesn't correspond to this xlsx file name
def test_verifications_original_data_filename():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/original_data_filename.xlsx", "ABS")
    assert "- <original_data_filename>: C12 value doesn't correspond to this xlsx file name" in verf_result
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/original_data_filename_correct.xlsx", "ABS")
    assert "- <original_data_filename>: C12 value doesn't correspond to this xlsx file name" not in verf_result

# <structure><sections variable_parameter>
def test_verifications_sections_var_param():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/sections_var_param.xlsx", "ABS")
    assert '<structure><sections variable_parameter>: BandList, sections, C64' in verf_result


# no section and subsection UIDs in Band UIDs
def test_verifications_section_and_subsections_no_UIDs():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/section_and_subsections_no_UIDs.xlsx", "ABS")
    assert 'Section_1, no band UID for Section Band UID 94' in verf_result
    assert 'Section_3, sub_section_1, no band UID for Section Band UID 3139' in verf_result


# more than one section and subsection UIDs in Band UIDs
def test_verifications_section_and_subsections_more_UIDs():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/section_and_subsections_more_UIDs.xlsx", "ABS")
    assert 'Section_1, no band UID for Section Band UID 94' in verf_result


# Band
# Band type = "new version" are not in "oubliettes"
def test_verifications_new_version_accepted():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/new_version_accepted.xlsx", "ABS")
    assert 'Section_1, no band UID for Section Band UID 94' in verf_result


# <bands><assignments>: no assignment found
def test_verifications_no_bands_assignment():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/no_bands_assignment.xlsx", "ABS")
    assert '<bands><assignments>: Band_3, No assignment found in H31' in verf_result


# <bands><characteristics><excitation><laser_wavelength>: mandatory for Raman
def test_verifications_laser_wavelength_Raman():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/laser_wavelength_Raman.xlsx", "RAMAN")
    assert '<bands><characteristics><excitation><laser_wavelength>: Band_12, characteristic_1, CG44' in verf_result


# <bands><characteristics><excitation><laser_wavelength>: must be "" for Absorption
def test_verifications_laser_wavelength_ABS():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/laser_wavelength_ABS.xlsx", "ABS")
    assert "<bands><characteristics><excitation><laser_wavelength>: Band_13, non-empty value when bandlist_type is 'absorption'" in verf_result


# <bands><characteristics><excitation><sample_orientation_mode>: mandatory for Raman
def test_verifications_excitation_sample_orientation_mode():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/excitation_sample_orientation_mode.xlsx", "RAMAN")
    assert "<bands><characteristics><excitation><sample_orientation_mode>: Band_13, characteristic_1, CH50" in verf_result


# <bands><characteristics><excitation><sample_orientation>: mandatory for Raman if <sample_orientation_mode> == "oriented"
def test_verifications_excitation_sample_orientation():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/excitation_sample_orientation.xlsx", "RAMAN")
    assert "<bands><characteristics><excitation><sample_orientation>: Band_14, characteristic_2, CI57" in verf_result


# <bands><characteristics><excitation><polarization_orientation_mode>: mandatory for Raman and absorption if <sample_orientation_mode> == "oriented"
def test_verifications_excitation_polarization_orientation_mode():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/excitation_polarization_orientation_mode.xlsx", "RAMAN")
    assert "<bands><characteristics><excitation><polarization_orientation_mode>: Band_14, characteristic_1, CJ56" in verf_result
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/excitation_polarization_orientation_mode.xlsx", "ABS")
    assert "<bands><characteristics><excitation><polarization_orientation_mode>: Band_15, characteristic_2, CJ65" in verf_result


# <bands><characteristics><excitation><polarization_orientation>: mandatory if <polarization_orientation_mode> == "polarized"
def test_verifications_excitation_polarization_orientation():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/excitation_polarization_orientation.xlsx", "RAMAN")
    assert "<bands><characteristics><excitation><polarization_orientation>: Band_12, characteristic_2, CK45" in verf_result
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/excitation_polarization_orientation.xlsx", "ABS")
    assert "<bands><characteristics><excitation><polarization_orientation>: Band_16, characteristic_1, CK70" in verf_result


# <bands><characteristics><width><asymmetry_factor>: mandatory for <shape> 'asymmetric', 'asymmetric low frequency wing', 'asymmetric high frequency wing'
def test_verifications_width_asymmetry_factor():
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/width_asymmetry_factor.xlsx", "RAMAN")
    assert "<bands><characteristics><width><asymmetry_factor>: Band_3, characteristic_1, DK31" in verf_result # asymmetric
    assert "<bands><characteristics><width><asymmetry_factor>: Band_11, characteristic_2, DK39" in verf_result # asymmetric low frequency wing
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/part/width_asymmetry_factor.xlsx", "ABS")
    assert "<bands><characteristics><width><asymmetry_factor>: Band_25, characteristic_1, DK123" in verf_result # asymmetric high frequency wing


def test_verification_bandlist_general_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_general.xlsx", "RAMAN")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # no other errors
    verf_result = verf_result.replace('- <structure><sections><band_uid>: BandList, section_1: no band_uid', '')
    verf_result = verf_result.replace('- <bands><import_mode>: Band_1: no import_mode', '')
    verf_result = verf_result.replace('- <bands><uid>: Band_1: no uid', '')
    verf_result = verf_result.replace('- <bands><assignments>: Band_1, No assignment found in', '')
    verf_result = verf_result.replace('- <bands><characteristics>: Band_1, No characteristic found', '')
    verf_result = verf_result.replace('MANDATORY list:', '')
    verf_result = verf_result.replace('- <structure><sections variable_parameter>: BandList, sections, C64', '')
    verf_result = verf_result.replace('- <structure><sections><section>: BandList, sections: no section', '')
    verf_result = verf_result.replace('- <structure><sections><title>: BandList, section_1, B67', '')
    verf_result = verf_result.replace('- <bands><publications>: Band_1: no publications', '')
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <structure><section><bands>: Section_1, no band UID for Section Band UID NULL', '')
    verf_result = verf_result.replace('- <bands><band><uid>: Band_1, no Band UID in BandList structure', '')
    # import_mode
    str_verif = '- <import_mode>: BandList, C3'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # type
    str_verif = '- <type>: BandList, C4'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # title
    str_verif = '- <title>: BandList, C5'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # export_filename
    str_verif = '- <export_filename>: BandList, C13'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # uid
    str_verif = '- <uid>: BandList, A17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # constituent uid
    str_verif = '- <constituent><uid>: BandList, B17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # constituent primary_specie_uid
    str_verif = '- <constituent><primary_specie_uid>: BandList, C17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral unit
    str_verif = '- <parameters_spectral><unit>: BandList, A34'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral standard
    str_verif = '- <parameters_spectral><standard>: BandList, B34'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral range_types type
    str_verif = '- <parameters_spectral><range_types><type>: BandList, C34-39'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral ranges min
    str_verif = '- <parameters_spectral><ranges><min>: BandList, D34-37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral ranges max
    str_verif = '- <parameters_spectral><ranges><max>: BandList, E34-37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_general.xlsx", "ABS")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # no other errors
    verf_result = verf_result.replace('- <structure><sections><band_uid>: BandList, section_1: no band_uid', '')
    verf_result = verf_result.replace('- <bands><import_mode>: Band_1: no import_mode', '')
    verf_result = verf_result.replace('- <bands><uid>: Band_1: no uid', '')
    verf_result = verf_result.replace('- <bands><assignments>: Band_1, No assignment found in', '')
    verf_result = verf_result.replace('- <bands><characteristics>: Band_1, No characteristic found', '')
    verf_result = verf_result.replace('MANDATORY list:', '')
    verf_result = verf_result.replace('- <structure><sections variable_parameter>: BandList, sections, C64', '')
    verf_result = verf_result.replace('- <structure><sections><section>: BandList, sections: no section', '')
    verf_result = verf_result.replace('- <structure><sections><title>: BandList, section_1, B67', '')
    verf_result = verf_result.replace('- <bands><publications>: Band_1: no publications', '')
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <structure><section><bands>: Section_1, no band UID for Section Band UID NULL', '')
    verf_result = verf_result.replace('- <bands><band><uid>: Band_1, no Band UID in BandList structure', '')
    # import_mode
    str_verif = '- <import_mode>: BandList, C3'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # type
    str_verif = '- <type>: BandList, C4'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # title
    str_verif = '- <title>: BandList, C5'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # export_filename
    str_verif = '- <export_filename>: BandList, C13'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # uid
    str_verif = '- <uid>: BandList, A17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # constituent uid
    str_verif = '- <constituent><uid>: BandList, B17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # constituent primary_specie_uid
    str_verif = '- <constituent><primary_specie_uid>: BandList, C17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral unit
    str_verif = '- <parameters_spectral><unit>: BandList, A34'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral standard
    str_verif = '- <parameters_spectral><standard>: BandList, B34'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral range_types type
    str_verif = '- <parameters_spectral><range_types><type>: BandList, C34-39'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral ranges min
    str_verif = '- <parameters_spectral><ranges><min>: BandList, D34-37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # parameters_spectral ranges max
    str_verif = '- <parameters_spectral><ranges><max>: BandList, E34-37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_bandlist_version_abs_mandatory():
    # RAMAN new_version
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_general_new_version.xlsx", "RAMAN")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version status
    str_verif = '- <previous_version><status>: BandList, B53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version comments
    str_verif = '- <previous_version><comments>: BandList, C53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS new_version
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_general_new_version.xlsx", "ABS")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version status
    str_verif = '- <previous_version><status>: BandList, B53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version comments
    str_verif = '- <previous_version><comments>: BandList, C53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # RAMAN invalidate
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_general_invalidate.xlsx", "RAMAN")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version status
    str_verif = '- <previous_version><status>: BandList, B53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version comments
    str_verif = '- <previous_version><comments>: BandList, C53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS invalidate
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_general_invalidate.xlsx", "ABS")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version status
    str_verif = '- <previous_version><status>: BandList, B53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # previous_version comments
    str_verif = '- <previous_version><comments>: BandList, C53'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_bandlist_section_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_section.xlsx", "RAMAN")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # no other errors
    verf_result = verf_result.replace('MANDATORY list:', '')
    verf_result = verf_result.replace('- <structure><sections><section>: BandList, sections: no section', '')
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <structure><section><bands>: Section_1, no band UID for Section Band UID NULL', '')
    # structure sections band_uid
    str_verif = '- <structure><sections><band_uid>: BandList, section_1: no band_uid'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/bandlist_section.xlsx", "ABS")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # no other errors
    verf_result = verf_result.replace('MANDATORY list:', '')
    verf_result = verf_result.replace('- <structure><sections><section>: BandList, sections: no section', '')
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <structure><section><bands>: Section_1, no band UID for Section Band UID NULL', '')
    # structure sections band_uid
    str_verif = '- <structure><sections><band_uid>: BandList, section_1: no band_uid'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_general_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_general.xlsx", "RAMAN")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # no other errors
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <structure><section><bands>: Section_1, no band UID for Section Band UID 106', '')
    verf_result = verf_result.replace('- <bands><band><uid>: Band_4, no Band UID in BandList structure', '')
    # bands uid
    str_verif = '- <bands><uid>: Band_2, C29'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_general.xlsx", "ABS")
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # no other errors
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <bands><band><uid>: Band_4, no Band UID in BandList structure', '')
    # bands uid
    str_verif = '- <bands><uid>: Band_4, C99'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_no_assignments_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_no_assignments_ram.xlsx", "RAMAN")
    # no other errors
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <bands><characteristics><nominal_flag>: Band_1, More than one nominal_flag', '')
    verf_result = verf_result.replace('- <bands><characteristics><nominal_flag>: Band_2, More than one nominal_flag', '')
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments
    str_verif = '- <bands><assignments>: Band_2, No assignment found in H33'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_no_assignments_abs.xlsx", "ABS")
    # no other errors
    verf_result = verf_result.replace('OUBLIETTES list:', '')
    verf_result = verf_result.replace('- <bands><characteristics><nominal_flag>: Band_1, More than one nominal_flag', '')
    verf_result = verf_result.replace('- <bands><characteristics><nominal_flag>: Band_2, More than one nominal_flag', '')
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments
    str_verif = '- <bands><assignments>: Band_2, No assignment found in H33'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_assignments_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_assignments_ram.xlsx", "RAMAN")
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments label
    str_verif = '- <bands><assignments><label>: Band_1, assignment_3, I21'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments category
    str_verif = '- <bands><assignments><category>: Band_2, assignment_1, K51'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments multiplicity type
    str_verif = '- <bands><assignments><multiplicity><type>: Band_1, assignment_1, R17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><multiplicity><type>: Band_2, assignment_2, R47'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments primary_specie uid
    str_verif = '- <bands><assignments><primary_specie><uid>: Band_2, assignment_2, Y45'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><primary_specie><uid>: Band_3, assignment_1, Y57'
    assert str_verif not in verf_result
    # bands assignments transition
    str_verif = '- <bands><assignments><transition>: Band_2, assignment_3, AK39'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_assignments_abs.xlsx", "ABS")
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments label
    str_verif = '- <bands><assignments><label>: Band_1, assignment_3, I21'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments category
    str_verif = '- <bands><assignments><category>: Band_2, assignment_1, K51'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments multiplicity type
    str_verif = '- <bands><assignments><multiplicity><type>: Band_1, assignment_1, R17'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><multiplicity><type>: Band_2, assignment_2, R47'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments primary_specie uid
    str_verif = '- <bands><assignments><primary_specie><uid>: Band_2, assignment_2, Y45'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><primary_specie><uid>: Band_3, assignment_1, Y57'
    assert str_verif not in verf_result
    # bands assignments transition
    str_verif = '- <bands><assignments><transition>: Band_2, assignment_3, AK39'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_no_characteristic_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_no_characteristic_ram.xlsx", "RAMAN")
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics
    str_verif = '- <bands><characteristics>: Band_3, No characteristic found'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_no_characteristic_abs.xlsx", "ABS")
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics
    str_verif = '- <bands><characteristics>: Band_3, No characteristic found'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_characteristics_abs_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_characteristics_ram.xlsx", "RAMAN")
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics temperature unit
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_1, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_2, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_3, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_4, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_5, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_6, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_7, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_8, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_9, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_10, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_1, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_2, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_3, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_4, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_5, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics temperature value
    str_verif = '- <bands><characteristics><temperature><value>: Band_1, characteristic_4, BT18'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics pressure unit
    # no other errors
    str_verif = 'MANDATORY list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><value>: Band_1, characteristic_5, BZ19'
    verf_result = verf_result.replace(str_verif, '')
    # unit
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_1, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_2, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_3, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_4, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_5, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_6, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_7, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_8, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_9, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_1, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_2, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_3, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_4, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_5, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_10, CC8'
    assert str_verif not in verf_result
    # bands characteristics position peak_method
    str_verif = '- <bands><characteristics><position><peak_method>: Band_1, characteristic_7, CW25'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position peak_error
    str_verif = '- <bands><characteristics><position><peak_error>: Band_1, characteristic_9, CY31'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position peak
    str_verif = '- <bands><characteristics><position><peak>: Band_2, characteristic_1, CX37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position center
    str_verif = '- <bands><characteristics><position><center>: Band_2, characteristic_1, DA37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position center_method
    str_verif = '- <bands><characteristics><position><center_method>: Band_1, characteristic_5, CZ19'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position center_error
    str_verif = '- <bands><characteristics><position><center_error>: Band_1, characteristic_5, DB19'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position evaluation
    str_verif = '- <bands><characteristics><position><evaluation>: Band_1, characteristic_2, DC16'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics bandlist_nominal_flag
    str_verif = '- <bands><characteristics><bandlist_nominal_flag>: Band_2, characteristic_4, ES45'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/absm/band_characteristics_abs.xlsx", "ABS")
    # abs_mand
    str_verif = 'ABS_MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics temperature unit
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_1, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_2, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_3, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_4, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_5, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_6, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_7, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_8, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_9, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_1, characteristic_10, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_1, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_2, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_3, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_4, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><temperature><unit>: Band_2, characteristic_5, BW8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics temperature value
    str_verif = '- <bands><characteristics><temperature><value>: Band_1, characteristic_4, BT18'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics pressure unit
    # no other errors
    str_verif = 'MANDATORY list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><value>: Band_1, characteristic_5, BZ19'
    verf_result = verf_result.replace(str_verif, '')
    # unit
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_1, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_2, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_3, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_4, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_5, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_6, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_7, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_8, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_9, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_1, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_2, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_3, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_4, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_2, characteristic_5, CC8'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics><pressure><unit>: Band_1, characteristic_10, CC8'
    assert str_verif not in verf_result
    # bands characteristics position peak_method
    str_verif = '- <bands><characteristics><position><peak_method>: Band_1, characteristic_7, CW25'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position peak_error
    str_verif = '- <bands><characteristics><position><peak_error>: Band_1, characteristic_9, CY31'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position peak
    str_verif = '- <bands><characteristics><position><peak>: Band_2, characteristic_1, CX37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position center
    str_verif = '- <bands><characteristics><position><center>: Band_2, characteristic_1, DA37'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position center_method
    str_verif = '- <bands><characteristics><position><center_method>: Band_1, characteristic_5, CZ19'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position center_error
    str_verif = '- <bands><characteristics><position><center_error>: Band_1, characteristic_5, DB19'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics position evaluation
    str_verif = '- <bands><characteristics><position><evaluation>: Band_1, characteristic_2, DC16'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands characteristics bandlist_nominal_flag
    str_verif = '- <bands><characteristics><bandlist_nominal_flag>: Band_2, characteristic_4, ES45'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_bandlist_general_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/bandlist_general.xlsx", "RAMAN")
    # np other errors
    str_verif = 'ABS_MANDATORY list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections><band_uid>: BandList, section_1: no band_uid'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><import_mode>: Band_1: no import_mode'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><uid>: Band_1: no uid'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments>: Band_1, No assignment found in'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics>: Band_1, No characteristic found'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = 'MANDATORY list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections variable_parameter>: BandList, sections, C64'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections><section>: BandList, sections: no section'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections><title>: BandList, section_1, B67'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><publications>: Band_1: no publications'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = 'OUBLIETTES list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><section><bands>: Section_1, no band UID for Section Band UID NULL'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><band><uid>: Band_1, no Band UID in BandList structure'
    verf_result = verf_result.replace(str_verif, '')
    # description
    str_verif = '- <description>: BandList, C6'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # analysis
    str_verif = '- <analysis>: BandList, C7'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # quality_flag
    str_verif = '- <quality_flag>: BandList, A44'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # date_validated
    str_verif = '- <date_validated>: BandList, B44'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # validators
    str_verif = '- <validators>: BandList, C44-47'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/bandlist_general.xlsx", "ABS")
    # np other errors
    str_verif = 'ABS_MANDATORY list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections><band_uid>: BandList, section_1: no band_uid'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><import_mode>: Band_1: no import_mode'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><uid>: Band_1: no uid'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments>: Band_1, No assignment found in'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><characteristics>: Band_1, No characteristic found'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections variable_parameter>: BandList, sections, C64'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections><section>: BandList, sections: no section'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><sections><title>: BandList, section_1, B67'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><publications>: Band_1: no publications'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = 'OUBLIETTES list:'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <structure><section><bands>: Section_1, no band UID for Section Band UID NULL'
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><band><uid>: Band_1, no Band UID in BandList structure'
    verf_result = verf_result.replace(str_verif, '')
    # MANDATORY
    str_verif = 'MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # description
    str_verif = '- <description>: BandList, C6'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # analysis
    str_verif = '- <analysis>: BandList, C7'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # quality_flag
    str_verif = '- <quality_flag>: BandList, A44'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # date_validated
    str_verif = '- <date_validated>: BandList, B44'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # validators
    str_verif = '- <validators>: BandList, C44-47'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_bandlist_section_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/bandlist_section.xlsx", "RAMAN")
    str_verif = 'MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # structure sections variable_parameter
    str_verif = '- <structure><sections variable_parameter>: BandList, sections, C64'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # structure sections title
    str_verif = '- <structure><sections><title>: BandList, section_1, B67'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # structure subsections title
    str_verif = '- <structure><subsections><title>: BandList, section_2, sub_section_2, E79'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/bandlist_section.xlsx", "ABS")
    str_verif = 'MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # structure sections variable_parameter
    str_verif = '- <structure><sections variable_parameter>: BandList, sections, C64'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # structure sections title
    str_verif = '- <structure><sections><title>: BandList, section_1, B67'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # structure subsections title
    str_verif = '- <structure><subsections><title>: BandList, section_2, sub_section_2, E79'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_publications_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/band_publication_ram.xlsx", "RAMAN")
    str_verif = 'MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands publications
    str_verif = '- <bands><publications>: Band_1: no publications'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''
    # ABS
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/band_publication_abs.xlsx", "ABS")
    str_verif = 'MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands publications
    str_verif = '- <bands><publications>: Band_1: no publications'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # empty
    assert verf_result.strip() == ''


def test_verification_band_assignment_mandatory():
    # RAMAN
    verf_result = XMLGenerator_Bandlist_core.verification_F("xlsx/verifications/mand/band_assignments_ram.xlsx", "RAMAN")
    str_verif = 'MANDATORY list:'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments level
    str_verif = '- <bands><assignments><level>: Band_2, assignment_4, M33'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments symmetry_label
    str_verif = '- <bands><assignments><symmetry_label>: Band_1, assignment_2, J27'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><symmetry_label>: Band_1, assignment_3, J21'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><symmetry_label>: Band_3, assignment_1, J57'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments evaluation
    str_verif = '- <bands><assignments><evaluation>: Band_2, assignment_2, N45'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments multiplicity other_band_uid
    str_verif = '- <bands><assignments><multiplicity><other_band_uid>: Band_2, assignment_4, T33'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments multiplicity degeneracy
    str_verif = '- <bands><assignments><multiplicity><degeneracy>: Band_1, assignment_1, S15'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><multiplicity><degeneracy>: Band_1, assignment_1, S18'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    str_verif = '- <bands><assignments><multiplicity><degeneracy>: Band_2, assignment_2, S48'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # bands assignments multiplicity contribution_level
    str_verif = '- <bands><assignments><contribution_level>: Band_2, assignment_2, U45'
    assert str_verif in verf_result
    verf_result = verf_result.replace(str_verif, '')
    # il doit y avoir encore des errors !!!

    # empty
    assert verf_result.strip() == ''


"""
    # Not finished

    if data_to_verif["BL_Type"] in ["absorption", "Raman"]:
        infrared_flag = 1
        
                
                            
                contribution_flag = 0
                
                for multy_index in range(0, len(data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Multiplicity_Types"])):
                    if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Multiplicity_Types"][multy_index] or data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Multiplicity_Degeneracy"][multy_index] or data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Multiplicity_Other_band"][multy_index]:
                        

                        if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Multiplicity_Types"][multy_index] not in ["no", "mode", "site degeneracy", "unknown", ""] and data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Multiplicity_Types"][multy_index] in ["accidental degeneracy", "other isotope of primary specie", "other constituent specie", "other", ""]:
                            contribution_flag = 1
                
                if contribution_flag:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Contribution_Level", ["bands", "assignments", "contribution_level"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                
                if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Category"] == "electronic transition":
                    electronic_flag = 1
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Electronic_Labels", ["bands", "assignments", "transition", "electronic_modes", "label"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Electronic_Types", ["bands", "assignments", "transition", "electronic_modes", "type"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Category"] in ["fundamental vibration", "overtone vibration", "combination vibration"]:
                    for vib_number in range(1, data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Vibrations_qty"] + 1):
                        mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Vibration_{vib_number}_Label", ["bands", "assignments", "transition", "vibration_modes", "label"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                        mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Vibration_{vib_number}_Types", ["bands", "assignments", "transition", "vibration_modes", "type"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                        mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Vibration_{vib_number}_Bonds", ["bands", "assignments", "transition", "vibration_modes", "bonds"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Category"] in ["rotation", "overtone rotation"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Rotation_Label", ["bands", "assignments", "transition", "rotation_modes", "label"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Rotation_Types", ["bands", "assignments", "transition", "rotation_modes", "type"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Category"] == "phonon mode":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Phonon_Label", ["bands", "assignments", "transition", "phonon_modes", "label"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Phonon_Types", ["bands", "assignments", "transition", "phonon_modes", "type"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True)
                for resonance_number in range(0, len(data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Resonances_Types"])):
                    if data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Resonances_Types"][resonance_number] or (data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Resonances_Band"][resonance_number] and data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Resonances_Band"][resonance_number] != "NULL") or (data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Resonances_Nb"][resonance_number] and data_to_verif[f"B_{band_number}_Assignment_{assignment_number}_Resonances_Nb"][resonance_number] != "NULL"):
                        mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Resonances_Types", ["bands", "assignments", "resonances", "type"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True, resonance_number)
                        mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Resonances_Band", ["bands", "assignments", "resonances", "band_uid"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True, resonance_number)
                        mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Assignment_{assignment_number}_Resonances_Nb", ["bands", "assignments", "resonances", "band_assignment_number"], f"Band_{current_band_number}, assignment_{data_to_verif[f'B_{band_number}_Assignment_{assignment_number}_Number']}", True, resonance_number)
        
        no_chars = False
        if data_to_verif[f"B_{band_number}_Characteristics_qty"] == 0 or (data_to_verif[f"B_{band_number}_Characteristics_qty"] == 1 and f"B_{band_number}_Characteristic_1_Nb" in data_to_verif.keys() and data_to_verif[f"B_{band_number}_Characteristic_1_Nb"] == ""):
            no_chars = True
        if not no_chars:
            for char_number in range(1, data_to_verif[f"B_{band_number}_Characteristics_qty"] + 1):
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] or data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"]:
                    if electronic_flag:
                        electronic_flag = 2
                    if infrared_flag:
                        infrared_flag = 2
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_T_Error", ["bands", "characteristics", "temperature", "error"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_T_Max", ["bands", "characteristics", "temperature", "max"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_P_Error"] or data_to_verif[f"B_{band_number}_Characteristic_{char_number}_P_Formation"] or data_to_verif[f"B_{band_number}_Characteristic_{char_number}_P_Max"] or data_to_verif[f"B_{band_number}_Characteristic_{char_number}_P_Stress_type"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_P_Value", ["bands", "characteristics", "pressure", "value"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif["BL_Type"] in ["Raman scattering", "fluorescence emission"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Laser_excitation_Wavelength", ["bands", "characteristics", "excitation", "laser_wavelength"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif["BL_Type"] in ["Raman scattering"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Sample_Orient_mode", ["bands", "characteristics", "excitation", "sample_orientation_mode"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif["BL_Type"] in ["Raman scattering"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Sample_Orient_mode"] == "oriented":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Sample_Orient", ["bands", "characteristics", "excitation", "sample_orientation"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif["BL_Type"] in ["Raman scattering", "absorption"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Sample_Orient_mode"] == "oriented":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Polarization_Orient_mode", ["bands", "characteristics", "excitation", "polarization_orientation_mode"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Polarization_Orient_mode"] == "polarized":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Polarization_Orient", ["bands", "characteristics", "excitation", "polarization_orientation"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Method_1_Types", ["bands", "characteristics", "method", "type"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Methods_Overlap", ["bands", "characteristics", "overlap"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Width_FWHM", ["bands", "characteristics", "width", "fwhm"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Width_FWHM"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Width_FWHM"] != "NULL":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Width_Method", ["bands", "characteristics", "width", "method"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Width_FWHM_error", ["bands", "characteristics", "width", "fwhm_error"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Width_Evaluation", ["bands", "characteristics", "width", "evaluation"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Width_Shape", ["bands", "characteristics", "width", "shape"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Width_Shape"] in ["asymmetric", "asymmetric low frequency wing", "asymmetric high frequency wing"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Width_Asymm_factor", ["bands", "characteristics", "width", "asymmetry_factor"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Strength"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Strength"] != "NULL"):
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Method", ["bands", "characteristics", "peak_intensity", "method"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif["BL_Type"] == "absorption" and not data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef", ["bands", "characteristics", "peak_intensity", "abscoef"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] != "NULL":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef_error", ["bands", "characteristics", "peak_intensity", "abscoef_error"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] == [""] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] != [""]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative", ["bands", "characteristics", "peak_intensity", "relative"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] != [""] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] == [""]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef", ["bands", "characteristics", "peak_intensity", "abscoef"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] != "NULL":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative_error", ["bands", "characteristics", "peak_intensity", "relative_error"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Strength", ["bands", "characteristics", "peak_intensity", "strength"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Abs_coef"] != "NULL"):
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Evaluation", ["bands", "characteristics", "peak_intensity", "evaluation"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Strength"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Strength"] != "NULL"):
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Method", ["bands", "characteristics", "integrated_intensity", "method"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif["BL_Type"] == "absorption" and not data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"]:
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef", ["bands", "characteristics", "integrated_intensity", "abscoef"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] != "NULL":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef_error", ["bands", "characteristics", "integrated_intensity", "abscoef_error"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                elif data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] != "NULL":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative", ["bands", "characteristics", "integrated_intensity", "relative"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] != "NULL":
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative_error", ["bands", "characteristics", "integrated_intensity", "relative_error"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Abs_coef"] != "NULL"):
                    mand_problems = mand_problems + verif_action(data_to_verif, data_position, f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Evaluation", ["bands", "characteristics", "integrated_intensity", "evaluation"], f"Band_{current_band_number}, characteristic_{data_to_verif[f'B_{band_number}_Characteristic_{char_number}_Nb']}", True)
                if not ref_position_IR_flag and ((data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Peak_intensity_Relative"] != "NULL") or (data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] and data_to_verif[f"B_{band_number}_Characteristic_{char_number}_Integrated_intensity_Relative"] != "NULL")):
                    ref_position_IR_flag = 1
    if electronic_flag == 2:
        mand_problems = mand_problems + verif_action(data_to_verif, data_position, "BL_Spectral_Ref_pos_electronic", ["reference_position", "electronic"], "BandList", True)
    if infrared_flag == 2 or ref_position_IR_flag:
        mand_problems = mand_problems + verif_action(data_to_verif, data_position, "BL_Spectral_Ref_pos_absorption", ["reference_position", "infrared"], "BandList", True)
    if mand_problems != "MANDATORY list:\n":
        if str_list_problems:
            str_list_problems = str_list_problems + "\n"
        str_list_problems = str_list_problems + mand_problems
"""



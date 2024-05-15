"""
@author: Nikos Kosioris
"""

import pandas as pd
from contextlib import suppress
import json

estimate = {}
refutel = {}
results = {}
results['Linear Regression'] = {}
results['Propensity Score Matching'] = {}
results['Propensity Score Stratification'] = {}
results['Propensity Score Weighting'] = {}

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\er_5gas.csv')

#Creating the 
causal_graph = """
digraph {
residents;
build_era;
occupied_days;
occupied_nights;
weeklyhoursofwork;
ageleavingeducation;
externalwindows;
windowsopen;
many_externaldoors;
externalwalls;
cubic_area;
radiators;
cubic_area_for_clothesdrying_percent;
cubic_area_with_trvs_percent;
dehumidifier;
dishwasher_electric;
electricheater_electric;
electrichob_electric;
electricoven_electric;
electricshower_electric;
freezer_electric;
fridge_electric;
fridgefreezer_electric;
grill_electric;
kettle_electric;
microwave_electric;
other_electric;
toaster_electric;
tumbledrier_electric;
vacuumcleaner_electric;
washingmachine_electric;
washingmachinetumbledrier_electric;
woodburningstove_other_fuel;
air_conditioning;
computer;
dehumidifier_electric;
electric_blanket;
electric_fan;
electric_heater;
humidifier;
iron;
laptop;
media_entertainment;
motor_vehicle;
non_smart_phone;
other_high_power_1;
other_high_power_2;
other_high_power_3;
other_high_power_4;
outdoor_electric_space_heater;
outdoor_hot_tub;
outdoor_light;
outdoor_water_feature;
smartphone;
sound_system;
tablet;
television;
vacuum_cleaner;
unit_charge_pence_per_kwh_gas;
unit_charge_pence_per_kwh_electricity;
income_band;
high_gas_pulse_consumption;
electric_con_per_year_mean;
bath_gas;
gasfire_gas;
gashob_gas;
gasoven_gas;
shower_gas;
sink_gas;
U[label="Unobserved Confounders"];

income_band -> residents;
income_band -> electric_fan;
income_band -> sound_system;
income_band -> iron;
income_band -> media_entertainment;
income_band -> laptop;
income_band -> smartphone;
income_band -> television;
income_band -> computer;
income_band -> tablet;
income_band -> non_smart_phone;
income_band -> motor_vehicle;
income_band -> dishwasher_electric; 
income_band -> electrichob_electric;
income_band -> electricoven_electric;
income_band -> other_electric;
income_band -> vacuumcleaner_electric;
income_band -> freezer_electric;
income_band -> grill_electric;
income_band -> tumbledrier_electric;
income_band -> washingmachine_electric;
income_band -> washigmachinetumbledrier;
income_band -> fridge_electric;
income_band -> electricheater_electric;
income_band -> kettle_electric;
income_band -> microwave_electric;
income_band -> air_conditioning;
income_band -> dehumidifier;
income_band -> dehumidifier_electric;
income_band -> electric_blanket;
income_band -> electric_heater;
income_band -> build_era;
income_band -> vacuum_cleaner;
income_band -> outdoor_electric_space_heater;
income_band -> humidifier;
income_band -> other_high_power_1;
income_band -> other_high_power_2;
income_band -> other_high_power_3;
income_band -> other_high_power_4;
income_band -> gashob_gas;
income_band -> gasoven_gas;
income_band -> toaster_electric;
residents -> vacuum_cleaner;
residents -> outdoor_electric_space_heater;
residents -> other_high_power_3;
residents -> other_high_power_2;
residents -> other_high_power_4;
residents -> humidifier;
residents -> other_high_power_1;
residents -> occupied_days;
residents -> electric_fan;
residents -> electric_blanket;
residents -> occupied_nights;
residents -> iron;
residents -> dehumidifier;
residents -> weeklyhoursofwork;
residents -> sound_system;
residents -> dehumidifier_electric;
residents -> microwave_electric;
residents -> electricheater_electric;
residents -> air_conditioning;
residents -> kettle_electric;
residents -> laptop;
residents -> freezer_electric;
residents -> fridge_electric;
residents -> electrichob_electric;
residents -> computer;
residents -> washingmachine_electric;
residents -> vacuumcleaner_electric;
residents -> dishwasher_electric;
residents -> washingmachinetumbledrier_electric;
residents -> electricoven_electric;
residents -> tumbledrier_electric;
residents -> grill_electric;
residents -> toaster_electric;
residents -> other_electric;
residents -> media_entertainment;
residents -> fridgefreezer_electric;
residents -> smartphone;
residents -> tablet;
residents -> motor_vehicle;
residents -> unit_charge_pence_per_kwh;
residents -> non_smart_phone;
residents -> television;
residents -> gashob_gas;
residents -> gasoven_gas;
radiators -> electricheater_electric;
radiators -> electric_con_per_year_mean;
radiators -> high_gas_pulse_consumption;
radiators -> woodburningstove_other_fuel;
radiators -> cubic_area_with_trvs_percent;
radiators -> electric_blanket;
radiators -> electric_heater;
cubic_area_for_clothesdrying_percent -> dehumidifier;
cubic_area_for_clothesdrying_percent -> dehumidifier_electric;
ageleavingeducation -> income_band;
externalwindows -> open;
cubic_area -> vacuum_cleaner;
dehumidifier -> electric_con_per_year_mean;
dehumidifier -> high_gas_pulse_consumption;
dishwasher_electric -> electric_con_per_year_mean;
electricheater_electric -> electric_con_per_year_mean;
electrichob_electric -> electric_con_per_year_mean;
electrichob_electric -> electricoven_electric;
electrichob_electric -> gashob_gas;
electricoven_electric -> electric_con_per_year_mean;
electricoven_electric -> gasoven_gas;
electricshower_electric -> electric_con_per_year_mean;
electricshower_electric -> high_gas_pulse_consumption;
freezer_electric -> fridgefreezer_electric;
fridge_electric -> fridgefreezer_electric;
fridgefreezer_electric -> electric_con_per_year_mean;
grill_electric -> electric_con_per_year_mean;
kettle_electric -> electric_con_per_year_mean;
microwave_electric -> electric_con_per_year_mean;
other_electric -> electric_con_per_year_mean;
toaster_electric -> electric_con_per_year_mean;
tumbledrier_electric -> washingmachinetumbledrier_electric;
vacuumcleaner_electric -> electric_con_per_year_mean;
washingmachine_electric -> washingmachinetumbledrier_electric;
washingmachinetumbledrier_electric -> electric_con_per_year_mean;
woodburningstove_other_fuel -> electric_con_per_year_mean;
woodburningstove_other_fuel -> high_gas_pulse_consumption;
air_conditioning -> electric_fan;
air_conditioning -> electric_con_per_year_mean;
air_conditioning -> high_gas_pulse_consumption;
computer -> electric_con_per_year_mean;
dehumidifier_electric -> electric_con_per_year_mean;
dehumidifier_electric -> high_gas_pulse_consumption;
electric_blanket -> electric_con_per_year_mean;
electric_blanket -> high_gas_pulse_consumption;
electric_fan -> electric_con_per_year_mean;
electric_fan -> high_gas_pulse_consumption;
electric_heater -> electric_con_per_year_mean;
electric_heater -> high_gas_pulse_consumption;
electric_heater -> high_gas_pulse_consumption;
humidifier -> electric_con_per_year_mean;
humidifier -> high_gas_pulse_consumption;
iron -> electric_con_per_year_mean;
laptop -> electric_con_per_year_mean;
media_entertainment -> electric_con_per_year_mean;
motor_vehicle -> electric_con_per_year_mean;
non_smartphone -> electric_con_per_year_mean;
other_high_power_1 -> electric_con_per_year_mean;
other_high_power_2 -> electric_con_per_year_mean;
other_high_power_3 -> electric_con_per_year_mean;
other_high_power_4 -> electric_con_per_year_mean;
outdoor_electric_space_heater -> electric_con_per_year_mean;
outdoor_hot_tub -> electric_con_per_year_mean;
outdoor_light -> electric_con_per_year_mean;
outdoor_water_feature -> electric_con_per_year_mean;
smartphone -> media_entertainment;
smartphone -> non_smartphone;
smartphone -> electric_con_per_year_mean;
sound_system -> electric_con_per_year_mean;
tablet -> media_entertainment;
tablet -> electric_con_per_year_mean;
television -> media_entertainment;
vacuum_cleaner -> electric_con_per_year_mean;
unit_charge_pence_per_kwh_electricity -> electric_con_per_year_mean;
unit_charge_pence_per_kwh_gas -> electric_con_per_year_mean;
unit_charge_pence_per_kwh_electricity -> high_gas_pulse_consumption;
bath_gas -> high_gas_pulse_consumption;
bath_gas -> electric_con_per_year_mean;
shower_gas -> electric_con_per_year_mean;
shower_gas -> high_gas_pulse_consumption;
gasfire_gas -> high_gas_pulse_consumption;
gasfire_gas -> electric_con_per_year_mean;
gashob_gas -> high_gas_pulse_consumption;
gashob_gas -> electric_con_per_year_mean;
gasoven_gas -> high_gas_pulse_consumption;
gasoven_gas -> electric_con_per_year_mean;
electricoven_electric -> freezer_electric;
electricoven_electric -> fridge_electric;
electrichob_electric -> freezer_electric;
electrichob_electric -> fridge_electric;
electricoven_electric -> fridgefreezer_electric;
build_era -> gasfire_gas;
build_era -> electricshower_electric;
build_era -> bath_gas;
build_era -> shower_gas;
build_era -> sink_gas;
sink_gas -> high_gas_pulse_consumption;
education_A_to_Levels_or_Highers;
education_Degree_level_qualification_or_equivalent_eg_BSc_BA_MSc_MA;
education_GCSE_grade_D_to_G_or_CSE_grade_2_to_5_or_Standard_Grade_level_4_to_6;
education_Higher_educational_qualification_below_degree_level;
education_No_formal_qualifications;
education_O_Level_or_GCSE_equivalent_Grade_A_to_C_or_O_Grade_CSE_equivalent_Grade_1_or_Standard_Grade_level_1;
education_Other_qualifications;
education_PhD;
urban_rural_name_Large_Urban_Areas;
urban_rural_name_Other_Urban_Areas;
urban_rural_name_Small_Towns_or_Rural_Areas;
U -> high_gas_pulse_consumption;
U -> electric_con_per_year_mean;
externalwindows -> radiators;
externalwindows -> dehumidifier_electric;
externalwindows -> electricheater_electric;
externalwindows -> gasfire_gas;
externalwindows -> woodburningstove_other_fuel;
externalwindows -> air_conditioning;
externalwindows -> dehumidifier;
externalwindows -> electric_blanket;
externalwindows -> electric_fan;
externalwindows -> electric_heater;
externalwindows -> humidifier;
windowsopen -> radiators;
windowsopen -> dehumidifier_electric;
windowsopen -> electricheater_electric;
windowsopen -> gasfire_gas;
windowsopen -> woodburningstove_other_fuel;
windowsopen -> air_conditioning;
windowsopen -> dehumidifier;
windowsopen -> electric_blanket;
windowsopen -> electric_fan;
windowsopen -> electric_heater;
windowsopen -> humidifier;
many_externaldoors -> radiators;
many_externaldoors -> dehumidifier_electric;
many_externaldoors -> electricheater_electric;
many_externaldoors -> gasfire_gas;
many_externaldoors -> woodburningstove_other_fuel;
many_externaldoors -> air_conditioning;
many_externaldoors -> dehumidifier;
many_externaldoors -> electric_blanket;
many_externaldoors -> electric_fan;
many_externaldoors -> electric_heater;
many_externaldoors -> humidifier;
externalwalls -> radiators;
externalwalls -> dehumidifier_electric;
externalwalls -> electricheater_electric;
externalwalls -> gasfire_gas;
externalwalls -> woodburningstove_other_fuel;
externalwalls -> air_conditioning;
externalwalls -> dehumidifier;
externalwalls -> electric_blanket;
externalwalls -> electric_fan;
externalwalls -> electric_heater;
externalwalls -> humidifier;
cubic_area -> radiators;
cubic_area -> dehumidifier_electric;
cubic_area -> electricheater_electric;
cubic_area -> gasfire_gas;
cubic_area -> woodburningstove_other_fuel;
cubic_area -> air_conditioning;
cubic_area -> dehumidifier;
cubic_area -> electric_blanket;
cubic_area -> electric_fan;
cubic_area -> electric_heater;
cubic_area -> humidifier;
cubic_area_for_clothesdrying_percent -> radiators;
cubic_area_for_clothesdrying_percent -> dehumidifier_electric;
cubic_area_for_clothesdrying_percent -> electricheater_electric;
cubic_area_for_clothesdrying_percent -> gasfire_gas;
cubic_area_for_clothesdrying_percent -> woodburningstove_other_fuel;
cubic_area_for_clothesdrying_percent -> air_conditioning;
cubic_area_for_clothesdrying_percent -> electric_blanket;
cubic_area_for_clothesdrying_percent -> electric_fan;
cubic_area_for_clothesdrying_percent -> electric_heater;
cubic_area_for_clothesdrying_percent -> humidifier;
cubic_area_with_trvs_percent -> dehumidifier_electric;
cubic_area_with_trvs_percent -> electricheater_electric;
cubic_area_with_trvs_percent -> gasfire_gas;
cubic_area_with_trvs_percent -> woodburningstove_other_fuel;
cubic_area_with_trvs_percent -> air_conditioning;
cubic_area_with_trvs_percent -> dehumidifier;
cubic_area_with_trvs_percent -> electric_blanket;
cubic_area_with_trvs_percent -> electric_fan;
cubic_area_with_trvs_percent -> electric_heater;
cubic_area_with_trvs_percent -> humidifier;
build_era -> outdoor_water_feature; 
build_era -> outdoor_hot_tub;
build_era -> outdoor_light;
build_era -> radiators;
build_era -> woodburningstove_other_fuel;
build_era -> externalwindows;
build_era -> many_externaldoors;
build_era -> cubic_area;
build_era -> cubic_area_for_clothesdrying_percent;
build_era -> cubic_area_with_trvs_percent;
build_era -> windowsopen;
education_A_to_Levels_or_Highers -> ageleavingeducation;
education_A_to_Levels_or_Highers -> income_band;
education_Degree_level_qualification_or_equivalent_eg_BSc_BA_MSc_MA -> ageleavingeducation;
education_Degree_level_qualification_or_equivalent_eg_BSc_BA_MSc_MA -> income_band;
education_GCSE_grade_D_to_G_or_CSE_grade_2_to_5_or_Standard_Grade_level_4_to_6 -> ageleavingeducation;
education_GCSE_grade_D_to_G_or_CSE_grade_2_to_5_or_Standard_Grade_level_4_to_6 -> income_band;
education_Higher_educational_qualification_below_degree_level -> ageleavingeducation;
education_Higher_educational_qualification_below_degree_level -> income_band;
education_No_formal_qualifications -> ageleavingeducation;
education_No_formal_qualifications -> income_band;
education_O_Level_or_GCSE_equivalent_Grade_A_to_C_or_O_Grade_CSE_equivalent_Grade_1_or_Standard_Grade_level_1 -> ageleavingeducation;
education_O_Level_or_GCSE_equivalent_Grade_A_to_C_or_O_Grade_CSE_equivalent_Grade_1_or_Standard_Grade_level_1 -> income_band;
education_Other_qualifications -> ageleavingeducation;
education_Other_qualifications -> income_band;
education_PhD -> ageleavingeducation;
education_PhD -> income_band;
income_band -> urban_rural_name_Large_Urban_Areas;
urban_rural_name_Large_Urban_Areas -> outdoor_water_feature;
urban_rural_name_Large_Urban_Areas -> outdoor_electric_space_heater;
urban_rural_name_Large_Urban_Areas -> outdoor_hot_tub;
urban_rural_name_Large_Urban_Areas -> outdoor_light;
urban_rural_name_Large_Urban_Areas -> woodburningstove_other_fuel;
urban_rural_name_Large_Urban_Areas -> cubic_area_with_trvs_percent;
urban_rural_name_Large_Urban_Areas -> externalwalls;
urban_rural_name_Large_Urban_Areas -> cubic_area_for_clothesdrying_percent;
urban_rural_name_Large_Urban_Areas -> windowsopen;
urban_rural_name_Large_Urban_Areas -> cubic_area;
urban_rural_name_Large_Urban_Areas -> radiators;
urban_rural_name_Large_Urban_Areas -> externalwindows;
urban_rural_name_Large_Urban_Areas -> build_era;
urban_rural_name_Large_Urban_Areas -> gasfire_gas;
income_band -> urban_rural_name_Other_Urban_Areas;
urban_rural_name_Other_Urban_Areas -> outdoor_water_feature;
urban_rural_name_Other_Urban_Areas -> outdoor_electric_space_heater;
urban_rural_name_Other_Urban_Areas -> outdoor_hot_tub;
urban_rural_name_Other_Urban_Areas -> outdoor_light;
urban_rural_name_Other_Urban_Areas -> woodburningstove_other_fuel;
urban_rural_name_Other_Urban_Areas -> cubic_area_with_trvs_percent;
urban_rural_name_Other_Urban_Areas -> externalwalls;
urban_rural_name_Other_Urban_Areas -> cubic_area_for_clothesdrying_percent;
urban_rural_name_Other_Urban_Areas -> windowsopen;
urban_rural_name_Other_Urban_Areas -> cubic_area;
urban_rural_name_Other_Urban_Areas -> radiators;
urban_rural_name_Other_Urban_Areas -> externalwindows;
urban_rural_name_Other_Urban_Areas -> build_era;
urban_rural_name_Other_Urban_Areas -> gasfire_gas;
income_band -> urban_rural_name_Small_Towns_or_Rural_Areas;
urban_rural_name_Small_Towns_or_Rural_Areas -> outdoor_water_feature;
urban_rural_name_Small_Towns_or_Rural_Areas -> outdoor_electric_space_heater;
urban_rural_name_Small_Towns_or_Rural_Areas -> outdoor_hot_tub;
urban_rural_name_Small_Towns_or_Rural_Areas -> outdoor_light;
urban_rural_name_Small_Towns_or_Rural_Areas -> woodburningstove_other_fuel;
urban_rural_name_Small_Towns_or_Rural_Areas -> cubic_area_with_trvs_percent;
urban_rural_name_Small_Towns_or_Rural_Areas -> externalwalls;
urban_rural_name_Small_Towns_or_Rural_Areas -> cubic_area_for_clothesdrying_percent;
urban_rural_name_Small_Towns_or_Rural_Areas -> windowsopen;
urban_rural_name_Small_Towns_or_Rural_Areas -> cubic_area;
urban_rural_name_Small_Towns_or_Rural_Areas -> radiators;
urban_rural_name_Small_Towns_or_Rural_Areas -> externalwindows;
urban_rural_name_Small_Towns_or_Rural_Areas -> build_era;
urban_rural_name_Small_Towns_or_Rural_Areas -> gasfire_gas;
}
"""

from dowhy import CausalModel
from IPython.display import Image, display

model= CausalModel(
        data = df,
        graph=causal_graph.replace("\n", " "),
        treatment='many_externaldoors',
        outcome='high_gas_pulse_consumption')
model.view_model()
display(Image(filename="causal_model.png"))

#Identify the causal effect
estimands = model.identify_effect()
print(estimands)

#################Causal Effect Estimation using Linear Regression##############

with suppress(Exception):
    #Causal Effect Estimation
    estimate[0] = model.estimate_effect(estimands,method_name = "backdoor.linear_regression")
    print(estimate[0])
    results['Linear Regression']['Estimation'] = str(estimate[0])
with suppress(Exception):
    #Refute the obtained estimate
    refutel[0] = model.refute_estimate(estimands,estimate[0], "random_common_cause")
    
    results['Linear Regression']['Random Common Cause'] = str(refutel[0])
with suppress(Exception):
    #Refute the obtained estimate
    refutel[1] = model.refute_estimate(estimands,estimate[0], "add_unobserved_common_cause")
    
    results['Linear Regression']['Add Unobserved Common Cause'] = str(refutel[1])
with suppress(Exception):
    #Refute the obtained estimate
    refutel[2] = model.refute_estimate(estimands,estimate[0], "placebo_treatment_refuter")
    
    results['Linear Regression']['Placebo Treatment Refuter'] = str(refutel[2])
with suppress(Exception):
    #Refute the obtained estimate
    refutel[3] = model.refute_estimate(estimands,estimate[0], "data_subset_refuter")
    
    results['Linear Regression']['Data Subset Refuter'] = str(refutel[3])

#################Causal Effect Estimation using Propensity Score Matching##############

with suppress(Exception):
    #Causal Effect Estimation
    estimate[1] = model.estimate_effect(estimands,method_name = "backdoor.propensity_score_matching")
    print(estimate[1])
    results['Propensity Score Matching']['Estimation'] = str(estimate[1])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[4] = model.refute_estimate(estimands,estimate[1], "random_common_cause")
    print(refutel[4])    
    results['Propensity Score Matching']['Random Common Cause'] = str(refutel[4])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[5] = model.refute_estimate(estimands,estimate[1], "add_unobserved_common_cause")
    print(refutel[5])        
    results['Propensity Score Matching']['Add Unobserved Common Cause'] = str(refutel[5])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[6] = model.refute_estimate(estimands,estimate[1], "placebo_treatment_refuter")
    print(refutel[6])     
    results['Propensity Score Matching']['Placebo Treatment Refuter'] = str(refutel[6])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[7] = model.refute_estimate(estimands,estimate[1], "data_subset_refuter")
    print(refutel[7])      
    results['Propensity Score Matching']['Data Subset Refuter'] = str(refutel[7])

#################Causal Effect Estimation using Propensity Score Stratification##############

with suppress(Exception):
    #Causal Effect Estimation
    estimate[2] = model.estimate_effect(estimands,method_name = "backdoor.propensity_score_stratification")
    print(estimate[2])
    results['Propensity Score Stratification']['Estimation'] = str(estimate[2])   
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[8] = model.refute_estimate(estimands,estimate[2], "random_common_cause")
    print(refutel[8])      
    results['Propensity Score Stratification']['Random Common Cause'] = str(refutel[8])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[9] = model.refute_estimate(estimands,estimate[2], "add_unobserved_common_cause")
    print(refutel[9])      
    results['Propensity Score Stratification']['Add Unobserved Common Cause'] = str(refutel[9])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[10] = model.refute_estimate(estimands,estimate[2], "placebo_treatment_refuter")
    print(refutel[10])      
    results['Propensity Score Stratification']['Placebo Treatment Refuter'] = str(refutel[10])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[11] = model.refute_estimate(estimands,estimate[2], "data_subset_refuter")
    print(refutel[11])      
    results['Propensity Score Stratification']['Data Subset Refuter'] = str(refutel[11])

#################Causal Effect Estimation using Propensity Score Weighting##############

with suppress(Exception):
    #Causal Effect Estimation
    estimate[3] = model.estimate_effect(estimands,method_name = "backdoor.propensity_score_weighting")
    print(estimate[3])    
    results['Propensity Score Weighting']['Estimation'] = str(estimate[3])   
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[12] = model.refute_estimate(estimands,estimate[3], "random_common_cause")
    print(refutel[12])      
    results['Propensity Score Weighting']['Random Common Cause'] = str(refutel[12])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[13] = model.refute_estimate(estimands,estimate[3], "add_unobserved_common_cause")
    print(refutel[13])      
    results['Propensity Score Weighting']['Add Unobserved Common Cause'] = str(refutel[13])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[14] = model.refute_estimate(estimands,estimate[3], "placebo_treatment_refuter")
    print(refutel[14])      
    results['Propensity Score Weighting']['Placebo Treatment Refuter'] = str(refutel[14])
with suppress(Exception):    
    #Refute the obtained estimate
    refutel[15] = model.refute_estimate(estimands,estimate[3], "data_subset_refuter")
    print(refutel[15])      
    results['Propensity Score Weighting']['Data Subset Refuter'] = str(refutel[15])

with open(r'C:\Users\User\Desktop\Results doWhy\result_er_5gas_hot_months.json', 'w') as fp:
    json.dump(results, fp, indent=4) 

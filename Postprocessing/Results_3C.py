# -*- coding: utf-8 -*-
"""
Created on Tue Jul   13:31:07 2021

@author: Jocelyn Mbenoun
"""
# =============================================================================
# Results file for the 3 cluster model. This file is created based on the 
# results file of the one cluster model. underneath, additional code and/or 
# function needs are highlighted. All code should be applicable to the 3 cluster model, 
# since only adapted code, ready for the 3 cluster model is pasted in this file.
# =============================================================================


# =============================================================================
# Needed additional code
# =============================================================================


#%% capacity

name_capacity = "new_capacity" # name used for the variable for the capacity of each node
name_capacity_0 = "pre_installed_capacity" # name used for the parameter used for the installed capacity
name_capacity_max = "max_capacity" # name used for the parameter for capacity max

#capacity forward/backward for NG and H2 to be added
cluster_names_capacities = get_cluster_names_from_parameter(name_capacity_0,dictionary_3C)
cluster_capacities = get_cluster_capacities_from_nodes(cluster_names_capacities,name_capacity,name_capacity_0,name_capacity_max,dictionary_3C)

cluster_subnodes_names_capacity = dict()
for cluster in clusters:
    cluster_subnodes_names_capacity[cluster] = get_cluster_subnodes_names_from_parameter(cluster,name_capacity_0,dictionary_3C)
cluster_subnodes_capacities = dict()
for cluster in clusters:
    cluster_subnodes_capacities[cluster] = get_cluster_subnodes_capacities_from_nodes(cluster_subnodes_names_capacity[cluster],cluster,name_capacity,name_capacity_0,name_capacity_max,dictionary_3C)

name_capacity_power = "new_power_capacity"
name_capacity_energy = "new_energy_capacity"
name_capacity_0_power = "pre_installed_capacity_power"
name_capacity_0_energy = "pre_installed_capacity_energy"
name_capacity_max_power = "max_capacity_power"
name_capacity_max_energy = "max_capacity_energy"

cluster_subnodes_2_capacities_storage = dict()
for cluster in clusters:
    cluster_subnodes_2_capacities_storage[cluster] = get_cluster_subnodes_names_from_parameter(cluster,"max_capacity_power",dictionary_3C)

cluster_subnodes_cap_storage = dict()
for cluster in clusters:
    cluster_subnodes_cap_storage[cluster] = get_cluster_subnodes_capacities_from_storage(cluster_subnodes_2_capacities_storage[cluster],cluster,name_capacity_power,name_capacity_0_power,name_capacity_max_power,name_capacity_energy,name_capacity_0_energy,name_capacity_max_energy,dictionary_3C)

cluster_subnodes_capacities_tot = dict()
for cluster in clusters:
    cluster_subnodes_capacities_tot[cluster] = merge_dictionaries(cluster_subnodes_cap_storage[cluster],cluster_subnodes_capacities[cluster])

table_cluster_subnodes_capacities = {}
table_cluster_subnodes_cap_storage = {}
table_cluster_subnodes_cap_tot = {}
for cluster in clusters:
    table_cluster_subnodes_capacities[cluster] = transform_into_table(cluster_subnodes_capacities[cluster])
    table_cluster_subnodes_cap_storage[cluster] = transform_into_table(cluster_subnodes_cap_storage[cluster])
    table_cluster_subnodes_cap_tot[cluster] = transform_into_table(cluster_subnodes_capacities_tot[cluster])
    if cluster in clusters_belgium:
        save_table_into_csv(table_cluster_subnodes_cap_tot[cluster],title + '/capacities for '+cluster)
    


#%% TOTAL capacities FOR BELGIUM: OFFSHORE, ZEEBRUGGE, INLAND, ELECTRICITY IMPORTS FROM NEIGHBOURING COUNTRIES, HVDC costs between OFFSHORE, ZEEBRUGGE and INLAND

electricity_subnodes = get_subnodes_energy_vector('energy_electricity',dictionary_3C)
carbon_dioxide_subnodes = get_subnodes_energy_vector('energy_carbon_dioxide',dictionary_3C)
natural_gas_subnodes = get_subnodes_energy_vector('energy_natural_gas',dictionary_3C)
hydrogen_subnodes = get_subnodes_energy_vector('energy_hydrogen',dictionary_3C)

GW_subnodes = merge_lists(get_subnodes_energy_vector('unit_GW',dictionary_3C),get_subnodes_energy_vector('unit_power_GW',dictionary_3C))
GWh_subnodes = merge_lists(get_subnodes_energy_vector('unit_GWh',dictionary_3C),get_subnodes_energy_vector('unit_energy_GWh',dictionary_3C))
kt_subnodes = get_subnodes_energy_vector('unit_energy_kt',dictionary_3C)
kt_h_subnodes = merge_lists(get_subnodes_energy_vector('unit_kt_h',dictionary_3C),get_subnodes_energy_vector('unit_power_kt_h',dictionary_3C))

    
cluster_subnodes_caps_BE = dict()
cluster_subnodes_caps_BE['GW'] = dict()
cluster_subnodes_caps_BE['GWh'] = dict()
cluster_subnodes_caps_BE['kt_h'] = dict()
cluster_subnodes_caps_BE['kt'] = dict()

table_cluster_subnodes_caps_BE = dict()
for cluster in clusters_belgium:
    cluster_subnodes = dictionary_3C["solution"]["elements"][cluster]["sub_elements"].keys()
    for subnode in cluster_subnodes:
        if subnode in electricity_subnodes:
            color = '#2c2c2c'
            vector = 'electricity'
        elif subnode in carbon_dioxide_subnodes:
            color = '#79b932'
            vector = 'CO2'
        elif subnode in natural_gas_subnodes + ["LINEPACK_NG"]:
            color = '#c55a11'
            vector = 'natural_gas'
        elif subnode in hydrogen_subnodes:
             color = '#2e75b6'
             vector = 'hydrogen'
        else:
            color = 'black'
            vector = 'not specified'
            
        if subnode in GW_subnodes:
            pre_cap = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity',dictionary_3C)[0]
            pre_cap_power = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity_power',dictionary_3C)[0]
            preinstalled_capacity = pre_cap + pre_cap_power
            add_cap = get_cluster_element_variable(cluster,subnode,'new_capacity',dictionary_3C)
            if not type(add_cap) == int:
                add_cap = add_cap['values'][0]
            add_cap_power = get_cluster_element_variable(cluster,subnode,'new_power_capacity',dictionary_3C)
            if not type(add_cap_power) == int:
                add_cap_power = add_cap_power['values'][0]
            added_capacity = add_cap + add_cap_power
            max_cap = get_cluster_element_parameter(cluster,subnode,'max_capacity',dictionary_3C)
            max_cap_power = get_cluster_element_parameter(cluster,subnode,'max_capacity_power',dictionary_3C)
            maximum_capacity = max_cap + max_cap_power
            total_cap = preinstalled_capacity + added_capacity
            
            cluster_subnodes_caps_BE['GW'][cluster + ' ' + subnode] = {'preinstalled capacity':preinstalled_capacity,'added capacity':added_capacity,'maximum capacity':maximum_capacity,
                                    'total capacity':total_cap,'color':color,'vector':vector}
            
        if subnode in GWh_subnodes:
            pre_cap = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity',dictionary_3C)[0]
            pre_cap_energy = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity_energy',dictionary_3C)[0]
            preinstalled_capacity = pre_cap + pre_cap_energy
            add_cap = get_cluster_element_variable(cluster,subnode,'new_capacity',dictionary_3C)
            if not type(add_cap) == int:
                add_cap = add_cap['values'][0]
            add_cap_energy = get_cluster_element_variable(cluster,subnode,'new_energy_capacity',dictionary_3C)
            if not type(add_cap_energy) == int:
                add_cap_energy = add_cap_energy['values'][0]
            added_capacity = add_cap + add_cap_energy
            max_cap = get_cluster_element_parameter(cluster,subnode,'max_capacity',dictionary_3C)
            max_cap_energy = get_cluster_element_parameter(cluster,subnode,'max_capacity_energy',dictionary_3C)
            maximum_capacity = max_cap + max_cap_energy
            total_cap = preinstalled_capacity + added_capacity
            
            cluster_subnodes_caps_BE['GWh'][cluster + ' ' + subnode] = {'preinstalled capacity':preinstalled_capacity,'added capacity':added_capacity,'maximum capacity':maximum_capacity,
                                    'total capacity':total_cap,'color':color,'vector':vector}
            
        if subnode in kt_h_subnodes:
            pre_cap = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity',dictionary_3C)[0]
            pre_cap_power = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity_power',dictionary_3C)[0]
            preinstalled_capacity = pre_cap + pre_cap_power
            add_cap = get_cluster_element_variable(cluster,subnode,'new_capacity',dictionary_3C)
            if not type(add_cap) == int:
                add_cap = add_cap['values'][0]
            add_cap_power = get_cluster_element_variable(cluster,subnode,'new_power_capacity',dictionary_3C)
            if not type(add_cap_power) == int:
                add_cap_power = add_cap_power['values'][0]
            added_capacity = add_cap + add_cap_power
            max_cap = get_cluster_element_parameter(cluster,subnode,'max_capacity',dictionary_3C)
            max_cap_power = get_cluster_element_parameter(cluster,subnode,'max_capacity_power',dictionary_3C)
            maximum_capacity = max_cap + max_cap_power
            total_cap = preinstalled_capacity + added_capacity
            
            cluster_subnodes_caps_BE['kt_h'][cluster + ' ' + subnode] = {'preinstalled capacity':preinstalled_capacity,'added capacity':added_capacity,'maximum capacity':maximum_capacity,
                                    'total capacity':total_cap,'color':color,'vector':vector}
        if subnode in kt_subnodes:
            pre_cap = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity',dictionary_3C)[0]
            pre_cap_energy = get_cluster_element_parameter(cluster,subnode,'pre_installed_capacity_energy',dictionary_3C)[0]
            preinstalled_capacity = pre_cap + pre_cap_energy
            add_cap = get_cluster_element_variable(cluster,subnode,'new_capacity',dictionary_3C)
            if not type(add_cap) == int:
                add_cap = add_cap['values'][0]
            add_cap_energy = get_cluster_element_variable(cluster,subnode,'new_energy_capacity',dictionary_3C)
            if not type(add_cap_energy) == int:
                add_cap_energy = add_cap_energy['values'][0]
            added_capacity = add_cap + add_cap_energy
            max_cap = get_cluster_element_parameter(cluster,subnode,'max_capacity',dictionary_3C)
            max_cap_energy = get_cluster_element_parameter(cluster,subnode,'max_capacity_energy',dictionary_3C)
            maximum_capacity = max_cap + max_cap_energy
            total_cap = preinstalled_capacity + added_capacity
            
            cluster_subnodes_caps_BE['kt'][cluster + ' ' + subnode] = {'preinstalled capacity':preinstalled_capacity,'added capacity':added_capacity,'maximum capacity':maximum_capacity,
                                    'total capacity':total_cap,'color':color,'vector':vector}
        
    

#%% total production and consumption
cluster_subnodes_e_produced = dict()
cluster_subnodes_h2_produced = dict()
cluster_subnodes_ng_produced = dict()
for cluster in clusters:
    cluster_subnodes_e_produced[cluster] = get_cluster_subnodes_names_from_variable("e_produced",cluster,dictionary_3C)
    cluster_subnodes_h2_produced[cluster] = get_cluster_subnodes_names_from_variable("h2_produced",cluster,dictionary_3C)
    cluster_subnodes_ng_produced[cluster] = get_cluster_subnodes_names_from_variable("ng_produced",cluster,dictionary_3C)

cluster_subnodes_producing = dict()
for cluster in clusters:
    cluster_subnodes_producing[cluster] = merge_lists(cluster_subnodes_e_produced[cluster],cluster_subnodes_h2_produced[cluster],cluster_subnodes_ng_produced[cluster])
variables = ["e_produced","h2_produced","ng_produced","ng_consumed","co2_produced","e_consumed","h2_consumed","ng_consumed","co2_consumed","co2_captured"]

cluster_subnodes_total_production = dict()
table_cluster_subnodes_total_production = dict()
for cluster in clusters:
    cluster_subnodes_total_production[cluster] = get_total_value_of_variables_in_cluster_subnodes(variables,cluster,cluster_subnodes_producing[cluster],dictionary_3C)
    table_cluster_subnodes_total_production[cluster] = transform_into_table(cluster_subnodes_total_production[cluster])

#%% PCCC and DAC capture
# total volumes of co2 emitted, air captured and released on cluster level
variables = ["co2_emitted","co2_air_captured","co2_released"]
cluster_emission = dict()
table_cluster_emission = dict()
for cluster in clusters:
    cluster_emission[cluster] = get_total_value_of_variables_in_cluster(variables,cluster,dictionary_3C)
    table_cluster_emission[cluster] = transform_into_table(cluster_emission[cluster])
# intra cluster level DAC and PCCC technologies co2 released, captured and exiting
cluster_subnodes_PCCC_DAC = dict()
for cluster in clusters:
    cluster_subnodes_PCCC_DAC[cluster] = get_cluster_subnodes_names_from_variable("co2_captured",cluster,dictionary_3C)

variables = ["co2_captured","co2_released","co2_exiting","e_consumed","h2_consumed","ng_consumed"]
cluster_subnodes_total_capture_co2 = dict()
table_cluster_subnodes_total_capture_co2 = dict()
for cluster in clusters:
    cluster_subnodes_total_capture_co2[cluster] =  get_total_value_of_variables_in_cluster_subnodes(variables,cluster,cluster_subnodes_PCCC_DAC[cluster],dictionary_3C) 
    table_cluster_subnodes_total_capture_co2[cluster] = transform_into_table(cluster_subnodes_total_capture_co2[cluster])
    



"""
nodes_PCCC_DAC = add_variables_in_list(variables, nodes_PCCC_DAC)

variables = ["co2_captured","co2_released","co2_exiting"]
"ng_consumed","e_consumed",
"co2_emitted","co2_air_captured","co2_released" on cluster level

total_capture_co2 =  get_total_value_of_variables_in_nodes(variables,nodes_PCCC_DAC,dictionary) 
table_total_capture_co2 = transform_into_table(total_capture_co2)
"""

#%% Load shedding and shifting

dsr_subnodes = ["LOAD_SHIFTING","LOAD_SHEDDING_1","LOAD_SHEDDING_2","LOAD_SHEDDING_4","LOAD_SHEDDING_8","LOAD_SHEDDING_UNLIM"]
if dsr_subnodes[0] in dictionary_3C["solution"]["elements"]["INLAND"]["sub_elements"]:
    variables = ["load_increase","load_reduction","new_capacity"]
    total_dsr = dict()
    total_dsr = get_total_value_of_variables_in_cluster_subnodes(variables,"INLAND",dsr_subnodes,dictionary_3C)
    table_total_dsr = transform_into_table(total_dsr)  
    monthly_dsr = dict()

    for node in dsr_subnodes:
        monthly_dsr[node] = dict()
        monthly_dsr[node]['load_reduction']= zoom_on_variable_in_cluster_subnode("INLAND",'load_reduction',node,'Month',dictionary_3C)


#%% ng_demand

total_ng_demand = get_total_value_of_global_parameters(["demand_ng_heat","demand_ng_industry","demand_ng_to_h2","demand_ng_transport","demand_ng_transport2"],dictionary_3C)
table_total_ng_demand = transform_into_table(total_ng_demand)

#%% h2 demand

total_h2_demand = get_total_value_of_global_parameters(["demand_h2_industry","demand_h2_transport","demand_h2_transport2",'demand_h2_heat'],dictionary_3C)
table_total_h2_demand = transform_into_table(total_h2_demand)

#%% electricity demand

total_el_demand = get_total_value_of_global_parameters(["demand_el","demand_el_ht","daily_demand_for_electric_vehicle"],dictionary_3C)
table_total_el_demand = transform_into_table(total_el_demand)

#%% energy not served
## CLUSTER LEVEL

variables = ["e_ens","ng_ens","h2_ens"]
total_cluster_ens = dict() 
table_total_cluster_ens = dict()
for cluster in clusters:
    total_cluster_ens[cluster] = get_total_value_of_variables_in_cluster(variables,cluster,dictionary_3C)
    table_total_cluster_ens[cluster] = transform_into_table(total_cluster_ens[cluster])    



costs = ["value_of_lost_load_e","value_of_lost_load_ng","value_of_lost_load_h2"]
total_cost = ["total_cost_e_ens","total_cost_ng_ens","total_cost_h2_ens",]
vars_costs = [variables,costs,total_cost]
total_cluster_cost_ens = dict()
table_total_cluster_cost_ens = dict()
for cluster in clusters:
    total_cluster_cost_ens[cluster] = get_total_value_of_variables_and_costs_in_cluster(vars_costs,cluster,dictionary_3C)
    table_total_cluster_cost_ens[cluster] = transform_into_table(total_cluster_cost_ens[cluster])

#%% fuel costs

cluster_subnodes_technologies = dict()
for cluster in clusters:
    cluster_subnodes_technologies[cluster] = get_cluster_subnodes_names_from_parameter(cluster,"fuel_cost",dictionary_3C)

e_produced= "e_produced"
conversion_efficiency = "conversion_efficiency"
fuel_cost = "fuel_cost"

cluster_subnodes_technology_costs = dict()
for cluster in clusters:
    cluster_subnodes_technology_costs[cluster] = get_cluster_subnodes_technology_costs_from_nodes(cluster_subnodes_technologies[cluster],cluster,e_produced,conversion_efficiency,fuel_cost,dictionary_3C)


    
table_cluster_subnodes_technology_costs = {}
for cluster in clusters:
    table_cluster_subnodes_technology_costs[cluster] = transform_into_table(cluster_subnodes_technology_costs[cluster])


#%% capacity factor

# electricity production
capacity_factor_e_produced = dict()
table_capacity_factor_e_produced = dict()
for cluster in clusters:
    capacity_factor_e_produced[cluster] = get_capacity_factors_from_capacity("e_produced",cluster,cluster_subnodes_e_produced[cluster],cluster_subnodes_capacities[cluster],dictionary_3C)
    table_capacity_factor_e_produced[cluster] = transform_into_table(capacity_factor_e_produced[cluster])

#capacity_factor_e = get_capacity_factors_from_parameter("e_produced",["BIOMASS_POWER_PLANT","CHP","WASTE_POWER_PLANT"],"max_capacity",dictionary)

# hydrogen production
#nodes_h2_produced = remove_variables_from_list(["ELECTROLYSIS_PLANTS"],nodes_h2_produced)
capacity_factor_h2_produced = dict()
capacity_factor_e_cons = dict()
table_capacity_factor_h2_produced = dict()
table_capacity_factor_e_cons = dict()
for cluster in clusters:
    capacity_factor_h2_produced[cluster] = get_capacity_factors_from_capacity("h2_produced",cluster,cluster_subnodes_h2_produced[cluster],cluster_subnodes_capacities[cluster],dictionary_3C)
    capacity_factor_e_cons[cluster] = get_capacity_factors_from_capacity("e_consumed",cluster,cluster_subnodes_h2_produced[cluster],cluster_subnodes_capacities[cluster],dictionary_3C)
    table_capacity_factor_h2_produced[cluster] = transform_into_table(capacity_factor_h2_produced[cluster])
    table_capacity_factor_e_cons[cluster] = transform_into_table(capacity_factor_e_cons[cluster])
    

# natural gas production
capacity_factor_ng_produced = dict()
table_capacity_factor_ng_produced = dict()
for cluster in clusters:
    capacity_factor_ng_produced[cluster] = get_capacity_factors_from_capacity("ng_produced",cluster,cluster_subnodes_ng_produced[cluster],cluster_subnodes_capacities[cluster],dictionary_3C)
    table_capacity_factor_ng_produced[cluster] = transform_into_table(capacity_factor_ng_produced[cluster])

# co2 capture
capacity_factor_PCCC_produced = dict()
table_capacity_factor_PCCC_produced = dict()
for cluster in clusters:
    capacity_factor_PCCC_produced[cluster] = get_capacity_factors_from_capacity("co2_captured",cluster,cluster_subnodes_PCCC_DAC[cluster],cluster_subnodes_capacities[cluster],dictionary_3C)
    table_capacity_factor_PCCC_produced[cluster] = transform_into_table(capacity_factor_PCCC_produced[cluster])


# merging dicitonaries
capacity_factors_production = dict()
table_capacity_factors = dict()
for cluster in clusters:
    capacity_factors_production[cluster] = merge_dictionaries(capacity_factor_e_produced[cluster],capacity_factor_h2_produced[cluster],capacity_factor_ng_produced[cluster],capacity_factor_PCCC_produced[cluster])
    table_capacity_factors[cluster] = transform_into_table(capacity_factors_production[cluster])
    
# STORAGE CAPACITY FACTORS

# h2 storage
#capacity_factor_h2_storage = get_capacity_factors_from_capacity("h2_charged",["H2_STORAGE"],capacities,dictionary)

# ELECTRICITY IMPORT/EXPORT CAPACITY FACTOS

# electricity import and export
#capacity_factor_import = get_capacity_factors_from_parameter("imported",["E_INTERCONNECTION"],"import_capacity",dictionary)
#capacity_factor_export = get_capacity_factors_from_parameter("export",["E_INTERCONNECTION"],"import_capacity",dictionary)

#%%
# INTERCONNECTION CAPACITIES AND ACCORDING ENERGY VOLUMES ON ANNUAL BASIS
# INCLUDING FOR ELECTRICITY: INTERCONNECTIONS BETWEEN BELGIUM AND NEIGHBOURING COUNTRIES AND BETWEEN ZEEBRUGGE-INLAND-OFFSHORE    
# INCLUDING FOR 

interconnections = dict()

# elec interconnection between BELGIUM and interconnected countries
for neighbour in clusters_neighbours:
    interconnections[neighbour] = dict()
    interconnections[neighbour]['el export capacity'] = get_cluster_parameter(neighbour,'export_capacity',dictionary_3C)[0]
    interconnections[neighbour]['el import capacity'] = get_cluster_parameter(neighbour,'import_capacity',dictionary_3C)[0]
    interconnections[neighbour]['el imported volume'] = sum(x for x in get_cluster_variable(neighbour,"imported",dictionary_3C)['values'])
    interconnections[neighbour]['el exported volume'] = sum(x for x in get_cluster_variable(neighbour,"exported",dictionary_3C)['values'])
    
# H2, ng and elec interconnection within BELGIUM (between ZB/OFF/INLAND)
for interc in clusters_interconnection_elec:
    interconnections[interc] = dict()
    interconnections[interc]['new capacity'] = get_cluster_variable(interc,'new_capacity',dictionary_3C)['values'][0]
    interconnections[interc]['pre installed capacity'] = get_cluster_parameter(interc,"pre_installed_capacity",dictionary_3C)[0]
    interconnections[interc]['Total capacity'] = interconnections[interc]['new capacity'] +  interconnections[interc]['pre installed capacity']
    interconnections[interc]['total volume in'] = sum(x for x in get_cluster_variable(interc,"e_forward_in",dictionary_3C)['values']) - sum(x for x in get_cluster_variable(interc,"e_reverse_out",dictionary_3C)['values'])
    interconnections[interc]['total volume out'] = sum(x for x in get_cluster_variable(interc,"e_forward_out",dictionary_3C)['values']) - sum(x for x in get_cluster_variable(interc,"e_reverse_in",dictionary_3C)['values'])
for interc in clusters_interconnection_mol:    
    interconnections[interc] = dict()
    interconnections[interc]['new capacity forward'] = get_cluster_variable(interc,'new_capacity_forward',dictionary_3C)['values'][0]
    interconnections[interc]['new capacity reverse'] = get_cluster_variable(interc,'new_capacity_reverse',dictionary_3C)['values'][0]
    interconnections[interc]['pre installed capacity forward'] = get_cluster_parameter(interc,"pre_installed_capacity_forward",dictionary_3C)[0]
    interconnections[interc]['pre installed capacity reverse'] = get_cluster_parameter(interc,"pre_installed_capacity_reverse",dictionary_3C)[0]
    interconnections[interc]['Total capacity'] = interconnections[interc]['new capacity forward'] +  interconnections[interc]['pre installed capacity forward']
    interconnections[interc]['total volume in'] = sum(x for x in get_cluster_variable(interc,"flow_forward_in",dictionary_3C)['values']) - sum(x for x in get_cluster_variable(interc,"flow_reverse_out",dictionary_3C)['values'])
    interconnections[interc]['total volume out'] = sum(x for x in get_cluster_variable(interc,"flow_forward_out",dictionary_3C)['values']) - sum(x for x in get_cluster_variable(interc,"flow_reverse_in",dictionary_3C)['values'])
# H2 and/or ng interconnections between BELGIUM and interconnected countries
Zeebrugge_interconnections = ["H2_INTERCONNECTION_FR","H2_INTERCONNECTION_UK","H2_INTERCONNECTION_NV","NG_INTERCONNECTION_FR","NG_INTERCONNECTION_NV","NG_INTERCONNECTION_UK","REGAS","REGAS_H2","REGAS_GREEN"]
for interc in Zeebrugge_interconnections:
    interconnections[interc] = dict()
    if interc == "NG_INTERCONNECTION_FR":
        interconnections[interc]['import capacity'] = get_cluster_element_parameter("ZEEBRUGGE",interc,'import_capacity',dictionary_3C)[0]
        interconnections[interc]['imported'] = sum(x for x in get_cluster_element_variable("ZEEBRUGGE",interc,"imported",dictionary_3C)['values'])
    else:
        interconnections[interc]['export capacity'] = get_cluster_element_parameter("ZEEBRUGGE",interc,'export_capacity',dictionary_3C)[0]
        interconnections[interc]['import capacity'] = get_cluster_element_parameter("ZEEBRUGGE",interc,'import_capacity',dictionary_3C)[0]
        interconnections[interc]['imported'] = sum(x for x in get_cluster_element_variable("ZEEBRUGGE",interc,"imported",dictionary_3C)['values'])
        interconnections[interc]['exported'] = sum(x for x in get_cluster_element_variable("ZEEBRUGGE",interc,"exported",dictionary_3C)['values'])
INLAND_interconnections = ["H2_INTERCONNECTION_DE","H2_INTERCONNECTION_NL","NG_INTERCONNECTION_DE","NG_INTERCONNECTION_FR","NG_INTERCONNECTION_NL"]
for interc in INLAND_interconnections:
    if interc == "NG_INTERCONNECTION_FR":
        interconnections[interc]['export capacity'] = get_cluster_element_parameter("INLAND",interc,'export_capacity',dictionary_3C)[0]
        interconnections[interc]['exported'] = sum(x for x in get_cluster_element_variable("INLAND",interc,"exported",dictionary_3C)['values'])
    else:
        interconnections[interc] = dict() 
        interconnections[interc]['export capacity'] = get_cluster_element_parameter("INLAND",interc,'export_capacity',dictionary_3C)[0]
        interconnections[interc]['import capacity'] = get_cluster_element_parameter("INLAND",interc,'import_capacity',dictionary_3C)[0]
        interconnections[interc]['imported'] = sum(x for x in get_cluster_element_variable("INLAND",interc,"imported",dictionary_3C)['values'])
        interconnections[interc]['exported'] = sum(x for x in get_cluster_element_variable("INLAND",interc,"exported",dictionary_3C)['values'])
#%% capex, fom, vom


# CAPEX
cluster_subnodes_capex_no_sto = dict()
for cluster in clusters:
    cluster_subnodes_capex_no_sto[cluster] = get_capex_from_cluster_subnodes_capacity(cluster,"yearly_capex",cluster_subnodes_capacities[cluster],dictionary_3C)

cluster_subnodes_capex_sto = dict()

mapping_technologies_capex = {'NG_STORAGE power':['NG_STORAGE','yearly_capex_power'],'NG_STORAGE energy':['NG_STORAGE','yearly_capex_energy'],'BATTERIES power':['BATTERIES','yearly_capex_power'],'BATTERIES energy':['BATTERIES','yearly_capex_energy'],'PUMPED_HYDRO power':['PUMPED_HYDRO','yearly_capex_power'],'PUMPED_HYDRO energy':['PUMPED_HYDRO','yearly_capex_energy'],'H2_STORAGE power':['H2_STORAGE','yearly_capex_power'],'H2_STORAGE energy':['H2_STORAGE','yearly_capex_energy'],'CO2_STORAGE power':['CO2_STORAGE','yearly_capex_power'],'H2O_STORAGE power':['H2O_STORAGE','yearly_capex_power'],'H2O_STORAGE energy':['H2O_STORAGE','yearly_capex_energy'],'CO2_STORAGE energy':['CO2_STORAGE','yearly_capex_energy']}
for cluster in clusters:
    cluster_subnodes_capex_sto[cluster] = dict()
    for parameter in cluster_subnodes_cap_storage[cluster]:
        capex = get_cluster_element_parameter(cluster,mapping_technologies_capex[parameter][0], mapping_technologies_capex[parameter][1], dictionary_3C)[0]
        capacity = cluster_subnodes_cap_storage[cluster][parameter]["Added capacity"]
        cluster_subnodes_capex_sto[cluster][parameter] = {"Capex":capex,"Added capacity":capacity,"Installation cost":capex*capacity}
"""      
    capex_B_power[cluster] = get_cluster_element_parameter(cluster,"BATTERIES", "yearly_capex_power", dictionary_3C)
    cap_B_power[cluster] = cluster_subnodes_cap_storage[cluster]["BATTERIES power"]["Added capacity"]
    capex_sto[cluster]["BATTERIES power"] = {"Capex":capex_B_power[cluster],"Added capacity":cap_B_power[cluster],"Installation cost":capex_B_power[cluster]*cap_B_power[cluster]}
    
    capex_B_energy[cluster] = get_cluster_element_parameter(cluster,"BATTERIES", "yearly_capex_energy", dictionary_3C)
    cap_B_energy[cluster] = cluster_subnodes_cap_storage[cluster]["BATTERIES energy"]["Added capacity"]
    capex_sto[cluster]["BATTERIES energy"] = {"Capex":capex_B_energy[cluster],"Added capacity":cap_B_energy[cluster],"Installation cost":capex_B_energy[cluster]*cap_B_energy[cluster]}
    
    capex_PH_power[cluster] = get_cluster_element_parameter(cluster,"PUMPED_HYDRO", "yearly_capex_power", dictionary_3C)
    cap_PH_power[cluster] = cluster_subnodes_cap_storage[cluster]["PUMPED_HYDRO power"]["Added capacity"]
    capex_sto[cluster]["PUMPED_HYDRO power"] = {"Capex":capex_PH_power[cluster],"Added capacity":cap_PH_power[cluster],"Installation cost":capex_PH_power[cluster]*cap_PH_power[cluster]}

    capex_PH_energy[cluster] = get_cluster_element_parameter(cluster,"PUMPED_HYDRO", "yearly_capex_energy", dictionary_3C)
    cap_PH_energy[cluster] = cluster_subnodes_cap_storage[cluster]["PUMPED_HYDRO energy"]["Added capacity"]
    capex_sto[cluster]["PUMPED_HYDRO energy"] = {"Capex":capex_PH_energy[cluster],"Added capacity":cap_PH_energy[cluster],"Installation cost":capex_PH_energy[cluster]*cap_PH_energy[cluster]}
"""
cluster_subnodes_capex_all = dict()
table_cluster_subnodes_capex_all = dict()
for cluster in clusters:
    cluster_subnodes_capex_all[cluster] = merge_dictionaries(cluster_subnodes_capex_no_sto[cluster],cluster_subnodes_capex_sto[cluster])
    table_cluster_subnodes_capex_all[cluster] = transform_into_table(cluster_subnodes_capex_all[cluster])

# FOM

cluster_subnodes_fom_no_sto = dict()
for cluster in clusters:
    cluster_subnodes_fom_no_sto[cluster] = get_fom_from_cluster_subnodes_capacity(cluster,"fom",cluster_subnodes_capacities[cluster],dictionary_3C)

cluster_subnodes_fom_sto = dict()
mapping_technologies_fom = {'NG_STORAGE power':['NG_STORAGE','fom_power'],'NG_STORAGE energy':['NG_STORAGE','fom_energy'],'H2O_STORAGE power':['H2O_STORAGE','fom_power'],'H2O_STORAGE energy':['H2O_STORAGE','fom_energy'],'BATTERIES power':['BATTERIES','fom_power'],'BATTERIES energy':['BATTERIES','fom_energy'],'PUMPED_HYDRO power':['PUMPED_HYDRO','fom_power'],'PUMPED_HYDRO energy':['PUMPED_HYDRO','fom_energy'],'H2_STORAGE power':['H2_STORAGE','fom_power'],'H2_STORAGE energy':['H2_STORAGE','fom_energy'],'CO2_STORAGE power':['CO2_STORAGE','yearly_fom_power'],'CO2_STORAGE energy':['CO2_STORAGE','yearly_fom_energy']}
for cluster in clusters:
    cluster_subnodes_fom_sto[cluster] = dict()
    for parameter in cluster_subnodes_cap_storage[cluster]:
        fom = get_cluster_element_parameter(cluster,mapping_technologies_fom[parameter][0], mapping_technologies_fom[parameter][1], dictionary_3C)[0]
        capacity = cluster_subnodes_cap_storage[cluster][parameter]["Added capacity"]
        cluster_subnodes_fom_sto[cluster][parameter] = {"Fom":fom,"Total capacity":capacity,"tot fom cost":fom*capacity}

cluster_subnodes_fom_all = dict()
table_cluster_subnodes_fom_all = dict()
for cluster in clusters:
    cluster_subnodes_fom_all[cluster] = merge_dictionaries(cluster_subnodes_fom_no_sto[cluster],cluster_subnodes_fom_sto[cluster])
    table_cluster_subnodes_fom_all[cluster] = transform_into_table(cluster_subnodes_fom_all[cluster])

# VOM
"""
cluster_subnodes_vom_no_sto = dict()
for cluster in clusters:
    cluster_subnodes_vom_no_sto[cluster] = get_vom_from_cluster_subnodes_capacity(cluster,"vom",cluster_subnodes_capacities[cluster],dictionary_3C)

cluster_subnodes_vom_sto = dict()
mapping_technologies_vom = {'NG_STORAGE power':['NG_STORAGE','vom_power'],'NG_STORAGE energy':['NG_STORAGE','vom_energy'],'BATTERIES power':['BATTERIES','vom_power'],'BATTERIES energy':['BATTERIES','vom_energy'],'PUMPED_HYDRO power':['PUMPED_HYDRO','vom_power'],'PUMPED_HYDRO energy':['PUMPED_HYDRO','vom_energy'],'H2_STORAGE power':['H2_STORAGE','vom_power'],'H2_STORAGE energy':['H2_STORAGE','vom_energy']}
for cluster in clusters:
    cluster_subnodes_vom_sto[cluster] = dict()
    for parameter in cluster_subnodes_cap_storage[cluster]:
        vom = get_cluster_element_parameter(cluster,mapping_technologies_vom[parameter][0], mapping_technologies_vom[parameter][1], dictionary_3C)
        capacity = cluster_subnodes_cap_storage[cluster][parameter]["Added capacity"]
        cluster_subnodes_vom_sto[cluster][parameter] = {"vom":vom,"Added capacity":capacity,"Installation cost":vom*capacity}

cluster_subnodes_vom_all = dict()
table_cluster_subnodes_vom_all = dict()
for cluster in clusters:
    cluster_subnodes_vom_all[cluster] = merge_dictionaries(cluster_subnodes_vom_no_sto[cluster],cluster_subnodes_vom_sto[cluster])
    table_cluster_subnodes_vom_all[cluster] = transform_into_table(cluster_subnodes_vom_all[cluster])
"""
cluster_subnodes_vom_e_produced = dict()
cluster_subnodes_vom_h2_produced = dict()
cluster_subnodes_vom_ng_produced = dict()

# TO BE REVIEWED
cluster_subnodes_vom_co2_captured = dict()
cluster_subnodes_vom_PH = dict()
cluster_subnodes_vom_e_charged = dict()
cluster_subnodes_vom_all = dict()
table_cluster_subnodes_vom_all = dict()
for cluster in clusters:  
    cluster_subnodes_vom_e_produced[cluster] = get_vom_from_cluster_subnodes_variable(cluster,"vom", "e_produced",cluster_subnodes_e_produced[cluster], dictionary_3C)
    cluster_subnodes_vom_h2_produced[cluster] = get_vom_from_cluster_subnodes_variable(cluster,"vom", "h2_produced",cluster_subnodes_h2_produced[cluster], dictionary_3C)
    cluster_subnodes_vom_ng_produced[cluster] = get_vom_from_cluster_subnodes_variable(cluster,"vom", "ng_produced",cluster_subnodes_ng_produced[cluster], dictionary_3C)
    #vom_co2_captured[cluster] = get_vom_from_cluster_subnodes_variable(cluster,"vom", "co2_captured", nodes_PCCC_DAC[:-1], dictionary_3C)
    #vom_PH[cluster] = get_vom_from_cluster_subnodes_variable(cluster,"vom","e_charged",["PUMPED_HYDRO"], dictionary_3C)
    #vom_e_charged[cluster] = {}
    #vom_e_charged[cluster]["PUMPED_HYDRO power"] = vom_PH["PUMPED_HYDRO"]

    cluster_subnodes_vom_all[cluster] = merge_dictionaries(cluster_subnodes_vom_e_produced[cluster],cluster_subnodes_vom_h2_produced[cluster],cluster_subnodes_vom_ng_produced[cluster])
    table_cluster_subnodes_vom_all[cluster] = transform_into_table(cluster_subnodes_vom_all[cluster])




# TO DO
cluster_subnodes_total_cost_old = dict()
table_cluster_subnodes_total_cost_old = dict()
for cluster in clusters:
    cluster_subnodes_total_cost_old[cluster] = get_total_cluster_subnodes_cost(cluster_subnodes_capex_all[cluster], cluster_subnodes_fom_all[cluster], cluster_subnodes_vom_all[cluster])
    table_cluster_subnodes_total_cost_old[cluster] = transform_into_table(cluster_subnodes_total_cost_old[cluster])

#%%
"""
cluster_subnodes_caps_costs = dict()
table_cluster_subnodes_caps_costs = dict()
for cluster in clusters:
    cluster_subnodes_caps_costs[cluster] = merge_dictionaries(cluster_subnodes_total_cost_old[cluster],cluster_subnodes_capacities_tot[cluster])
    table_cluster_subnodes_caps_costs[cluster] = transform_into_table(cluster_subnodes_caps_costs[cluster])
"""

#%%
# TOTAL COST per cluster DICTIONARY


# total cost conmprised of yearly existing cost (capex_existing + fom new), yearly new (capex + fom new), VOM and fuel costs (to the applicable nodes)
cluster_subnodes_total_cost = dict()
table_cluster_subnodes_total_cost = dict()
for cluster in clusters:
    cluster_subnodes_total_cost[cluster] = dict()
    cluster_subnodes = dictionary_3C["solution"]["elements"][cluster]["sub_elements"].keys()
    for subnode in cluster_subnodes:
        if subnode != "BALANCES":
            fix_cost_existing =  get_cluster_element_parameter(cluster,subnode,'yearly_existing_cost',dictionary_3C)[0]# yearly_existing_cost parameter in nodes
            fix_cost_new = get_objective_element(cluster,subnode,'fix_cost',dictionary_3C) # fix_cost in objective
            fix_cost_new_sto = get_objective_element(cluster,subnode,'fix_cost_power',dictionary_3C) + get_objective_element(cluster,subnode,'fix_cost_energy',dictionary_3C)
            var_cost = get_objective_element(cluster,subnode,'var_cost',dictionary_3C) # var_cost in objective
            fuel_cost = get_objective_element(cluster,subnode,'fuel_cost',dictionary_3C)# fuel cost in objective
            CO2_cost = get_objective_element(cluster,subnode,'co2_cost',dictionary_3C) # cà2_cost in objective
            import_cost =  get_objective_element(cluster,subnode,'import_cost',dictionary_3C) # equals the cost for import minus the revenues one gets for export. 
            export_cost = get_objective_element(cluster,subnode,'export_cost',dictionary_3C)
            CO2_capt_cost = get_objective_element(cluster,subnode,'co2_capt_cost',dictionary_3C)
            total_cost  = fix_cost_existing + fix_cost_new + fix_cost_new_sto + var_cost + fuel_cost + CO2_cost + import_cost + export_cost - CO2_capt_cost# + import_cost + export_cost
            
            cluster_subnodes_total_cost[cluster][subnode] = {'existing fix cost':fix_cost_existing,'new fix cost':fix_cost_new,'new fix cost storage':fix_cost_new_sto,'Variable cost':
                var_cost,'fuel cost':fuel_cost,'CO2 cost':CO2_cost,'CO2 capt cost':- CO2_capt_cost,'import cost':import_cost,'export cost':export_cost,'total cost':total_cost}
            
    table_cluster_subnodes_total_cost[cluster] = transform_into_table(cluster_subnodes_total_cost[cluster])

cluster_subnodes_sorted = dict()
cluster_subnodes_total_cost_sorted = dict()
table_cluster_subnodes_total_cost_sorted = dict()
for cluster in clusters:
    cluster_subnodes_total_cost_sorted[cluster] = dict()
    cluster_subnodes_sorted[cluster] = sorted(cluster_subnodes_total_cost[cluster].keys(), key = lambda x:(cluster_subnodes_total_cost[cluster][x]['total cost']), reverse=True)
    for subnode in cluster_subnodes_sorted[cluster]:
        cluster_subnodes_total_cost_sorted[cluster][subnode] = cluster_subnodes_total_cost[cluster][subnode]
    table_cluster_subnodes_total_cost_sorted[cluster] = transform_into_table(cluster_subnodes_total_cost_sorted[cluster])
#.items()
"""
cluster_subnodes_total_cost_sorted = dict()
for cluster in clusters:
    cluster_subnodes_total_cost_sorted[cluster] = sorted(table_cluster_subnodes_total_cost[cluster].items(), key = lambda kv:(kv[1], kv[0]))
    """
    
#%% TOTAL COST FOR BELGIUM: OFFSHORE, ZEEBRUGGE, INLAND, ELECTRICITY IMPORTS FROM NEIGHBOURING COUNTRIES, HVDC costs between OFFSHORE, ZEEBRUGGE and INLAND

electricity_subnodes = get_subnodes_energy_vector('energy_electricity',dictionary_3C)
carbon_dioxide_subnodes = get_subnodes_energy_vector('energy_carbon_dioxide',dictionary_3C)
natural_gas_subnodes = get_subnodes_energy_vector('energy_natural_gas',dictionary_3C)
hydrogen_subnodes = get_subnodes_energy_vector('energy_hydrogen',dictionary_3C)



    
cluster_subnodes_total_cost_BE = dict()
table_cluster_subnodes_total_cost_BE = dict()
for cluster in clusters_belgium:
    cluster_subnodes = dictionary_3C["solution"]["elements"][cluster]["sub_elements"].keys()
    for subnode in cluster_subnodes:
        if subnode != "BALANCES":
            fix_cost_existing =  get_cluster_element_parameter(cluster,subnode,'yearly_existing_cost',dictionary_3C)[0]# yearly_existing_cost parameter in nodes
            fix_cost_new = get_objective_element(cluster,subnode,'fix_cost',dictionary_3C) # fix_cost in objective
            fix_cost_new_sto = get_objective_element(cluster,subnode,'fix_cost_power',dictionary_3C) + get_objective_element(cluster,subnode,'fix_cost_energy',dictionary_3C)
            var_cost = get_objective_element(cluster,subnode,'var_cost',dictionary_3C) # var_cost in objective
            var_cost_sto = get_objective_element(cluster,subnode,'var_cost_power',dictionary_3C) + get_objective_element(cluster,subnode,'var_cost_energy',dictionary_3C)
            fuel_cost = get_objective_element(cluster,subnode,'fuel_cost',dictionary_3C)# fuel cost in objective
            CO2_cost = get_objective_element(cluster,subnode,'co2_cost',dictionary_3C) # cà2_cost in objective
            CO2_capt_cost = get_objective_element(cluster,subnode,'co2_capt_cost',dictionary_3C)
            import_cost =  get_objective_element(cluster,subnode,'import_cost',dictionary_3C) # equals the cost for import minus the revenues one gets for export. 
            export_cost = get_objective_element(cluster,subnode,'export_cost',dictionary_3C)
            curt_cost = get_objective_element(cluster,subnode,'curt_cost',dictionary_3C)
            grid_cost = get_objective_element(cluster,subnode,'grid_cost',dictionary_3C)
            total_cost  = fix_cost_existing + fix_cost_new + fix_cost_new_sto + var_cost + var_cost_sto + fuel_cost + CO2_cost + import_cost + export_cost + curt_cost + grid_cost - CO2_capt_cost # + import_cost + export_cost
            if subnode in electricity_subnodes:
                color = '#2c2c2c'
                vector = 'electricity'
            elif subnode in carbon_dioxide_subnodes:
                color = '#79b932'
                vector = 'CO2'
            elif subnode in natural_gas_subnodes:
                color = '#c55a11'
                vector = 'natural_gas'
            elif subnode in hydrogen_subnodes:
                 color = '#2e75b6'
                 vector = 'hydrogen'
            else:
                color = 'black'
                vector = 'not specified'
            cluster_subnodes_total_cost_BE[cluster + ' ' + subnode] = {'existing fix cost':fix_cost_existing,'new fix cost':fix_cost_new,'new fix cost storage':fix_cost_new_sto,'Variable cost':
                var_cost + var_cost_sto,'fuel cost':fuel_cost,'CO2 cost':CO2_cost,'CO2 capt cost': - CO2_capt_cost,'import cost':import_cost,'export cost':export_cost,'curtailment cost':
                    curt_cost,'grid cost':grid_cost,'total cost':total_cost,'color':color,'vector':vector}
for cluster in clusters_neighbours:
    import_cost =  get_cluster_objective(cluster, 'import_cost', dictionary_3C)
    export_revenue = - get_cluster_objective(cluster, 'export_cost', dictionary_3C)
    total_cost = import_cost + export_revenue
    if cluster in electricity_subnodes:
        color = '#2c2c2c'
        vector = 'electricity'
    elif cluster in carbon_dioxide_subnodes:
        color = '#79b932'
        vector = 'CO2'
    elif cluster in natural_gas_subnodes:
        color = '#c55a11'
        vector = 'natural_gas'
    elif cluster in hydrogen_subnodes:
        color = '#2e75b6'
        vector = 'hydrogen'
    else:
        color = 'black'
        vector = 'not specified'
    cluster_subnodes_total_cost_BE[cluster + ' EL_INTERCONNECTION'] = {'existing fix cost':0,'new fix cost':0,'new fix cost storage':0,'Variable cost':
        0,'fuel cost':0,'CO2 cost':0,'CO2 capt cost': 0,'import cost':import_cost,'export cost':export_revenue,'curtailment cost':
        0,'grid cost':0,'total cost':total_cost,'color':color,'vector':vector}

for cluster in clusters_interconnection_elec:
    fix_cost = get_cluster_objective(cluster, 'fix_cost', dictionary_3C)
    var_cost = get_cluster_objective(cluster, 'var_cost', dictionary_3C)
    fix_cost_existing = get_cluster_parameter(cluster,'yearly_existing_cost',dictionary_3C)[0]
    total_cost = var_cost + fix_cost + fix_cost_existing
    if cluster in electricity_subnodes:
        color = '#2c2c2c'
        vector = 'electricity'
    elif cluster in carbon_dioxide_subnodes:
        color = '#79b932'
        vector = 'CO2'
    elif cluster in natural_gas_subnodes:
        color = '#c55a11'
        vector = 'natural_gas'
    elif cluster in hydrogen_subnodes:
        color = '#2e75b6'
        vector = 'hydrogen'
    else:
        color = 'black'
        vector = 'not specified'
    cluster_subnodes_total_cost_BE[cluster + ' EL_INTERCONNECTION'] = {'existing fix cost':fix_cost_existing,'new fix cost':fix_cost,'new fix cost storage':0,'Variable cost':
        var_cost,'fuel cost':0,'CO2 cost':0, 'CO2 capt cost': 0,'import cost':0,'export cost':0,'curtailment cost':
        0,'grid cost':0,'total cost':total_cost,'color':color,'vector':vector}
        
for cluster in clusters_interconnection_mol:
    if cluster[:7] == 'PIPE_H2':
        fix_cost = get_cluster_objective(cluster, 'fix_cost', dictionary_3C)
        var_cost = get_cluster_objective(cluster, 'var_cost', dictionary_3C)
        fix_cost_existing = get_cluster_parameter(cluster,'yearly_existing_cost',dictionary_3C)[0]
        total_cost = fix_cost_existing + fix_cost + var_cost
        color = '#2e75b6'
        vector = 'hydrogen'
        cluster_subnodes_total_cost_BE[cluster + ' H2_INTERCONNECTION'] = {'existing fix cost':fix_cost_existing,'new fix cost':fix_cost,'new fix cost storage':0,'Variable cost':
        var_cost,'fuel cost':0,'CO2 cost':0,'CO2 capt cost': 0,'import cost':0,'export cost':0,'curtailment cost':
        0,'grid cost':0,'total cost':total_cost,'color':color,'vector':vector}
    elif cluster[:7] == 'PIPE_NG':
        fix_cost = get_cluster_objective(cluster, 'fix_cost', dictionary_3C)
        var_cost = get_cluster_objective(cluster, 'var_cost', dictionary_3C)
        fix_cost_existing = get_cluster_parameter(cluster,'yearly_existing_cost',dictionary_3C)[0]
        total_cost = fix_cost_existing + fix_cost + var_cost
        color = '#c55a11'
        vector = 'natural_gas'
        cluster_subnodes_total_cost_BE[cluster + ' NG_INTERCONNECTION'] = {'existing fix cost':fix_cost_existing,'new fix cost':fix_cost,'new fix cost storage':0,'Variable cost':
        var_cost,'fuel cost':0,'CO2 cost':0,'CO2 capt cost': 0,'import cost':0,'export cost':0,'curtailment cost':
        0,'grid cost':0,'total cost':total_cost,'color':color,'vector':vector}
  
# Cost of co2 taxes on the demand of natural gas
            
demand_ch4 = sum(total_ng_demand[i]['Total value'] for i in total_ng_demand) - total_cluster_ens['INLAND']['ng_ens']
total_cost_co2_demand = get_total_value_of_global_parameters(['co2_emission_cost'],dictionary_3C)['co2_emission_cost']['Total value'] * get_total_value_of_global_parameters(['spec_co2_emission'],dictionary_3C)['spec_co2_emission']['Total value'] * demand_ch4
CO2_cost = total_cost_co2_demand
total_cost = CO2_cost
color = '#c55a11'
vector = 'natural_gas'
cluster_subnodes_total_cost_BE['Natural gas demand CO2 taxes'] = {'existing fix cost':0,'new fix cost': 0,'new fix cost storage':0,'Variable cost':
0,'fuel cost':0,'CO2 cost': CO2_cost, 'CO2 capt cost': 0,'import cost':0,'export cost':0,'curtailment cost':
0,'grid cost':0,'total cost':total_cost,'color':color,'vector':vector}

#%% Cost of energy

total_cost_tech = sum(cluster_subnodes_total_cost_BE[node]['total cost'] for node in cluster_subnodes_total_cost_BE)

total_cost_ens = total_cluster_cost_ens['INLAND']['total_cost_e_ens'] + total_cluster_cost_ens['INLAND']['total_cost_ng_ens'] + total_cluster_cost_ens['INLAND']['total_cost_h2_ens']

total_cost = total_cost_tech + total_cost_ens 

total_demand_el = sum(total_el_demand[demand]['Total value'] for demand in total_el_demand)
total_demand_h2 = sum(total_h2_demand[demand]['Total value'] for demand in total_h2_demand)
total_demand_ng = sum(total_ng_demand[demand]['Total value'] for demand in total_ng_demand)

total_demand = total_demand_el + total_demand_h2 + total_demand_ng
total_ens =  sum(total_cluster_ens['INLAND'][x] for x in total_cluster_ens['INLAND'])

cost_of_energy = (total_cost - total_cost_ens)/(total_demand - total_ens)
total_co2_emitted = get_cluster_variable('INLAND','total_co2_emitted',dictionary_3C)['values'][0] - get_cluster_variable('ZEEBRUGGE','total_co2_captured',dictionary_3C)['values'][0]

print(f'Total cost [MEur] :{total_cost}')
print(f'Total cost ens [MEur] :{total_cost_ens}')
print(f'cost of energy [Eur/MWh] :{cost_of_energy * 1000}')

data = [[total_cost,'MEur'],[total_ens,'GWh'],[total_cost_ens,'MEur'],[cost_of_energy*1000,'Eur/MWh'],[total_co2_emitted,'kt']]
index = ['Total cost','Energy not served','Total cost ens','Cost of energy','Total CO2 emitted']
table_total_cost = pd.DataFrame(data,columns=['Value','Unit'],index=index)
save_table_into_csv(table_total_cost,title + "/Total_costs")

"""    
BE_subnodes_sorted = dict()
cluster_subnodes_total_cost_BE_sorted = dict()
table_cluster_subnodes_total_cost_BE_sorted = dict()
    
BE_subnodes_sorted = sorted(cluster_subnodes_total_cost_BE.keys(), key = lambda x:(cluster_subnodes_total_cost_BE[x]['total cost']), reverse=True)
for subnode in BE_subnodes_sorted:
    cluster_subnodes_total_cost_BE_sorted[subnode] = cluster_subnodes_total_cost_BE[subnode]
table_cluster_subnodes_total_cost_BE_sorted = transform_into_table(cluster_subnodes_total_cost_BE_sorted)
"""
    
    
#%% Cost of interclusters interconnection

interconnection = ['HV_OFF_ZB EL_INTERCONNECTION','HV_ZB_INL EL_INTERCONNECTION','PIPE_H2_OFF_ZB H2_INTERCONNECTION','PIPE_H2_ZB_INL H2_INTERCONNECTION']

total_cost_interco = sum([cluster_subnodes_total_cost_BE[i]['total cost'] for i in interconnection])
new_cost_interco = sum([cluster_subnodes_total_cost_BE[i]['new fix cost'] for i in interconnection]) + sum([cluster_subnodes_total_cost_BE[i]['Variable cost'] for i in interconnection])

print(f'Total cost interconnections [MEur] :{total_cost_interco}')    
print(f'New cost interconnections [MEur] :{new_cost_interco}')  

inst_cost_interco_el = sum([get_cluster_variable(i,'new_capacity',dictionary_3C)['values'][0] * get_cluster_parameter(i,'capex',dictionary_3C)[0] for i in clusters_interconnection_elec])
inst_cost_interco_mol = sum([get_cluster_variable(i,'new_capacity_forward',dictionary_3C)['values'][0] * get_cluster_parameter(i,'capex',dictionary_3C)[0] for i in clusters_interconnection_mol])  
inst_cost_interco = inst_cost_interco_el + inst_cost_interco_mol
print(f'Installation cost interconnections [MEur] :{inst_cost_interco}')

if 'lifetime' in dictionary_3C["model"]["nodes"]['HV_OFF_ZB']["parameters"]:
    fom_cost_interco_el = sum([get_cluster_variable(i,'new_capacity',dictionary_3C)['values'][0] * get_cluster_parameter(i,'fom',dictionary_3C)[0] * get_cluster_parameter(i,'lifetime',dictionary_3C)[0] for i in clusters_interconnection_elec])
else:
    fom_cost_interco_el = sum([get_cluster_variable(i,'new_capacity',dictionary_3C)['values'][0] * get_cluster_parameter(i,'fom',dictionary_3C)[0] * get_cluster_parameter(i,'lifetime',dictionary_3C)[0] for i in ['HV_ZB_INL']]) + sum([get_cluster_variable(i,'new_capacity',dictionary_3C)['values'][0] * get_cluster_parameter(i,'fom',dictionary_3C)[0] * get_cluster_parameter(i,'lifetime_lines',dictionary_3C)[0] for i in ['HV_OFF_ZB']])
fom_cost_interco_mol = sum([get_cluster_variable(i,'new_capacity_forward',dictionary_3C)['values'][0] * get_cluster_parameter(i,'fom',dictionary_3C)[0] * get_cluster_parameter(i,'lifetime',dictionary_3C)[0] for i in clusters_interconnection_mol])
fom_cost_interco = fom_cost_interco_el + fom_cost_interco_mol
print(f'FOM cost interconnections [MEur] :{fom_cost_interco}')

total_cost_interco = inst_cost_interco + fom_cost_interco
print(f'Total cost interconnections [MEur] :{total_cost_interco}')

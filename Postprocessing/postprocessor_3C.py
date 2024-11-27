# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:01:12 2021

@author: Jocelyn Mbenoun
"""

# =============================================================================
# Post processor file for the 3 cluster model. This file is created based on the 
# post processor file of the one cluster model. underneath, additional code and/or 
# function needs are highlighted. All code should be applicable to the 3 cluster model, 
# since only adapted code, ready for the 3 cluster model is pasted in this file.
# =============================================================================


# =============================================================================
# 
# =============================================================================

import matplotlib.pyplot as plt
import pandas as pd


# -----------------------------------------------------------------------------

# Approach to define additional functions for the different layers.

#%% functions

# functions to get parameter, variables and nodes
def get_cluster_variable(node,variable,dictionary): 
    # get value of "variable" from "cluster" as a list in "node" from data in "dictionary"  
    return dictionary["solution"]["elements"][node]["variables"][variable]

def get_cluster_element_variable(cluster,element,variable,dictionary): 
    # get value of "variable" from "cluster" as a list in "node" from data in "dictionary"  
    if "variables" in dictionary["solution"]["elements"][cluster]["sub_elements"][element]:
        if variable in dictionary["solution"]["elements"][cluster]["sub_elements"][element]["variables"]:
            return dictionary["solution"]["elements"][cluster]["sub_elements"][element]["variables"][variable]
        else:
            return 0
    else:
        return 0
    #return dictionary["solution"]["elements"][cluster]["sub_elements"][element]["variables"][variable]

def get_cluster_parameter(node,parameter,dictionary):
    # get value of "parameter" as a list in "node" from data in "dictionary" 
    return dictionary["model"]["nodes"][node]["parameters"][parameter]

def get_cluster_element_parameter(cluster,element,parameter,dictionary):
    # get value of "parameter" as a list in "node" from data in "dictionary" 
    if "parameters" in dictionary["model"]["nodes"][cluster]["sub_nodes"][element]:
        if parameter in dictionary["model"]["nodes"][cluster]["sub_nodes"][element]["parameters"]:
            return dictionary["model"]["nodes"][cluster]["sub_nodes"][element]["parameters"][parameter]
        else:
            return [0]
    else:
        return [0]



"""
def get_all_cluster_names(dictionary): 
    # get the names of all nodes as a list from data in "dictionary"
    dic_nodes = dictionary["model"]["nodes"]
    nodes_name = []
    for node in dic_nodes:
        nodes_name.append(node)
    return nodes_name

def get_all_cluster_subnodes_names(cluster,dictionary): 
    # get the names of all nodes as a list from data in "dictionary"
    dic_nodes = dictionary["model"]["nodes"]
    nodes_name = []
    for node in dic_nodes:
        nodes_name.append(node)
    return nodes_name
"""

def get_cluster_names_from_variable(variable,dictionary): 
    # get the names of nodes as a list in which the variable named "variable" is used
    dic_nodes = dictionary["model"]["nodes"]
    nodes_name = []
    for node in dic_nodes:
        if variable in dic_nodes[node]["variables"]:
            nodes_name.append(node)
    return nodes_name

def get_cluster_subnodes_names_from_variable(variable,cluster,dictionary): 
    # get the names of nodes as a list in which the variable named "variable" is used
    dic_nodes = dictionary["solution"]["elements"][cluster]["sub_elements"]
    nodes_name = []
    for node in dic_nodes:
        if "variables" in dic_nodes[node]:
            if variable in dic_nodes[node]["variables"]:
                nodes_name.append(node)
    return nodes_name


def get_cluster_names_from_parameter(parameter,dictionary):
    # get the names of global nodes as a list in which the "parameter" is used
    dic_nodes = dictionary["model"]["nodes"]
    nodes_name = []
    for node in dic_nodes:
        if parameter in dic_nodes[node]["parameters"]:
            nodes_name.append(node)
    return nodes_name

def get_cluster_subnodes_names_from_parameter(cluster,parameter,dictionary):
    # get the names of nodes as a list in which the "parameter" is used
    dic_nodes = dictionary["model"]["nodes"][cluster]["sub_nodes"]
    nodes_name = []
    for node in dic_nodes:
        if parameter in dic_nodes[node]["parameters"]:
            nodes_name.append(node)
    return nodes_name

# functions to post process the data



def get_cluster_capacities_from_nodes(nodes,name_capacity,name_capacity_0,name_capacity_max,dictionary):
    # Create a dictionary with the capacity, the limit on the capacity and the preinstalled capacity for each node in the list
    # "nodes". "name_capacity" is the name of the variable corresponding to the capacity, "name_capacity_0" is the name used for
    # parameter corresponding to the preinstalled capacity and "name_capacity_max" is the parameter corresponding to the maximum 
    # capacity that can be installed
    # if no preinstalled capacity or max capacity used in the code, just insert a empty char for those inputs like that: ''
    capacities = {}
    dic_nodes_var = dictionary["solution"]["elements"]
    dic_nodes_par = dictionary["model"]["nodes"]
    for node in nodes:  
        if name_capacity in dic_nodes_var[node]["variables"]:
            capacity = get_cluster_variable(node,name_capacity,dictionary)
            capacity = capacity['values'][0]
        else:
            capacity = 0
        if name_capacity_0 in dic_nodes_par[node]["parameters"]:
            capacity_0 = get_cluster_parameter(node,name_capacity_0,dictionary)
            capacity_0 = capacity_0[0]
        else:
            capacity_0 = 0
        if name_capacity_max in dic_nodes_par[node]["parameters"]:
            capacity_max = get_cluster_parameter(node,name_capacity_max,dictionary)
            capacity_max = capacity_max[0]
        else:
            capacity_max = 'Not given'
        total_capacity = capacity_0 + capacity
        key = node
        capacities[key] = {"Preinstalled capacity":capacity_0,"Added capacity":capacity, "Total capacity":total_capacity, "Max capacity": capacity_max}
    return capacities

def get_cluster_subnodes_capacities_from_nodes(nodes,cluster,name_capacity,name_capacity_0,name_capacity_max,dictionary):
    # Create a dictionary with the capacity, the limit on the capacity and the preinstalled capacity for each node in the list
    # "nodes". "name_capacity" is the name of the variable corresponding to the capacity, "name_capacity_0" is the name used for
    # parameter corresponding to the preinstalled capacity and "name_capacity_max" is the parameter corresponding to the maximum 
    # capacity that can be installed
    # if no preinstalled capacity or max capacity used in the code, just insert a empty char for those inputs like that: ''
    capacities = {}
    dic_nodes_var = dictionary["solution"]["elements"][cluster]["sub_elements"]
    dic_nodes_par = dictionary["model"]["nodes"][cluster]["sub_nodes"]
    for node in nodes:  
        if name_capacity in dic_nodes_var[node]["variables"]:
            capacity = get_cluster_element_variable(cluster,node,name_capacity,dictionary)
            capacity = capacity['values'][0]
        else:
            capacity = 0
        if name_capacity_0 in dic_nodes_par[node]["parameters"]:
            capacity_0 = get_cluster_element_parameter(cluster,node,name_capacity_0,dictionary)
            capacity_0 = capacity_0[0]
        else:
            capacity_0 = 0
        if name_capacity_max in dic_nodes_par[node]["parameters"]:
            capacity_max = get_cluster_element_parameter(cluster,node,name_capacity_max,dictionary)
            capacity_max = capacity_max[0]
        else:
            capacity_max = 'Not given'
        total_capacity = capacity_0 + capacity
        key = node
        capacities[key] = {"Preinstalled capacity":capacity_0,"Added capacity":capacity, "Total capacity":total_capacity, "Max capacity": capacity_max}
    return capacities

def get_cluster_subnodes_capacities_from_storage(nodes,cluster,name_capacity_power,name_capacity_0_power,name_capacity_max_power,name_capacity_energy,name_capacity_0_energy,name_capacity_max_energy,dictionary):
    # Create a dictionary with the capacity of energy and power, the limit on those capacities and their preinstalled capaciies 
    # for each node in the list "nodes". "name_capacity" is the name of the variable corresponding to the capacity, "name_capacity_0" 
    # is the name used for parameter corresponding to the preinstalled capacity and "name_capacity_max" is the parameter
    # corresponding to the maximum capacity that can be installed
    # if no preinstalled capacity or max capacity used in the code, just insert a empty char for those inputs like that ''
    cap_storage = {}
    #dic_nodes = dictionary["solution"]["elements"][cluster]["sub_elements"]
    dic_nodes_var = dictionary["solution"]["elements"][cluster]["sub_elements"]
    for node in nodes:
        # for power
        if name_capacity_power in dic_nodes_var[node]["variables"]:
            capacity = get_cluster_element_variable(cluster,node,name_capacity_power,dictionary)
            capacity = capacity['values'][0]
        else:
            capacity = 0
        if name_capacity_0_power in dictionary["model"]["nodes"][cluster]["sub_nodes"][node]["parameters"]:
            capacity_0 = get_cluster_element_parameter(cluster,node,name_capacity_0_power,dictionary)
            capacity_0 = capacity_0[0]
        else:
            capacity_0 = 0
        if name_capacity_max_power in dictionary["model"]["nodes"][cluster]["sub_nodes"][node]["parameters"]:
            capacity_max = get_cluster_element_parameter(cluster,node,name_capacity_max_power,dictionary)
            capacity_max = capacity_max[0]
        else:
            capacity_max = 'Not given'
        total_capacity = capacity_0 + capacity
        key = node+' power'
        cap_storage[key] = {"Preinstalled capacity":capacity_0,"Added capacity":capacity, "Total capacity":total_capacity, "Max capacity": capacity_max}
        # for energy
        if name_capacity_energy in dic_nodes_var[node]["variables"]:
            capacity = get_cluster_element_variable(cluster,node,name_capacity_energy,dictionary)
            capacity = capacity['values'][0]
        else:
            capacity = 0
        if name_capacity_0_energy in dictionary["model"]["nodes"][cluster]["sub_nodes"][node]["parameters"]:
            capacity_0 = get_cluster_element_parameter(cluster,node,name_capacity_0_energy,dictionary)
            capacity_0 = capacity_0[0]
        else:
            capacity_0 = 0
        if name_capacity_max_energy in dictionary["model"]["nodes"][cluster]["sub_nodes"][node]["parameters"]:
            capacity_max = get_cluster_element_parameter(cluster,node,name_capacity_max_energy,dictionary)
            capacity_max = capacity_max[0]
        else:
            capacity_max = 'Not given'
        total_capacity = capacity_0 + capacity
        key = node+' energy'
        cap_storage[key] = {"Preinstalled capacity":capacity_0,"Added capacity":capacity, "Total capacity":total_capacity, "Max capacity": capacity_max}
    return cap_storage



def get_cluster_subnodes_technology_costs_from_nodes(nodes,cluster,e_produced,conversion_efficiency,fuel_cost,dictionary):
    # Create a dictionary with the capacity, the limit on the capacity and the preinstalled capacity for each node in the list
    # "nodes". "name_capacity" is the name of the variable corresponding to the capacity, "name_capacity_0" is the name used for
    # parameter corresponding to the preinstalled capacity and "name_capacity_max" is the parameter corresponding to the maximum 
    # capacity that can be installed
    # if no preinstalled capacity or max capacity used in the code, just insert a empty char for those inputs like that: ''
    capacities = {}
    dic_nodes_var = dictionary["solution"]["elements"][cluster]["sub_elements"]
    dic_nodes_par = dictionary["model"]["nodes"][cluster]["sub_nodes"]
    for node in nodes:  
        if e_produced in dic_nodes_var[node]["variables"]:
            e_prod = sum(get_cluster_element_variable(cluster,node,e_produced,dictionary)['values'])
        else:
            capacity = 0
            e_prod = 0
        if conversion_efficiency in dic_nodes_par[node]["parameters"]:
            eff = get_cluster_element_parameter(cluster,node,conversion_efficiency,dictionary)[0]
        else:
            eff = 'Not given'
        if fuel_cost in dic_nodes_par[node]["parameters"]:
            fu_cost = get_cluster_element_parameter(cluster,node,fuel_cost,dictionary)[0]
        else:
            fu_cost = 'Not given'
        key = node
        capacities[key] = {"conversion_efficiency":eff,"e_produced":e_prod, "fuel_price": fu_cost, "total_fuel_cost":fu_cost*e_prod/eff}
    return capacities



def get_total_value_of_variables_in_cluster_subnodes(variables,cluster,nodes,dictionary):
    # create a dictionary with sum of of all elements of each vectorial variable in the list "variables" for each node in the list "nodes"
    total_variables = {}
    dic_nodes = dictionary["solution"]["elements"][cluster]["sub_elements"]
    for node in nodes:
        total_variables[node] = {} # initialization
        for variable in variables:
            if variable in dic_nodes[node]["variables"]:
                total = sum(dic_nodes[node]["variables"][variable]['values'])
            else:
                total = 0
            total_variables[node][variable] = total
    return total_variables



def get_total_value_of_global_parameters(parameters,dictionary):
    total_parameters = {}
    dic_nodes = dictionary["model"]["global_parameters"]
    for parameter in parameters:
        if parameter in dic_nodes:
            total = sum(dic_nodes[parameter])
        else:
            total = 0
        total_parameters[parameter] = {"Total value":total}
    return total_parameters





def get_capacity_factors_from_capacity(variable,cluster,nodes,capacities,dictionary):
    # create a dictionary calculating the capacity factor of each node in the list "nodes" using the dictionary "capacities" 
    # created by the function "get_capacities_from_nodes" and "get_capacities_from_storage" and the name of variable "variable"
    # as references for the capacity factor
    capacity_factors = {}
    dic_nodes = dictionary["solution"]["elements"][cluster]["sub_elements"]
    for node in nodes:
        if node in capacities:
            capacity = capacities[node]["Total capacity"]
            if capacities[node]["Total capacity"] > 0:
                total_production = sum(dic_nodes[node]["variables"][variable]['values'])
                capacity_factor = sum(dic_nodes[node]["variables"][variable]['values'])/(capacities[node]["Total capacity"]*len(dic_nodes[node]["variables"][variable]['values']))
            else:
                total_production = 0
                capacity_factor = "No capacity installed"
            capacity_factors[node +' '+variable] = {"Capacity": capacity, "Total production": total_production, "Capacity factor":capacity_factor}   
    return capacity_factors

"""
def get_capacity_factors_from_parameter(variable,nodes,parameter,dictionary):
    # create a dictionary calculating the capacity factor of each node in the list "nodes" using the parameter "parameter" 
    # and the name of variable "variable" as references for the capacity factor
    capacity_factors = {}
    dic_nodes_var = dictionary["solution"]["nodes"]
    dic_nodes_par = dictionary["model"]["nodes"]
    for node in nodes:
        capacity = dic_nodes_par[node]["parameters"][parameter][0]
        if parameter in dic_nodes_par[node]["parameters"]:
            total_production = sum(dic_nodes_var[node]["variables"][variable])
            capacity_factor = sum(dic_nodes_var[node]["variables"][variable])/(dic_nodes_par[node]["parameters"][parameter][0]*len(dic_nodes_var[node]["variables"][variable]))
            capacity_factors[node+' '+variable] = {"Capacity": capacity, "Total production": total_production, "Capacity factor":capacity_factor}   
    return capacity_factors
"""




def get_total_value_of_variables_in_cluster(variables,cluster,dictionary):
    # create a dictionary with sum of of all elements of each vectorial variable in the list "variables" for each node in the list "nodes"
    total_variables = {}
    cluster_vars = dictionary["solution"]["elements"][cluster]["variables"]
    for variable in variables:
        if variable in cluster_vars:
            
            total_variables[variable] = sum(cluster_vars[variable]['values'])
        else:
            total_variables[variable] = 0
    return total_variables


def get_total_value_of_variables_and_costs_in_cluster(vars_costs,cluster,dictionary):
    # create a dictionary with sum of of all elements of each vectorial variable in the list "variables" for each node in the list "nodes"
    total_variables = {}
    dic_nodes_var = dictionary["solution"]["elements"][cluster]["variables"]
    dic_nodes_par = dictionary["model"]["nodes"][cluster]["parameters"]
    for i in range(len(vars_costs[0])):
        if vars_costs[0][i] in dic_nodes_var:
            ens = sum(dic_nodes_var[vars_costs[0][i]]['values'])
            cost = dic_nodes_par[vars_costs[1][i]][0]
            total_variables[vars_costs[0][i]] = ens
            total_variables[vars_costs[1][i]] = cost
            total_variables[vars_costs[2][i]] = ens*cost
    return total_variables







def get_capex_from_cluster_subnodes_capacity(cluster,capex_name,capacities,dictionary):
    # create a dictionary calculating the total capex cost of each node where a capacity is calculated 
    # from the name used for the capex in node and the dictionary of capacity
    capex_all = {}
    dic_nodes_par = dictionary["model"]["nodes"][cluster]["sub_nodes"]
    for node in capacities:
        if capex_name in dic_nodes_par[node]["parameters"]:
            capex =  dic_nodes_par[node]["parameters"][capex_name][0]
            #capex =  dic_nodes_par[node]["parameters"][capex_name][0]/dic_nodes_par[node]["parameters"]["lifetime"][0]
        else:
            capex = 0
        tot_cap = capacities[node]["Added capacity"]
        inst_cost = capex * tot_cap 
        capex_all[node] = {"Capex":capex,"Added capacity":tot_cap,"Installation cost":inst_cost}
    return capex_all
    
def get_fom_from_cluster_subnodes_capacity(cluster,fom_name,capacities,dictionary):
    # create a dictionary calculating the total fixed operation and maintenance cost of each node where 
    # a capacity is calculated from the name used for the fom in node and the dictionary of capacity
    fom_all = {}
    dic_nodes_par = dictionary["model"]["nodes"][cluster]["sub_nodes"]
    for node in capacities:
        if fom_name in dic_nodes_par[node]["parameters"]:
            fom =  dic_nodes_par[node]["parameters"][fom_name][0]
        else:
            fom = 0
        tot_cap = capacities[node]["Total capacity"]
        fom_cost = fom * tot_cap 
        fom_all[node] = {"Fom":fom,"Total capacity":tot_cap,"tot fom cost":fom_cost}
    return fom_all    

def get_vom_from_cluster_subnodes_variable(cluster,vom_name,variable,nodes,dictionary):
    vom_all = {}
    dic_nodes_var = dictionary["solution"]["elements"][cluster]["sub_elements"]
    dic_nodes_par = dictionary["model"]["nodes"][cluster]["sub_nodes"]
    for node in nodes:
        total_prod = sum(dic_nodes_var[node]["variables"][variable]['values'])
        if vom_name in dic_nodes_par[node]["parameters"]:
            vom = dic_nodes_par[node]["parameters"][vom_name][0]
        else:
            vom = 0
        vom_cost = total_prod * vom
        vom_all[node] = {"Vom":vom,"Total production":total_prod,"tot vom cost":vom_cost}    
    return vom_all

def get_total_cluster_subnodes_cost(capex_dict,fom_dict,vom_dict):
    total_cost = {}
    for node in capex_dict:
        capacity = fom_dict[node]["Total capacity"]
        inst_cost = capex_dict[node]["Installation cost"]
        if node in fom_dict:
            fom_tot = fom_dict[node]["tot fom cost"]
        else:
            fom_tot = 0
        if node in vom_dict:
            vom_tot = vom_dict[node]["tot vom cost"]
        else:
            vom_tot = 0
        tot_cost = inst_cost + fom_tot + vom_tot
        total_cost[node] = {"Total capacity":capacity,"Installation cost":inst_cost,"Fixed OM cost":fom_tot,"Variable OM cost":vom_tot,"Total Cost":tot_cost}
    return total_cost
    

def get_cluster_objective(cluster, objective_elem,dictionary):
    # Get the element "objective_elem from the objective results of subnode in cluster
    if "objectives" in dictionary["solution"]["elements"][cluster]:
        if "named" not in dictionary["solution"]["elements"][cluster]["objectives"]:
            return 'check this subnodes objective'
        elif objective_elem in dictionary["solution"]["elements"][cluster]["objectives"]["named"]:
                return dictionary["solution"]["elements"][cluster]["objectives"]['named'][objective_elem]
        else:
            return 0
    else:
        return 0

def get_objective_element(cluster,subnode,objective_elem,dictionary):
    # Get the element "objective_elem from the objective results of subnode in cluster
    if "objectives" in dictionary["solution"]["elements"][cluster]["sub_elements"][subnode]:
        if "named" not in dictionary["solution"]["elements"][cluster]["sub_elements"][subnode]["objectives"]:
            return 'check this subnodes objective'
        elif objective_elem in dictionary["solution"]["elements"][cluster]["sub_elements"][subnode]["objectives"]["named"]:
                return dictionary["solution"]["elements"][cluster]["sub_elements"][subnode]["objectives"]['named'][objective_elem]
        else:
            return 0
    else:
        return 0
    
    
def get_subnodes_energy_vector(energy_vector,dictionary):
    nodes = []
    for cluster in dictionary["model"]["nodes"].keys():
        #if "parameters" in dictionary["model"]["nodes"][cluster]:
            #if energy_vector in dictionary["model"]["nodes"][cluster]["parameters"]:
                #nodes.append(cluster)
                
        if "sub_nodes" in dictionary["model"]["nodes"][cluster]:
            for subnode in dictionary["model"]["nodes"][cluster]["sub_nodes"].keys():
                if "parameters" in dictionary["model"]["nodes"][cluster]["sub_nodes"][subnode]:
                    if energy_vector in dictionary["model"]["nodes"][cluster]["sub_nodes"][subnode]["parameters"]:
                        nodes.append(subnode)
    return nodes

def get_duals_from_hyperedge(constraint,hyperedge,dictionary):
    return dictionary["solution"]["elements"][hyperedge]["constraints"][constraint]['dual']

def get_duals_from_cluster(constraint,cluster,dictionary):
    return dictionary["solution"]["elements"][cluster]["constraints"][constraint]['dual']

    
"""    
def get_unnamed_objectives(cluster,dictionary):
    if "objectives" in dictionary["solution"]["elements"][cluster]["sub_elements"][subnode]:
        if "unnamed" in dictionary["solution"]["elements"][cluster]["sub_elements"][subnode]["objective"]:
"""

# functions to get timeseries
#get_timeseries_in_cluster(clusters_belgium,dictionary_3C)

#get_timeseries_in_
# functions to convert the type of the data data 




def merge_dictionaries(*dictionaries):
    # merge dictionaries together
    dict_merged = {}
    for dictionary in dictionaries:
        dict_merged.update(dictionary)
    return dict_merged

def merge_lists(*lists):
    # merge dictionaries together
    list_merged = []
    for list in lists:
        list_merged += list
    return list_merged

def transform_into_table(data):
    # Convert dictionary into dataframe table
    table = pd.DataFrame.from_dict(data, orient='index')
    return table
    
def save_table_into_csv(table,table_name):
    # save dataframe table as a csv file
    table.to_csv(r'' + table_name+'.csv')

def save_table_into_excel(table,table_name):
    # save dataframe table as a csv file
    table.to_excel(r'' + table_name+'.xlsx')

# functions to zoom on data
def zoom_on_variable_in_cluster(cluster,variable,zoom,dictionary): 
    var = dictionary["solution"]["elements"][cluster]["variables"][variable]['values']
    variable_zoomed = []
    if zoom == 'Hour':
        variable_zoomed = var
    if zoom == 'Day':
        n_hour = 24
        for x in range(0,len(var),n_hour):
            if x + n_hour < len(var):
                variable_zoomed.append(sum(var[x:x+n_hour]))
            else:
                variable_zoomed.append(sum(var[x:]))
    elif zoom == 'Week':
        n_hour = 7 * 24
        for x in range(0,len(var),n_hour):
            if x + n_hour < len(var):
                variable_zoomed.append(sum(var[x:x+n_hour]))
            else:
                variable_zoomed.append(sum(var[x:]))
    elif zoom == 'Month':
        n_hour = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] * int(len(var)/8760)
        n_hour = [x * 24 for x in n_hour] 
        n = 0
        for x in range(0,12 * int(len(var)/8760)):
            variable_zoomed.append(sum(var[n:n+n_hour[x]]))
            n += n_hour[x]
    return variable_zoomed

def zoom_on_variable_in_cluster_subnode(cluster,variable,node,zoom,dictionary): 
    var = dictionary["solution"]["elements"][cluster]["sub_elements"][node]["variables"][variable]['values']
    variable_zoomed = []
    if zoom == 'Hour':
        variable_zoomed = var
    if zoom == 'Day':
        n_hour = 24
        for x in range(0,len(var),n_hour):
            if x + n_hour < len(var):
                variable_zoomed.append(sum(var[x:x+n_hour]))
            else:
                variable_zoomed.append(sum(var[x:]))
    elif zoom == 'Week':
        n_hour = 7 * 24
        for x in range(0,len(var),n_hour):
            if x + n_hour < len(var):
                variable_zoomed.append(sum(var[x:x+n_hour]))
            else:
                variable_zoomed.append(sum(var[x:]))
    elif zoom == 'Month':
        n_hour = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] * int(len(var)/8760)
        n_hour = [x * 24 for x in n_hour] 
        n = 0
        for x in range(0,12 * int(len(var)/8760)):
            variable_zoomed.append(sum(var[n:n+n_hour[x]]))
            n += n_hour[x]
    return variable_zoomed

def zoom_on_global_parameter(global_parameter,zoom,dictionary): 
    var = dictionary["model"]["global_parameters"][global_parameter]
    variable_zoomed = []
    if zoom == 'Hour':
        variable_zoomed = var
    if zoom == 'Day':
        n_hour = 24
        for x in range(0,len(var),n_hour):
            if x + n_hour < len(var):
                variable_zoomed.append(sum(var[x:x+n_hour]))
            else:
                variable_zoomed.append(sum(var[x:]))
    elif zoom == 'Week':
        n_hour = 7 * 24
        for x in range(0,len(var),n_hour):
            if x + n_hour < len(var):
                variable_zoomed.append(sum(var[x:x+n_hour]))
            else:
                variable_zoomed.append(sum(var[x:]))
    elif zoom == 'Month':
        n_hour = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] * int(len(var)/8760)
        n_hour = [x * 24 for x in n_hour] 
        n = 0
        for x in range(0, 12*int(len(var)/8760)):
            variable_zoomed.append(sum(var[n:n+n_hour[x]]))
            n += n_hour[x]
    return variable_zoomed

# functions to create graph
def plot_timeseries(axes, x, y, bot, lab):

  # Plot the inputs x,y in the provided color
  axes.bar(x, y, bottom = bot, label = lab)

  # Set the x-axis label
  #axes.set_xlabel(xlabel)

  # Set the y-axis label
  #axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  #axes.tick_params('y', colors=color)
  

# ---------------------------------------------------------------------------------

#Approach to have the cluster layers inside the end results --> much complication inside functions

"""
def get_nodes_names_from_parameter_3C(parameter,clusters,dictionary):
    # get the names of nodes as a list in which the "parameter" is used
    dic_nodes = dict()
    nodes_name = dict()
    for cluster in clusters:
        dic_nodes[cluster] = dictionary["model"]["nodes"][cluster]["sub_nodes"] 
        nodes_name[cluster] = []
        for node in dic_nodes[cluster]:
            if parameter in dic_nodes[cluster][node]["parameters"]:
                nodes_name[cluster].append(node)

    return nodes_name
"""
def get_nodes_names_from_parameter_3C(parameter,clusters,dictionary):
    # get the names of nodes as a Dictionay in which the "parameter" is used
    dic_nodes = dictionary["model"]["nodes"]
    nodes_name = {'other':[]}
    for node in dic_nodes:
        if node in clusters:
            #dic_nodes[node] = dictionary["model"]["nodes"][node]["sub_nodes"] 
            nodes_name[node] = []
            for sub_node in dic_nodes[node]["sub_nodes"]:
                if parameter in dic_nodes[node]["sub_nodes"][sub_node]["parameters"]:
                    nodes_name[node].append(sub_node)
        else:
            if parameter in dic_nodes[node]["parameters"]:
                nodes_name['other'].append(node)
    return nodes_name



# functions to post process the data
    
def get_capacities_from_nodes_3C(nodes,name_capacity,name_capacity_0,name_capacity_max,clusters,dictionary):
    # Create a dictionary with the capacity, the limit on the capacity and the preinstalled capacity for each node in the dictionary
    # "nodes". "name_capacity" is the name of the variable corresponding to the capacity, "name_capacity_0" is the name used for
    # parameter corresponding to the preinstalled capacity and "name_capacity_max" is the parameter corresponding to the maximum 
    # capacity that can be installed
    # if no preinstalled capacity or max capacity used in the code, just insert a empty char for those inputs like that: ''
    capacities = dict()
    dic_nodes_var = dictionary["solution"]["elements"]
    dic_nodes_par = dictionary["model"]["nodes"]
    for node_category in nodes:
        if node_category in clusters:
            for node in nodes[node_category]:
                
                if name_capacity in dic_nodes_var[node]["variables"]:
                    capacity = get_variable(node,name_capacity,dictionary)
                    capacity = capacity[0]
                else:
                    capacity = 0
                if name_capacity_0 in dic_nodes_par[node]["parameters"]:
                    capacity_0 = get_parameter(node,name_capacity_0,dictionary)
                    capacity_0 = capacity_0[0]
                else:
                    capacity_0 = 0
                if name_capacity_max in dic_nodes_par[node]["parameters"]:
                    capacity_max = get_parameter(node,name_capacity_max,dictionary)
                    capacity_max = capacity_max[0]
                else:
                    capacity_max = 'Not given'
                total_capacity = capacity_0 + capacity
                key = node
                capacities[key] = {"Preinstalled capacity":capacity_0,"Added capacity":capacity, "Total capacity":total_capacity, "Max capacity": capacity_max}
    return capacities
    
# fonctions to convert the type of the data data 

    
    
# functions to zoom on data

# functions to create graph


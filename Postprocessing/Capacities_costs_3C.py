# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:42:57 2022

@author: bosquetn
"""
import matplotlib.pyplot as plt
import pandas as pd

#%% SUBNODES NAMES AND ENERGY VECTOR DEFINITION

# PASTE THE SORTED LIST HERE ONCE IT IS MADE
capa_data = cluster_subnodes_capacities_tot


capa_data_sorted = dict()
for cluster in clusters:
    capa_data_sorted[cluster] = sorted(capa_data[cluster].keys(), key = lambda x:(capa_data[cluster][x]['Total capacity']), reverse = True)
    

# Retrieve names of all cluster subnodes for which capacities are assigned
cluster_subnodes_name = dict()
for cluster in clusters:
    cluster_subnodes_name[cluster] = capa_data[cluster].keys() 
"""
# colors    
# Define dictionaries to store subnode name associated to an energy vector. Transformation technologies are assigned
# to their output energy vector.
cluster_subnodes_electricity = dict()
cluster_subnodes_hydrogen = dict()
cluster_subnodes_ng = dict()
cluster_subnodes_co2 = dict()
cluster_subnodes_by_vector = dict()
color_tech = dict()

# Fill empty energy vector dicts with the appropriate cluster subnodes
for cluster in clusters:
    cluster_subnodes_electricity[cluster] = cluster_subnodes_e_produced[cluster] + list(cluster_subnodes_cap_storage[cluster].keys())
    cluster_subnodes_hydrogen[cluster] = cluster_subnodes_h2_produced[cluster] + ["H2_STORAGE"]
    cluster_subnodes_ng[cluster] = cluster_subnodes_ng_produced[cluster] + ["NG_STORAGE"]
    cluster_subnodes_co2[cluster] = cluster_subnodes_PCCC_DAC[cluster] + ["CO2_STORAGE"]
    cluster_subnodes_by_vector[cluster] = {"electricity":cluster_subnodes_electricity[cluster],"hydrogen":cluster_subnodes_hydrogen[cluster],"ng":cluster_subnodes_ng[cluster],"co2":cluster_subnodes_co2[cluster]}
    color_tech[cluster] = dict()
    for subnode in capa_data_sorted[cluster]:
        if subnode in cluster_subnodes_electricity[cluster]:
            color_tech[cluster][subnode] = '#2c2c2c'
        if subnode in cluster_subnodes_hydrogen[cluster]:
            color_tech[cluster][subnode] = '#2e75b6'
        if subnode in cluster_subnodes_ng[cluster]:
            color_tech[cluster][subnode] = '#c55a11'
        if subnode in cluster_subnodes_co2[cluster]:
            color_tech[cluster][subnode] = '#79b932'

"""
#%% CAPACITY GRAPH
# Define dicts where all the capacity subnodes are assigned to their unit
                     
#subnodes_GWh = {"GWh":["BATTERIES energy", "NG_STORAGE energy", "PUMPED_HYDRO energy","H2_STORAGE energy"]}
subnodes_GWh = {"GWh":["BATTERIES energy", "PUMPED_HYDRO energy","H2_STORAGE energy"]}
subnodes_GW = {"GW":["BATTERIES power","METHANATION", "NG_STORAGE power", "H2_STORAGE power", "BIOMASS", "BIOMETHANE", "CCGT", "CHP", "ELECTROLYSIS_PLANTS","FUEL_CELLS","H2_STORAGE power", "NUCLEAR", "OCGT", "PUMPED_HYDRO power", "PV", "SMR", "WASTE", "WIND_ONSHORE","WIND_OFFSHORE"]}
subnodes_kt = {"kt":["CO2_STORAGE energy","H2O_STORAGE energy"]}
subnodes_kt_h = {"kt/h":["DAC","PCCC_BM","PCCC_CCGT","PCCC_CHP","PCCC_OCGT","PCCC_SMR","PCCC_WS","CO2_STORAGE power","H2O_STORAGE power"]}
"""
units_cluster_subnodes = dict()
cluster_subnodes_by_unit = dict()
for cluster in clusters:
    units_cluster_subnodes[cluster] = {'GWh':merge_lists(get_subnodes_energy_vector('unit_GWh',cluster,dictionary_3C),get_subnodes_energy_vector('unit_energy_GWh',cluster,dictionary_3C)),
                          'GW':merge_lists(get_subnodes_energy_vector('unit_GW',cluster,dictionary_3C),get_subnodes_energy_vector('unit_power_GW',cluster,dictionary_3C)),
                          'kt':get_subnodes_energy_vector('unit_energy_kt',cluster,dictionary_3C),
                          'kt/h':merge_lists(get_subnodes_energy_vector('unit_kt_h',cluster,dictionary_3C),get_subnodes_energy_vector('unit_power_kt_h',cluster,dictionary_3C))}
    #units_cluster_subnodes[cluster]['GW'] = merge_lists(get_subnodes_energy_vector('unit_GW',cluster,dictionary_3C),get_subnodes_energy_vector('unit_power_GW',cluster,dictionary_3C))
    #units_cluster_subnodes[cluster]['kt'] = get_subnodes_energy_vector('unit_energy_kt',cluster,dictionary_3C)
    #units_cluster_subnodes[cluster]['kt/h'] = merge_lists(get_subnodes_energy_vector('unit_kt_h',cluster,dictionary_3C),get_subnodes_energy_vector('unit_power_kt_h',cluster,dictionary_3C))
subnodes_GWh = {"GWh":merge_lists(get_subnodes_energy_vector('unit_GWh',dictionary_3C),get_subnodes_energy_vector('unit_energy_GWh',dictionary_3C))}
subnodes_GW = {"GW":merge_lists(get_subnodes_energy_vector('unit_GW',dictionary_3C),get_subnodes_energy_vector('unit_power_GW',dictionary_3C))}
subnodes_kt = {"kt":get_subnodes_energy_vector('unit_energy_kt',dictionary_3C)}
subnodes_kt_h = {"kt/h":merge_lists(get_subnodes_energy_vector('unit_kt_h',dictionary_3C), get_subnodes_energy_vector('unit_power_kt_h',dictionary_3C))}
"""
subnodes_by_unit = merge_dictionaries(subnodes_GWh,subnodes_GW,subnodes_kt,subnodes_kt_h)


# The below block of code transforms the data stored 
cluster_subnodes_cap_data = dict()
for cluster in clusters:
    #cluster_subnodes_tot_capacity[cluster] = []
    cluster_subnodes_cap_data[cluster] = dict()
    for key in subnodes_by_unit.keys():
        cluster_subnodes_cap_data[cluster][key] = dict()
        
        cluster_subnodes_cap_data[cluster][key]["subnode"] = [] #list(nodes for nodes in capa_data[cluster].keys() AND)
        cluster_subnodes_cap_data[cluster][key]["Preinstalled capacity"] = []
        cluster_subnodes_cap_data[cluster][key]["Added capacity"] = []
        cluster_subnodes_cap_data[cluster][key]["Max capacity"] = []
        cluster_subnodes_cap_data[cluster][key]["Total capacity"] = []
        for subnode in capa_data_sorted[cluster]:
            if subnode in subnodes_by_unit[key]:
                #cluster_subnodes_tot_capacity[cluster].append(capa_data[cluster][subnode]["Total capacity"])
                cluster_subnodes_cap_data[cluster][key]["subnode"].append(subnode)
                cluster_subnodes_cap_data[cluster][key]["Preinstalled capacity"].append(capa_data[cluster][subnode]["Preinstalled capacity"])
                cluster_subnodes_cap_data[cluster][key]["Added capacity"].append(capa_data[cluster][subnode]["Added capacity"])
                cluster_subnodes_cap_data[cluster][key]["Max capacity"].append(capa_data[cluster][subnode]["Max capacity"])
                cluster_subnodes_cap_data[cluster][key]["Total capacity"].append(capa_data[cluster][subnode]["Total capacity"])
        #cluster_subnodes_cap_data[cluster][subnode] = capa_data[cluster][subnode]["Total capacity"]

#cluster subnodes_cap_data_by_vector
# transform dataset to dataframe to be used in plots
s = dict()
for cluster in clusters:
    s[cluster] = dict()
    for key in cluster_subnodes_cap_data[cluster].keys():
        s[cluster][key] = pd.DataFrame.from_dict(cluster_subnodes_cap_data[cluster][key])
    """
    s[cluster] = pd.Series(cluster_subnodes_cap_data[cluster], name = "Total capacity")
    s[cluster].index.name = "Technology"
    s[cluster].reset_index()
    """
    
clust_capas = ["OFFSHORE","ZEEBRUGGE","INLAND"]

for clust_capa in clust_capas:
    
    # introduce plot object
    fig, ax = plt.subplots(2, 2)
    
    # Plot pre installed capacity for GWh capacities
    ax[0,0].barh(s[clust_capa]["GWh"]['subnode'],s[clust_capa]["GWh"]['Preinstalled capacity'], label = "Pre installed capacity")
    # Stack with added capacity 
    ax[0,0].barh(s[clust_capa]["GWh"]['subnode'],s[clust_capa]["GWh"]['Added capacity'], left=s[clust_capa]["GWh"]['Preinstalled capacity'], label="Added capacity")
    # Set the x-axis tick labels to subnodes 
    #ax[0,0].set_xticklabels(s[clust_capa]["GWh"]['subnode'], rotation=90, fontsize=8)
    #ax[0,0].set_xlim([0, 100])
    #- set y limits
    #ax[0,0].set_ylim([0, 80])
    #ax[0,0].set_ylabel("Total Capacity (GWh)", fontsize=15)
    ax[0,0].set_xlabel("Total Capacity (GWh)", fontsize=15)
    #tot_caps = cluster_subnodes_cap_data[clust_capa]["GWh"]["Total capacity"]
    #for index, value in enumerate(tot_caps):
     #   ax[0,0].text(value, index, round(value,1))
    ax[0,0].legend(prop={'size': 12})
    
    # Plot pre installed capacity for GW capacities
    ax[0,1].barh(s[clust_capa]["GW"]['subnode'],s[clust_capa]["GW"]['Preinstalled capacity'], label = "Pre installed capacity")
    # Stack with added capacity
    ax[0,1].barh(s[clust_capa]["GW"]['subnode'],s[clust_capa]["GW"]['Added capacity'], left=s[clust_capa]["GW"]['Preinstalled capacity'], label="Added capacity")
    # Set the x-axis tick labels to subnodes 
    #ax[0,1].set_xticklabels(s[clust_capa]["GW"]['subnode'], rotation=90, fontsize=8)
    #ax[0,1].set_xlim([0, 80])
    #- set y limits
    #ax[0,1].set_ylim([0, 80])
    #ax[0,1].set_ylabel("Total Capacity (GW)", fontsize=15)
    ax[0,1].set_xlabel("Total Capacity (GW)", fontsize=15)
    #tot_caps = cluster_subnodes_cap_data[clust_capa]["GW"]["Total capacity"]
    #for index, value in enumerate(tot_caps):
     #   ax[0,1].text(value, index, round(value,1))
    ax[0,1].legend(prop={'size': 12})
    
    
    # Plot pre installed capacity for kt capacities
    ax[1,0].barh(s[clust_capa]["kt"]['subnode'],s[clust_capa]["kt"]['Preinstalled capacity'], label = "Pre installed capacity")
    # Stack with added capacity
    ax[1,0].barh(s[clust_capa]["kt"]['subnode'],s[clust_capa]["kt"]['Added capacity'], left=s[clust_capa]["kt"]['Preinstalled capacity'], label="Added capacity")
    # Set the x-axis tick labels to subnodes 
    #ax[1,0].set_xticklabels(s[clust_capa]["kt"]['subnode'], rotation=90, fontsize=8)
    #ax[0,0].set_xlim([0, 80])
    #- set y limits
    #ax[1,0].set_ylim([0, 80])
    #ax[1,0].set_ylabel("Total Capacity (kt)", fontsize=15)
    ax[1,0].set_xlabel("Total Capacity (kt)", fontsize=15)
    #tot_caps = cluster_subnodes_cap_data[clust_capa]["kt"]["Total capacity"]
    #for index, value in enumerate(tot_caps):
     #   ax[1,0].text(value, index, round(value,1))
    #ax[1,0].legend(prop={'size': 12})
    
    
    ax[1,1].barh(s[clust_capa]["kt/h"]['subnode'],s[clust_capa]["kt/h"]['Preinstalled capacity'], label = "Pre installed capacity")
    
    ax[1,1].barh(s[clust_capa]["kt/h"]['subnode'],s[clust_capa]["kt/h"]['Added capacity'], left=s[clust_capa]["kt/h"]['Preinstalled capacity'], label="Added capacity")
    
    #ax[1,1].set_xticklabels(s[clust_capa]["kt/h"]['subnode'], rotation=90, fontsize=8)
    
    #ax[1,1].set_ylim([0, 80])
    ax[1,1].set_xlabel("Total Capacity (kt/h)", fontsize=15)
    ax[1,1].legend(prop={'size': 12})
    
    
    fig.suptitle(name_fig_capa + ' ' + clust_capa, y=0.99, fontsize=20)
    fig.set_size_inches(15,15)
    #fig.tight_layout(rect=(0, 0, 0, 0.95))
    if save_fig_capa == 1:
        fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        plt.savefig(title + '/' + name_fig_capa + ' ' + clust_capa + '.png',dpi=300)
    
    plt.show()



#%% costs for OFFSHORE + ZEEBRUGGE + INLAND + neighbouring countries electricity

cost_data_BE = cluster_subnodes_total_cost_BE


cost_data_sorted_BE = dict()

cost_data_sorted_BE = sorted(cost_data_BE.keys(), key = lambda x:(cost_data_BE[x]['total cost']), reverse=True)
    
# The below block of code transforms the data stored 

    
cluster_subnodes_cost_data_BE = dict()
cluster_subnodes_cost_data_BE["subnode"] = []
cluster_subnodes_cost_data_BE["CO2 captured tariff"] = []
cluster_subnodes_cost_data_BE["CO2 cost"] = []
cluster_subnodes_cost_data_BE["Variable cost"] = []
cluster_subnodes_cost_data_BE["existing fix cost"] = []
cluster_subnodes_cost_data_BE["export cost"] = []
cluster_subnodes_cost_data_BE["fuel cost"] = []
cluster_subnodes_cost_data_BE["import cost"] = []
cluster_subnodes_cost_data_BE["new fix cost"] = []
cluster_subnodes_cost_data_BE["new fix cost storage"] = []
cluster_subnodes_cost_data_BE["curtailment cost"] = []
cluster_subnodes_cost_data_BE["grid expansion cost"] = []
cluster_subnodes_cost_data_BE["total cost"] = []
cluster_subnodes_cost_data_BE["color"] = []
cluster_subnodes_cost_data_BE["vector"] = []
for subnode in cost_data_sorted_BE:
    if cost_data_BE[subnode]["total cost"] != 0:
        cluster_subnodes_cost_data_BE["subnode"].append(subnode)
        cluster_subnodes_cost_data_BE["CO2 captured tariff"].append(cost_data_BE[subnode]["CO2 capt cost"])
        cluster_subnodes_cost_data_BE["CO2 cost"].append(cost_data_BE[subnode]["CO2 cost"])
        cluster_subnodes_cost_data_BE["Variable cost"].append(cost_data_BE[subnode]["Variable cost"])
        cluster_subnodes_cost_data_BE["existing fix cost"].append(cost_data_BE[subnode]["existing fix cost"])
        cluster_subnodes_cost_data_BE["export cost"].append(cost_data_BE[subnode]["export cost"])
        cluster_subnodes_cost_data_BE["fuel cost"].append(cost_data_BE[subnode]["fuel cost"])
        cluster_subnodes_cost_data_BE["import cost"].append(cost_data_BE[subnode]["import cost"])
        cluster_subnodes_cost_data_BE["new fix cost"].append(cost_data_BE[subnode]["new fix cost"])
        cluster_subnodes_cost_data_BE["new fix cost storage"].append(cost_data_BE[subnode]["new fix cost storage"])
        cluster_subnodes_cost_data_BE["curtailment cost"].append(cost_data_BE[subnode]["curtailment cost"])
        cluster_subnodes_cost_data_BE["grid expansion cost"].append(cost_data_BE[subnode]["grid cost"])
        cluster_subnodes_cost_data_BE["total cost"].append(cost_data_BE[subnode]["total cost"])
        cluster_subnodes_cost_data_BE["color"].append(cost_data_BE[subnode]["color"])
        cluster_subnodes_cost_data_BE["vector"].append(cost_data_BE[subnode]["vector"])
#cluster subnodes_cap_data_by_vector
# transform dataset to dataframe to be used in plots
c = dict()
c = pd.DataFrame.from_dict(cluster_subnodes_cost_data_BE)

    

# introduce plot object
    

#c['export cost']
# DEFINE FIGURE AND PLOT OBJECTS
fig, ax = plt.subplots()

ax.barh(c['subnode'],c["CO2 captured tariff"], label = "CO2 captured tariff",color='#66CDAA',zorder=-1)
ax.barh(c['subnode'],c['export cost'], label = "export cost",color='#9ecae1',zorder=-1)
ax.barh(c['subnode'],c['existing fix cost'], label = "fixed cost existing capacity",color='#7f0000',zorder=-1)
ax.barh(c['subnode'],c['new fix cost'], left=c['existing fix cost'], label = "fixed cost new non storage capacity",color='#b30000',zorder=-1)
ax.barh(c['subnode'],c['new fix cost storage'], left=c['existing fix cost']+c['new fix cost'], label = "fixed cost new storage capacity",color='#d7301f',zorder=-1)
ax.barh(c['subnode'],c['Variable cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage'], label = "variable cost",color='#ef6548',zorder=-1)
ax.barh(c['subnode'],c['fuel cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost'], label = "fuel cost",color='#fc8d59',zorder=-1)
ax.barh(c['subnode'],c['import cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost'], label = "import cost",color='#fdbb84',zorder=-1)
ax.barh(c['subnode'],c['CO2 cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost']+c['import cost'], label = "CO2 cost",color='#fdd49e',zorder=-1)
ax.barh(c['subnode'],c['curtailment cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost']+c['import cost']+c['CO2 cost'], label = "curtailment cost",color='#fee8c8',zorder=-1)
ax.barh(c['subnode'],c['grid expansion cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost']+c['import cost']+c['CO2 cost']+c['curtailment cost'], label = "grid expansion cost",color='#fff7ec',zorder=-1)
ax.scatter(c["total cost"],c['subnode'], label="Total cost", color='black', zorder=1)
#ax.set_xticklabels(c['subnode'], rotation=90, fontsize=12)
#- set y limits
#ax[0,0].set_ylim([0, 80])
ax.set_xlabel("Million Euros/an", fontsize=28)
ax.legend(prop={'size': 15})
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
fig.suptitle(name_fig_BE_costs + ' ' , y=0.99, fontsize=32)
if logscale == 1:
    ax.set_xscale('log')

fig.set_size_inches(15,15)
if save_fig_BE_costs == 1:
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
    #plt.tight_layout()
    plt.savefig(title + '/' + name_fig_BE_costs + ' ' + '.png',dpi=600)

plt.show()

c.to_excel(title + '/' + name_fig_BE_costs+ ' '+ title + '.xlsx')#,startcol=-1)

#%% Total costs grouped by energy vector
logscale = logscale
fig, ax = plt.subplots()

for x,y,z,lb in zip(c['subnode'],c["total cost"],c['color'],c['vector']):
    ax.barh(x, y, color=z, label=lb)
    
# if i == 0 else ""
#ax.barh(c['subnode'],c["total cost"], label="Total cost", color=c['color'], zorder=1)
#ax.set_xticklabels(c['subnode'], rotation=90, fontsize=12)
#- set y limits
#ax[0,0].set_ylim([0, 80])
ax.set_xlabel("Million Euros/an", fontsize=28)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),prop={'size': 15})
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#ax.legend(prop={'size': 15})

fig.suptitle(name_fig_BE_total_costs + ' ' , y=0.99, fontsize=32)
if logscale == 1:
    ax.set_xscale('log')

fig.set_size_inches(15,15)
if save_fig_BE_total_costs == 1:
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
    #plt.tight_layout()
    plt.savefig(title + '/' + name_fig_BE_total_costs + ' ' + '.png',dpi=600)

plt.show()


#%% Capacities per node per type of capacity (preinstalled, new, total, max)
units = ['GW','GWh','kt_h','kt']
xlabels = {'GW':'GW','GWh':'GWh','kt_h':'kt/h','kt':'kt'}
caps_data_BE = cluster_subnodes_caps_BE

cluster_subnodes_caps_data_BE = dict()
cap = dict()
caps_data_sorted_BE = dict()
for unit in units:
    caps_data_sorted_BE[unit] = sorted(caps_data_BE[unit].keys(), key = lambda x:(caps_data_BE[unit][x]['total capacity']), reverse=True)
    cluster_subnodes_caps_data_BE[unit] = dict()

# The below block of code transforms the data stored 



    cluster_subnodes_caps_data_BE[unit]["subnode"] = []
    cluster_subnodes_caps_data_BE[unit]["preinstalled capacity"] = []
    cluster_subnodes_caps_data_BE[unit]["added capacity"] = []
    cluster_subnodes_caps_data_BE[unit]["total capacity"] = []
    cluster_subnodes_caps_data_BE[unit]["maximum capacity"] = []
    cluster_subnodes_caps_data_BE[unit]["color"] = []
    cluster_subnodes_caps_data_BE[unit]["vector"] = []
    for subnode in caps_data_sorted_BE[unit]:
        if caps_data_BE[unit][subnode]["total capacity"] != 0:
            cluster_subnodes_caps_data_BE[unit]["subnode"].append(subnode)
            cluster_subnodes_caps_data_BE[unit]["preinstalled capacity"].append(caps_data_BE[unit][subnode]["preinstalled capacity"])
            cluster_subnodes_caps_data_BE[unit]["added capacity"].append(caps_data_BE[unit][subnode]["added capacity"])
            cluster_subnodes_caps_data_BE[unit]["total capacity"].append(caps_data_BE[unit][subnode]["total capacity"])
            cluster_subnodes_caps_data_BE[unit]["maximum capacity"].append(caps_data_BE[unit][subnode]["maximum capacity"])
            cluster_subnodes_caps_data_BE[unit]["color"].append(caps_data_BE[unit][subnode]["color"])
            cluster_subnodes_caps_data_BE[unit]["vector"].append(caps_data_BE[unit][subnode]["vector"])
#cluster subnodes_cap_data_by_vector
# transform dataset to dataframe to be used in plots
    cap[unit] = dict()

    cap[unit] = pd.DataFrame.from_dict(cluster_subnodes_caps_data_BE[unit])

    

# introduce plot object
    

#c['export cost']
# DEFINE FIGURE AND PLOT OBJECTS
    # if not len(cap[unit]) == 0:    
    #     fig, ax = plt.subplots()
        
    
    #     ax.barh(cap[unit]['subnode'],cap[unit]["preinstalled capacity"], label = "preinstalled capacity",color='#7f0000',zorder=-1)
    #     ax.barh(cap[unit]['subnode'],cap[unit]['added capacity'], left=cap[unit]['preinstalled capacity'], label = "added capacity",color='#b30000',zorder=-1)
    #     ax.scatter(cap[unit]["maximum capacity"],cap[unit]['subnode'], label="maximum capacity", color='black', zorder=1)
    #     #ax.set_xticklabels(c['subnode'], rotation=90, fontsize=12)
    #     #- set y limits
    #     #ax[0,0].set_ylim([0, 80])
    #     ax.set_xlabel(xlabels[unit], fontsize=20)
    #     ax.legend(prop={'size': 15})
        
    #     fig.suptitle(name_fig_capa_alt, y=0.99, fontsize=20)
    #     if logscale == 1:
    #         ax.set_xscale('log')
        
    #     fig.set_size_inches(15,15)
    #     if save_fig_capa == 1:
    #         fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
    #         #plt.tight_layout()
    #         plt.savefig(title + '/' + name_fig_capa_alt + ' by cap category '  + unit + '.png',dpi=300)
        
    #     plt.show()
    


#%% Total capacity grouped by energy vector
for unit in units:
    if unit == "GWh":
        logscale = 1
    else:
        logscale = 0
    if not len(cap[unit]) == 0:      

        fig, ax = plt.subplots()
        
        for x,y,z,lb in zip(cap[unit]['subnode'],cap[unit]["total capacity"],cap[unit]['color'],cap[unit]['vector']):
            ax.barh(x, y, color=z, label=lb)
    
# if i == 0 else ""
#ax.barh(c['subnode'],c["total cost"], label="Total cost", color=c['color'], zorder=1)
#ax.set_xticklabels(c['subnode'], rotation=90, fontsize=12)
#- set y limits
#ax[0,0].set_ylim([0, 80])
        ax.set_xlabel(xlabels[unit], fontsize=28)
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        
        ax.legend(by_label.values(), by_label.keys(),prop={'size': 20})
        
        #ax.legend(prop={'size': 15})
        
        fig.suptitle(name_fig_capa_alt, y=0.99, fontsize=32)
        if logscale == 1:
            ax.set_xscale('log')
        
        fig.set_size_inches(15,15)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        if save_fig_capa == 1:
            fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
            #plt.tight_layout()
            plt.savefig(title + '/' + name_fig_capa_alt + ' by energy vector '  + unit + '.png',dpi=300)
        
        plt.show()



#%%
# costs per cluster separately

# NEEDS UPDATE IF TO BE USED
"""
cost_data = cluster_subnodes_total_cost


cost_data_sorted = dict()
for cluster in clusters:
    cost_data_sorted[cluster] = sorted(cost_data[cluster].keys(), key = lambda x:(cost_data[cluster][x]['total cost']), reverse=True)
    
# The below block of code transforms the data stored 
cluster_subnodes_cost_data = dict()
for cluster in clusters:
    #cluster_subnodes_tot_capacity[cluster] = []
    
    cluster_subnodes_cost_data[cluster] = dict()
    cluster_subnodes_cost_data[cluster]["subnode"] = []
    cluster_subnodes_cost_data[cluster]["CO2 cost"] = []
    cluster_subnodes_cost_data[cluster]["Variable cost"] = []
    cluster_subnodes_cost_data[cluster]["existing fix cost"] = []
    cluster_subnodes_cost_data[cluster]["export cost"] = []
    cluster_subnodes_cost_data[cluster]["fuel cost"] = []
    cluster_subnodes_cost_data[cluster]["import cost"] = []
    cluster_subnodes_cost_data[cluster]["new fix cost"] = []
    cluster_subnodes_cost_data[cluster]["new fix cost storage"] = []
    cluster_subnodes_cost_data[cluster]["total cost"] = []
    for subnode in cost_data_sorted[cluster]:
        cluster_subnodes_cost_data[cluster]["subnode"].append(subnode)
        cluster_subnodes_cost_data[cluster]["CO2 cost"].append(cost_data[cluster][subnode]["CO2 cost"])
        cluster_subnodes_cost_data[cluster]["Variable cost"].append(cost_data[cluster][subnode]["Variable cost"])
        cluster_subnodes_cost_data[cluster]["existing fix cost"].append(cost_data[cluster][subnode]["existing fix cost"])
        cluster_subnodes_cost_data[cluster]["export cost"].append(cost_data[cluster][subnode]["export cost"])
        cluster_subnodes_cost_data[cluster]["fuel cost"].append(cost_data[cluster][subnode]["fuel cost"])
        cluster_subnodes_cost_data[cluster]["import cost"].append(cost_data[cluster][subnode]["import cost"])
        cluster_subnodes_cost_data[cluster]["new fix cost"].append(cost_data[cluster][subnode]["new fix cost"])
        cluster_subnodes_cost_data[cluster]["new fix cost storage"].append(cost_data[cluster][subnode]["new fix cost storage"])
        cluster_subnodes_cost_data[cluster]["total cost"].append(cost_data[cluster][subnode]["total cost"])
        
        
#cluster subnodes_cap_data_by_vector
# transform dataset to dataframe to be used in plots
c = dict()
for cluster in clusters:
    c[cluster] = pd.DataFrame.from_dict(cluster_subnodes_cost_data[cluster])
    

# introduce plot object
    


# DEFINE FIGURE AND PLOT OBJECTS
fig, ax = plt.subplots()

ax.barh(c[clust]['subnode'],c[clust]['export cost'], label = "export cost")
ax.barh(c[clust]['subnode'],c[clust]['existing fix cost'], left=c[clust]['export cost'], label = "existing fix")
ax.barh(c[clust]['subnode'],c[clust]['new fix cost'], left=c[clust]['export cost']+c[clust]['existing fix cost'], label = "new fix")
ax.barh(c[clust]['subnode'],c[clust]['new fix cost storage'], left=c[clust]['export cost']+c[clust]['existing fix cost']+c[clust]['new fix cost'], label = "new fix sto")
ax.barh(c[clust]['subnode'],c[clust]['Variable cost'], left=c[clust]['export cost']+c[clust]['existing fix cost']+c[clust]['new fix cost']+c[clust]['new fix cost storage'], label = "var")
ax.barh(c[clust]['subnode'],c[clust]['fuel cost'], left=c[clust]['export cost']+c[clust]['existing fix cost']+c[clust]['new fix cost']+c[clust]['new fix cost storage']+c[clust]['Variable cost'], label = "fuel cost")
ax.barh(c[clust]['subnode'],c[clust]['import cost'], left=c[clust]['export cost']+c[clust]['existing fix cost']+c[clust]['new fix cost']+c[clust]['new fix cost storage']+c[clust]['Variable cost']+c[clust]['fuel cost'], label = "import")
ax.barh(c[clust]['subnode'],c[clust]['CO2 cost'], left=c[clust]['export cost']+c[clust]['existing fix cost']+c[clust]['new fix cost']+c[clust]['new fix cost storage']+c[clust]['Variable cost']+c[clust]['fuel cost']+c[clust]['import cost'], label = "CO2")

ax.set_xticklabels(c[clust]['subnode'], rotation=90, fontsize=12)
#- set y limits
#ax[0,0].set_ylim([0, 80])
ax.set_ylabel("Million €", fontsize=20)
ax.legend(prop={'size': 15})

fig.suptitle(name_fig_costs + ' ' + clust, y=1.01, fontsize=20)

fig.set_size_inches(15,15)
if save_fig_costs == 1:
    plt.tight_layout()
    plt.savefig(name_fig_costs + ' ' + clust + '.png',dpi=600)

plt.show()
"""
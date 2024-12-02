# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:27:23 2023

@author: Jocelyn
"""

import seaborn as sns
import numpy as np

""" Graphique des capacités des technologies de production """


technologies = ['PV','WIND_ONSHORE','WIND_OFFSHORE','CCGT','OCGT','FUEL_CELLS','ELECTROLYSIS_PLANTS','SMR','BIOMETHANE','METHANATION','DAC','PCCC_CCGT','PCCC_OCGT','DESALINATION']
techno_conv = dict()
zoom = 'Hour'
for technology in technologies:
    for cluster in clusters_belgium:
        if technology in capa_data[cluster]:
            techno_conv[cluster + ' ' + technology] = dict()
            if technology in ['PV','WIND_ONSHORE','WIND_OFFSHORE','CCGT','OCGT','FUEL_CELLS']:
                variable = 'e_produced'
                techno_conv[cluster + ' ' + technology] = capacity_factors_production[cluster][technology + ' ' + variable].copy()
                if techno_conv[cluster + ' ' + technology]['Capacity'] > 0: 
                    techno_conv[cluster + ' ' + technology]['Capacity Factor'] = techno_conv[cluster + ' ' + technology]['Capacity factor'] * techno_conv[cluster + ' ' + technology]['Capacity']
                else : 
                    techno_conv[cluster + ' ' + technology]['Capacity Factor'] = 0
                techno_conv[cluster + ' ' + technology]['Total production'] = capacity_factors_production[cluster][technology + ' ' + variable]['Total production']/1000
                techno_conv[cluster + ' ' + technology]['Max production'] =  max(zoom_on_variable_in_cluster_subnode(cluster,variable,technology,zoom,dictionary_3C))
                techno_conv[cluster + ' ' + technology]['Type'] =  'Elec'
            elif technology in ['ELECTROLYSIS_PLANTS','SMR']:
                 variable = 'h2_produced'
                 techno_conv[cluster + ' ' + technology] = capacity_factors_production[cluster][technology + ' ' + variable].copy()
                 if techno_conv[cluster + ' ' + technology]['Capacity'] > 0: 
                     techno_conv[cluster + ' ' + technology]['Capacity Factor'] = techno_conv[cluster + ' ' + technology]['Capacity factor'] * techno_conv[cluster + ' ' + technology]['Capacity']
                 else : 
                     techno_conv[cluster + ' ' + technology]['Capacity Factor'] = 0
                 techno_conv[cluster + ' ' + technology]['Total production'] = capacity_factors_production[cluster][technology + ' ' + variable]['Total production']/1000 
                 techno_conv[cluster + ' ' + technology]['Max production'] =  max(zoom_on_variable_in_cluster_subnode(cluster,variable,technology,zoom,dictionary_3C))
                 techno_conv[cluster + ' ' + technology]['Type'] =  'H2'
            elif technology in ['BIOMETHANE','METHANATION']:
                 variable = 'ng_produced'
                 techno_conv[cluster + ' ' + technology] = capacity_factors_production[cluster][technology + ' ' + variable].copy()
                 if techno_conv[cluster + ' ' + technology]['Capacity'] > 0: 
                     techno_conv[cluster + ' ' + technology]['Capacity Factor'] = techno_conv[cluster + ' ' + technology]['Capacity factor'] * techno_conv[cluster + ' ' + technology]['Capacity']
                 else : 
                     techno_conv[cluster + ' ' + technology]['Capacity Factor'] = 0
                 techno_conv[cluster + ' ' + technology]['Total production'] = capacity_factors_production[cluster][technology + ' ' + variable]['Total production']/1000 
                 techno_conv[cluster + ' ' + technology]['Max production'] =  max(zoom_on_variable_in_cluster_subnode(cluster,variable,technology,zoom,dictionary_3C))
                 techno_conv[cluster + ' ' + technology]['Type'] =  'CH4'
            elif technology in ['DAC','PCCC_CCGT','PCCC_OCGT']:
                 variable = 'co2_captured'
                 techno_conv[cluster + ' ' + technology] = capacity_factors_production[cluster][technology + ' ' + variable].copy()
                 if techno_conv[cluster + ' ' + technology]['Capacity'] > 0: 
                     techno_conv[cluster + ' ' + technology]['Capacity Factor'] = techno_conv[cluster + ' ' + technology]['Capacity factor'] * techno_conv[cluster + ' ' + technology]['Capacity']
                 else : 
                     techno_conv[cluster + ' ' + technology]['Capacity Factor'] = 0
                 techno_conv[cluster + ' ' + technology]['Total production'] = capacity_factors_production[cluster][technology + ' ' + variable]['Total production']/1000
                 techno_conv[cluster + ' ' + technology]['Max production'] =  max(zoom_on_variable_in_cluster_subnode(cluster,variable,technology,zoom,dictionary_3C))
                 techno_conv[cluster + ' ' + technology]['Type'] =  'CO2'
            elif technology in ['DESALINATION']:
                variable = 'h2o_produced'
                techno_conv[cluster + ' ' + technology]['Capacity'] = cluster_subnodes_capacities_tot['OFFSHORE']['DESALINATION']['Total capacity']
                techno_conv[cluster + ' ' + technology]['Total production'] = sum(zoom_on_variable_in_cluster_subnode(cluster,variable,technology,zoom,dictionary_3C))/1000
                if techno_conv[cluster + ' ' + technology]['Capacity'] > 0:
                    techno_conv[cluster + ' ' + technology]['Capacity factor'] = techno_conv[cluster + ' ' + technology]['Total production']*1000/(8760 * techno_conv[cluster + ' ' + technology]['Capacity'])
                else:
                    techno_conv[cluster + ' ' + technology]['Capacity factor'] = 0
                techno_conv[cluster + ' ' + technology]['Capacity Factor'] = techno_conv[cluster + ' ' + technology]['Capacity factor'] * techno_conv[cluster + ' ' + technology]['Capacity']
                techno_conv[cluster + ' ' + technology]['Max production'] = max(zoom_on_variable_in_cluster_subnode(cluster,variable,technology,zoom,dictionary_3C))
                techno_conv[cluster + ' ' + technology]['Type'] =  'H2O'

# Define the keys you want to include in the graph (categories and data points)
technos = [i for i in techno_conv]
data_points_to_include = ['Capacity','Max production', 'Capacity Factor']

# Filter the data based on the keys
filtered_data = {
    techno: {data_point: techno_conv[techno][data_point] for data_point in data_points_to_include}
    for techno in technos
}

# Convert the filtered data to a DataFrame and transpose it
df = pd.DataFrame(filtered_data).T

# Create the horizontal stacked bar graph
ax = df.plot.barh(stacked=False, figsize=(6, 6))

ax.invert_yaxis()

# Set the title and axis labels
#plt.title('Horizontal Stacked Graph for Certain Keys')
plt.xlabel('Capacity in GW or kt/h', fontsize = 16)
plt.ylabel('Conversion nodes', fontsize = 16)

# Add the legend to the plot
ax.legend(loc='center right')

# Show the plot
plt.show()

data_points_to_include = ['Total production']

# Filter the data based on the keys
filtered_data = {
    techno: {data_point: techno_conv[techno][data_point] for data_point in data_points_to_include}
    for techno in technos
}

# Convert the filtered data to a DataFrame and transpose it
df = pd.DataFrame(filtered_data).T

# Create the horizontal stacked bar graph
ax = df.plot.barh(stacked=False, figsize=(6, 6))

ax.invert_yaxis()

# Set the title and axis labels
#plt.title('Horizontal Stacked Graph for Certain Keys')
plt.xlabel('Production in TWh or Mt', fontsize = 16)
plt.ylabel('Conversion nodes', fontsize = 16)

# Add the legend to the plot
ax.legend(loc='center right')

# Show the plot
plt.show()

table_techno = transform_into_table(techno_conv)
save_table_into_csv(table_techno,title + "/Conversion_nodes")


data = pd.read_csv(title + "/Conversion_nodes.csv")
data = data[data["Capacity"] > 0]

data.rename(columns = {'Unnamed: 0':'Name'}, inplace = True)
data.rename(columns = {'Capacity Factor':'Average Power'}, inplace = True)

#put H2O in T
data.loc[data.Name == "OFFSHORE DESALINATION", "Capacity"] *= 1000
data.loc[data.Name == "OFFSHORE DESALINATION", "Total production"] *= 1000
data.loc[data.Name == "OFFSHORE DESALINATION", "Average Power"] *= 1000
data.loc[data.Name == "OFFSHORE DESALINATION", "Max production"] *= 1000

# better names
names = {
    "INLAND PV": "PV Panels (Inland)",
    "INLAND WIND_ONSHORE": "Wind Turbines (Onshore)",
    "OFFSHORE WIND_OFFSHORE": "Wind Turbines (Offshore)",
    "INLAND CCGT": "CCGT (Inland)",
    "OFFSHORE ELECTROLYSIS_PLANTS": "Electrolysis (Offshore)",
    "ZEEBRUGGE ELECTROLYSIS_PLANTS": "Electrolysis (Zeebrugge)",
    "INLAND ELECTROLYSIS_PLANTS": "Electrolysis (Inland)",
    "INLAND BIOMETHANE": "Biomethanation (Inland)",
    "INLAND DAC": "Direct Air Capture (Inland)",
    "INLAND PCCC_CCGT": "Post-Combustion Capture (Inland)",
    "OFFSHORE DESALINATION": "Desalination (Offshore)"
}

data["Name"] = data["Name"].map(names)

sns.set_theme(style="ticks")
categories = ["Elec", "CH4", "H2", "CO2", "H2O"]
names = ["Electricity", "Gas", "Hydrogen", "$CO_2$", "Water"]
units_power = ["GW_e", "GW_{CH_4}", "GW_{H_2}", "kT_{CO_2}/h", "T_{H_2O}/h"]
units_quantity = ["TWh_e", "TWh_{CH_4}", "TWh_{H_2}", "MT_{CO_2}", "kT_{H_2O}"]

n_type = []
for types in categories:
    data_type = data[data["Type"] == types]
    n_type.append(len(data_type))

categories_kept = list()
for i in range(0,len(n_type)):
    if n_type[i] > 0:
        categories_kept.append(categories[i])
        
names_kept = list()
for i in range(0,len(n_type)):
    if n_type[i] > 0:
        names_kept.append(names[i])
        
units_power_kept = list()
for i in range(0,len(n_type)):
    if n_type[i] > 0:
        units_power_kept.append(units_power[i])
        
units_quantity_kept = list()
for i in range(0,len(n_type)):
    if n_type[i] > 0:
        units_quantity_kept.append(units_quantity[i])

n_type = [x for x in n_type if x != 0]
n_rows = len(n_type)

fig, axs = plt.subplots(nrows=n_rows,ncols=2,figsize=(10, 5),height_ratios=n_type,width_ratios=[3,2])
palette = sns.color_palette("YlGnBu", n_colors=5)[1:]

for types, name, unit_power, unit_quantity, ax in zip(categories_kept, names_kept, units_power_kept, units_quantity_kept, axs):
    filter_data = data[data["Type"] == types]
    if filter_data.empty:
        print("No data available for the selected type:", types)
    else:
        sns.barplot(x="Capacity", y="Name", data=data[data["Type"] == types],
                    label="Installed Power", color=palette[0], ax=ax[0], width=1)
        for i in ax[0].containers:
            ax[0].bar_label(i,fmt=f"$%.2f\ {unit_power}$", label_type="edge", padding=2, fontsize=9)
        sns.barplot(x="Max production", y="Name", data=data[data["Type"] == types],
                    label="Peak power", color=palette[1], ax=ax[0], width=1)
        sns.barplot(x="Average Power", y="Name", data=data[data["Type"] == types],
                    label="Average Power", color=palette[2], ax=ax[0], width=1)
        #ax[0].set(xlabel=None, ylabel=f"{name}\n$({unit_power})$")
        ax[0].set(xlabel=None, ylabel=f"{name}")
        ax[0].yaxis.label.set_size(12)
    
        sns.barplot(x="Total production", y="Name", data=data[data["Type"] == types],
                    label="Total production", color=palette[3], ax=ax[1], width=1)
        for i in ax[1].containers:
            ax[1].bar_label(i,fmt=f"$%.2f\ {unit_quantity}$", label_type="edge", padding=2, fontsize=9)
        #ax[1].set(xlabel=None, ylabel=f"$({unit_quantity})$")
        ax[1].set(xlabel=None, ylabel=None)
        ax[1].yaxis.label.set_size(10)
        ax[1].yaxis.set_tick_params(labelleft=False)
    
        ax[0].grid(False)
        ax[1].grid(False)
        ax[0].tick_params(left=False)
        ax[1].tick_params(left=False)

axs[0][0].set_title("Power")
axs[0][1].set_title("Energy or Quantity")

#axs[-1][0].legend(bbox_to_anchor=(-0.7, -3.0, 2, 0.1), loc='lower left',
#                      ncols=3, mode="expand", borderaxespad=0.)
axs[-1][0].legend(bbox_to_anchor=(-0.7, -3.0, 2, 0.1), loc='lower center',
                      ncols=3, borderaxespad=0.,reverse=True)
axs[-1][1].legend(bbox_to_anchor=(0, -3.0, 1.3, 0.1), loc='lower center',
                      ncols=1, borderaxespad=0.,reverse=True)
#axs[-1][0].legend()
sns.despine(left=True, bottom=True)
#plt.subplots_adjust(wspace=0.6, hspace=1)
plt.subplots_adjust(wspace=0.5, hspace=1)
fig.align_ylabels()
plt.tight_layout()
#plt.savefig('C:\\Users\\jocel\\OneDrive\\Doctorat\\My papers\\Impact of wind offshore on the Belgium energy system\\Article\\Images\\Cap_prod_conv_nodes.pdf')
plt.savefig(title + '/' + 'Cap_prod_conv_nodes.pdf',dpi=600)


#%% 

""" Cost of all nodes """

cost_data_BE = cluster_subnodes_total_cost_BE


cost_data_sorted_BE = dict()

cost_data_sorted_BE = sorted(cost_data_BE.keys(), key = lambda x:(cost_data_BE[x]['total cost']), reverse=False)
    
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
# fig, ax = plt.subplots()

# ax.barh(c['subnode'],c["CO2 captured tariff"], label = "CO2 captured tariff",color='#66CDAA',zorder=-1)
# ax.barh(c['subnode'],c['export cost'], label = "export cost",color='#9ecae1',zorder=-1)
# ax.barh(c['subnode'],c['existing fix cost'], label = "fixed cost existing capacity",color='#7f0000',zorder=-1)
# ax.barh(c['subnode'],c['new fix cost'], left=c['existing fix cost'], label = "fixed cost new non storage capacity",color='#b30000',zorder=-1)
# ax.barh(c['subnode'],c['new fix cost storage'], left=c['existing fix cost']+c['new fix cost'], label = "fixed cost new storage capacity",color='#d7301f',zorder=-1)
# ax.barh(c['subnode'],c['Variable cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage'], label = "variable cost",color='#ef6548',zorder=-1)
# ax.barh(c['subnode'],c['fuel cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost'], label = "fuel cost",color='#fc8d59',zorder=-1)
# ax.barh(c['subnode'],c['import cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost'], label = "import cost",color='#fdbb84',zorder=-1)
# ax.barh(c['subnode'],c['CO2 cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost']+c['import cost'], label = "CO2 cost",color='#fdd49e',zorder=-1)
# ax.barh(c['subnode'],c['curtailment cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost']+c['import cost']+c['CO2 cost'], label = "curtailment cost",color='#fee8c8',zorder=-1)
# ax.barh(c['subnode'],c['grid expansion cost'], left=c['existing fix cost']+c['new fix cost']+c['new fix cost storage']+c['Variable cost']+c['fuel cost']+c['import cost']+c['CO2 cost']+c['curtailment cost'], label = "grid expansion cost",color='#fff7ec',zorder=-1)
# ax.scatter(c["total cost"],c['subnode'], label="Total cost", color='black', zorder=1)
# #ax.set_xticklabels(c['subnode'], rotation=90, fontsize=12)
# #- set y limits
# #ax[0,0].set_ylim([0, 80])
# ax.set_xlabel("Million Euros/an", fontsize=28)
# ax.legend(prop={'size': 15})
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# fig.suptitle(name_fig_BE_costs + ' ' , y=0.99, fontsize=32)
# if logscale == 1:
#     ax.set_xscale('log')

# fig.set_size_inches(15,15)
# if save_fig_BE_costs == 1:
#     fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
#     #plt.tight_layout()
#     plt.savefig(title + '/' + name_fig_BE_costs + ' ' + '.png',dpi=600)

# plt.show()

# c.to_excel(title + '/' + name_fig_BE_costs+ ' '+ title + '.xlsx')#,startcol=-1)

#% Total costs grouped by energy vector
logscale = logscale
fig, ax = plt.subplots()

for x,y,z,lb in zip(c['subnode'],c["total cost"],c['color'],c['vector']):
    ax.barh(x, y, color=z, label=lb)
    
# if i == 0 else ""
#ax.barh(c['subnode'],c["total cost"], label="Total cost", color=c['color'], zorder=1)
#ax.set_xticklabels(c['subnode'], rotation=90, fontsize=12)
#- set y limits
#ax[0,0].set_ylim([0, 80])
ax.set_xlabel("Million Euros/year", fontsize=28)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),prop={'size': 15})
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#ax.legend(prop={'size': 15})

#fig.suptitle(name_fig_BE_total_costs + ' ' , y=0.99, fontsize=32)
if logscale == 1:
    ax.set_xscale('log')

fig.set_size_inches(15,15)
fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
#plt.tight_layout()
#plt.savefig('C:\\Users\\jocel\\OneDrive\\Doctorat\\My papers\\Impact of wind offshore on the Belgium energy system\\Article\\Images\\' + name_fig_BE_total_costs + ' ' + '.pdf',dpi=600)
plt.savefig(title + '/' + name_fig_BE_total_costs + ' ' + '.pdf',dpi=600)
plt.show()


#%%
""" Electricity balance of the Coastal cluster  """

zoom = 'Hour'
elec_ch_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','charged','BATTERIES','Hour',dictionary_3C)
elec_disch_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','discharged','BATTERIES','Hour',dictionary_3C)
elec_soc_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','state_of_charge','BATTERIES','Hour',dictionary_3C)
elec_imp_dk = zoom_on_variable_in_cluster('DENMARK','imported','Hour',dictionary_3C)
elec_imp_uk = zoom_on_variable_in_cluster('UNITED_KINGDOM','imported','Hour',dictionary_3C)

max_imp_dk = max(elec_imp_dk)
max_imp_uk = max(elec_imp_uk)

h2_ep_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','e_consumed','ELECTROLYSIS_PLANTS','Hour',dictionary_3C)
cap_ep_zb = cluster_subnodes_capacities_tot['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['Total capacity']

elec_off_zb = zoom_on_variable_in_cluster('HV_OFF_ZB','e_forward_out','Hour',dictionary_3C)
elec_inl_zb = zoom_on_variable_in_cluster('HV_ZB_INL','e_reverse_out','Hour',dictionary_3C)

elec_zb_inl = [-x for x in zoom_on_variable_in_cluster('HV_ZB_INL','e_forward_in','Hour',dictionary_3C)]
elec_zb_off = [-x for x in zoom_on_variable_in_cluster('HV_OFF_ZB','e_reverse_in','Hour',dictionary_3C)]
pipe_zb_inl = [-x for x in zoom_on_variable_in_cluster('PIPE_H2_ZB_INL','e_consumed','Hour',dictionary_3C)]

ng_imp_nv = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_NV',zoom,dictionary_3C)
ng_imp_uk = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_UK',zoom,dictionary_3C)
ng_imp_fr = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_FR',zoom,dictionary_3C)

max_ng_imp_nv = max(ng_imp_nv)
max_ng_imp_uk = max(ng_imp_uk)
max_ng_imp_fr = max(ng_imp_fr)

""" Summer """

start = 4728 
end = start + 48 + 1

x_ticks = [x for x in range(0,end - start,24)]
fig, ax1 = plt.subplots()

#ax1.plot(elec_imp_dk[start:end],label = 'DK',color = 'y')
#ax1.plot(elec_imp_uk[start:end], label = 'UK', color = 'b')
ax1.plot(elec_off_zb[start:end],label = 'Offshore production',color = 'r')
ax1.plot(elec_inl_zb[start:end], label = 'Inland production', color = 'g')
battery= [elec_disch_zb[x] - elec_ch_zb[x] for x in range(0,len(elec_inl_zb))]
ax1.plot(battery[start:end], label = 'Electrical batteries', color = 'black')
ax1.plot(battery[start:end], label = 'Electrical batteries', color = 'black')
ax1.plot(battery[start:end], label = 'Electrical batteries', color = 'black')

ax1.plot([-x for x in h2_ep_zb[start:end]],label = 'Electrolysers consumption')
ax1.plot(elec_zb_inl[start:end], label = 'Inland consumption', color = 'purple')
ax1.plot(elec_zb_off[start:end], label = 'to offshore', color = 'gray')
ax1.plot(pipe_zb_inl[start:end], label = 'Pipe consumption',color = 'blue')
ax1.legend(loc = 'upper right', prop = {'size' : 7})
#ax1.legend(loc='center left', bbox_to_anchor=(1, 0.0),prop={'size': 8})
#max_y2 = max(max(h2_ep_zb[start:end]),max(elec_ch_zb[start:end]),max(elec_disch_zb[start:end]))
#ax1.set_ylim(-max_y2, max_y2)
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(['Day 1', 'Day 2', 'Day 3'])
ax1.set_ylabel('Electricity [TWh]')
#ax1.set_xlabel('Day')

#plt.savefig('C:\\Users\\jocel\\OneDrive\\Doctorat\\My papers\\Impact of wind offshore on the Belgium energy system\\Article\\Images\\elec_summer_coa.pdf')
plt.savefig(title + '/elec_summer_coa.pdf',dpi=600)
plt.show()
# plt.plot(elec_soc_zb[start:end],label = 'SOC zb')
# plt.show()

summer_elec = dict()
summer_elec['Offshore production'] = elec_off_zb[start:end]
summer_elec['Inland production'] = elec_inl_zb[start:end]
summer_elec['Electrical batteries'] = battery[start:end]

summer_elec['Electrolysers consumption'] = [-x for x in h2_ep_zb[start:end]]
summer_elec['Inland consumption'] = elec_zb_inl[start:end]
summer_elec['Offshore consumption'] = elec_zb_off[start:end]
summer_elec['Pipe consumption'] = pipe_zb_inl[start:end]

table_summer_elec = pd.DataFrame(summer_elec)
table_summer_elec.to_excel(title +'/summer_elec.xlsx')


# # Données pour les barres
# x_ticks = np.arange(len(elec_off_zb[start:end]))  # Position des barres sur l'axe des x
# fig, ax1 = plt.subplots()

# # Création des graphiques à barres superposées

# elec_imp_dk = np.array(elec_imp_dk[start:end])
# elec_imp_uk = np.array(elec_imp_uk[start:end])
# elec_off_zb = np.array(elec_off_zb[start:end])
# elec_inl_zb = np.array(elec_inl_zb[start:end])

# # Création du graphique à aires empilées continues
# # ax1.fill_between(x_ticks, np.array(elec_imp_dk[start:end]) + np.array(elec_imp_uk[start:end]) + np.array(elec_off_zb[start:end]) + np.array(elec_inl_zb[start:end]),label='Electricity Imports', color='orange')
# # ax1.fill_between(x_ticks, np.array(elec_imp_dk[start:end]) + np.array(elec_imp_uk[start:end]) + np.array(elec_off_zb[start:end]),
# #                   label='From Offshore', color='r')
# # ax1.fill_between(x_ticks, np.array(elec_imp_dk[start:end]) + np.array(elec_imp_uk[start:end]), label='From Imports', color='orange', alpha=0.7)
# # ax1.fill_between(x_ticks, elec_off_zb[start:end], label='From Offshore Wind', color='r', alpha=0.7)
# # ax1.fill_between(x_ticks, elec_inl_zb[start:end], label='From Inland Wind', color='g')
# # ax1.fill_between(x_ticks, np.array(elec_zb_inl[start:end]) + np.array(elec_zb_off[start:end]), label='To Inland and Offshore', color='purple')
# # ax1.fill_between(x_ticks, elec_zb_inl[start:end], label='To Inland', color='purple', alpha=0.7)
# # ax1.fill_between(x_ticks, elec_zb_off[start:end], label='To Offshore', color='gray')
# # ax1.fill_between(x_ticks, np.array(elec_off_zb[start:end]) + np.array(battery[start:end]) - np.array(h2_ep_zb[start:end]),
# #                   label='Net Offshore Production', color='black')

# ax1.bar(x_ticks, elec_imp_dk[start:end], width=bar_width, label='Imports', color='orange', align='center', bottom = np.array(battery[start:end]))
# ax1.bar(x_ticks, elec_imp_uk[start:end], width=bar_width, color='orange', align='center', bottom = np.array(battery[start:end]) + np.array(elec_imp_dk[start:end]))
# ax1.bar(x_ticks, elec_off_zb[start:end], width=bar_width, label='From Offshore', color='r', align='center',bottom=np.array(elec_inl_zb[start:end]))
# ax1.bar(x_ticks, elec_inl_zb[start:end], width=bar_width, label='From Inland', color='g', align='center', bottom = [0] * len(elec_off_zb[start:end]))
# ax1.bar(x_ticks, [-x for x in h2_ep_zb[start:end]], width=bar_width, label='Electrolysers consumption', color = 'b', align='center', bottom = [0] * len(elec_off_zb[start:end]))
# ax1.bar(x_ticks, elec_zb_inl[start:end], width=bar_width, label='To Inland', color='purple', align='center', bottom = - np.array(h2_ep_zb[start:end]) + np.array(elec_zb_off[start:end]))
# ax1.bar(x_ticks, elec_zb_off[start:end], width=bar_width, label='To Offshore', color='gray', align='center')
# ax1.bar(x_ticks, battery[start:end], width=bar_width, label='Electrical batteries', color='black', align='center', bottom = np.array(elec_off_zb[start:end]) - np.array(h2_ep_zb[start:end]))
# ax1.bar(x_ticks, elec_off_zb[start:end], width=bar_width, color='r', align='center',bottom=np.array(elec_inl_zb[start:end]))
# ax1.bar(x_ticks, [-x for x in h2_ep_zb[start:end]], width=bar_width, color = 'b', align='center', bottom = [0] * len(elec_off_zb[start:end]))


# # Personnalisation de l'axe des x
# x_ticks = [x for x in range(0,end - start,24)]
# label = [x for x in range(start,end,24)]
# ax1.set_xticks(x_ticks)  # Position des étiquettes sur l'axe des x
# ax1.set_xticklabels(['Day 1', 'Day 2', 'Day 3'])

# # Ajout de légendes et de labels
# ax1.set_ylabel('Electricity [TWh]')
# ax1.legend(loc='upper right', prop={'size': 7})

# # Sauvegarde et affichage du graphique
# plt.savefig('C:\\Users\\jocel\\OneDrive\\Doctorat\\My papers\\Impact of wind offshore on the Belgium energy system\\Article\\Images\\elec_summer_coa.pdf')
# plt.show()
#%%
""" Winter """

start = 0
end = start + 48 + 1

#max_y = max(max(y1), max(y2), abs(min(y1)), abs(min(y2)))

x_ticks = [x for x in range(0,end - start,24)]
label = [x for x in range(start,end,24)]


fig, ax1 = plt.subplots()

#ax1.plot(elec_imp_dk[start:end],label = 'DK',color = 'y')
#ax1.plot(elec_imp_uk[start:end], label = 'UK', color = 'b')
ax1.plot(elec_off_zb[start:end],label = 'Offshore production ',color = 'r')
ax1.plot(elec_inl_zb[start:end], label = 'Inland production', color = 'g')
battery= [elec_disch_zb[x] - elec_ch_zb[x] for x in range(0,len(elec_inl_zb))]
ax1.plot(battery[start:end], label = 'Electrical batteries', color = 'black')

ax1.plot([-x for x in h2_ep_zb[start:end]],label = 'Electrolysers consumption')
ax1.plot(elec_zb_inl[start:end], label = 'Inland consumption', color = 'purple')
ax1.legend(loc = 'upper right', prop = {'size' : 7})
#ax1.legend(loc='center left', bbox_to_anchor=(1, 0.0),prop={'size': 8})
#max_y2 = max(max(h2_ep_zb[start:end]),max(elec_ch_zb[start:end]),max(elec_disch_zb[start:end]))
#ax1.set_ylim(-max_y2, max_y2)
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(['Day 1', 'Day 2', 'Day 3'])
ax1.set_ylabel('Electricity [TWh]')
#ax1.set_xlabel('Day')
plt.savefig(title + '/' + 'elec_winter_coa.pdf', dpi = 600)
plt.show()

# Données pour les barres
x_ticks = np.arange(len(elec_off_zb[start:end]))  # Position des barres sur l'axe des x
fig, ax1 = plt.subplots()

# Création des graphiques à barres superposées
bar_width = 0.8  # Largeur des barres


ax1.bar(x_ticks, elec_off_zb[start:end], width=bar_width, label='Offshore production', color='r', align='center',bottom=np.array(elec_inl_zb[start:end]))
ax1.bar(x_ticks, elec_inl_zb[start:end], width=bar_width, label='Inland production', color='g', align='center', bottom = [0] * len(elec_off_zb[start:end]))
ax1.bar(x_ticks, [-x for x in h2_ep_zb[start:end]], width=bar_width, label='Electrolysers consumption', color = 'b', align='center', bottom = [0] * len(elec_off_zb[start:end]))
ax1.bar(x_ticks, elec_zb_inl[start:end], width=bar_width, label='Inland consumption', color='purple', align='center', bottom= - np.array(h2_ep_zb[start:end]))
#np.array(elec_off_zb[start:end]) + np.array(elec_inl_zb[start:end]) + np.array(battery[start:end]) 
ax1.bar(x_ticks, battery[start:end], width=bar_width, label='Electrical batteries', color='black', align='center', bottom = np.array(elec_off_zb[start:end]))
ax1.bar(x_ticks, battery[start:end], width=bar_width, color='black', align='center', bottom = np.array(elec_zb_inl[start:end]))
ax1.bar(x_ticks, elec_off_zb[start:end], width=bar_width, color='r', align='center',bottom=np.array(elec_inl_zb[start:end]))
ax1.bar(x_ticks, elec_zb_inl[start:end], width=bar_width, color='purple', align='center', bottom= - np.array(h2_ep_zb[start:end]))
# Personnalisation de l'axe des x
x_ticks = [x for x in range(0,end - start,24)]
label = [x for x in range(start,end,24)]
ax1.set_xticks(x_ticks)  # Position des étiquettes sur l'axe des x
ax1.set_xticklabels(['Day 1', 'Day 2', 'Day 3'])

# Ajout de légendes et de labels
ax1.set_ylabel('Electricity [TWh]')
ax1.legend(loc='upper right', prop={'size': 7})
#ax1.set_xlabel('Day')
plt.savefig('C:\\Users\\jocel\\OneDrive\\Doctorat\\My papers\\Impact of wind offshore on the Belgium energy system\\Article\\Images\\elec_winter_coa.pdf')
plt.show()


winter_elec = {}
winter_elec['Offshore production'] = elec_off_zb[start:end]
winter_elec['Inland production'] = elec_inl_zb[start:end]
winter_elec['Electrical batteries'] = battery[start:end]

winter_elec['Electrolysers consumption'] = [-x for x in h2_ep_zb[start:end]]
winter_elec['Inland consumption'] = elec_zb_inl[start:end]
winter_elec['Offshore consumption'] = elec_zb_off[start:end]
winter_elec['Pipe consumption'] = pipe_zb_inl[start:end]


table_winter_elec = pd.DataFrame(winter_elec)
table_winter_elec.to_excel(title + '/' + 'winter_elec.xlsx')

#%%

import matplotlib.pyplot as plt
import seaborn as sns

#define data
data = [5697.79757177202, 5460.8864592226, 1850.44672278312, 1635.98251175241, 1004.30124300188, 953.868435699058, 839.476750862313, 761.008320981723, 1048.8730124830001, 1112.7147003169998, 338.991514664]
labels = ['Import H2', 'Import NG', 'PV', 'Offshore WT', 'CCGT', 'PCCC CCGT', 'Onshore WT', 'Biomethane', 'Import Elec', 'Transmission', 'Others']

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:10]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')#, labeldistance=1.05)

plt.show()

#%% Import vs production

data = [200.48, 150.43]
labels = ['Import','Production']

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:2]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')#, labeldistance=1.05)

plt.show()

#%% Transformation, losses, end-users

data = [226.68, 118.50,5.73]
labels = ['End users','Conversion','Losses']

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:3]

# #create pie chart
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')#, labeldistance=1.05)

# plt.show()

def func(pct, allvals):
    absolute = round((int(np.round(pct/100.*np.sum(allvals))))/1, 2)
    return f"{pct:.1f}%\n({absolute} TWh)"

wdges, labs, autopct = plt.pie(data, labels = labels, colors = colors, radius=1.4, autopct=lambda pct: func(pct, data), wedgeprops={'linewidth': 3}, textprops={'fontsize': 10}, pctdistance=0.6, labeldistance=1.02, rotatelabels=False)
# Adjust label positions to avoid overlapping
for lab in labs:
    lab.set_horizontalalignment('center')  # Align labels at the center
plt.tight_layout()

plt.setp(labs, fontsize=8)
plt.savefig(title + '/pie_chart.png',dpi = 600)

plt.show()

#%%

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = [
        1004.30124300188,
        953.868435699058,
        839.476750862313,
        761.008320981723,
        715.7283673,
        338.991514664,
        5697.79757177202,
        5460.8864592226,
        1850.44672278312,
        1635.98251175241,
        1048.8730124830001,
        ]
labels = ['CCGT', #'#e31a1c' #  rouge
           'PCCC CCGT', #'#b2df8a' # vert clair
          'Onshore WT', #'#fb9a99' # rose
          'Biomethane', #'#fdbf6f' # orange clair
          'Others', #'gray'
          'Transmission',#'#33a02c' # vert
          'Import H2',# '#1f78b4' # bleu
          'Import NG', # '#ff7f00', #  - orange
          'PV',# '#ffff99' # jaune
          'Offshore WT',# '#cab2d6' # mauve clair
          'Import Electricity'# '#6a3d9a' # violet
]


colors = ['#b2df8a', # vert clair
          '#6a3d9a', # violet
          '#33a02c', # vert
          '#fb9a99', # rose
          '#fdbf6f', # orange clair
          'gray',
          '#1f78b4', # bleu
          '#ff7f00', #  - orange
          '#ffff99', # jaune
          '#cab2d6', # mauve clair
          '#e31a1c' #  rouge
]

colors = ['#b2df8a', # vert clair
          '#a6cee3', # bleu clair '#6a3d9a', # violet
        '#cab2d6', # mauve clair
          '#fb9a99', # rose
          '#fdbf6f', # orange clair
          'silver',
          '#1f78b4', # bleu
          '#ff7f00', #  - orange
          '#ffff99', # jaune
            '#33a02c', # vert
          'sandybrown'# '#e31a1c' #  rouge
]


def func(pct, allvals):
    absolute = round((int(np.round(pct/100.*np.sum(allvals))))/1000, 2)
    return f"{pct:.1f}%\n({absolute} B€)"

wdges, labs, autopct = plt.pie(data, labels = labels, colors = colors, radius=1.4, autopct=lambda pct: func(pct, data), wedgeprops={'linewidth': 3}, textprops={'fontsize': 5.6}, pctdistance=0.9, labeldistance=1.08, rotatelabels=False)
# Adjust label positions to avoid overlapping
for lab in labs:
    lab.set_horizontalalignment('center')  # Align labels at the center
plt.tight_layout()



plt.setp(labs, fontsize=8)
plt.savefig(title + '/pie_chart.png', dpi = 600)



plt.show()


#%%

# 










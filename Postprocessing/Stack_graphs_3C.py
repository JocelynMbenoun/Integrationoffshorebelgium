# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:00:27 2022

@author: bosquetn
"""

import numpy as np
import pandas as pd

max_for_bar = 1000

#%% collect excel files 

# collect h2 groups of nodes with associated colors
df_aggregation_h2 = pd.read_excel(r'color_nodes.xlsx', sheet_name='Aggregation H2')
df_aggregation_h2_reduced = df_aggregation_h2[['group','HEX_code']]
color_dict_h2_help = df_aggregation_h2_reduced.set_index('group').T.to_dict('list')
color_dict_h2 = dict()
for key in color_dict_h2_help.keys():
    color_dict_h2[key] = color_dict_h2_help[key][0]

# collect h2 node to be highlighted
df_highlighted_h2 = pd.read_excel(r'color_nodes.xlsx', sheet_name='Highlighted H2')
df_highlighted_h2_reduced = df_highlighted_h2[['node','HEX_code']]
color_dict_h2_highlighted_help = df_highlighted_h2_reduced.set_index('node').T.to_dict('list')
color_dict_h2_highlighted = dict()
for key in color_dict_h2_highlighted_help.keys():
    color_dict_h2_highlighted[key] = color_dict_h2_highlighted_help[key][0]

# collect ng groups of nodes with associated colors
df_aggregation_ng = pd.read_excel(r'color_nodes.xlsx', sheet_name='Aggregation NG')
df_aggregation_ng_reduced = df_aggregation_ng[['group','HEX_code']]
color_dict_ng_help = df_aggregation_ng_reduced.set_index('group').T.to_dict('list')
color_dict_ng = dict()
for key in color_dict_ng_help.keys():
    color_dict_ng[key] = color_dict_ng_help[key][0]

# collect ng node to be highlighted
df_highlighted_ng= pd.read_excel(r'color_nodes.xlsx', sheet_name='Highlighted NG')
df_highlighted_ng_reduced = df_highlighted_ng[['node','HEX_code']]
color_dict_ng_highlighted_help = df_highlighted_ng_reduced.set_index('node').T.to_dict('list')
color_dict_ng_highlighted = dict()
for key in color_dict_ng_highlighted_help.keys():
    color_dict_ng_highlighted[key] = color_dict_ng_highlighted_help[key][0]

# collect elec groups of nodes with associated colors
df_aggregation_e = pd.read_excel(r'color_nodes.xlsx', sheet_name='Aggregation e')
df_aggregation_e_reduced = df_aggregation_e[['group','HEX_code']]
color_dict_e_help = df_aggregation_e_reduced.set_index('group').T.to_dict('list')
color_dict_e = dict()
for key in color_dict_e_help.keys():
    color_dict_e[key] = color_dict_e_help[key][0]

# collect elec node to be highlighted
df_highlighted_e = pd.read_excel(r'color_nodes.xlsx', sheet_name='Highlighted e')
df_highlighted_e_reduced = df_highlighted_e[['node','HEX_code']]
color_dict_e_highlighted_help = df_highlighted_e_reduced.set_index('node').T.to_dict('list')
color_dict_e_highlighted = dict()
for key in color_dict_e_highlighted_help.keys():
    color_dict_e_highlighted[key] = color_dict_e_highlighted_help[key][0]
    
# collect CO2_pipe groups of nodes with associated colors
df_aggregation_CO2_pipe = pd.read_excel(r'color_nodes.xlsx', sheet_name='Aggregation CO2_pipe')
df_aggregation_CO2_pipe_reduced = df_aggregation_CO2_pipe[['group','HEX_code']]
color_dict_CO2_pipe_help = df_aggregation_CO2_pipe_reduced.set_index('group').T.to_dict('list')
color_dict_CO2_pipe = dict()
for key in color_dict_CO2_pipe_help.keys():
    color_dict_CO2_pipe[key] = color_dict_CO2_pipe_help[key][0]

# collect CO2_pipe node to be highlighted
df_highlighted_CO2_pipe = pd.read_excel(r'color_nodes.xlsx', sheet_name='Highlighted CO2_pipe')
df_highlighted_CO2_pipe_reduced = df_highlighted_CO2_pipe[['node','HEX_code']]
color_dict_CO2_pipe_highlighted_help = df_highlighted_CO2_pipe_reduced.set_index('node').T.to_dict('list')
color_dict_CO2_pipe_highlighted = dict()
for key in color_dict_CO2_pipe_highlighted_help.keys():
    color_dict_CO2_pipe_highlighted[key] = color_dict_CO2_pipe_highlighted_help[key][0]

# collect CO2_air groups of nodes with associated colors
df_aggregation_CO2_air = pd.read_excel(r'color_nodes.xlsx', sheet_name='Aggregation CO2_air')
df_aggregation_CO2_air_reduced = df_aggregation_CO2_air[['group','HEX_code']]
color_dict_CO2_air_help = df_aggregation_CO2_air_reduced.set_index('group').T.to_dict('list')
color_dict_CO2_air = dict()
for key in color_dict_CO2_air_help.keys():
    color_dict_CO2_air[key] = color_dict_CO2_air_help[key][0]

# collect CO2_air node to be highlighted
df_highlighted_CO2_air = pd.read_excel(r'color_nodes.xlsx', sheet_name='Highlighted CO2_air')
df_highlighted_CO2_air_reduced = df_highlighted_CO2_air[['node','HEX_code']]
color_dict_CO2_air_highlighted_help = df_highlighted_CO2_air_reduced.set_index('node').T.to_dict('list')
color_dict_CO2_air_highlighted = dict()
for key in color_dict_CO2_air_highlighted_help.keys():
    color_dict_CO2_air_highlighted[key] = color_dict_CO2_air_highlighted_help[key][0]

# collect colors for energy carriers
df_carriers_colors = pd.read_excel(r'color_nodes.xlsx', sheet_name='energy_vector_colors')
carriers_colors_dict_help = df_carriers_colors.set_index('energy_vector').T.to_dict('list')
carriers_colors_dict = dict()
for key in carriers_colors_dict_help.keys():
    carriers_colors_dict[key] = carriers_colors_dict_help[key][0]

#%% hydrogen

zoom = resolution_h2
start = time_series_h2[0]
end = time_series_h2[1]  

h2_demands = ["demand_h2_heat","demand_h2_industry","demand_h2_transport","demand_h2_transport2"]
h2_storage_subnodes = ['LINEPACK_H2','H2_STORAGE']
h2_interconnections = ["H2_INTERCONNECTION_NL","REGAS_H2"]

h2_cons_prod_data = {'consumption':dict(),'production':dict()}

# data collection
# subnodes in belgium clusters
# 
for demand in h2_demands:
    h2_cons_prod_data['consumption']['Global' + ' ' + demand] = [-x for x in zoom_on_global_parameter(demand,zoom,dictionary_3C)]


for cluster in clusters_belgium:
    for intercon in h2_interconnections:
        if intercon in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            h2_cons_prod_data['consumption'][cluster + 'h2 ' + "exported to " + intercon] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"exported",intercon,zoom,dictionary_3C)]
            h2_cons_prod_data['production'][cluster + ' h2 ' + "imported from " + intercon] = zoom_on_variable_in_cluster_subnode(cluster,"imported",intercon,zoom,dictionary_3C)

    h2_consuming_subnodes = get_cluster_subnodes_names_from_variable("h2_consumed",cluster,dictionary_3C)
    h2_producing_subnodes = get_cluster_subnodes_names_from_variable("h2_produced",cluster,dictionary_3C)
    for subnode in h2_consuming_subnodes:
        h2_cons_prod_data['consumption'][cluster + ' ' + subnode + ' h2 ' + "consumption"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"h2_consumed",subnode,zoom,dictionary_3C)]
    for subnode in h2_producing_subnodes:    
        h2_cons_prod_data['production'][cluster + ' ' + subnode + ' h2 ' + "production"] = zoom_on_variable_in_cluster_subnode(cluster,"h2_produced",subnode,zoom,dictionary_3C)
    
    for subnode in h2_storage_subnodes:
        if subnode in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            h2_cons_prod_data['consumption'][cluster + ' ' + subnode +  ' h2 ' + "charged"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"charged",subnode,zoom,dictionary_3C)]
            h2_cons_prod_data['production'][cluster + ' ' + subnode +  ' h2 ' + "discharged"] = zoom_on_variable_in_cluster_subnode(cluster,"discharged",subnode,zoom,dictionary_3C)

    if "h2_ens" in dictionary_3C["solution"]["elements"][cluster]["variables"]:
        h2_cons_prod_data['production'][cluster + ' h2 ' + "ens"] = zoom_on_variable_in_cluster(cluster,"h2_ens",zoom,dictionary_3C)
    

# remove zero columns 
cons_keys_to_delete = []
for elem in h2_cons_prod_data['consumption'].keys():
    if sum(x for x in h2_cons_prod_data['consumption'][elem]) == 0:
        cons_keys_to_delete.append(elem) 
for elem in cons_keys_to_delete:
    del h2_cons_prod_data['consumption'][elem]
    
prod_keys_to_delete = []
for elem in h2_cons_prod_data['production'].keys():
    if sum(x for x in h2_cons_prod_data['production'][elem]) == 0:
        prod_keys_to_delete.append(elem) 
for elem in prod_keys_to_delete:
    del h2_cons_prod_data['production'][elem]    

#%% construction of dictionary of grouped nodes based on complete dictionary
h2_cons_prod_data_grouped = {'consumption':dict(),'production':dict()}
for index, row in df_aggregation_h2.iterrows():
    if row['node'] in h2_cons_prod_data['consumption'].keys():
        if row['group'] in h2_cons_prod_data_grouped['consumption'].keys():
            sum_lists = [h2_cons_prod_data_grouped['consumption'][row['group']][x] + h2_cons_prod_data['consumption'][row['node']][x] for x in range(len(h2_cons_prod_data['consumption'][row['node']]))] 
            h2_cons_prod_data_grouped['consumption'][row['group']] = sum_lists
        else:
            h2_cons_prod_data_grouped['consumption'][row['group']] = h2_cons_prod_data['consumption'][row['node']]
            
    if row['node'] in h2_cons_prod_data['production'].keys():
        if row['group'] in h2_cons_prod_data_grouped['production'].keys():
            sum_lists = [h2_cons_prod_data_grouped['production'][row['group']][x] + h2_cons_prod_data['production'][row['node']][x] for x in range(len(h2_cons_prod_data['production'][row['node']]))] 
            h2_cons_prod_data_grouped['production'][row['group']] = sum_lists
        else:
            h2_cons_prod_data_grouped['production'][row['group']] = h2_cons_prod_data['production'][row['node']]
#%% bar stack graph

x_ticks = []
if zoom == 'Hour':
    x_ticks = [x for x in range(0,end-start,24)]
    index = [x for x in range(1,8761)]
if zoom == 'Day':
    x_ticks = [x for x in range(-1,end-start,5)]
    index = [x for x in range(1,366)]
if zoom == 'Week':
    x_ticks = [x for x in range(-1,end-start,10)]
    index = [x for x in range(1,54)]
if zoom == 'Month':
    x_ticks = [x for x in range(0,end-start,1)]
    index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

if zoom in ['Day','Week','Month'] or (zoom == 'Hour' and end-start <= max_for_bar):

    
    h2_cons_prod_data_merged = merge_dictionaries(h2_cons_prod_data['consumption'],h2_cons_prod_data['production']).copy()
    h2 = pd.DataFrame.from_dict(h2_cons_prod_data_merged)
    if zoom in ['Week','Month']:
        h2 = h2/1000
    h2['index'] = index
    h2 = h2.set_index('index')
    h2_cons_prod_data_grouped_merged = merge_dictionaries(h2_cons_prod_data_grouped['consumption'],h2_cons_prod_data_grouped['production']).copy()
    h2_cons_prod_data_grouped_merged_old = h2_cons_prod_data_grouped_merged.copy()
    h2_grouped = pd.DataFrame.from_dict(h2_cons_prod_data_grouped_merged)
    if zoom in ['Week','Month']:
        h2_grouped = h2_grouped/1000
    h2_grouped['index'] = index
    h2_grouped = h2_grouped.set_index('index')
    
    
    if legend == 1:
        ax = h2_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_h2.get(x, '#E9E9E9') for x in h2_grouped.columns])
    else:
        h2_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_h2.get(x, '#E9E9E9') for x in h2_grouped.columns],legend=None)
    
    #h2[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_h2, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        handles, labels = ax.get_legend_handles_labels()
        handles = handles[5:1:-1] + handles[0:2]
        labels = labels[5:1:-1] + labels[0:2]
        ax.legend(handles,labels,loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    #plt.set_size_inches(10,10)
    if save_fig_h2 == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_h2 + ' grouped'  +'.png',dpi=300)
        else:
            if not isdir(title + '/no legends'):
                makedirs(title + '/no legends')
            plt.savefig(title + '/no legends/' + name_fig_h2 + ' grouped'  +'.png',dpi=300)
    plt.show()
    
    
# all technologies    

    if legend == 1:
        h2[start:end].plot(kind='bar',width=1.0,stacked=True)
    else:
        h2[start:end].plot(kind='bar',width=1.0,stacked=True,legend=None)
        
    plt.title(title_h2, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    #plt.set_size_inches(10,10)
    if save_fig_h2 == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_h2 + '.png',dpi=300)
        else: 
            plt.savefig(title + '/no legends/' + name_fig_h2 + '.png',dpi=300)
    plt.show()

# get highlighted 

    if legend == 1:
        ax = h2[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_h2_highlighted.get(x, '#E9E9E9') for x in h2.columns])
    else:
        h2[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_h2_highlighted.get(x, '#E9E9E9') for x in h2.columns],legend=None)
    
    #h2[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_h2, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        handles, labels = ax.get_legend_handles_labels()
        handles = handles[15:6:-1] + handles[0:7]
        labels = labels[15:6:-1] + labels[0:7]
        ax.legend(handles,labels,loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    #plt.set_size_inches(10,10)
    if save_fig_h2 == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_h2 + ' highlighted'  +'.png',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_h2 + ' highlighted'  +'.png',dpi=300)
    plt.show()
    


       
# Plot pre installed capacity for GWh capacities
#%% linear stack graph
"""
if zoom == 'Hour' and (end - start) > max_for_bar:
    h2_cons = pd.DataFrame.from_dict(h2_cons_prod_data['consumption'])
    h2_prod = pd.DataFrame.from_dict(h2_cons_prod_data['production'])
    
    fig, ax = plt.subplots()
    
    h2_cons_slice = h2_cons.iloc[pd.np.r_[start:end]]
    
    ax.stackplot(h2_cons_slice.index,h2_cons_dict)
    
    for key in 
    
    labels_p = [key for key in h2_cons_prod_data['production'].keys()]
    labels_p = h2_cons_prod_data['production'].keys()
    
    i = 0
    
    for i in range(end-start):
        plt.stackplot([j for j in range(start+1,end+1)], h2_cons["Global demand_h2_heat"][start:end])
    
    values_p = h2_cons_prod_data['production'].values()
    #colors_p = []
    labels_c = [key for key in h2_cons_prod_data['consumption'].keys()]
    #colors_n = []
    
    plt..stackplot([j for j in range(start+1,end+1)], h2_cons["Global demand_h2_heat"][start:end])
    plt.stackplot([j for j in range(start+1,end+1)], h2_cons["Global demand_h2_heat"][start:end])
    plt.stackplot([j for j in range(start+1,end+1)], h2_cons["INLAND h2 charged"][start:end])

    h2_cons_prod_data['consumption'][labels_c[0]][0:6]
    
    plt.stackplot([j for j in range(start+1,end+1)],h2_EL[start:end],h2_SMR[start:end],h2_ENS[start:end],h2_disch[start:end],h2_imports[start:end],labels=labels_p,colors = colors_p)
    plt.stackplot([j for j in range(start+1,end+1)],h2_FC[start:end],h2_MT[start:end],h2_ch[start:end],demand_h2_id[start:end],demand_h2_tr[start:end],labels=labels_n,colors = colors_n)
    
    plt.title(title_h2)
    plt.xlabel(zoom + ' of the year')
    plt.ylabel('GWh')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    if save_fig_h2 == 1:
        plt.tight_layout()
        plt.savefig(name_fig_h2 + '.png',dpi=300)
        plt.savefig(name_fig_h2 + '.svg')
    plt.show()
"""

#%% NATURAL GAS

zoom = resolution_ng
start = time_series_ng[0]
end = time_series_ng[1]  

ng_demands = ["demand_ng_heat","demand_ng_industry","demand_ng_transport","demand_ng_transport2"]
ng_interconnections = ["NG_INTERCONNECTION_FR","NG_INTERCONNECTION_NV","NG_INTERCONNECTION_NL","NG_INTERCONNECTION_DE","NG_INTERCONNECTION_UK","REGAS","REGAS_GREEN"]
ng_storage_subnodes = ['LINEPACK_NG','NG_STORAGE']
ng_cons_prod_data = {'consumption':dict(),'production':dict()}

# data collection
# subnodes in belgium clusters
# 
for demand in ng_demands:
    ng_cons_prod_data['consumption']['Global' + ' ' + demand] = [-x for x in zoom_on_global_parameter(demand,zoom,dictionary_3C)]


for cluster in clusters_belgium:
    for intercon in ng_interconnections:
        if intercon in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            ng_cons_prod_data['consumption'][cluster + 'ng ' + "exported to " + intercon] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"exported",intercon,zoom,dictionary_3C)]
            ng_cons_prod_data['production'][cluster + ' ng ' + "imported from " + intercon] = zoom_on_variable_in_cluster_subnode(cluster,"imported",intercon,zoom,dictionary_3C)

    ng_consuming_subnodes = get_cluster_subnodes_names_from_variable("ng_consumed",cluster,dictionary_3C)
    ng_producing_subnodes = get_cluster_subnodes_names_from_variable("ng_produced",cluster,dictionary_3C)
    for subnode in ng_consuming_subnodes:
        ng_cons_prod_data['consumption'][cluster + ' ' + subnode + ' ng ' + "consumption"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"ng_consumed",subnode,zoom,dictionary_3C)]
    for subnode in ng_producing_subnodes:    
        ng_cons_prod_data['production'][cluster + ' ' + subnode + ' ng ' + "production"] = zoom_on_variable_in_cluster_subnode(cluster,"ng_produced",subnode,zoom,dictionary_3C)

    # TO DO LINEPACK
    for subnode in ng_storage_subnodes:
        if subnode in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            ng_cons_prod_data['consumption'][cluster + ' ' + subnode +  ' ng ' + "charged"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"charged",subnode,zoom,dictionary_3C)]
            ng_cons_prod_data['production'][cluster + ' ' + subnode +  ' ng ' + "discharged"] = zoom_on_variable_in_cluster_subnode(cluster,"discharged",subnode,zoom,dictionary_3C)
    if "ng_ens" in dictionary_3C["solution"]["elements"][cluster]["variables"]:
        ng_cons_prod_data['production'][cluster + ' ng ' + "ens"] = zoom_on_variable_in_cluster(cluster,"ng_ens",zoom,dictionary_3C)


# remove zero columns 
cons_keys_to_delete_ng = []
for elem in ng_cons_prod_data['consumption'].keys():
    if sum(x for x in ng_cons_prod_data['consumption'][elem]) == 0:
        cons_keys_to_delete_ng.append(elem) 
for elem in cons_keys_to_delete_ng:
    del ng_cons_prod_data['consumption'][elem]
    
prod_keys_to_delete_ng = []
for elem in ng_cons_prod_data['production'].keys():
    if sum(x for x in ng_cons_prod_data['production'][elem]) == 0:
        prod_keys_to_delete_ng.append(elem) 
for elem in prod_keys_to_delete_ng:
    del ng_cons_prod_data['production'][elem]
    
#%% construction of dictionary of grouped nodes based on complete dictionary
ng_cons_prod_data_grouped = {'consumption':dict(),'production':dict()}
for index, row in df_aggregation_ng.iterrows():
    if row['node'] in ng_cons_prod_data['consumption'].keys():
        if row['group'] in ng_cons_prod_data_grouped['consumption'].keys():
            sum_lists = [ng_cons_prod_data_grouped['consumption'][row['group']][x] + ng_cons_prod_data['consumption'][row['node']][x] for x in range(len(ng_cons_prod_data['consumption'][row['node']]))] 
            ng_cons_prod_data_grouped['consumption'][row['group']] = sum_lists
        else:
            ng_cons_prod_data_grouped['consumption'][row['group']] = ng_cons_prod_data['consumption'][row['node']]
            
    if row['node'] in ng_cons_prod_data['production'].keys():
        if row['group'] in ng_cons_prod_data_grouped['production'].keys():
            sum_lists = [ng_cons_prod_data_grouped['production'][row['group']][x] + ng_cons_prod_data['production'][row['node']][x] for x in range(len(ng_cons_prod_data['production'][row['node']]))] 
            ng_cons_prod_data_grouped['production'][row['group']] = sum_lists
        else:
            ng_cons_prod_data_grouped['production'][row['group']] = ng_cons_prod_data['production'][row['node']]

#%% bar stack graph

x_ticks = []
if zoom == 'Hour':
    x_ticks = [x for x in range(0,end-start,int((end-start)/8))]
    index = [x for x in range(1,8761)]
if zoom == 'Day':
    x_ticks = [x for x in range(-1,end-start,5)]
    index = [x for x in range(1,366)]
if zoom == 'Week':
    x_ticks = [x for x in range(-1,end-start,10)]
    index = [x for x in range(1,54)]
if zoom == 'Month':
    x_ticks = [x for x in range(0,end-start,1)]
    index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

if zoom in ['Day','Week','Month'] or (zoom == 'Hour' and end-start <= max_for_bar):

    
    ng_cons_prod_data_merged = merge_dictionaries(ng_cons_prod_data['consumption'],ng_cons_prod_data['production'])
    ng = pd.DataFrame.from_dict(ng_cons_prod_data_merged)
    if zoom in ['Week','Month']:
        ng = ng/1000
    ng['index'] = index
    ng = ng.set_index('index')
    ng_cons_prod_data_grouped_merged = merge_dictionaries(ng_cons_prod_data_grouped['consumption'],ng_cons_prod_data_grouped['production'])
    ng_grouped = pd.DataFrame.from_dict(ng_cons_prod_data_grouped_merged)
    if zoom in ['Week','Month']:
        ng_grouped = ng_grouped/1000
    ng_grouped['index'] = index
    ng_grouped = ng_grouped.set_index('index')

# grouped    

    if legend == 1:
        ax = ng_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_ng.get(x, '#E9E9E9') for x in ng_grouped.columns])
    else:
        ng_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_ng.get(x, '#E9E9E9') for x in ng_grouped.columns],legend=None)
    
    
    #ng[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_ng, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        handles, labels = ax.get_legend_handles_labels()
        labels = labels[7:4:-1] + labels[0:5]
        handles = handles[7:4:-1] + handles[0:5]
        ax.legend(handles, labels,loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    #plt.set_size_inches(10,10)
    if save_fig_ng == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_ng + ' grouped'  +'.png',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_ng + ' grouped'  +'.png',dpi=300)
    plt.show()
    
# all technologies    
    #fig, ax = plt.subplots()
    if legend == 1:
        ng[start:end].plot(kind='bar',width=1.0,stacked=True)
    else: 
        ng[start:end].plot(kind='bar',width=1.0,stacked=True,legend=None)
    #ng[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_ng, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    if save_fig_ng == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        if legend == 1:
            plt.savefig(title + '/' + name_fig_ng + '.png',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_ng + '.png',dpi=300)
    plt.show()

# get highlighted 
    #fig, ax = plt.subplots()
    if legend == 1:
        ng[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_ng_highlighted.get(x, '#E9E9E9') for x in ng.columns])
    else:
        ng[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_ng_highlighted.get(x, '#E9E9E9') for x in ng.columns],legend=None)
    
    #ng[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_ng, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    #plt.set_size_inches(10,10)
    if save_fig_ng == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_ng + ' highlighted'  +'.png',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_ng + ' highlighted'  +'.png',dpi=300)
    plt.show()
    

#%% ELECTRICITY


# same principles as for hydrogen and natural gas except for the imports and export which are not assigned to cluster subnodes but rather to the cluster nodes themselves
    
    
zoom = resolution_e
start = time_series_e[0]
end = time_series_e[1]  

e_demands = ["demand_el","demand_el_ht"] # "daily_demand_for_electric_vehicle" defined on dayily timeframe, not hourly --> issues when transforming to 'zoom' 
e_cons_prod_data = {'consumption':dict(),'production':dict()}

# data collection
# subnodes in belgium clusters
# 
for demand in e_demands:
    e_cons_prod_data['consumption']['Global' + ' ' + demand] = [-x for x in zoom_on_global_parameter(demand,zoom,dictionary_3C)]
e_cons_prod_data['consumption']['Global' + ' demand_el_tr'] = [-x for x in zoom_on_variable_in_cluster(cluster,"demand_el_tr",zoom,dictionary_3C)]

for cluster in clusters:
    e_importing_clusters = get_cluster_names_from_variable('imported',dictionary_3C)
    e_exporting_clusters = get_cluster_names_from_variable('exported',dictionary_3C)
    for cluster in e_importing_clusters:
        e_cons_prod_data['production'][cluster + ' e ' + "imported"] = zoom_on_variable_in_cluster(cluster,"imported",zoom,dictionary_3C)
    for cluster in e_exporting_clusters:
        e_cons_prod_data['consumption'][cluster + ' e ' + "exported"] = [-x for x in zoom_on_variable_in_cluster(cluster,"exported",zoom,dictionary_3C)]

for cluster in clusters_belgium:
    e_consuming_subnodes = get_cluster_subnodes_names_from_variable("e_consumed",cluster,dictionary_3C)
    e_producing_subnodes = get_cluster_subnodes_names_from_variable("e_produced",cluster,dictionary_3C)
    for subnode in e_consuming_subnodes:
        e_cons_prod_data['consumption'][cluster + ' ' + subnode + ' e ' + "consumption"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"e_consumed",subnode,zoom,dictionary_3C)]
    for subnode in e_producing_subnodes:    
        e_cons_prod_data['production'][cluster + ' ' + subnode + ' e ' + "production"] = zoom_on_variable_in_cluster_subnode(cluster,"e_produced",subnode,zoom,dictionary_3C)

    if "BATTERIES" in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
        e_cons_prod_data['consumption'][cluster + ' e ' + "charged"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"charged","BATTERIES",zoom,dictionary_3C)]
        e_cons_prod_data['production'][cluster + ' e ' + "discharged"] = zoom_on_variable_in_cluster_subnode(cluster,"discharged","BATTERIES",zoom,dictionary_3C)

    if "e_ens" in dictionary_3C["solution"]["elements"][cluster]["variables"]:
        e_cons_prod_data['production'][cluster + ' e ' + "ens"] = zoom_on_variable_in_cluster(cluster,"e_ens",zoom,dictionary_3C)
    
    
# remove zero columns 
cons_keys_to_delete_e = []
for elem in e_cons_prod_data['consumption'].keys():
    if sum(x for x in e_cons_prod_data['consumption'][elem]) == 0:
        cons_keys_to_delete_e.append(elem) 
for elem in cons_keys_to_delete_e:
    del e_cons_prod_data['consumption'][elem]
    
prod_keys_to_delete_e = []
for elem in e_cons_prod_data['production'].keys():
    if sum(x for x in e_cons_prod_data['production'][elem]) == 0:
        prod_keys_to_delete_e.append(elem) 
for elem in prod_keys_to_delete_e:
    del e_cons_prod_data['production'][elem]

#% construction of dictionary of grouped nodes based on complete dictionary
e_cons_prod_data_grouped = {'consumption':dict(),'production':dict()}
for index, row in df_aggregation_e.iterrows():
    if row['node'] in e_cons_prod_data['consumption'].keys():
        if row['group'] in e_cons_prod_data_grouped['consumption'].keys():
            sum_lists = [e_cons_prod_data_grouped['consumption'][row['group']][x] + e_cons_prod_data['consumption'][row['node']][x] for x in range(len(e_cons_prod_data['consumption'][row['node']]))] 
            e_cons_prod_data_grouped['consumption'][row['group']] = sum_lists
        else:
            e_cons_prod_data_grouped['consumption'][row['group']] = e_cons_prod_data['consumption'][row['node']]
            
    if row['node'] in e_cons_prod_data['production'].keys():
        if row['group'] in e_cons_prod_data_grouped['production'].keys():
            sum_lists = [e_cons_prod_data_grouped['production'][row['group']][x] + e_cons_prod_data['production'][row['node']][x] for x in range(len(e_cons_prod_data['production'][row['node']]))] 
            e_cons_prod_data_grouped['production'][row['group']] = sum_lists
        else:
            e_cons_prod_data_grouped['production'][row['group']] = e_cons_prod_data['production'][row['node']]

#% bar stack graph

x_ticks = []
if zoom == 'Hour':
    x_ticks = [x for x in range(0,end-start,24)]
    index = [x for x in range(1,8761)]
if zoom == 'Day':
    x_ticks = [x for x in range(-1,end-start,5)]
    index = [x for x in range(1,366)]
if zoom == 'Week':
    x_ticks = [x for x in range(-1,end-start,10)]
    index = [x for x in range(1,54)]
if zoom == 'Month':
    x_ticks = [x for x in range(0,end-start,1)]
    index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

if zoom in ['Day','Week','Month'] or (zoom == 'Hour' and end-start <= max_for_bar):

    
    e_cons_prod_data_merged = merge_dictionaries(e_cons_prod_data['consumption'],e_cons_prod_data['production'])
    e = pd.DataFrame.from_dict(e_cons_prod_data_merged)
    if zoom in ['Week','Month']:
        e = e/1000
    e['index'] = index
    e = e.set_index('index')
    e_cons_prod_data_grouped_merged = merge_dictionaries(e_cons_prod_data_grouped['consumption'],e_cons_prod_data_grouped['production'])
    e_grouped = pd.DataFrame.from_dict(e_cons_prod_data_grouped_merged)
    if zoom in ['Week','Month']:
        e_grouped = e_grouped/1000
    e_grouped['index'] = index
    e_grouped = e_grouped.set_index('index')
    
    e_grouped.to_csv(title + '/' + 'elec_month.csv')

# grouped    

    if legend == 1:
        ax = e_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_e.get(x, '#E9E9E9') for x in e_grouped.columns])
    else:
        e_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_e.get(x, '#E9E9E9') for x in e_grouped.columns],legend=None)
    
    #ng[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_e, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        handles, labels = ax.get_legend_handles_labels()
        labels = labels[7:3:-1] + labels[0:4]
        handles = handles[7:3:-1] + handles[0:4]
        ax.legend(handles,labels, loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 5}, fontsize = 'x-large')
    #plt.set_size_inches(10,10)
    if save_fig_e == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_e + ' grouped'  +'.pdf',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_e + ' grouped'  +'.pdf',dpi=300)
    plt.show()
    
# all technologies        
    #fig, ax = plt.subplots()

    if len(e[start:end]) <= 60:
        width = 1
    else:
        width = 1
    if legend == 1:
        e[start:end].plot(kind='bar',width=1.0,stacked=True)
    else:
        e[start:end].plot(kind='bar',width=1.0,stacked=True,legend=None)
    #e[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_e, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
    if save_fig_e == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        if legend == 1:
            plt.savefig(title + '/' + name_fig_e + '.png',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_e + '.png',dpi=300)
    plt.show()
 
#%% get highlighted 
    #fig, ax = plt.subplots()
    if legend == 1:
        ax = e[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_e_highlighted.get(x, '#E9E9E9') for x in e.columns])
    else:
        e[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_e_highlighted.get(x, '#E9E9E9') for x in e.columns],legend=None)
    
    
    #ng[start:end].plot.bar(stacked=True,width=width,align='center')
    
    plt.title(title_e, y=0.99, fontsize=10)
    plt.xlabel(zoom + ' in the selected timeframe')
    plt.ylabel('GWh')
    if zoom in ['Week','Month']:
        plt.ylabel('TWh')
    plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
    if legend == 1:
        handles, labels = ax.get_legend_handles_labels()
        labels = labels[26:13:-1] + labels[0:14]
        handles = handles[26:13:-1] + handles[0:14]
        ax.legend(handles,labels, loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 5})
    #plt.set_size_inches(10,10)
    if save_fig_e == 1:
        plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
        #plt.tight_layout()
        if legend == 1:
            plt.savefig(title + '/' + name_fig_e + ' highlighted'  +'.png',dpi=300)
        else:
            plt.savefig(title + '/no legends/' + name_fig_e + ' highlighted'  +'.png',dpi=300)
    plt.show()

#%% CO2 balance in pipes

if co2_graph == 1:
    zoom = resolution_CO2_pipe
    start = time_series_CO2_pipe[0]
    end = time_series_CO2_pipe[1]  
    
    PCCCs = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_SMR','PCCC_WS']
    #CO2_pipe_prod_pipes = ['CO2_STORAGE','CO2_EXPORT','METHANATION']
    CO2_pipe_cons_prod_data = {'consumption':dict(),'production':dict()}
    
    
    #'DAC','C02_STORAGE'
    
    #'CO2_STORAGE','CO2_EXPORT','METHANATION'
    # data collection
    # subnodes in belgium clusters
    for cluster in clusters_belgium:
        for pccc in PCCCs:
            if pccc in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
                CO2_pipe_cons_prod_data['production'][cluster + ' co2 ' + "captured in " + pccc] = zoom_on_variable_in_cluster_subnode(cluster,"co2_captured",pccc,zoom,dictionary_3C)
        
        if 'DAC' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            if "co2_exiting" in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]['DAC']["variables"]:
                CO2_pipe_cons_prod_data['production'][cluster + ' co2 ' + "exited from " + 'DAC'] = zoom_on_variable_in_cluster_subnode(cluster,"co2_exiting",'DAC',zoom,dictionary_3C)
            
        if 'CO2_STORAGE' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            CO2_pipe_cons_prod_data['production'][cluster + ' co2 ' + "discharged from " + 'CO2_STORAGE'] = zoom_on_variable_in_cluster_subnode(cluster,"discharged",'CO2_STORAGE',zoom,dictionary_3C)
            CO2_pipe_cons_prod_data['consumption'][cluster + ' co2 ' + "charged into " + 'CO2_STORAGE'] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"charged",'CO2_STORAGE',zoom,dictionary_3C)]
        
        if 'CO2_EXPORT' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            CO2_pipe_cons_prod_data['consumption'][cluster + ' co2 ' + "exported"] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"exported",'CO2_EXPORT',zoom,dictionary_3C)]
        
        if 'METHANATION' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            CO2_pipe_cons_prod_data['consumption'][cluster + ' co2 ' + "consumed by " + 'METHANATION'] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"co2_consumed",'METHANATION',zoom,dictionary_3C)]
        
    
    # remove zero columns 
    cons_keys_to_delete_CO2_pipe = []
    for elem in CO2_pipe_cons_prod_data['consumption'].keys():
        if sum(x for x in CO2_pipe_cons_prod_data['consumption'][elem]) == 0:
            cons_keys_to_delete_CO2_pipe.append(elem) 
    for elem in cons_keys_to_delete_CO2_pipe:
        del CO2_pipe_cons_prod_data['consumption'][elem]
        
    prod_keys_to_delete_CO2_pipe = []
    for elem in CO2_pipe_cons_prod_data['production'].keys():
        if sum(x for x in CO2_pipe_cons_prod_data['production'][elem]) == 0:
            prod_keys_to_delete_CO2_pipe.append(elem) 
    for elem in prod_keys_to_delete_CO2_pipe:
        del CO2_pipe_cons_prod_data['production'][elem]
        
    #%% construction of dictionary of grouped nodes based on complete dictionary
    CO2_pipe_cons_prod_data_grouped = {'consumption':dict(),'production':dict()}
    for index, row in df_aggregation_CO2_pipe.iterrows():
        if row['node'] in CO2_pipe_cons_prod_data['consumption'].keys():
            if row['group'] in CO2_pipe_cons_prod_data_grouped['consumption'].keys():
                sum_lists = [CO2_pipe_cons_prod_data_grouped['consumption'][row['group']][x] + CO2_pipe_cons_prod_data['consumption'][row['node']][x] for x in range(len(CO2_pipe_cons_prod_data['consumption'][row['node']]))] 
                CO2_pipe_cons_prod_data_grouped['consumption'][row['group']] = sum_lists
            else:
                CO2_pipe_cons_prod_data_grouped['consumption'][row['group']] = CO2_pipe_cons_prod_data['consumption'][row['node']]
                
        if row['node'] in CO2_pipe_cons_prod_data['production'].keys():
            if row['group'] in CO2_pipe_cons_prod_data_grouped['production'].keys():
                sum_lists = [CO2_pipe_cons_prod_data_grouped['production'][row['group']][x] + CO2_pipe_cons_prod_data['production'][row['node']][x] for x in range(len(CO2_pipe_cons_prod_data['production'][row['node']]))] 
                CO2_pipe_cons_prod_data_grouped['production'][row['group']] = sum_lists
            else:
                CO2_pipe_cons_prod_data_grouped['production'][row['group']] = CO2_pipe_cons_prod_data['production'][row['node']]
    
    #%% bar stack graph
    
    x_ticks = []
    if zoom == 'Hour':
        x_ticks = [x for x in range(0,end-start,24)]
        index = [x for x in range(1,8761)]
    if zoom == 'Day':
        x_ticks = [x for x in range(-1,end-start,5)]
        index = [x for x in range(1,366)]
    if zoom == 'Week':
        x_ticks = [x for x in range(-1,end-start,10)]
        index = [x for x in range(1,54)]
    if zoom == 'Month':
        x_ticks = [x for x in range(0,end-start,1)]
        index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    if zoom in ['Day','Week','Month'] or (zoom == 'Hour' and end-start <= max_for_bar):
    
        
        CO2_pipe_cons_prod_data_merged = merge_dictionaries(CO2_pipe_cons_prod_data['consumption'],CO2_pipe_cons_prod_data['production'])
        CO2_pipe = pd.DataFrame.from_dict(CO2_pipe_cons_prod_data_merged)
        CO2_pipe['index'] = index
        CO2_pipe = CO2_pipe.set_index('index')
        CO2_pipe_cons_prod_data_grouped_merged = merge_dictionaries(CO2_pipe_cons_prod_data_grouped['consumption'],CO2_pipe_cons_prod_data_grouped['production'])
        CO2_pipe_grouped = pd.DataFrame.from_dict(CO2_pipe_cons_prod_data_grouped_merged)
        CO2_pipe_grouped['index'] = index
        CO2_pipe_grouped = CO2_pipe_grouped.set_index('index')
    
    # grouped    
        fig, ax = plt.subplots()
        if len(CO2_pipe_cons_prod_data_grouped_merged.keys()) != 0:
            if legend == 1:
                CO2_pipe_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_pipe.get(x, '#E9E9E9') for x in CO2_pipe_grouped.columns])
            else:
                CO2_pipe_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_pipe.get(x, '#E9E9E9') for x in CO2_pipe_grouped.columns],legend=None)
                                
            
            #CO2_pipe[start:end].plot.bar(stacked=True,width=width,align='center')
            
            plt.title(title_CO2_pipe, y=0.99, fontsize=10)
            plt.xlabel(zoom + ' in the selected timeframe')
            plt.ylabel('kt')
            plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
            if legend == 1:
                plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
            #plt.set_size_inches(10,10)
            if save_fig_CO2_pipe == 1:
                plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
                #plt.tight_layout()
                if legend == 1:
                    plt.savefig(title + '/' + name_fig_CO2_pipe + ' grouped'  +'.png',dpi=300)
                else:
                    plt.savefig(title + '/no legends/' + name_fig_CO2_pipe + ' grouped'  +'.png',dpi=300)
            plt.show()
        
    # all technologies    
        fig, ax = plt.subplots()
        if len(CO2_pipe_cons_prod_data_merged.keys()) != 0:
            if legend == 1:
                CO2_pipe[start:end].plot(kind='bar',width=1.0,stacked=True)
            else:
                CO2_pipe[start:end].plot(kind='bar',width=1.0,stacked=True,legend=None)
            #ng[start:end].plot.bar(stacked=True,width=width,align='center')
            
            plt.title(title_CO2_pipe, y=0.99, fontsize=10)
            plt.xlabel(zoom + ' in the selected timeframe')
            plt.ylabel('kt')
            plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
            if legend == 1:
                plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
            if save_fig_CO2_pipe == 1:
                plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
                if legend == 1:
                    plt.savefig(title + '/' + name_fig_CO2_pipe + '.png',dpi=300)
                else:
                    plt.savefig(title + '/no legends/' + name_fig_CO2_pipe + '.png',dpi=300)
            plt.show()
    
    # get highlighted 
            fig, ax = plt.subplots()
            if legend == 1:
                CO2_pipe[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_pipe_highlighted.get(x, '#E9E9E9') for x in CO2_pipe.columns])
            else:
                CO2_pipe[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_pipe_highlighted.get(x, '#E9E9E9') for x in CO2_pipe.columns],legend=None)
            
            #ng[start:end].plot.bar(stacked=True,width=width,align='center')
            
            plt.title(title_CO2_pipe, y=0.99, fontsize=10)
            plt.xlabel(zoom + ' in the selected timeframe')
            plt.ylabel('kt')
            plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
            if legend == 1:
                plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
            #plt.set_size_inches(10,10)
            if save_fig_CO2_pipe == 1:
                plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
                #plt.tight_layout()
                if legend == 1:
                    plt.savefig(title + '/' + name_fig_CO2_pipe + ' highlighted'  +'.png',dpi=300)
                else:
                    plt.savefig(title + '/no legends/' + name_fig_CO2_pipe + ' highlighted'  +'.png',dpi=300)
            plt.show()
        
    
    
    #%% CO2 balance in air
    
    zoom = resolution_CO2_air
    start = time_series_CO2_air[0]
    end = time_series_CO2_air[1]  
    
    PCCCs = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_SMR','PCCC_WS']
    co2_producers = ['BIOMASS','CCGT','CHP','OCGT','SMR','WASTE']
    #CO2_air_prod_pipes = ['CO2_STORAGE','CO2_EXPORT','METHANATION']
    CO2_air_cons_prod_data = {'consumption':dict(),'production':dict()}
    
    
    #'DAC','C02_STORAGE'
    
    #'CO2_STORAGE','CO2_EXPORT','METHANATION'
    # data collection
    # subnodes in belgium clusters
    for cluster in clusters_belgium:
        for producer in co2_producers:
            if producer in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
                CO2_air_cons_prod_data['production'][cluster + ' co2 ' + "produced by " + producer] = zoom_on_variable_in_cluster_subnode(cluster,"co2_produced",producer,zoom,dictionary_3C)
        for pccc in PCCCs:
            if pccc in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
                CO2_air_cons_prod_data['consumption'][cluster + ' co2 ' + "captured by " + pccc] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"co2_captured",pccc,zoom,dictionary_3C)]
        
        if 'DAC' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            if "co2_captured" in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]['DAC']["variables"]:
                CO2_air_cons_prod_data['consumption'][cluster + ' co2 ' + "captured by " + 'DAC'] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"co2_captured",'DAC',zoom,dictionary_3C)]
            
        if 'BIOMETHANE' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            CO2_air_cons_prod_data['consumption'][cluster + ' co2 ' + "captured by " + 'BIOMETHANE'] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"co2_captured",'BIOMETHANE',zoom,dictionary_3C)]
        
        if 'REGAS_GREEN' in dictionary_3C["solution"]["elements"][cluster]["sub_elements"]:
            CO2_air_cons_prod_data['consumption'][cluster + ' co2 ' + "captured by " + 'REGAS_GREEN'] = [-x for x in zoom_on_variable_in_cluster_subnode(cluster,"co2_captured",'REGAS_GREEN',zoom,dictionary_3C)]    
    
    # remove zero columns 
    cons_keys_to_delete_CO2_air = []
    for elem in CO2_air_cons_prod_data['consumption'].keys():
        if sum(x for x in CO2_air_cons_prod_data['consumption'][elem]) == 0:
            cons_keys_to_delete_CO2_air.append(elem) 
    for elem in cons_keys_to_delete_CO2_air:
        del CO2_air_cons_prod_data['consumption'][elem]
        
    prod_keys_to_delete_CO2_air = []
    for elem in CO2_air_cons_prod_data['production'].keys():
        if sum(x for x in CO2_air_cons_prod_data['production'][elem]) == 0:
            prod_keys_to_delete_CO2_air.append(elem) 
    for elem in prod_keys_to_delete_CO2_air:
        del CO2_air_cons_prod_data['production'][elem]
        
    #%% construction of dictionary of grouped nodes based on complete dictionary
    CO2_air_cons_prod_data_grouped = {'consumption':dict(),'production':dict()}
    for index, row in df_aggregation_CO2_air.iterrows():
        if row['node'] in CO2_air_cons_prod_data['consumption'].keys():
            if row['group'] in CO2_air_cons_prod_data_grouped['consumption'].keys():
                sum_lists = [CO2_air_cons_prod_data_grouped['consumption'][row['group']][x] + CO2_air_cons_prod_data['consumption'][row['node']][x] for x in range(len(CO2_air_cons_prod_data['consumption'][row['node']]))] 
                CO2_air_cons_prod_data_grouped['consumption'][row['group']] = sum_lists
            else:
                CO2_air_cons_prod_data_grouped['consumption'][row['group']] = CO2_air_cons_prod_data['consumption'][row['node']]
                
        if row['node'] in CO2_air_cons_prod_data['production'].keys():
            if row['group'] in CO2_air_cons_prod_data_grouped['production'].keys():
                sum_lists = [CO2_air_cons_prod_data_grouped['production'][row['group']][x] + CO2_air_cons_prod_data['production'][row['node']][x] for x in range(len(CO2_air_cons_prod_data['production'][row['node']]))] 
                CO2_air_cons_prod_data_grouped['production'][row['group']] = sum_lists
            else:
                CO2_air_cons_prod_data_grouped['production'][row['group']] = CO2_air_cons_prod_data['production'][row['node']]
    
    #%% bar stack graph
    
    x_ticks = []
    if zoom == 'Hour':
        x_ticks = [x for x in range(0,end-start,int((end-start)/8))]
        index = [x for x in range(1,8761)]
    if zoom == 'Day':
        x_ticks = [x for x in range(-1,end-start,5)]
        index = [x for x in range(1,366)]
    if zoom == 'Week':
        x_ticks = [x for x in range(-1,end-start,10)]
        index = [x for x in range(1,54)]
    if zoom == 'Month':
        x_ticks = [x for x in range(0,end-start,1)]
        index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    if zoom in ['Day','Week','Month'] or (zoom == 'Hour' and end-start <= max_for_bar):
    
        
        CO2_air_cons_prod_data_merged = merge_dictionaries(CO2_air_cons_prod_data['consumption'],CO2_air_cons_prod_data['production'])
        CO2_air = pd.DataFrame.from_dict(CO2_air_cons_prod_data_merged)
        CO2_air['index'] = index
        CO2_air = CO2_air.set_index('index')
        CO2_air_cons_prod_data_grouped_merged = merge_dictionaries(CO2_air_cons_prod_data_grouped['consumption'],CO2_air_cons_prod_data_grouped['production'])
        CO2_air_grouped = pd.DataFrame.from_dict(CO2_air_cons_prod_data_grouped_merged)
        CO2_air_grouped['index'] = index
        CO2_air_grouped = CO2_air_grouped.set_index('index')
        
    # grouped    
        fig, ax = plt.subplots()
        if legend == 1:
            CO2_air_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_air.get(x, '#E9E9E9') for x in CO2_air_grouped.columns])
        else:
            CO2_air_grouped[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_air.get(x, '#E9E9E9') for x in CO2_air_grouped.columns],legend=None)
        
        #CO2_air[start:end].plot.bar(stacked=True,width=width,align='center')
        
        plt.title(title_CO2_air, y=0.99, fontsize=10)
        plt.xlabel(zoom + ' in the selected timeframe')
        plt.ylabel('kt')
        plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
        if legend == 1:
            plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
        #plt.set_size_inches(10,10)
        if save_fig_CO2_air == 1:
            plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
            #plt.tight_layout()
            if legend == 1:
                plt.savefig(title + '/' + name_fig_CO2_air + ' grouped'  +'.png',dpi=300)
            else:
                plt.savefig(title + '/no legends/' + name_fig_CO2_air + ' grouped'  +'.png',dpi=300)
        plt.show()
        
    # all technologies    
        fig, ax = plt.subplots()
        if legend == 1:
            CO2_air[start:end].plot(kind='bar',width=1.0,stacked=True)
        else:
            CO2_air[start:end].plot(kind='bar',width=1.0,stacked=True,legend=None)
        #ng[start:end].plot.bar(stacked=True,width=width,align='center')
        
        plt.title(title_CO2_air, y=0.99, fontsize=10)
        plt.xlabel(zoom + ' in the selected timeframe')
        plt.ylabel('kt')
        plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
        if legend == 1:
            plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
        if save_fig_CO2_air == 1:
            plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
            if legend == 1:
                plt.savefig(title + '/' + name_fig_CO2_air + '.png',dpi=300)
            else:
                plt.savefig(title + '/no legends/' + name_fig_CO2_air + '.png',dpi=300)
        plt.show()
    
    # get highlighted 
        fig, ax = plt.subplots()
        if legend == 1:
            CO2_air[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_air_highlighted.get(x, '#E9E9E9') for x in CO2_air.columns])
        else:
            CO2_air[start:end].plot(kind='bar',width=1.0,stacked=True,color=[color_dict_CO2_air_highlighted.get(x, '#E9E9E9') for x in CO2_air.columns],legend=None)
        
        #ng[start:end].plot.bar(stacked=True,width=width,align='center')
        
        plt.title(title_CO2_air, y=0.99, fontsize=10)
        plt.xlabel(zoom + ' in the selected timeframe')
        plt.ylabel('kt')
        plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
        if legend == 1:
            plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
        #plt.set_size_inches(10,10)
        if save_fig_CO2_air == 1:
            plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
            #plt.tight_layout()
            if legend == 1:
                plt.savefig(title + '/' + name_fig_CO2_air + ' highlighted'  +'.png',dpi=300)
            else:
                plt.savefig(title + '/no legends/' + name_fig_CO2_air + ' highlighted'  +'.png',dpi=300)
        plt.show()
    



#%% all energy vectors graph 

if all_en == 1: 
    all_energies_cons_prod = {'consumption':dict(),'production':dict()}
    energy_carriers = {'hydrogen':h2_cons_prod_data,'natural gas':ng_cons_prod_data,'electricity':e_cons_prod_data}
    for energy_vec in energy_carriers.keys():
        for cons_prod in all_energies_cons_prod.keys():
            for cons_nodes in energy_carriers[energy_vec][cons_prod].keys():
                if 'imported' in cons_nodes or 'exported' in cons_nodes or 'production' in cons_nodes or 'demand' in cons_nodes:
                    if energy_vec + ' ' + cons_prod in all_energies_cons_prod[cons_prod]:
                        sum_ts = [all_energies_cons_prod[cons_prod][energy_vec + ' ' + cons_prod][x] + energy_carriers[energy_vec][cons_prod][cons_nodes][x] for x in range(len(all_energies_cons_prod[cons_prod][energy_vec + ' ' + cons_prod]))] 
                        all_energies_cons_prod[cons_prod][energy_vec + ' ' + cons_prod] = sum_ts
                    else:
                        all_energies_cons_prod[cons_prod][energy_vec + ' ' + cons_prod] = energy_carriers[energy_vec][cons_prod][cons_nodes]
        
    zoom = resolution_all
    start = time_series_all[0]
    end = time_series_all[1]  
    
    
    x_ticks = []
    if zoom == 'Hour':
        x_ticks = [x for x in range(0,end-start,int((end-start)/8))]
        index = [x for x in range(1,8761)]
    if zoom == 'Day':
        x_ticks = [x for x in range(-1,end-start,5)]
        index = [x for x in range(1,366)]
    if zoom == 'Week':
        x_ticks = [x for x in range(-1,end-start,10)]
        index = [x for x in range(1,54)]
    if zoom == 'Month':
        x_ticks = [x for x in range(0,end-start,1)]
        index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    if zoom in ['Day','Week','Month'] or (zoom == 'Hour' and end-start <= max_for_bar):
    
        
        all_energies_cons_prod_merged = merge_dictionaries(all_energies_cons_prod['consumption'],all_energies_cons_prod['production'])
        all_energies = pd.DataFrame.from_dict(all_energies_cons_prod_merged)
        if zoom in ['Week','Month']:
            all_energies = all_energies/1000
        all_energies['index'] = index
        all_energies = all_energies.set_index('index')
            
    # all technologies    
        fig, ax = plt.subplots()
        if legend == 1:
            all_energies[start:end].plot(kind='bar',width=1.0,stacked=True,color=[carriers_colors_dict.get(x, '#E9E9E9') for x in all_energies.columns])
        else:
            all_energies[start:end].plot(kind='bar',width=1.0,stacked=True,color=[carriers_colors_dict.get(x, '#E9E9E9') for x in all_energies.columns],legend=None)
        #ng[start:end].plot.bar(stacked=True,width=width,align='center')
        
        plt.title(title_all, y=0.99, fontsize=10)
        plt.xlabel(zoom + ' in the selected timeframe')
        plt.ylabel('GWh')
        if zoom in ['Week','Month']:
            plt.ylabel('TWh')
        plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
        if legend == 1:
            plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 5})
        if save_fig_all == 1:
            plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
            if legend == 1:
                plt.savefig(title + '/' + name_fig_all +  '.png',dpi=300)
            else:
                plt.savefig(title + '/no legends/' + name_fig_all +  '.png',dpi=300)
        plt.show()




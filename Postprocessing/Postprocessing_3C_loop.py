# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:14:20 2022

@author: Jocelyn Mbenoun
"""

import json
from postprocessor_3C import *
from bs4 import BeautifulSoup
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'pdf')
import subprocess
import time
from os import makedirs
from os.path import isdir, join
                

titles = ['base_case_cost_h2_0.075','base_case_elec_cost_h2_0.075','High_renew_cost_h2_0.075','High_renew_elec_cost_h2_0.075'] # nom de modèle pour lequel on veut 
titles = ['base_case_elec_cost_h2_0.075','High_renew_cost_h2_0.075','High_renew_elec_cost_h2_0.075']

opti = 0 # 1 to run the optimisation
cos_cap = 0 # 1 to produce and save the graphs of costs and capacities
diag = 0 # 1 to produce and save the diagram
st_gr = 1 # 1 to produce and save the stack graphs
study = 0 # 1 to produce stack graph by clusters
graphs = 0 # 1 to produce graphs used for the papers

for title in titles:
    
    name_file = '3_clusters_Belgium_'+ title
    name_output = name_file
    file_path = 'C:/Users/jocel/Documents/Doctorat/3_clusters/' + name_file + '.json' # path to the json file
    save_tables = 1 # if 1: tables of results are saved in csv, if 0: tables are not saved
    
    # read file 
    with open (file_path, 'r') as myfile:
        data = myfile.read()
        
    # Create folder for results to be saved
    
    if not isdir(title):
        makedirs(title)
        
    # parse file
    dictionary_3C = json.loads(data)
    
    # Define Clusters
    clusters_belgium = ["OFFSHORE", "ZEEBRUGGE","INLAND"]
    clusters_neighbours = ["DENMARK","DEUTSCHLAND","FRANCE","LUXEMBOURG","NETHERLANDS","UNITED_KINGDOM"]
    clusters = ["OFFSHORE", "ZEEBRUGGE","INLAND","DENMARK","DEUTSCHLAND","FRANCE","LUXEMBOURG","NETHERLANDS","UNITED_KINGDOM"] 
    clusters_interconnection_elec = ["HV_OFF_ZB","HV_ZB_INL"]
    clusters_interconnection_mol = ["PIPE_H2_OFF_ZB","PIPE_H2_ZB_INL","PIPE_NG_ZB_INL"]
    exec(open("postprocessor_3C.py").read())
    
    exec(open("Results_3C.py").read())
    
    
    # costs
    
    if cos_cap == 1:
        
        logscale = 0
        clust_capa = 'INLAND'
        clust = 'INLAND'
        name_fig_capa_alt = 'Installed capacities in Belgium'
        name_fig_capa = 'Total subnodes capacities in cluster'
        name_fig_costs = 'Total subnodes costs in cluster'
        name_fig_BE_costs = 'Total costs in BELGIUM by cost category'
        name_fig_BE_total_costs = 'Total costs in BELGIUM by energy vector'
        save_fig_capa = 1
        save_fig_costs = 1
        save_fig_BE_costs = 1
        save_fig_BE_total_costs = 1
        exec(open("Capacities_costs_3C.py").read())
    
    # Diagram
    
    if diag == 1:
    
        exec(open("Diagram_3C.py").read())
    
    
    # Stacks graphs for each energetic vector
    
    if st_gr == 1:
        
        startTime = time.time()
        # Production and consumption
        
        # Check all nodes on al levels where there is consumption and/production of a certain energy vector.
        
        legend = 1
        co2_graph = 1
        all_en = 0
        while legend < 2:
            #resolutions = ['Hour','Day','Week','Month']
            resolutions = ['Month']
            save_figs = 1
            
            for resolution in resolutions:
                if resolution == 'Hour':
                    time_series = [0,0+24*30]#[16*24,26*24]
                if resolution == 'Day':
                    time_series = [0,31]    
                if resolution == 'Week':
                    time_series = [0,53]    
                if resolution == 'Month':
                    time_series = [0,12]
                        
                resolution_h2 = resolution
                time_series_h2 = time_series
                title_h2 = 'Hydrogen for ' + title
                save_fig_h2 = save_figs
                name_fig_h2 = 'Hydrogen ' + title + '_' + resolution
                
                resolution_e = resolution
                time_series_e = time_series
                title_e = 'Electricity for ' + title
                save_fig_e = save_figs
                name_fig_e = 'Electricity ' + title + '_' + resolution
                    
                resolution_ng = resolution
                time_series_ng = time_series
                title_ng = 'Natural gas for ' + title
                save_fig_ng = save_figs
                name_fig_ng = 'Natural gas ' + title + '_' + resolution
                
                resolution_CO2_pipe = resolution
                time_series_CO2_pipe = time_series
                title_CO2_pipe = 'CO2 pipe for ' + title
                save_fig_CO2_pipe = save_figs
                name_fig_CO2_pipe = 'CO2 pipe ' + title + '_' + resolution
                
                resolution_CO2_air = resolution
                time_series_CO2_air = time_series
                title_CO2_air = 'CO2 air for ' + title
                save_fig_CO2_air = save_figs
                name_fig_CO2_air = 'CO2 air ' + title + '_' + resolution
                
                resolution_all = resolution
                time_series_all = time_series
                title_all = 'All energy carriers for ' + title
                save_fig_all = save_figs
                name_fig_all = 'All energy carriers ' + title + '_' + resolution
                exec(open("Stack_graphs_3C.py").read())
            
            legend += 1
            
            
        executionTime = (time.time() - startTime)
        print('Execution time in seconds: ' + str(executionTime))
        
    if study == 1:
        
        exec(open("Studies_3C.py").read())
        
        
    if graphs == 1:
        if cos_cap == 0:
            logscale = 0
            clust_capa = 'INLAND'
            clust = 'INLAND'
            name_fig_capa_alt = 'Installed capacities in Belgium'
            name_fig_capa = 'Total subnodes capacities in cluster'
            name_fig_costs = 'Total subnodes costs in cluster'
            name_fig_BE_costs = 'Total costs in BELGIUM by cost category'
            name_fig_BE_total_costs = 'Total costs in BELGIUM by energy vector'
            save_fig_capa = 1
            save_fig_costs = 1
            save_fig_BE_costs = 1
            save_fig_BE_total_costs = 1
            exec(open("Capacities_costs_3C.py").read())
            
        
        exec(open("Graphs.py").read())



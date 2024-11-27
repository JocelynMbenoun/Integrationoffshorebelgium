# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 08:05:43 2022

@author: Jocelyn
"""

import numpy as np
import matplotlib.pyplot as plt

zoom = 'Hour'
start = 0
end = 24*3

""" Electricity balances """

# Electricité Offshore

elec_woff = zoom_on_variable_in_cluster_subnode('OFFSHORE','e_produced','WIND_OFFSHORE',zoom,dictionary_3C)
elec_disch = zoom_on_variable_in_cluster_subnode('OFFSHORE','discharged','BATTERIES',zoom,dictionary_3C)
elec_fc = zoom_on_variable_in_cluster_subnode('OFFSHORE','e_produced','FUEL_CELLS',zoom,dictionary_3C)
elec_zb_off = zoom_on_variable_in_cluster('HV_OFF_ZB','e_reverse_out',zoom,dictionary_3C)
elec_ep = [-x for x in zoom_on_variable_in_cluster_subnode('OFFSHORE','e_consumed','ELECTROLYSIS_PLANTS',zoom,dictionary_3C)]
elec_ch = [-x for x in zoom_on_variable_in_cluster_subnode('OFFSHORE','charged','BATTERIES',zoom,dictionary_3C)]
elec_off_zb = [-x for x in zoom_on_variable_in_cluster('HV_OFF_ZB','e_forward_in',zoom,dictionary_3C)]

 
y_values_neg = {
    "EP":elec_ep[start:end],
    "BATT CH":elec_ch[start:end], 
    "OFF-ZB":elec_off_zb[start:end]}
y_values_pos = {
    "WOFF": elec_woff[start:end], 
    "BATT DISCH": elec_disch[start:end],
    "FC":elec_fc[start:end], 
    "ZB-OFF":elec_zb_off[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Offshore electricity balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

# Electricité Zeebrugge

elec_off_zb = zoom_on_variable_in_cluster('HV_OFF_ZB','e_forward_out',zoom,dictionary_3C)
elec_inl_zb = zoom_on_variable_in_cluster('HV_ZB_INL','e_reverse_out',zoom,dictionary_3C)
elec_imp_dk = zoom_on_variable_in_cluster('DENMARK','imported',zoom,dictionary_3C)
elec_imp_uk = zoom_on_variable_in_cluster('UNITED_KINGDOM','imported',zoom,dictionary_3C)
elec_disch = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','discharged','BATTERIES',zoom,dictionary_3C)
elec_zb_off = [-x for x in zoom_on_variable_in_cluster('HV_OFF_ZB','e_reverse_in',zoom,dictionary_3C)]
elec_zb_inl = [-x for x in zoom_on_variable_in_cluster('HV_ZB_INL','e_forward_in',zoom,dictionary_3C)]
elec_ep = [-x for x in zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','e_consumed','ELECTROLYSIS_PLANTS',zoom,dictionary_3C)]
elec_dac = [-x for x in zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','e_consumed','DAC',zoom,dictionary_3C)]
elec_ch = [-x for x in zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','charged','BATTERIES',zoom,dictionary_3C)]


y_values_neg = {
    "ZB-OFF":elec_zb_off[start:end],
    "ZB-INL":elec_zb_inl[start:end], 
    "EP":elec_ep[start:end], 
    "DAC":elec_dac[start:end],
    "BATT CH":elec_ch[start:end]}
y_values_pos = {
    "BATT DISCH":elec_disch[start:end],
    "OFF-ZB": elec_off_zb[start:end], 
    "INL-ZB": elec_inl_zb[start:end],
    "DK":elec_imp_dk[start:end], 
    "UK":elec_imp_uk[start:end]}
    

x = [i for i in range(start+1,end+1)]

x_ticks = []
if zoom == 'Hour':
    x_ticks = [x for x in range(0,end-start,24)]
    index = [x for x in range(1,8761)]
if zoom == 'Day':
    x_ticks = [x for x in range(-1,end-start,1)]
    index = [x for x in range(1,366)]
if zoom == 'Week':
    x_ticks = [x for x in range(-1,end-start,10)]
    index = [x for x in range(1,54)]
if zoom == 'Month':
    x_ticks = [x for x in range(0,end-start,1)]
    index = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Zeebrugge electricity balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
#plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()



#%% Electricité Inland

zoom = 'Month'
start = 0
end = start + 12

elec_zb_inl = zoom_on_variable_in_cluster('HV_ZB_INL','e_forward_out',zoom,dictionary_3C)
elec_pv = zoom_on_variable_in_cluster_subnode('INLAND','e_produced','PV',zoom,dictionary_3C)
elec_won = zoom_on_variable_in_cluster_subnode('INLAND','e_produced','WIND_ONSHORE',zoom,dictionary_3C)
elec_ccgt = zoom_on_variable_in_cluster_subnode('INLAND','e_produced','CCGT',zoom,dictionary_3C)
elec_ocgt = zoom_on_variable_in_cluster_subnode('INLAND','e_produced','OCGT',zoom,dictionary_3C)
elec_bm = zoom_on_variable_in_cluster_subnode('INLAND','e_produced','BIOMASS',zoom,dictionary_3C)
elec_disch = zoom_on_variable_in_cluster_subnode('INLAND','discharged','BATTERIES',zoom,dictionary_3C)
elec_disch_ph = zoom_on_variable_in_cluster_subnode('INLAND','discharged','PUMPED_HYDRO',zoom,dictionary_3C)
elec_imp_nl = zoom_on_variable_in_cluster('NETHERLANDS','imported',zoom,dictionary_3C)
elec_imp_fr = zoom_on_variable_in_cluster('FRANCE','imported',zoom,dictionary_3C)
elec_imp_lu = zoom_on_variable_in_cluster('LUXEMBOURG','imported',zoom,dictionary_3C)
elec_imp_de = zoom_on_variable_in_cluster('DEUTSCHLAND','imported',zoom,dictionary_3C)

elec_inl_zb = [-x for x in zoom_on_variable_in_cluster('HV_ZB_INL','e_reverse_in',zoom,dictionary_3C)]
elec_ep = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','e_consumed','ELECTROLYSIS_PLANTS',zoom,dictionary_3C)] 
elec_dac = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','e_consumed','DAC',zoom,dictionary_3C)]
elec_smr = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','e_consumed','SMR',zoom,dictionary_3C)]
elec_ch = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','BATTERIES',zoom,dictionary_3C)]
elec_ch_ph = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','PUMPED_HYDRO',zoom,dictionary_3C)]
elec_dem = [-x for x in zoom_on_global_parameter("demand_el",zoom,dictionary_3C)]
elec_dem_ht = [-x for x in zoom_on_global_parameter("demand_el_ht",zoom,dictionary_3C)]
elec_dem_tr = [-x for x in zoom_on_variable_in_cluster("INLAND","demand_el_tr",zoom,dictionary_3C)]

y_values_neg = {
    "INL-ZB":elec_inl_zb[start:end],
    "EP":elec_ep[start:end], 
    "DAC":elec_dac[start:end], 
    "SMR":elec_smr[start:end],
    "BATT CH":elec_ch[start:end],
    "PH CH":elec_ch_ph[start:end],
    "DEM BASE":elec_dem[start:end],
    "DEM HT":elec_dem_ht[start:end],
    "DEM TR":elec_dem_tr[start:end]}
y_values_pos = {
    "ZB-INL": elec_zb_inl[start:end], 
    "PV": elec_pv[start:end],
    "WON":elec_won[start:end],
    "CCGT":elec_ccgt[start:end],
    "OCGT":elec_ocgt[start:end],
    "BM":elec_bm[start:end],
    "BATT DISCH":elec_disch[start:end],
    "PH DISCH":elec_disch_ph[start:end],
    "NL":elec_imp_nl[start:end],
    "FR":elec_imp_fr[start:end],
    "LU":elec_imp_lu[start:end],
    "DE":elec_imp_de[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Inland electricity balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
#plt.xticks(ticks=x_ticks, rotation=0, horizontalalignment="center")
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

""" Hydrogen balance """

#%% Hydrogen Offshore

h2_ep = zoom_on_variable_in_cluster_subnode('OFFSHORE','h2_produced','ELECTROLYSIS_PLANTS',zoom,dictionary_3C)
h2_zb_off = zoom_on_variable_in_cluster('PIPE_H2_OFF_ZB','flow_reverse_out',zoom,dictionary_3C)
h2_disch = zoom_on_variable_in_cluster_subnode('OFFSHORE','discharged','H2_STORAGE',zoom,dictionary_3C)

h2_fc = [-x for x in zoom_on_variable_in_cluster_subnode('OFFSHORE','h2_consumed','FUEL_CELLS',zoom,dictionary_3C)]
h2_off_zb = [-x for x in zoom_on_variable_in_cluster('PIPE_H2_OFF_ZB','flow_forward_in',zoom,dictionary_3C)]
h2_ch = [-x for x in zoom_on_variable_in_cluster_subnode('OFFSHORE','charged','H2_STORAGE',zoom,dictionary_3C)]

y_values_neg = {
    "FC":h2_fc[start:end], 
    "OFF-ZB":h2_off_zb[start:end],
    "H2 CH":h2_ch[start:end]}
y_values_pos = {
    "EP":h2_ep[start:end], 
    "ZB-OFF":h2_zb_off[start:end],
    "H2 DISCH":h2_disch[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Offshore hydrogen balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

# Hydrogen Zeebrugge

h2_off_zb = zoom_on_variable_in_cluster('PIPE_H2_OFF_ZB','flow_forward_out',zoom,dictionary_3C)
h2_ep = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','h2_produced','ELECTROLYSIS_PLANTS',zoom,dictionary_3C)
h2_inl_zb = zoom_on_variable_in_cluster('PIPE_H2_ZB_INL','flow_reverse_out',zoom,dictionary_3C)
h2_disch = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','discharged','H2_STORAGE',zoom,dictionary_3C)
h2_imp_nv = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','H2_INTERCONNECTION_NV',zoom,dictionary_3C)
h2_imp_uk = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','H2_INTERCONNECTION_UK',zoom,dictionary_3C)
h2_imp_fr = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','H2_INTERCONNECTION_FR',zoom,dictionary_3C)

h2_zb_off = [-x for x in zoom_on_variable_in_cluster('PIPE_H2_OFF_ZB','flow_reverse_in',zoom,dictionary_3C)]
h2_zb_inl = [-x for x in zoom_on_variable_in_cluster('PIPE_H2_ZB_INL','flow_forward_in',zoom,dictionary_3C)]
h2_fc = [-x for x in zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','h2_consumed','FUEL_CELLS',zoom,dictionary_3C)]
h2_ch = [-x for x in zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','charged','H2_STORAGE',zoom,dictionary_3C)]


y_values_neg = {
    "ZB-OFF":h2_zb_off[start:end],
    "ZB-INL":h2_zb_inl[start:end],
    "FC":h2_fc[start:end], 
    "H2 CH":h2_ch[start:end]}
y_values_pos = {
    "OFF-ZB": h2_off_zb[start:end], 
    "INL-ZB": h2_inl_zb[start:end],
    "EP":h2_ep[start:end], 
    "H2 DISCH":h2_disch[start:end],
    "NV":h2_imp_nv[start:end], 
    "UK":h2_imp_uk[start:end],
    "FR":h2_imp_fr[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Zeebrugge hydrogen balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

# Hydrogen Inland

h2_zb_inl = zoom_on_variable_in_cluster('PIPE_H2_ZB_INL','flow_forward_out',zoom,dictionary_3C)
h2_ep = zoom_on_variable_in_cluster_subnode('INLAND','h2_produced','ELECTROLYSIS_PLANTS',zoom,dictionary_3C)
h2_smr = zoom_on_variable_in_cluster_subnode('INLAND','h2_produced','SMR',zoom,dictionary_3C)
h2_disch = zoom_on_variable_in_cluster_subnode('INLAND','discharged','H2_STORAGE',zoom,dictionary_3C)
h2_imp_de = zoom_on_variable_in_cluster_subnode('INLAND','imported','H2_INTERCONNECTION_DE',zoom,dictionary_3C)
h2_imp_nl = zoom_on_variable_in_cluster_subnode('INLAND','imported','H2_INTERCONNECTION_NL',zoom,dictionary_3C)

h2_inl_zb = [-x for x in zoom_on_variable_in_cluster('PIPE_H2_ZB_INL','flow_reverse_in',zoom,dictionary_3C)]
h2_fc = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','h2_consumed','FUEL_CELLS',zoom,dictionary_3C)]
h2_ch = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','H2_STORAGE',zoom,dictionary_3C)]
h2_dem_ind = [-x for x in zoom_on_global_parameter("demand_h2_industry",zoom,dictionary_3C)]
h2_dem_ht = [-x for x in zoom_on_global_parameter("demand_h2_heat",zoom,dictionary_3C)]
h2_dem_tr = [-x for x in zoom_on_global_parameter("demand_h2_transport",zoom,dictionary_3C)]
h2_dem_tr2 = [-x for x in zoom_on_global_parameter("demand_h2_transport2",zoom,dictionary_3C)]

y_values_neg = {
    "INL-ZB":h2_inl_zb[start:end],
    "FC":h2_fc[start:end], 
    "H2 CH":h2_ch[start:end],
    "DEM IND":h2_dem_ind[start:end],
    "DEM HT":h2_dem_ht[start:end],
    "DEM TR":h2_dem_tr[start:end],
    "DEM TR2":h2_dem_tr2[start:end]}
y_values_pos = {
    "ZB-INL": h2_zb_inl[start:end], 
    "EP":h2_ep[start:end], 
    "SMR":h2_smr[start:end],
    "H2 DISCH":h2_disch[start:end],
    "DE":h2_imp_de[start:end], 
    "NL":h2_imp_nl[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Inland hydrogen balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

""" Natural gas balance """

# Zeebrugge natural gas

ng_inl_zb = zoom_on_variable_in_cluster('PIPE_NG_ZB_INL','flow_reverse_out',zoom,dictionary_3C)
ng_imp_gr = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','REGAS_GREEN',zoom,dictionary_3C)
ng_imp_nv = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_NV',zoom,dictionary_3C)
ng_imp_uk = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_UK',zoom,dictionary_3C)
ng_imp_fr = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_FR',zoom,dictionary_3C)

ng_zb_inl = [-x for x in zoom_on_variable_in_cluster('PIPE_NG_ZB_INL','flow_forward_in',zoom,dictionary_3C)]

y_values_neg = {
    "ZB-INL":ng_zb_inl[start:end]}
y_values_pos = {
    "GREEN":ng_imp_gr[start:end],
    "NV":ng_imp_nv[start:end], 
    "UK":ng_imp_uk[start:end],
    "FR":ng_imp_fr[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Zeebrugge natural gas balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

# Inland natural gas

ng_zb_inl = zoom_on_variable_in_cluster('PIPE_NG_ZB_INL','flow_forward_out',zoom,dictionary_3C)
ng_bmt = zoom_on_variable_in_cluster_subnode('INLAND','ng_produced','BIOMETHANE',zoom,dictionary_3C)
ng_disch = zoom_on_variable_in_cluster_subnode('INLAND','discharged','NG_STORAGE',zoom,dictionary_3C)
ng_lp_disch = zoom_on_variable_in_cluster_subnode('INLAND','discharged','LINEPACK_NG',zoom,dictionary_3C)
ng_imp_de = zoom_on_variable_in_cluster_subnode('INLAND','imported','NG_INTERCONNECTION_DE',zoom,dictionary_3C)
ng_imp_nl = zoom_on_variable_in_cluster_subnode('INLAND','imported','NG_INTERCONNECTION_NL',zoom,dictionary_3C)

ng_inl_zb = [-x for x in zoom_on_variable_in_cluster('PIPE_NG_ZB_INL','flow_reverse_in',zoom,dictionary_3C)]
ng_ccgt = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','CCGT',zoom,dictionary_3C)]
ng_ocgt = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','OCGT',zoom,dictionary_3C)]
ng_chp = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','CHP',zoom,dictionary_3C)]
ng_smr = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','SMR',zoom,dictionary_3C)]
ng_ch = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','NG_STORAGE',zoom,dictionary_3C)]
ng_lp_ch = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','LINEPACK_NG',zoom,dictionary_3C)]
ng_dem_ind = [-x for x in zoom_on_global_parameter("demand_ng_industry",zoom,dictionary_3C)]
ng_dem_ht = [-x for x in zoom_on_global_parameter("demand_ng_heat",zoom,dictionary_3C)]
ng_dem_tr = [-x for x in zoom_on_global_parameter("demand_ng_transport",zoom,dictionary_3C)]
ng_dem_tr2 = [-x for x in zoom_on_global_parameter("demand_ng_transport2",zoom,dictionary_3C)]

y_values_neg = {
    "INL-ZB":ng_inl_zb[start:end],
    "CCGT":ng_ccgt[start:end], 
    "OCGT":ng_ocgt[start:end],
    "CHP":ng_chp[start:end],
    "SMR":ng_smr[start:end],
    "NG CH":ng_ch[start:end],
    "NG LP CH":ng_lp_ch[start:end],
    "DEM IND":ng_dem_ind[start:end],
    "DEM HT":ng_dem_ht[start:end],
    "DEM TR":ng_dem_tr[start:end],
    "DEM TR2":ng_dem_tr2[start:end]}
y_values_pos = {
    "ZB-INL": ng_zb_inl[start:end], 
    "BMT":ng_bmt[start:end], 
    "NG DISCH":ng_disch[start:end],
    "NG LP DISCH":ng_lp_disch[start:end],
    "DE":ng_imp_de[start:end], 
    "NL":ng_imp_nl[start:end]}

x = [i for i in range(start+1,end+1)]

plt.stackplot(x, y_values_pos.values(), labels = y_values_pos.keys())
plt.stackplot(x, y_values_neg.values(), labels = y_values_neg.keys())
plt.title("Inland natural gas balance for " + title, y=0.99, fontsize=18)
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()



""" Storages studies """ 

# Storages


Batt_off =  zoom_on_variable_in_cluster_subnode('OFFSHORE','state_of_charge','BATTERIES',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_off[start:end], labels = ["Offshore Batteries for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_batt_off = get_total_value_of_variables_in_cluster_subnodes(['charged'],'OFFSHORE',['BATTERIES'],dictionary_3C)['BATTERIES']['charged']/cluster_subnodes_cap_storage['OFFSHORE']['BATTERIES energy']['Total capacity']
max_batt_ch_off = max(zoom_on_variable_in_cluster_subnode('OFFSHORE','charged','BATTERIES','Hour',dictionary_3C))
max_batt_disch_off = max(zoom_on_variable_in_cluster_subnode('OFFSHORE','discharged','BATTERIES','Hour',dictionary_3C))

Batt_off =  zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','state_of_charge','BATTERIES',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_off[start:end], labels = ["Zeebrugge Batteries for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_batt_zb = get_total_value_of_variables_in_cluster_subnodes(['charged'],'ZEEBRUGGE',['BATTERIES'],dictionary_3C)['BATTERIES']['charged']/cluster_subnodes_cap_storage['ZEEBRUGGE']['BATTERIES energy']['Total capacity']
max_batt_ch_zb = max(zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','charged','BATTERIES','Hour',dictionary_3C))
max_batt_disch_zb = max(zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','discharged','BATTERIES','Hour',dictionary_3C))

Batt_inl =  zoom_on_variable_in_cluster_subnode('INLAND','state_of_charge','BATTERIES',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_inl[start:end], labels = ["Inland Batteries for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_batt_inl = get_total_value_of_variables_in_cluster_subnodes(['charged'],'INLAND',['BATTERIES'],dictionary_3C)['BATTERIES']['charged']/cluster_subnodes_cap_storage['INLAND']['BATTERIES energy']['Total capacity']
batt_dis = zoom_on_variable_in_cluster_subnode('INLAND','discharged','BATTERIES','Hour',dictionary_3C)
ind_max_batt_dis = batt_dis.index(max(batt_dis))
batt_ch = zoom_on_variable_in_cluster_subnode('INLAND','charged','BATTERIES','Hour',dictionary_3C)
ind_max_batt_ch = batt_ch.index(max(batt_ch))
max_batt_ch_inl = max(zoom_on_variable_in_cluster_subnode('INLAND','charged','BATTERIES','Hour',dictionary_3C))
max_batt_disch_inl = max(zoom_on_variable_in_cluster_subnode('INLAND','discharged','BATTERIES','Hour',dictionary_3C))


Batt_inl =  zoom_on_variable_in_cluster_subnode('INLAND','state_of_charge','H2_STORAGE',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_inl[start:end], labels = ["Inland h2 storage for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
if cluster_subnodes_cap_storage['INLAND']['H2_STORAGE energy']['Total capacity'] > 0:
    nb_cycle_h2_sto = get_total_value_of_variables_in_cluster_subnodes(['charged'],'INLAND',['H2_STORAGE'],dictionary_3C)['H2_STORAGE']['charged']/cluster_subnodes_cap_storage['INLAND']['H2_STORAGE energy']['Total capacity']
else:
    nb_cycle_h2_sto = 0

Batt_inl =  zoom_on_variable_in_cluster_subnode('INLAND','state_of_charge','NG_STORAGE',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_inl[start:end], labels = ["Inland ch4 storage for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_ng_sto = get_total_value_of_variables_in_cluster_subnodes(['charged'],'INLAND',['NG_STORAGE'],dictionary_3C)['NG_STORAGE']['charged']/cluster_subnodes_cap_storage['INLAND']['NG_STORAGE energy']['Total capacity']

Batt_inl =  zoom_on_variable_in_cluster_subnode('INLAND','state_of_charge','PUMPED_HYDRO',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_inl[start:end], labels = ["Pumped hydro storage for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_ph_inl = get_total_value_of_variables_in_cluster_subnodes(['charged'],'INLAND',['PUMPED_HYDRO'],dictionary_3C)['PUMPED_HYDRO']['charged']/cluster_subnodes_cap_storage['INLAND']['PUMPED_HYDRO energy']['Total capacity']

Batt_inl =  zoom_on_variable_in_cluster_subnode('INLAND','state_of_charge','LINEPACK_NG',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_inl[start:end], labels = ["Linepack for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_lp_inl = get_total_value_of_variables_in_cluster_subnodes(['charged'],'INLAND',['LINEPACK_NG'],dictionary_3C)['LINEPACK_NG']['charged']/get_cluster_element_parameter("INLAND","LINEPACK_NG","pre_installed_capacity",dictionary_3C)[0]
max_lp_ch_inl = max(zoom_on_variable_in_cluster_subnode('INLAND','charged','LINEPACK_NG','Hour',dictionary_3C))
max_lp_disch_inl = max(zoom_on_variable_in_cluster_subnode('INLAND','discharged','LINEPACK_NG','Hour',dictionary_3C))

Batt_inl =  zoom_on_variable_in_cluster_subnode('OFFSHORE','state_of_charge','H2O_STORAGE',zoom,dictionary_3C)
plt.stackplot([i for i in range(start+1,end+1)],Batt_inl[start:end], labels = ["Inland ch4 storage for "+title])
plt.xlabel(zoom + ' in the selected timeframe', fontsize=15)
plt.ylabel('GWh',fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()
nb_cycle_h2o_sto = get_total_value_of_variables_in_cluster_subnodes(['charged'],'OFFSHORE',['H2O_STORAGE'],dictionary_3C)['H2O_STORAGE']['charged']/cluster_subnodes_cap_storage['OFFSHORE']['H2O_STORAGE energy']['Total capacity']
max_h2o_ch_off = max(zoom_on_variable_in_cluster_subnode('OFFSHORE','charged','H2O_STORAGE','Hour',dictionary_3C))
max_h2o_disch_off = max(zoom_on_variable_in_cluster_subnode('OFFSHORE','discharged','H2O_STORAGE','Hour',dictionary_3C))

#%%
""" Studies Offshore """

elec_woff = zoom_on_variable_in_cluster_subnode('OFFSHORE','e_produced','WIND_OFFSHORE','Hour',dictionary_3C)
max_elec_woff = max(elec_woff)
cf_elec_woff = sum(elec_woff)/(8760*cluster_subnodes_capacities_tot['OFFSHORE']['WIND_OFFSHORE']['Total capacity'])
elec_woff_pot = [cluster_subnodes_capacities_tot['OFFSHORE']['WIND_OFFSHORE']['Total capacity'] * i for i in get_cluster_element_parameter("OFFSHORE","WIND_OFFSHORE","production_profile",dictionary_3C)]
max_elec_woff_pot = max(elec_woff_pot)

hour_curt_woff = 0
for i in range(0,len(elec_woff)):
    if elec_woff_pot[i] - elec_woff[i] > 0.01:
        hour_curt_woff +=1
        
curt_woff = sum(elec_woff_pot) - sum(elec_woff)

elec_ch_off = zoom_on_variable_in_cluster_subnode('OFFSHORE','charged','BATTERIES','Hour',dictionary_3C)
elec_soc_off = zoom_on_variable_in_cluster_subnode('OFFSHORE','state_of_charge','BATTERIES','Hour',dictionary_3C)

h2_ep_off = zoom_on_variable_in_cluster_subnode('OFFSHORE','h2_produced','ELECTROLYSIS_PLANTS','Hour',dictionary_3C)
cap_ep_off = cluster_subnodes_capacities_tot['OFFSHORE']['ELECTROLYSIS_PLANTS']['Total capacity']

h2o_ch_off = zoom_on_variable_in_cluster_subnode('OFFSHORE','charged','H2O_STORAGE','Hour',dictionary_3C)
max_h2o_ch_off = max(h2o_ch_off)
h2o_disch_off = zoom_on_variable_in_cluster_subnode('OFFSHORE','discharged','H2O_STORAGE','Hour',dictionary_3C)
max_h2o_disch_off = max(h2o_disch_off)

start = 744*1
end = start + int(744/2)

#max_y = max(max(y1), max(y2), abs(min(y1)), abs(min(y2)))

fig, ax1 = plt.subplots()

ax1.plot(elec_woff[start:end],label = 'prod woff',color = 'r')
ax1.plot(elec_woff_pot[start:end], label = 'pot woff', color = 'g')
ax1.legend(loc='center left', bbox_to_anchor=(-0.5, 0.5),prop={'size': 15})

ax2 = ax1.twinx()

ax2.plot(h2_ep_off[start:end],label = 'ep off')
ax2.plot(elec_ch_off[start:end], label = 'batt ch off')
ax2.legend(loc='center left', bbox_to_anchor=(1.0, 0.5),prop={'size': 15})
plt.show()

plt.plot(elec_soc_off[start:end],label = 'SOC off')
plt.show()

""" Studies Zeebrugge """
#%%
zoom = 'Hour'
elec_ch_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','charged','BATTERIES','Hour',dictionary_3C)
elec_disch_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','discharged','BATTERIES','Hour',dictionary_3C)
elec_soc_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','state_of_charge','BATTERIES','Hour',dictionary_3C)
elec_imp_dk = zoom_on_variable_in_cluster('DENMARK','imported','Hour',dictionary_3C)
elec_imp_uk = zoom_on_variable_in_cluster('UNITED_KINGDOM','imported','Hour',dictionary_3C)

max_imp_dk = max(elec_imp_dk)
max_imp_uk = max(elec_imp_uk)
tot_imp_dk = sum(elec_imp_dk)
tot_imp_uk = sum(elec_imp_uk)

h2_ep_zb = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','h2_produced','ELECTROLYSIS_PLANTS','Hour',dictionary_3C)
cap_ep_zb = cluster_subnodes_capacities_tot['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['Total capacity']

elec_off_zb = zoom_on_variable_in_cluster('HV_OFF_ZB','e_forward_out','Hour',dictionary_3C)
elec_inl_zb = zoom_on_variable_in_cluster('HV_ZB_INL','e_reverse_out','Hour',dictionary_3C)

elec_zb_inl = [-x for x in zoom_on_variable_in_cluster('HV_ZB_INL','e_forward_in','Hour',dictionary_3C)]

ng_imp_nv = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_NV',zoom,dictionary_3C)
ng_imp_uk = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_UK',zoom,dictionary_3C)
ng_imp_fr = zoom_on_variable_in_cluster_subnode('ZEEBRUGGE','imported','NG_INTERCONNECTION_FR',zoom,dictionary_3C)

max_ng_imp_nv = max(ng_imp_nv)
max_ng_imp_uk = max(ng_imp_uk)
max_ng_imp_fr = max(ng_imp_fr)

start = 4680
end = start + 96 + 1

#max_y = max(max(y1), max(y2), abs(min(y1)), abs(min(y2)))

x_ticks = [x for x in range(0,end - start,24)]
label = [x for x in range(start,end,24)]


fig, ax1 = plt.subplots()

ax1.plot(elec_imp_dk[start:end],label = 'DK',color = 'y')
ax1.plot(elec_imp_uk[start:end], label = 'UK', color = 'b')
ax1.plot(elec_off_zb[start:end],label = 'OFF',color = 'r')
ax1.plot(elec_zb_inl[start:end], label = 'ZB INL', color = 'purple')
ax1.legend(loc='center left', bbox_to_anchor=(-0.4, 0.5),prop={'size': 15})
ax1.set_ylabel('TWh')

ax2 = ax1.twinx()

ax2.plot(elec_disch_zb[start:end], label = 'batt dis zb', color = 'black')
ax2.plot(elec_inl_zb[start:end], label = 'INL ZB', color = 'g')
ax2.plot([-x for x in h2_ep_zb[start:end]],label = 'ep zb')
ax2.plot([-x for x in elec_ch_zb[start:end]], label = 'batt ch zb', color = 'black')
ax2.legend(loc='center left', bbox_to_anchor=(1.1, 0.5),prop={'size': 15})
max_y2 = max(max(h2_ep_zb[start:end]),max(elec_ch_zb[start:end]),max(elec_disch_zb[start:end]))
ax2.set_ylim(-max_y2, max_y2)
ax2.set_xticks(x_ticks)
ax2.set_xticklabels(label)
ax2.set_ylabel('TWh')
plt.show()

# plt.plot(elec_soc_zb[start:end],label = 'SOC zb')
# plt.show()

""" Studies Inland """
#%%
cluster = 'INLAND'

zoom = 'Hour'

elec_pv = zoom_on_variable_in_cluster_subnode('INLAND','e_produced','PV','Hour',dictionary_3C)
max_elec_pv = max(elec_pv)
cf_elec_pv = sum(elec_pv)/(8760*cluster_subnodes_capacities_tot['INLAND']['PV']['Total capacity'])
elec_pv_pot = [cluster_subnodes_capacities_tot['INLAND']['PV']['Total capacity'] * i for i in get_cluster_element_parameter('INLAND','PV',"production_profile",dictionary_3C)]
max_elec_pv_pot = max(elec_pv_pot)

hour_curt_pv = 0
for i in range(0,len(elec_pv)):
    if elec_pv_pot[i] - elec_pv[i] > 0.01 :
        hour_curt_pv +=1
        
curt_pv = sum(elec_pv_pot) - sum(elec_pv)

node = 'WIND_ONSHORE'
elec_won = zoom_on_variable_in_cluster_subnode('INLAND','e_produced',node,'Hour',dictionary_3C)
max_elec_won = max(elec_won)
cf_elec_won = sum(elec_won)/(8760*cluster_subnodes_capacities_tot['INLAND'][node]['Total capacity'])
elec_won_pot = [cluster_subnodes_capacities_tot['INLAND'][node]['Total capacity'] * i for i in get_cluster_element_parameter('INLAND',node,"production_profile",dictionary_3C)]
max_elec_won_pot = max(elec_won_pot)

hour_curt_won = 0
for i in range(0,len(elec_won)):
    if elec_won_pot[i] - elec_won[i] > 0.1:
        hour_curt_won +=1

curt_won = sum(elec_won_pot) - sum(elec_won)

node = 'CCGT'
elec_ccgt = zoom_on_variable_in_cluster_subnode('INLAND','e_produced',node,'Hour',dictionary_3C)
max_elec_ccgt = max(elec_ccgt)

elec_imp_nl = zoom_on_variable_in_cluster('NETHERLANDS','imported',zoom,dictionary_3C)
elec_imp_fr = zoom_on_variable_in_cluster('FRANCE','imported',zoom,dictionary_3C)
elec_imp_lu = zoom_on_variable_in_cluster('LUXEMBOURG','imported',zoom,dictionary_3C)
elec_imp_de = zoom_on_variable_in_cluster('DEUTSCHLAND','imported',zoom,dictionary_3C)
h2_imp_nl = zoom_on_variable_in_cluster_subnode('INLAND','imported','H2_INTERCONNECTION_NL',zoom,dictionary_3C)


max_imp_nl = max(elec_imp_nl)
max_imp_fr = max(elec_imp_fr)
max_imp_lu = max(elec_imp_lu)
max_imp_de = max(elec_imp_de)
max_h2_imp_nl = max(h2_imp_nl)

#import 

tot_imp_fr = sum(elec_imp_fr)
tot_imp_lu = sum(elec_imp_lu)
tot_imp_de = sum(elec_imp_de)
tot_imp_nl = sum(elec_imp_nl)

start = 3768
end = start + 49
x_ticks = [x for x in range(0,end - start,24)]
label = [x for x in range(start,end,24)]

fig, ax1 = plt.subplots()
ax1.plot(elec_pv_pot[start:end], label = 'pot pv')
ax1.plot(elec_pv[start:end],label = 'prod pv')
ax1.plot(elec_won_pot[start:end], label = 'pot won')
ax1.plot(elec_won[start:end],label = 'prod won')
ax1.plot(elec_woff_pot[start:end], label = 'pot woff')
ax1.plot(elec_woff[start:end],label = 'prod woff')
ax1.plot(elec_ccgt[start:end], label = 'prod ccgt')
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(label)
plt.ylabel('GWh')
plt.xlabel('Hour of the year')
plt.legend()
plt.plot()

#%% Load shedding and load shifting

node = 'LOAD_SHIFTING'
lsf_red = zoom_on_variable_in_cluster_subnode('INLAND','load_reduction',node,'Hour',dictionary_3C)
lsf_inc = zoom_on_variable_in_cluster_subnode('INLAND','load_increase',node,'Hour',dictionary_3C)
lsf_nb_cycle = sum(lsf_red)/abs(get_cluster_element_parameter("INLAND",node,"pre_installed_capacity",dictionary_3C)[0])
lsf_total = sum(lsf_red)

nb_hour = 0
for i in range(0,len(lsf_red)):
    if lsf_red[i] > 0.015 or lsf_inc[i] > 0.015:
        nb_hour += 1
nb_hour_lsf = nb_hour

node = 'LOAD_SHEDDING_1'
lsd1_red = zoom_on_variable_in_cluster_subnode('INLAND','load_reduction',node,'Hour',dictionary_3C)
lsd1_total = sum(lsd1_red)

nb_hour = 0
var = lsd1_red
for i in range(0,len(var)):
    if var[i] > 0.00: 
        nb_hour += 1
nb_hour_lsd1 = nb_hour

node = 'LOAD_SHEDDING_2'
lsd2_red = zoom_on_variable_in_cluster_subnode('INLAND','load_reduction',node,'Hour',dictionary_3C)
lsd2_total = sum(lsd2_red)

nb_hour = 0
var = lsd2_red
for i in range(0,len(var)):
    if var[i] > 0.00000: 
        nb_hour += 1
nb_hour_lsd2 = nb_hour

node = 'LOAD_SHEDDING_4'
lsd4_red = zoom_on_variable_in_cluster_subnode('INLAND','load_reduction',node,'Hour',dictionary_3C)
lsd4_total = sum(lsd4_red)

nb_hour = 0
var = lsd4_red
for i in range(0,len(var)):
    if var[i] > 0.00000: 
        nb_hour += 1
nb_hour_lsd4 = nb_hour

node = 'LOAD_SHEDDING_8'
lsd8_red = zoom_on_variable_in_cluster_subnode('INLAND','load_reduction',node,'Hour',dictionary_3C)
lsd8_total = sum(lsd8_red)

nb_hour = 0
var = lsd8_red
for i in range(0,len(var)):
    if var[i] > 0.00000: 
        nb_hour += 1
nb_hour_lsd8 = nb_hour

node = 'LOAD_SHEDDING_UNLIM'
lsdu_red = zoom_on_variable_in_cluster_subnode('INLAND','load_reduction',node,'Hour',dictionary_3C)
lsdu_total = sum(lsdu_red)

nb_hour = 0
var = lsdu_red
for i in range(0,len(var)):
    if var[i] > 0.000000: 
        nb_hour += 1
nb_hour_lsdu = nb_hour

lsd_total = lsd1_total + lsd2_total + lsd4_total + lsd8_total + lsdu_total

ens_el = zoom_on_variable_in_cluster("INLAND","e_ens",'Hour',dictionary_3C)
ens_total = sum(ens_el)
max_ens_el = max(ens_el)

nb_hour = 0
var = ens_el
for i in range(0,len(var)):
    if var[i] > 0.000000: 
        nb_hour += 1
nb_hour_ens_el = nb_hour


start = 400
end = start + 200
step = 20
x_ticks = [x for x in range(0,end - start,step)]
label = [x for x in range(start,end,step)]

fig, ax1 = plt.subplots()
ax1.plot(lsd1_red[start:end], label = 'lsd1')
ax1.plot(lsd2_red[start:end],label = 'lsd2')
ax1.plot(lsd4_red[start:end], label = 'lsd4')
ax1.plot(lsd8_red[start:end],label = 'lsd8')
ax1.plot(lsdu_red[start:end], label = 'lsdu')
ax1.plot(ens_el[start:end], label = 'ens')
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(label)
plt.legend()
plt.plot()

start = 7* 24 * 5 
end = start + 24*7
step = 24
x_ticks = [x for x in range(0,end - start,step)]
label = [x for x in range(start,end,step)]
fig, ax1 = plt.subplots()

ax1.plot(lsf_inc[start:end], label = 'lsf_inc')
ax1.plot([-x for x in lsf_red[start:end]], label = 'lsf_red')
ax1.plot(elec_won[start:end],label = 'prod won')
ax1.plot(elec_pv[start:end],label = 'prod pv')
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(label)
plt.legend()
plt.plot()

#%% demandes totales

# Hydrogène
zoom = 'Hour'
h2_dem_ind = zoom_on_global_parameter("demand_h2_industry",zoom,dictionary_3C)
h2_dem_ht = zoom_on_global_parameter("demand_h2_heat",zoom,dictionary_3C)
h2_dem_tr = zoom_on_global_parameter("demand_h2_transport",zoom,dictionary_3C)
h2_dem_tr2 = zoom_on_global_parameter("demand_h2_transport2",zoom,dictionary_3C)

h2_dem = [h2_dem_ind,h2_dem_ht,h2_dem_tr,h2_dem_tr2]
h2_dem_total = [0] * len(h2_dem_ind)
for dem in h2_dem:
    h2_dem_total =  [h2_dem_total[i] + dem[i] for i in range(0,len(h2_dem_total))]
    
h2_dem_max = max(h2_dem_total)

# Natural gaz
ng_inl_zb = [-x for x in zoom_on_variable_in_cluster('PIPE_NG_ZB_INL','flow_reverse_in',zoom,dictionary_3C)]
ng_ccgt = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','CCGT',zoom,dictionary_3C)]
ng_ocgt = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','OCGT',zoom,dictionary_3C)]
ng_chp = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','CHP',zoom,dictionary_3C)]
ng_smr = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','ng_consumed','SMR',zoom,dictionary_3C)]
ng_ch = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','NG_STORAGE',zoom,dictionary_3C)]
ng_lp_ch = [-x for x in zoom_on_variable_in_cluster_subnode('INLAND','charged','LINEPACK_NG',zoom,dictionary_3C)]
ng_dem_ind = [-x for x in zoom_on_global_parameter("demand_ng_industry",zoom,dictionary_3C)]
ng_dem_ht = [-x for x in zoom_on_global_parameter("demand_ng_heat",zoom,dictionary_3C)]
ng_dem_tr = [-x for x in zoom_on_global_parameter("demand_ng_transport",zoom,dictionary_3C)]
ng_dem_tr2 = [-x for x in zoom_on_global_parameter("demand_ng_transport2",zoom,dictionary_3C)]

ng_dem = [ng_ccgt,ng_smr,ng_ch,ng_lp_ch,ng_dem_ind,ng_dem_ht,ng_dem_tr,ng_dem_tr2]
ng_dem_total = [0] * len(ng_dem_ind)
for dem in ng_dem:
    ng_dem_total =  [ng_dem_total[i] + dem[i] for i in range(0,len(ng_dem_total))]
    
ng_dem_max = min(ng_dem_total)

#%%
""" Studies interco """

zoom = 'Hour'

elec_off_zb = [-x for x in zoom_on_variable_in_cluster('HV_OFF_ZB','e_forward_in',zoom,dictionary_3C)]
total_elec_off_zb = sum(elec_off_zb)
elec_zb_off = [-x for x in zoom_on_variable_in_cluster('HV_OFF_ZB','e_reverse_in',zoom,dictionary_3C)]
total_elec_zb_off = sum(elec_zb_off)
elec_zb_inl = [-x for x in zoom_on_variable_in_cluster('HV_ZB_INL','e_forward_in',zoom,dictionary_3C)]
total_elec_zb_inl = sum(elec_zb_inl)
elec_inl_zb = [-x for x in zoom_on_variable_in_cluster('HV_ZB_INL','e_reverse_in',zoom,dictionary_3C)]
total_elec_inl_zb = sum(elec_inl_zb)


#%%
""" Curtailment """

curtailment = {}

cluster = 'OFFSHORE'
node = 'WIND_OFFSHORE'
cap_woff = cluster_subnodes_capacities_tot[cluster][node]['Total capacity']
woff_max = [i * cap_woff for i in get_cluster_element_parameter(cluster,node,"production_profile",dictionary_3C)]
woff_real = get_cluster_element_variable(cluster,node,'e_produced',dictionary_3C)['values']
curtailment[node] = [woff_max[i] - woff_real[i] for i in range(0,len(woff_max))]

cluster = 'INLAND'
nodes = ['PV','WIND_ONSHORE']
for node in nodes:
    cap_woff = cluster_subnodes_capacities_tot[cluster][node]['Total capacity']
    woff_max = [i * cap_woff for i in get_cluster_element_parameter(cluster,node,"production_profile",dictionary_3C)]
    woff_real = get_cluster_element_variable(cluster,node,'e_produced',dictionary_3C)['values']
    curtailment[node] = [woff_max[i] - woff_real[i] for i in range(0,len(woff_max))]
    
table_curt = pd.DataFrame(curtailment)
table_curt.to_excel(title + '/' + 'curtailment.xlsx')
    


 
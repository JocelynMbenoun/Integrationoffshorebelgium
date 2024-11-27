# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:56:53 2022

@author: Jocelyn Mbenoun
"""
from bs4 import BeautifulSoup

# diagram
diagram = '3 clusters.svg' # input file for the diagram 
new_diagram = title + '/Diagram 3 clusters.svg' # output file for the diagram

with open(diagram) as fp:
    soup = BeautifulSoup(fp, 'xml')


#% Functions
""" functions """

def line_to_value(ID,soup,text,fontsize):
    tag = soup.find(id=ID)
    tag.name = "text"
    x = tag['x1'] 
    y = tag['y1']
    tag['x'] = x
    tag['y'] = y
    tag['fill'] = 'black'
    tag['font-family'] = 'Arial'
    tag['font-size'] = str(fontsize)
    del tag['x1']
    del tag['y1']
    del tag['x2']
    del tag['y2']
    #del tag['stroke']
    tag.string = text
    type(tag)
    
def line_to_triangle(ID,soup,width,orientation,types):
    tag = soup.find(id=ID)
    tag.name = "polygon"
    x_1 = tag['x1'] 
    y_1 = tag['y1']
    x_2 = tag['x2']
    y_2 = tag['y2']
    color = tag['stroke']
    d = 4
    del tag['x1']
    del tag['y1']
    del tag['x2']
    del tag['y2']
    del tag['stroke']
    type(tag)
    if orientation == 'horizontal':
        if types == 'center':
            p1 = x_1 + ',' + str(float(y_1) - width/2 - d)
            p2 = x_1 + ',' + str(float(y_1) + width/2 + d)
            p3 = x_2 + ',' + y_2
        if types == 'lower':
            p1 = x_1 + ',' + str(float(y_1) - width - d + 1)
            p2 = x_1 + ',' + str(float(y_1) + d)
            p3 = x_2 + ',' + str(float(y_2) - width/2)
        if types == 'upper':
            p1 = x_1 + ',' + str(float(y_1) - d)
            p2 = x_1 + ',' + str(float(y_1) + width + d - 1)
            p3 = x_2 + ',' + str(float(y_2) + width/2)
    if orientation == 'vertical':
        if types == 'center':
            p1 = str(float(x_1) + width/2 + d) + ',' + y_1
            p2 = str(float(x_1) - width/2 - d) + ',' + y_1
            p3 = x_2 + ',' + y_2
        if types == 'lower':
            p1 = str(float(x_1) + width + d - 1) + ',' + y_1
            p2 = str(float(x_1) - d ) + ',' + y_1
            p3 = str(float(x_2) + width/2) +  ',' + y_2
        if types == 'upper':
            p1 = str(float(x_1) - width - d + 1) + ',' + y_1
            p2 = str(float(x_1) + d ) + ',' + y_1
            p3 = str(float(x_2) - width/2) +  ',' + y_2
    tag['points'] = p1 + ' ' + p2 + ' ' + p3
    if width == 0:
        tag['points'] = p1 + ' ' + p1 + ' ' + p1
    tag['style'] = "fill:" + color + ";" + 'stroke:' + color + ';' + 'stroke-width:1'
    

#% Police and units
""" Police and units"""
    
base_case = 0 

if base_case == 1:
    scale = 12000 * dictionary_3C['model']['horizon']/8760 # value by witch the fluxes are divided to determine the width of the lines in the schema

    fontsize_cap = 14
    fontsize_cap_2 = 12
    nb_dec_cap = 1
    
    fontsize_flux_1 = 12
    fontsize_flux_2 = 10
    unit_flux =  " TWh"
    ratio_flux = 1000
    nb_dec_flux = 2
    nb_dec_width = 5
    
    unit_capacity = " GW"
    unit_storage = " GWh"
    ratio_cap = 1
    
    ratio_co2 = 1
    nb_dec_co2 = 1
    unit_co2_cap = " kt"
    unit_co2 = " kt"
    scale_co2 = 1500 * dictionary_3C['model']['horizon']/8760

else:
    scale = 12000 * dictionary_3C['model']['horizon']/8760 # value by witch the fluxes are divided to determine the width of the lines in the schema
    
    fontsize_cap = 22
    fontsize_cap_2 = 16
    nb_dec_cap = 2
    
    fontsize_flux_1 = 20
    fontsize_flux_2 = 20
    unit_flux =  " TWh"
    ratio_flux = 1000
    nb_dec_flux = 2
    nb_dec_width = 5
    
    unit_capacity = " GW"
    unit_storage = " GWh"
    ratio_cap = 1
    
    ratio_co2 = 1000
    nb_dec_co2 = 2
    unit_co2_cap = " kt"
    unit_co2 = " Mt"
    scale_co2 = 1500 * dictionary_3C['model']['horizon']/8760

#% Electricity
""" Electricity """

""" Offshore """

# Woff el

ID = 'Woff cap'
value = cluster_subnodes_capacities_tot['OFFSHORE']['WIND_OFFSHORE']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Woff el value'
value = cluster_subnodes_total_production['OFFSHORE']['WIND_OFFSHORE']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Woff cf'
if cluster_subnodes_capacities_tot['OFFSHORE']['WIND_OFFSHORE']['Total capacity'] > 0:
    value = cluster_subnodes_total_production['OFFSHORE']['WIND_OFFSHORE']['e_produced']/(sum(get_cluster_element_parameter("OFFSHORE","WIND_OFFSHORE","production_profile",dictionary_3C)) * cluster_subnodes_capacities_tot['OFFSHORE']['WIND_OFFSHORE']['Total capacity'])
else:
        value = 0
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Woff el')
width = round(value/scale,nb_dec_width)
tag['width'] = str(width)
type(tag)

tag = soup.find(id='Woff el - EPoff el')
width_tot = width
tag['stroke-width'] = str(width_tot)
type(tag)


# EP el

ID = 'EPoff el value'
value = cluster_subnodes_total_production['OFFSHORE']['ELECTROLYSIS_PLANTS']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='EPoff el - EPoff el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'EPoff el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='EPoff el - FCoff el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)

# Batteries

ID = 'Battoff cape'
value = cluster_subnodes_capacities_tot['OFFSHORE']['BATTERIES power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Battoff caps'
value = cluster_subnodes_capacities_tot['OFFSHORE']['BATTERIES energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# Fuel cells

ID = 'FCoff cap'
value = cluster_subnodes_capacities_tot['OFFSHORE']['FUEL_CELLS']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)


ID = 'FCoff el value'
value = cluster_subnodes_total_production['OFFSHORE']['FUEL_CELLS']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='FCoff el')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='FCoff el - HVDCoff el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)

# Transmission Offshore - Zeebrugge

ID = 'HV_off_zb cap'
value = interconnections['HV_OFF_ZB']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'HVoff out el value'
value = interconnections['HV_OFF_ZB']['total volume in']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'HVzb in el value'
value = interconnections['HV_OFF_ZB']['total volume out']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='HVzb el - Intzb el')
width = round(value/scale,nb_dec_width)
width_tot = width
tag['stroke-width'] = str(width_tot)
type(tag)

""" Zeebrugge """

# Import/export electricity

ID = 'Intzb el cap'
value = interconnections['DENMARK']["el import capacity"] + interconnections['UNITED_KINGDOM']["el import capacity"] 
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Intzb el real cap'
value =  max([get_cluster_variable('DENMARK','imported',dictionary_3C)['values'][i] + get_cluster_variable('UNITED_KINGDOM','imported',dictionary_3C)['values'][i] for i in range(0,dictionary_3C['model']['horizon'])])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Impzb el value'
value_imp = interconnections['DENMARK']["el imported volume"] + interconnections['UNITED_KINGDOM']["el imported volume"] 
text = str(round(abs(value_imp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Impzb el')
width = round(value_imp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Impzb el in'
line_to_triangle(ID,soup,width,'vertical','center')


ID = 'Expzb el value'
value_exp = interconnections['DENMARK']["el exported volume"] + interconnections['UNITED_KINGDOM']["el exported volume"] 
text = str(round(abs(value_exp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Expzb el')
width = round(value_exp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Expzb el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Intzb el - EPzb el')
width = round((value_imp - value_exp)/scale,nb_dec_width)
width_tot = width_tot + width
tag['stroke-width'] = str(width_tot)
type(tag)

# Batteries

ID = 'Battzb cape'
value = cluster_subnodes_capacities_tot['ZEEBRUGGE']['BATTERIES power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Battzb caps'
value = cluster_subnodes_capacities_tot['ZEEBRUGGE']['BATTERIES energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# EP el

ID = 'EPzb el value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='EPzb el - EPzb el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'EPzb el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='EPzb el - DACzb el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)


# DAC el

ID = 'DACzb el value'
value = cluster_subnodes_total_capture_co2['ZEEBRUGGE']['DAC']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DACzb el - DACzb el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'DACzb el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='DACzb el - FCzb el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)

# Fuel cells

ID = 'FCzb cap'
value = cluster_subnodes_capacities_tot['ZEEBRUGGE']['FUEL_CELLS']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)


ID = 'FCzb el value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['FUEL_CELLS']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='FCzb el')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='FCzb el - HVzb out el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)

# Transmission Zeebrugge - Inland

ID = 'HV_zb_inl cap'
value = interconnections['HV_ZB_INL']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'HVzb out el value'
value = interconnections['HV_ZB_INL']['total volume in']
text = str(round(value/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'HVinl in el value'
value = interconnections['HV_ZB_INL']['total volume out']
text = str(round(value/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='HVinl in el - Intinl el')
tag['stroke-width'] = str(width_tot)
type(tag)


""" Inland """

# Import/export electricity

ID = 'Intinl el cap'
value = interconnections['DEUTSCHLAND']["el import capacity"] + interconnections['FRANCE']["el import capacity"] + interconnections['LUXEMBOURG']["el import capacity"] + interconnections['NETHERLANDS']["el import capacity"]
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Intinl el real cap'
value =  max([get_cluster_variable('DEUTSCHLAND','imported',dictionary_3C)['values'][i] + get_cluster_variable('FRANCE','imported',dictionary_3C)['values'][i] + get_cluster_variable('LUXEMBOURG','imported',dictionary_3C)['values'][i] + get_cluster_variable('NETHERLANDS','imported',dictionary_3C)['values'][i] for i in range(0,dictionary_3C['model']['horizon'])])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Impinl el value'
value_imp = interconnections['DEUTSCHLAND']["el imported volume"] + interconnections['FRANCE']["el imported volume"] + interconnections['LUXEMBOURG']["el imported volume"] + interconnections['NETHERLANDS']["el imported volume"]
text = str(round(abs(value_imp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Impinl el')
width = round(value_imp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Impinl el in'
line_to_triangle(ID,soup,width,'vertical','center')


ID = 'Expinl el value'
value_exp = interconnections['DEUTSCHLAND']["el exported volume"] + interconnections['FRANCE']["el exported volume"] + interconnections['LUXEMBOURG']["el exported volume"] + interconnections['NETHERLANDS']["el exported volume"]
text = str(round(abs(value_exp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Expinl el')
width = round(value_exp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Expinl el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Intinl el - Renew NK el')
width = round((value_imp - value_exp)/scale,nb_dec_width)
width_tot = width_tot + width
tag['stroke-width'] = str(width_tot)
type(tag)

# PV el

ID = 'PV cap'
value = cluster_subnodes_capacities_tot['INLAND']['PV']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'PV cf'
if cluster_subnodes_capacities_tot['INLAND']['PV']['Total capacity'] > 0:
    value = round(cluster_subnodes_total_production['INLAND']['PV']['e_produced'],2)/(sum(get_cluster_element_parameter("INLAND","PV","production_profile",dictionary_3C)) * cluster_subnodes_capacities_tot['INLAND']['PV']['Total capacity'])
else:
    value = 0
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'PV el value'
value = cluster_subnodes_total_production['INLAND']['PV']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)


tag = soup.find(id='PV el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='PV el - Won el')
width_renew = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width_renew)
type(tag)

# Won el

ID = 'Won cap'
value = cluster_subnodes_capacities_tot['INLAND']['WIND_ONSHORE']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Won cf'
value = cluster_subnodes_total_production['INLAND']['WIND_ONSHORE']['e_produced']/(sum(get_cluster_element_parameter("INLAND","WIND_ONSHORE","production_profile",dictionary_3C)) * cluster_subnodes_capacities_tot['INLAND']['WIND_ONSHORE']['Total capacity'])
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Won el value'
value = cluster_subnodes_total_production['INLAND']['WIND_ONSHORE']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Won el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='Won el - NK el')
width_renew = width + width_renew
tag['stroke-width'] = str(width_renew)
type(tag)

# NK el

ID = 'NK cap'
value = cluster_subnodes_capacities_tot['INLAND']['NUCLEAR']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'NK cf'
if cluster_subnodes_capacities_tot['INLAND']['NUCLEAR']['Total capacity'] == 0:
    value = 0
else:
    value = round(cluster_subnodes_total_production['INLAND']['NUCLEAR']['e_produced'],1)/(dictionary_3C['model']['horizon'] * cluster_subnodes_capacities_tot['INLAND']['NUCLEAR']['Total capacity'])
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'NK el value'
value = cluster_subnodes_total_production['INLAND']['NUCLEAR']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='NK el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

tag = soup.find(id='Renew NK el')
width_renew = width + width_renew
tag['stroke-width'] = str(width_renew)
type(tag)

ID = 'Renew NK el out'
line_to_triangle(ID,soup,width_renew,'vertical','center')

ID = 'Renew NK total el'
value = cluster_subnodes_total_production['INLAND']['PV']['e_produced'] + cluster_subnodes_total_production['INLAND']['WIND_ONSHORE']['e_produced'] + cluster_subnodes_total_production['INLAND']['NUCLEAR']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id="NRenew - NDisp el")
width_tot = width_tot + width_renew
tag['stroke-width'] = str(width_tot)
type(tag)

# Pumped Hydro

ID = 'PH cape'
value = cluster_subnodes_capacities_tot['INLAND']['PUMPED_HYDRO power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'PH caps'
value = cluster_subnodes_capacities_tot['INLAND']['PUMPED_HYDRO energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# Batteries

ID = 'Batt cape'
value = cluster_subnodes_capacities_tot['INLAND']['BATTERIES power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Batt caps'
value = cluster_subnodes_capacities_tot['INLAND']['BATTERIES energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# AFC el 

ID = 'AFC cap'
value = 0
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'AFC el value'
value = 0
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='AFC el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='AFC el - CHP el')
width_disp = width
tag['stroke-width'] = str(width)
type(tag)

# CHP el

ID = 'CHP cap'
value = cluster_subnodes_capacities_tot['INLAND']['CHP']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'CHP el value'
value = cluster_subnodes_total_production['INLAND']['CHP']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux))
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='CHP el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='CHP el - BM el')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# BM el

ID = 'BM cap'
value = cluster_subnodes_capacities_tot['INLAND']['BIOMASS']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'BM el value'
value = cluster_subnodes_total_production['INLAND']['BIOMASS']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='BM el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='BM el - OCGT el')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# OCGT el

ID = 'OCGT cap'
value = cluster_subnodes_capacities_tot['INLAND']['OCGT']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'OCGT el value'
value = cluster_subnodes_total_production['INLAND']['OCGT']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='OCGT el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='OCGT el - WS el')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# WS el

ID = 'WS cap'
value = cluster_subnodes_capacities_tot['INLAND']['WASTE']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'WS el value'
value = cluster_subnodes_total_production['INLAND']['WASTE']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='WS el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)


tag = soup.find(id='WS el - CCGT el')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# CCGT el

ID = 'CCGT cap'
value = cluster_subnodes_capacities_tot['INLAND']['CCGT']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'CCGT cf'
if cluster_subnodes_capacities_tot['INLAND']['CCGT']['Total capacity'] == 0:
    value = 0
else:
    value = round(cluster_subnodes_total_production['INLAND']['CCGT']['e_produced'],1)/(dictionary_3C['model']['horizon'] * cluster_subnodes_capacities_tot['INLAND']['CCGT']['Total capacity'])
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'CCGT el value'
value = cluster_subnodes_total_production['INLAND']['CCGT']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='CCGT el')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

tag = soup.find(id='CCGT el - NDisp el out')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

ID = 'NDisp el out'
line_to_triangle(ID,soup,width,'vertical','center')

# Dispactchable - FC

ID = 'Disp total el'
value = cluster_subnodes_total_production['INLAND']['CHP']['e_produced'] + cluster_subnodes_total_production['INLAND']['BIOMASS']['e_produced'] + cluster_subnodes_total_production['INLAND']['OCGT']['e_produced'] + cluster_subnodes_total_production['INLAND']['WASTE']['e_produced'] + cluster_subnodes_total_production['INLAND']['CCGT']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id="NDisp el - FC el")
width_tot = width_renew + width_disp
tag['stroke-width'] = str(width_tot)
type(tag)

# FC el

ID = 'FC cap'
value = cluster_subnodes_capacities_tot['INLAND']['FUEL_CELLS']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'FC el value'
value = cluster_subnodes_total_production['INLAND']['FUEL_CELLS']['e_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='FC el - FC el out')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)


ID = 'FC el out'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='FC el - EP el')
width_tot = width + width_tot
tag['stroke-width'] = str(width_tot)
type(tag)

# EP el

ID = 'EP el value'
value = cluster_subnodes_total_production['INLAND']['ELECTROLYSIS_PLANTS']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='EP el - EP el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'EP el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='EP el - PCCC el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)

# PCCC el

ID = 'PCCC el value'
value = cluster_subnodes_total_capture_co2['INLAND']['PCCC_SMR']['e_consumed'] +  cluster_subnodes_total_capture_co2['INLAND']['PCCC_OCGT']['e_consumed'] + cluster_subnodes_total_capture_co2['INLAND']['PCCC_CCGT']['e_consumed'] + cluster_subnodes_total_capture_co2['INLAND']['PCCC_CHP']['e_consumed'] + cluster_subnodes_total_capture_co2['INLAND']['PCCC_BM']['e_consumed'] + cluster_subnodes_total_capture_co2['INLAND']['PCCC_WS']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='PCCC el - PCCC el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'PCCC el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='PCCC el - SMR el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag)

# SMR el

ID = 'SMR el value'
value = cluster_subnodes_total_production['INLAND']['SMR']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='SMR el - SMR el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'SMR el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='SMR el - DAC el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag) 

# DAC el

ID = 'DAC el value'
value = cluster_subnodes_total_capture_co2['INLAND']['DAC']['e_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DAC el - DAC el in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'DAC el in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='DAC el - NDem/Exp el')
width_tot = width_tot - width
tag['stroke-width'] = str(width_tot)
type(tag) 

# Demand el

ID = 'Dem el value'
value = sum(total_el_demand[i]['Total value'] for i in total_el_demand) - total_cluster_ens['INLAND']['e_ens']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Dem el in'
line_to_triangle(ID,soup,width_tot,'horizontal','center')

ID = 'ENS el'
value = total_cluster_ens['INLAND']['e_ens']
if value > 0 and value < 10**(-nb_dec_flux) * ratio_flux:
    text = 'ENS < 0.1' + unit_flux
else:
    text = 'ENS: ' + str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)



""" Natural gas """


""" Zeebrugge """

# Regas

ID = 'Regaszb ch4 cap'
value = interconnections['REGAS_GREEN']['import capacity'] 
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Regaszb ch4 value'
value = interconnections['REGAS']['imported'] + interconnections['REGAS_GREEN']['imported']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Regaszb ch4')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Regaszb in ch4'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Regaszb ch4 - Intzb ch4')
width_ch4 = width
tag['stroke-width'] = str(width_ch4)
type(tag)

ID = 'Regaszb co2 capt'
value_capt = cluster_subnodes_total_capture_co2['ZEEBRUGGE']['REGAS_GREEN']['co2_captured'] 
text = str(round(abs(value_capt)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

# Imports/exports

ID = 'Intzb ch4 cap'
value = interconnections['NG_INTERCONNECTION_NV']['import capacity'] + interconnections['NG_INTERCONNECTION_UK']['import capacity'] + interconnections['NG_INTERCONNECTION_FR']['import capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Intzb ch4 real cap'
value =  max([get_cluster_element_variable('ZEEBRUGGE','NG_INTERCONNECTION_NV','imported',dictionary_3C)['values'][i] + get_cluster_element_variable('ZEEBRUGGE','NG_INTERCONNECTION_UK','imported',dictionary_3C)['values'][i] + get_cluster_element_variable('ZEEBRUGGE','NG_INTERCONNECTION_FR','imported',dictionary_3C)['values'][i] for i in range(0,dictionary_3C['model']['horizon'])])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Impzb ch4 value'
value_imp = interconnections['NG_INTERCONNECTION_NV']['imported'] + interconnections['NG_INTERCONNECTION_UK']['imported'] + interconnections['NG_INTERCONNECTION_FR']['imported']
text = str(round(abs(value_imp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Impzb ch4')
width = round(value_imp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Impzb ch4 in'
line_to_triangle(ID,soup,width,'vertical','center')


ID = 'Expzb ch4 value'
value_exp = interconnections['NG_INTERCONNECTION_NV']['exported'] + interconnections['NG_INTERCONNECTION_UK']['exported']
text = str(round(abs(value_exp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Expzb ch4')
width = round(value_exp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Expzb ch4 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Intzb ch4 - MTzb ch4')
width = round((value_imp - value_exp)/scale,nb_dec_width)
width_ch4 = width_ch4 + width
tag['stroke-width'] = str(width_ch4)
type(tag)

# Methanation 

ID = 'MTzb cap'
value = cluster_subnodes_capacities_tot['ZEEBRUGGE']['METHANATION']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'MTzb ch4 value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['METHANATION']['ng_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='MTzb ch4')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='MTzb ch4 - Pipezb ch4')
width_ch4 = width_ch4 + width
tag['stroke-width'] = str(width_ch4)
type(tag)

# Pipe Zeebrugge - Inland

ID = 'Pipezb out ch4 value'
value = interconnections['PIPE_NG_ZB_INL']['total volume in']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Pipech4_zb_inl cap'
value = interconnections['PIPE_NG_ZB_INL']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)


ID = 'Pipeinl in ch4 value'
value = interconnections['PIPE_NG_ZB_INL']['total volume out']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Pipeinl ch4 - Intinl ch4')
tag['stroke-width'] = str(width_ch4)
type(tag)

# Imports/exports

ID = 'Intinl ch4 cap'
value = interconnections['NG_INTERCONNECTION_NL']['import capacity'] + interconnections['NG_INTERCONNECTION_DE']['import capacity'] 
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Intinl ch4 real cap'
value =  max([get_cluster_element_variable('INLAND','NG_INTERCONNECTION_NL','imported',dictionary_3C)['values'][i] + get_cluster_element_variable('INLAND','NG_INTERCONNECTION_DE','imported',dictionary_3C)['values'][i] for i in range(0,dictionary_3C['model']['horizon'])])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Impinl ch4 value'
value_imp = interconnections['NG_INTERCONNECTION_NL']['imported'] + interconnections['NG_INTERCONNECTION_DE']['imported']
text = str(round(abs(value_imp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Impinl ch4')
width = round(value_imp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Impinl ch4 in'
line_to_triangle(ID,soup,width,'vertical','center')

ID = 'Expinl ch4 value'
value_exp = interconnections['NG_INTERCONNECTION_NL']['exported'] + interconnections['NG_INTERCONNECTION_DE']['exported'] + interconnections['NG_INTERCONNECTION_FR']['exported'] 
text = str(round(abs(value_exp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Expinl ch4')
width = round(value_exp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Expinl ch4 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='NImp - MT CH4')
width = round((value_imp - value_exp)/scale,nb_dec_width)
width_ch4 = width_ch4 + width
tag['stroke-width'] = str(width_ch4)
type(tag)

# Stockage CH4

ID = 'Sto CH4 cape'
value = cluster_subnodes_capacities_tot['INLAND']['NG_STORAGE power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Sto CH4 caps'
value = cluster_subnodes_capacities_tot['INLAND']['NG_STORAGE energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# Methanation CH4

ID = 'MT CH4 cap'
value = cluster_subnodes_capacities_tot['INLAND']['METHANATION']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'MT CH4 value'
value = cluster_subnodes_total_production['INLAND']['METHANATION']['ng_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='MT - MT CH4 out')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'MT CH4 out'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='MT - NDips CH4')
width_ch4 = width + width_ch4
tag['stroke-width'] = str(width_ch4)
type(tag)

# AFC CH4

ID = 'AFC CH4 value'
value = 0
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='AFC CH4')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

ID = 'AFC CH4 in'
line_to_triangle(ID,soup,width,'horizontal','upper')

tag = soup.find(id='AFC - CHP CH4')
width_disp = width
tag['stroke-width'] = str(width)
type(tag)


# CHP CH4

ID = 'CHP CH4 value'
value = cluster_subnodes_total_production['INLAND']['CHP']['ng_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='CHP CH4')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

ID = 'CHP CH4 in'
line_to_triangle(ID,soup,width,'horizontal','upper')

tag = soup.find(id='CHP - OCGT CH4')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# OCGT CH4

ID = 'OCGT CH4 value'
value = cluster_subnodes_total_production['INLAND']['OCGT']['ng_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='OCGT CH4')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

ID = 'OCGT CH4 in'
line_to_triangle(ID,soup,width,'horizontal','upper')

tag = soup.find(id='OCGT - CCGT CH4')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# CCGT CH4

ID = 'CCGT CH4 value'
value = cluster_subnodes_total_production['INLAND']['CCGT']['ng_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) 
line_to_value(ID,soup,text,fontsize_flux_2)

tag = soup.find(id='CCGT CH4')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

ID = 'CCGT CH4 in'
line_to_triangle(ID,soup,width,'horizontal','upper')

tag = soup.find(id='NDisp - CCGT CH4')
width_disp = width + width_disp
tag['stroke-width'] = str(width_disp)
type(tag)

# Dispactchable - Bio CH4

ID = 'Disp total ch4'
value = cluster_subnodes_total_production['INLAND']['CHP']['ng_consumed'] + cluster_subnodes_total_production['INLAND']['BIOMASS']['ng_consumed'] + cluster_subnodes_total_production['INLAND']['OCGT']['ng_consumed'] + cluster_subnodes_total_production['INLAND']['WASTE']['ng_consumed'] + cluster_subnodes_total_production['INLAND']['CCGT']['ng_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id="NDisp - Bio CH4")
width_ch4 = width_ch4 - width_disp
tag['stroke-width'] = str(width_ch4)
type(tag)

# Linepack CH4

ID = 'Lp CH4 cape'
value = get_cluster_element_parameter('INLAND','LINEPACK_NG','duration_ratio',dictionary_3C)[0] * get_cluster_element_parameter('INLAND','LINEPACK_NG','pre_installed_capacity',dictionary_3C)[0]
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Lp CH4 caps'
value = get_cluster_element_parameter('INLAND','LINEPACK_NG','pre_installed_capacity',dictionary_3C)[0]
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# Biomethane CH4

ID = 'Bio cap'
value = cluster_subnodes_capacities_tot['INLAND']['BIOMETHANE']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Bio co2 capt'
value = cluster_subnodes_total_production['INLAND']['BIOMETHANE']['co2_captured']
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Bio ch4 value'
value = cluster_subnodes_total_production['INLAND']['BIOMETHANE']['ng_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Bio ch4')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Bio ch4 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Bio ch4 - SMR ch4')
width_ch4 = width + width_ch4
tag['stroke-width'] = str(width_ch4)
type(tag)

# SMR CH4

ID = 'SMR CH4 value'
value = cluster_subnodes_total_production['INLAND']['SMR']['ng_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='SMR - SMR CH4 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'SMR CH4 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='SMR - DAC CH4')
width_ch4 = width_ch4 - width
tag['stroke-width'] = str(width_ch4)
type(tag)

# DAC CH4

ID = 'DAC CH4 value'
value = cluster_subnodes_total_capture_co2['INLAND']['DAC']['ng_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DAC - DAC CH4 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'DAC CH4 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='DAC - Dem ch4')
width_ch4 = width_ch4 - width
tag['stroke-width'] = str(width_ch4)
type(tag)

# Demand CH4

ID = 'Dem CH4 value'
value = sum(total_ng_demand[i]['Total value'] for i in total_ng_demand) - total_cluster_ens['INLAND']['ng_ens']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Dem CH4 in'
line_to_triangle(ID,soup,width_ch4,'horizontal','center')

ID = 'ENS CH4'
value = total_cluster_ens['INLAND']['ng_ens']
if value > 0 and value < 10**(-nb_dec_flux) * ratio_flux:
    text = 'ENS < 0.1' + unit_flux
else:
    text = 'ENS: ' + str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

""" Hydrogen """

""" Offshore """

# Electrolysis 

ID = 'EPoff cap'
value = cluster_subnodes_capacities_tot['OFFSHORE']['ELECTROLYSIS_PLANTS']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'EPoff cf'
if cluster_subnodes_capacities_tot['OFFSHORE']['ELECTROLYSIS_PLANTS']['Total capacity'] == 0:
    value = 0
else:
    value = round(cluster_subnodes_total_production['OFFSHORE']['ELECTROLYSIS_PLANTS']['h2_produced'],1)/(dictionary_3C['model']['horizon'] * cluster_subnodes_capacities_tot['OFFSHORE']['ELECTROLYSIS_PLANTS']['Total capacity'])
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'EPoff h2 value'
value = cluster_subnodes_total_production['OFFSHORE']['ELECTROLYSIS_PLANTS']['h2_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='EPoff h2')
width = round(value/scale,nb_dec_width)
width_h2 = width
tag['width'] = str(width)
type(tag)

tag = soup.find(id='EPoff h2 - FCoff h2')
tag['stroke-width'] = str(width_h2)
type(tag)

# FC

ID = 'FCoff h2 value'
value = cluster_subnodes_total_production['OFFSHORE']['FUEL_CELLS']['h2_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='FCoff h2 - FCoff h2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'FCoff h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='FCoff h2 - Pipeoff h2')
width_h2 = width_h2 - width
tag['stroke-width'] = str(width_h2)
type(tag)

# Transmission Offshore - Zeebrugge

ID = 'Pipeoff h2 value'
value = interconnections['PIPE_H2_OFF_ZB']['total volume in']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Pipeh2_off_zb cap'
value = interconnections['PIPE_H2_OFF_ZB']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = "Pipezb in h2 value"
value = interconnections['PIPE_H2_OFF_ZB']['total volume out']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Pipezb h2 - Regaszb h2')
width_h2 = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width_h2)
type(tag)

""" Zeebrugge """


# Regas 

ID = 'Regaszb h2 cap'
value = interconnections['REGAS_H2']['import capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Regaszb h2 value'
value = interconnections['REGAS_H2']['imported']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Regaszb h2')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='Regaszb h2 - Intzb h2')
width_h2 = width_h2 + width
tag['stroke-width'] = str(width_h2)
type(tag)

# H2 interconnection

ID = 'Intzb h2 cap'
value = interconnections['H2_INTERCONNECTION_FR']['import capacity'] + interconnections['H2_INTERCONNECTION_UK']['import capacity'] + interconnections['H2_INTERCONNECTION_NV']['import capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Impzb h2 value'
value_imp = interconnections['H2_INTERCONNECTION_FR']['imported'] + interconnections['H2_INTERCONNECTION_UK']['imported'] + interconnections['H2_INTERCONNECTION_NV']['imported']
text = str(round(abs(value_imp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Impzb h2')
width = round(value_imp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Impzb h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

ID = 'Expzb h2 value'
value_exp = interconnections['H2_INTERCONNECTION_FR']['exported'] + interconnections['H2_INTERCONNECTION_UK']['exported']
text = str(round(abs(value_exp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Expzb h2')
width = round(value_exp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Expzb h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Intzb h2 - EPzb h2')
width = round((value_imp - value_exp)/scale,nb_dec_width)
width_h2 = width_h2 + width
tag['stroke-width'] = str(width_h2)
type(tag)

# Electrolysis

ID = 'EPzb cap'
value = cluster_subnodes_capacities_tot['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'EPzb cf'
if cluster_subnodes_capacities_tot['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['Total capacity'] == 0:
    value = 0
else:
    value = round(cluster_subnodes_total_production['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['h2_produced'],1)/(dictionary_3C['model']['horizon'] * cluster_subnodes_capacities_tot['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['Total capacity'])
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'EPzb h2 value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['ELECTROLYSIS_PLANTS']['h2_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='EPzb h2')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='EPzb h2 - DACzb h2')
width_h2 = width_h2 + width
tag['stroke-width'] = str(width_h2)
type(tag)

# DAC 

ID = 'DACzb h2 value'
value = cluster_subnodes_total_capture_co2['ZEEBRUGGE']['DAC']['h2_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DACzb h2 - DACzb h2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'DACzb h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='DACzb h2 - FCzb h2')
width_h2 = width_h2 - width
tag['stroke-width'] = str(width_h2)
type(tag)

# Fuel-Cells

ID = 'FCzb h2 value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['FUEL_CELLS']['h2_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='FCzb h2 - FCzb h2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'FCzb h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='FCzb h2 - MTzb h2')
width_h2 = width_h2 - width
tag['stroke-width'] = str(width_h2)

# Methanation

ID = 'MTzb h2 value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['METHANATION']['h2_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='MTzb h2 - MTzb h2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'MTzb h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='MTzb h2 - Pipezb h2')
width_h2 = width_h2 - width
tag['stroke-width'] = str(width_h2)
type(tag)


# Transmission Zeebrugge - Inland

ID = "Pipezb out h2 value"
value = interconnections['PIPE_H2_ZB_INL']['total volume in']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Pipeh2_zb_inl cap'
value = interconnections['PIPE_H2_ZB_INL']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = "Pipeinl in h2 value"
value = interconnections['PIPE_H2_ZB_INL']['total volume out']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Pipeinl h2 - MT h2')
tag['stroke-width'] = str(width_h2)
type(tag)

""" Inland """

# Stockage H2

ID = 'H2 sto cape'
value = cluster_subnodes_capacities_tot['INLAND']['H2_STORAGE power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'H2 sto real cape'
value = max(get_cluster_element_variable('INLAND','H2_STORAGE','discharged',dictionary_3C)['values'])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)


ID = 'H2 sto caps'
value = cluster_subnodes_capacities_tot['INLAND']['H2_STORAGE energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_storage + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# H2 interconnection

ID = 'Intinl h2 cap'
value = interconnections['H2_INTERCONNECTION_NL']['import capacity'] + interconnections['H2_INTERCONNECTION_DE']['import capacity'] 
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Intinl h2 real cap'
value =  max([get_cluster_element_variable('INLAND','H2_INTERCONNECTION_NL','imported',dictionary_3C)['values'][i] + get_cluster_element_variable('INLAND','H2_INTERCONNECTION_DE','imported',dictionary_3C)['values'][i] for i in range(0,dictionary_3C['model']['horizon'])])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Impinl h2 value'
value_imp = interconnections['H2_INTERCONNECTION_NL']['imported'] + interconnections['H2_INTERCONNECTION_DE']['imported'] 
text = str(round(abs(value_imp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Impinl h2')
width = round(value_imp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Impinl h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

ID = 'Expinl h2 value'
value_exp = interconnections['H2_INTERCONNECTION_NL']['exported'] + interconnections['H2_INTERCONNECTION_DE']['exported']
text = str(round(abs(value_exp)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Expinl h2')
width = round(value_exp/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'Expinl h2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='Intinl h2 - MTinl h2')
width = round((value_imp - value_exp)/scale,nb_dec_width)
width_h2 = width_h2 + width
tag['stroke-width'] = str(width_h2)
type(tag) 

# Methanation H2

ID = 'MT H2 value'
value = cluster_subnodes_total_production['INLAND']['METHANATION']['h2_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='MT - MT H2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'MT H2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='MT - FC H2')
width_h2 = width_h2 - width
tag['stroke-width'] = str(width_h2)
type(tag)

# Fuel cells H2

ID = 'FC H2 value'
value = cluster_subnodes_total_production['INLAND']['FUEL_CELLS']['h2_consumed']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='FC - FC H2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'FC H2 in'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='FC - EP H2')
width_h2 = width_h2 - width
tag['stroke-width'] = str(width_h2)
type(tag)


# Electrolysis H2

ID = 'EP cap'
value = cluster_subnodes_capacities_tot['INLAND']['ELECTROLYSIS_PLANTS']['Total capacity']
text = str(round(abs(value)/ratio_cap,1)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'EP cf'
if cluster_subnodes_capacities_tot['INLAND']['ELECTROLYSIS_PLANTS']['Total capacity'] == 0:
    value = 0
else:
    value = round(cluster_subnodes_total_production['INLAND']['ELECTROLYSIS_PLANTS']['h2_produced'],1)/(dictionary_3C['model']['horizon'] * cluster_subnodes_capacities_tot['INLAND']['ELECTROLYSIS_PLANTS']['Total capacity'])
text = str(round(value * 100,nb_dec_flux)) + ' %'
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'EP H2 value'
value = cluster_subnodes_total_production['INLAND']['ELECTROLYSIS_PLANTS']['h2_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='EP - EP H2 out')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'EP H2 out'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='EP - SMR H2')
width_h2 = width_h2 + width
tag['stroke-width'] = str(width_h2)
type(tag)

# SMR H2

ID = 'SMR cap'
value = cluster_subnodes_capacities_tot['INLAND']['SMR']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_capacity
line_to_value(ID,soup,text,fontsize_cap)

ID = 'SMR H2 value'
value = cluster_subnodes_total_production['INLAND']['SMR']['h2_produced']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='SMR - SMR H2 out')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'SMR H2 out'
line_to_triangle(ID,soup,width,'vertical','center')

tag = soup.find(id='SMR - NDem/Exp H2')
width_h2 = width_h2 + width
tag['stroke-width'] = str(width_h2)
type(tag)

# Demand H2

ID = 'Dem H2 value'
value = sum(total_h2_demand[i]['Total value'] for i in total_h2_demand) - total_cluster_ens['INLAND']['h2_ens']
text = str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'Dem H2 in'
line_to_triangle(ID,soup,width,'horizontal','center')

ID = 'ENS H2'
value = total_cluster_ens['INLAND']['h2_ens']
if value > 0 and value < 10**(-nb_dec_flux) * ratio_flux:
    text = 'ENS < ' + str(10**(-nb_dec_flux)) + ' ' + unit_flux
else:
    text = 'ENS: ' + str(round(abs(value)/ratio_flux,nb_dec_flux)) + unit_flux
line_to_value(ID,soup,text,fontsize_flux_1)


""" Carbon dioxide """


""" Zeebrugge """

# DAC

ID = 'DACzb cap'
value = cluster_subnodes_capacities_tot['ZEEBRUGGE']['DAC']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_co2)) + unit_co2_cap + '/h'
line_to_value(ID,soup,text,fontsize_cap)

ID = 'DACzb co2 value'
value = cluster_subnodes_total_capture_co2['ZEEBRUGGE']['DAC']['co2_captured']
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DACzb co2')
width = round(value/scale,nb_dec_width)
width_co2 = width
tag['height'] = str(width)
type(tag)

# Methanation

ID = 'MTzb co2 value'
value = cluster_subnodes_total_production['ZEEBRUGGE']['METHANATION']['co2_consumed']
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DACzb co2 - MTzb co2 in')
width = round(value/scale,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'MTzb co2 in'
line_to_triangle(ID,soup,width,'vertical','center')

# Zeebrugge - Inland

ID = 'zb co2 value'
value = sum(get_cluster_variable('ZEEBRUGGE','co2_balanced',dictionary_3C)['values'])
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='zb co2 - inl co2 1')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)

tag = soup.find(id='zb co2 - inl co2 2')
width = round(value/scale,nb_dec_width)
tag['height'] = str(width)
type(tag)



""" Inland """

# Dispatchable to PCCC and CO2 released

ID = 'Disp CO2 value'
Disp = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_WS']
value = sum(cluster_subnodes_total_capture_co2['INLAND'][i]['co2_captured'] + cluster_subnodes_total_capture_co2['INLAND'][i]['co2_released'] for i in Disp)
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Disp - PCCC CO2')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'PCCC Disp CO2 value'
Disp = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_WS']
value = sum(cluster_subnodes_total_capture_co2['INLAND'][i]['co2_captured'] for i in Disp)
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='PCCC - PCCC Disp CO2 in')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='Disp - PCCC CO2')
x = tag['x2']
x = float(x) + width/2 - 0.5
tag['x2'] = str(x)

ID = 'PCCC Disp CO2 in'
line_to_triangle(ID,soup,width,'vertical','center')

ID = 'CO2 released disp value'
Disp = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_WS']
value = sum(cluster_subnodes_total_capture_co2['INLAND'][i]['co2_released'] for i in Disp)
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='PCCC - CO2 released')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'CO2 released in 1'
line_to_triangle(ID,soup,width,'horizontal','center')

# CO2 captured from SMR

ID = 'SMR CO2 captured value'
value = cluster_subnodes_total_capture_co2['INLAND']['PCCC_SMR']['co2_captured'] 
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)


tag = soup.find(id='SMR - PCCC CO2 1')
width = round(value/scale_co2,nb_dec_width)
tag['height'] = str(width)
type(tag)

tag = soup.find(id='SMR - PCCC CO2 2')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'SMR CO2 in'
line_to_triangle(ID,soup,width,'vertical','center')

# PCCC CO2 captured

ID = 'PCCC cap'
Disp = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_WS','PCCC_SMR'] 
value = sum(cluster_subnodes_capacities_tot['INLAND'][i]['Total capacity'] for i in Disp)
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_co2_cap + "/h"
line_to_value(ID,soup,text,fontsize_cap)

ID = 'PCCC CO2 value'
Disp = ['PCCC_BM','PCCC_CCGT','PCCC_CHP','PCCC_OCGT','PCCC_WS','PCCC_SMR'] 
value = sum(cluster_subnodes_total_capture_co2['INLAND'][i]['co2_captured'] for i in Disp)
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='PCCC - DAC CO2')
width = round(value/scale_co2,nb_dec_width)
width_co2 = width
tag['stroke-width'] = str(width)
type(tag)

# DAC CO2

ID = 'DAC cap' 
value = cluster_subnodes_capacities_tot['INLAND']['DAC']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_co2)) + unit_co2_cap + '/h'
line_to_value(ID,soup,text,fontsize_cap)

ID = 'DAC co2 capt' 
value = cluster_subnodes_total_capture_co2['INLAND']['DAC']['co2_captured'] 
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

ID = 'DAC CO2 value' 
value = cluster_subnodes_total_capture_co2['INLAND']['DAC']['co2_exiting'] 
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='DAC - DAC CO2 out')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='DAC - MT CO2')
x = tag['x1']
x = float(x) - width/2 + 0.5
tag['x1'] = str(x)

tag = soup.find(id='DAC - MT CO2')
width_co2 = width_co2 + width
tag['stroke-width'] = str(width_co2)
type(tag)

# MT CO2

ID = 'MT CO2 value' 
value = cluster_subnodes_total_production['INLAND']['METHANATION']['co2_consumed'] 
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='MT - MT CO2 in 3')
width = round(value/scale_co2,nb_dec_width)
tag['width'] = str(width)
type(tag)

ID = 'MT CO2 in'
line_to_triangle(ID,soup,width,'vertical','center')

# MT + Zeebrugge CO2

tag = soup.find(id='MT - MT CO2 in 1')
value = sum(get_cluster_variable('ZEEBRUGGE','co2_balanced',dictionary_3C)['values']) - value
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

tag = soup.find(id='MT - MT CO2 in 2')
width = round(value/scale_co2,nb_dec_width)
tag['height'] = str(width)
type(tag)


# CO2 storage

ID = 'CO2 sto cape'
value = cluster_subnodes_capacities_tot['INLAND']['CO2_STORAGE power']['Total capacity']
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_co2_cap + "/h"
line_to_value(ID,soup,text,fontsize_cap)

ID = 'CO2 sto caps'
value = cluster_subnodes_capacities_tot['INLAND']['CO2_STORAGE energy']['Total capacity']
text = "(" + str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_co2_cap + ")"
line_to_value(ID,soup,text,fontsize_cap_2)

# Export CO2

ID = 'Exp CO2 cap'
value = get_cluster_element_parameter('INLAND','CO2_EXPORT','export_capacity',dictionary_3C)[0]
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_co2_cap + "/h"
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Exp CO2 real cap'
value = max(get_cluster_element_variable('INLAND','CO2_EXPORT','exported',dictionary_3C)['values'])
text = str(round(abs(value)/ratio_cap,nb_dec_cap)) + unit_co2_cap + "/h"
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Exp CO2 value'
value = get_total_value_of_variables_in_cluster_subnodes(['exported'],'INLAND',['CO2_EXPORT'],dictionary_3C)['CO2_EXPORT']['exported']
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='MT - Exp CO2')
width_co2 = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width_co2)
type(tag)

ID = 'Exp CO2 in'
width = round(value/scale_co2,nb_dec_width)
line_to_triangle(ID,soup,width,'horizontal','center')

# SMR CO2 released

ID = 'SMR CO2 released value'
value = cluster_subnodes_total_capture_co2['INLAND']['PCCC_SMR']['co2_released'] 
value_co2_smr = value
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)


tag = soup.find(id='SMR - Exp CO2 1')
width = round(value/scale_co2,nb_dec_width)
tag['height'] = str(width)
type(tag)

tag = soup.find(id='SMR - Exp CO2 2')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

# CO2 from CH4 demand

ID = 'Dem CH4 CO2 value'
spec_co2_emission = dictionary_3C['model']['global_parameters']['spec_co2_emission'][0]
demand_ch4 = sum(total_ng_demand[i]['Total value'] for i in total_ng_demand) - total_cluster_ens['INLAND']['ng_ens']
value = spec_co2_emission * demand_ch4
value_co2_ch4 = value
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='Dem - Dem CH4 CO2 out')
width = round(value/scale_co2,nb_dec_width)
tag['height'] = str(width)
type(tag)

# CO2 released

ID = 'CO2 released value'
value = value_co2_smr + value_co2_ch4
text = str(round(abs(value)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_flux_1)

tag = soup.find(id='CO2 - CO2 released in')
width = round(value/scale_co2,nb_dec_width)
tag['stroke-width'] = str(width)
type(tag)

ID = 'CO2 released in'
line_to_triangle(ID,soup,width,'vertical','center')

ID = 'Total co2 captured'
value_capt = cluster_subnodes_total_capture_co2['INLAND']['DAC']['co2_captured'] + cluster_subnodes_total_production['INLAND']['BIOMETHANE']['co2_captured'] + get_cluster_variable('ZEEBRUGGE','total_co2_captured',dictionary_3C)['values'][0]
text = "co2 captured :" + str(round(abs(value_capt)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_cap)

ID = 'Total co2 released'
value_rele = value_co2_ch4 + sum(cluster_subnodes_total_capture_co2['INLAND'][i]['co2_released'] for i in Disp)
text = "co2 released :" + str(round(abs(value_rele)/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_cap)

ID = 'co2 balance'
value = value_rele - value_capt
text = "co2 balance :" + str(round(value/ratio_co2,nb_dec_co2)) + unit_co2
line_to_value(ID,soup,text,fontsize_cap)

""" Costs """

ID = 'Total_cost'
value = total_cost
text = "Total cost: " + str(round(value/ratio_cap,nb_dec_cap)) + " MEur"
line_to_value(ID,soup,text,24)

ID = 'COE'
value = cost_of_energy * 1000
text = "COE: " + str(round(value/ratio_cap,nb_dec_cap)) + " Eur/MWh"
line_to_value(ID,soup,text,24)

# cleaning

""" Suppression 0 sur le schéma """

tags = soup.find_all(text = '0.0 TWh')
for tag in tags:
    tag.parent.string = ''
    

tags = soup.find_all(text = '0.0 kt')
for tag in tags:
    tag.parent.string = ''
    
tags = soup.find_all(text = '0.0 Mt')
for tag in tags:
    tag.parent.string = ''
    
""" Agrandissement lignes de petites épaisseurs """

tags = soup.find_all('line')

for tag in tags:
    if tag.has_attr('stroke-width'):
        if float(tag['stroke-width']) > 0 and float(tag['stroke-width']) < 1 :
            tag['stroke-width'] = 1
       
tags = soup.find_all('rect')

for tag in tags:
    if float(tag['height']) > 0 and float(tag['height']) < 1 :
        tag['height'] = 1
    if float(tag['width']) > 0 and float(tag['width']) < 1 :
        tag['width'] = 1
# save of the new diagram

with open(new_diagram,'w') as file:
    file.write(str(soup))


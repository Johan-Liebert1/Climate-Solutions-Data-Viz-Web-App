import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
sns.set_palette("dark")
sns.set_style("whitegrid")

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
dataset_url=https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions
import opendatasets as od
od.download(dataset_url)
data_dir = '/'
emission_table = pd.read_csv("/kaggle/input/international-greenhouse-gas-emissions/greenhouse_gas_inventory_data_data.csv")   #Change thisss

def prep():
    pd.set_option('display.max_colwidth', -1)
    by_category  = emission_table.groupby(['category'])
    category_count = by_category.count()

def algo():
    new_category_index = []
    for string in strp:
        p = len(string)
        pos = string.find("_in_kilotonne_co2_equivalent",0,p)
        string = string[:pos]
        new_category_index.append(string)
    new_category_index_reborn = []
    for lingo in new_category_index:
        q = len(lingo)
        pos = lingo.find("_without",0,p)
        lingo = lingo[:pos]
        new_category_index_reborn.append(lingo)
    short_category = ["co2","ghg(indirect co2)","ghg","hfc","ch4","nf3","n2o","pfc","sf6","hfc+pfc"]
    category_count["Shorted_category"] = short_category

def clean():
    trying_emission = emission_table
    replaced_emission = trying_emission.replace(to_replace=["carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_"
                                     "forestry_lulucf_in_kilotonne_co2_equivalent","greenhouse_gas_ghgs_emissions_including_indirect_co2"
                                    "_without_lulucf_in_kilotonne_co2_equivalent","greenhouse_gas_ghgs_emissions_without_land_use_land_use"
                                    "_change_and_forestry_lulucf_in_kilotonne_co2_equivalent","hydrofluorocarbons_hfcs_emissions_in_kilotonne_co2_equivalent",
                                    "methane_ch4_emissions_without_land_use_land_use_change"
                                    "_and_forestry_lulucf_in_kilotonne_co2_equivalent","nitrogen_trifluoride_nf3_emissions_in_kilotonne_co2_equivalent",
                                    "nitrous_oxide_n2o_emissions_without_land_use_land_use_change" 
                                    "_and_forestry_lulucf_in_kilotonne_co2_equivalent","perfluorocarbons_pfcs_emissions_in_kilotonne_co2_equivalent",
                                    "sulphur_hexafluoride_sf6_emissions_in_kilotonne_co2_equivalent",
                                    "unspecified_mix_of_hydrofluorocarbons_hfcs_and_perfluorocarbons"
                                    "_pfcs_emissions_in_kilotonne_co2_equivalent"], value = ["CO2","GHG(Indirect CO2)","GHG","HFC","CH4","NF3","N2O","PFC","SF6","HFC+PFC"])
    loct = replaced_emission.groupby(['category'])['value'].sum()
    replaced_emission['Total Emitted Gas'] = replaced_emission['value'].groupby(replaced_emission['category']).transform('sum')
    new_dataframe_emission = pd.DataFrame(loct.index)
    new_dataframe_emission["Total Amount Emitted(In Kilotones)"] = loct.values

table = pd.pivot_table(emission_table, values='value', index=['country_or_area', 'year'], columns=['category'])
def tableplot():
    '''Plots the contents of the table of data created in our Prepatory steps'''
    fig=table.plot()
    return fig
gasnames = table.columns.values
def country_plot(nameOfCountry):
    data = table.loc[nameOfCountry]
    plt.plot(data)
    plt.legend(gasnames,title='title', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(nameOfCountry)
def gascount():
    plt.figure(figsize=(15,7))
    ax = sns.countplot(replaced_emission["category"])
    ax.set_xticklabels(ax.get_xticklabels(),rotation=40, ha="right", fontsize=14)
    plt.tight_layout()
    plt.xlabel("Gas category",fontsize=16)
    plt.ylabel("Count",fontsize=16)
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.show()
    return gascount
    #Calculating the Total amount of gases emitted
def data():
    data_div = pd.pivot_table(replaced_emission,values="value",index = ["country_or_area", "year"],columns = ["category"])
    data_div.plot()
gases = data_div.columns.values
# lets define a function that can plot the country data 
def plot_the_country(name):
    find = data_div.loc[name]
    plt.plot(find)
    plt.title(name)
    plt.legend(gases)
    plt.tick_params(labelsize=12)
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.xlim(2000,2014)
def compare_plot():
    area_div = pd.pivot_table(replaced_emission, values='value', index=['category', 'year'], columns=['country_or_area'])
    print(area_div)
    sns.heatmap(area_div)
countries = area_div.columns.values
def country_wise_plot(name):
    ''' Individual COuntry wise pollutors'''
    cname = area_div.loc[name]
    plt.plot(cname)
    plt.tick_params(labelsize=14)
    plt.legend(countries, loc = "center left",bbox_to_anchor=(1, 0.5),fontsize = 18,ncol = 3)
    plt.rcParams["figure.figsize"] = [15, 10]
#Comparing Countries By Passing Required Series
def gas_accord_country1(gas_name, country_name):                          # years from 1990-2004
    data = area_div.loc[gas_name]
    data.plot( y = country_name)
    plt.legend(country_name,loc = "center left",bbox_to_anchor=(1, 0.5),fontsize = 18,ncol = 2)
    plt.tick_params(labelsize=14)
    plt.xlabel("Year",fontsize=14)
    plt.xlim(1990,2004)
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.title(gas_name)
    
    
def gas_accord_country2(gas_name, country_name):
    data = area_div.loc[gas_name]
    data.plot( y = country_name)
    plt.legend(country_name,loc = "center left",bbox_to_anchor=(1, 0.5),fontsize = 18,ncol = 2)
    plt.tick_params(labelsize=14)
    plt.xlabel("Year",fontsize=14)
    plt.xlim(2004,2017)
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.title(gas_name)
#Cleaning the GHG & GHG(Indirect CO2) column
def clean_data():
    data_div["GHG"].plot()
    cleaned_data = data_div
    cleaned_data["Check"] = cleaned_data["GHG"] - cleaned_data["GHG(Indirect CO2)"]

nf3_data = cleaned_data[cleaned_data["NF3"].isnull()==False].reset_index()
nf3_countries = nf3_data.groupby("country_or_area").count().index
#gas_accord_country1(gases[7],nf3_countries)

#Checking Gas Emissions in a country
#Let's define a function, that can check for the plot WRT the country name passed.
def check_country(name):
    clean_new_table.plot(x = 'category', y = name)
    plt.tick_params(labelsize=14)
    plt.xlabel("Category Of GreenHouse Gases",fontsize=14)
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.legend(fontsize = 20)
def tabulation_new(name):
    point = clean_new_table[name].sum()
    data_storage = clean_new_table[['category',name]]
    data_storage['Percent'] = (data_storage[name]/point * 100)
    print(data_storage)
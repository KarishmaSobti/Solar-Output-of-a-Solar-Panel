import pandas as pd
import numpy as np
import requests
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns



print("DAILY ENERGY OUTPUT FROM SOLAR PANEL")
number=int(input("Enter the number of solar panels you have installed="))

wattage_str=input("Enter the panel wattage of one solar panel(in Watt) =")
wattage_cleanstr1=wattage_str.replace('W','')
wattage_cleanstr2=wattage_cleanstr1.replace('w','')
wattage=float(wattage_cleanstr2)

efficiency_str=input("Enter your solar panel efficiency (in percentage)=")
efficiency_cleanstr=efficiency_str.replace('%' , '')
efficiency=float(efficiency_cleanstr)

sunhours=float(input("Enter the number of sunhours a day="))

energyoutput=(number*(wattage*sunhours*(efficiency/100)))/1000
print("your daily solar energy output in kW is= ", energyoutput, "kW")
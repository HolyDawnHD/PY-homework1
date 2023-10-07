import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from openpyxl.workbook import Workbook


def main():

    drinks=pd.read_csv('../PY-homework1-main/drinks.csv',keep_default_na=False)


###获取各大洲简称###
    # print(drinks.drop_duplicates(subset='continent'))

###啤酒的平均消耗量###
    AS_beer=drinks[drinks.continent=='AS'].describe().at['mean','beer_servings']
    EU_beer=drinks[drinks.continent=='EU'].describe().at['mean','beer_servings']
    AF_beer=drinks[drinks.continent=='AF'].describe().at['mean','beer_servings']
    NA_beer=drinks[drinks.continent=='NA'].describe().at['mean','beer_servings']
    SA_beer=drinks[drinks.continent=='SA'].describe().at['mean','beer_servings']
    OC_beer=drinks[drinks.continent=='OC'].describe().at['mean','beer_servings']

###以柱状图形式体现###
    categories = ['AS', 'EU', 'AF', 'NA','SA','OC']
    values = [AS_beer, EU_beer, AF_beer, NA_beer,SA_beer,OC_beer]

    plt.bar(categories, values, color='blue', alpha=0.6)

    plt.title('drinks')
    plt.xlabel('continent')
    plt.ylabel('beer_servings_mean')

    plt.show()
    print('由数据可知，欧洲（EU）平均消耗的啤酒最多，为：%0.6f\n'%EU_beer)

###结果以beer_data.txt文件形式输出###
    f=open("beer_data.txt",'w')
    f.write('由数据可知，欧洲（EU）平均消耗的啤酒最多，为：%0.6f\n'%EU_beer)
    f.close()

###红酒的描述性统计值###
    print("****************************wine*****************************\n")
    s_AS=drinks[drinks.continent=='AS'].describe().loc[:,'wine_servings']
    print('AS:\n',s_AS,'\n')
    s_EU=drinks[drinks.continent=='EU'].describe().loc[:,'wine_servings']
    print('EU:\n',s_EU,'\n')
    s_AF=drinks[drinks.continent=='AF'].describe().loc[:,'wine_servings']
    print('AF:\n',s_AF,'\n')
    s_NA=drinks[drinks.continent=='NA'].describe().loc[:,'wine_servings']
    print('NA:\n',s_NA,'\n')
    s_SA=drinks[drinks.continent=='SA'].describe().loc[:,'wine_servings']
    print('SA:\n',s_SA,'\n')
    s_OC=drinks[drinks.continent=='OC'].describe().loc[:,'wine_servings']
    print('OC:\n',s_OC,'\n')

###结果保存在wine_data.csv中###
    df=pd.DataFrame({'AS wine':s_AS,'EU wine':s_EU,'AF wine':s_AF,'NA wine':s_NA,'SA wine':s_SA,'OC wine':s_OC})
    df.to_csv('wine_data.csv', index=True)
    # df.to_excel('wine_data.xlsx', index=True)

###每个大洲每种酒消耗量###
    print("**************************每个大洲每种酒消耗平均值*************************\n")
    print("AS")
    print("beer_mean:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['mean',"beer_servings"])
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['mean',"spirit_servings"])
    print("wine_mean:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['mean',"wine_servings"])
    print("EU")
    print("beer_mean:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['mean',"beer_servings"])
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['mean',"spirit_servings"])
    print("wine_mean:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['mean',"wine_servings"])
    print("AF")
    print("beer_mean:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['mean',"beer_servings"])
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['mean',"spirit_servings"])
    print("wine_mean:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['mean',"wine_servings"])
    print("NA")
    print("beer_mean:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['mean',"beer_servings"])
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['mean',"spirit_servings"])
    print("wine_mean:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['mean',"wine_servings"])
    print("SA")
    print("beer_mean:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['mean',"beer_servings"])
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['mean',"spirit_servings"])
    print("wine_mean:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['mean',"wine_servings"])
    print("OC")
    print("beer_mean:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['mean',"beer_servings"])
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['mean',"spirit_servings"])
    print("wine_mean:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['mean',"wine_servings"])

    f=open("mean_data.txt",'w')
    f.write("AS\n")
    f.write("beer_mean:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['mean',"beer_servings"])
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['mean',"spirit_servings"])
    f.write("wine_mean:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['mean',"wine_servings"])
    f.write("EU\n")
    f.write("beer_mean:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['mean',"beer_servings"])
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['mean',"spirit_servings"])
    f.write("wine_mean:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['mean',"wine_servings"])
    f.write("AF\n")
    f.write("beer_mean:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['mean',"beer_servings"])
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['mean',"spirit_servings"])
    f.write("wine_mean:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['mean',"wine_servings"])
    f.write("NA\n")
    f.write("beer_mean:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['mean',"beer_servings"])
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['mean',"spirit_servings"])
    f.write("wine_mean:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['mean',"wine_servings"])
    f.write("SA\n")
    f.write("beer_mean:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['mean',"beer_servings"])
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['mean',"spirit_servings"])
    f.write("wine_mean:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['mean',"wine_servings"])
    f.write("OC\n")
    f.write("beer_mean:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['mean',"beer_servings"])
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['mean',"spirit_servings"])
    f.write("wine_mean:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['mean',"wine_servings"])
    f.close()

    print("**************************每个大洲每种酒消耗中位数*************************\n")
    print("AS")
    print("beer_middle:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['50%',"beer_servings"])
    print("spirit_middle:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['50%',"spirit_servings"])
    print("wine_middle:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['50%',"wine_servings"])
    print("EU")
    print("beer_middle:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['50%',"beer_servings"])
    print("spirit_middle:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['50%',"spirit_servings"])
    print("wine_middle:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['50%',"wine_servings"])
    print("AF")
    print("beer_middle:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['50%',"beer_servings"])
    print("spirit_middle:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['50%',"spirit_servings"])
    print("wine_middle:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['50%',"wine_servings"])
    print("NA")
    print("beer_middle:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['50%',"beer_servings"])
    print("spirit_middle:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['50%',"spirit_servings"])
    print("wine_middle:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['50%',"wine_servings"])
    print("SA")
    print("beer_middle:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['50%',"beer_servings"])
    print("spirit_middle:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['50%',"spirit_servings"])
    print("wine_middle:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['50%',"wine_servings"])
    print("OC")
    print("beer_middle:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['50%',"beer_servings"])
    print("spirit_middle:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['50%',"spirit_servings"])
    print("wine_middle:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['50%',"wine_servings"])

    f=open("middle_data.txt",'w')
    f.write("AS\n")
    f.write("beer_middle:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['50%',"beer_servings"])
    f.write("spirit_middle:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['50%',"spirit_servings"])
    f.write("wine_middle:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['50%',"wine_servings"])
    f.write("EU\n")
    f.write("beer_middle:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['50%',"beer_servings"])
    f.write("spirit_middle:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['50%',"spirit_servings"])
    f.write("wine_middle:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['50%',"wine_servings"])
    f.write("AF\n")
    f.write("beer_middle:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['50%',"beer_servings"])
    f.write("spirit_middle:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['50%',"spirit_servings"])
    f.write("wine_middle:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['50%',"wine_servings"])
    f.write("NA\n")
    f.write("beer_middle:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['50%',"beer_servings"])
    f.write("spirit_middle:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['50%',"spirit_servings"])
    f.write("wine_middle:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['50%',"wine_servings"])
    f.write("SA\n")
    f.write("beer_middle:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['50%',"beer_servings"])
    f.write("spirit_middle:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['50%',"spirit_servings"])
    f.write("wine_middle:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['50%',"wine_servings"])
    f.write("OC\n")
    f.write("beer_middle:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['50%',"beer_servings"])
    f.write("spirit_middle:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['50%',"spirit_servings"])
    f.write("wine_middle:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['50%',"wine_servings"])
    f.close()

    print("**************************每个大洲spirit的平均值、最大、最小值*************************\n")
    print("AS")
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['mean',"spirit_servings"])
    print("spirit_max:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['max',"spirit_servings"])
    print("spirit_min:%0.6f"%drinks[drinks.continent=='AS'].describe().loc['min',"spirit_servings"])
    print("EU")
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['mean',"spirit_servings"])
    print("spirit_max:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['max',"spirit_servings"])
    print("spirit_min:%0.6f"%drinks[drinks.continent=='EU'].describe().loc['min',"spirit_servings"])
    print("AF")
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['mean',"spirit_servings"])
    print("spirit_max:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['max',"spirit_servings"])
    print("spirit_min:%0.6f"%drinks[drinks.continent=='AF'].describe().loc['min',"spirit_servings"])
    print("NA")
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['mean',"spirit_servings"])
    print("spirit_max:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['max',"spirit_servings"])
    print("spirit_min:%0.6f"%drinks[drinks.continent=='NA'].describe().loc['min',"spirit_servings"])
    print("SA")
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['mean',"spirit_servings"])
    print("spirit_max:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['max',"spirit_servings"])
    print("spirit_min:%0.6f"%drinks[drinks.continent=='SA'].describe().loc['min',"spirit_servings"])
    print("OC")
    print("spirit_mean:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['mean',"spirit_servings"])
    print("spirit_max:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['max',"spirit_servings"])
    print("spirit_min:%0.6f"%drinks[drinks.continent=='OC'].describe().loc['min',"spirit_servings"])
    
    f=open("spirit_data.txt","w")
    f.write("AS\n")
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['mean',"spirit_servings"])
    f.write("spirit_max:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['max',"spirit_servings"])
    f.write("spirit_min:%0.6f\n"%drinks[drinks.continent=='AS'].describe().loc['min',"spirit_servings"])
    f.write("EU\n")
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['mean',"spirit_servings"])
    f.write("spirit_max:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['max',"spirit_servings"])
    f.write("spirit_min:%0.6f\n"%drinks[drinks.continent=='EU'].describe().loc['min',"spirit_servings"])
    f.write("AF\n")
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['mean',"spirit_servings"])
    f.write("spirit_max:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['max',"spirit_servings"])
    f.write("spirit_min:%0.6f\n"%drinks[drinks.continent=='AF'].describe().loc['min',"spirit_servings"])
    f.write("NA\n")
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['mean',"spirit_servings"])
    f.write("spirit_max:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['max',"spirit_servings"])
    f.write("spirit_min:%0.6f\n"%drinks[drinks.continent=='NA'].describe().loc['min',"spirit_servings"])
    f.write("SA\n")
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['mean',"spirit_servings"])
    f.write("spirit_max:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['max',"spirit_servings"])
    f.write("spirit_min:%0.6f\n"%drinks[drinks.continent=='SA'].describe().loc['min',"spirit_servings"])
    f.write("OC\n")
    f.write("spirit_mean:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['mean',"spirit_servings"])
    f.write("spirit_max:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['max',"spirit_servings"])
    f.write("spirit_min:%0.6f\n"%drinks[drinks.continent=='OC'].describe().loc['min',"spirit_servings"])
    f.close()




if __name__ == '__main__':
    main()
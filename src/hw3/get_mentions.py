import pandas as pd
import argparse
import os.path as osp
import json
import sys

canonical_ponys=['twilight','applejack','rarity','pinkie','rainbow','fluttershy']
ponys_fullname=['Twilight Sparkle', 'Applejack','Rarity', 'Pinkie Pie', 'Rainbow Dash','Fluttershy']
full_to_can={'Twilight Sparkle':'twilight','Applejack':'applejack','Rarity':'rarity','Pinkie Pie':'pinkie','Rainbow Dash':'rainbow','Fluttershy':'fluttershy'}
mention_igcase={'applejack':r'A(p|P)(p|P)(l|L)(e|E)(j|J)(a|A)(c|C)(k|K)','rarity':r'R(a|A)(r|R)(i|I)(t|T)(y|Y)','fluttershy':r'F(l|L)(u|U)(t|T)(t|T)(e|E)(r|R)(s|S)(h|H)(y|Y)'}


def get_mentions(df):
        import re
        ment={}
        for i in range(6):
                one_pony = df[(df['pony']).str.lower() == (ponys_fullname[i]).lower()] # get dialog for one pony
                ment_one={}
                acc=0
                namelist_for_i=canonical_ponys.copy()
                namelist_for_i.pop(i)
                ment_one=dict.fromkeys(namelist_for_i, 0)
                for key in namelist_for_i:#count number 
                #if u == i:
                #       continue;
                        if key == 'twilight':
                                num1=one_pony.apply(lambda row: len(re.findall(r'T(w|W)(i|I)(l|L)(i|I)(g|G)(h|H)(t|T)',str(row['dialog']))),axis=1).sum()
                                #num1=one_pony[one_pony['dialog'].str.contains(r'T(w|W)(i|I)(l|L)(i|I)(g|G)(h|H)(t|T)',regex=True)==True].shape[0]
                                num2=one_pony.apply(lambda row: len(re.findall(r'S(p|P)(a|A)(r|R)(k|K)(l|L)(e|E)',str(row['dialog']))),axis=1).sum()
                                #num2=one_pony[one_pony['dialog'].str.contains(r'S(p|P)(a|A)(r|R)(k|K)(l|L)(e|E)',regex=True)==True].shape[0]
                                num3=one_pony.apply(lambda row: len(re.findall(r'T(w|W)(i|I)(l|L)(i|I)(g|G)(h|H)(t|T) S(p|P)(a|A)(r|R)(k|K)(l|L)(e|E)',str(row['dialog']))),axis=1).sum()
                                #num3=one_pony[one_pony['dialog'].str.contains(r'T(w|W)(i|I)(l|L)(i|I)(g|G)(h|H)(t|T) S(p|P)(a|A)(r|R)(k|K)(l|L)(e|E)',regex=True)==True].shape[0]
                                ment_one[key]=num1+num2-num3
                                acc=acc+ment_one[key]
                        elif key == 'pinkie':
                                num1=one_pony.apply(lambda row: len(re.findall(r"P(i|I)(n|N)(k|K)(i|I)(e|E)",str(row['dialog']))),axis=1).sum()
                                #num1=one_pony[one_pony['dialog'].str.contains(r"P(i|I)(n|N)(k|K)(i|I)(e|E)",regex=True)==True].shape[0]
                                num2=one_pony.apply(lambda row: len(re.findall(r'P(i|I)(e|E)',str(row['dialog']))),axis=1).sum()
                                #num2=one_pony[one_pony['dialog'].str.contains(r'P(i|I)(e|E)', regex=True)==True].shape[0]
                                num3=one_pony.apply(lambda row: len(re.findall(r"P(i|I)(n|N)(k|K)(i|I)(e|E) P(i|I)(e|E)",str(row['dialog']))),axis=1).sum()
                                #num3=one_pony[one_pony['dialog'].str.contains(r"P(i|I)(n|N)(k|K)(i|I)(e|E) P(i|I)(e|E)",regex=True)==True].shape[0]
                                ment_one[key]=num1+num2-num3
                                acc=acc+ment_one[key]
                        elif key == 'rainbow':
                                num1=one_pony.apply(lambda row: len(re.findall(r'R(a|A)(i|I)(n|N)(b|B)(o|O)(w|W)',str(row['dialog']))),axis=1).sum()
                                #num1=one_pony[one_pony['dialog'].str.contains(r'R(a|A)(i|I)(n|N)(b|B)(o|O)(w|W)', regex=True)==True].shape[0]
                                num2=one_pony.apply(lambda row: len(re.findall(r'D(a|A)(s|S)(h|H)',str(row['dialog']))),axis=1).sum()
                                #num2=one_pony[one_pony['dialog'].str.contains(r'D(a|A)(s|S)(h|H)',regex=True)==True].shape[0]
                                num3=one_pony.apply(lambda row: len(re.findall(r'R(a|A)(i|I)(n|N)(b|B)(o|O)(w|W) D(a|A)(s|S)(h|H)',str(row['dialog']))),axis=1).sum()
                                #num3=one_pony[one_pony['dialog'].str.contains(r'R(a|A)(i|I)(n|N)(b|B)(o|O)(w|W) D(a|A)(s|S)(h|H)',regex=True)==True].shape[0]                          
                                ment_one[key]=num1+num2-num3
                                acc=acc+ment_one[key]
                        #ment_one[canonical_ponys[u]] = one_pony[one_pony['dialog'].str.contains(ponys_fullname[u])].shape[0]                   
                        else:
                                ment_one[key]=one_pony.apply(lambda row: len(re.findall(mention_igcase[key],str(row['dialog']))),axis=1).sum()
                                #ment_one[key]=one_pony[one_pony['dialog'].str.contains(ponys_fullname[canonical_ponys.index(key)])].shape[0]
                                acc=acc+ment_one[key]
                for w in range (6): #calculate percent                  
                        if w == i :
                                continue
                        ment_one[canonical_ponys[w]]= round((ment_one[canonical_ponys[w]] / acc),2)
                ment[canonical_ponys[i]]= ment_one
        return ment


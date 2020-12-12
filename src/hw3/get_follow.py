import pandas as pd
import argparse
import os.path as osp
import json
import sys

canonical_ponys=['twilight','applejack','rarity','pinkie','rainbow','fluttershy']
ponys_fullname=['Twilight Sparkle', 'Applejack','Rarity', 'Pinkie Pie', 'Rainbow Dash','Fluttershy']
full_to_can={'Twilight Sparkle':'twilight','Applejack':'applejack','Rarity':'rarity','Pinkie Pie':'pinkie','Rainbow Dash':'rainbow','Fluttershy':'fluttershy'}
mention_igcase={'applejack':r'A(p|P)(p|P)(l|L)(e|E)(j|J)(a|A)(c|C)(k|K)','rarity':r'R(a|A)(r|R)(i|I)(t|T)(y|Y)','fluttershy':r'F(l|L)(u|U)(t|T)(t|T)(e|E)(r|R)(s|S)(h|H)(y|Y)'}

def get_follow(df):
        foll={}
        for i in range(6):
                new_dict=canonical_ponys.copy()
                new_dict.pop(i)

                new_fullname=ponys_fullname.copy()
                new_fullname.pop(i)
                one_pony = df
                one_pony[canonical_ponys[i]]=(df['pony']).str.lower() == (ponys_fullname[i]).lower() # add new feature
                #initailize the dict for one pony
                foll_one=dict.fromkeys(new_dict, 0)
                foll_one['other']=0
                for u in range(one_pony.shape[0]):
                        if one_pony.loc[u][4+i] == False:
                                continue
                        else:
                                if one_pony.loc[u-1][2] in new_fullname:
                                        #index= new_fullname.index(one_pony.loc[u-1][2])
                                        foll_one[full_to_can[one_pony.loc[u-1][2]]] += 1
                                elif one_pony.loc[u-1][2] != ponys_fullname[i]:
                                        foll_one['other'] += 1
                #tot=df[(df['pony']).str.lower() == (ponys_fullname[i]).lower()].shape[0]
                tot=sum(foll_one.values())
                for key in foll_one:
                        foll_one[key]=round ((foll_one[key]/tot),2)

                foll[canonical_ponys[i]]=foll_one
        return foll

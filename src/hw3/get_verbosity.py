import pandas as pd
import argparse
import os.path as osp 
import json
import sys 

canonical_ponys=['twilight','applejack','rarity','pinkie','rainbow','fluttershy']
ponys_fullname=['Twilight Sparkle', 'Applejack','Rarity', 'Pinkie Pie', 'Rainbow Dash','Fluttershy']

def get_verbosity(df):
        verb={}
        total = 0 
        for i in range(6):
                df_for_one = df[(df['pony']).str.lower() == (ponys_fullname[i]).lower()]
                indx=-1
                counter=0
                prev_title=None
                for index, row in df_for_one.iterrows():
                        if index != (indx+1):
                                counter+=1
                                #indx=index
    
                        elif row['title'] != prev_title:
                                counter+=1
                                #indx=index
                                #continue
                        indx=index
                        prev_title=row['title']  
                total=total+counter
                verb[canonical_ponys[i]] = counter
    
        for i in range(6):
                verb[canonical_ponys[i]] = round ((verb[canonical_ponys[i]] / total),2)
        return verb

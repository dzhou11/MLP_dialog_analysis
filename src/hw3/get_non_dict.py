import pandas as pd
import argparse
import os.path as osp
import json
import sys

script_dir = osp.dirname(__file__)

canonical_ponys=['twilight','applejack','rarity','pinkie','rainbow','fluttershy']
ponys_fullname=['Twilight Sparkle', 'Applejack','Rarity', 'Pinkie Pie', 'Rainbow Dash','Fluttershy']
full_to_can={'Twilight Sparkle':'twilight','Applejack':'applejack','Rarity':'rarity','Pinkie Pie':'pinkie','Rainbow Dash':'rainbow','Fluttershy':'fluttershy'}
mention_igcase={'applejack':r'A(p|P)(p|P)(l|L)(e|E)(j|J)(a|A)(c|C)(k|K)','rarity':r'R(a|A)(r|R)(i|I)(t|T)(y|Y)','fluttershy':r'F(l|L)(u|U)(t|T)(t|T)(e|E)(r|R)(s|S)(h|H)(y|Y)'}


def get_non_dict(df):
        import re
        import itertools
        non_dict={}
        parser = argparse.ArgumentParser()
        alpha_path = osp.join(script_dir, '..', '..', 'data', 'words_alpha.txt')
        with open (alpha_path , "r") as diction:    #need change
                in_dict= diction.readlines()
        diction.close()
        #in_dict= [s.replace("/<U+[0-9]{4}/>","") for s in in_dict]

        in_dict = [x.strip() for x in in_dict]
        #diction.close()

        in_dict=set(in_dict)
        for i in range (6):
                one_pony_said={}

                temp= df[df[canonical_ponys[i]]==True]

                out = ' '.join(temp["dialog"].astype(str))
                out=re.sub("\<U\+[0-9]{4}\>"," ",out)
                words=re.sub("[^\w]", " ",out).split()

                for u in words:
                        l=u.lower()
                        if l not in in_dict:
                                if l not in one_pony_said:
                                        one_pony_said[l]=1
                                else:
                                        one_pony_said[l]=one_pony_said[l]+1
                one_pony_said={k: v for k, v in sorted(one_pony_said.items(), key=lambda item: item[1],reverse=True)}
                one_pony_said=dict(itertools.islice(one_pony_said.items(), 5))
                non_dict[canonical_ponys[i]]=list(one_pony_said.keys())
        return non_dict

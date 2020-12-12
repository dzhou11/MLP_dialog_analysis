"""
anaylsis on my little pony
"""

import pandas as pd
import argparse
import os.path as osp
import json
import sys
#print(sys.path)
from hw3.get_verbosity import *
from hw3.get_mentions import *
from hw3.get_follow import *
from hw3.get_non_dict import *

script_dir = osp.dirname(__file__)

canonical_ponys=['twilight','applejack','rarity','pinkie','rainbow','fluttershy']
ponys_fullname=['Twilight Sparkle', 'Applejack','Rarity', 'Pinkie Pie', 'Rainbow Dash','Fluttershy']
full_to_can={'Twilight Sparkle':'twilight','Applejack':'applejack','Rarity':'rarity','Pinkie Pie':'pinkie','Rainbow Dash':'rainbow','Fluttershy':'fluttershy'}
mention_igcase={'applejack':r'A(p|P)(p|P)(l|L)(e|E)(j|J)(a|A)(c|C)(k|K)','rarity':r'R(a|A)(r|R)(i|I)(t|T)(y|Y)','fluttershy':r'F(l|L)(u|U)(t|T)(t|T)(e|E)(r|R)(s|S)(h|H)(y|Y)'}

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('src_file', help='File path of the dataset.')
	parser.add_argument('-o', help='The file name of output.')
	if len(sys.argv)==1:
		parser.print_help(sys.stderr)
		sys.exit(1)

	
	#change the path to the argument
	#src_file = osp.join(script_dir, '..', 'data', 'clean_dialog.csv')
	args=parser.parse_args()
	#print(args)
	src_file=args.src_file
	
	filename=args.o	
	#print(filename)
	#return	


	df=pd.read_csv(src_file)
	out={}
	out["verbosity"]=get_verbosity(df)
	out["mentions"]=get_mentions(df)
	out["follow_on_comments"]=get_follow(df)
	out["non_dictionary_words"]=get_non_dict(df)
	json_out=json.dumps(out,indent=4)
	if filename != None:
		with open(filename,'w')as out:
			out.write(json_out)
	
	return json_out
	
	#print(json_out)	
	#print(df.head())
	#print("--------------------")
	#get_verbosity(df)
	#print(get_follow(df))
	#print("--------------------")
	#print(get_verbosity(df))
	#print("--------------------")
	#print(get_mentions(df))
	#print("--------------------")
	#print(get_non_dict(df))
if __name__ == '__main__':
	main()

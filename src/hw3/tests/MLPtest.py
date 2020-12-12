import unittest
#from ..MLP_functions import *
from ..get_verbosity import *
from ..get_mentions import *
from ..get_follow import *
from ..get_non_dict import *

import pandas as pd                                                                               
import argparse                                                                                     
import os.path as osp                                                                              
import json                                                                                          
import sys 

script_dir = osp.dirname(__file__)
parser = argparse.ArgumentParser()
data_path=osp.join(script_dir,'..','..','..','data', 'clean_dialog.csv')
alpha_path = osp.join(script_dir, '..','..','..','data', 'words_alpha.txt')
df=pd.read_csv(data_path)
ponys_fullname=['Twilight Sparkle', 'Applejack','Rarity', 'Pinkie Pie', 'Rainbow Dash','Fluttershy']
canonical_ponys=['twilight','applejack','rarity','pinkie','rainbow','fluttershy']
full_to_can={'Twilight Sparkle':'twilight','Applejack':'applejack','Rarity':'rarity','Pinkie Pie':'pinkie','Rainbow Dash':'rainbow','Fluttershy':'fluttershy'}
mention_igcase={'applejack':r'A(p|P)(p|P)(l|L)(e|E)(j|J)(a|A)(c|C)(k|K)','rarity':r'R(a|A)(r|R)(i|I)(t|T)(y|Y)','fluttershy':r'F(l|L)(u|U)(t|T)(t|T)(e|E)(r|R)(s|S)(h|H)(y|Y)'}

class MLPTestCase(unittest.TestCase):

	def test_verbosity_format(self):
		values = get_verbosity(df)
		num_of_member=len(values)
		self.assertEqual(num_of_member,6)

	def test_mentions_format_1(self):
	        values = get_mentions(df)
	        num_of_member=len(values)
	        self.assertEqual(num_of_member,6) 

	def test_mentions_format_2(self):
	        values = get_mentions(df)
	        num_of_member=len(values["twilight"])
	        self.assertEqual(num_of_member,5) 

	def test_follow_format_1(self):
	        values = get_follow(df)
	        num_of_member=len(values)
	        self.assertEqual(num_of_member,6)

	def test_follow_format_2(self):
	        values = get_follow(df)
	        num_of_member=len(values["twilight"])
	        self.assertEqual(num_of_member,6)  

	def test_non_dict_format_2(self):
	        values = get_non_dict(df)
	        num_of_member=len(values["twilight"])
	        self.assertEqual(num_of_member,5)

	def test_non_dict_format_1(self):
	        values = get_non_dict(df)
	        num_of_member=len(values)
	        self.assertEqual(num_of_member,6) 

	def test_verbosity_value(self):
		out=get_verbosity(df)
		result=True
		for key in out:
			if out[key]>=1:
				result=False
				break
		self.assertEqual(result,True)

	def test_mentions_value(self):
		out=get_mentions(df)
		result=True
		for key1 in out:
			for key2 in out[key1]:
				if out[key1][key2]>=1:
					result=False
					break
		self.assertEqual(result,True)

	def test_follow_value(self):
		out=get_follow(df)
		result=True
		for key1 in out:
			for key2 in out[key1]:
				if out[key1][key2]>=1:
					result=False
					break
		self.assertEqual(result,True)

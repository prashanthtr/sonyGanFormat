# Generates Sonygan json for a collection of audio files

# Input: Audio/Sound files/Path
# Output: Examples.json in SonyGan format
# Fileformat: soundName--p1-val--p2-val--..--seg-val.wav

# Segment pop

import numpy as np
import os  # for mkdir
import sys
import json
import math
import pdb

class SonyGanJson():
	def __init__(self, src, sr) :
		self.src = src:  # dataset type: 0 or "natural" and 1 or "artificial".
		if src == "natural" or src == 0:
			self.src_string = "Natural"
		elif src == "generated" or src == 1:
			self.src_string = "Generated"
		else:
			self.src_string = "Undecided"
		self.sr = sr
		self.fileList =  []
		self.SGjson = {}

	def read():
		#Reads single Files and stores metaParams

	def readAll(paramPath):
		# Reads all files in a folder
		fileList = [f for f in os.listdir(parampath) if '.wav' in f]
		self.fileList = fileList

	def storeRecords():

		for filename in self.fileList:
		    sgrecord = {}
		    fileArr = os.path.splitext(filename)[0].split("-")
		    sgrecord["sound_name"] = filename

		    for x in range(1, len(fileArr)-1):
		        pName = fileArr[x].split(":")[0]
		        print(pName+"natural")
		        normVal = float(fileArr[x].split(":")[1])
		        sgrecord[pName+"_norm"] = float(normVal); #unique string with parameters
		        if pName == "cf_exp":
		            sgrecord[pName+"_natural"] = 440*np.power(2,normVal)
		            sgrecord["midi_num"] = freq2Midi(440*np.power(2,normVal))
		        elif pName == "rate_exp":
		            sgrecord[pName+"_natural"]=np.power(2,normVal)
		        else:
		        	sgrecord[pName+"_natural"] = .04*np.power(10,normVal)

		    sgrecord["segment_number"] = fileArr[len(fileArr)-1].split(":")[1]
		    sgrecord["sound_name"] = fileArr[0]	
		    sgrecord["samplerate"] = self.sr; 
		    sgrecord["sound_source"] = self.dsType; #0 natural, 1 generated
		    sgrecord["sound_source_str"] = "generated"
		    sgrecord["sound_source_src"] = "https://github.com/prashanthtr/popTextureDS"
		    self.SGjson[filename]=sgrecord

	def ppRecords():
		print(json.dumps(self.SGjson, indent=4, sort_keys=True))

	def write2File():
		with open('sonyGan.json', 'w') as outfile:
			json.dump(self.SGjson, outfile, indent=4, sort_keys=True)

# Freq to MIdi for datasets with center frequency
def freq2Midi(freq):
	return round(12*math.log2(freq/440))+69;

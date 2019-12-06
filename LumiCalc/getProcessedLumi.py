from ROOT import *
import sys, argparse
import os
import FWCore.PythonUtilities.LumiList as LumiList

#----- Argument parser --------
parser = argparse.ArgumentParser()

parser.add_argument("--outputFile", help="output file", default='test.json')
parser.add_argument("--dir", help="base directory containing input files")

args = parser.parse_args()
#------------------------------

lumilist = {}

BASE_DIR = args.dir
filelist = [f for f in os.listdir(BASE_DIR) if 'Ds' in f]
print filelist

def fillLumi(FILENAME, lumilist):
   infile = TFile(FILENAME, "READ")
   _tree = infile.Get('T3MTree/t3mtree')
   nevents = _tree.GetEntriesFast()
   for i in xrange(nevents):
      _tree.GetEntry(i)
      run = _tree.Event_RunNumber
      lumi = _tree.Event_luminosityBlock
      if str(run) in lumilist:
        if lumi not in lumilist[str(run)]: lumilist[str(run)].append(lumi)
      else:
         lumilist[str(run)] = [lumi]

for filename in filelist:
   FILENAME = BASE_DIR+'/'+filename
   fillLumi(FILENAME, lumilist)

tmplist = LumiList.LumiList(runsAndLumis=lumilist)
tmplist.writeJSON(fileName=args.outputFile)

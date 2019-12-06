Lgin to lxplus node and run the following commands prior to lumi calculations
```
export PATH=$HOME/.local/bin:/cvmfs/cms-bril.cern.ch/brilconda/bin:$PATH
export PATH=$HOME/.local/bin:/nfshome0/lumipro/brilconda/bin:$PATH
```
Check if the brilws is updated. If not, use the following command to update brilws
```
pip install --install-option="--prefix=$HOME/.local" brilws --upgrade
pip show brilws
```
To calculate integrated luminosity in femto barn inverse, do
```
brilcalc lumi -u /fb -b "STABLE BEAMS" --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i <your-processedLumi.json>
```

If the processedLumi.json cannot be obtained from crab report, use the following command to create a JSON file.

```
python getProcessedLumi.py --dir <path-to-dir-with-ntuples> --outputFile <procesedLumi.json>
```

To get processedLumi.json for a list of datasets, run the following command

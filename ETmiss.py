import sys, os,math
import numpy as np
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad
from array import array

def read_lhe(input_file):
  lhe = EventFile(input_file)


  ETmiss=[]

  for event in lhe:
      pTmiss=[0,0]
      for particle in event:

         # if (particle.pid==13 or particle.pid== -13):
              p = FourMomentum(particle)
              pTmiss[0]+=p.px
              pTmiss[1]+=p.py
              #print(pT)        

      ETmiss.append(math.sqrt(pTmiss[0]**2+pTmiss[1]**2))
  #print(ETmiss) 
  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas()
  myC.Divide(2,1)

  myC.cd(1)
  gPad.SetLogy()
  #gPad.SetLogx()
  hname = "ETmiss"
  nbins, xmin, xmax = 100, min(ETmiss), max(ETmiss)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(ETmiss):
    h1.Fill(pt)
  h1.SetTitle("ETmiss;ETmiss[GeV];Events/bin")
  h1.GetXaxis().SetRangeUser(0,200)
  h1.GetXaxis().CenterTitle()
  h1.GetYaxis().SetRangeUser(1e-3,1e4)
  h1.GetYaxis().CenterTitle()
  h1.Draw()
  leg = R.TLegend(0.4,0.7,0.6,0.8)
  leg.SetHeader("mN[m=GeV]","C")
  leg.AddEntry(h1,"400","f")
  leg.Draw()
  #myC.SaveAs("pt.png")
  #tfout= R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()
  #return myC
  gBenchMark.Show("canvas")

#if __name__ == "__main__":

input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
read_lhe(input_file=input_file)

     

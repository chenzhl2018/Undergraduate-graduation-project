#!/usr/bin/env python2.7
import sys, os,math
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gStyle,gPad
######################################################################
#######Create a class################################################
class ETMISS:
 def __init__(self,name,mass,weight):
  self.name=name
  self.mass=mass
  self.weight=weight
 def read_lhe(self,input_file):
  lhe = EventFile(input_file)
  ETmiss= []
  for event in lhe:
      pTmiss=[0,0]
      for particle in event:
         p = FourMomentum(particle)

         if (particle.status== 1):
              pTmiss[0]+=p.px
              pTmiss[1]+=p.py
      ETmiss.append(math.sqrt(pTmiss[0]**2+pTmiss[1]**2))

  #Create histograms
  hname = "%s_ETmiss"%self.name
  nbins, xmin, xmax = 100, min(ETmiss), max(ETmiss)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, ET in enumerate(ETmiss):
    h1.Fill(ET,self.weight)
  h1.SetTitle("ETmiss,sqrt(s)=13TeV,L=300fb-1;ETmiss[GeV];Events/bin")



  #Write histograms to root file
  tfout = R.TFile("ETmiss.root","update")
  tfout.cd()
  h1.Write()
  tfout.Close()

  
################################################################
##########Read files############################################
#if __name__ == "__main__":

#input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
#read_lhe(input_file=input_file)

run_02=ETMISS("run_02",400,0.4554)
run_02.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz")
run_03=ETMISS("run_03",1000,0.29994)
run_03.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_03/unweighted_events.lhe.gz")
run_04=ETMISS("run_04",4000,0.04995)
run_04.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_04/unweighted_events.lhe.gz")
run_05=ETMISS("run_05",10000,0.009345)
run_05.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_05/unweighted_events.lhe.gz")

#########################################################################
#########Draw histograms#################################################
myC= R.TCanvas("c")
#myC.Divide(2,1)
gStyle.SetOptStat(0)

tfout = R.TFile("ETmiss.root")

#myC.cd(1)
gPad.SetLogy()
R.run_02_ETmiss.GetXaxis().CenterTitle()
#R.run_02_ETmiss.GetXaxis().SetRangeUser(0,1500)
R.run_02_ETmiss.GetYaxis().CenterTitle()
R.run_02_ETmiss.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_ETmiss.SetFillColor(1)
R.run_02_ETmiss.SetLineColor(2)
R.run_03_ETmiss.SetLineColor(3)
R.run_04_ETmiss.SetLineColor(4)
R.run_05_ETmiss.SetLineColor(5)
R.run_02_ETmiss.SetLineWidth(3)
R.run_03_ETmiss.SetLineWidth(3)
R.run_04_ETmiss.SetLineWidth(3)
R.run_05_ETmiss.SetLineWidth(3)
R.run_02_ETmiss.Draw("hist")
R.run_03_ETmiss.Draw("hist same")
R.run_04_ETmiss.Draw("hist same")
R.run_05_ETmiss.Draw("hist same")
leg_ETmiss= R.TLegend(0.4,0.7,0.6,0.9)
leg_ETmiss.SetHeader("mN[GeV]","C")
leg_ETmiss.AddEntry(R.run_02_ETmiss,"400","f")
leg_ETmiss.AddEntry(R.run_03_ETmiss,"1000","f")
leg_ETmiss.AddEntry(R.run_04_ETmiss,"4000","f")
leg_ETmiss.AddEntry(R.run_05_ETmiss,"10000","f")
leg_ETmiss.Draw()



#!/usr/bin/env python2.7
import sys, os,math
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gStyle,gPad
######################################################################
#######Create a class################################################
class HT:
 def __init__(self,name,mass,weight):
  self.name=name
  self.mass=mass
  self.weight=weight
 def read_lhe(self,input_file):
  lhe = EventFile(input_file)
  HT_u= []
  HT_j= []
  pt_u1= []
  pt_u2= []
  pt_j1= []
  pt_j2= []
  event_num=0
  for event in lhe:
      pt_event_u=[]
      pt_event_j=[]
      for particle in event:
          p = FourMomentum(particle)

          if (particle.pid== -13 or particle.pid== 13):
              pt_event_u.append(p.pt)

          if (particle.status==1
                and particle.pid!= -13
                and particle.pid!=  13):
              pt_event_j.append(p.pt)

      pt_u1.append(max(pt_event_u))
      pt_u2.append(min(pt_event_u))
      pt_j1.append(max(pt_event_j))
      pt_j2.append(min(pt_event_j))

      HT_u.append(pt_u1[event_num]+pt_u2[event_num])
      HT_j.append(pt_j1[event_num]+pt_j2[event_num])
      event_num+=1

  #Create  ograms
  hname = "%s_u1u2"%self.name
  nbins, xmin, xmax = 100, min(HT_u), max(HT_u)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, ht in enumerate(HT_u):
    h1.Fill(ht,self.weight)
  h1.SetTitle("(a) HT_u,sqrt(s)=13TeV,L=300fb-1;HT_u[GeV];Events/bin")


  hname = "%s_j1j2"%self.name
  nbins, xmin, xmax = 100, min(HT_j), max(HT_j)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, ht in enumerate(HT_j):
    h2.Fill(ht,self.weight)
  h2.SetTitle("(b) HT_j,sqrt(s)=13TeV,L=300fb-1;HT_j[GeV];Events/bin")

  #Write  ograms to root file
  tfout = R.TFile("HT.root","update")
  tfout.cd()
  h1.Write()
  h2.Write()
  tfout.Close()

  
################################################################
##########Read files############################################
#if __name__ == "__main__":

#input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
#read_lhe(input_file=input_file)

run_02=HT("run_02",400,0.4554)
run_02.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz")
run_03=HT("run_03",1000,0.29994)
run_03.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_03/unweighted_events.lhe.gz")
run_04=HT("run_04",4000,0.04995)
run_04.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_04/unweighted_events.lhe.gz")
run_05=HT("run_05",10000,0.009345)
run_05.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_05/unweighted_events.lhe.gz")

#########################################################################
#########Draw  ograms#################################################
myC= R.TCanvas("c")
myC.Divide(2,1)
gStyle.SetOptStat(0)

tfout = R.TFile("HT.root")

myC.cd(1)
gPad.SetLogy()
R.run_02_u1u2.GetXaxis().CenterTitle()
R.run_02_u1u2.GetXaxis().SetRangeUser(0,2000)
R.run_02_u1u2.GetYaxis().CenterTitle()
R.run_02_u1u2.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_u1u2.SetFillColor(1)
R.run_02_u1u2.SetLineColor(2)
R.run_03_u1u2.SetLineColor(3)
R.run_04_u1u2.SetLineColor(4)
R.run_05_u1u2.SetLineColor(5)
R.run_02_u1u2.SetLineWidth(3)
R.run_03_u1u2.SetLineWidth(3)
R.run_04_u1u2.SetLineWidth(3)
R.run_05_u1u2.SetLineWidth(3)
R.run_02_u1u2.Draw(" ")
R.run_03_u1u2.Draw("  same")
R.run_04_u1u2.Draw("  same")
R.run_05_u1u2.Draw("  same")
leg_u1u2= R.TLegend(0.7,0.7,0.9,0.9)
leg_u1u2.SetHeader("mN[GeV]","C")
leg_u1u2.AddEntry(R.run_02_u1u2,"400","f")
leg_u1u2.AddEntry(R.run_03_u1u2,"1000","f")
leg_u1u2.AddEntry(R.run_04_u1u2,"4000","f")
leg_u1u2.AddEntry(R.run_05_u1u2,"10000","f")
leg_u1u2.Draw()


myC.cd(2)
gPad.SetLogy()
R.run_02_j1j2.GetXaxis().CenterTitle()
R.run_02_j1j2.GetXaxis().SetRangeUser(0,600)
R.run_02_j1j2.GetYaxis().CenterTitle()
R.run_02_j1j2.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_j1j2.SetFillColor(1)
R.run_02_j1j2.SetLineColor(2)
R.run_03_j1j2.SetLineColor(3)
R.run_04_j1j2.SetLineColor(4)
R.run_05_j1j2.SetLineColor(5)
R.run_02_j1j2.SetLineWidth(3)
R.run_03_j1j2.SetLineWidth(3)
R.run_04_j1j2.SetLineWidth(3)
R.run_05_j1j2.SetLineWidth(3)
R.run_02_j1j2.Draw(" ")
R.run_03_j1j2.Draw("  same")
R.run_04_j1j2.Draw("  same")
R.run_05_j1j2.Draw("  same")
leg_j1j2= R.TLegend(0.7,0.7,0.9,0.9)
leg_j1j2.SetHeader("mN[GeV]","C")
leg_j1j2.AddEntry(R.run_02_j1j2,"400","f")
leg_j1j2.AddEntry(R.run_03_j1j2,"1000","f")
leg_j1j2.AddEntry(R.run_04_j1j2,"4000","f")
leg_j1j2.AddEntry(R.run_05_j1j2,"10000","f")
leg_j1j2.Draw()

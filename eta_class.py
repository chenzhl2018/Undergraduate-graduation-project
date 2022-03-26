#!/usr/bin/env python2.7
import sys, os
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gStyle,gPad
######################################################################
#######Create a class################################################
class ETA:
 def __init__(self,name,mass,weight):
  self.name=name
  self.mass=mass
  self.weight=weight
 def read_lhe(self,input_file):
  lhe = EventFile(input_file)
  eta_u1= []
  eta_u2= []
  eta_j1= []
  eta_j2= []
  for event in lhe:
      eta_event_u=[]
      eta_event_j=[]
      for particle in event:
          p = FourMomentum(particle)

          if (particle.pid== -13 or particle.pid== 13):
              eta_event_u.append(p.pt)
              eta_event_u.append(p.pseudorapidity)         

          if (particle.status==1
                and particle.pid!= -13
                and particle.pid!=  13):
              eta_event_j.append(p.pt)
              eta_event_j.append(p.pseudorapidity)

      if eta_event_u[0]>=eta_event_u[2]:
          eta_u1.append(eta_event_u[1])
          eta_u2.append(eta_event_u[3])
      else:
          eta_u1.append(eta_event_u[3])
          eta_u2.append(eta_event_u[1])
      if eta_event_j[0]>=eta_event_j[2]:
          eta_j1.append(eta_event_j[1])
          eta_j2.append(eta_event_j[3])
      else:
          eta_j1.append(eta_event_j[3])
          eta_j2.append(eta_event_j[1])

  #Create histograms
  hname = "%s_u1"%self.name
  nbins, xmin, xmax = 100, min(eta_u1), max(eta_u1)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_u1):
    h1.Fill(eta,self.weight)
  h1.SetTitle("(a) eta(u1),sqrt(s)=13TeV,L=300fb-1;eta(u1)[GeV];Events/bin")

  hname = "%s_u2"%self.name
  nbins, xmin, xmax = 100, min(eta_u2), max(eta_u2)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_u2):
    h2.Fill(eta,self.weight)
  h2.SetTitle("(b) eta(u2),sqrt(s)=13TeV,L=300fb-1;eta(u2)[GeV];Events/bin")

  hname = "%s_j1"%self.name
  nbins, xmin, xmax = 100, min(eta_j1), max(eta_j1)
  h3 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_j1):
    h3.Fill(eta,self.weight)
  h3.SetTitle("(c) eta(j1),sqrt(s)=13TeV,L=300fb-1;eta(j1)[GeV];Events/bin")

  hname = "%s_j2"%self.name
  nbins, xmin, xmax = 100, min(eta_j2), max(eta_j2)
  h4 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_j2):
    h4.Fill(eta,self.weight)
  h4.SetTitle("(d) eta(j2),sqrt(s)=13TeV,L=300fb-1;eta(j2)[GeV];Events/bin")
 
  tfout = R.TFile("eta.root","update")
  tfout.cd()
  h1.Write()
  h2.Write()
  h3.Write()
  h4.Write()
  tfout.Close()

  
################################################################
##########Read files############################################
#if __name__ == "__main__":

#input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
#read_lhe(input_file=input_file)

run_02=ETA("run_02",400,0.4554)
run_02.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz")
run_03=ETA("run_03",1000,0.29994)
run_03.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_03/unweighted_events.lhe.gz")
run_04=ETA("run_04",4000,0.04995)
run_04.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_04/unweighted_events.lhe.gz")
run_05=ETA("run_05",10000,0.009345)
run_05.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_05/unweighted_events.lhe.gz")

#########################################################################
#########Draw histograms#################################################
myC= R.TCanvas("c")
myC.Divide(2,2)
gStyle.SetOptStat(0)

tfout = R.TFile("eta.root")

myC.cd(1)
gPad.SetLogy()
R.run_02_u1.GetXaxis().CenterTitle()
R.run_02_u1.GetYaxis().CenterTitle()
R.run_02_u1.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_u1.SetFillColor(1)
R.run_02_u1.SetLineColor(2)
R.run_03_u1.SetLineColor(3)
R.run_04_u1.SetLineColor(4)
R.run_05_u1.SetLineColor(5)
R.run_02_u1.SetLineWidth(3)
R.run_03_u1.SetLineWidth(3)
R.run_04_u1.SetLineWidth(3)
R.run_05_u1.SetLineWidth(3)
R.run_02_u1.Draw("")
R.run_03_u1.Draw("same")
R.run_04_u1.Draw("same")
R.run_05_u1.Draw("same")
leg_u1= R.TLegend(0.75,0.7,0.9,0.9)
leg_u1.SetHeader("mN[GeV]","C")
leg_u1.AddEntry(R.run_02_u1,"400","f")
leg_u1.AddEntry(R.run_03_u1,"1000","f")
leg_u1.AddEntry(R.run_04_u1,"4000","f")
leg_u1.AddEntry(R.run_05_u1,"10000","f")
leg_u1.Draw()


myC.cd(2)
gPad.SetLogy()
R.run_02_u2.GetXaxis().CenterTitle()
R.run_02_u2.GetYaxis().CenterTitle()
R.run_02_u2.GetYaxis().SetRangeUser(1e-1,1e3)
R.run_02_u2.SetLineColor(2)
R.run_03_u2.SetLineColor(3)
R.run_04_u2.SetLineColor(4)
R.run_05_u2.SetLineColor(5)
R.run_02_u2.SetLineWidth(3)
R.run_03_u2.SetLineWidth(3)
R.run_04_u2.SetLineWidth(3)
R.run_05_u2.SetLineWidth(3)
R.run_02_u2.Draw("")
R.run_03_u2.Draw("same")
R.run_04_u2.Draw("same")
R.run_05_u2.Draw("same")
leg_u2 = R.TLegend(0.75,0.7,0.9,0.9)
leg_u2.SetHeader("mN[GeV]","C")
leg_u2.AddEntry(R.run_02_u2,"400","f")
leg_u2.AddEntry(R.run_03_u2,"1000","f")
leg_u2.AddEntry(R.run_04_u2,"4000","f")
leg_u2.AddEntry(R.run_05_u2,"10000","f")
leg_u2.Draw()


myC.cd(3)
gPad.SetLogy()
R.run_02_j1.GetXaxis().CenterTitle()
R.run_02_j1.GetYaxis().CenterTitle()
R.run_02_j1.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_j1.SetFillColor(1)
R.run_02_j1.SetLineColor(2)
R.run_03_j1.SetLineColor(3)
R.run_04_j1.SetLineColor(4)
R.run_05_j1.SetLineColor(5)
R.run_02_j1.SetLineWidth(3)
R.run_03_j1.SetLineWidth(3)
R.run_04_j1.SetLineWidth(3)
R.run_05_j1.SetLineWidth(3)
R.run_02_j1.Draw("")
R.run_03_j1.Draw("same")
R.run_04_j1.Draw("same")
R.run_05_j1.Draw("same")
leg_j1= R.TLegend(0.75,0.7,0.9,0.9)
leg_j1.SetHeader("mN[GeV]","C")
leg_j1.AddEntry(R.run_02_j1,"400","f")
leg_j1.AddEntry(R.run_03_j1,"1000","f")
leg_j1.AddEntry(R.run_04_j1,"4000","f")
leg_j1.AddEntry(R.run_05_j1,"10000","f")
leg_j1.Draw()

myC.cd(4)
gPad.SetLogy()
R.run_02_j2.GetXaxis().CenterTitle()
R.run_02_j2.GetYaxis().CenterTitle()
R.run_02_j2.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_j2.SetFillColor(1)
R.run_02_j2.SetLineColor(2)
R.run_03_j2.SetLineColor(3)
R.run_04_j2.SetLineColor(4)
R.run_05_j2.SetLineColor(5)
R.run_02_j2.SetLineWidth(3)
R.run_03_j2.SetLineWidth(3)
R.run_04_j2.SetLineWidth(3)
R.run_05_j2.SetLineWidth(3)
R.run_02_j2.Draw("")
R.run_03_j2.Draw("same")
R.run_04_j2.Draw("same")
R.run_05_j2.Draw("same")
leg_j2= R.TLegend(0.75,0.7,0.9,0.9)
leg_j2.SetHeader("mN[GeV]","C")
leg_j2.AddEntry(R.run_02_j2,"400","f")
leg_j2.AddEntry(R.run_03_j2,"1000","f")
leg_j2.AddEntry(R.run_04_j2,"4000","f")
leg_j2.AddEntry(R.run_05_j2,"10000","f")
leg_j2.Draw()

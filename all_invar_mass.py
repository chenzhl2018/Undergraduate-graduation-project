#!/usr/bin/env python2.7

# import some modules
import sys, os
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gStyle,gPad
from array import array
######################################################################
#######Create a class################################################
class INVAR:
 def __init__(self,name,mass,weight):
  self.name=name
  self.mass=mass
  self.weight=weight
 def read_lhe(self,input_file):
  lhe = EventFile(input_file)
  pt_u1= []
  pt_u2= []
  pt_j1= []
  pt_j2= []
  invar_mass_j=[]
  for event in lhe:
      pt_event_u=[]
      pt_event_j=[]
      eta_event_u=[]
      eta_event_j=[]
      p_event_j=[0,0,0,0]
      in_mass_j=[]
      for particle in event:
          p = FourMomentum(particle)

          if (particle.pid== -13 or particle.pid== 13):

              pt_event_u.append(p.pt)
              eta_event_u.append(p.pseudorapidity)
          if (particle.status==1
                and particle.pid!= -13
                and particle.pid!=  13):
              pt_event_j.append(p.pt)
              eta_event_j.append(p.pseudorapidity)
              p_event_j[0]+=p.E
              p_event_j[1]+=p.px
              p_event_j[2]+=p.py
              p_event_j[3]+=p.pz
      in_mass_j.append(math.sqrt(p_event_j[0]**2-p_event_j[1]**2-p_event_j[2]**2-p_event_j[3]**2))
  #Preselection Cuts
      if (max(pt_event_u)>=27 and min(pt_event_u)>= 10
      and min(pt_event_j)>=25 and max(eta_event_u)<=2.7
      and max(eta_event_j)<=4.5 and min(in_mass_j)>=700):
          pt_u1.append(max(pt_event_u))
          pt_u2.append(min(pt_event_u))
          pt_j1.append(max(pt_event_j))
          pt_j2.append(min(pt_event_j))
          invar_mass_j.append(min(in_mass_j))
  #Create histograms
  hname = "%s_j1j2"%self.name
  binEdges=array('f',[700,750,800,850,900,950,1000,1100,1200,1400,
    1600,1800,2000,2200,2500,3500,4500,6000])
  nbins=len(binEdges)-1
  h1 = R.TH1F(hname, hname,nbins,binEdges)
  for i, invar_mass in enumerate(invar_mass_j):
    h1.Fill(invar_mass,self.weight)
  h1.SetTitle("(a) pt(u2),sqrt(s)=13TeV,L=300fb-1;pt(u2)[GeV];Events/bin")
  h1.Scale(1, "width")
  
  #Write histograms to root file
  tfout = R.TFile("invar_mass_all.root","update")
  tfout.cd()
  h1.Write()
  tfout.Close()


################################################################
##########Read files############################################
#if __name__ == "__main__":

#input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/sign_150/unweighted_events.lhe.gz"
#read_lhe(input_file=input_file)

sign_150=INVAR("sign_150",400,0.3583)
sign_150.read_lhe("/root/MG5_aMC_v3_3_1/Launch/sign_Gen/Events/run_01/unweighted_events.lhe.gz")
sign_1500=INVAR("sign_1500",1000,0.2017)
sign_1500.read_lhe("/root/MG5_aMC_v3_3_1/Launch/sign_Gen/Events/run_02/unweighted_events.lhe.gz")
sign_5000=INVAR("sign_5000",4000,0.03409)
sign_5000.read_lhe("/root/MG5_aMC_v3_3_1/Launch/sign_Gen/Events/run_03/unweighted_events.lhe.gz")
back_QCD=INVAR("back_QCD",10000,0.08801)
back_QCD.read_lhe("/root/MG5_aMC_v3_3_1/Launch/back_QCD_SR/Events/run_01/unweighted_events.lhe.gz")
back_EW=INVAR("back_EW",10000,0.08598)
back_EW.read_lhe("/root/MG5_aMC_v3_3_1/Launch/back_EW_SR/Events/run_01/unweighted_events.lhe.gz")
#########################################################################
#########Draw histograms#################################################
tfout = R.TFile("invar_mass_all.root")

myC= R.TCanvas("c")
myC.SetFillColor(0)
#myC.Divide(2,2)
gStyle.SetOptStat(0)
myS=R.THStack("s","")

binEdges=array('f',[700,750,800,850,900,950,1000,1100,1200,1400,1600,1800,2000,2200,2500,3500,4500,6000])
nbins=len(binEdges)-1
sum_back=R.TH1F("sum_back","sum_back",nbins,binEdges)
sum_back.Add(R.back_QCD_j1j2,1)
sum_back.Add(R.back_EW_j1j2,1)

#myC.cd(1)
gPad.SetLogy()

#R.sign_150_j1j2.GetXaxis().CenterTitle()
#R.sign_150_j1j2.GetXaxis().SetRangeUser(0,1000)
#R.sign_150_j1j2.GetYaxis().CenterTitle()
#R.sign_150_j1j2.GetYaxis().SetRangeUser(1e-1,1e3)
R.back_QCD_j1j2.SetFillColor(7)
R.back_EW_j1j2.SetFillColor(9)
#R.sign_150_j1j2.SetFillColor(1)
R.sign_150_j1j2.SetLineColor(2)
R.sign_1500_j1j2.SetLineColor(3)
R.sign_5000_j1j2.SetLineColor(4)
#R.back_QCD_j1j2.SetLineColor(5)
#R.back_EW_j1j2.SetLineColor(6)
sum_back.SetLineColor(1)
R.sign_150_j1j2.SetLineWidth(3)
R.sign_1500_j1j2.SetLineWidth(3)
R.sign_5000_j1j2.SetLineWidth(3)
#R.back_QCD_j1j2.SetLineWidth(3)
#R.back_EW_j1j2.SetLineWidth(3)
sum_back.SetLineWidth(3)

myS.Add(R.back_QCD_j1j2,"hist")
myS.Add(R.back_EW_j1j2,"hist same")

myS.Draw("")
R.sign_150_j1j2.Draw("sameE")
R.sign_1500_j1j2.Draw("sameE")
R.sign_5000_j1j2.Draw("sameE")
#R.back_QCD_j1j2.Draw("hist")
#R.back_EW_j1j2.Draw("hist sameHE")
sum_back.Draw("sameE")

myS.GetXaxis().SetTitle("M(j1,j2)[GeV]")
myS.GetXaxis().CenterTitle()
myS.GetYaxis().SetTitle("dN/dM(j1,j2)[1/GeV]")
myS.GetYaxis().CenterTitle()
myS.SetMaximum(10)

#sign_150_j1j2_entry=R.sign_150_j1j2.GetEntries()
#sign_1500_j1j2_entry=R.sign_1500_j1j2.GetEntries()
#sign_5000_j1j2_entry=R.sign_1500_j1j2.GetEntries()
#back_QCD_j1j2_entry=R.back_QCD_j1j2.GetEntries()
#back_EW_j1j2_entry=R.back_EW_j1j2.GetEntries()

leg1_j1j2= R.TLegend(0.7,0.69,0.9,0.89)
#leg1_j1j2.SetHeader("mN[GeV]","C")
leg1_j1j2.SetBorderSize(0)
"""
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
"""
leg1_j1j2.AddEntry(R.sign_150_j1j2,"150GeV","le")
leg1_j1j2.AddEntry(R.sign_1500_j1j2,"1500GeV","le")
leg1_j1j2.AddEntry(R.sign_5000_j1j2,"5000GeV","le")
leg1_j1j2.Draw()

leg2_j1j2= R.TLegend(0.5,0.69,0.7,0.89)
#leg2_j1j2.SetHeader("mN[GeV]","C")
leg2_j1j2.SetBorderSize(0)
"""
  "l" means line, "p" means polymarker, "f" means box, "e" means draw vertical error bar if option "L" is also specified
"""
leg2_j1j2.AddEntry(R.back_QCD_j1j2,"WW(QCD)","f")
leg2_j1j2.AddEntry(R.back_EW_j1j2,"WW(EW)","f")
leg2_j1j2.AddEntry(sum_back,"back_QCD+EW","le")
leg2_j1j2.Draw()

latex = R.TLatex()
latex.SetTextSize(0.04)
latex.DrawLatexNDC(0.2, 0.85, "#bf{#bf{#sqrt{s} = 13TeV,L=300fb^{-1}}}")

import sys, os,math
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gStyle,gPad
######################################################################
#######Create a class################################################
class INVARMASS:
 def __init__(self,name,mass,weight):
  self.name=name
  self.mass=mass
  self.weight=weight
 def read_lhe(self,input_file):
  lhe = EventFile(input_file)
  in_mass_u= []
  in_mass_j= []
  for event in lhe:
      p_event_u=[0,0,0,0]
      p_event_j=[0,0,0,0]
      for particle in event:
          p = FourMomentum(particle)

          if (particle.pid== -13 or particle.pid== 13):
              p_event_u[0]+=p.E
              p_event_u[1]+=p.px
              p_event_u[2]+=p.py
              p_event_u[3]+=p.pz

          if (particle.status==1
                and particle.pid!= -13
                and particle.pid!=  13):
              p_event_j[0]+=p.E
              p_event_j[1]+=p.px
              p_event_j[2]+=p.py
              p_event_j[3]+=p.pz
      in_mass_u.append(math.sqrt(p_event_u[0]**2-p_event_u[1]**2-p_event_u[2]**2-p_event_u[3]**2))
      in_mass_j.append(math.sqrt(p_event_j[0]**2-p_event_j[1]**2-p_event_j[2]**2-p_event_j[3]**2))

  #Create histograms
  hname = "%s_invar_mass_u1u2"%self.name
  nbins, xmin, xmax = 100, min(in_mass_u), max(in_mass_u)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, in_mass in enumerate(in_mass_u):
    h1.Fill(in_mass,self.weight)
  h1.SetTitle("(a) in_mass_u,sqrt(s)=13TeV,L=300fb-1;M(u1u2)[GeV];Events/bin")


  hname = "%s_invar_mass_j1j2"%self.name
  nbins, xmin, xmax = 100, min(in_mass_j), max(in_mass_j)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, in_mass in enumerate(in_mass_j):
    h2.Fill(in_mass,self.weight)
  h2.SetTitle("(b) in_mass_j,sqrt(s)=13TeV,L=300fb-1;M(j1j2)[GeV];Events/bin")

  #Write histograms to root file
  tfout = R.TFile("in_mass.root","update")
  tfout.cd()
  h1.Write()
  h2.Write()
  tfout.Close()

  
################################################################
##########Read files############################################
#if __name__ == "__main__":

#input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
#read_lhe(input_file=input_file)

run_02=INVARMASS("run_02",400,0.4554)
run_02.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz")
run_03=INVARMASS("run_03",1000,0.29994)
run_03.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_03/unweighted_events.lhe.gz")
run_04=INVARMASS("run_04",4000,0.04995)
run_04.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_04/unweighted_events.lhe.gz")
run_05=INVARMASS("run_05",10000,0.009345)
run_05.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_05/unweighted_events.lhe.gz")

#########################################################################
#########Draw histograms#################################################
myC= R.TCanvas("c")
myC.Divide(2,1)
gStyle.SetOptStat(0)

tfout = R.TFile("in_mass.root")

myC.cd(1)
gPad.SetLogy()
R.run_02_invar_mass_u1u2.GetXaxis().CenterTitle()
R.run_02_invar_mass_u1u2.GetXaxis().SetRangeUser(0,3000)
R.run_02_invar_mass_u1u2.GetYaxis().CenterTitle()
R.run_02_invar_mass_u1u2.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_invar_mass_u1u2.SetFillColor(1)
R.run_02_invar_mass_u1u2.SetLineColor(2)
R.run_03_invar_mass_u1u2.SetLineColor(3)
R.run_04_invar_mass_u1u2.SetLineColor(4)
R.run_05_invar_mass_u1u2.SetLineColor(5)
R.run_02_invar_mass_u1u2.SetLineWidth(3)
R.run_03_invar_mass_u1u2.SetLineWidth(3)
R.run_04_invar_mass_u1u2.SetLineWidth(3)
R.run_05_invar_mass_u1u2.SetLineWidth(3)
R.run_02_invar_mass_u1u2.Draw("hist")
R.run_03_invar_mass_u1u2.Draw("hist same")
R.run_04_invar_mass_u1u2.Draw("hist same")
R.run_05_invar_mass_u1u2.Draw("hist same")
leg_invar_mass_u1u2= R.TLegend(0.7,0.7,0.9,0.9)
leg_invar_mass_u1u2.SetHeader("mN[GeV]","C")
leg_invar_mass_u1u2.AddEntry(R.run_02_invar_mass_u1u2,"400","f")
leg_invar_mass_u1u2.AddEntry(R.run_03_invar_mass_u1u2,"1000","f")
leg_invar_mass_u1u2.AddEntry(R.run_04_invar_mass_u1u2,"4000","f")
leg_invar_mass_u1u2.AddEntry(R.run_05_invar_mass_u1u2,"10000","f")
leg_invar_mass_u1u2.Draw()


myC.cd(2)
gPad.SetLogy()
R.run_02_invar_mass_j1j2.GetXaxis().CenterTitle()
R.run_02_invar_mass_j1j2.GetXaxis().SetRangeUser(0,3000)
R.run_02_invar_mass_j1j2.GetYaxis().CenterTitle()
R.run_02_invar_mass_j1j2.GetYaxis().SetRangeUser(1e-1,1e3)
#R.run_02_invar_mass_j1j2.SetFillColor(1)
R.run_02_invar_mass_j1j2.SetLineColor(2)
R.run_03_invar_mass_j1j2.SetLineColor(3)
R.run_04_invar_mass_j1j2.SetLineColor(4)
R.run_05_invar_mass_j1j2.SetLineColor(5)
R.run_02_invar_mass_j1j2.SetLineWidth(3)
R.run_03_invar_mass_j1j2.SetLineWidth(3)
R.run_04_invar_mass_j1j2.SetLineWidth(3)
R.run_05_invar_mass_j1j2.SetLineWidth(3)
R.run_02_invar_mass_j1j2.Draw("hist")
R.run_03_invar_mass_j1j2.Draw("hist same")
R.run_04_invar_mass_j1j2.Draw("hist same")
R.run_05_invar_mass_j1j2.Draw("hist same")
leg_invar_mass_j1j2= R.TLegend(0.7,0.7,0.9,0.9)
leg_invar_mass_j1j2.SetHeader("mN[GeV]","C")
leg_invar_mass_j1j2.AddEntry(R.run_02_invar_mass_j1j2,"400","f")
leg_invar_mass_j1j2.AddEntry(R.run_03_invar_mass_j1j2,"1000","f")
leg_invar_mass_j1j2.AddEntry(R.run_04_invar_mass_j1j2,"4000","f")
leg_invar_mass_j1j2.AddEntry(R.run_05_invar_mass_j1j2,"10000","f")
leg_invar_mass_j1j2.Draw()

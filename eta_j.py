import sys, os,numpy
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad

def read_lhe(input_file):
  lhe = EventFile(input_file)
  eta_j1=[]
  eta_j2=[]
  for event in lhe:

      event_j=[]
      for particle in event:
          if (particle.status==1
                and particle.pid!=13
                and particle.pid!= -13):
              p = FourMomentum(particle)
              event_j.append(p.pt)
              event_j.append(p.pseudorapidity)
      if event_j[0]>= event_j[2]:
           eta_j1.append(event_j[1])
           eta_j2.append(event_j[3])
      else:
           eta_j1.append(event_j[3])
           eta_j2.append(event_j[1])
      #print(eta)
      #eta_max=max(eta)
      #etamin=min(eta)

  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas()
  myC.Divide(2,1)

  myC.cd(1)
  gPad.SetLogy()
  hname = "eta_j1"
  nbins, xmin, xmax = 100, min(eta_j1), max(eta_j1)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_j1):
    h1.Fill(eta)
  h1.SetTitle("eta(j1);eta(j1);Event/bin")
  h1.GetXaxis().SetRangeUser(-5,5)
  h1.GetXaxis().CenterTitle()
  h1.GetYaxis().SetRangeUser(1e-1,1e4)
  h1.GetYaxis().CenterTitle()
  h1.Draw()
  leg = R.TLegend(0.4,0.7,0.6,0.8)
  leg.SetHeader("mN[GeV]","C")
  leg.AddEntry(h1,"400","f")
  leg.Draw()
  #myC.SaveAs("pt.png")
  #gBenchMark.Show("canvas")
  #tfout = R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()
  #return myC

  myC.cd(2)
  gPad.SetLogy()
  hname = "eta_j2"
  nbins, xmin, xmax = 100, min(eta_j2), max(eta_j2)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_j2):
    h2.Fill(eta)
  h2.SetTitle("eta(j2);eta(j2);Event/bin")
  h2.GetXaxis().SetRangeUser(-5,5)
  h2.GetXaxis().CenterTitle()
  h2.GetYaxis().SetRangeUser(1e-1,1e4)
  h2.GetYaxis().CenterTitle()
  h2.Draw()
  leg2 = R.TLegend(0.4,0.7,0.6,0.8)
  leg2.SetHeader("mN[GeV]","C")
  leg2.AddEntry(h1,"400","f")
  leg2.Draw()
  #myC.SaveAs("pt.png")
  gBenchMark.Show("canvas")
  #tfout = R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()
  #return myC
#if __name__ == "__main__":

input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
read_lhe(input_file=input_file)

          
    
    
 

import sys, os
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad

def read_lhe(input_file):
  lhe = EventFile(input_file)

  pt_j1= []
  pt_j2= []
  for event in lhe:
      pt_event_j=[]
      for particle in event:

          if (particle.status==1
                and particle.pid!= -13
                and particle.pid!=  13):
              p = FourMomentum(particle)
              pt_event_j.append(p.pt)

      pt_j1.append(max(pt_event_j))
      pt_j2.append(min(pt_event_j))

  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas()
  myC.Divide(2,1)

  myC.cd(1)
  gPad.SetLogy()
  hname = "pt_j1"
  nbins, xmin, xmax = 100, min(pt_j1), max(pt_j1)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(pt_j1):
    h1.Fill(pt)
  h1.SetTitle("pt(j1);pt(j1)[GeV];Events/bin")
  #h1.GetXaxis().SetRangeUser(0,500)
  h1.GetXaxis().CenterTitle()
  h1.GetYaxis().SetRangeUser(1e-2,1e4)
  h1.GetYaxis().CenterTitle()
  h1.Draw()
  leg = R.TLegend(0.4,0.7,0.6,0.8)
  leg.SetHeader("mN[GeV]","C")
  leg.AddEntry(h1,"400","f")
  leg.Draw()
  #myC.SaveAs("pt.png")
  #tfout= R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()
  #return myC

  myC.cd(2)
  gPad.SetLogy()
  hname = "pt_j2"
  nbins, xmin, xmax = 100, min(pt_j2), max(pt_j2)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(pt_j2):
    h2.Fill(pt)
  h2.SetTitle("pt(j2);pt(j2)/GeV;count")
  #h2.GetXaxis().SetRangeUser(0,500)
  h2.GetXaxis().CenterTitle()
  h2.GetYaxis().SetRangeUser(1e-2,1e4)
  h2.GetYaxis().CenterTitle()
  h2.Draw()
  leg2 = R.TLegend(0.4,0.7,0.6,0.8)
  leg2.SetHeader("mN[GeV]","C")
  leg2.AddEntry(h2,"400","f")
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

import sys, os,numpy
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad

def read_lhe(input_file):
  lhe = EventFile(input_file)
  eta_u1=[]
  eta_u2=[]
  for event in lhe:

      event_u=[]

      for particle in event:
          if particle.pid== -13 or particle.pid==13:
              p = FourMomentum(particle)
              event_u.append(p.pt)
              event_u.append(p.pseudorapidity)
      if event_u[0]>=event_u[2]:
          eta_u1.append(event_u[1])
          eta_u2.append(event_u[3])
      else:
          eta_u1.append(event_u[3])
          eta_u2.append(event_u[1])
      #print(eta)
      #eta_max=max(eta)
      #eta_min=min(eta)

  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas()
  myC.Divide(2,1)

  myC.cd(1)
  gPad.SetLogy()
  hname = "eta_u1"
  nbins, xmin, xmax = 100, min(eta_u1),max(eta_u1)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_u1):
    h1.Fill(eta)
  h1.SetTitle("eta(u1);eta(u1);Event/bins")
 # h1.GetXaxis().SetRangeUser(-4,4)
  h1.GetXaxis().CenterTitle()
  h1.GetYaxis().SetRangeUser(1e-2,1e4)
  h1.GetYaxis().CenterTitle()
  h1.Draw()
  #leg = R.TLegend(0.4,0.7,0.6,0.8)
  #leg.SetHeader("pt","C")
  #leg.AddEntry(h1,"t and t~","f")
  #leg.Draw()
  #myC.SaveAs("pt.png")
  #gBenchMark.Show("canvas")
  #tfout = R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()
  #return myC

  myC.cd(2)
  gPad.SetLogy()
  hname = "eta_u2"
  nbins, xmin, xmax = 100, min(eta_u2),max(eta_u2)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, eta in enumerate(eta_u2):
    h2.Fill(eta)
  h2.SetTitle("eta(u2);eta(u2);Event/bins")
 # h2.GetXaxis().SetRangeUser(-4,4)
  h2.GetXaxis().CenterTitle()
  h2.GetYaxis().SetRangeUser(1e-2,1e4)
  h2.GetYaxis().CenterTitle()
  h2.Draw()
  #leg = R.TLegend(0.4,0.7,0.6,0.8)
  #leg.SetHeader("pt","C")
  #leg.AddEntry(h1,"t and t~","f")
  #leg.Draw()
  #myC.SaveAs("pt.png")
  gBenchMark.Show("canvas")
  #tfout = R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h2.Write()
  #tfout.Close()
  #return myC
#if __name__ == "__main__":

input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
read_lhe(input_file=input_file)

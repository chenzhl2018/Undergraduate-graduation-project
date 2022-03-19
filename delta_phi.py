import sys, os,math
import numpy as np
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad
from array import array

def read_lhe(input_file):
  lhe = EventFile(input_file)


  delta_phi=[]

  for event in lhe:
      pt_u=[]
      for particle in event:

          if (particle.pid== -13 or particle.pid== 13):
              p = FourMomentum(particle)

              pt_u.append(p.px)
              pt_u.append(p.py)
              pt_u.append(p.pt)
      delta_phi.append(math.acos((pt_u[0]*pt_u[3]+pt_u[1]*pt_u[4])/(pt_u[2]*pt_u[5])))

  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas()
  myC.Divide(2,1)

  myC.cd(1)
  gPad.SetLogy()
  #gPad.SetLogx()
  hname = "detla_phi"
  nbins, xmin, xmax = 100, min(delta_phi), max(delta_phi)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(delta_phi):
    h1.Fill(pt)
  h1.SetTitle("delta_phi;delta_phi(u1)[GeV];Events/bin")
  #h1.GetXaxis().SetRangeUser(0,1500)
  h1.GetXaxis().CenterTitle()
  h1.GetYaxis().SetRangeUser(1e-2,1e3)
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
  gBenchMark.Show("canvas")

#if __name__ == "__main__":

input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
read_lhe(input_file=input_file)
  

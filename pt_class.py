import sys, os
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad

class PT:
 def __init__(self,name,mass):
  self.name=name
  self.mass=mass

 def read_lhe(self,input_file):
  lhe = EventFile(input_file)

  pt_u1= []
  pt_u2= []
  for event in lhe:
      pt_event_u=[]
      for particle in event:
          
          if (particle.pid== -13 or particle.pid== 13):
              p = FourMomentum(particle)
              pt_square = p.pt2
              pt = math.sqrt(pt_square)
              pt_event_u.append(pt)
      pt_u1.append(max(pt_event_u))
      pt_u2.append(min(pt_event_u))
  
  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas("c")
  myC.DrawClone()
  myC.Divide(2,1)
  
  myC.cd(1)  
  gPad.SetLogy()
  hname = "pt_u1"
  nbins, xmin, xmax = 100, min(pt_u1), max(pt_u1)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(pt_u1):
    h1.Fill(pt)
  h1.SetTitle("pt(u1);pt(u1)[GeV];Events/bin")
  h1.GetXaxis().SetRangeUser(0,1500)
  h1.GetXaxis().CenterTitle()
  h1.GetYaxis().SetRangeUser(1e-2,1e4)
  h1.GetYaxis().CenterTitle()
  h1.DrawClone()
  leg = R.TLegend(0.4,0.75,0.6,0.85)
  leg.SetHeader("mN[GeV]","C")
  leg.AddEntry(h1,"%s"%self.mass,"f")
  leg.DrawClone()
  #myC.SaveAs("pt.png")
  #tfout= R.TFile("pt.root")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()
  #return myC

  myC.cd(2)  
  gPad.SetLogy()
  hname = "self.name,pt_u2"
  nbins, xmin, xmax = 100, min(pt_u2), max(pt_u2)
  h2 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(pt_u2):
    h2.Fill(pt)
  h2.SetTitle("pt(u2);pt(u2)[GeV];Events/bin")
  h2.GetXaxis().SetRangeUser(0,1500)
  h2.GetXaxis().CenterTitle()
  h2.GetYaxis().SetRangeUser(1e-2,1e4)
  h2.GetYaxis().CenterTitle()
  h2.DrawClone()
  leg2 = R.TLegend(0.4,0.75,0.6,0.85)
  leg2.SetHeader("mN[GeV]","C")
  leg2.AddEntry(h2,"self.mass","f")
  leg2.DrawClone()
  #myC.Print("pt_u.pdf")
  #gBenchMark.Show("canvas")
  tfout = R.TFile("pt.root","update")
  tfout.cd()
  myC.Write()
  h1.Write()
  tfout.Close()

#if __name__ == "__main__":

#input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
#read_lhe(input_file=input_file)

run_02=PT("run_02",400)
run_02.read_lhe("/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz")

tfout = R.TFile("pt.root")
#c=tfout.c
h=tfout.pt_u1
R.c.Draw()
#h.Draw()

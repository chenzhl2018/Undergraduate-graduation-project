import sys, os
sys.path.append("/root/MG5_aMC_v3_3_1")
from madgraph.various.lhe_parser import *
import ROOT as R
from ROOT import gBenchmark,gPad

def read_lhe(input_file):
  lhe = EventFile(input_file)
  HT=[]
  r_HT_u1=[]
  pt_j1= []
  pt_j2= []
  pt_u1=[]
  pt_u2=[]
  event_num=0
  for event in lhe:
      pt_event_j=[]
      pt_event_u=[]
      for particle in event:
          if (particle.pid== 13 or particle.pid== -13):
              p = FourMomentum(particle)
              pt_event_u.append(p.pt)
                            

          if (particle.status==1 
		and particle.pid!= -13 
		and particle.pid!=  13):
              p = FourMomentum(particle)
              pt_event_j.append(p.pt)
      pt_u1.append(max(pt_event_u))        
      pt_u2.append(min(pt_event_u))        
      pt_j1.append(max(pt_event_j))
      pt_j2.append(min(pt_event_j))
      HT.append(pt_j1[event_num]+pt_j2[event_num])
      r_HT_u1.append(HT[event_num]/pt_u1[event_num])
      event_num+=1
  #print (data)
  gBenchmark.Start("canvas")
  myC= R.TCanvas()
  myC.Divide(2,1)
  
  myC.cd(1)  
  gPad.SetLogy()
  hname = "pt_j1"
  nbins, xmin, xmax = 100, min(r_HT_u1), max(r_HT_u1)
  h1 = R.TH1F(hname, hname, nbins, xmin, xmax)
  for i, pt in enumerate(r_HT_u1):
    h1.Fill(pt)
  h1.SetTitle("pt(j1);pt(j1)[GeV];Events/bin")
  h1.GetXaxis().SetRangeUser(0,4)
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
  gBenchMark.Show("canvas")


#if __name__ == "__main__":

input_file="/root/MG5_aMC_v3_3_1/PRO1/Events/run_02/unweighted_events.lhe.gz"
read_lhe(input_file=input_file)

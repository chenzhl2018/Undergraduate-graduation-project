import sys, os
from ROOT import gPad,gStyle
import ROOT as R
from array import array

mN=array('f',[40,100,400,1000,4000,10000])
sigma=array('f',[3.173,8.897,15.18,9.998,1.665,0.3115])
sigmaerror=array('f',[9.3e-03,2.5e-02,6.1e-02,2.7e-02,5.9e-03,7.3e-04])
fig2=R.TGraphErrors(6,mN,sigma,0,sigmaerror)

sigma2=array('f',[50.77,142.4,242.8,160,26.64,4.985])
sigmaerror2=array('f',[0.15,0.4,0.97,0.44,9.4e-02,1.2e-02])
fig22=R.TGraphErrors(6,mN,sigma2,0,sigmaerror2)

#fig2=R.TGraph(6,mN,sigma)
b=R.TCanvas()
b.SetLogx()
b.SetLogy()
#b.Range(40,1e-1,1e4,1e7)
#b.DrawFrame(40,1e-1,1e4,1e7)
fig2.GetXaxis().SetRangeUser(40,1e4)
fig2.GetXaxis().CenterTitle()
fig2.GetYaxis().SetRangeUser(1e-1,1e7)
fig2.GetYaxis().CenterTitle()
fig2.SetTitle("Fig2;mN[GeV];sigma0[fb]")
fig2.Draw("AC")
fig2.SetLineColor(619)
#gStyle.SetLineStyleString(11,"400 200")
#fig2.SetLineStyle(10)
fig2.SetLineWidth(3)

fig22.SetLineWidth(3)
fig22.SetLineColor(2)
fig22.Draw("C")
#b.DrawFrame(40,1e-1,1e4,1e7)
#fig2.GetXaxis().SetTitle("mN[GeV]")
#fig2.GetTitle().SetTitle("fig2")
#fig2.GetYaxis().SetTitle("sigma0")
#fig2.GetXaxis().SetTitleSize(40)
fig2.GetXaxis().SetLabelSize(0.05)
fig2.GetXaxis().SetTitleOffset(1.5)


t1=R.TText(1000,1e5,"13 TeV LHC")
t1.SetTextFont(43)
t1.SetTextSize(40)
t1.Draw()
t2=R.TText(1000,10,"WW(LO)")
t2.SetTextColor(619)
t2.Draw()
t3=R.TText(1000,160,"16 WW(LO)")
t3.SetTextColor(2)
t3.Draw()

b.Print("fig2.png")


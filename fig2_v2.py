import sys, os
from ROOT import gPad,gStyle
import ROOT as R
from array import array

#multi=R.TMultiGraph()

#WW
mN_WW=array('f',[40,100,400,1000,4000,10000])
sigma_WW=array('f',[3.173,8.897,15.18,9.998,1.665,0.3115])
sigmaerror_WW=array('f',[9.3e-03,2.5e-02,6.1e-02,2.7e-02,5.9e-03,7.3e-04])
fig2_WW=R.TGraphErrors(6,mN_WW,sigma_WW,0,sigmaerror_WW)
#CCDY
mN_CCDY=array('f',[40,50,60,80,100,400,1000,1200,2000])
sigma_CCDY=array('f',[7840e3,5364e3,2713e3,60.5e3,19.32e3,0.1185e3,0.002563e3,0.001051e3,5.405e-02])
sigmaerror_CCDY=array('f',[ 20e3,13e3,4.7e3,0.21e3,0.065e3,0.00035e3,7.5e-03,2.8e-03,1.3e-04])
fig2_CCDY=R.TGraphErrors(9,mN_CCDY,sigma_CCDY,0,sigmaerror_CCDY)
#W
mN_W=array('f',[40,50,60,80,100,400,1000,1200,2000,4000])
sigma_W=array('f',[7.38e3,5.036e3,2.572e3,0.1661e3,0.1222e3,0.02838e3,0.004265e3,0.00255e3,0.0004082e3,6.838e-03])
sigmaerror_W=array('f',[0.023e3,0.017e3,0.0093e3,0.00054e3,0.00046e3,0.00011e3,1.2e-02,8.8e-03,1.1e-03,3e-05])
fig2_W=R.TGraphErrors(10,mN_W,sigma_W,0,sigmaerror_W)

#fig2=R.TGraph(6,mN,sigma)
b=R.TCanvas()
b.SetLogx()
b.SetLogy()
#b.Range(40,1e-1,1e4,1e7)
#b.DrawFrame(40,1e-1,1e4,1e7)
fig2_WW.GetXaxis().SetRangeUser(40,1e4)
fig2_WW.GetXaxis().CenterTitle()
fig2_WW.GetYaxis().SetRangeUser(1e-1,1e7)
fig2_WW.GetYaxis().CenterTitle()
fig2_WW.SetTitle("Fig2;mN[GeV];sigma0[fb]")
fig2_WW.Draw("AC")
fig2_WW.SetLineColor(619)
#gStyle.SetLineStyleString(11,"400 200")
#fig2.SetLineStyle(10)
fig2_WW.SetLineWidth(3)
#fig2.GetXaxis().SetTitleSize(40)
fig2_WW.GetXaxis().SetLabelSize(0.05)
fig2_WW.GetXaxis().SetTitleOffset(1.5)

fig2_CCDY.Draw("CE")
fig2_CCDY.SetLineColor(2)
fig2_CCDY.SetLineWidth(3)

fig2_W.Draw("C")
fig2_W.SetLineColor(3)
fig2_W.SetLineWidth(3)

t1=R.TText(1000,1e5,"13 TeV LHC")
t1.SetTextFont(43)
t1.SetTextSize(40)
t1.Draw()
t2=R.TText(1000,10,"WW(LO)")
t2.SetTextColor(619)
t2.Draw()
t3=R.TText(120,1e4,"CCDY(LO)")
t3.SetTextColor(2)
t3.Draw()
t4=R.TText(120,1e2,"W(LO)")
t4.SetTextColor(3)
t4.Draw()


#multi.Add(fig2)
#multi.Add(fig2_CCDY)

#b.Print("fig2.png")

clear all
insheet using "C:\Users\Nathan\Desktop\Informatics HW\labeled_data.csv", comma

*create 2nd to 5th order polynomial

gen pop2 = pop * pop
gen pop3 = popu * popu * popu
gen pop4 = popu * popu * popu * popu
gen pop5 = popu * popu * popu * popu * popu

local poly2 popu pop2
local poly3 popu pop2 pop3
local poly4 popu pop2 pop3 pop4
local poly5 popu pop2 pop3 pop4 pop5



reg num popu
eststo m1

reg num `poly2'
eststo m2
regvalidate, reps(10)

reg num `poly3'
eststo m3
**regvalidate, reps(10)

reg num `poly4'
eststo m4
**regvalidate, reps(10)

reg num `poly5'
eststo m5
**regvalidate, reps(10)

crossfold reg num popu, k(10)
crossfold reg num popu, k(10) r2

crossfold reg num `poly2', k(10)
crossfold reg num `poly2', k(10) r2

crossfold reg num `poly3', k(10)
crossfold reg num `poly3', k(10) r2

crossfold reg num `poly4', k(10)
crossfold reg num `poly4', k(10) r2

crossfold reg num `poly5', k(10) loud
crossfold reg num `poly5', k(10) r2

/*
bootstrap, reps(10): reg num popu
di e(rmse)
eststo p1
bootstrap, reps(10): reg num `poly2'
di e(rmse)
eststo p2
bootstrap, reps(10): reg num `poly3'
di e(rmse)
eststo p3
bootstrap, reps(10): reg num `poly4'
di e(rmse)
eststo p4
bootstrap, reps(10): reg num `poly5' 
di e(rmse)
eststo p5
*/

******************************
*******************************
********************************
crossfold reg num popu, k(10) loud
*******************************
crossfold reg num `poly2', k(10) loud
*******************************
crossfold reg num `poly3', k(10) loud
*******************************
crossfold reg num `poly4', k(10) loud
*******************************
crossfold reg num `poly5', k(10) loud

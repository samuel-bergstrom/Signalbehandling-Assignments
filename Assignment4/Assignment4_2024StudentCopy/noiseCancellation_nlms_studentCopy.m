%-----------
% 1TE651 Signal Processing 
% Template for the Assignment: Active Noise Cancellation
%-------

clear all
close all

% choose the noise type, possible values: 1,2,3,4 
mynoiseScenario=1; 

% assumes that DATASETA folder is a subfolder of your current Matlab directory
noisefile=sprintf('DATASETA/N%d.wav',mynoiseScenario);
signalfile=sprintf('DATASETA/vocalN%d.wav',mynoiseScenario);

% noise signal
[w,~] = audioread(noisefile);
w=w(:);

% music +noise signal
[xw,Fs] = audioread(signalfile);
xw=xw(:);

%----------------------------------------------
% todo:processing of the signals, to be completed by the course
% participants




% --------------------------------------
% At this point,  recx should hold the reconstructed music variable. 
% Make sure to normalize recx with its maximum absolute value before saving it.
% It will be useful to think why this normalization is necessary.

recfile=sprintf('recvocalN%d.wav',mynoiseScenario); % file name
audiowrite(recfile,recx,Fs); % write to file

%  todo: code for plotting power spectrum: 
% Matlab commands  fft, periodogram, pwelch,  may be useful for this purpose.
% For readability,  while plotting the power spectrum, use decibels in the y-axis.
% That is, instead of plotting, for instance P, plot  $10 *log10 (P)$.  



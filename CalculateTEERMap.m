% clean workspace %
clear all
close all

names = [];
for k = 1:3
    Data = readingDataFile();
    tmp_GAP(k, 1:length(Data.Gap)) = Data.Gap;
    P = Data.pairName;
    names = [P ' ' names]
end
colorMap = [linspace(1,0,256)', linspace(0,1,256)', zeros(256,1)]

c1 = [ones(128,1), linspace(1,0,128)' ,linspace(1,0,128)']
c2 = [linspace(0,1,128)',linspace(0,1,128)',ones(128,1)]
C = [ c2; c1]

%h.xlabel = linspace(0,length(Data.Gap)/2,length(Data.Gap))
Yname = strsplit(names);
Yname = flip(Yname(1:(length(Yname)-1)))

h = heatmap(tmp_GAP);
h.Colormap = C;



h.YData = Yname;
h.XData = Data.Time
if (abs(min(min(tmp_GAP))) > max(max(tmp_GAP)))
    val_lims = abs(min(min(tmp_GAP)));
else
    val_lims = max(max(tmp_GAP));
end
caxis([(val_lims)*-1 (val_lims)])


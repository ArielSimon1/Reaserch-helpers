% **A mission**
% this function select and read the data file
function [Data_structure] = readingDataFile()
% create an empty data structure with proper fields.
Data_structure = struct('Pre_pair',[],'Post_pair',[],'Gap', [],'Time',[],'fileName',[],'pairName',[]);

% file choosing:
[file, path] = uigetfile({'*.xls';'*.xlsx'},'File Selector'); %% '*' means ignore until this point
Data_structure.pairName = file;
newStr = erase(file,".xls");
Data_structure.pairName = newStr;
Data_structure.fileName = [path file];

% read the metadata file fields:
[numericData, headers] = xlsread(Data_structure.fileName); %%  '~' do not present
Data_structure.Time =  numericData(:,1);
numericData = numericData(:,2:(length(headers)));

% fill Data_structur fields with metadata_file values:
Data_structure.Pre_pair = headers{1,4};
Data_structure.Post_pair = headers{1,2};

% Gap calc
% pre
for k = 1:length(numericData)
    pre_avg(k) = (numericData(k,3) + numericData(k,4))/2;
end

%post
for k = 1:length(numericData)
    post_avg(k) = (numericData(k,1) + numericData(k,2))/2;
end

Data_structure.Gap = pre_avg-post_avg;
% if the gap is "-", so pre is lower (more berrier affected), if it's "+"
% so post is the lower.




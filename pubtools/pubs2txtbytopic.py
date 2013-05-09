#! /usr/bin/python

import cPickle
import sys
import textwrap
import re

# Year comparison function
def compare(item1, item2):
    match1 = re.search(r'((\d\d\d\d))',item1).group(0)
    match2 = re.search(r'((\d\d\d\d))',item2).group(0)

    print "comparing " + match1 + " and " + match2
    if match1 > match2:
        print "-1"
        return -1
    if match1 < match2:
        print "1"
        return 1
    else:
        print "0"
        return 0

#get the original data from the pickled list
infile = open("data.txt","rb")
completelist = cPickle.load(infile)
infile.close()

#create empty lists
SocialSignalProcessing = []
VideoAnalytics = []
AcousticSignalProcessing = []
SensorDataFusionMobileSensing = []
_3DModelingAndAnalysis = []
MachineLearning = []
MouseBehaviorAnalysis = []
InVitroNeuronalNetworkAnalysis = []
StructuralFunctionalBrainConnectivityAnalysis = []
ClusteringAnalysisfordrugdiscovery = []
Otherworks = []

#fill the lists with their corresponding papers
for item in completelist:
    if item[1] == 'Social Signal Processing':
        SocialSignalProcessing.append(item[0])
    elif item[1] == 'Video Analytics':
        VideoAnalytics.append(item[0])
    elif item[1] == 'Acoustic Signal Processing':
        AcousticSignalProcessing.append(item[0])
    elif item[1] == 'Sensor and Data Fusion, Mobile Sensing':
        SensorDataFusionMobileSensing.append(item[0])
    elif item[1] == '3D Modeling and Analysis':
        _3DModelingAndAnalysis.append(item[0])
    elif item[1] == 'Machine Learning':
        MachineLearning.append(item[0])
    elif item[1] == 'Mouse Behavior Analysis':
        MouseBehaviorAnalysis.append(item[0])
    elif item[1] == 'In-Vitro Neuronal Network Analysis':
        InVitroNeuronalNetworkAnalysis.append(item[0])
    elif item[1] == 'Structural and Functional Brain Connectivity Analysis':
        StructuralFunctionalBrainConnectivityAnalysis.append(item[0])
    elif item[1] == 'Clustering Analysis for drug discovery':
        ClusteringAnalysisfordrugdiscovery.append(item[0])
    elif item[1] == 'Other works':
        Otherworks.append(item[0])
    else:
        print item[1]
        print "Default case"

#sort the lists
SocialSignalProcessing.sort(compare)
VideoAnalytics.sort(compare)
AcousticSignalProcessing.sort(compare)
SensorDataFusionMobileSensing.sort(compare)
_3DModelingAndAnalysis.sort(compare)
MachineLearning.sort(compare)
MouseBehaviorAnalysis.sort(compare)
InVitroNeuronalNetworkAnalysis.sort(compare)
StructuralFunctionalBrainConnectivityAnalysis.sort(compare)
ClusteringAnalysisfordrugdiscovery.sort(compare)
Otherworks.sort(compare)

#Print out everything by topic
print ""
print "Social Signal Processing"
print "----------------"
for item in SocialSignalProcessing: print "\n" + item
print ""
print "Video Analytics"
print "----------------"
for item in VideoAnalytics: print "\n" + item
print ""
print "Acoustic Signal Processing"
print "----------------"
for item in AcousticSignalProcessing: print "\n" + item
print ""
print "Sensor and Data Fusion, Mobile Sensing"
print "----------------"
for item in SensorDataFusionMobileSensing: print "\n" + item
print ""
print "3D Modeling and Analysis"
print "----------------"
for item in _3DModelingAndAnalysis: print "\n" + item 
print ""
print "Machine Learning"
print "----------------"
for item in MachineLearning: print "\n" + item
print ""
print "Mouse Behavior Analysis"
print "----------------"
for item in MouseBehaviorAnalysis: print "\n" + item
print ""
print "In-Vitro Neuronal Network Analysis"
print "----------------"
for item in InVitroNeuronalNetworkAnalysis: print "\n" + item
print ""
print "Structural and Functional Brain Connectivity Analysis"
print "----------------"
for item in StructuralFunctionalBrainConnectivityAnalysis: print "\n" + item
print ""
print "Clustering Analysis for drug discovery"
print "----------------"
for item in ClusteringAnalysisfordrugdiscovery: print "\n" + item
print ""
print "Other Works"
print "----------------"
for item in Otherworks: print "\n" + item


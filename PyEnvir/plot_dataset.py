import os, csv 
from matplotlib import pyplot

datasetPath = f"{os.path.expanduser('~\\Desktop')}\\dataset eg"
figurePath = f"{os.path.expanduser('~\\Desktop')}\\dataset eg"

for filename in os.listdir(datasetPath):
    with open(os.path.join(datasetPath, filename)) as file:
        table = [row for row in csv.reader(file)]
        labelStats = [[], []]
        for r in range(len(table)):
            labelStats[int(float(table[r][2]))].append(r)
        labelColors = ["#005BBB", "#FFD500"]
        pyplot.clf()
        pyplot.axes().set_aspect(aspect = 1)
        for labelValue in [0, 1]:
            xValues = []
            yValues = []
            for r in labelStats[labelValue]:
                xValues.append(float(table[r][0]))
                yValues.append(float(table[r][1]))
            pyplot.plot(xValues, yValues, 's', color = labelColors[labelValue], markersize = 4)
        pyplot.savefig(os.path.join(figurePath, f"{filename.split('.')[0]}.png"), dpi = 300)
    print(f"Finished plotting {filename}")

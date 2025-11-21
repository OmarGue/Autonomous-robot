from matplotlib import pyplot as plt

#liste des points du chemin le plus court
chemin=[[14, 0], [41, 10], [50, 3], [47, 13], [41, 20], [47, 26], [34, 30], [30, 42], [34, 50], [9, 46], [4, 50], [5, 45], [5, 42], [0, 22], [0, 4]]

#position du robot
robot=[10,40]

#renvoie la distance entre deux points
def distance(p0,p1):
	a=p0[0]-p1[0]
	b=p0[1]-p1[1]
	return b**2 + a**2

#renvoie la valeur de l'index du plus proche point du robot
def plusProchePoint(chemin,robot):
    index=0
    d2=0
    d1=distance(chemin[0],robot)
    for i in range(1,len(chemin)):
        d2=distance(chemin[i],robot)
        if d2<d1:
            d1=d2
            index=i
    return index

#renvoie une liste adapté au point le plus proche
def plusProcheChemin(chemin,robot):
    index=plusProchePoint(chemin,robot)
    chemin2=[]
    for i in range (index,len(chemin)):
        chemin2.append(chemin[i])
    for i in range (index):
        chemin2.append(chemin[i])
    return chemin2


def scatter_plot(chemin2,robot):
    plusProche=chemin2[0]
    xs,ys=zip(*chemin2)
    plt.scatter(xs,ys) and plt.scatter(robot[0],robot[1],c='r') and plt.scatter(plusProche[0],plusProche[1],c='y')
    plt.show()


chemin2=plusProcheChemin(chemin,robot)
print(chemin)
print(chemin2)
scatter_plot(chemin2,robot)





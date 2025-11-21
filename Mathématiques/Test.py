
from matplotlib import pyplot as plt
from random import randint
from math import *


#return nbr coordonnees de point (x,y) entre min et max
def create_points(nbr,min=0,max=50):
	return [[randint(min,max),randint(min,max)] \
			for _ in range(nbr)]


#affiche les points de coords et si elle est donnée, affiche les points dans l'ordre de env_convex
def scatter_plot(coords,env_convex=None):
	xs,ys=zip(*coords) # separe coords en 2 listes xs et ys
	plt.scatter(xs,ys) # affiche chaque point
	if env_convex!=None:
		for i in range(1,len(env_convex)+1):
			if i==len(env_convex): i=0 # permet de relier le dernier point au premier
			c0=env_convex[i-1]
			c1=env_convex[i]
			plt.plot((c0[0],c1[0]),(c0[1],c1[1]),'r')
	plt.show()


#retourne la valeur de l'angle polaire entre 2 points, si un seul est donne, on se réfere au point d'ancrage (variable globale)
def angle_polaire(p0,p1=None):
	if p1==None: 
		p1=anchor
	a=p0[0]-p1[0]
	b=p0[1]-p1[1]
	return atan2(b,a)

#returne la valeur de la distance entre 2 points, si un seul est donne, on se réfere au point d'ancrage (variable globale)
def distance(p0,p1=None):
	if p1==None:
		p1=anchor
	a=p0[0]-p1[0]
	b=p0[1]-p1[1]
	return b**2 + a**2


#retourn le determinats de :
# 	[p1(x) p1(y) 1]
#	[p2(x) p2(y) 1]
# 	[p3(x) p3(y) 1]
# Si >0 alors sens trigo
# Si <0 alors horaire
# Si =0 alors colineaires
def det(p1,p2,p3):
	return   (p2[0]-p1[0])*(p3[1]-p1[1]) \
			-(p2[1]-p1[1])*(p3[0]-p1[0])


#sors une liste de coordonnees dont l'angle polaire est du plus petit au plus grand par rapport au point d'ancrage
#si les angles sont egaux on les tries par rapport à leur distance avec le point d'ancrage
def tri(coords):
	if len(coords)<=1: 
		return coords
	petit,egal,grand=[],[],[]
	piv_ang=angle_polaire(coords[randint(0,len(coords)-1)])
	for pt in coords:
		pt_ang=angle_polaire(pt)
		if   pt_ang<piv_ang:
			petit.append(pt)
		elif pt_ang==piv_ang:
			egal.append(pt)
		else:
			grand.append(pt)
	return   tri(petit) + sorted(egal,key=distance) + tri(grand)


# Returns the vertices comprising the boundaries of
# convex hull containing all points in the input set. 
# The input 'points' is a list of (x,y) coordinates.
# If 'show_progress' is set to True, the progress in 
# constructing the hull will be plotted on each iteration.
def graham_scan(points,show_progress=False):
	global anchor # to be set, (x,y) with smallest y value

	# Find the (x,y) point with the lowest y value,
	# along with its index in the 'points' list. If
	# there are multiple points with the same y value,
	# choose the one with smallest x.
	min_idx=None
	for i,(x,y) in enumerate(points):
		if min_idx==None or y<points[min_idx][1]:
			min_idx=i
		if y==points[min_idx][1] and x<points[min_idx][0]:
			min_idx=i

	# set the global variable 'anchor', used by the
	# 'polar_angle' and 'distance' functions
	anchor=points[min_idx]

	# sort the points by polar angle then delete 
	# the anchor from the sorted list
	sorted_pts=tri(points)
	del sorted_pts[sorted_pts.index(anchor)]

	# anchor and point with smallest polar angle will always be on hull
	hull=[anchor,sorted_pts[0]]
	for s in sorted_pts[1:]:
		while det(hull[-2],hull[-1],s)<=0:
			del hull[-1] # backtrack
			#if len(hull)<2: break
		hull.append(s)
		if show_progress: scatter_plot(points,hull)
	return hull


#permet d'avoir les points qu'il reste en dehors de l'enveloppe
def autre(pts, env_convex):
	reste = []
	for i in range(len(pts)):
		k=True
		for j in range(len(env_convex)):
			if pts[i]==env_convex[j]:
				k=False
		if k:
			reste.append(pts[i])
	return(reste)

			
#méthode de recherche des deux points de l'enveloppe les plus proche d'un point
#conditions du choix du placement : distances entre un point et 2 points de l'enveloppe consecutif
def insertion1(pts):
	hull=graham_scan(pts)
	scatter_plot(pts,hull)
	reste=autre(pts,hull)
	for _ in range(len(reste)):
		index=len(hull)-1
		l1=distance(hull[len(hull)-1],reste[0])+distance(hull[0],reste[0])
		for j in range (len(hull)-1):
			l2=distance(hull[j],reste[0])+distance(hull[j+1],reste[0])
			if l1>l2 :
				index=j
				l1=l2
		hull.insert(index+1,reste[0])
		del reste[0]
	scatter_plot(pts,hull)
	return(hull)

#méthode de recherche des deux points de l'enveloppe les plus proche d'un point 
#conditions du choix du placement : distances entre un point et 2 points de l'enveloppe consecutif - la distance des 2 points de l'enveloppe
def insertion2(pts):
	hull=graham_scan(pts)
	scatter_plot(pts,hull)
	reste=autre(pts,hull)
	for _ in range(len(reste)):
		index=len(hull)-1
		l1=distance(hull[len(hull)-1],reste[0])+distance(hull[0],reste[0])-distance(hull[len(hull)-1],hull[0])
		for j in range (len(hull)-1):
			l2=distance(hull[j],reste[0])+distance(hull[j+1],reste[0])-distance(hull[j],hull[j+1])
			if l1>l2 :
				index=j
				l1=l2
		hull.insert(index+1,reste[0])
		del reste[0]
	scatter_plot(pts,hull)
	return(hull)

#méthode pas encore au point mais semble inutile
def insertion3(pts):
	hull=graham_scan(pts)
	scatter_plot(pts,hull)
	reste = autre(pts,hull)
	k=0
	l=1
	while len(hull)!=len(pts):
		index=0
		l1=distance(hull[k],reste[0])+distance(hull[l],reste[0])
		for i in range(1,len(reste)):
			l2=distance(hull[k],reste[i])+distance(hull[l],reste[i])
			if l1>l2 :
				index=l
				l1=l2
		hull.insert(l,reste[i])
		del reste[0]
		if l==len(hull):
			l=0
			k=k+1
		if k==len(hull):
			k=0
			l=l+1
		else :
			k=k+1
			l=l+1
		scatter_plot(pts,hull)
	return(hull)

pts=create_points(15)
hull=graham_scan(pts)
reste = autre(pts, hull)
#print(pts)
#print(hull)
#print(reste)

road=insertion2(pts)

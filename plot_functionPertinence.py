import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def main():
	""" Plot a figure
	"""
	sns.set_style("white")
	Gatys_value = [1.03*10**5,4.57*10**3,2.32*10**5,7.90*10**5,2.11*10**4,4.33*10**3, 8.01*10**3,6.44*10**3,  2.40*10**3,3.64*10**3]
	R_value = [9.61*10**8,2.37*10**6,6.50*10**8, 4.59*10**8,3.20*10**6, 2.11*10**6,2.54*10**4, 8.77*10**5,3.47*10**5,5.91*10**5]
	R_std = [ 4.21*10**8,2.37*10**5,3.46*10**7,2.00*10**7,9.56*10**4,8.38*10**4,3.79*10**3,1.91*10**4,1.4*10**4,2.41*10**4]
	CasMalGere = np.array([1,0,1,1,1,2,0,2,0,2])
	# 1 bien gere par gatys pas par R : bleu
	# 0 mieux gere par R que par Gatys : rouge
	# 2 identique : vert
	

	colors = ['#e41a1c', '#377eb8', '#4daf4a']
	colors = ["r", "b", "g"]
	x = np.array(range(len(Gatys_value)))
	Gatys_value = np.array(Gatys_value)
	R_value = np.array(R_value)
	R_std = np.array(R_std)
	print(len(x),len(Gatys_value),len(R_value),len(R_std))
	f,ax =plt.subplots()
	ax.set_yscale("log", nonposy='clip')
	#plt.errorbar(x, R_value, R_std, linestyle='None', marker='^')
	
	gatys = plt.scatter(x,Gatys_value,marker='o',color=np.array(colors)[CasMalGere], label='Gatys')
	galerne = plt.scatter(x,R_value,marker='^',color=np.array(colors)[CasMalGere], label='Galerne')
	#cb = plt.colorbar(gatys)
	_,_,galerne_err = plt.errorbar(x, R_value, yerr=R_std, linestyle='None', marker='None')# ,c=CasMalGere
	galerne_err[0].set_color(np.array(colors)[CasMalGere])
	
	
	#ax.set_title('Compromis entre style et contenu')
	plt.legend(handles=[galerne,gatys])
	ax.xaxis.set_ticklabels([1,2,3,4,5,6,7,8,9,10])
	ax.set_xlabel('Numero Image')
	ax.set_ylabel('Fonction cout')
	ax.tick_params(axis='x', which='minor')
	plt.xticks( np.arange(10) )
	plt.savefig("Pertinence",dpi=300)
	 

if __name__ == '__main__':
	main()

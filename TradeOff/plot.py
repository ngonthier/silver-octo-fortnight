
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    """ Plot a figure
    """
    content_strengh= [1.,0.1,0.01,0.001,0.0001,0.00001,0.000001,0.0000001]
    content_loss = [1.13*10**7,3.27*10**6,5.67*10**5,1.14*10**5,1.77*10**4,3.40*10**3,4.71*10**2,7.11*10**1]
    style_loss = [1.42*10**7, 2.91*10**6,3.47*10**5,1.28*10**5, 1.20*10**5,1.15*10**5,1.2*10**5,7.04*10**4]

    sns.set_style("white")
    content_loss_modif = []
    for i in range(len(content_loss)):
        if(content_strengh[i]==0):
            content_loss_modif += [0]
        else:
            content_loss_modif += [content_loss[i] / content_strengh[i]]
    print(content_loss_modif)
    print(style_loss)
    
    #ax = sns.pointplot(x=content_loss_modif, y=style_loss,hue=content_strengh)
    f,ax =plt.subplots()
    ax.plot(content_loss_modif,style_loss,marker='o')
    ax.set_title('Compromis entre style et contenu')
    ax.set_xlabel('Contenu')
    ax.set_ylabel('Style')
    print(ax.get_xticks())
    content_strengh_str_tab= []
    for i in range(len(content_strengh)):
        content_strengh_str = '{:.1e}'.format(content_strengh[i])
        content_strengh_str_tab += [content_strengh_str]
    style_loss2 = [1.42*10**7, 2.91*10**6,3.47*10**5,1.28*10**5, 1.28*10**5,1.28*10**5,1.28*10**5,7.04*10**4]
    content_loss_modif2 = content_loss_modif
    content_loss_modif2[5] *= 1/1.1
    [ax.text(p[0]*1.1, p[1]*1.01, p[2], color='b') for p in zip(content_loss_modif,style_loss2,content_strengh_str_tab)]
    ax.ticklabel_format(axis='x', style='scientific')
    ax.ticklabel_format(axis='y', style='scientific')
    plt.loglog()
    plt.savefig("TradeOff",dpi=1000)
     

if __name__ == '__main__':
    main()

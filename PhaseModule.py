import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
import scipy
import scipy.io

# fonction de normalisation
def norma(mat):
     mat1 = mat.real
     mat1 -= mat1.min()
     mat1 *= 255. / mat1.max()
     return mat1

#fonction de normailsation sur une échelle logarithmique
def normalog(mat):
     mat1 = norma(mat)
     mat1 = numpy.log(1 + mat1)
     mat1 *= 255. / mat1.max()
     return mat1

lena = scipy.misc.imread('Lena.png')

# transformée de Fourier de l'image
lena_fft = numpy.fft.fft2(lena)

# module de la transformée de Fourier de l'image
lena_fft_abs = abs(lena_fft)
# centré
lena_fft_abs_centre = numpy.fft.fftshift(lena_fft_abs)

# phase de la transformée de Fourier de l'image
lena_fft_phase = lena_fft / lena_fft_abs
# centré
lena_fft_phase_centre = numpy.fft.fftshift(lena_fft_phase)

# transformée de Fourier inverse du module
lena_abs = numpy.fft.ifft2(lena_fft_abs)

# transformée de Fourier inverse de la phase
lena_phase = numpy.fft.ifft2(lena_fft_phase)

fig = plt.figure()

ax1 = fig.add_subplot(2, 3, 1)
plt.title('lena')
ax1.imshow(lena, cmap = mpl.cm.gray)

ax2 = fig.add_subplot(2, 3, 2)
plt.title('fft module')
ax2.imshow(normalog(lena_fft_abs_centre), cmap = mpl.cm.gray)

ax3 = fig.add_subplot(2, 3, 3)
plt.title('fft phase')
ax3.imshow(norma(lena_fft_phase_centre), cmap = mpl.cm.gray)

ax5 = fig.add_subplot(2, 3, 5)
plt.title('module')
ax5.imshow(normalog(lena_abs), cmap = mpl.cm.gray)

ax6 = fig.add_subplot(2, 3, 6)
plt.title('phase')
ax6.imshow(norma(lena_phase), cmap = mpl.cm.gray)

plt.show()

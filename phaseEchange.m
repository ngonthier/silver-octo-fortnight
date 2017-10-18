clear all
close all
clc

Lena = mean(imread('Lena.png'),3);
Maison = mean(imread('Maison.png'),3);

LenaFFT = fft2(Lena);
MaisonFFT = fft2(Maison);

LenaMod = abs(LenaFFT);
LenaArg = angle(LenaFFT);

MaisonMod = abs(MaisonFFT);
MaisonArg = angle(MaisonFFT);

LenaFFT2 = LenaMod.*exp(1i*MaisonArg);
MaisonFFT2 = MaisonMod.*exp(1i*LenaArg);

Lena2 = ifft2(LenaFFT2);
Maison2 = ifft2(MaisonFFT2);

figure(1)
subplot(1,4,1)
imagesc(Lena), colormap(gray)
set(gca,'XTick',[])
set(gca,'YTick',[])
title('Image A')
subplot(1,4,2)
imagesc(Maison), colormap(gray)
set(gca,'XTick',[])
set(gca,'YTick',[])
title('Image B')
subplot(1,4,3)
imagesc(Lena2), colormap(gray)
set(gca,'XTick',[])
set(gca,'YTick',[])
title('Module de l''image A et phase de l''image B')
subplot(1,4,4)
imagesc(Maison2), colormap(gray)
set(gca,'XTick',[])
set(gca,'YTick',[])
title('Module de l''image B et phase de l''image A')
saveas(gcf,'fur','png')
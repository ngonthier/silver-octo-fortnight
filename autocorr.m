clear all
close all
clc

sand = mean(imread('sand.png'),3);
D20_01 = mean(imread('D20_01.png'),3);

Nsx = 256;  % Synthetic image dimensions
Nsy = 256;
sand = imresize(sand,[Nsy Nsx]);
D20_01 = imresize(D20_01,[Nsy Nsx]);
sandFFT = fft2(sand);
D20_01FFT = fft2(D20_01);


sandMod2 = ifftshift(ifft2(abs(sandFFT).^2));
D20_01Mod2 = ifftshift(ifft2(abs(D20_01FFT).^2));
pas = 8
[X,Y] = meshgrid(1:pas:256,1:pas:256);
sandMod2 = sandMod2(1:pas:256,1:pas:256);
D20_01Mod2 = D20_01Mod2(1:pas:256,1:pas:256);
figure(1)
ax0 = subplot(2,2,1)
imagesc(sand);
colormap(ax0,gray)
set(gca,'XTick',[])
set(gca,'YTick',[])
title('Image A')
ax00 = subplot(2,2,2)
imagesc(D20_01);
colormap(ax00,gray)
set(gca,'XTick',[])
set(gca,'YTick',[])
title('Image B')
ax2 = subplot(2,2,3)
s = surf(X,Y,sandMod2,'FaceAlpha',0.5);
colormap(ax2,summer)
s.EdgeColor = 'none';
title('Autocorrélation de A')
ax1 = subplot(2,2,4)
s = surf(X,Y,D20_01Mod2,'FaceAlpha',0.5);
colormap(ax1,summer)
s.EdgeColor = 'none';
title('Autocorrélation de B')



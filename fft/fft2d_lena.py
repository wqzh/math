import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size'] = '4'

plt.figure( dpi=300)
lena = plt.imread(r'./lena_std.tif',) 
lenagray = (0.299*lena[...,0]+0.587*lena[...,1]+0.114*lena[...,2]).astype('int32')
M,N = lenagray.shape # 512, 512
M2, N2 = M//2, N//2
cmap = plt.cm.gray

fft2 = np.fft.fft2(lenagray)    # fft2 of lenagray 
lena1 = np.log(np.abs(fft2))    # log(|F(u,v)|)
lena2 = np.log(np.abs(fft2))**2 # log(|F(u,v)|)^2
lena1shf = np.fft.fftshift(lena1) # center
lena2shf = np.fft.fftshift(lena2) # center

plt.figure(dpi=350)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=0, hspace=0.7)

plt.subplot(4,4,1)
plt.imshow(lenagray, cmap); plt.title('1、原始图像')
plt.subplot(4,4,5)
plt.imshow(lena1, cmap); plt.title('2、$log(|F(u,v)|)$')
plt.subplot(4,4,6)
plt.imshow(lena2, cmap); plt.title('3、${log}^{2}(|F(u,v)|)$')
plt.subplot(4,4,7)
plt.imshow(lena1shf, cmap);plt.title('4.a、中心平移图2')
plt.subplot(4,4,8)
plt.imshow(lena2shf, cmap);plt.title('4.b、中心平移图3')


### low-pass filter
mask1 = np.zeros((M,N), dtype='bool') # default false
mask2 = np.zeros((M,N), dtype='bool') # default false

thre = 10000 # r = 100
for u in range(M):
    for v in range(N):
        if (M2-u)**2 + (N2-v)**2 > thre:
            mask1[u,v] = True # mask1: out
mask2 = ~mask1 # mask2 in

### process low frequency
fft2cp1 = fft2.copy() # low-pass, inner circle 
fft2cp1_shf = np.fft.fftshift(fft2cp1)
fft2cp1_shf[mask1] = 1
lena_thre1 = np.log(np.abs(fft2cp1_shf))
plt.subplot(4,4,9)
plt.imshow(lena_thre1, cmap);plt.title('5、图4low pass')

lena_thre1_ishf = np.fft.ifftshift(fft2cp1_shf)
plt.subplot(4,4,10)
plt.imshow(np.log(np.abs(lena_thre1_ishf)), cmap);plt.title('6、图5 ishift')
lenalow = np.fft.ifft2(lena_thre1_ishf)
lenalowgray = np.abs(lenalow)
plt.subplot(4,4,11)
plt.imshow(lenalowgray, cmap);plt.title('7、图6 ifft2')


### process high frequency
fft2cp2 = fft2.copy() # high-pass, outer region
fft2cp2_shf = np.fft.fftshift(fft2cp2)
fft2cp2_shf[mask2] = 1
lena_thre2 = np.log(np.abs(fft2cp2_shf))
plt.subplot(4,4,13)
plt.imshow(lena_thre2, cmap);plt.title('8、图4high pass')

lena_thre2_ishf = np.fft.ifftshift(fft2cp2_shf)
plt.subplot(4,4,14)
plt.imshow(np.log(np.abs(lena_thre2_ishf)), cmap);plt.title('9、图8 ishift')
lenahigh = np.fft.ifft2(lena_thre2_ishf)
lenahighgray = np.abs(lenahigh)
plt.subplot(4,4,15)
plt.imshow(lenahighgray, cmap);plt.title('10、图9 ifft')

plt.savefig('./fft2_lena.pdf')
plt.show()
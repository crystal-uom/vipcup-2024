import numpy as np
import matplotlib.pyplot as plt
import bm3d
from skimage import io, img_as_float

in_path = "D:/VIP Cup/Dataset/ICIP training data/2/RawDataQA-2 (24)/RawDataQA-2-24 (108).tiff"
out_path = "D:/VIP Cup/Results/bm3d library/2-bm3d_sigma_"

noisy_oct = img_as_float(io.imread(in_path, as_gray=True))

sigma = 0.08

save_path = out_path + f"{sigma:.3f}"  + ".tiff"

bm3d_denoised = bm3d.bm3d(noisy_oct, sigma_psd=sigma, stage_arg=bm3d.BM3DStages.ALL_STAGES)

plt.imshow(bm3d_denoised, cmap='gray')
plt.imsave(save_path, bm3d_denoised, cmap='gray')
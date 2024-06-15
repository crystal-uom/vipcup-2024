import glob
import os
from pathlib import Path
from PIL import Image
import nibabel as nib
import numpy as np

input_path = "D:/VIP Cup/Dataset/ICIP training data/0/RawDataQA (32)/"
output_path= "D:/VIP Cup/test_0_32.nii.gz"
vip_dataset = "D:/VIP Cup/Dataset/ICIP training data/"
denoised_dataset = "D:/VIP Cup/Output dataset/denoised_tiff_data/"
output_dataset = "D:/VIP Cup/Output dataset/denoised_nifti_dataset/"

converted_nifti_count = 0

def is_tiff_dir(curr_path):
    '''function to check if the current directory having any tiff files'''
    num_tiff = len(glob.glob(os.path.join(curr_path, '*.tiff')))
    return num_tiff>0

def convert_tiff_dir_to_nifti(input_dir, output_path, stack_axis=2):
    '''
        function to convert tiff dir to nifti files
        stacking on z axis, stack_axis=2
    '''
    try:
        img_dir = input_dir
        fns = list([str(oct_image) for oct_image in glob.glob(os.path.join(img_dir,'*.tiff*'))])

        case_no = lambda x: int(x.split('(')[-1].split(')')[0])
        oct_images = sorted(fns, key = lambda y: case_no(y))


        if not oct_images:
            raise ValueError(f'img_dir ({input_dir}) does not contain any .tif or .tiff images.')
    
        imgs = []
        for oct_image in oct_images:
            #print(oct_image)
            
            img = np.asarray(Image.open(oct_image)).astype(np.float32).squeeze()
            if img.ndim != 3:
                raise Exception(f'Only 2D data supported. File {oct_image} has dimension {img.ndim}.')
            else:
                imgs.append(img)

        img = np.stack(imgs, stack_axis)
        nib.Nifti1Image(img,None).to_filename(output_path)

    except Exception as e:
        print(e)

def out_path(in_path):
    '''generate output path'''
    base_name = os.path.basename(in_path)
    class_name = os.path.basename(os.path.dirname(in_path))
    out_path = os.path.join(output_dataset,class_name) + "/" + base_name + ".nii.gz"
    return out_path

#convert_tiff_dir_to_nifti(input_path, output_path)

if __name__ == "__main__":

    dataset = glob.iglob(os.path.join(denoised_dataset, '**'), recursive=True)

    for i,file in enumerate(dataset):
        if is_tiff_dir(file):

            # output directory of the corresponding nifti file
            dest_file = out_path(file)
            new_dir = os.path.dirname(dest_file)
            os.makedirs(new_dir, exist_ok=True)

            #converting tiff directory to nifti
            try:
                convert_tiff_dir_to_nifti(file, dest_file, stack_axis=3)
                converted_nifti_count += 1
                print(f"Succesfully converted total files: {converted_nifti_count}")

            except Exception as e:
                print(e)

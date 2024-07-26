#!/bin/bash 

#SBATCH --job-name="260-DDX4-R2K-260" 
#SBATCH --account=pcg_llps 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=96G 
#SBATCH --partition=dgx
#SBATCH --gres=gpu:1
##SBATCH --partition=teton
##SBATCH --partition=moran
#SBATCH --time=150:00:00 
#SBATCH --export=ALL 
#SBATCH --mail-user=vvarenth@uwyo.edu 
#SBATCH --mail-type=START,END,FAIL 


source ~/.bashrc  # Reload the shell

# Activate the Conda environment
#conda activate /home/vvarenth/anaconda3/envs/openabc
conda activate /pfs/tc1/gscratch/vvarenth/Project/2024/Dielectric/Openmm/Models/openabc
which python3

## build
echo "system Build"
python3 build_sys.py

echo "Compress"
python3 compress.py

# run slab simulation
echo "Slab"
T=260
output_dcd=slab_${T}K.dcd
# python3 run_slab.py --temperature ${T} --box_a 25 --box_b 25 --box_c 400 --output_dcd ${output_dcd} --output_interval 20000 --steps 200000000

python3 run_slab.py --temperature ${T} --box_a 17 --box_b 17 --box_c 120 --output_dcd ${output_dcd} --output_interval 20000 --steps 100000000


# align slab trajectory so that the largest cluster is at the center of the box
# the aligned center of mass (COM) coordinates are saved in ${aligned_COM_traj_npy}
aligned_output_dcd=aligned_slab_${T}K.dcd
aligned_COM_traj_npy=aligned_COM_traj.npy
python3 align_slab_traj.py ${output_dcd} ${aligned_output_dcd} ${aligned_COM_traj_npy}

# compute density profile
# use the second half of the trajectory, which is of frame index 5000-9999
# use regime -10<=z<=10 to compute density
start_frame_id=2500
end_frame_id=4999
boundary=5
output_csv=slab_density_${T}K.csv
python3 compute_density.py ${aligned_COM_traj_npy} ${start_frame_id} ${end_frame_id} ${boundary} ${output_csv}

# draw density profile
mkdir -p pictures
output_plot=pictures/slab_density_${T}K.pdf
python3 draw_density.py ${output_csv} ${output_plot}

echo "job done"
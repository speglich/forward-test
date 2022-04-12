#!/bin/bash

module load python/3.9.6
module load gcc/11.1.0

export DEVITO_OPT=advanced
export DEVITO_LANGUAGE=openmp
export DEVITO_PLATFORM=skx
export OMP_NUM_THREADS=18
export OMP_PLACES="{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}"
export OMP_PROC_BIND=close
export DEVITO_LOGGING=WARNING

for blk_size in `seq 10 10 100`; do
    for repeat in `seq 0 2`; do
        time numactl --cpubind=0 --interleave=0 python forward.py $blk_size
    done
done


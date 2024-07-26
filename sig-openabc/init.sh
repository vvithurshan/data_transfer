for dir in */; do
    if [ -d "$dir" ]; then
        echo "$dir"
        cd $dir
        rm -rf *.npy
        rm -rf pictures
        rm -rf *.xml
        rm -rf *.dcd
        rm -rf *.csv
        rm -rf *out
        rm -rf *.pdb
        rm -rf *.png
        rm -rf *chk
        cp ../build_sys.py ./
        cd ../
    fi
done


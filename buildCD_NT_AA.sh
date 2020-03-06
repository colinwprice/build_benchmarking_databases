#!/bin/bash
CWD="$(pwd)"
echo "Getting relevant modules from Rivanna..."
module load anaconda
module load blast
echo "Moving genomes to current directory..."
python3 get_CD_NT_genomes.py
python3 get_AA_genomes.py
echo "Modifying fasta files..."
python3 mutate_kraken_fastas.py
#echo "Cloning kraken2 repository..."
#git clone https://github.com/DerrickWood/kraken2
#cd kraken2
#chmod u+x install_kraken2.sh
#echo "Installing the build programs..."
#./install_kraken2.sh programs
#cd programs
#cp -rn "$(pwd)"/* $CWD
#cd $CWD
#echo "Downloading taxonomy..."
#./kraken2-build --download-taxonomy --db custom_db_NT
#cd $CWD
#echo "Adding .fna files to NT library..."
#for f in Train_NT/*.fna2; do
#    ./kraken2-build --add-to-library $f --db custom_db_NT
#done
#echo "Building kraken2 NT database..."
#./kraken2-build --build --db custom_db_NT
#echo "Cleaning kraken2 NT database..."
#./kraken2-build --clean --db custom_db_NT
echo "Downloading taxonomy..."
./kraken2-build --download-taxonomy --db custom_db_CD
cd $CWD
echo "Adding .fna files to CD library..."
for f in Train_CD/*.fna2; do
    ./kraken2-build --add-to-library $f --db custom_db_CD
done
echo "Building kraken2 CD database..."
./kraken2-build --build --db custom_db_CD
echo "Cleaning kraken2 CD database..."
./kraken2-build --clean --db custom_db_CD
echo "Downloading taxonomy..."
./kraken2-build --download-taxonomy --db custom_db_AA
cd $CWD
echo "Adding .faa files to AA library.."
for f in Train_AA/*.faa2; do
    ./kraken2-build --add-to-library $f --db custom_db_AA
done
echo "Building kraken2 AA database..."
./kraken2-build --build --db custom_db_AA --protein
echo "Cleaning kraken2 AA database..."
./kraken2-build --clean --db custom_db_AA

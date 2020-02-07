#!/bin/bash
CWD="$(pwd)"
echo "Loading necessary modules from Rivanna..."
module load blast
echo "Cloning kraken2 repository..."
git clone https://github.com/DerrickWood/kraken2
cd kraken2
chmod u+x install_kraken2.sh
echo "Installing the build programs..."
./install_kraken2.sh programs
cd programs
cp -rn "$(pwd)"/* $CWD
cd $CWD
echo "Downloading taxonomy..."
./kraken2-build --download-taxonomy --db custom_db_NT
cd $CWD
echo "Adding .fna files to NT library..."
for f in Train_NT/*.fna; do
    ./kraken2-build --add-to-library $f --db custom_db_NT
done
echo "Building kraken2 NT database..."
./kraken2-build --build --db custom_db_NT
echo "Cleaning kraken2 NT database..."
./kraken2-build --clean --db custom_db_NT
echo "Downloading taxonomy..."
./kraken2-build --download-taxonomy --db custom_db_CD
cd $CWD
echo "Adding .fna files to CD library..."
for f in Train_CD/*.fna; do
    ./kraken2-build --add-to-library $f --db custom_db_CD
done
echo "Building kraken2 CD database..."
./kraken2-build --build --db custom_db_CD
echo "Cleaning kraken2 CD database..."
./kraken2-build --clean --db custom_db_CD

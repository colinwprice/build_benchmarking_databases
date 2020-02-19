#!/bin/bash
CWD="$(pwd)"
echo "Loading relevant modules from Rivanna..."
module load anaconda
module load blast
echo "Moving genomes to current directory..."
python3 get_AA_genomes.py
echo "Replacing headers with taxid..."
python3 mutate_kaiju_fastas.py
cd Train_AA
cat * > merged.faa
cd $CWD
echo "Installing kaiju programs..."
git clone https://github.com/bioinformatics-centre/kaiju.git
cd kaiju/src
make
cd $CWD
chmod u+x ./kaiju/bin/kaiju-mkbwt
chmod u+x ./kaiju/bin/kaiju-mkfmi
echo "Building kaiju database..."
./kaiju/bin/kaiju-mkbwt -n 5 -o proteins ./Train_AA/merged.faa
echo "Building kaiju fmi..."
./kaiju/bin/kaiju-mkfmi ./Train_AA/proteins

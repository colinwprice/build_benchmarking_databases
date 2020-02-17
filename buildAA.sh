#!/bin/bash
CWD="$(pwd)"
echo "Loading relevant modules from Rivanna..."
module load perl
module load gcc/5.4.0
module load gcc/6.5.0
module load pgi/19.10
module load pgi/19.7
module load gcc/7.1.0
module load gcc/system
module load intel/18.0
module load mvapich2/2.3.1
module load openmpi/3.1.4
module load intelmpi/18.0
module load python/3.6.6
module load blast
echo "Moving genomes to current directory..."
python3 get_AA_genomes.py
echo "Building virtual environment..."
virtualenv for_edirect
source ./for_edirect/bin/activate
yes n | sh -c "$(wget -q ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh -O -)"
mv ~/edirect/ $CWD
cd edirect
cp -rn "$(pwd)"/* $CWD
cd $CWD
echo "Replacing headers with taxid..."
for f in Train_AA/*.faa; do
    echo ---------------
    echo $f
    #extract assembly ID from file header (first character until 2nd underscore)
    assembly=$(echo $f | cut -c 10-24)
    echo $assembly
    #esearch assembly ID for Taxid
    TAXID=$(./esearch -db assembly -q $(echo $assembly) | ./esummary | ./xtract -pattern DocumentSummary -element Taxid)
    echo $TAXID
    #perl replace all lines starting with ">" with ">TAXID"
    perl -i -pe"s/>.*/>${TAXID}/gi" $f
done
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
./kaiju/bin/kaiju-mkfmi ./Train_AA/proteins

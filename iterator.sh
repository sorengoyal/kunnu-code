N=10
python random_generator.py $N > rand.dat
NUMLIST=`cat rand.dat`
for I in $NUMLIST
do
	echo "Computing for $I"
	python2.7 1material_wave.py $I
done	

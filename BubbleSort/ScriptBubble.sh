# !/bin/bash 

ls -at | grep result
ls -at | grep .info   

echo "Remove result + .info"
for j in $(seq 1 1 100)
do
  rm -f test$j.csv
  rm -f test$j.info
  rm -r result$j
  rm -f test$j
  rm -f recond$j.txt
done

rm -r result
rm -f *.txt
rm -f test.info
rm -f test.gcda
rm -f test.gcno

ls -at | grep result
ls -at | grep .info   

let i=0;

time=$(date "+%Y-%m-%d-%H:%M:%S");
echo "$time" >> recond.txt

for x in {1..10}
do
   for y in {1..10}
   do
     for z in {1..10}
     do
       # if (($x==$y))
       # then 
       #   continue
       # fi

       # if (($x==$z))
       # then 
       #   continue
       # fi

       # if (($y==$z))
       # then 
       #   continue
       # fi
	
       let i=$[$i+1]
       echo "......gcc......times:${i}"
       gcc -fprofile-arcs -ftest-coverage test.c -o test${i}
       echo "......process test$i...... times:${i}"
       ./test${i} ${x} ${y} ${z} >> recond.txt
       echo "......gcov test.c...... "
       gcov test.c
       echo "......lcov test${i}.info...... "
   
       #echo "$info_file_name"
       lcov -c -d . -o "test$i.csv" -b . 
       echo "......genhtml result${i}...... "
       genhtml -o result${i} test${i}.csv
       #sleep 5&
     done
   done
done
#ls -at | grep result
#ls -at | grep .csv 

  

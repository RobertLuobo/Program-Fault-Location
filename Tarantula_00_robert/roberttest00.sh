# !/bin/bash 

for i in {1..5}
do
   
   echo "......lcov test$i.info...... "
   touch "test$i.info"
  # echo "$info_file_name"
  rm -f test$i.info
  rm -r result$i
done
ls -at | grep .info | grep result




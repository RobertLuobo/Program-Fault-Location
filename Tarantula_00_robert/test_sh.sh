# !/bin/bash 

function mid_function()
{
  #echo "x=$1 y=$2 z=$3";  
  let x=$1;
  let y=$2;
  let z=$3;
  #echo "$x $y $z"

  let m=$z;

  if (($2<$3))
  then 
     if (($1<$2))
     then 
        let m=$y;
     elif(($1<$3))
     then
        let m=$y; #**bug** 
     fi

  elif(($1>$2))
  then
     if (($1>$2))
     then 
        let m=$y;
     elif(($1>$3))
     then
        let m=$x;  
     fi
  fi  
  echo "middle number is:$m" ; 
   
}

 

echo "mid_function start!";
aa=`date`
echo "$aa"
#read x y z;
mid_function $1 $2 $3;
echo "Code ending";
.shunit2

#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[])
{
  int x,y,z,m;
  x = atoi(argv[1]);
  y = atoi(argv[2]);
  z = atoi(argv[3]);
  printf(" %2d %2d %2d ",x,y,z);
  m = z;
  if( y < z )
  { 
    if( x < y )
      m = y;
    else if( x < z )
      m = y;//**bug**
   }
   else
   { 
     if( x > y )
       m = y;
     else if(x > z)
       m=x;
    }
   printf("Mid=%2d\r\n",m);
   return 0;
}
                                                                                                 

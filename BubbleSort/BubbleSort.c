#include<stdio.h>
#include<stdlib.h>

int main(int argc,char *argv[])
{
    int temp = 0;
    int OuterLoop = 1;
    int InnerLoop = 1;
    int len = 0;    

    for(int i=1;i<argc;i++)
    {
       argv[i] = atoi(argv[i]);
    }
    

    while(OuterLoop < argc)
    {
        InnerLoop = OuterLoop + 1;
        while(InnerLoop < argc)
        {
            if(argv[OuterLoop] < argv[InnerLoop]){
                temp = argv[InnerLoop];
                argv[OuterLoop] = argv[InnerLoop]; //error!!!! should be ==> array[InnerLoop] = array[OuterLoop]
                argv[InnerLoop] = temp;
            }
            InnerLoop=InnerLoop + 1;
        }

        OuterLoop = OuterLoop + 1;
    }

    // printf("BubbleSortResult:%d",argc);
    

    
    for(int i=1;i<argc;i++){     
      printf("%2d\n", argv[i]);
    }

    return 0;
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void bubble(char *,int);

int main(int argc,char *argv[])
{
    int count = 0;
    char s[256];

    printf("INPUT:");
    for(int i = 1;i < argc; i++)
 
    {
       s[i] = atoi(argv[i]);
       printf("%d ", s[i]); 
    }
    

    count = strlen(s) ;
    // printf("\ninput length is %d\n",count);
    bubble(s,count);

    printf("Sorted:");
    for(int i = 1; i < (count - 1) ; i++)
    {
       printf("%d ",s[i]);    
    }    
    printf("\n");
    return 0;
}

void bubble(char *s,int count)
{
    int a,b;
    char t;

    for(a=1;a<count;a++){
        for(b=count-1;b>=a;--b){
            if(s[b-1]>s[b]){
                t=s[b-1];
                s[b]=s[b-1];// Ture:s[b-1]=s[b];
                s[b]=t;
            }
        }
    }
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void bubble(char *,int);

int main(int argc,char *argv[])
{
    int count = 0;
    char s[40];
    // printf("%s\n", argv[0]); 
    // printf("参数的个数：%d\n", argc);
    printf("input string is:");

    for(int i=1;i<argc;i++)
    {
       s[i] = atoi(argv[i]);
       printf("%d ", s[i]);       
    }

    // printf("input string is %d",s);

    count =strlen(s);

    printf("\ninput length is %d\n",count-1);

    bubble(s,count);

    printf("sort string is :");
    for(int i=1;i<(count);i++)
    {
       printf("%d ",s[i]);    
    }    

    return 0;
}

void bubble(char * s,int count)
{
    int a,b;
    char t;

    for(a=1;a<(count);a++)
    {
        for(b=count-1;b>=a;--b){
            if(s[b-1]>s[b]){
                t=s[b-1];
                s[b-1]=s[b];// bug  // 正确的是：s[b-1]=s[b]
                s[b]=t;
            }
        }
    }

}

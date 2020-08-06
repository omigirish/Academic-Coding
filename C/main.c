
#include <stdio.h>
int fact(int n)
    {
        
        int i,fact=1;
        for(i=1;i<=n;i++)
        {
            fact*=i;
        }
        return fact;
    }
    int main()
    {
        int i,r,h,n,a,b,c,s;
        printf("Enter the power upto which Pascal Triangle is expected:\n ");
        scanf("%d",&n);
        printf("                               THE PASCAL'S TRIANGLE\n");
        for(int i=0;i<=n;i++)
        {
            for(s=1;s<=(40-2*i);s++){printf(" ");}
            a=fact(i);
            for(r=0;r<=i;r++)
            {
                b=fact(r);
                c=fact(i-r);
                h=a/(b*c);
                printf("%3d ",h);
            }
            printf("\n");
        }
        return 0;
    
    }



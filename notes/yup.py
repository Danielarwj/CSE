#include <stdio.h>
#include <stdlib.h>
int main()
    {
        int seed;
	puts("Money amount? ");
        canf("%d",&seed);
        srand(seed);
        for(int i=0;i<16;i++)
		{
			printf("%d\n",rand()%36+1);
			rand();
        }
        return 0;
    }
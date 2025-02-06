// Zoe Jimenez, Expression practice C

#include <stdio.h>
#include <math.h>

int equation1 = 7-24/8*4+6;
int equation2 = 18/3-7+2*5; 
int equation3 = 6*4/12+72/8-9;
int equation4 = (17-6/2)+4*3;
int equation5 = -2*(1*4-2/2)+(6+2-3);
int equation6 = -1*((3-4*7)/5)-2*24/6;
int equation7 = (3* pow(5,2) /15)-(5- pow(2,2));
int equation8 = ( pow(1,4) * pow(2,2) + pow(3,3))- pow(2,5) /4;
int equation9 = ( pow(22/2-2*5,2)) + (pow(4-6/6,2));

int main(void){
 printf("%d, %d, %d, %d, %d, %d\n", equation1, equation2, equation3, equation4, equation5, equation6);
printf("%d, %d, %d\n ", equation7, equation8, equation9);
    return 0;
}
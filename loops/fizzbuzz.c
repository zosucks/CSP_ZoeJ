// Zoe jimenez, FizzBuzz C
#include <stdio.h>




int main(void){


int x;

for(x=1;x<=50;x++){
     if(x % 5 == 0 && x % 3 == 0){
        printf("FizzBuzz\n");
    }else if(x % 5 == 0){
        printf("Buzz\n");
    }else if(x % 3 == 0){
        printf("Fizz\n");
    }else{
        printf("%d\n", x);
    }
}
}
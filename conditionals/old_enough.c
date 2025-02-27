// Zoe jimenez, Old enough C
#include <stdio.h>
#include <string.h>

int age;



int main(void){
    printf("Hello i will tell you if you are old enough!\n");
    printf("How old are you?\n");
    scanf("%d", &age);



   if(age >= 18){
        printf("You are old enough to vote.\n");
    }else if(age >= 16){
        printf("You are old enough to drive.\n");
    }else if(age >= 15){
        printf("You are old enough to get your learners permit.\n");
    }else if(age >= 6){
        printf("You are old enough to go to school.\n");
    }else{
        printf("Youre too young for anything!!!!\n");
    }
    
    return 0;
}
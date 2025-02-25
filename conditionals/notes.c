// Zoe jimenez, Conditionals Notes C

#include <stdio.h>
#include <string.h> //Needed to compare strings
char name[]= "Treyson";
int num;


int main(void){
//How do you write an if statement in C?
if(strcmp(name,"Vienna") == 0){ //strcmp means string comparision when the outcome is 0 the strings are the same
    printf("Hello Ms. Larose, welcome to class");
//how do you write else statements in C?

}else{
    printf("Hello %s, welcome to class.\n", name);
}

//printf("How old are you?\n");
printf("how many siblings do you have?\n");
scanf("%d", &num); //numberds must always have the &
//How do you write elif/ else if statements in C?
if(num == 0){
    printf("You are a only child.\n");
}else if(num <= 2){
    printf("You have a couple of siblings.\n");
}else if(num <= 5){
    printf("You have a few siblings\n");
}else{
    printf("You have a lot of siblings\n");
}


//How do you write the 3 logical operators in C?
// && = and
// || = or
// ! = not
if(num == 7 || num == 13){
    printf("Thats is an unlucky number\n");
}else if(num <10 && num >5){
    printf("%d is a large single digit number\n", num);
}else if(!(num > 10)){
    if(num == 12){
        printf("Thats a dozen, exactly!\n");
    }
    printf("Thats a big number\n");
}else{
    printf("You typed a %d\n", num);
}
    
    return 0;
}
// Zoe jimenez, Function Notes C
#include <stdio.h>
int num;
char name[50], place[50], verb[50];
int add(int numOne, int numTwo){
    return numOne + numTwo;

}
void due(char assignment[50], char day[20]){
    printf("The %s assignment is due %s", assignment, day);
}

const char* word(char type[50]){
    char choice[50];
    printf("Please give me a %s: \n", type);
    scanf("%s", choice);
    return choice;


}


int main(void){
    //printf("Please tell me a number: \n");
    //scanf("%d", num);
    //add(num,1);
    //add(8,1);
    //add(72,1);
    //printf("%d",add);
    due("Functions notes", "Today");
    due("Hello world update", "Tommorrow");
    due("Fincanial calculator Update", "Friday");



    return 0;
}

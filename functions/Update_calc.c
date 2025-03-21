// Zoe jimenez, Financial Calculator UPDATE C 

#include <stdio.h>
#include <math.h>

char name [250];
float user_input(char*question){
    float value;
    printf("%s", question);
    scanf("%f", &value);
    return value;
}
void calculation(char*item_name, float number, float income){
    float percentage = (number/income)*100;
    printf("%s, your monthly %s is $%.2f which is %.2f%% of your income!\n", name, item_name, number, percentage);
}
int main(void){
    float income, rent, utilities, groceries, transportation, savings, spendings;

    income = user_input("What is your income?: \n");
    rent = user_input("What is your rent?: \n");
    utilities = user_input("How much do your utilities cost?: \n");
    groceries = user_input("How much do your groceries cost?: \n");
    transportation = user_input("How much does transportation cost?: \n");
   
    savings = income*0.1;
    spendings = income-savings-rent-utilities-groceries-transportation;

    calculation("rent", rent, income);
    calculation("utilities", utilities, income);
    calculation("groceries", groceries, income);
    calculation("transportation", transportation, income);
    calculation("savings", savings, income);
    calculation("spendings", spendings, income);
   
    return 0;
}
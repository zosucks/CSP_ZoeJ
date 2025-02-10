// Zoe jimenez, Financial Calculator C

#include <stdio.h>
#include <math.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;

int main(void){
    // print statment that welcomes user and tells what this program does
    printf("Hello user! This is a financial calculator for you and your money!\n");
// ask what their monthly income is (variable an input)
printf("What is your income?: \n");
scanf("%f", income);
// ask what their rent is (variable an input)
printf("What is your rent?: \n");
scanf("%f", rent);
// ask what their utilities cost is (variable an input)
printf("What is your utilities?: \n");
scanf("%f", utilities);
// ask what their  grocories cost is (variable an input)
printf("What is your groceries?: \n");
scanf("%f", groceries);
// ask what their transportation cost is (variable an input)
printf("What is your transportation?: \n");
scanf("%f", transportation);
//savings = income - rent - groceries - utilities - transportation
savings = income-rent-utilities-groceries-transportation;


float rents;
float utilitie;
float grocerie;
float transportations;
float spending;
float saving;


// calculate savings as 10% of income (income * .1) (a variable)
saving = income*.1;
// calculate percent income of rent (rent/income * 100) (variable)
rents = (rent/income)*100;
// calculate percent income of utilities (utilities/income * 100) (variable)
utilitie = (utilities/income)*100;
// calculate percent income of groceries (groceries/income * 100) (variable)
grocerie = (groceries/income)*100;
// calculate percent income of transportation (transportation/income * 100) (variable)
transportations = (transportation/income)*100;


printf("Your rent is %f, which is %f % of your income. \n", rent, rents);
printf("Your utilities is %f, which is %f % of your income. \n", utilities, utilitie);
printf("Your groceries is %f, which is %f % of your income. \n", groceries, grocerie);
printf("Your transportations is %f, which is %f % of your income. \n", transportation, transportations);
printf("Your savings is %f, which is %f % of your income. \n", savings, saving);
    return 0;
}



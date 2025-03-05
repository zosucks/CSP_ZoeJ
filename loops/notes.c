// Zoe Jimenez, Loop notes C

#include <stdio.h>


int main(void){
// While loop
int start = 0;
while(start<5){
    printf("Hello!\n");
    start++;
}
//For loops
int q;
for(q=0;q<5;q++){
    printf("%d\n", q);
}
// What are arrays(lists)
    // an array is a varibale that holds multiple values

// How do you make them?
//array all need to be the same data type!
int grades[] = {88, 97, 100, 70, 72, 99, 89};
// 1. set the data type
// 2. AFTER naming put brackets and write the length of the list
// 3. List is surrounded by curly brackets {}
// 4. Commas, between each items

printf("CSP grade: %d\n", grades[2]);
//change an item in the array
grades[2] = 95;
printf("New CSP grade: %d\n", grades[2]);

//size of list in bytes
int size = sizeof(grades);
// length in list items
int length = sizeof(grades)/sizeof(grades[0]);
printf("The array is %d items long\n", length);

//array with strings
// first brackets sets the length of the array
// second bracket sets length of each string
char movies[][20] = {"Cars", "Treasure Planet", "An American Tale", "Marley and Me", "The Avengers"};
printf("The movie is %s!\n", movies[1]);
int mlength = sizeof(movies)/sizeof(movies[0]);
// How to make a FOR loop in C
// set the iterator, keeps track of times through the loop (best practice to set x or i)
int x;
// in parens (starting point; ending point; count by)
for(x=0;x<=10;x++){
    printf("%d\n", x);
}

int m;
for(m=0;m<mlength;m++){
    printf("%s\n", movies[m]);
}

//How to make a WHILE loop
int w = 100; // start point

while(w>=0){ // stop point
    printf("%d\n", w);
    w -= 10; // what you count by
}


    return 0;
}


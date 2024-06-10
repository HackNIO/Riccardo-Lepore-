#include <stdio.h>
#define PI =3.14

int main ()
{
double raggio;
double area;

printf("Inserisci il raggio del cerchio: "); 
scanf("%lf", &raggio);

area = 3.14*raggio*raggio;

printf("L'area del cerchio è: %.2lf\n", area);

return 0;

}
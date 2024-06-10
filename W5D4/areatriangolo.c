#include <stdio.h>
#include <math.h>

int main() {
double D, area;

printf("Inserisci il lato del triangolo equilatero: ");
scanf("%lf", &D);
area = (sqrt(3) / 4) * D * D;
printf("L'area del triangolo equilatero è: %lf\n", area);

return 0;

    }
    
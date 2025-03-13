//7. Calculeaza o valoare aproximativa a radacinii patrate a unui numar real pozitiv, cu o precizie data.

#include <stdio.h>
#include <assert.h>
#include <math.h>


float babiloniana(float n, float e) {

	//functia returneaza radacina patrata aproximativa a numarului float (n) si precizia float(e)
	//Date de intrare
	// n, e - float, numere pozitive reale
	//Date de iesire
	// Radacina patrata aproximativa
	float x0 = n / 2;
	float x1 = (x0 + n / x0) / 2;
	while (fabs(x1 - x0) > e) {
		x0 = x1;
		x1 = (x0 + n / x0) / 2;
	}

	return x1;
}




void test_all() {






	for (int n = 1; n <= 10000	; n++) 
		for (int e = 1; e <= 100000; e=e*5) {
			float prec = 1.0 / e;
		
			assert(fabs(babiloniana(n, prec) - sqrt(n)) <= prec);

	}
	printf("toate testele au trecut cu succes\n");






}






int main() {



	test_all();




	float n, e;
	printf("Introduceti numarul n: ");
	if (scanf_s("%f", &n) != 1) {
		printf("Nu ati introdus un numar real pozitiv.");
		return 1;
	}
	printf("Introduceti precizia e: ");
	if (scanf_s("%f", &e) != 1) {
		printf("Nu ati introdus un numar real pozitiv.");
		return 1;
	}


	float rez = babiloniana(n, e);



	printf("Radacina patrata a numarului %f este aproximativ %f", n, rez);
	return 0;
}
#include <stdio.h>
#


int* NumerePare(int nr, int v[]) {




	return v;
}

void Run() {
	while (1) {
		char opt;

		printf("1.Numere Pare\n2.Afuera\nIntrodu boss\n\n=>");

		if (scanf_s(" %c", &opt, sizeof(opt)) != 1) {
			printf("Invalid input\n");
			return;
		}

		switch (opt) {
		case '1':
			
			NumerePare();
			break;

		case '2':
			return;
		}

		printf("\n\n");
	}
	};

int main() {


	Run();





	return 0;
}
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>



pid_t fiu[3];

void f(int sgn){
	printf("primit semnal %d\n",sgn);
	for(int i=0;i<3;i++){
		kill(fiu[i],SIGUSR2);}
	exit(0);
}

void g(int sgn){
	print("Fiul a primit semnalul %d\n",sgn);
	exit(0);}


int main(){
	int i;
	signal(SIGUSR1,f);
	for(i=0;i<3;i++){
		fiu[i]=fork();
		if(fiu[i]==0){
	while(1);
	exit(0);}}

	for(i=0;i<3;i++){
		wait(0);
	}

	return 0;
}

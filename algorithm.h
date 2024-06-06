#include <stdio.h>
#include <stdlib.h>

double C_mean(double* arr, int n){
	double res = 0;
	for(int i = 0; i < n; i++)res += arr[i];
	return res/n;
}

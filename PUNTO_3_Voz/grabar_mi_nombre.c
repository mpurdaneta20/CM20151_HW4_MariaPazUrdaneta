#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
/*
Comienza a grabar y el usuario tiene 10 segundos para grabar su nombre
*/
system("timeout 5 rec -c 1 -b 16 nombre.wav ");

return 0;
}



#include<stdio.h>
#include<stdlib.h>
#define MAX 26
/*descubrí algo que no tiene nada que ver Ctrl+g hac que se habra command palette, aunque puedes habrirla con menú, view, y ahí aparece*/

int size_of_word;

void enqueueFront(char *, char, int *, int *);
//void enqueueRear(char *, char, int *, int *);
char dequeueFront(char *, int *, int *);
char dequeueRear(char *, int *, int *);
int contador_de_letras(char *);
int count(char *);
void display(char *);
//algún día confirmaremos si necesito colocar la declaración de funciones en algún orden específico

void enqueueFront(char *arr, char item, int *front, int *rear)
{
    int i, k, c;

    if(*front==0 && (*rear)==(size_of_word-1)) 
    {
        printf("\nFalló, deque esta llena.\n");
        return;
    }

    if(*front==-1)
    {
        //solo entra una vez y es en la primera vez
        *front=*rear=0;
        arr[*front]=item;
        return;
    }

    if(*rear!=(size_of_word-1))
    {
        c=count(arr);
        k=*rear+1;

        for(i=1; i<=c; i++)
        {
            arr[k]=arr[k-1];
            k--;
        }
        arr[k]=item;
        *front=k;
        (*rear)++;
    } 
    else
    {
        (*front)--;
        arr[*front]=item;
    }
}


char dequeueFront(char *arr, int *front, int *rear) 
{
    int item;

    if(*front==-1) 
    {
        printf("\nFalló, la double queue (deque) esta vacia.\n");
        return 0;
    }

    item=arr[*front];
    arr[*front]=' ';

    if(*front==*rear)
        *front=*rear=-1;
    else
        (*front)++;

    return item;
}

char dequeueRear(char *arr, int *front, int *rear)
{
    int item;

    if(*front==-1)
    {
        printf("\nFalló, deque esta vacía.\n");
        return 0;
    }

    item=arr[*rear];
    arr[*rear]=' ';
    (*rear)--;

    if(*rear==-1)
        *front=-1;

    return item;
}

int contador_de_letras(char *arr)
{
    int c=0, i;
    for(i=0; i<MAX; i++)
    {
        if(arr[i]!=(' '))
        {
            c++;
        }
    }
    
    return c;
}

int count(char *arr)//devuelve cuantos luagres hay ocupados
//entre los muchos errores que he cometido es no inicializar el arreglo/cola
{
    int c=0, i;

    for(i=0; i<size_of_word; i++)
    {
        if(arr[i]!=' ')
            c++;
    }
    return c;
}

void display(char *arr)
{
    int i;

    printf("\n\trente:\t");
    for(i=0; i<size_of_word; i++)
        printf("  %c", arr[i]);
    printf("\t:parte trasera\n");
}

int main()
{
    char palabra[MAX];
    char *array;
    int i;
    int front, rear;
    char comparar1, comparar2;

    front=rear=-1;

    for(i=0;i<MAX;++i)
        palabra[i]=' ';

    printf("Bienvenido al verificador de palabras palíndromas\n");
    printf("Ingresa una palabra, todas en minúsculas o todas en mayúsculas, de máximo 25 caracteres\n");
    printf("Si es más de una palabra, no ingrese espacio: ");
    scanf("%s", palabra);
    size_of_word=contador_de_letras(palabra)-1;
    printf("La longitud de la palabra es de: %d", size_of_word);

    array=(char*)malloc((size_of_word)*sizeof(char));
    if(array)//es lo mismo que array!=NULL
    {
        for(i=0;i<size_of_word;++i)
            array[i]=' ';

        for(i=(size_of_word-1);i>=0;i--)
        {
            enqueueFront(array, palabra[i], &front, &rear);
        }
        /*es esencialmente lo mismo que display
        for(i=0;i<size_of_word;i++)
        {
            printf("\narray[%d]=%c", i, *(array+i));
        }*/
        display(array);

        //no necesito averiguar si es impar, por que si no es impar, me redondea pa' abajo, eso me beneficia, por que justo hasta ahí comparten el mismo c+odigo impares y pares, pero ya después lo impares tienen un proceso más
        for(i=0;i<(size_of_word/2);++i)//el número de comparaciones es la mitad del número de letras
        {
            comparar1=dequeueFront(array, &front, &rear);//en una cola normal o en una cola doble es normal quitar de front
            comparar2=dequeueRear(array, &front, &rear);
            if(comparar1!=comparar2)//si no entra simplemente continua
            {
                printf("La palabra no es palíndroma.\n");
                printf("Encontramos al menos un error: ");
                printf("Las letras %c y %c de tu palara no coinciden\n", comparar1, comparar2);
                printf("Podría haber más errores o no.\n");
                return 1;
            }
        }
            printf("La palabra es palíndroma");//nunca encontró un error
        else/*es impar, el problema es que cada vez de dequeues quitas, por lo que si el de en medio lo quitas con por ejmeplo dqueueFront, el deuqueRear lo va a identificar como vacía ya no tendrá que quitar*/
        {

        }
        free(array);
    }
    //confío en mi variable size_of_word
    return 0;
}

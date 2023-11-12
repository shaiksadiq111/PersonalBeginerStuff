#include <pthread.h>
#include <stdio.h>
#include <unistd.h>


int Sempahore  = 1;
int readerCount = 0;
int turn; //1 for writer and 0 for reader

void wait(){
    while(Sempahore <= 0){
        //do nothing 
    };

    Sempahore--;

}


void signal(){
    Sempahore++;
}

void writerFunction(){
    wait();
    turn = 1;
    // printf("the value of semaphore is %d\n", Sempahore);
    printf("we are inside writer function\n");
    printf("exiting writer\n");
    sleep(5);
    
    signal();
}


void *readerFunction(void * arg){
    if(turn == 1){
        wait();
    }
    turn = 0;
    readerCount++;
    // printf("the value of semaphore is %d\n", Sempahore);
    printf("We are inside reader function\n");
    printf("number of readers are %d\n", readerCount);
    printf("exiting reader function\n");
    sleep(10);
    
    readerCount--;
    signal();
    return NULL;
}

int main(){
    

    pthread_t reader_id1, reader_id2, reader_id3, reader_id4, reader_id5;
    pthread_t writer_id;

    pthread_create(&reader_id1, NULL, (void *)readerFunction, NULL);
    writerFunction();
    pthread_create(&reader_id2, NULL, (void *)readerFunction, NULL);
    pthread_create(&reader_id3, NULL, (void *)readerFunction, NULL);
    writerFunction();
    pthread_create(&reader_id4, NULL, (void *)readerFunction, NULL);
    pthread_create(&reader_id5, NULL, (void *)readerFunction, NULL);
    
    writerFunction();

    pthread_join(&reader_id5, NULL);
    return 0;
}
#include <iostream>
using namespace std;

//in this programm we are implementing sjf (non-pre-emptive)

int currentTime = 0;

class Process{
    public:
    int arrivalTime;
    int cpuBursts;
    int IOBurst;
    int IOInterval;
    int pid;
    int completed = 0; // 0 means not done 1 means done

    Process(int pidx, int arrivalTimex, int cpuBurstsx, int IOBurstx, int IOInteralx);
    int getArrivaltime();
    void startJob();

    int turnAroundTime;
    int waitingTime;
    int ResponseTime;

};

Process :: Process(int pidx, int arrivalTimex, int cpuBurstsx, int IOBurstx, int IOInteralx){
    pid = pidx;
    arrivalTime = arrivalTimex;
    cpuBursts = cpuBurstsx;
    IOBurst = IOBurstx;
    IOInterval = IOInteralx;

    // cout << arrivalTime <<endl;
};

int Process :: getArrivaltime(){
    return this->arrivalTime;
}

void Process :: startJob(){
    waitingTime = currentTime;

    int completeFractionalBurts = cpuBursts/IOInterval;
    int timeRequired = 0;
    timeRequired = timeRequired +  completeFractionalBurts*IOBurst;
    timeRequired = timeRequired + completeFractionalBurts*IOInterval;
    int remainingTime = cpuBursts - completeFractionalBurts*IOInterval;
    timeRequired = timeRequired + remainingTime;
    currentTime = currentTime + timeRequired;
    completed = 1;
    turnAroundTime = currentTime - arrivalTime;
    cout <<"P" << pid << ";" << waitingTime << ";" << turnAroundTime <<endl;
    



}

int findSmallestIndex(int* array, int n){
    int current = array[0];
    int index = 0;
    for(int i = 0; i < n - 1; i++){
        if(current > array[i + 1]){
            current = array[i+1];
            index = i + 1;
        }
    }

    return index;
}

Process* PickShortestJob(Process* array[], int  n){
    Process* possibleJobs[n];
    int possibleJobsTime[n];
    int index = 0;

    for(int i = 0; i < n; i++){
       int arrival = array[i]->getArrivaltime();
       int completed = array[i]->completed;

       if(completed == 0){
           if(arrival <= currentTime){
               // it is a possible candidate for shortest job
               possibleJobs[index] = array[i];
               possibleJobsTime[index] = array[i]->cpuBursts;
               index++;
           }
       }

    }

    if(index == 0){
        return nullptr;
    }
    else{
        int smallestJob = findSmallestIndex(possibleJobsTime, index);
        return possibleJobs[smallestJob];
    };
}



void SJFAlgorithm(Process* array[], int n){
    int flag = 1;
    while(flag){
        Process* toExecute = PickShortestJob(array, n);
        if(toExecute == nullptr){
            flag = 0;
            break;
        }
        else{
            toExecute->startJob();

        }


    }

}


int main(){
    Process P0 = Process(0,0,24,2,5);
    Process P1 = Process(1, 3,17,3,6);
    Process P2 = Process(2,8,50,2,5);
    Process P3 = Process(3,15,10,3,6);

    Process* array[4] = {&P0, &P1, &P2, &P3};

    SJFAlgorithm(array, 4);

    // PickShortestJob(array, 4);


    
    return 0;
}
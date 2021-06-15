#include <bits/stdc++.h>
#include <iostream>

using namespace std;

const int sizen = 1000;
const int MAX_THREAD=4;
int part = 0;

long long costMatrixA[sizen][sizen];
long long costMatrixB[sizen][sizen];


long long productMat[sizen][sizen];

long long filterArray[4][sizen];
long long finalMat[sizen /4];


void* multi(void*)
{
    int core = part++;
  
    // Each thread computes 1/4th of matrix multiplication
    for (int i = core * sizen / 4; i < (core + 1) * sizen / 4; i++) 
        for (int k = 0; k < sizen; k++) 
            for (int j = 0; j < sizen; j++) 
                {
                productMat[i][j] += costMatrixA[i][k] * costMatrixB[k][j];
                }
    
    return NULL;
}

int main()
{
    if(sizen%4!=0)
    {
        cout<<"Size of matrix should be a multiple of 4";
        return 0;
    }
    int i, j, k;
    srand(time(0));

    // Initialisation
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            costMatrixA[i][j] = 1 + rand() % 10;
            costMatrixB[i][j] = 1 + rand() % 10;
            productMat[i][j] = 0;
        }
    }

    // Replacing each element of both matrix with the expected cost (max for B and min for A) to reach n,n
    for(int i=sizen-2;i>=0;i--)
    {
        costMatrixA[i][sizen-1]+=costMatrixA[(i+1)][sizen-1];
        costMatrixB[i][sizen-1]+=costMatrixB[(i+1)][sizen-1];

        costMatrixA[sizen-1][i]+=costMatrixA[sizen-1][(i+1)];
        costMatrixB[sizen-1][i]+=costMatrixB[sizen-1][(i+1)];
    }

    for (int i=sizen-2;i>=0;i--)
    {
        for (int j=sizen-2;j>=0;j--)
        {
            costMatrixA[i][j]+=min(costMatrixA[i+1][j],costMatrixA[i][j+1]);
            costMatrixB[i][j]+=max(costMatrixB[i+1][j],costMatrixB[i][j+1]);
        }
    }


    // declaring four threads
    pthread_t threads[MAX_THREAD];
  
    // Creating four threads, each evaluating its own part
    for (int i = 0; i < MAX_THREAD; i++) 
    {
        pthread_create(&threads[i], NULL, multi, NULL);
    }
  
    // joining and waiting for all threads to complete
    for (int i = 0; i < MAX_THREAD; i++) 
    {
        pthread_join(threads[i], NULL);
    }

    //filter of size 4 x n
    
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < sizen; j++)
            filterArray[i][j] = rand() % 2;
    }
    // matrix of dimension (sizen/c) x 1 where c = 4
    
    // applying the filter
    for (i = 0; i <= sizen - 4; i += 4)
    {
        long long sum = 0;
        // dot product of 4xn portion of productMat
        for (j = 0; j < sizen; j++)
        {
            for (int filterRow = 0; filterRow < 4; filterRow++)
            {
                sum += productMat[i + filterRow][j]*filterArray[filterRow][j];
            }
        }
        finalMat[i / 4] = sum;
    }

    return 0;

}
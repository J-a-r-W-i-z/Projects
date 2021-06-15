
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

const int sizen = 1000;

long long costMatrixA[sizen][sizen];
long long costMatrixB[sizen][sizen];

long long productMat[sizen][sizen];

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


    //creating productMat as explained in the beginning
    for (i = 0; i < sizen; i++)
    {
        for (k = 0; k < sizen; k++)
        {
            for (j = 0; j < sizen; j++)
                productMat[i][j] += costMatrixA[i][k]*costMatrixB[k][j];
        }
    }


    //filter of size 4 x n
    long long filterArray[4][sizen];
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < sizen; j++)
            filterArray[i][j] = rand() % 2;
    }
    // matrix of dimension (sizen/c) x 1 where c = 4
    long long finalMat[sizen /4];
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
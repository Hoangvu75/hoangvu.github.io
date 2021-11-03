#include <iostream>
#include <time.h> 
using namespace std;
#include<sstream>

int main()
{
    int row;
    int fakerow;
    int column;
    int fakecolumn;
    int bombnumber;
    cout << "Number of row : " << endl;
    cin >> fakerow;
    row = fakerow + 1;
    cout << "Number of column : " << endl;
    cin >> fakecolumn;
    column = fakecolumn + 1;
    cout << "Number of bomb : " << endl;
    cin >> bombnumber;
    
    int matrix[row][column];
    
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {
            matrix[i][j] = 0;
        }
    }

    srand(time(NULL));
    for (int b = 0; b < bombnumber; b++)
    {
        int i;
        int j;
        i = 0 + rand()%(-0+row-2+1);
        j = 0 + rand()%(-0+column-2+1);
        if (matrix[i][j] == 0)
        {
            matrix[i][j] = -1;  
        }
        else if (matrix[i][j+1] == 0)
        {
            matrix[i][j+1] = -1;
        }
        else if (matrix[i-1][j+1] == 0)
        {
            matrix[i-1][j+1] = -1;
        }
        else if (matrix[i-1][j] == 0)
        {
            matrix[i-1][j] = -1;
        }
        else if (matrix[i-1][j-1] == 0)
        {
            matrix[i-1][j-1] = -1;
        }
        else if (matrix[i][j-1] == 0)
        {
            matrix[i][j-1] = -1;
        }
        else if (matrix[i+1][j-1] == 0)
        {
            matrix[i+1][j-1] = -1;
        }
        else if (matrix[i+1][j] == 0)
        {
            matrix[i+1][j] = -1;
        }
        else if (matrix[i+1][j+1] == 0)
        {
            matrix[i+1][j+1] = -1;
        }
    }
    
    
    for (int i = 0; i < row-1; i++)
    {
        for (int j = 0; j < column-1; j++)
        {
            if (matrix[i][j] == -1) 
            {
                if (matrix[i][j+1] != -1)
                {
                    matrix[i][j+1] = matrix[i][j+1] + 1;
                }
                if (matrix[i-1][j+1] != -1)
                {
                    matrix[i-1][j+1] = matrix[i-1][j+1] + 1;
                }
                if (matrix[i-1][j] != -1)
                {
                    matrix[i-1][j] = matrix[i-1][j] + 1;
                }
                if (matrix[i-1][j-1] != -1)
                {
                    matrix[i-1][j-1] = matrix[i-1][j-1] + 1;
                }
                if (matrix[i][j-1] != -1)
                {
                    matrix[i][j-1] = matrix[i][j-1] + 1;
                }
                if (matrix[i+1][j-1] != -1)
                {
                    matrix[i+1][j-1] = matrix[i+1][j-1] + 1;
                }
                if (matrix[i+1][j] != -1)
                {
                    matrix[i+1][j] = matrix[i+1][j] + 1;
                }
                if (matrix[i+1][j+1] != -1)
                {
                    matrix[i+1][j+1] = matrix[i+1][j+1] + 1;
                }
            }
        }
    }

    string fakematrix[row][column];

    for (int i = 0; i < row-1; i++)
    {
        for (int j = 0; j < column-1; j++)
        {
            stringstream ss;
            ss << matrix[i][j];
            string str = ss.str();
            if (str == "-1")
            {
                fakematrix[i][j] = "B";
            }
            else
            {
                fakematrix[i][j] = str;
            }
        }
    }
    
    cout << "" << endl;
    cout << "uncensored" << endl;
    for (int i = 0; i < row-1; i++)
    {
        for (int j = 0; j < column-1; j++)
        {
            cout << fakematrix[i][j] << " ";
        }
        cout << "" << endl;
    }
    
    string grid[row][column];
    
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {
            grid[i][j] = "X";
        }
    }
    
    cout << "" << endl;
    cout<< "censored" <<endl;
    for (int i = 0; i < row-1; i++)
    {
        for (int j = 0; j < column-1; j++)
        {
            cout << grid[i][j] << " ";
        }
        cout << "" << endl;
    }

    cout << "------------------------------------" << endl;
    
    for (int i = 0; i < (row-1)*(column-1); i++)
    {
        int r;
        int c;
        cout << "Enter row ( 0 -> row - 1 ) and column ( 0 -> column - 1 )" << endl;
        cin >> r >> c;    
        grid[r][c] = fakematrix[r][c];
        if (grid[r][c] == "B")
        {
            cout << "you lose" << endl;
        }
        cout << "" << endl;
        if (grid[r][c] != "B")
        {
            for (int m = 0; m < row-1; m++)
            {
                for (int n = 0; n < column-1; n++)
                {
                    cout << grid[m][n] << " ";
                }
                cout << "" << endl;
            }
            cout << "" << endl;
        }
    }   
    
    return 0;
}
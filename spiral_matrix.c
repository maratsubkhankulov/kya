#include <stdio.h>

void square_matrix_print(int arr[3][3], int size)
{
    int i, row = 0, col = 0, row_end = size - 1, col_end = size - 1;

    while (row <= row_end && col <= col_end )
    {
        for (i = col; i <= col_end; i++)
            printf("%d ", arr[row][i]);

        row++;
        i = row;
        for (; i <= row_end; i++)
            printf("%d ", arr[i][col_end]);

        col_end--;
        i = col_end;
        for (; i >= col; i--)
            printf("%d ", arr[row_end][i]);

        row_end--;
        i = row_end;
        for (; i >= row; i--)
            printf("%d ", arr[i][col]);
        col++;
    }
    printf("\n");
}

int main()
{
    int arr[3][3] = { {1,2,3}, {4,5,6}, {7,8,9} };

    square_matrix_print(arr, 3);
}

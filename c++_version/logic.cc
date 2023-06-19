#include<iostream>
#include<vector>
#include<random>

using namespace std;

typedef vector< vector< int>> Matrix;

void print_matrix(const Matrix& m) {
    int rows = m.size();

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < rows; ++j) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}



pair<int, int> count_around(const Matrix& matrix, int i, int j) {
    int total_a = 0, total_b = 0;
    int row_count = matrix.size();

    if (i > 0 and j > 0){
        if (matrix[i-1][j-1] == 1) total_a++;
        else if (matrix[i-1][j-1] == 2) total_b++;
    }

    if (i > 0){
        if (matrix[i-1][j] == 1) total_a++;
        else if (matrix[i-1][j] == 2) total_b++;
    } 

    if (i > 0 and j < (row_count-1)) {
        if (matrix[i-1][j+1] == 1) total_a++;
        else if (matrix[i-1][j+1] == 2) total_b++;

    }

    if (i < (row_count-1)) {
        if (matrix[i][j+1] == 1) total_a++;
        else if (matrix[i][j+1] == 2) total_b++;
    }

    if (i < (row_count-1) and j < (row_count-1)) {
        if (matrix[i+1][j+1] == 1) total_a++;
        else if (matrix[i+1][j+1] == 2) total_b++;
    }

    if (i < (row_count-1)) {
        if (matrix[i+1][j] == 1) total_a++;
        else if (matrix[i+1][j] == 2) total_b++;
    }

    if (i < (row_count-1) and j > 0) {
        if (matrix[i+1][j-1] == 1) total_a++;
        else if (matrix[i+1][j-1] == 2) total_b++;
    }

    if (j > 0) {
        if (matrix[i][j-1] == 1) total_a++;
        else if (matrix[i][j-1] == 2) total_b++;
    }

    return make_pair(total_a, total_b);
}

void update_cells(Matrix& matrix) {

    int row_count = matrix.size();

    vector< vector <int>> new_matrix = matrix;

    std::random_device rd;
    std::mt19937_64 gen(rd());

    uniform_int_distribution<int> distribution(1, 100);

    for (int i = 0; i < row_count; ++i) {
        for (int j = 0; j < row_count; ++j) {
            pair<int, int> p = count_around(matrix, i, j);

            if (matrix[i][j] == 1) {
                if (p.second > p.first) {
                    new_matrix[i][j] = 2;
                }

                else {
                    int randomNumber = distribution(gen);                

                    if (randomNumber > 85) {
                        new_matrix[i][j] = 0;
                    }
                }
            }

            else if (matrix[i][j] == 2) {
                if (p.first > p.second) new_matrix[i][j] = 1;
                else {
                    int randomNumber = distribution(gen);                
                    
                    if (randomNumber > 85) new_matrix[i][j] = 0;
                }
            }

            else {
                if (p.first > p.second) new_matrix[i][j] = 1;
                if (p.second > p.first) new_matrix[i][j] = 2;
            }
        }
    }

    matrix = new_matrix;
}

int check_winnage(const Matrix& matrix) {
    bool team_a = true, team_b = true;
    int row_count = matrix.size();

    for (int i = 0; i < row_count; ++i) {
        for (int j = 0; j < row_count; ++j) {
            if (matrix[i][j] == team_a) team_b = false;
            else if (matrix[i][j] == team_b) team_a = false;

            if (not team_b and not team_a) return 0;
        }
    }

    if (team_a and not team_b) return 1;
    else if (team_b and not team_a) return 2;
    else return 3;
}

Matrix generate_random(int rows) {
    vector< vector <int>> new_matrix(rows, vector<int>(rows, 0));
    std::random_device rd;
    std::mt19937_64 gen(rd());

    uniform_int_distribution<int> distribution(0, 2);

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < rows; ++j) {
            new_matrix[i][j] = distribution(gen);
        }
    }

    return new_matrix;
}
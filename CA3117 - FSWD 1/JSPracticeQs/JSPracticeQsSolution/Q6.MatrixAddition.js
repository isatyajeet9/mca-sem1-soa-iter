// Q6: Matrix Addition using forEach

let A = [[1, 2], [3, 4]];
let B = [[5, 6], [7, 8]];
let C = [];

A.forEach((row, i) => {
    C[i] = [];
    row.forEach((value, j) => {
        C[i][j] = value + B[i][j];
    });
});

console.log("Matrix A:", A);
console.log("Matrix B:", B);
console.log("Result (A + B):", C);

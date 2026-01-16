// Q3: Factorial using Recursion

function factorial(n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

let num = 5;
console.log("Factorial of " + num + " is " + factorial(num));

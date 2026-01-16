// Q4: Prime Numbers from 51 to 120

let primes = "";

for (let n = 51; n <= 120; n++) {
    let count = 0;

    for (let i = 1; i <= n; i++) {
        if (n % i == 0) 
            count++;
    }

    if (count == 2) 
        primes += n + " ";
}

console.log("Prime Numbers (51-120):", primes);


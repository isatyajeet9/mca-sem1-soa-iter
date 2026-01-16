// Q2: Array Operations (push, pop, shift, unshift, splice)

let DU23 = [14, 56, 15, 72, 11, 23, 40, 35];

DU23.push(11, 22, 65);
DU23.unshift(91, 28, 44);
DU23.pop();
DU23.push(3);
DU23.shift();
DU23.pop();
DU23.shift();
DU23.pop();
DU23.pop();
DU23.unshift(2);

DU23.splice(2, 2, 51, 10, 13);

console.log("Final Array:", DU23);

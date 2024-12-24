function sortBalls(arr) {
    let low = 0, mid = 0, high = arr.length - 1;

    while (mid <= high) {
        if (arr[mid] === 'B') {
            [arr[low], arr[mid]] = [arr[mid], arr[low]];
            low++;
            mid++;
        } else if (arr[mid] === 'G') {
            mid++;
        } else {
            [arr[mid], arr[high]] = [arr[mid], arr[low]];
            high--;
        }
    }
    return arr;
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the array of balls (e.g., R,G,B,G,G,R,B,B,G): ', (input) => {
    const balls = input.split(',');
    const sortedballs = sortBalls(balls);
    console.log('Sorted Balls:', sortedballs);
    rl.close();
})
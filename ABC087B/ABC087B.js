function main(input) {
  const [a, b, c, x] = input.split('\n');  //[ '2', '2', '2', '100' ]
let count = 0;
  //硬貨それぞれの枚数分ループ
for (let i = 0; i <= a; i++) {
    for (let j = 0; j <= b; j++) {
        for (let k = 0; k <= c; k++) {
          if ((500 * i + 100 * j + 50 * k) == x) {
          count += 1;
          }
          }
      }
  }

  console.log(count);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));

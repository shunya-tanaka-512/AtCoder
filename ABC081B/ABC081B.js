function main(input) {
  input = input.split('\n'); //[ '3', '8 12 40' ]
var arr = input[1].split(' '); //[ '8', '12', '40' ]
  var count = 0;
  var flag = false;
while (true) {
     for ( let j = 0; j < arr.length; j++) {
       //奇数だったら次の処理へ
       if (arr[j] % 2 !== 0) {
         flag = true;
         break;
      }
     }
    if (flag){
    break;
    }
     //arrを2で割った配列へ代入
  arr = arr.map(value => value / 2);
    count += 1;
  }

  console.log(count);
}
main(require('fs').readFileSync('/dev/stdin', 'utf8'));

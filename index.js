// function checkLuhn(cardNo) {
//   let nDigits = cardNo.length;

//   let nSum = 0;
//   let isSecond = false;
//   for (let i = nDigits - 1; i >= 0; i--) {
//     console.log(cardNo[i], cardNo[i].charCodeAt());
//     console.log(cardNo[i], "0".charCodeAt());
//     let d = cardNo[i].charCodeAt() - "0".charCodeAt();
//     // console.log(cardNo[i], d);
//     //   if (isSecond == true) d = d * 2;

//     //   // We add two digits to handle
//     //   // cases that make two digits
//     //   // after doubling
//     //   nSum += parseInt(d / 10, 10);
//     //   nSum += d % 10;

//     //   isSecond = !isSecond;
//   }
//   return nSum % 10 == 0;
// }
// let cardNo = "79927398713";
// if (checkLuhn(cardNo)) console.log("This is a valid card");
// else console.log("This is not a valid card");
// arr = Array(3).fill(Array(4).fill(0));
// console.log(arr);
text1 = "abcftykdsuyewsa";
text2 = "aceydueydggs";
const cls = (text1, text2) => {
  arr = Array(text1.length + 1).fill(Array(text2.length + 1).fill(0));
  for (let row = text1.length - 1; row >= 0; row--) {
    for (let col = text2.length - 1; col >= 0; col--) {
      if (text1[row] === text2[col]) arr[row][col] = 1 + arr[row + 1][col + 1];
      else arr[row][col] = Math.max(arr[row + 1][col], arr[row][col + 1]);
    }
  }
  return arr[0][0];
};

console.log(cls(text1, text2));

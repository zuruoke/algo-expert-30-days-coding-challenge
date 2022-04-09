const coin_change = (coins, amount) => {
  if (amount === 0) return [];
  if (amount < 0) return null;
  let shortestCombination = null;

  for (let coin of coins) {
    remainder = amount - coin;
    remainderCombination = coin_change(coins, remainder);
    if (remainderCombination !== null) {
      const combination = [...remainderCombination, coin];
      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination;
      }
    }
  }
  return shortestCombination;
};

const bestSum = (targetSum, numbers) => {
  if (targetSum === 0) return [];
  if (targetSum < 0) return null;
  let shortestCombination = null;
  for (let num of numbers) {
    const remainder = targetSum - num;
    const remainderCombination = bestSum(remainder, numbers);
    if (remainderCombination !== null) {
      const combination = [...remainderCombination, num];
      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination;
      }
    }
  }
  return shortestCombination;
};

console.log(coin_change([1, 2, 5], 11));

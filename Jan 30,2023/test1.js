function sum() {
  var total = 0;
  for (var i = 0, len = arguments.length; i < len; ++i) {
    total += arguments[i];
  }
  return total;
}

function sum2(...args) {
  return args.reduce((total, item) => {
    return total + item;
  });
}

console.log(sum2(1, 2, 3)); // returns 6

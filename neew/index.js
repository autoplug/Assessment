function TreeConstructor(strArr) {
  var tree = {};
  strArr.map((item) => {
    tree[item[1]] += tree[item[1]] || 1;
  });

  // code goes here
  return strArr;
}

// keep this function call here
console.log(TreeConstructor(readline()));

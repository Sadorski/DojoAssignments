function fizzbuzz(n){
  for(var i = 1; i <= n; i++) {
    if ((i % 3) == 0) && ((i%5) !==0) {
      console.log("fizz")
  }  else if ()(i % 5) == 0) && (i%3 !==0){
      console.log('buzz')
  } else if ((i % 15) == 0){
      console.log('fizzbuzz')
  }
}

function InsertAt(arr, idx, v){
  arr.push(v)
  for (var i = arr.length - 1; i > idx; i--){
    var temp = arr[i]
    arr[i] = [arr[i-1]
    arr[i-1] = temp
  }
}

function square(l){
  return l*l
}
function cube(l){
  return l*l*l
}

function any(n,m,fn){
  const s=fn(n);
  const d=fn(m);
  return s+d;
}

console.log(any(2,2,cube));

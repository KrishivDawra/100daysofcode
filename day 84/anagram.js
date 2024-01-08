/*
  Write a function `isAnagram` which takes 2 parameters and returns true/false if those are anagrams or not.
  What's Anagram?
  - A word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
*/

function isAnagram(str1, str2) {
  let s,d,f=0;
  d=str1.length;
  s=str2.length;
  if(d==s){
    for(let i=0;i<d;i++){
      for(let j=0;j<s;j++){
        if(str1[i]==str2[j] || str1[i]==str2[j].toLowerCase() || str1[i]==str2[j].toUpperCase()){
          f=f+1;
        }
      }
    }
  
    if(f==d){
      return true;
    }
    else{
      return false;
    }
  }
  else{
    return false;
  }
}

module.exports = isAnagram;



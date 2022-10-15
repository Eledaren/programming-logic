const anagram = (a,b) => {
  if(a.length !== b.length) {
    console.log('Invalid Input!')
    return
  }

  let str1 = a.split('').sort().join('')
  let str2 = b.split('').sort().join('')

  if(str1 === str2) console.log(true)
  else console.log(false); 
}

anagram("indian","ndiani") 
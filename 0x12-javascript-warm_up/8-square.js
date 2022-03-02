#!/usr/bin/node
const size = Math.floor(process.argv[2]);
let side;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    side = '';
    for (let j = 0; j < size; j++) {
      side += 'X';
    }
    console.log(side);
  }
}

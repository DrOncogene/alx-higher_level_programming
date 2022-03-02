#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  let nums = args.splice(2, args.length);
  nums = nums.sort((a, b) => { return (a - b); });
  console.log(nums[nums.length - 2]);
}

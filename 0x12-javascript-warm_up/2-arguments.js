#!/usr/bin/node
const num = process.argv.length;
if (num === 3) {
  console.log('Argument found');
} else if (num > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}

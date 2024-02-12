#!/usr/bin/node
const num = process.argv.length;
if (num > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

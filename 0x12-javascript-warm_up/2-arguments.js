#!/usr/bin/node
//if else statement using process argv

if (process.argv.length < 3) {
	console.log('No argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else if(process.argv.length > 3) {
	console.log('Argument found');
}

// Program starts

// Imports readline module to get user input
const readline = require("readline");

// Some instructions
console.log("\nIn this program, we will find force applied on an object using python.");
console.log("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n");

// Input prompt starts
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// First question
rl.question("Enter the mass of the object: ", (mass) => {
    // Second question
    rl.question("Enter the acceleration of the object: ", (acceleration) => {
        /*
        if (mass != String && acceleration != String){
            return NaN;
        };
        */
        console.log(`The force applied on the object is ${mass*acceleration} Newton`)
        rl.close();
        // Input prompt terminated
    });
});

// Program ends
const readline = require("readline");

console.log("\nIn this program, we will find force applied on an object using python.");
console.log("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter the mass of the object: ", (mass) => {
    rl.question("Enter the acceleration of the object: ", (acceleration) => {
        console.log(`The force applied on the object is ${mass*acceleration} Newton`)
        rl.close();
    });
});

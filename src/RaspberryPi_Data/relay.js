const Gpio = require("onoff").Gpio;
const relay = new Gpio(20, "high"); // IMPORTANT: Use 'high' if relay uses low level trigger

console.log(
  "Program started. Relay should be off. Relay will turn on in 5 seconds."
);

// setTimeout(() => {
//   relay.writeSync(0);
//   console.log("Relay should be on. Relay will turn off in 5 seconds.");

//   setTimeout(() => {
//     relay.writeSync(1);
//     console.log("Relay should be off. ");
//   }, 5000);
// }, 5000);

function relayOn() {
  if (relay.readSync() === 0) {
    relay.writeSync(1); //set output to 1 i.e turn relay on
    console.log("Relay should be on.");
  } else {
    relay.writeSync(0); //set output to 0 i.e. turn relay off
  }
}
setTimeout(relayOn, 5000);
function relayOff() {
  // clearInterval(blinkInterval);
  relay.writeSync(0);
  relay.unexport(); // Unexport GPIO to free resources
}
setTimeout(relayOff, 5000);

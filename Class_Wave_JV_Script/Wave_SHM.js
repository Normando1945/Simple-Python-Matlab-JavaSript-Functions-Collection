let R = 100;                                    // Maximum amplitude of the array
let T = 600;                                    // Maximum period of the array
let phi = 0;                                    // Initial phase
let number_waves = 2                            // Initial number of responses for the summation
let max_number_waves = 10;                      // Final number of responses for the summation
let inv_frames = 0.05;                          // Animation speed
let number_of_pi = 1;                           // Initial value of phi                
let waveSlider;                                 // Variable
let ranCB = 170;                                // Initial color range [RGB]
let ranCS = 200;                                // Final color range [RGB]
let amplitudes = [];                            // Set the array of amplitude values
for (let i = 1; i < max_number_waves; i+=1) {   // Calculate the amplitude values
  amplitudes.push(R*4/(i*3.14));
}

let condition  = 0;                             // Initial condition to start the animation [off = 0]
let waves = [];                                 // Set the variable 'waves' to store the results from the class function

class Wave_Calss{                               // Create a class with the data of amplitude, period, and phase
  constructor(R, T, phi){                       // Constructor function
    this.R = R;
    this.T = T;
    this.phi = phi;
  }
  Response(t){                                  // Calculate the response
    let wn = TWO_PI*t/this.T;
    return cos(wn + this.phi)*this.R;       
  }
  actualiza(){                                  // Pan Function (update animation based on "inv_frames")
    this.phi += inv_frames;
  }
}

//////////////////////////////////////////////////// Java Setup /////////////////////////////////////////////////// 
function setup() {
  createCanvas(windowWidth,windowHeight);                                                    // Set the canvas size to match the window dimensions
  
  waveSlider = createSlider(1, max_number_waves, number_waves, 1);                           // Slider values range from 1 to 10, starting at "number_waves"
  waveSlider.position(20 , windowHeight-70);                                                 // Position

  let button = createButton('Start/Pause: Animation');
  button.position(20, 70 - 40);
  button.mousePressed(Start_Pause);
  button.style('cursor', 'pointer'); 

  for (let i=0; i < number_waves; i++){
    let amplitude = amplitudes[i % amplitudes.length];
    waves[i] = new Wave_Calss(amplitude, random(10,T), random(phi, number_of_pi*TWO_PI)) ;   // Utilizing the class and its function
  }
}

function Start_Pause() {
  condition = condition == 1 ? 0 : 1; 
}

//////////////////////////////////////////////////// Java Draw /////////////////////////////////////////////////// 
function draw() {
  background(255);                                     // bakground color
  
  let currentNumberWaves = waveSlider.value();                   // Obtain the current value of the slider for "# of waves"
  if (currentNumberWaves !== number_waves) {                     // Checking if the number of waves has changed
    number_waves = currentNumberWaves;                           // Update the visualization to reflect the current number of waves
    waves = [];                                                  // Clearing the array of waves after each update of the number of waves
    for (let i = 0; i < number_waves; i++) {                     // Reconstruct using the class and its function
      let amplitude = amplitudes[i % amplitudes.length];
      waves[i] = new Wave_Calss(amplitude, random(50, T), random(phi, number_of_pi * TWO_PI));
    }
  }

  stroke(0,0,0)
  line(0, windowHeight/1.5, windowWidth, windowHeight/1.5);      // Line representing the 0 amplitude for the sum of sinusoids
  stroke(0,0,0)
  line(0, windowHeight/4.0, windowWidth, windowHeight/4.0);      // Line representing the 0 amplitude for the all sinusoids
  
  stroke(0, 0, 0)
  for (let t = 0; t < windowWidth; t += T/190){                  // Loop through values of "t" from 0 to the window size in steps of T/190
    let yy = 0;
    beginShape();
    for (let j of waves){
      let y = j.Response(t);
      stroke(0);
      alpha(0.5);
      point(t, y+windowHeight/4)
      stroke(100,75)
      vertex(t, y+windowHeight/4);
    }
    endShape()
    for (let jj of waves){
      yy += jj.Response(t);
      // Mapping the values of "yy" to set a range of color values between ranCB and ranCS
      let colorValue = map(yy, 20, R, ranCB, ranCS);            // Range of color values between ranCB and ranCS
      fill(colorValue, ranCB, ranCS - colorValue);              // Set the colors between ranCB and ranCS                
    }
   stroke(255) 
   ellipse(t, yy+windowHeight/1.5, 10)
   let colorValue = map(yy, 20, R, ranCB, 255); 
   stroke(colorValue, ranCB, ranCS - colorValue); 
   line(t, windowHeight/1.5, t, yy + windowHeight/1.5);  
  }
  if (condition == 1){
    for (let z of waves){
      z.actualiza();
    }
  } else {
    
  }
  noStroke();

  fill('black'); 
  // textStyle(BOLD);
  textSize(16);
  textAlign(CENTER, CENTER);
  text('Displacement Response (SHM)', windowWidth/2 , 20);

  fill('blue'); 
  textAlign(LEFT, CENTER);
  textSize(12);
  text('Structural Engineering: Dynamics, Seismic Solution, and AI Integration [caceli.net]', 20 , windowHeight - 20);
  
  fill('black'); 
  textAlign(LEFT, CENTER);
  textSize(12);
  text('Slider, Number of Response used = ' + number_waves, 20 , windowHeight - 75);
}
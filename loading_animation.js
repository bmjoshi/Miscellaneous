var t = 0;
var N = 20;
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  for (var i=0; i<N; i++) {
    var z = abs(t+i*0.005)%1;
    var alpha = 2*PI*sin(2*PI*z);
    var beta = 2*PI*sin(2*PI*z);
    var x = 30*sin(alpha);
    var y = 30*cos(beta);
    circle(x+200, y+200, 0.2+i*(1/10));
  }
  t = t+0.005;
}

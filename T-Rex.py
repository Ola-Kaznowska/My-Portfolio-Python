from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>T-REX Google Game</title>
        <style>
            body { background-color: black; color: white; text-align: center; font-family: Arial, sans-serif; }
            h1 { margin-top: 20px; }
            .start-btn { background: linear-gradient(90deg, red, blue, green); padding: 10px 20px; border: none; color: white; font-size: 20px; cursor: pointer; transition: 0.3s; }
            .start-btn:hover { background: linear-gradient(90deg, green, blue, red); }
            canvas { display: block; margin: 20px auto; }
        </style>
    </head>
    <body>
        <h1>T-REX Google Game</h1>
        <button class="start-btn" onclick="startGame()">Start</button>
        <canvas id="gameCanvas" width="600" height="200" style="background-color: white; display: none;"></canvas>
        <script>
            let canvas, ctx;
            let trexImg = new Image();
            trexImg.src = "https://chromedino.com/assets/offline-sprite-2x.png";
            let trex = { 
                x: 50, 
                y: 150, 
                width: 44, 
                height: 47, 
                velocityY: 0, 
                gravity: 1,  
                jumpPower: -18,  
                jumpSpeedFactor: 1,
                jumpLimit: 150 
            };
            let obstacles = [];
            let gameActive = false;
            let score = 0;
            let lastObstacleX = 600;
            let minObstacleSpacing = 100;
            let obstacleSpeed = 2;
            let logos = [
                "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",
                "https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg",
                "https://upload.wikimedia.org/wikipedia/commons/b/bd/Logo_C_sharp.svg",
                "https://upload.wikimedia.org/wikipedia/commons/3/3b/Python-logo-notext.svg",
                "https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/3/38/HTML5_Badge.svg",
                "https://upload.wikimedia.org/wikipedia/commons/6/62/CSS3_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/b/b2/Bootstrap_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
            ];
            let codeSnippets = ["<div>", "function(){}", "def foo():", "public static", "console.log()"];

            function startGame() {
                document.querySelector(".start-btn").style.display = "none";
                canvas = document.getElementById("gameCanvas");
                ctx = canvas.getContext("2d");
                canvas.style.display = "block";
                gameActive = true;
                score = 0;
                obstacles = [];
                trex.y = 150;
                trex.velocityY = 0;
                trex.jumpSpeedFactor = 1;
                obstacleSpeed = 2;
                lastObstacleX = 600;
                requestAnimationFrame(update);
                setInterval(spawnObstacle, 1500);  
            }

            function update() {
                if (!gameActive) return;
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                trex.velocityY += trex.gravity;
                trex.y += trex.velocityY;

                // Ograniczenie skoku
                if (trex.y > trex.jumpLimit) {
                    trex.y = trex.jumpLimit;  
                    trex.velocityY = 0;  
                }

                if (trex.velocityY < 0) {
                    trex.gravity = 0.6;  
                } else {
                    trex.gravity = 1;  
                }

                ctx.drawImage(trexImg, 76, 6, 88, 94, trex.x, trex.y, trex.width, trex.height);

                // Zwiększanie prędkości gry
                if (score < 30) {
                    // Stopniowe zwiększanie prędkości do 30 punktów
                    if (score % 5 === 0 && score > 0) {
                        obstacleSpeed += 0.2;
                    }
                } else {
                    // Po 30 punktach prędkość wzrasta gwałtownie
                    obstacleSpeed += 0.5;
                }

                // Sprawdzanie kolizji
                for (let i = 0; i < obstacles.length; i++) {
                    obstacles[i].x -= obstacleSpeed;
                    let img = new Image();
                    img.src = obstacles[i].logo;
                    ctx.drawImage(img, obstacles[i].x, obstacles[i].y, obstacles[i].width, obstacles[i].height);

                    if (obstacles[i].x + obstacles[i].width < 0) {
                        obstacles.splice(i, 1);
                        score++;
                    }

                    // Kolizja z przeszkodą (koniec gry)
                    if (trex.x < obstacles[i].x + obstacles[i].width && trex.x + trex.width > obstacles[i].x && trex.y + trex.height > obstacles[i].y) {
                        gameOver();
                        return;
                    }
                }

                ctx.fillStyle = "black";
                ctx.font = "20px Arial";
                ctx.fillText("Score: " + score, 500, 30);
                codeSnippets.forEach((text, index) => {
                    ctx.fillText(text, index * 120 + 10, 50);
                });

                requestAnimationFrame(update);
            }

            function spawnObstacle() {
                if (!gameActive) return;
                let newX = lastObstacleX + minObstacleSpacing + Math.floor(Math.random() * 30);
                let randomLogo = logos[Math.floor(Math.random() * logos.length)];
                obstacles.push({ x: newX, y: 160, width: 30, height: 40, logo: randomLogo });
                lastObstacleX = newX + Math.floor(Math.random() * 100);
            }

            document.addEventListener("keydown", function(event) {
                if (event.code === "Space" && trex.y === 150) {
                    trex.velocityY = trex.jumpPower * trex.jumpSpeedFactor;
                }
            });

            function gameOver() {
                alert("Game Over! Your final score is: " + score);
                gameActive = false;
                document.querySelector(".start-btn").style.display = "block";
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
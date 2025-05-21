// 取得 canvas 元素和繪圖上下文
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

var dragImage = document.getElementById("a");
var clickEffect = document.createElement("div");
clickEffect.id = "click-effect";
document.body.appendChild(clickEffect);
clickEffect.style.display = "none";

// 設置初始得分
let score = 0;
const scoreElement = document.getElementById('score');
scoreElement.textContent = score;

// 載入圖片
const aImage = new Image();
aImage.src = '../static/fish.png';

const bImage = new Image();
bImage.src = '../static/pond2.png';

// 當圖片載入完成後開始遊戲
aImage.onload = function () {
	bImage.onload = function () {


		// 繪製圖片
		ctx.drawImage(bImage, 0, 0, canvas.width, canvas.height);


		// 當 a.png 被拖曳時
		document.getElementById('a').addEventListener('dragstart', function (e) {
			e.dataTransfer.setData('text', 'a');
		});

		// 當 a.png 被放置時
		canvas.addEventListener('drop', function (e) {


			e.preventDefault();
			const data = e.dataTransfer.getData('text');
			if (data === 'a' && e.offsetX >= canvas.width / 2 - aImage.width / 2 && e.offsetX <= canvas.width / 2 + aImage.width / 2 && e.offsetY >= canvas.height / 2 - aImage.height / 2 && e.offsetY <= canvas.height / 2 + aImage.height / 2) {
				score++;
				scoreElement.textContent = score;
				// 獲取滑鼠放開時的座標
				var x = e.pageX;
				var y = e.pageY;

				// 創建一個div元素，並設置其為「陰德+1」字樣
				var div = document.createElement('div');
				div.id = "click-effect"
				div.innerText = '陰德+1';

				// 設置div元素的樣式
				div.style.position = 'absolute';
				div.style.top = y + 'px';
				div.style.left = x + 'px';
				
				// 將div元素添加到body中
				document.body.appendChild(div);

				// 一秒後自動刪除div元素
				setTimeout(function () {
					document.body.removeChild(div);
				}, 1000);
			}
		});

		// 監聽img元素的mouseup事件
		canvas.addEventListener('mouseup', function (e) {


		});




		// 防止預設行為
		canvas.addEventListener('dragover', function (e) {
			e.preventDefault();
		});
	};
};



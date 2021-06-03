const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* 添加图片循环 */
for(let i=1;i<6;i++){
	const newImage = document.createElement('img');
	newImage.setAttribute('src', 'images/pic'+i+'.jpg');
	thumbBar.appendChild(newImage);
	newImage.onclick = function(e){
		displayedImage.src = newImage.src;
	}
}


/* 编写 变暗/变量 按钮功能 */


btn.onclick = function() {
  const btnClass = btn.getAttribute('class');
  if(btnClass === 'dark') {
    btn.setAttribute('class','light');
    btn.textContent = '变亮';
    overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
  } else {
    btn.setAttribute('class','dark');
    btn.textContent = '变暗';
    overlay.style.backgroundColor = 'rgba(0,0,0,0)';
  }
}
document.getElementById("addPrice").onclick = openPrice;
var open=false;
var spam=0;

function openPrice(){
	if(open == false){
		open = true;
		document.getElementById("priceWindow").style.display = "block";
		document.getElementById("closePrice").onclick = closePrice;
		document.getElementById("submit").onclick = addPrice;
	} else{
		open = false;
		document.getElementById("priceWindow").style.display = "none";
	}
}
function closePrice(){
	open = false;
	document.getElementById("priceWindow").style.display = "none";
}
function addPrice(level){
	openPrice();
	spam++;
	var item = document.getElementById("price").value;
	var description = document.getElementById("cost").value;
	if(spam > 2){
		alert("Woah! Slow down!");
		return;
	}
	if (item == '' || description == ''){
		alert("Fill out all fields!")
		return;
	}
	level = 'good';
	document.getElementById("priceList").innerHTML += 
	`
	<div class="`+level+` price">
		<h3 class="text">`+item+`</h3>
		<p class="description"> Price: `+description+`</p>
	</div>
	`;
}
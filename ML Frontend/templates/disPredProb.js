
document.getElementById("pk_sdk_symptoms1").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms2").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms3").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms4").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms5").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms6").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms7").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms8").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms9").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms10").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms11").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms12").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms13").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms14").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms15").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms16").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms17").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms18").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms19").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms20").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms21").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms22").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms23").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms24").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms25").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms26").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms27").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms28").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms29").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms30").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms31").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms32").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms33").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms34").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms35").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms36").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms37").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms38").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms39").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms40").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms41").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms42").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms43").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms44").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms45").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms46").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms47").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms48").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms49").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms50").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms51").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms52").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms53").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms54").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms55").addEventListener("click",fun);
document.getElementById("pk_sdk_symptoms56").addEventListener("click",fun);

var n1 = document.getElementById("nextBtn1");
var symptomCount = 0;
function fun(){
	if(this.style.background == "rgb(255, 255, 0)"){
		this.style.background = '#ffffff';
		console.log(this.style.background);
	}
	else{
		this.style.background = '#ffff00';
		console.log(this.style.background);
		symptomCount += 1;
		console.log(symptomCount);	
	}
	// var c = 0;
	// var s= ".style.background";
	// for(i=1;i<=56;i++){
	// 	s = 'v' + i + s;
	// 	if(s === "rgb(255, 255, 0)"){
	// 		console.log("done");
	// 	}
	// 	console.log(s , typeof(s));
	// 	s= ".style.background";	
	// }
	if(symptomCount !== 0){
	 document.getElementById("pk_sdk_symptoms16").disabled = true;	
	}
}

// document.getElementById("bag2").disabled=true;
// document.getElementById("bag3").disabled=true;
// document.getElementById("bag4").disabled=true;
// document.getElementById("bag5").disabled=true;
// document.getElementById("bag6").disabled=true;
// $("#bag2").children().attr('disabled',true);
// $("#bag3").children().attr('disabled',true);
// $("#bag4").children().attr('disabled',true);
// $("#bag5").children().attr('disabled',true);
// $("#bag6").children().attr('disabled',true);

// var nodes = document.getElementById("bag").getElementsByTagName('*');
// for(var i = 0; i < nodes.length; i++){
//      nodes[i].disabled = true;	
// }
// $("#bag1").find("*").prop('disabled',true);
// $('#bag2 *').attr("disabled", true);
// n1.addEventListener("click",visible);
// function visible(){
// 	document.getElementById("bag2").disabled=false;
// 	// ('#bag2 *').attr("disabled", false);
// 	console.log("Trying to make enable");
// }

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

document.getElementById("noneof1").addEventListener("click",funNone1);
document.getElementById("noneof2").addEventListener("click",funNone2);
document.getElementById("noneof3").addEventListener("click",funNone3);
document.getElementById("noneof4").addEventListener("click",funNone4);


var n1 = document.getElementById("nextBtn1");
var n2 = document.getElementById("nextBtn2");
var n3 = document.getElementById("nextBtn3");
var n4 = document.getElementById("nextBtn4");


n1.addEventListener("click",function(){
	document.querySelector(".test2").style.display="inline";
	
});

n2.addEventListener("click",function(){
	document.querySelector(".test3").style.display="inline";
	
});

n3.addEventListener("click",function(){
	document.querySelector(".test4").style.display="inline";
	
});

// n4.addEventListener("click",function(){
// 	document.querySelector("").style.display="inline";
	
// });


var symptomCount = 0;
function fun(){
	if(this.style.background == "rgb(0, 204, 0)"){
		this.style.background = "#ffffff";
		this.style.color = "#00cc00";
		console.log(this.style.background);
		symptomCount -= 1;
		console.log(symptomCount);
	}
	else{
		this.style.background = "#00cc00";
		console.log(this.style.background);
		this.style.color = "#000000";
		symptomCount += 1;
		console.log(symptomCount);	
	}
}

function funNone1(){
	if(symptomCount == 0){
		if(this.style.background == "rgb(0, 204, 0)"){
			this.style.background = "#ffffff";
			this.style.color = "#00cc00";
		}
		else{
			this.style.background = "#00cc00";
			console.log(this.style.background);
			this.style.color = "#000000";
		}
		document.getElementById("pk_sdk_symptoms1").disabled = true;
		document.getElementById("pk_sdk_symptoms2").disabled = true;
		document.getElementById("pk_sdk_symptoms3").disabled = true;
		document.getElementById("pk_sdk_symptoms4").disabled = true;
		document.getElementById("pk_sdk_symptoms5").disabled = true;
		document.getElementById("pk_sdk_symptoms6").disabled = true;
		document.getElementById("pk_sdk_symptoms7").disabled = true;
		document.getElementById("pk_sdk_symptoms8").disabled = true;
		document.getElementById("pk_sdk_symptoms9").disabled = true;
		document.getElementById("pk_sdk_symptoms10").disabled = true;
		document.getElementById("pk_sdk_symptoms11").disabled = true;
		document.getElementById("pk_sdk_symptoms12").disabled = true;
		document.getElementById("pk_sdk_symptoms13").disabled = true;
		document.getElementById("pk_sdk_symptoms14").disabled = true;
	}
	else{
		document.getElementById("noneof1").disabled = true;
	}
}

function funNone2(){
	if(symptomCount == 0){
		if(this.style.background == "rgb(0, 204, 0)"){
			this.style.background = "#ffffff";
			this.style.color = "#00cc00";
		}
		else{
			this.style.background = "#00cc00";
			console.log(this.style.background);
			this.style.color = "#000000";
		}
		document.getElementById("pk_sdk_symptoms15").disabled = true;
		document.getElementById("pk_sdk_symptoms16").disabled = true;
		document.getElementById("pk_sdk_symptoms17").disabled = true;
		document.getElementById("pk_sdk_symptoms18").disabled = true;
		document.getElementById("pk_sdk_symptoms19").disabled = true;
		document.getElementById("pk_sdk_symptoms20").disabled = true;
		document.getElementById("pk_sdk_symptoms21").disabled = true;
		document.getElementById("pk_sdk_symptoms22").disabled = true;
		document.getElementById("pk_sdk_symptoms23").disabled = true;
		document.getElementById("pk_sdk_symptoms24").disabled = true;
		document.getElementById("pk_sdk_symptoms25").disabled = true;
		document.getElementById("pk_sdk_symptoms26").disabled = true;
		document.getElementById("pk_sdk_symptoms27").disabled = true;
		document.getElementById("pk_sdk_symptoms28").disabled = true;
		document.getElementById("pk_sdk_symptoms29").disabled = true;
	}
	else{
		document.getElementById("noneof2").disabled = true;
	}
}

function funNone3(){
	if(symptomCount == 0){
		if(this.style.background == "rgb(0, 204, 0)"){
			this.style.background = "#ffffff";
			this.style.color = "#00cc00";
		}
		else{
			this.style.background = "#00cc00";
			console.log(this.style.background);
			this.style.color = "#000000";
		}
		document.getElementById("pk_sdk_symptoms30").disabled = true;
		document.getElementById("pk_sdk_symptoms31").disabled = true;
		document.getElementById("pk_sdk_symptoms32").disabled = true;
		document.getElementById("pk_sdk_symptoms33").disabled = true;
		document.getElementById("pk_sdk_symptoms34").disabled = true;
		document.getElementById("pk_sdk_symptoms35").disabled = true;
		document.getElementById("pk_sdk_symptoms36").disabled = true;
		document.getElementById("pk_sdk_symptoms37").disabled = true;
		document.getElementById("pk_sdk_symptoms38").disabled = true;
		document.getElementById("pk_sdk_symptoms39").disabled = true;
		document.getElementById("pk_sdk_symptoms40").disabled = true;
		document.getElementById("pk_sdk_symptoms41").disabled = true;
		document.getElementById("pk_sdk_symptoms42").disabled = true;
		document.getElementById("pk_sdk_symptoms43").disabled = true;
		document.getElementById("pk_sdk_symptoms44").disabled = true;
	}
	else{
		document.getElementById("noneof3").disabled = true;
	}
}

function funNone4(){
	if(symptomCount == 0){
		if(this.style.background == "rgb(0, 204, 0)"){
			this.style.background = "#ffffff";
			this.style.color = "#00cc00";
		}
		else{
			this.style.background = "#00cc00";
			console.log(this.style.background);
			this.style.color = "#000000";
		}
		
		document.getElementById("pk_sdk_symptoms45").disabled = true;
		document.getElementById("pk_sdk_symptoms46").disabled = true;
		document.getElementById("pk_sdk_symptoms47").disabled = true;
		document.getElementById("pk_sdk_symptoms48").disabled = true;
		document.getElementById("pk_sdk_symptoms49").disabled = true;
		document.getElementById("pk_sdk_symptoms50").disabled = true;
		document.getElementById("pk_sdk_symptoms51").disabled = true;
		document.getElementById("pk_sdk_symptoms52").disabled = true;
		document.getElementById("pk_sdk_symptoms53").disabled = true;
		document.getElementById("pk_sdk_symptoms54").disabled = true;
		document.getElementById("pk_sdk_symptoms55").disabled = true;
		document.getElementById("pk_sdk_symptoms56").disabled = true;

	}
	else{
		document.getElementById("noneof4").disabled = true;
	}
}

// var symptoms = ["bloody_stools","fecal_leakage","swelling","dizziness","confusion","fatigue","itching","vomiting","arm_pain","cough", "muscle_pain", "depression", "fever","painful_bowel_moments", "urine_blood","sweating","nausea", "stiff_neck","decreased_appetite",'weak',"wheezing","bleeding","hives","bleed","headache", "dry_mouth","sweat","stomach_pain","stool_pressure","anxiety","shoulder_pain","anus_itching", "vision_problem","abdominal_pain","chest_pain", "weight_loss","diarrhea" ,"breath_problems","thirsty","anus_swelling", "blood_o_tissue","constipation","neck_pain","low_heartbeat","more_urine","low_breath","muscle_cramps","muscle_spasm","yawning","rash","back_pain","anal_bleeding","lump_anus","cold","skin_rash","neck_stiff"]

var s = "pk_sdk_symptoms";
var symp = ["fever","cough","vomiting","cold","stomach_pain","vision_problem","shoulder_pain","confusion","arm_pain","itching","muscle_pain","depression","headache","headache","sweating","low_heartbeat","painful_bowel_moments","stiff_neck","nausea","dry_mouth","chest_pain","yawning","low_breath","stool_pressure","skin_rash","swelling","fatigue","urine_blood","weak","back_pain","anal_bleeding","constipation","bloody_stools","fecal_leakage","muscle_cramps","abdominal_pain","weight_loss","dizziness","sweat","more_urine","bleed","neck_pain","rash","muscle_pain","breath_problems","anus_swelling","thirsty","anus_itching","decreased_appetite","wheezing","diarrhea","blood_o_tissue","neck_stiff","lump_anus","anxiety","bleeding","hives"]
n4.addEventListener("click",function(){
	var p = []	
	try{
		for(var i = 0;i<symp.length;i++){
			j = i + 1;
			s = s + j.toString();
			if(document.getElementById(s).style.background == "rgb(0, 204, 0)"){
				console.log(symp[j]);
				p.push(symp[j]);
			}
			if(i==55){
				funny(p);
			}
			console.log(p);
			s = "pk_sdk_symptoms";
		}
	}

	catch(err){
		console.log(err);
	}


	function funny(p){
		if(p.length< 5){
		document.querySelector(".alert").style.display="inline";
		console.log(p.length);
		console.log("working");
		}
	}
	

});

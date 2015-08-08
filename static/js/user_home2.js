$(document).ready(function(){
	$("div.well ul.nav-list li").click(function() {
		$("ul.nav-list li").removeClass("active");
		$(this).addClass("active");
		var thisval=$(this).text();
		$("div.description").html(makeHtmldata(thisval));
		});
		
	function makeHtmldata(fn) {
		var htm='';
		if (fn=='Help'){		
			htm+='<b>Exam Specific Instructions</b>';
			htm+='<ul style="list-style-type: decimal; text-align: left">';
			htm+='<li>The clock has been set at server and count down timer at the top right corner of the screen will display left out time to closure from where you can monitor time you have to complete the exam. </li>';
			htm+='<li>Click one of the answer option buttons to select your answer.</li>';
			htm+='<li>To change an answer, simply click the desired option button. </li>';
			htm+='<li>Click on <b>RESET</b> button to deselect a chosen answer.  </li>';
			htm+='<li>Click on <b>SAVE &amp; NEXT</b> to save the answer before moving to the next question. The next question will automatically be displayed.</li>';
			htm+='<li>Click on <b>SKIP</b> to move to the next question without saving the current question.</li>';
			htm+='<li>Make sure you click on <b>SAVE &amp; NEXT</b> button everytime you want to save your answer.</li>';
			htm+='<li>To go to a question, click on the question number on the right side of the screen.</li>';
			htm+='<li>The color coded buttons on the right side of the screen shows the status of the questions : </li>';
			htm+='<ul><li>White - you have not visited the Question.</li>';
			htm+='<li>Red - you have not answered the Question.</li>';
			htm+='<li>Green - you have answered the Question.</li></ul>';
			htm+='<li>All the answered questions(saved or marked) will be considered for calculating the final score.</li>';
			htm+='<li><b><font color="red"> Do Not CLICK on the SUBMIT Button unless you have completed the exam.In case you click SUBMIT button, you will not be permitted to continue.</font></b></li></ul>';
		}
		else if (fn=='Settings'){
			htm+='<ul class="nav nav-pills nav-stacked">'
			htm+='<li class="active"><a>'+fn+'</a></li>'
			htm+='<li><a href="/accounts/profile/exam/?examtype=JEE+Main+2013">JEE Main 2013 Question paper</a></li>'
			htm+='<li><a href="#">Messages</a></li></ul>'
        }
        else if (fn=='Profile'){
        	htm+='<h4>Ur profile picture</h4>'
			htm+='<img  style="width:140px;height:110px;" src="/static/media/{{ employer.avatar }}" />'
			htm+='<a data-toggle="modal" href="/profilepic/">Upload new</a>'
			
					
        }
		return(htm);
	}
	

});

from django import template
register = template.Library()


@register.simple_tag
def SelectCountry(sel):
	str_q='<select name="country" id="country" onChange="setStates();" style="width:235px;" ><option value="">SelectCountry</option>'
	for i in ("Australia","Bangladesh","Canada","India","Malaysia","Mexico","Saudi Arabia","United Arab Emirates","United Kingdom","United States"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectState(sel):
	str_q='<select name="state" id="state" onChange="setCities();" style="width:235px;"><option value="">SelectState</option>'
	for i in ("Australia","Bangladesh","Canada","India","Malaysia","Mexico","Saudi Arabia","United Arab Emirates","United Kingdom","United States"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectCity(sel):
	str_q='<select name="city" id="city" style="width:235px;"><option value="">SelectState</option>'
	for i in ("Australia","Bangladesh","Canada","India","Malaysia","Mexico","Saudi Arabia","United Arab Emirates","United Kingdom","United States"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectPreferTime(sel):
	str_q='<select  name="prefertime" style="width:235px;"><option value="">Select Time</option>'
	for i in ("Any Time","10AM-12PM","12PM-02PM","02PM-04PM","04PM-06PM"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectGender(sel):
	str_q='<select name="gender" style="width:235px;" ><option value=""> Select </option>'
	for i in ("Male","Female","General"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectMaritalStatus(sel):
	str_q='<select name="maritalstatus" style="width:235px;" ><option value=""> Select </option>'
	for i in ("Single/Unmarried","Married","Widowed","Divorced","Separated","Other"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectExpYears(sel):
	str_q='<select name="work_expyears" style="width:90px;" ><option value="">Year</option>'
	for i in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>Years'
	return str_q

@register.simple_tag
def SelectExpMonths(sel):
	str_q='<select name="work_expmonths" style="width:90px;" ><option value="">Month</option>'
	for i in ('0','1','2','3','4','5','6','7','8','9','10','11'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>Months'
	return str_q


@register.simple_tag
def SelectAnnualSalary(sel):
	str_q='<select name="salary" style="width:235px;" ><option value=""> Select </option><optgroup label="Month Wise">'

	for i in ("Lessthan 20,000$","20,000$ - 30,000$","30,000$ - 40,000$","40,000$ - 50,000$","50,000$ - 60,000$","60,000$ - 70,000$","Above 70,000$","<optgroup label='Hour Wise'>","Lessthan 40$/hr","40$/hr - 50$/hr","50$/hr - 60$/hr","60$/hr - 70$/hr","70$/hr - 80$/hr","80$/hr - 90$/hr","90$/hr - 100$/hr","Above 100$/hr"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

	"""
	for i in ():
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	


	
                <script type="text/javascript">

                    var Salary=new Array("Lessthan 20,000$","20,000$ - 30,000$","30,000$ - 40,000$","40,000$ - 50,000$","50,000$ - 60,000$","60,000$ - 70,000$","Above 70,000$");

                    for(var i=0;i<Salary.length;i++)

                    document.write("<option value=\""+Salary[i]+"\">"+Salary[i]+"</option>");

                </script>
                </optgroup>
                <optgroup label="Hour Wise">
                   <script type="text/javascript">

                    var Salary=new Array("Lessthan 40$/hr","40$/hr - 50$/hr","50$/hr - 60$/hr","60$/hr - 70$/hr","70$/hr - 80$/hr","80$/hr - 90$/hr","90$/hr - 100$/hr","Above 100$/hr");

                    for(var i=0;i<Salary.length;i++)

                    document.write("<option value=\""+Salary[i]+"\">"+Salary[i]+"</option>");

                </script>


                </optgroup>


	for i in ("Below 10000","10000-20000","20000-30000","30000-40000","40000-50000","50000-60000","60000-70000","70000-80000","Above 80000"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q
	"""


@register.simple_tag
def SelectIndustry(sel):
	str_i='<select name="industry" style="width:235px;" ><option value=""> Select </option>'
	for i in ("Accounting/Finance","Advertising/PR/MR/Events","Agriculture/Dairy","Animation","Architecture/Interior Designing","Auto/Auto Ancillary","Aviation / Aerospace Firms","Banking/Financial Services/Broking","BPO/ITES","Brewery / Distillery","Ceramics /Sanitary ware","Chemicals/PetroChemical/Plastic/Rubber","Construction/Engineering/Cement/Metals","Consumer Durables","Courier/Transportation/Freight","Defence/Government","Education/Teaching/Training","Education/Teaching/Training","Electricals / Switchgears","Export/Import","Facility Management","Fertilizers/Pesticides","FMCG/Foods/Beverage","Food Processing","Fresher/Trainee","Gems & Jewellery","Glass","Heat Ventilation Air Conditioning","Hotels/Restaurants/Airlines/Travel","Industrial Products/Heavy Machinery","Insurance","IT-Hardware & Networking","IT-Software/Software Services","KPO / Research /Analytics","Legal","Media/Dotcom/Entertainment","Internet/Ecommerce","Medical/Healthcare/Hospital","Mining","NGO/Social Services","Office Equipment/Automation","Oil and Gas/Power/Infrastructure/Energy","Paper","Pharma/Biotech/Clinical Research","Printing/Packaging","Publishing","Real Estate/Property","Recruitment","Retail","Security/Law Enforcement","Semiconductors/Electronics","Shipping/Marine","Steel","Strategy /Management Consulting Firms","Telcom/ISP","Textiles/Garments/Accessories","Tyres","Water Treatment / Waste Management","Wellness/Fitness/Sports","Other"):
		if i==sel:str_i+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_i+='<option value="%s">%s</option>' %(i,i)
	str_i+='</select>'
	return str_i



@register.simple_tag
def SelectFunctionalArea(sel):
	
	str_f='<select name="functional_area" style="width:235px;" ><option value=""> Select </option>'
	for i in ("Accounts/Finance/Tax/CS/Audit","Agent","Analytics & Business Intelligence","Architecture/Interior Design","Banking/Insurance","Content/Journalism","Corporate Planning/Consulting","Engineering Design/R&D","Export/Import/Merchandising","Fashion/Garments/Merchandising","Guards/Security Services","Hotels/Restaurants","HR/Administration/IR","IT Software-Client Server","IT Software-Mainframe","IT Software-Middleware","IT Software-Mobile","IT Software-Other","IT Software-System Programming","IT Software-Telecom Software","IT Software-Application Programming/Maintenance","IT Software-DBA/Datawarehousing","IT Software-E-Commerce/Internet Technologies","IT Software-Embedded/EDA/VLSI/ASIC/Chip Des","IT Software-ERP/CRM","IT Software-Network Administration/Security","IT Software-QA & Testing","IT Software-Systems/EDP/MIS","IT-Hardware/Telecom/Technical Staff/Support","ITES/BPO/KPO/Customer Service/Operations","Legal","Marketing/Advertising/MR/PR","Packaging","Pharma/Biotech/Healthcare/Medical/R&D","Production/Maintenance/Quality","Purchase/Logistics/Supply Chain","Sales/BD","Secretary/Front Office/Data Entry","Self Employed/Consultants","Shipping","Site Engineering/Project Management","Teaching/Education","Ticketing/Travel/Airlines","Top Management","TV/Films/Production","Web/Graphic Design/Visualiser","Other"):
		if i==sel:str_f+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_f+='<option value="%s">%s</option>' %(i,i)
	str_f+='</select>'
	return str_f


@register.simple_tag
def SelectDegree(sel,cnt):

	str_f='<select name="degree%s"><option value=""> Select </option>' %cnt
	for i in ('Military service','High school','Associate','Pre- Bachelors','Bachelors','Post-Bachelors','Masters','Post- Masters','PHD - Doctorate','MBA','Other'):
		if i==sel:str_f+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_f+='<option value="%s">%s</option>' %(i,i)
	str_f+='</select>'
	return str_f

@register.simple_tag
def SelectEditCountry(sel,cnt):
	str_q='<select name="country%s" id="country%s"><option value="">Select</option>' %(cnt,cnt)
	for i in ("Afganistan","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bonaire","Bosnia &amp; Herzegovina","Botswana","Brazil","British Indian Ocean Ter","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Canary Islands","Cape Verde","Cayman Islands","Central African Republic","Chad","Channel Islands","Chile","China","Christmas Island","Cocos Island","Colombia","Comoros","Congo","Cook Islands","Costa Rica","Cote DIvoire","Croatia","Cuba","Curaco","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Guiana","French Polynesia","French Southern Ter","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Great Britain","Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala","Guinea","Guyana","Haiti","Hawaii","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea North","Korea Sout","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malaysia","Malawi","Maldives","Mali","Malta","Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico","Midway Islands","Moldova","Monaco","Mongolia","Montserrat","Morocco","Mozambique","Myanmar","Nambia","Nauru","Nepal","Netherland Antilles","Netherlands","Nevis","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","Norway","Oman","Pakistan","Palau Island","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Phillipines","Pitcairn Island","Poland","Portugal","Puerto Rico","Qatar","Republic of Montenegro","Republic of Serbia","Reunion","Romania","Russia","Rwanda","St Barthelemy","St Eustatius","St Helena","St Kitts-Nevis","St Lucia","St Maarten","St Pierre &amp; Miquelon","St Vincent &amp; Grenadines","Saipan","Samoa","Samoa American","San Marino","Sao Tome & Principe","Saudi Arabia","Senegal","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Tahiti","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tokelau","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos Is","Tuvalu","Uganda","Ukraine","United Arab Erimates","United Kingdom","United States of America","Uraguay","Uzbekistan","Vanuatu","Vatican City State","Venezuela","Vietnam","Virgin Islands (Brit)","Virgin Islands (USA)","Wake Island","Wallis &amp; Futana Is","Yemen","Zaire","Zambia","Zimbabwe"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectUGYear(sel):
	
	str_f='<select name="ug_year" style="width:235px;" ><option value=""> Select </option>'
	for i in ("2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985"):
		if i==sel:str_f+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_f+='<option value="%s">%s</option>' %(i,i)
	str_f+='</select>'
	return str_f


@register.simple_tag
def SelectOtherYear(sel):
	
	str_f='<select name="other_year" style="width:235px;" ><option value=""> Select </option>'
	for i in ("2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985"):
		if i==sel:str_f+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_f+='<option value="%s">%s</option>' %(i,i)
	str_f+='</select>'
	return str_f


@register.simple_tag
def SelectSkillLastUsed(sel,year):

	str_q='<select  name="lastused%s" id="lastused%s" style="width:100px;" ><option value="">Select</option>'%(year,year)
	for i in ("2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectSkillYear(sel,year):

	str_q='<select  name="skillyear%s" id="skillyear%s" style="width:100px;" ><option value="">Select</option>'%(year,year)
	for i in ('0','1','2','3','4','5','6','7','8','9','10','11','12'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>Years'
	return str_q

@register.simple_tag
def SelectSkillMonth(sel,mon):

	str_q='<select  name="skillmon%s" id="skillmon%s" style="width:100px;" ><option value="">Select</option>'%(mon,mon)
	for i in ('0','1','2','3','4','5','6','7','8','9','10','11'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>Months'
	return str_q


@register.simple_tag
def SelectRole(sel,cnt):
	
	str_f='<select name="role%s" class="input-xlarge"><option value=""> Select </option>' %cnt
	for i in ("Domain Expert","Sr.Project Leader","Solution Architect","Quality Analyst","Database Architect/DBA","Network/System Administrator","Project Leader","Module Leader","Sr.Programmer","Programmer","Test Engineer","Other"):
		if i==sel:str_f+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_f+='<option value="%s">%s</option>' %(i,i)
	str_f+='</select>'
	return str_f

@register.simple_tag
def SelectTeamSize(sel,cnt):
	str_f='<select name="teamsize%s" class="input-xlarge"><option value=""> Select </option>' %cnt
	for i in ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'):
		if i==sel:str_f+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_f+='<option value="%s">%s</option>' %(i,i)
	str_f+='</select>'
	return str_f




@register.simple_tag
def SelectLanguageProficiency(sel,profn):

	str_q='<select  name="proficiency%s" id="proficiency%s"><option value="">Select</option>'%(profn,profn)
	for i in ("Beginner","Proficient","Expert"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectWorkPermit(sel):

	str_q='<select  name="workpermit" id="workpermit" style="width:250px;" ><option value="">Select</option>'
	for i in ("Have H1 Visa","Need H1 Visa","TN Permit Holder","Green Card Holder","US Citizen","Authorize to work in US"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectEmploymentType(sel):

	str_q='<select id="emptype"  name="emptype" size="4" style="width:250px;"><option value="">Select</option>'
	for i in ("Full time","Contract - Corp to Corp","Contract - Independent","Contract - W2","Contract to Hire - Corp to Corp","Contract to Hire - Independent","Contract to Hire - W2","Part time"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q



@register.simple_tag
def SelectOtherCountry(sel):
	s=[i.strip() for i in sel.split(',')]
	str_q='<select name="workother" id="workother" multiple="" size="5" style="width:250px;" ><option value="">Select</option>'
	for i in ('Afghanistan','Albania','Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh','Belarus','Belgium','Bhutan','Botswana','Brazil','Burma','Burundi','Cambodia','Cameroon','Canada','Chile','China','Colombia','Comoros','Congo','Cuba','Cyprus','Czech Republic','Denmark','Egypt','Estonia','Ethiopia','France','Gambia','Georgia','Germany','Ghana','Greece','Guinea','Guyana','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Kenya','Korea','Kuwait','Lebanon','Liberia','Libya','Lithuania','Malaysia','Maldives','Mexico','Moldova','Mongolia','Namibia','Nepal','Netherlands','New Zealand','Nigeria','Norway','Oman','Pakistan','Panama','Philippines','Poland','Portugal','Qatar','Russia','Saint Lucia','Saudi Arabia','Serbia','Singapore','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Sweden','Switzerland','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Vatican City','Vietnam','Yemen','Zambia','Zimbabwe'):
		if i in s:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q



@register.simple_tag
def SelectTravelPercent(sel):

	str_q='<select id="travel" name="travel" style="width:250px;"><option value="">Select</option>'
	for i in ("0% - No travel","25%","50%","75%","100%"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q



@register.simple_tag
def SelectRelocateChoice(sel):
	s=[i.strip() for i in sel.split(',')]
	str_q='<select id="relocatechoice"  name="relocatechoice" size="5" multiple style="width:250px;"><option value="">Select</option>'
	for i in ('Afghanistan','Albania','Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh','Belarus','Belgium','Bhutan','Botswana','Brazil','Burma','Burundi','Cambodia','Cameroon','Canada','Chile','China','Colombia','Comoros','Congo','Cuba','Cyprus','Czech Republic','Denmark','Egypt','Estonia','Ethiopia','France','Gambia','Georgia','Germany','Ghana','Greece','Guinea','Guyana','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Kenya','Korea','Kuwait','Lebanon','Liberia','Libya','Lithuania','Malaysia','Maldives','Mexico','Moldova','Mongolia','Namibia','Nepal','Netherlands','New Zealand','Nigeria','Norway','Oman','Pakistan','Panama','Philippines','Poland','Portugal','Qatar','Russia','Saint Lucia','Saudi Arabia','Serbia','Singapore','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Sweden','Switzerland','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Vatican City','Vietnam','Yemen','Zambia','Zimbabwe'):
		if i in s:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q



@register.simple_tag
def SelectEmpIndustry(sel):

	str_q='<select name="industry" style="width:260px;" required="true"><option value="">Select</option>'
	for i in ('Accounting/Finance','Advertising/PR/MR/Events','Agriculture/Dairy','Animation','Architecture/Interior Designing','Auto/Auto Ancillary','Aviation/Aerospace Firms','Banking/Financial Services/Broking','BPO/ITES','Brewery/Distillery','Ceramics/Sanitary ware','Chemicals/PetroChemical/Plastic/Rubber','Construction/Engineering/Cement/Metals','Consumer Durables','Courier/Transportation/Freight','Defence/Government','Education/Teaching/Training','Electricals/Switchgears','Export/Import','Facility Management','Fertilizers/Pesticides','FMCG/Foods/Beverage','Food Processing','Fresher/Trainee','Gems & Jewellery','Glass','Heat Ventilation Air Conditioning','Hotels/Restaurants/Airlines/Travel','Industrial Products/Heavy Machinery','Insurance','IT-Hardware & Networking','IT-Software/Software Services','KPO/Research /Analytics','Legal','Media/Dotcom/Entertainment','Internet/Ecommerce','Medical/Healthcare/Hospital','Mining','NGO/Social Services','Office Equipment/Automation','Oil and Gas/Power/Infrastructure/Energy','Paper','Pharma/Biotech/Clinical Research','Printing/Packaging','Publishing','Real Estate/Property','Recruitment','Retail','Security/Law Enforcement','Semiconductors/Electronics','Shipping/Marine','Steel','Strategy/Management Consulting Firms','Telcom/ISP','Textiles/Garments/Accessories','Tyres','Water Treatment/Waste Management','Wellness/Fitness/Sports','Other'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpFun(sel):

	str_q='<select name="functionalarea" style="width:260px;" required="true"><option value="">Select</option>'
	for i in ('Accounts/Finance/Tax/CS/Audit','Agent','Analytics & Business Intelligence','Architecture Interior Design','Banking/Insurance','Content/Journalism','Corporate Planning/Consulting','Engineering Design/R&D','Export/Import/Merchandising','Fashion/Garments/Merchandising','Guards/Security Services','Hotels/Restaurants','HR/Administration/IR','IT Software-Client Server','IT Software-Mainframe','IT Software-Middleware','IT Software-Mobile','IT Software-Other','IT Software-System Programming','IT Software-Telecom Software','IT Software-Application Programming/Maintenance','IT Software-DBA/Datawarehousing','IT Software-E-Commerce/Internet Technologies','IT Software-Embedded/EDA/VLSI/ASIC/Chip Des.','IT Software-ERP/CRM','IT Software-Network Administration/Security','IT Software-QA&Testing','IT Software-Systems/EDP/MIS','IT-Hardware/Telecom/Technical Staff/Support','ITES/BPO/KPO/Customer Service/Operations','Legal','Marketing/Advertising/MR/PR','Packaging','Pharma/Biotech/Healthcare/Medical/R&D','Production/Maintenance/Quality','Purchase/Logistics/Supply Chain','Sales/BD','Secretary/Front Office/Data Entry','Self Employed/Consultants','Shipping','Site Engineering/Project Management','Teaching/Education','Ticketing/Travel/Airlines','Top Management','TV/Films/Production','Web/Graphic Design/Visualiser','Other'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpExp(sel,fname):

	str_q='<select class="input-small" name="%s" required="true"><option value="">Select</option>'%fname
	for i in range(11):
		curs=' selected' if i==int(sel) else ''#:str_q+='<option value="%s" selected>%s</option>' %(i,i)
		str_q+='<option value="%s"%s>%s</option>' %(i,curs,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpSecretClear(sel):
	str_q='<select required class="input-xlarge" name="empsecretclear"><option value="">Select</option>'
	for i in ('Not Need','Public Trust','NACI','ADP1/IT1','ADP2/IT2','Confidential','DOE L','DOE Q','Secret','Top Secret','Top Secret/SCI','Top Secret/SCI CI Polygeaph','Top Secret/SCI Full Scope Polygeaph','Other Clearance'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def SelectEmpWorkPermit(sel):

	str_q='<select  name="workpermit" id="workpermit" style="width:250px;" ><option value="">Select</option>'
	for i in ("Have H1 Visa","Need H1 Visa","TN Permit Holder","Green Card Holder","US Citizen","Authorize to work in US"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpTravelReq(sel):
	str_q='<select required="" style="width:260px;" name="emptravel"><option value="">Select</option>'
	for i in ('Not Need','25%','50%','75%','100%'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpJobType(sel):
	str_q='<select style="width:260px;" name="jobtype"><option value="">Select</option>'
	for i in ('Freelance','Fulltime','Parttime','Internship','Contract - Corp-to-Corp','Contract - Independent','Contract - W2','Contract to Hire - Corp-to-Corp','Contract to Hire - Independent','Contract to Hire - W2','Temporary'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpSalaryRange(sel):
	str_q='<select style="width:260px;" name="salary_range"><option value=""> Select </option><optgroup label="Month Wise">'

	for i in ("Lessthan 20,000$","20,000$ - 30,000$","30,000$ - 40,000$","40,000$ - 50,000$","50,000$ - 60,000$","60,000$ - 70,000$","Above 70,000$","<optgroup label='Hour Wise'>","Lessthan 40$/hr","40$/hr - 50$/hr","50$/hr - 60$/hr","60$/hr - 70$/hr","70$/hr - 80$/hr","80$/hr - 90$/hr","90$/hr - 100$/hr","Above 100$/hr"):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q
@register.simple_tag
def SelectEmpQualification(sel):
	s=[i.strip() for i in sel.split(',')]
	str_q='<select name="qualification" multiple style="width:260px;"><option value="">Select</option>'
	for i in ("Military service","High school","Associate","Pre- Bachelor's","Bachelor's","Post-Bachelor's","Masters","Post- Masters","PHD - Doctorate","MBA"):
		if i in s:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q



@register.simple_tag
def SelectEmpCountry(sel):
	str_q='<select name="country" id="country" onChange="setStates();" style="width:260px;" required="true"><option value="">Select</option>'
	for i in ('Australia','Bangladesh','Canada','India','Malaysia','Mexico','Saudi Arabia','United Arab Emirates','United Kingdom','United States'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q

@register.simple_tag
def SelectEmpState(sel):
	str_q='<select name="state" id="state" onChange="setCities();" style="width:260px;" required="true"><option value="">Select</option>'
	for i in ('Australia','Bangladesh','Canada','India','Malaysia','Mexico','Saudi Arabia','United Arab Emirates','United Kingdom','United States'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q


@register.simple_tag
def secret(sel):
	str_q='<select name="jssecretclear" class="input-xlarge" ><option value="">Select</option>'
	for i in ('None','Public Trust','NACI','ADP1/IT1','ADP2/IT2','Confidential','DOE L','DOE Q','Secret','Top Secret','Top Secret/SCI','Top Secret/SCI CI Polygeaph','Top Secret/SCI Full Scope Polygeaph','Other Clearance'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q
@register.simple_tag
def resactbtn(sel):
	from registration.models import JSResumeActive
	if JSResumeActive.objects.filter(resumeActive_id=sel):
		return '<a class="btn btn-mini btn-success activeresume" data-resumeid="%d" href="#">Make it deactive</a>' %sel
	else:return '<a class="btn btn-mini btn-danger activeresume" data-resumeid="%d" href="#">Make it active</a>' %sel

@register.simple_tag
def jobstatus(sel):
	from registration.models import jobs
	from datetime import datetime
	if jobs.objects.filter(id=sel,todate__gte=datetime.now().date(),marklive__lte=datetime.now().date(),is_active=True):return 'Active'
	elif jobs.objects.filter(id=sel,marklive__gt=datetime.now().date(),is_active=True):return 'Future'
	else:return 'Inactive'
@register.simple_tag
def ownername(sel):
	from registration.models import jobs
	a=[]
	s=''
	for job in jobs.objects.filter(emp_id=sel,is_delete=False):
		if job.ownername not in a:
			a.append(job.ownername)
			s+='<option value="%s">%s</option>' %(job.ownername,job.ownername)
	return s
@register.simple_tag
def refcode(sel):
	from registration.models import jobs
	s=''
	for job in jobs.objects.filter(emp_id=sel,is_delete=False):
		s+='<option value="%s">%s</option>' %(job.referencecode,job.referencecode)
	return s
@register.simple_tag
def jobtitle(sel):
	from registration.models import jobs
	s=''
	for job in jobs.objects.filter(emp_id=sel,is_delete=False):
		s+='<option value="%s">%s</option>' %(job.title,job.title)
	return s
@register.simple_tag
def profileimg(n):
	return "success"

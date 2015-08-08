TOPICS_DATA=(
		('General Purpose','cast'),
		('Products','cchip'),
		('Telecommunication','ctech'),
		('Pharmaceutical','czoo'),
		('Graphics','csun'),
		('Business','cbio'),
		('Gaming','cgame'),
		('Only Visible to Other Recruiter or JobSeeker','cbot'),
		('Science','cst'),
		)
#User(username,email,first_name,last_name,EMPLOYER/JOBSEEKER)
USERS_DATA=(
		("suhailvs","suhailvs@gmail.com","Suhail","VS","e"),
		("jani","suhailvs0@gmail.com","Jani","Hashmi","e"),
		("sumesh","suhailvs1@gmail.com","Sumesh","Jacob","j"),
		("sumee","suhspams@gmail.com","Sumee","vs","j"),
		("anoop","suhfiles@gmail.com","Anoop","T","j"),
	)

#Question(user, topic, question)
QUESTIONS_DATA=(
		("suhailvs",9,
			"""
			I was attending my philosophy class and in the middle 
			of student presentations, I found myself mentally 
			wondering off and thinking about light. 
			After a few minutes of trying to piece together 
			how the sun works I came to ask a question I could 
			not answer myself. Why does each individual photon 
			have such a low amount of energy? I am hit by photons 
			all day and I find it amazing that I am not vaporized. 
			Am I simply too physically big for the photons to harm 
			me much, or perhaps the Earth's magnetic field filters 
			out enough harmful causes such as gammy rays?
			"""),

		("suhailvs",7, 
			"""
			Is anyone eagerly anticipating the unveiling 
			of the new xbox 720 today? This could almost be in the 
			'News' section making a much needed diversion 
			from gay marriage debates and broken britian.
			"""),		
		("jani",9, 
			"""
			The ordinary adult never bothers his head about 
			the problems of space and time. These are things he 
			has thought of as a child. But I developed so slowly 
			that I began to wonder about space and time only when 
			I was already grown up. Consequently, I probed more 
			deeply into the problem than an ordinary child would have.
			"""),
		("jani",9,
			"""
			Is the world near to its end?"""),
		("jani",9,
			"""
			Does red light block infrared?
			How to mask infrared vision"""),
		("suhailvs",7, 
			"""
		Is gravity part of physics?
		I'm have to complete a science assignment and I want to do it on gravity but I want to make sure gravity is part of physics, physical world, thanks."""),
		)

		#(0,7, 
		#	"""
		#
		#	"""),



#Answer(user,question,answer)
ANSWERS_DATA=(
		("sumesh",1,
			"""
			Slightly off topic, but in 'Profiles of the future', when talking about the possibility of invisibility, 
			Arthur C Clarke says 'An invisible man wouldn't just be blind, he would be dead'. 
			At first I misinterpreted this as saying any 'inivisibility potion' would kill you.
			But what it is saying is that normal light would disrupt the processes going on in your cells too much, so its a good thing you've got a fairly opaque skin to keep it out.
		"""),
		("sumesh",1,
			"""
			Individual photons are very small and don't have much energy. If you put a lot of them together in one place you can hurt somebody - 
			by simply supplying enough power to melt an object (ask any spy on a table underneath a laser beam). 
			There is another very odd feature of photons. Although lots of them can provide a lot of energy and heat an object, it takes an individual photon of enough energy to break a chemical bond. 
			So while a single high-energy ultraviolet photon can break a molecule in your skin and cause damage, a billion lower energy visible photons hitting the same point can't break that single bond. 
			Even though they together carry much more energy, it is the energy that is delivered in a single photon that matters in chemistry.
			Fortunately the Earth's atmosphere shields us from the photons with enough energy to break most chemical bonds.
			"""),
		("sumesh",1,
			"""
			I have a somewhat non-physics answer for you. 
			If you allow me to broaden your question a bit to "why doesn't light kill or otherwise make all life on 
			Earth impossible" the answer is that the Earth is in what we call "the habitable zone".

			If the Sun produced so much light or light at such high energies that it would kill you, 
			it also would heat the planet so much that liquid water would not be possible. 
			In this case, it's probably reasonable to argue via the "anthropic principle" 
			that we live on a planet in the habitable zone because otherwise we wouldn't exist to ask such questions. 
			Note of course too that we've defined the habitable zone based on our own life parameters 
			so there is a bit of a circular definition here.
			"""),			
		("anoop",1,
			"""
			This question is more interesting than I thought at first. 
			I like it. There are several different parts to an answer to this question; 
			I'll just contribute a couple that have something in common:
			our bodies (and everything else, it has nothing to do with bodies)
			also emit photons about as fast as they absorb them.

			On the macroscopic/thermal scale, 
			we have black-body radiation. Via black-body radiation, 
			all matter emits a continuous spectrum of radiation. 
			The distribution of this spectrum depends primarily on 
			the temperature of the object. This is why objects placed 
			in a fire appear to glow red, whether they be wood or metal or rocks. 
			Our bodies also emit radiation this way, but at our temperature, 
			this spectrum is in the infrared range, so it isn't visible 
			(to humans snakes can see body heat). Since everything absorbs 
			and emits photons this way, there's an equilibrium where we 
			receive as much thermal energy as we lose, although that's only 
			in an environment where everything is at equilibrium. 
			Hot things like the sun and incandescent lights can throw this 
			off, which is why it feels hot to go outside... or to 
			be under a heat lamp. Anyway, don't worry about filling 
			up on too many photons, they leave you just as fast.

			On the microscopic scale, we have the hard-to-spell
			phenomenon of fluorescence. When a high-energy photon 
			is absorbed by an atom, some of its energy can be 
			reemitted as a lower-energy photon. Of course, 
			this doesn't happen every time, and I don't know if it 
			happens much in our bodies. It depends on the material's 
			properties. That's where we get fluorescent lights and 
			pigments and laundry detergents detergent manufacturers 
			actually include fluorescent pigments in their products 
			so that clothes emit more visible light than they 
			physically should by absorbing UV light and reemitting 
			it in the visible range. Anyway, while I'm not sure if 
			that principle in particular saves you from atomization, 
			it's worth remembering that not every photon that hits you 
			stays there.

			So in conclusion, even though the energy that light 
			brings to our bodies (and the earth) is substantial 
			(imagine if there were no sun radiation is important!), 
			we're not going to fill up on photons to bursting. We're 
			at equilibrium.
			"""),
		("anoop",2,
			"""
			lol society. I'm also happy with my Nokia 3310.
			TBH I'd like to see whats new with the xbox but 
			expect it'll be at least 2 years before I get one. 
			I cant beleive we'll be at the point whereby we 
			look at our old 360s with the sort of disdain usually 
			reserved for a PS1 or original Xbox.
			Xbox 360 - appearing at a car boot near you! 
			"""),
		("anoop",3,
			"""
			I thought that Einstein said it wonderfully!
			None the less, as we grow older we find ourselves 
			having to focus on day to day problems and don't 
			have the time or energy to just wonder about stuff.

			On the other hand children don't have the knowledge 
			nor the skills to really dig in to the things they 
			have time to wonder about.

			Einstein notes that he had the ability to 
			wonder AND the tools to unravel that which he wondered about.

			I'm thinking that my version is far less understandable 
			than his.
			"""),
)		
#		("anoop",4,
#			"""
#
#			"""),
#		("anoop",5,
#
#			)
#		("anoop",6,
#
#			),
#		("sumesh",4,
#
#			),
#		("sumesh",4,
#
#			),
#total user:5, total topics:9


################################################
##  fixtures for letter templates  #############
################################################

#employers suhailvs,jani
LETTERTEMPLATES=(
		("suhailvs","SAMPLE RECRUITMENT LETTER 1",
		"""
date
address
Dear contact person

I am a recruiter for the [name] Fire Department. Our
Department is hiring for the position of firefighter and I
am disseminating information about this opportunity.
Firefighting requires candidates who are team players, self-
motivated, physically fit, enjoy working with people, and
are determined to succeed at whatever they do. My Fire
Department is actively seeking candidates including women
and minorities.
Prerequisites for the position of firefighter include the
following: [age], [education], [EMT or paramedic license],
[residence], [firefighter certifications], [CA Drivers
License], and [other]. I would like to schedule a time to
visit your campus [or facility] to discuss this opportunity
and distribute literature. If a visit is not possible,
please distribute the enclosed brochures and display the
posters in an appropriate location.
Firefighting is an exciting and rewarding career. I am sure
that many of your students [or clients] would be interested
in this career and ultimately find satisfaction as a
firefighter, if they are made aware of the opportunity.
Thank you for your time and attention. Please contact me at
your earliest availability to discuss potential recruitment
efforts. I am available at [phone number or email].
Sincerely,
[name and position] 
		""",
		),
		("jani","SAMPLE RECRUITMENT LETTER 1",
		"""
Dear [contact person]:
It is my pleasure to invite you to participate in a one-day meeting to assess our local
public health system. The meeting will be conducted as a retreat at the
[Location] on,[Date]. 

It will be held from [FromTime] until [EndTime].
The meeting beginning promptly at [MeetingTime]. Lunch will be provided.
The	[InsertHealthDepartmentHere] is one of numerous health departments in the state
of (Insert State Here) participating in the CDCs National Public Health Performance
Standards Program to strengthen	public	health	systems. As you are aware, a public
health system is made up of all public, private and voluntary entities that contribute to
the delivery of essential public health services within a jurisdiction. In order to
measure the performance of our local public health system, it is important to have re
presentatives from organizations and sectors that are involved in our local
public health system.

CDC	will analyze our completed assessment, and feedback will be provided in the form of a
report that can be used to identify strengths and weaknesses both locally and statewide.
I am enclosing(a copy of the assessment) AND (informational materials)
so that	you may	begin preparing for our	meeting.
Also, directions to	(Insert Meeting LocationHere) are enclosed.

Please RSVP no later than (Insert Date Here) 2013, by email to
(Insert Contact	Nameand Information	Here), or by calling
(Insert	Contact	Name Here)	at (Insert Contact Information Here).

I look forward to having you join together with other community
partners to take a close look at our public health system.
Sincerely,
		"""	),
		("jani","Virgin Islands Acknowledge1",
		"""
Thank you for sending your resume/application for the position on the campus of the University of the Virgin Islands. 
We have received many applications for this position and the screening process is still in progress. 
The	search committee is reviewing your documentation and will notify you if you are selected for an interview.
		"""),
		("jani","Virgin Islands Acknowledge2",
		"""
We have received your application materials for the position of .
Application materials will be reviewed over the next few weeks. We expect to contact candidates for interviews
during the week of .
Thank you for expressing an interest in the position
		"""),
		("jani","Virgin Islands Acknowledge3",
		"""
		I am writing to acknowledge receipt of your resume and letter of application for the position of on the campus of
the University of the Virgin Islands. Once the application deadline has passed, all completed applications will be
forwarded to the Selection Committee for review and ranking. The top candidates will be interviewed; off-island
candidates will be interviewed via tele-conference. Final interview(s) will be in person.
Thank you for your interest in the University of the Virgin Islands
		"""),
		("jani","Missing Documents Letter",
		"""
Thank you for sending your resume/application/letter of application for the position of on the campus of the
University of the Virgin Islands. After reviewing your application materials, we found that the following documents
are missing:
_____Letters of recommendation
_____Official transcripts
_____Other________________________________________
Please submit the missing documents as soon as possible, and no later than .
Thank you for your interest in the University of the Virgin Islands
"""),
		("jani","Not Interviewed 1",
		"""
Thank you for giving us the opportunity to review your credentials for the position of on the campus of the
University of the Virgin Islands. However, after reviewing all of the application materials received for this position,
we have determined that other applicants have qualifications that more closely fit our department's needs.
Please accept our good wishes, and thank you for your interest in the University of the Virgin Islands.
OR for employee applicants
We wish you continued success in your career at the University of the Virgin Islands
"""),
		("jani","Not Interviewed 2",
		"""
Thank you for your interest in employment with the University of the Virgin Islands.
The screening progress for the position of has been completed. We received many applications from candidates
with relevant experience and training. We carefully reviewed your application and resume and were impressed
with your credentials. However, we have identified candidates whose experience more closely match our
requirements. Your application materials will be sent to our Human Resources Department and kept on file for
six months.
Please accept our best wishes for success in your career.
"""),
		("jani","Interviewed 1",
		"""
Thank you for meeting with us to discuss your qualifications for the position of on the of the University of the Virgin
Islands.
We were fortunate to have many/several qualified candidates for our position and met with each of the top
candidates. However, we decided that the credentials of another candidate are more appropriate to our needs.
Please accept our best wishes and thank you for your interest in the University of the Virgin islands.
OR for employee candidates
We wish you continued success in your career at the University of the Virgin Islands. 
"""),		
		("jani","Interviewed 2",
		"""
Thank you for your interest in the position of on the of the University of the Virgin Islands.
After careful review of your application materials (i.e. relevant work experience, educational background, interviews,
and reference checks), we selected another candidate whose qualifications more closely fit the position.
Your application materials will be kept on file for six months,
I trust that the outcome f the process does not discourage you from seeking employment with University in the
future. Thank you for showing interest in working at UVI.
"""),
)


#def loadcaptca():
	#x=urllib.urlopen('http://api.textcaptcha.com/47v6jb6y8zgg8ok0kcwg88gok2qk6je9')
	#ans=x.readlines()
	#return ans[0].split('<question>')[1].split('</question>')[0]
CAPTCHAS=(
		("The 3rd letter in 'stumping' is?","u"),
		("Soup, house, finger or house: the body part is?","finger"),
		("Which word IN this sentence is all in capitals?","in"),
		("The 2nd colour in blue, arm, yellow and lion is?","yellow"),
		("The number of body parts in the list butter, chin, shorts and school is?","1,one"),
		("Sunday, Thursday or Tuesday: which day is part of the weekend?","thursday"),
		("What is the 4th digit in 7303214?","3,three"),
		("Which in this list is the name of a person: shorts, school, sock, duck or David?","david"),
		("Which of bee, hand, ant or egg is a body part?","hand"),
		("The list chin, toe, bee, bank, stomach and elephant contains how many body parts?","3,three"),
		("One add four equals ?","five,5"),
		("Of the numbers forty six, 69, thirty three, 57 or forty, which is the largest?","69,sixty nine,sixtynine"),
		("What is thirty eight thousand one hundred and twenty nine as a number?","38129"),
		("99, 1, eighty four, 61 or 14: which of these is the highest?",""),
		("What is sixty thousand and ninety eight as digits?",""),
		("Which of 12, 54, 87, eighty, seventy nine or 71 is the lowest?",""),
		("15 - 5 is what?",""),
		("What day is today, if tomorrow is Saturday?",""),
		("Richard&apos;s name is?",""),
		("The list shirt, white, brain, yellow, green and pink contains how many colours?",""),
		("If the chin is brown, what colour is it?",""),
		("Which of fifty eight, 76 or two is the largest?",""),
		("Which of 38, fourteen, 41 or 25 is the largest?",""),
		("Which of twenty four, seventy one, seventy two, eighty four or fifty five is the largest?",""),
		("What is forty three thousand six hundred and ninety five as a number?",""),
		("Butter, arm, cheese, head and house: how many body parts in the list?",""),
		("The 1st number from 40, fifteen, thirty one, 2 and twenty eight is?",""),
		("Susan&apos;s name is?",""),
		("The list yellow, green, blue, brown, white and sweatshirt contains how many colours?",""),
		("Jennifer&apos;s name is?",""),
		("How many colours in the list chest, blue, yellow, hotel and purple?",""),
		("What is fifty two thousand one hundred and seventy nine as a number?",""),
		("The list church, T-shirt, arm, dress, ear and pub contains how many body parts?",""),
		("The purple elbow is what colour?",""),
		("The 2nd number from twenty, 32, seven and 11 is?",""),
		("What is the 7th digit in 2459376?",""),
		("73, forty one or thirty eight: the largest is?",""),
		("What number is 3rd in the series 4, 35 and 3?",""),
		("Which digit is 7th in the number 6767538?",""),
		("The list blue, butter and mosquito contains how many colours?",""),
		("What is Ruth&apos;s name?",""),
		("What is seventy eight thousand eight hundred and fifty six as a number?",""),
		("Enter the lowest number of 34, thirty five, 53, seventy two, 99 or 22:",""),
		("Fifty four, thirty, eighty three, eighty two, 79 or seventy seven: which of these is the smallest?",""),
		("If the elephant is brown, what colour is it?",""),
		("What is six thousand five hundred and eighty six as a number?",""),
		("What is the 2nd digit in 4346231?",""),
		("If the bank is green, what colour is it?",""),
		("Enter the number fifty three thousand two hundred and fifty five in digits:",""),
		("If a person is called Thomas, what is their name?",""),
		("Enter the number twenty one thousand and seventy six in digits:",""),
		("Of the numbers forty four, 76, eighty one or sixty five, which is the biggest?",""),
		("Ear, heart, face and sweatshirt: how many body parts in the list?",""),
		("Enter the lowest number of 66, nineteen, 10, eighty six, forty seven or forty three:",""),
		("The name of Edward is?",""),
		("Which digit is 1st in the number 8440033?",""),
		("Which of seventeen, 70, 87, 25, 70 or 47 is the lowest?",""),
		("How many colours in the list brown, lion and bee?",""),
		("The 4th number from 24, 35, 31 and 23 is?",""),		
	)


FEEDLINKS=(
	('Engadget','http://feeds.engadget.com/weblogsinc/engadget'),
('The Verge','http://www.theverge.com/rss/index.xml'),
('Mashable','http://feeds.mashable.com/Mashable'),
('Tech Radar','http://feeds.feedburner.com/techradar/allnews?format=xml'),
('Maximum Pc','http://www.maximumpc.com/articles/all/feed'),
('Greek','http://www.geek.com/feed/'),
('Boing Boing','http://feeds.boingboing.net/boingboing/iBag'),
('Read Write','http://readwrite.com/main/feed/articles.xml'),
('CDNL','http://cdnl.complex.com/feeds/channels/all.xml'),
('Business Insider','http://feeds.feedburner.com/businessinsider?format=xml'),
)

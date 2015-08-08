import feedparser
from BeautifulSoup import BeautifulSoup
from django import template
register = template.Library()

class FeedStory(object):
    def __init__(self,title,link,updated,summary):
        self.title,self.link,self.updated,self.rawsummary = (title,link,updated,summary)
        #dec_s=summary.encode('iso8859-1','ignore')        
        self.summary = BeautifulSoup(summary.encode('utf-8')) #summary

    def get_media(self):
    	#get picture url
        #------------------------------
    	for i in self.summary.findAll('img'):
    		mediaurl=i['src']
    		if mediaurl.strip()[-4:]=='.jpg': return mediaurl
    	return ''

    def get_summary(self):
    	#get the summary of the feed.
    	#------------------------------
    	try:
            p=self.summary.find('p')
            return ' '.join(p.findAllNext(text=True))
        except:return ''#self.rawsummary

    def get_html(self):
    	media=self.get_media()
    	
    	summary=self.get_summary()
    	if not (media or summary):return ''
    	#image caption
    	cap=self.title
        if len(cap)>53:cap=cap[:50]+'...'
        #------------------------------

        # add this to line47 for a strech result.style="width: 220px; height: 200px;"
    	return u'''
    	<td>
    		<a data-imgurl="{0}" data-headline="{1}" data-description="{2}"
        data-published="{3}" data-url="{4}" data-username="test" href="#myModal" 
        class="img-modal thumbnail">
        	<div class="wrapper">
        		<div class="clipwrapper">
        			<div class="clip">
        				<img src="{0}">
        			</div>
        		</div>
        		<div class="blackcaption">
        			<p>{5}</p>
        		</div>
        	</div>
        </td>
        '''.format(media,self.title,summary,self.updated,self.link,cap)
       

#this function uses a class which is inherited from Feedstory(look attr cl)
def createfeed(url,cl):
	#parse using feed parser
	#.......................			
	feed = feedparser.parse(url)
	entries = feed.entries

	#Only first 5 feeds
	if len(entries)>100:ne=100
	else:ne=len(entries)
	#.......................

	fd=[]
	for e in range(ne):
		f=dict()
		for i in ['title','link','updated','summary']:
			if i=="summary":
				try:f[i]=entries[e][i]
				except:
					try:f[i]=entries[e]['content'][2]
					except:f[i]=''
			else:
				try:f[i]=entries[e][i]
				except:f[i]=''
		fd.append(cl(f['title'],f['link'],f['updated'],f['summary']))
	return fd

@register.simple_tag
def get_feed_thumb(url):
    feeds=createfeed(url,FeedStory)
    str_f='<table><tr>\n'
    feedcounter=0
    for i,feed in enumerate(feeds):
        str_feed=feed.get_html()
        if str_feed:
            feedcounter+=1
            str_f+=str_feed
        else:continue
        if len(feeds)!=i+1 and (feedcounter%4==0):str_f+='</tr><tr>' #if 4 create new row		
    return str_f+'</tr></table>'

###########################################################
#####  MULTIPILE SELET BOX FOR USER TO ADD NEW FEEDS ######
###########################################################
@register.simple_tag
def frm_addfeed(usr):
    from feeds.models import FeedList,UsrFeeds
    allfeeds=FeedList.objects.all()
    #fd=UsrFeeds.objects.filter(user=usr)   #the feeds which user have
    #usrfeedsid=[f.feed.id for f in fd] 

    str_f='<optgroup label="Technology">'    
    for feed in allfeeds:        
        str_f+='<option value="%s"%s>%s</option>'%(feed.id,' id="selected"' if feed.have_feed(usr) else '',feed.name)
        #temp+=str(feed.have_feed(usr))+'-'+feed.name
    #temp+='-->'
    str_f+='</optgroup>'
    return str_f

                       
            
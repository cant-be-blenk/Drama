from datetime import datetime

from yattag import Doc

from files.helpers.get import *
from files.routes.wrappers import *

from .front import frontlist
from files.__main__ import app

@app.get('/rss')
@app.get('/feed')
@app.get('/rss/<sort>/<t>')
def feeds_user(sort='hot', t='all'):

	try: page = max(int(request.values.get("page", 1)), 1)
	except: page = 1

	ids, next_exists = frontlist(
		sort=sort,
		page=page,
		t=t,
		v=None,
		)
	
	posts = get_posts(ids)

	doc, tag, text = Doc().tagtext()

	with tag("feed", ("xmlns:media","http://search.yahoo.com/mrss/"), xmlns="http://www.w3.org/2005/Atom",):
		with tag("title", type="text"):
			text(f"{sort} posts from {SITE}")

		with tag("id"):
			text(SITE_FULL + request.full_path)
		with tag("updated"):
			text(datetime.now().isoformat()+"Z")
		doc.stag("link", rel="self", type="application/atom+xml", href=SITE_FULL + request.full_path)
		doc.stag("link", rel="alternate", type="text/html", href=SITE_FULL)

		for post in posts:
			with tag("entry", ("xml:base", SITE_FULL + request.full_path)):
				with tag("title", type="html"):
					text(post.realtitle(None))

				with tag("id"):
					text(post.permalink)

				with tag("updated"):
					if (post.edited_utc):
						text(datetime.utcfromtimestamp(post.edited_utc).isoformat()+"Z")
					else:
						text(datetime.utcfromtimestamp(post.created_utc).isoformat()+"Z")

				with tag("published"):
					text(datetime.utcfromtimestamp(post.created_utc).isoformat()+"Z")
				
				with tag("author"):
					with tag("name"):
						text(post.author_name)
					with tag("uri"):
						text(f'/@{post.author_name}')

				doc.stag("link", href=post.permalink)

				image_url = post.thumb_url or post.embed_url or post.url

				doc.stag("media:thumbnail", url=image_url)

				if len(post.body_html):
					with tag("content", type="html"):
						doc.cdata(f'''<img alt="{post.realtitle(None)}" loading="lazy" src="{image_url}"><br>{post.realbody(None)}''')

	return Response("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+ doc.getvalue(), mimetype="application/xml")

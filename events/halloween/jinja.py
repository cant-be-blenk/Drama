def bar_position():
	"""
	db = db_session()
	vaxxed = db.execute(text("SELECT COUNT(*) FROM users WHERE hw_zombie > 0")).one()[0]
	zombie = db.execute(text("SELECT COUNT(*) FROM users WHERE hw_zombie < 0")).one()[0]
	total = db.execute(text("SELECT COUNT(*) FROM "
		"(SELECT DISTINCT ON (author_id) author_id AS uid FROM comments "
			"WHERE created_utc > 1666402200) AS q1 "
		"FULL OUTER JOIN (SELECT id AS uid FROM users WHERE hw_zombie != 0) as q2 "
		"ON q1.uid = q2.uid")).one()[0]
	total = max(total, 1)

	return [int((vaxxed * 100) / total), int((zombie * 100) / total), vaxxed, zombie]
	"""
	
	return [1,1,1,1]
	
EVENT_JINJA_CONST = {
	"EVENT_BANNER": "banner_rDrama.html",
	"EVENT_STYLES": "spooky.css",
	"bar_position": bar_position()
}


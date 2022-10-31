from os import path
import subprocess
from importlib import import_module
from events.conf import *

def linkEventAssets():
	root = "/rDrama"
	assets = ["assets/css", "assets/js", "assets/fonts",\
	 "assets/images", "assets/media", "templates"]

	print("linking event assets...")
	
	for directory in assets:
		src = root + "/events/" + EVENT_NAME + "/" + directory
		dest = root + "/files/" + directory + "/event"

		try:
			if path.exists(dest):
				subprocess.run(["rm", dest])
				print("path " + directory + " already exists, removing")
				
			subprocess.run(["ln", "-s", src, dest])
			print("linked " + src + " -> " + dest)
		except Exception as e:
			print(e)

def loadModule(module):
	if not EVENT_ACTIVE: return None
	try: return import_module("events." + EVENT_NAME + module)
	except: return None

if EVENT_ACTIVE:
	linkEventAssets()
	
event = loadModule("")

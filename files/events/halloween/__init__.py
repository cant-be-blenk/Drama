from os import path
import subprocess

ROOT_PATH = "/rDrama/files/"
EVENT_PATH = "events/halloween/"
ASSET_PATHS = ["assets/css", "assets/js", "assets/fonts", "assets/images", "assets/media", "templates/"]

for asset_path in ASSET_PATHS:
	if not path.exists(ROOT_PATH+asset_path+"/halloween/"):
		subprocess.run(["ln", "-s", str(ROOT_PATH + EVENT_PATH + asset_path), str(ROOT_PATH + asset_path + "/halloween")])

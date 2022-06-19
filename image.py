from PIL import Image, ImageDraw, ImageFont
import sqlite3 as db

def create_background(img_width, img_height, color=(23,23,23)):
	return Image.new('RGB', (img_width, img_height), color=color)

def add_time(img, time):
	width, height = img.size
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('./data/fonts/arnamu_bold.ttf', 60)
	time_width, time_height = draw.textsize(time, font=font)
	
	draw.text( ((width - time_width)/2, 200 + 380), time, font=font, fill="white")
	return img

def add_result(img, home_goals, away_goals):
	width, height = img.size
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('./data/fonts/arnamu.ttf', 150)
	num_width, num_height = draw.textsize('1', font=font)
	dash_y = 400
	spacing = 50
	draw.text( (width/2 - spacing - num_width, dash_y), str(home_goals), font=font, fill="white")
	draw.text( (width/2 + spacing, dash_y), str(away_goals), font=font, fill="white")
	return img

def add_lines(img, line_width=3):
	width, height = img.size
	draw = ImageDraw.Draw(img, 'RGBA')
	alpha = 200
	spacing = 50
	draw.line((spacing, spacing, width - spacing + line_width/2, spacing), fill=(255,255,255,alpha), width=line_width)
	draw.line((width - spacing, spacing + 1 + line_width/2, width - spacing, height - spacing), fill=(255,255,255,alpha), width=line_width)
	draw.line((width - spacing - line_width/2, height - spacing + 1 - line_width/2, spacing, height - spacing + 1 - line_width/2), fill=(255,255,255,alpha), width=line_width)
	draw.line((spacing + line_width/2, height - spacing - line_width, spacing + line_width/2, spacing + 1 + line_width/2), fill=(255,255,255,alpha), width=line_width)

	return img

def add_logo(img):
	width, height = img.size
	logo = Image.open("./data/logo_main.png")
	wpercent = (250 / logo.size[0])
	hsize = int((logo.size[1] * wpercent))
	logo = logo.resize((250, hsize))
	img.paste(logo, (int((width - logo.size[0])/2), 100), logo)
	return img

def add_scorer(img, home_scorers, away_scorers):
	width, height = img.size
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('./data/fonts/arnamu.ttf', 40)
	test_width, test_height = draw.textsize('Սահակյան'.upper(), font=font)
	
	spacing = 200
	ball_spacing = 10
	scorers_spacing = 10
	for i in range(len(home_scorers)):
		ball_icon = Image.open("./data/icons/ball_icon.png").convert("RGBA")
		wpercent = test_height / ball_icon.size[0]
		hsize = int((ball_icon.size[1] * wpercent))
		ball_icon = ball_icon.resize((test_height, hsize))
	
		home_scorers[i] = home_scorers[i].upper()
		scorer_width, scorer_height = draw.textsize(home_scorers[i], font=font)
		img.paste(ball_icon, (spacing, 850 + i * (scorers_spacing + test_height)), ball_icon)
		draw.text( (spacing + ball_spacing + ball_icon.size[0], 850 + i * (scorers_spacing + test_height)), str(home_scorers[i]), font=font, fill="white")
		
	for i in range(len(away_scorers)):
		ball_icon = Image.open("./data/icons/ball_icon.png").convert("RGBA")
		wpercent = test_height / ball_icon.size[0]
		hsize = int((ball_icon.size[1] * wpercent))
		ball_icon = ball_icon.resize((test_height, hsize))
	
		away_scorers[i] = away_scorers[i].upper()
		scorer_width, scorer_height = draw.textsize(away_scorers[i], font=font)
		img.paste(ball_icon, (width - spacing - ball_icon.size[0], 850 + i * (scorers_spacing + test_height)), ball_icon)
		draw.text( (width - spacing - ball_spacing - ball_icon.size[0] - scorer_width, 850 + i * (scorers_spacing + test_height)), str(away_scorers[i]), font=font, fill="white")
		
	return img

def add_tournament(img, tournament):
	width, height = img.size
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('./data/fonts/arnamu_bold.ttf', 60)
	tournament_width, tournament_height = draw.textsize(tournament, font=font)
	
	draw.text(((width - tournament_width)/2, 300), tournament, font=font, fill="white")
	
	return img	

def add_teams(img, home_team, away_team, language):
	# Getting teams by id
	conn = db.connect('data/afg.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()

	home_team_name = c.execute("SELECT name_" + language + " from teams WHERE team_id is " + str(home_team)).fetchone()
	away_team_name = c.execute("SELECT name_" + language + " from teams WHERE team_id is " + str(away_team)).fetchone()

	conn.close()

	width, height = img.size
	
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('./data/fonts/arnamu_bold.ttf', 70)
	text = home_team_name + ' - ' + away_team_name	
	
	dash_width, dash_height = draw.textsize('-', font=font)
	dash_y = 450
	draw.text(( (width - dash_width)/2, dash_y), '-', font=font, fill="white")
	team_width = (width - dash_width)/2
	
	home_team_width, home_team_height = draw.textsize(home_team_name.upper(), font=font)
	away_team_width, away_team_height = draw.textsize(away_team_name.upper(), font=font)
	
	spacing = 200
	spacing_name = 30
	team_y = spacing + 450 + spacing_name
	
	draw.text( ((team_width - home_team_width)/2, team_y), home_team_name.upper(), font=font, fill="white")
	draw.text( ((team_width - away_team_width)/2 + team_width + dash_width, team_y), away_team_name.upper(), font=font, fill="white")
	
	home_team_logo = Image.open("./data/img/" + str(home_team) +".png")
	hpercent = home_team_logo.size[1] / 450
	wsize = int(home_team_logo.size[0] / hpercent)
	home_team_logo = home_team_logo.resize((wsize, 450))
	
	away_team_logo = Image.open("./data/img/" + str(away_team) + ".png")
	hpercent = away_team_logo.size[1] / 450
	wsize = int(away_team_logo.size[0] / hpercent)
	away_team_logo = away_team_logo.resize((wsize, 450))
	
	team_logo_y = 200
	
	img.paste(home_team_logo, (int( (team_width - home_team_logo.size[0])/2 ), team_logo_y), home_team_logo)
	img.paste(away_team_logo, (int( (team_width - away_team_logo.size[0])/2 + team_width + dash_width ), team_logo_y), away_team_logo)

	return img

def add_goal_team(img, team, text, language):
	conn = db.connect('data/afg.db')
	conn.row_factory = lambda cursor, row: row[0]
	c = conn.cursor()

	team_name = c.execute("SELECT name_" + language + " from teams WHERE team_id is " + str(team)).fetchone()
	conn.close()

	width, height = img.size
	
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('./data/fonts/arnamu_bold.ttf', 150)
	text_width, text_height = draw.textsize(text.upper(), font=font)

	team_logo = Image.open("./data/img/" + str(team) +".png")
	hpercent = team_logo.size[1] / 450
	wsize = int(team_logo.size[0] / hpercent)
	team_logo = team_logo.resize((wsize, 450))

	spacing = 60
	img.paste(team_logo, ((int((width/2 - (team_logo.size[0] + spacing + text_width)/2))), int(height/2 - team_logo.size[1]/2)), team_logo)

	width_1 = width/2 - (team_logo.size[0] + spacing + text_width)/2 + team_logo.size[0] + spacing
	height_1 = height/2 - text_height/2
	draw.text((width_1, height_1), text.upper(), font=font, fill="white")

	return img
	
from django import forms

class NombreMesForm(forms.Form):
	nombre_mes = forms.CharField(label='Nombre del mes', max_length=100)

#opciones para el formulario y la clase que lo representa
CHOICES = [('Challenger', 'Challenger'),
	   ('GrandMaster', 'GrandMaster'),
	   ('Master',  'Master'),
	   ('Diamond', 'Diamond'),
	   ('Platinum', 'Platinum')]

class EloForm(forms.Form):
	elo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

CHAMPS = [('Aatrox', 'Aatrox'), ('Ahri', 'Ahri'), ('Amumu', 'Amumu'), 
	  ('Annie', 'Annie'), ('Ashe', 'Ashe'), ('AurelionSol', 'AurelionSol'), ('Azir', 'Azir'),
	  ('Blitzcrank', 'Blitzcrank'), ('Brand', 'Brand'), ('Braum', 'Braum'), ('Caitlyn', 'Caitlyn'),
	  ('ChoGath', 'ChoGath'), ('Darius', 'Darius'), ('Diana', 'Diana'), ('DrMundo', 'DrMundo'),
	  ('Ekko', 'Ekko'), ('Ezreal', 'Ezreal'), ('Fiora', 'Fiora'), ('Fizz', 'Fizz'),
	  ('Gangplank', 'Gangplank'), ('Graves', 'Graves'), ('Irelia', 'Irelia'), ('Ivern', 'Ivern'),
          ('Janna', 'Janna'), ('JarvanIV', 'JarvanIV'), ('Jax', 'Jax'), ('Jayce', 'Jayce'),
          ('Jhin', 'Jhin'), ('Jinx', 'Jinx'), ('KaiSa', 'KaiSa'), ('Karma', 'Karma'),
	  ('Kassadin', 'Kassadin'), ('Kayle', 'Kayle'), ('KhaZix', 'KhaZix'), ('Kindred', 'Kindred'),
          ('KogMaw', 'KogMaw'), ('Leblanc', 'Leblanc'), ('Leona', 'Leona'), ('Lucian', 'Lucian'),
          ('Lulu', 'Lulu'), ('Lux', 'Lux'), ('Malphite', 'Malphite'), ('Malzahar', 'Malzahar'),
	  ('Maokai', 'Maokai'), ('MasterYi', 'MasterYi'), ('MissFortune', 'MissFortune'), ('Mordekaiser', 'Mordekaiser'), 
	  ('Nami', 'Nami'), ('Nasus', 'Nasus'), ('Nautilus', 'Nautilus'), ('Neeko', 'Neeko'), 
	  ('Nocturne', 'Nocturne'), ('Olaf', 'Olaf'), ('Ornn', 'Ornn'), ('Poppy', 'Poppy'), 
	  ('Rakan', 'Rakan'), ('RekSai', 'RekSai'), ('Renekton', 'Renekton'), ('Rumble', 'Rumble'),
	  ('Senna', 'Senna'), ('Shaco', 'Shaco'), ('Shen', 'Shen'), ('Singed', 'Singed'),
	  ('Sion', 'Sion'), ('Sivir', 'Sivir'), ('Skarner', 'Skarner'), ('Sona', 'Sona'),
	  ('Soraka', 'Soraka'), ('Syndra', 'Syndra'), ('Taliyah', 'Taliyah'), ('Taric', 'Taric'),
	  ('Thresh', 'Thresh'), ('TwistedFate', 'TwistedFate'), ('Twitch', 'Twitch'), ('Varus', 'Varus'),
	  ('Vayne', 'Vayne'), ('Veigar', 'Veigar'), ('VelKoz', 'VelKoz'), ('Vi', 'Vi'),
	  ('Vladimir', 'Vladimir'), ('Volibear', 'Volibear'), ('Warwick', 'Warwick'), ('WuKong', 'WuKong'), 
	  ('Xayah', 'Xayah'), ('Xerath', 'Xerath'), ('XinZhao', 'XinZhao'), ('Yasuo', 'Yasuo'),
	  ('Yorick', 'Yorick'), ('Zed', 'Zed'), ('Ziggs', 'Ziggs'), ('Zoe', 'Zoe'),
	  ('Zyra', 'Zyra')]

class PopularItemForm(forms.Form):
	form_champ = forms.ChoiceField(choices=CHAMPS, widget=forms.Select)

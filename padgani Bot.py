import discord
from discord.ext import commands
from discord import app_commands
import json
import scripts.yearscript as yearscript
#Imports

yearscript = yearscript
year = 0
#Variable Declaration
path = 'data/data.json'
with open(path, 'r') as f:
        loaded_data = json.load(f)
#Loading Data To Begin

support = yearscript.getyear(loaded_data)
        
#Year Data

support_fascism = 0.0
base_support_democracy = 0.0
base_support_dictatorship = 0.0
base_support_oligarchy = 0.0
base_support_monarchy = 0.0
base_support_fascism = support[4]
base_support_democracy = support[3]
base_support_dictatorship = support[2]
base_support_oligarchy = support[1]
base_support_monarchy = support[0]


class Client(commands.Bot):
        async def on_ready(self):
                print(f'Logged on as {self.user}!')
                self.messages = []
                self.stop = False
                try:
                        guild = discord.Object(id=1338387544991334400)
                        synced = await self.tree.sync(guild=guild)
                        print(f'Synced {len(synced)} commands to guild {guild.id}')

                except Exception as e: 
                        print(f'Error syncing commands: {e}')
        
        async def on_message(self, message):
                if message.author ==  self.user and message.content.startswith('spam') and self.stop == False or message.author == self.user and message.content.startswith('Spam') and self.stop == False:
                        await message.channel.send(f'spam')
                else:
                        if message.content.startswith('spam') and not message.author == self.user or message.content.startswith('Spam') and not message.author == self.user:
                                self.stop = False
                                await message.channel.send(f'spam')

                if message.content.startswith('stop') or message.content.startswith('Stop'):
                        self.stop = True

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Client(command_prefix="!", intents=intents)



GUILD_ID = discord.Object(id=1338387544991334400)


@client.tree.command(name="nuke", description="Nukes DougDoug", guild=GUILD_ID)
async def nukeDougDoug(interaction: discord.Interaction):
        await interaction.response.send_message("Why'd you nuke DougDoug :(")

@client.tree.command(name="nuke_someone", description="Nukes someone of your choice", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, nukesomeone: str):
        await interaction.response.send_message(f'Nuked {nukesomeone}')

@client.tree.command(name="update", description="Update", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, update: str):
        await interaction.response.send_message(f'Update is successful with year change of {update}')
        update = int(update)
        cleaned_year = cleaned_year + update
        loaded_data.append('year' + cleaned_year)
        with open(path , 'w') as f:
                json.dump(loaded_data, f)


@client.tree.command(name="embed_test", description="Tests the embed", guild=GUILD_ID)
async def embed(interaction: discord.Interaction):
        embed = discord.Embed(title="I am an embed", description="I am the description", color=discord.Color.red())
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtnvAOajH9gS4C30cRF7rD_voaTAKly2Ntaw&s")
        embed.set_image(url="https://lh4.googleusercontent.com/6YQQy2Qte5dWtBkLGqH3pmkcdy4BT7_65kT26CBYUdnz96DFG4p4shBEngTNCC--iFEJtjHS7YMXJTJAMQNCCw3cBbysdi3pBRn20Pa9csskmosDcypHgP9c9gdoxw5y8g=w1280")
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="set_government", description="Changes your government", guild=GUILD_ID)
async def government(interaction: discord.Interaction, government: str):
        fascism_list = ['fascism', 'facism', 'fasism', 'naziism', 'nazism', 'fasism', 'facist', 'fascist', 'nazi', 'fashism', 'fashiom', 'fashisum', 'fashist', 'nazii', 'naziii']
        democracy_list = ['democracy', 'democratic', 'democrat', 'demicracy', 'democrats', 'demicracy', 'deemocratsy', 'democrasy', 'demotcracy']
        dictatorship_list = ['dictatorship', 'dictetership', 'communism', 'dictator', 'communist', 'comunism', 'comunist', 'dicteter', 'dictereship']
        monarchy_list = ['monarchy', 'monarky', 'monarcy', 'queen', 'king', 'royal', 'family', 'monarch', 'monark', 'monarc']
        oligarchy_list = ['oligarchy', 'oligarky', 'oligarcy', 'oligarcky', 'oligarkie', 'oligarchie', 'oligarkie', 'oligarch', 'oligark', 'oligarc', 'oliegarchy', 'oliegarch', 'oliharhy', 'olicarcie']
        furry_list = ['furaffinity', 'furafinity', 'furry']
        if government.lower() in fascism_list:
                ignore = [1339439363234332702]
                roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                roles = str(roles)
                cleaned_roles = roles.strip("[]")
                cleaned_roles = str(cleaned_roles)
                cleaned_roles = cleaned_roles.replace("'", "")   
                resultfas = [i for i in loaded_data if i.startswith('1' + cleaned_roles)]
                if resultfas:             
                        support_fascism = resultfas[-1][len('1' + cleaned_roles):]
                else:
                        support_fascism = base_support_fascism
                        if support_fascism > 49:
                                await interaction.response.send_message('You are now Fascist')
                                with open(path, 'w') as f:
                                        ignore = [1339439363234332702]
                                        roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                                        roles = str(roles)
                                        cleaned_roles = roles.strip("[]")
                                        cleaned_roles = str(cleaned_roles)
                                        cleaned_roles = cleaned_roles.replace("'", "")
                                        loaded_data.append(cleaned_roles + 'Fascism')
                                        json.dump(loaded_data, f)
                        else:
                                await interaction.response.send_message(f'You do not have enough support for that. Your current Fascism support is{support_fascism}')
        elif government.lower() in democracy_list:
                await interaction.response.send_message("You are now a Democracy")
                with open(path, 'w') as f:
                        ignore = [1339439363234332702]
                        roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                        roles = str(roles)
                        cleaned_roles = roles.strip("[]")
                        cleaned_roles = str(cleaned_roles)
                        cleaned_roles = cleaned_roles.replace("'", "")
                        loaded_data.append(cleaned_roles + 'Democracy')
                        json.dump(loaded_data, f)
        elif government.lower() in dictatorship_list:
                await interaction.response.send_message('You are now a Dictatorship')
                with open(path, 'w') as f:
                        ignore = [1339439363234332702]
                        roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                        roles = str(roles)
                        cleaned_roles = roles.strip("[]")
                        cleaned_roles = str(cleaned_roles)
                        cleaned_roles = cleaned_roles.replace("'", "")
                        loaded_data.append(cleaned_roles + 'Dictatorship')
                        json.dump(loaded_data, f)
        elif government.lower() in monarchy_list:
                await interaction.response.send_message('You are now a Monarchy')
                with open(path, 'w') as f:
                        ignore = [1339439363234332702]
                        roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                        roles = str(roles)
                        cleaned_roles = roles.strip("[]")
                        cleaned_roles = str(cleaned_roles)
                        cleaned_roles = cleaned_roles.replace("'", "")
                        loaded_data.append(cleaned_roles + 'Monarchy')
                        json.dump(loaded_data, f)
        elif government.lower() in oligarchy_list:
                await interaction.response.send_message("You are now an Oligarchy")
                with open(path, 'w') as f:
                        ignore = [1339439363234332702]
                        roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                        roles = str(roles)
                        cleaned_roles = roles.strip("[]")
                        cleaned_roles = str(cleaned_roles)
                        cleaned_roles = cleaned_roles.replace("'", "")
                        loaded_data.append(cleaned_roles + 'Oligarchy')
                        json.dump(loaded_data, f)
        elif government.lower() in furry_list:
                await interaction.response.send_message("You are now a Furry")
                with open(path, 'w') as f:
                        ignore = [1339439363234332702]
                        roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                        roles = str(roles)
                        cleaned_roles = roles.strip("[]")
                        cleaned_roles = str(cleaned_roles)
                        cleaned_roles = cleaned_roles.replace("'", "")
                        loaded_data.append(cleaned_roles + 'Furry')
                        json.dump(loaded_data, f)
        else:
                await interaction.response.send_message(f'{government} is not an a valid government type. The valid government types are Fascist, Democracy, Dictatorship, Monarchy and Oligarchy')

@client.tree.command(name='query_government', description='sees your government', guild=GUILD_ID)
async def government(interaction: discord.Interaction):
        with open(path, 'r') as f:
                ignore = [1339439363234332702]
                roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                roles = str(roles)
                cleaned_roles = roles.strip("[]")
                cleaned_roles = str(cleaned_roles)
                cleaned_roles = cleaned_roles.replace("'", "")
                result = [i for i in loaded_data if i.startswith(cleaned_roles)]
                if result:
                        await interaction.response.send_message(f'Your ideology is {result[-1][len(cleaned_roles):]}')
                else:
                        await interaction.response.send_message(f'No ideology found assosiated with {cleaned_roles}')

@client.tree.command(name='tech', description='View tech tree', guild=GUILD_ID)
async def tech(interaction: discord.Interaction, catergory: str):
       warfare_list = ['warfare', 'war', 'army', 'weapons', 'wepons']
       production_list = ['production', 'produce', 'irrigation', 'iggorate']
       gathering_list = ['gathering', 'gather', 'shadoof', 'collect']
       information_technologies_list = ['information technologies', 'it', 'information', 'technology', 'tech', 'info', 'information']
       materials_list = ['materials', 'material', 'recource', 'recources']
       domestication_list = ['domestication', 'domestic', 'animals', 'domestic abuse']
       economy_list = ['economy', 'economic', 'economic tech', 'money']
       all_list = ['all', 'everything']
       other_list = ['other', 'other inventions', 'other_inventions', 'otherinventions', 'othen-inventions', 'misc', 'miscalanius', 'miscallanious', 'miscalanious', 'miscellaneous']
       if catergory.lower() in warfare_list:
              await interaction.response.send_message('Spears: 1 Research Point\n        Bronze Spears: 5 Research Points (Locked, Requires Spears, Bronze)\nAxes: 2 Reseach Points\n        Bronze Axes: 5 Research Points (Locked, Requires Axes, Bronze)\nClubs: 3 Reseach Points\n        Bronze Clubs: 5 Research Points (Locked, Requires Clubs, Bronze)\nBasic Defensive Foritifications: 10 Research Points\nChariots: 15 Research Points (Locked, Requires The Wheel)')
       elif catergory.lower() in production_list:
              await interaction.response.send_message('Irrigation: 5 Research Points\nDigging Sticks: 2 Research Points\nSickles: 3 Research Points\n        Bronze Sickles: 5 Research points (Locked, Requires Sickles)\nPlows: 10 Research Points (Locked, Requires Basic Farm Animals)')
       elif catergory.lower() in gathering_list:
              await interaction.response.send_message('Shadoof: 7 Reseach Points (Locked, Requires Lever),\nMore Advanced Gathering: 10 Research Points')
       elif catergory.lower() in information_technologies_list:
              await interaction.response.send_message('Reed Pens: 10 Research Points (Locked, Requires Ink)\n        Writing System: 15 Research points (Locked, Requires Reed Pens)\nCounting System: 20 Research Points (Locked, Requires Writing system)')
       elif catergory.lower() in materials_list:
              await interaction.response.send_message('Bronze: 10 Research Points, Gold: 15 Research Points, Tin: 5 Research Points, Copper: 5 Research Points, Clay: 5 Research Points')
       elif catergory.lower() in domestication_list:
              await interaction.response.send_message('Dog Domestication: 10 Research Points (Locked, Requires Basic Domestication Principles)\nHorse Domestication: 10 Research Points (Locked, Requires Basic Domestication Principles)\nBasic Farm Animals: 10 Reseach Points (Locked, Requires Basic Domestication Principles)')
       elif catergory.lower() in economy_list:
              await interaction.response.send_message('Bartering System: 10 Reseach Points\n        Trade Routes: 25 Research Points (Locked, Requires Bartering System)')
       elif catergory.lower() in other_list:
              await interaction.response.send_message('Ancient Calenders: 10 Research Points (Locked, Requires Counting System)\nPottery: 5 Research Points (Locked, Requires Clay)\nDomestication Principles: 10 Research Points (Locked, Requires Irrigation)\nThe Wheel: 20 Research Points\nLever: 10 Research Points (Locked, Requires More Advanced Gathering)\nInk: 5 Research Points (Locked, Requires More Advanced Gathering)')
       elif catergory.lower in all_list:
              await interaction.response.send_message('Spears: 1 Research Point\n        Bronze Spears: 5 Research Points (Locked, Requires Spears, Bronze)\nAxes: 2 Reseach Points\n        Bronze Axes: 5 Research Points (Locked, Requires Axes, Bronze)\nClubs: 3 Reseach Points\n        Bronze Clubs: 5 Research Points (Locked, Requires Clubs, Bronze)\nBasic Defensive Foritifications: 10 Research Points\nChariots: 15 Research Points (Locked, Requires The Wheel)\nIrrigation: 5 Research Points\nDigging Sticks: 2 Research Points\nSickles: 3 Research Points\n        Bronze Sickles: 5 Research points (Locked, Requires Sickles)\nPlows: 10 Research Points (Locked, Requires Basic Farm Animals)\nShadoof: 7 Reseach Points (Locked, Requires Lever),\nMore Advanced Gathering: 10 Research Points\nReed Pens: 10 Research Points (Locked, Requires Ink)\n        Writing System: 15 Research points (Locked, Requires Reed Pens)\nCounting System: 20 Research Points (Locked, Requires Writing system)\nBronze: 10 Research Points, Gold: 15 Research Points, Tin: 5 Research Points, Copper: 5 Research Points, Clay: 5 Research Points\nDog Domestication: 10 Research Points (Locked, Requires Basic Domestication Principles)\nHorse Domestication: 10 Research Points (Locked, Requires Basic Domestication Principles)\nBasic Farm Animals: 10 Reseach Points (Locked, Requires Basic Domestication Principles)\nBartering System: 10 Reseach Points\n        Trade Routes: 25 Research Points (Locked, Requires Bartering System)\nAncient Calenders: 10 Research Points (Locked, Requires Counting System)\nPottery: 5 Research Points (Locked, Requires Clay)\nDomestication Principles: 10 Research Points (Locked, Requires Irrigation)\nThe Wheel: 20 Research Points\nLever: 10 Research Points (Locked, Requires More Advanced Gathering)\nInk: 5 Research Points (Locked, Requires More Advanced Gathering)')
       else:
              await interaction.response.send_message('Available catergories are Warfare, Production, Gathering, Information Technologies, Materials, Domestication, Economy, Other and All')

@client.tree.command(name='invent_technology', description='Invent a new technology', guild=GUILD_ID)
async def leave(interaction: discord.Interaction, technology: str):
       tech_list = []
       result = (i for i in tech_list if i.startswith(technology))
       if result:
              print(result)
       else:
              await interaction.respnose.send_message('Technology could not be found. Use /tech to view the tech tree')

@client.tree.command(name='leave_country', description='Leave your current country', guild=GUILD_ID)
async def leave(interaction: discord.Interaction):
    guild = interaction.guild
    ignore = []
    
    roles_to_delete = [role for role in interaction.user.roles if role.id not in ignore and role.name != '@everyone']
    
    country_roles = [role_name for role_name in loaded_data if role_name.startswith('country')]
    
    roles_to_delete = [role for role in roles_to_delete if f'country{role.name}' in country_roles]
    
    if len(roles_to_delete) > 0:
        for role in roles_to_delete:
            try:
                await role.delete()
                await interaction.response.send_message(f'You have left the country: `{role.name}`')
                try:
                     loaded_data.remove('country' + str(role))
                except:
                       print('erm what')
                with open(path, 'w') as f:
                        json.dump(loaded_data, f)
            except discord.DiscordException as e:
                print(f'Failed to delete role {role.name}: {e}')
                await interaction.response.send_message(f'Failed to delete role `{role.name}`: {e}')
    else:
        await interaction.response.send_message(f'No country role to leave for {interaction.user.name}.')



@client.tree.command(name='create_country', description='Create a country', guild=GUILD_ID)
async def country(interaction: discord.Interaction, country: str, color: str = "#0000FF"):
    stop_stuff = False
    ignore = [1339439363234332702]
    roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name != '@everyone']
    
    country = country[0].upper() + country[1:].lower()

    if roles:
        await interaction.response.send_message(f'You already have a country. Current country is {", ".join(roles)}')
    else:

        guild = interaction.guild
        country_role = discord.utils.get(guild.roles, name=country)
        
        if country_role:  
                await interaction.response.send_message('That country already exists')
        else:

            bluevioletlist = ['blueviolet', 'blue violet', 'blue-violet', 'blue_violet']
            darkbluelist = ['dark blue', 'dark_blue', 'darkblue', 'dark-blue']
            darkcyanlist = ['dark cyan', 'darkcyan', 'dark_cyan', 'dark-cyan']
            darkgreylist = ['dark grey', 'dark_grey', 'darkgrey', 'dark-grey', 'dark gray', 'darkgray', 'dark_gray', 'dark-gray']
            darkgreenlist = ['dark green', 'darkgreen', 'dark_green', 'dark-green']
            darkmagentalist = ['dark magenta', 'dark_magenta', 'dark-magenta', 'darkmagenta']
            darkorangelist = ['dark orange', 'darkorange', 'dark_orange', 'dark-orange']
            darkredlist = ['darkred', 'dark_red', 'dark red', 'dark-red']
            darkvioletlist = ['darkviolet', 'dark violet', 'dark_violet', 'dark-violet']
            darkpinklist = ['darkpink', 'dark pink', 'dark_pink', 'dark-pink', 'deeppink', 'deep_pink', 'deep pink', 'deep-pink']
            dimgreylist = ['dimgrey', 'dim grey', 'dim_grey', 'dim-grey', 'dim gray', 'dimgray', 'dim_gray', 'dim-gray']
            forestlist = ['forest', 'darkforest', 'dark-forest', 'dark forest', 'dark_forest', 'forestgreen', 'forest green', 'forest_green', 'forest-green']
            greylist = ['grey', 'gray']
            greenyellowlist = ['greenyellow', 'green yellow', 'green_yellow', 'green-yellow', 'yellowgreen', 'yellow green', 'yellow_green', 'yellow-green']
            lightbluelist = ['lightblue', 'light blue', 'light_blue', 'light-blue']
            lightgreylist = ['lightgrey', 'light grey', 'light_grey', 'light-grey', 'light gray', 'lightgray', 'light_gray', 'light-gray']
            lightpinklist = ['lightpink', 'light pink', 'light_pink', 'light-pink']
            lightgreenlist = ['lightgreen', 'light green', 'light_green', 'light-green']
            lightyellowlist = ['light yellow', 'lightyellow', 'light_yellow', 'light-yellow']
            limegreenlist = ['limegreen', 'lime green', 'lime_green', 'lime-green']
            orangeredlist = ['orangered', 'orange red', 'orange_red', 'orange-red', 'redorange', 'red orange', 'red_orange', 'red-orange']
            yellowgreenlist = ['yellowgreen', 'yellow green', 'yellow_green', 'yellow-green', 'greenyellow', 'green yellow', 'green_yellow', 'green-yellow']

            if color.startswith('#'):
                try:
                        role_color = discord.Color(int(color.lstrip('#'), 16))

                except discord.DiscordException as e:
                        await interaction.response.send_message(f'An error occurred while creating the role: {e}')
            elif color.lower() == 'aqua':
                   role_color = discord.Color(int('00FFFF', 16))
            elif color.lower() == 'black':
                   role_color = discord.Color(int('000000', 16))
            elif color.lower() == 'blue':
                   role_color = discord.Color(int('0000FF', 16))
            elif color.lower() in bluevioletlist:
                   role_color = discord.Color(int('8A2BE2', 16))
            elif color.lower() == 'brown':
                   role_color = discord.Color(int('A52A2A', 16))
            elif color.lower() == 'coral':
                   role_color = discord.Color(int('FF7F50', 16))
            elif color.lower() == 'crimson':
                   role_color = discord.Color(int('DC143C', 16))
            elif color.lower() in darkbluelist:
                   role_color = discord.Color(int('00008B', 16))
            elif color.lower() in darkcyanlist:
                   role_color = discord.Color(int('008B8B', 16))
            elif color.lower() in darkgreylist:
                   role_color = discord.Color(int('A9A9A9', 16))
            elif color.lower() in darkgreenlist:
                   role_color = discord.Color(int('006400', 16))
            elif color.lower() in darkmagentalist:
                   role_color = discord.Color(int('8B008B', 16))
            elif color.lower() in darkorangelist:
                   role_color = discord.Color(int('FF8C00', 16))
            elif color.lower() in darkredlist:
                   role_color = discord.Color(int('8B0000', 16))
            elif color.lower() in darkvioletlist:
                   role_color = discord.Color(int('9400D3', 16))
            elif color.lower() in darkpinklist:
                   role_color = discord.Color(int('FF1493', 16))
            elif color.lower() in dimgreylist:
                   role_color = discord.Color(int('696969', 16))
            elif color.lower() in forestlist:
                   role_color = discord.Color(int('228B22', 16))
            elif color.lower() == 'gold':
                   role_color = discord.Color(int('FFD700', 16))
            elif color.lower() in greylist:
                   role_color = discord.Color(int('808080', 16))
            elif color.lower() == 'green':
                   role_color = discord.Color(int('008000', 16))
            elif color.lower() in greenyellowlist:
                   role_color = discord.Color(int('ADFF2F', 16))
            elif color.lower() == 'indigo':
                   role_color = discord.Color(int('4B0082', 16))
            elif color.lower() == 'ivory':
                   role_color = discord.Color(int('FFFFF0', 16))
            elif color.lower() in lightbluelist:
                   role_color = discord.Color(int('ADD8E6', 16))
            elif color.lower() in lightgreylist:
                   role_color = discord.Color(int('D3D3D3', 16))
            elif color.lower() in lightgreenlist:
                   role_color = discord.Color(int('90EE90', 16))
            elif color.lower() in lightpinklist:
                   role_color = discord.Color(int('FFB6C1', 16))
            elif color.lower() in lightyellowlist:
                   role_color = discord.Color(int('FFFFE0', 16))
            elif color.lower() == 'lime':
                   role_color = discord.Color(int('00FF00', 16))
            elif color.lower() in limegreenlist:
                   role_color = discord.Color(int('32CD32', 16))
            elif color.lower() == 'magenta':
                   role_color = discord.Color(int('FF00FF', 16))
            elif color.lower() == 'maroon':
                   role_color = discord.Color(int('800000', 16))
            elif color.lower() == 'navy':
                   role_color = discord.Color(int('000080', 16))
            elif color.lower() == 'olive':
                   role_color = discord.Color(int('808000', 16))
            elif color.lower() == 'orange':
                   role_color = discord.Color(int('FFA500', 16))
            elif color.lower() in orangeredlist:
                   role_color = discord.Color(int('FF4500', 16))
            elif color.lower() == 'orchid':
                   role_color = discord.Color(int('DA70D6', 16))
            elif color.lower() == 'pink':
                   role_color = discord.Color(int('FFC0CB', 16))
            elif color.lower() == 'purple':
                   role_color = discord.Color(int('800080', 16))
            elif color.lower() == 'red':
                   role_color = discord.Color(int('FF0000', 16))
            elif color.lower() == 'silver':
                   role_color = discord.Color(int('C0C0C0', 16))
            elif color.lower() == 'snow':
                   role_color = discord.Color(int('FFFAFA', 16))
            elif color.lower() == 'tan':
                   role_color = discord.Color(int('D2B48C', 16))
            elif color.lower() == 'teal':
                   role_color = discord.Color(int('008080', 16))
            elif color.lower() == 'tomato':
                   role_color = discord.Color(int('FF6347', 16))
            elif color.lower() == 'turquoise':
                   role_color = discord.Color(int('40E0D0', 16))
            elif color.lower() == 'violet':
                   role_color = discord.Color(int('EE82EE', 16))
            elif color.lower() == 'white':
                   role_color = discord.Color(int('FFFFFF', 16))
            elif color.lower() == 'yellow':
                   role_color = discord.Color(int('FFFF00', 16))
            elif color.lower() in yellowgreenlist:
                   role_color = discord.Color(int('9ACD32', 16))
            else:
                   stop_stuff = True
                   await interaction.response.send_message('To select a colour please select a hex code starting with # or type a colour out. Please note only a few colours are available if hex codes are not used. A list of the colours availabe without hex codes can be found with the command /colours')
            if stop_stuff == False:
                country_role = await guild.create_role(name=country, color=role_color)
                await interaction.user.add_roles(country_role)
                await interaction.response.send_message(f'You are now a part of {country}')
                loaded_data.append('country' + str(country_role))
                with open(path, 'w') as f:
                        json.dump(loaded_data, f)
@client.tree.command(name='colours', description='view available country colours', guild=GUILD_ID)
async def colours(interaction: discord.Interaction):
       await interaction.response.send_message('Available country colours are aqua, black, blue, blue-violet, brown, coral, crimson, dark blue, dark cyan, dark grey, dark green, dark magenta, dark orange, dark red, dark violet, dark pink, dim grey, forest, gold, grey, green, green-yellow, indigo, ivory, light blue, light grey, light green, light pink, light yellow, lime, lime-green, magenta, maroon, navy, olive, orange, orange-red, orchin, pink, purple, red, silver, snow, tan, teal, tomato, turquoise, violet, white, yellow, yellow-green')

@client.tree.command(name='increase_military', description='Increases your support for fascism', guild=GUILD_ID)
async def military(interaction: discord.Interaction):
        global support_fascism
        with open(path, 'w') as f:
                ignore = [1339439363234332702]
                roles = [role.name for role in interaction.user.roles if role.id not in ignore and role.name !='@everyone']
                roles = str(roles)
                cleaned_roles = roles.strip("[]")
                cleaned_roles = str(cleaned_roles)
                cleaned_roles = cleaned_roles.replace("'", "")
                resultfas = [i for i in loaded_data if i.startswith('1' + cleaned_roles)]
                if resultfas:
                        resultmon = [i for i in loaded_data if i.startswith('2' + cleaned_roles)]
                        if resultmon:
                                support_monarchy = resultmon[-1][len('2' + cleaned_roles):]
                                resultdi = [i for i in loaded_data if i.startswith('3' + cleaned_roles)]
                                resultde = [i for i in loaded_data if i.startswith('4' + cleaned_roles)]
                                resultol = [i for i in loaded_data if i.startswith('5' + cleaned_roles)]
                                support_dictatorship = resultdi[-1][len('3' + cleaned_roles):]
                                support_democracy = resultde[-1][len('4' + cleaned_roles):]
                                support_oligarchy = resultol[-1][len('5' + cleaned_roles):]
                        else:
                                support_monarchy = base_support_monarchy
                                support_democracy = base_support_democracy
                                support_dictatorship = base_support_dictatorship
                                support_oligarchy = base_support_oligarchy

                        support_fascism = resultfas[-1][len('1' + cleaned_roles):]
                        support_fascism = float(support_fascism)
                        support_monarchy = float(support_monarchy)
                        support_dictatorship = float(support_dictatorship)
                        support_democracy = float(support_democracy)
                        support_oligarchy = float(support_oligarchy)
                        no_run = False
                        if support_fascism < 11:
                                support_fascism = support_fascism + 9.0
                                divide_by = 9
                        elif support_fascism < 20:
                                support_fascism = support_fascism + 8.0
                                divide_by =8
                        elif support_fascism < 28:
                                support_fascism = support_fascism + 7.0
                                divide_by = 7
                        elif support_fascism < 35:
                                support_fascism = support_fascism + 6.0
                                divide_by = 6
                        elif support_fascism < 41:
                                support_fascism = support_fascism + 5.0
                                divide_by = 5
                        elif support_fascism < 46:
                                support_fascism = support_fascism + 4.0
                                divide_by = 4
                        elif support_fascism < 50:
                                support_fascism = support_fascism + 3.0
                                divide_by = 3
                        elif support_fascism < 53:
                                support_fascism = support_fascism + 2.0
                                divide_by = 2
                        elif support_fascism < 55:
                                support_fascism = support_fascism + 1.0
                                divide_by = 1
                        else:
                                await interaction.response.send_message('Your support for Fascism is maxed out')
                                no_run = True
                        if no_run == False:
                                total_support = support_monarchy + support_dictatorship + support_democracy + support_oligarchy
                                take_away = total_support / divide_by
                                monarchy_take_away = support_monarchy / take_away
                                support_monarchy = support_monarchy - monarchy_take_away
                                dictatorship_take_away = support_dictatorship / take_away
                                support_dictatorship = support_dictatorship - dictatorship_take_away
                                democracy_take_away = support_democracy / take_away
                                support_democracy = support_democracy - democracy_take_away
                                oligarchy_take_away = support_oligarchy / take_away
                                support_oligarchy = support_oligarchy - oligarchy_take_away
                                await interaction.response.send_message(f'Your support for fascism is now {support_fascism, support_monarchy, support_dictatorship, support_democracy, support_oligarchy}')

                                support_fascism = str(support_fascism)
                                support_monarchy = str(support_monarchy)
                                support_dictatorship = str(support_dictatorship)
                                support_democracy = str(support_democracy)
                                support_oligarchy = str(support_oligarchy)
                                loaded_data.append('1' + cleaned_roles + support_fascism)
                                loaded_data.append('2' + cleaned_roles + support_monarchy)
                                loaded_data.append('3' + cleaned_roles + support_dictatorship)
                                loaded_data.append('4' + cleaned_roles + support_democracy)
                                loaded_data.append('5' + cleaned_roles + support_oligarchy)
                                json.dump(loaded_data, f)
                else:
                        support_fascism = base_support_fascism
                        resultmon = [i for i in loaded_data if i.startswith('2' + cleaned_roles)]
                        if resultmon:
                                support_monarchy = resultmon[-1][len('2' + cleaned_roles):]
                                resultdi = [i for i in loaded_data if i.startswith('3' + cleaned_roles)]
                                resultde = [i for i in loaded_data if i.startswith('4' + cleaned_roles)]
                                resultol = [i for i in loaded_data if i.startswith('5' + cleaned_roles)]
                                support_dictatorship = resultdi[-1][len('3' + cleaned_roles):]
                                support_democracy = resultde[-1][len('4' + cleaned_roles):]
                                support_oligarchy = resultol[-1][len('5' + cleaned_roles):]
                        else:
                                support_monarchy = base_support_monarchy
                                support_democracy = base_support_democracy
                                support_dictatorship = base_support_dictatorship
                                support_oligarchy = base_support_oligarchy
                        support_fascism = float(support_fascism)
                        support_monarchy = float(support_monarchy)
                        support_dictatorship = float(support_dictatorship)
                        support_democracy = float(support_democracy)
                        support_oligarchy = float(support_oligarchy)
                        if support_fascism < 11:
                                support_fascism = support_fascism + 9.0
                                divide_by = 9
                        elif support_fascism < 20:
                                support_fascism = support_fascism + 8.0
                                divide_by =8
                        elif support_fascism < 28:
                                support_fascism = support_fascism + 7.0
                                divide_by = 7
                        elif support_fascism < 35:
                                support_fascism = support_fascism + 6.0
                                divide_by = 6
                        elif support_fascism < 41:
                                support_fascism = support_fascism + 5.0
                                divide_by = 5
                        elif support_fascism < 46:
                                support_fascism = support_fascism + 4.0
                                divide_by = 4
                        elif support_fascism < 50:
                                support_fascism = support_fascism + 3.0
                                divide_by = 3
                        elif support_fascism < 53:
                                support_fascism = support_fascism + 2.0
                                divide_by = 2
                        elif support_fascism < 55:
                                support_fascism = support_fascism + 1.0
                                divide_by = 1
                        else:
                                await interaction.response.send_message('Your support for Fascism is maxed out')
                        total_support = support_monarchy + support_dictatorship + support_democracy + support_oligarchy
                        take_away = total_support / divide_by
                        monarchy_take_away = support_monarchy / take_away
                        support_monarchy = support_monarchy - monarchy_take_away
                        dictatorship_take_away = support_dictatorship / take_away
                        support_dictatorship = support_dictatorship - dictatorship_take_away
                        democracy_take_away = support_democracy / take_away
                        support_democracy = support_democracy - democracy_take_away
                        oligarchy_take_away = support_oligarchy / take_away
                        support_oligarchy = support_oligarchy - oligarchy_take_away
                        await interaction.response.send_message(f'Your support for fascism is now {support_fascism, support_monarchy, support_dictatorship, support_democracy, support_oligarchy}')

                        support_fascism = str(support_fascism)
                        support_monarchy = str(support_monarchy)
                        support_dictatorship = str(support_dictatorship)
                        support_democracy = str(support_democracy)
                        support_oligarchy = str(support_oligarchy)
                        loaded_data.append('1' + cleaned_roles + support_fascism)
                        loaded_data.append('2' + cleaned_roles + support_monarchy)
                        loaded_data.append('3' + cleaned_roles + support_dictatorship)
                        loaded_data.append('4' + cleaned_roles + support_democracy)
                        loaded_data.append('5' + cleaned_roles + support_oligarchy)
                        json.dump(loaded_data, f)

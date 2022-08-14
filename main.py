import os

my_secret = os.environ['api_key']
import telebot

api_key = my_secret
my_secret = os.environ['api_key']

bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=['commands'])
def greet(message):
    bot.reply_to(message, "Welcome! I am the First Aid Crisis Bot. Please select one of the following commands so we can further assist you.\n\n\nLocations and Contacts: \n\n/hospitalnearme\n/emergencynumbers\n\nFirst Aid: \n\n/anaphylaxis\n/bleeding\n/choking\n/burn\n/fractures\n/nosebleed\n/insectbite\n/sprain\n/seizures\n\nCPR: \n\nCPR for child /cprchild\n\nCPR for adult /cpradult")

@bot.message_handler(commands=['hospitalnearme'])
def command_help(message):
    bot.reply_to(message, "Hospitals in your area: \nhttps://www.google.com/search?q=hospitals+near+me&oq=hospitals+near+me&aqs=chrome..69i57j0i402l2j0i512l7.5233j0j7&sourceid=chrome&ie=UTF-8 \nSelect /commands to go back to menu.")

@bot.message_handler(commands=['emergencynumbers'])
def command_help(message):
    bot.reply_to(message," 999 for Police.\n998 for Ambulance.\n997 for Fire Department (Civil Defence)\n996 for Coastguard.\n991 for electricity failure.\n922 for water failure.\nSelect /commands to go back to menu.")

@bot.message_handler(commands=['bleeding'])
def command_help(message):
    bot.reply_to(message,'''A severe allergic reaction (anaphylaxis) is life-threatening and requires urgent action. 

Lay the person flat – do not allow them to stand or walk.
Give adrenaline injector (such as EpiPen or Anapen) into the outer mid-thigh.
Phone an ambulance\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['anaphylaxis'])
def command_help(message):
    bot.reply_to(message,'''1. Stop Bleeding
Apply direct pressure on the cut or wound with a clean cloth, tissue, or piece of gauze until bleeding stops.
If blood soaks through the material, don’t remove it. Put more cloth or gauze on top of it and continue to apply pressure.
If the wound is on the arm or leg, raise limb above the heart, if possible, to help slow bleeding.
Wash your hands again after giving first aid and before cleaning and dressing the wound.
Do not apply a tourniquet unless the bleeding is severe and not stopped with direct pressure.
2. Clean Cut or Wound
Gently clean with soap and warm water. Try to rinse soap out of wound to prevent irritation.
Don’t use hydrogen peroxide or iodine, which can damage tissue.
3. Protect the Wound
Apply antibiotic cream to reduce risk of infection and cover with a sterile bandage.
Change the bandage daily to keep the wound clean and dry.
4. When to Call a Doctor
The wound is deep or the edges are jagged or gaping open.
The wound is on the person’s face.
The wound has dirt or debris that won’t come out.
The wound shows signs of infection, such as redness, tenderness, or a thick discharge, or if the person runs a fever.
The area around the wound feels numb.
Red streaks form around the wound.
The wound is a result of an animal or human bite.
The person has a puncture wound or deep cut and hasn’t had a tetanus shot in the past five years, or anyone who hasn’t had a tetanus shot in the past 10 years.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['choking'])
def command_help(message):
    bot.reply_to(message,'''Call for an ambulance.

1.    If patient is conscious, give up to 5 back blows 

With an adult or child, standing or sitting (and leaning forward), and using the heel of one hand, give the back blows between the patient’s shoulder blades. 
Check between each back blow to see if the item has been dislodged.
Place a baby face down on your lap for the back blows. Ensure you support the baby’s head. Give firm back blows, checking between each to see if the item is dislodged.
2.    If unsuccessful, give up to 5 chest thrusts

With an adult or child, standing or sitting, wrap both arms around the patient, at chest level. 
Place one fist with the thumb side against the middle of the breastbone. 
Grasp that fist with your other hand and give up to 5, separate, inward and upward thrusts. 
Check between each chest thrust to see if the item has been dislodged.
Place a baby face upwards on a firm surface and give up to 5 sharp chest thrusts just below the nipple line, checking between each thrust.
The back blows and chest thrusts are given separately with a check after each one to see if the obstruction has been relieved. 

3.    If the obstruction has not been relieved 

Ensure an ambulance has been called.
Continue alternating back blows and chest thrusts until the ambulance arrives. 
If the person becomes unresponsive, begin CPR.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['burn'])
def command_help(message):
    bot.reply_to(message,'''First aid for burns
Stop the burning process as soon as possible. This may mean removing the person from the area, dousing flames with water, or smothering flames with a blanket. Do not put yourself at risk of getting burnt as well.
Remove any clothing or jewellery near the burnt area of skin, including babies' nappies. But do not try to remove anything that's stuck to the burnt skin, as this could cause more damage.
Cool the burn with cool or lukewarm running water for 20 minutes as soon as possible after the injury. Never use ice, iced water, or any creams or greasy substances like butter.
Keep yourself or the person warm. Use a blanket or layers of clothing, but avoid putting them on the injured area. Keeping warm will prevent hypothermia, where a person's body temperature drops below 35C (95F). This is a risk if you're cooling a large burnt area, particularly in young children and elderly people.
Cover the burn with cling film. Lay the cling film over the burn, rather than wrapping it around a limb. A clean, clear plastic bag can be used for burns on your hand.
Treat the pain from a burn with paracetamol or ibuprofen. Always check the manufacturer's instructions when using over-the-counter medication. Children under 16 years of age should not be given aspirin.
Raise the affected area, if possible. This will hep to reduce swelling.
When to go to hospital
Once you have taken these steps, you'll need to decide whether further medical treatment is necessary. 

Go to a hospital emergency department for:

large burns bigger than the size of the affected person's hand
deep burns of any size that cause white or charred skin
burns on the face, neck, hands, feet, any joints, or genitals
all chemical and electrical burns
any other injuries that need treating
any signs of shock – symptoms include cold, clammy skin, sweating, rapid, shallow breathing, and weakness or dizziness.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['fractures'])
def command_help(message):
    bot.reply_to(message,'''If you suspect that someone has a broken bone, provide first-aid treatment and help them get professional care:

Stop any bleeding: If they’re bleeding, elevate and apply pressure to the wound using a sterile bandage, a clean cloth, or a clean piece of clothing.
Immobilize the injured area: If you suspect they’ve broken a bone in their neck or back, help them stay as still as possible. If you suspect they’ve broken a bone in one of their limbs, immobilize the area using a splint or sling.
Apply cold to the area: Wrap an ice pack or bag of ice cubes in a piece of cloth and apply it to the injured area for up to 10 minutes at a time.
Treat them for shock: Help them get into a comfortable position, encourage them to rest, and reassure them. Cover them with a blanket or clothing to keep them warm.
Get professional help: Call an ambulance or help them get to the emergency department for professional care.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['nosebleed'])
def command_help(message):
    bot.reply_to(message,'''Sit upright and lean forward. By remaining upright, you reduce blood pressure in the veins of your nose.
Gently blow your nose. 
Pinch your nose. 
To prevent re-bleeding, don't pick or blow your nose and don't bend down for several hours. 
If re-bleeding occurs, go through these steps again.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['insectbite'])
def command_help(message):
    bot.reply_to(message,'''To treat an insect bite or sting:

Remove the sting, tick or hairs if still in the skin.
Wash the affected area with soap and water.
Apply a cold compress (such as a flannel or cloth cooled with cold water) or an ice pack to any swelling for at least 10 minutes.
Raise or elevate the affected area if possible, as this can help reduce swelling.
Avoid scratching the area or bursting any blisters, to reduce the risk of infection – if your child has been bitten or stung, it may help to keep their fingernails short and clean.
Avoid traditional home remedies, such as vinegar and bicarbonate of soda, as they're unlikely to help.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['sprain'])
def command_help(message):
    bot.reply_to(message,'''Rest the injured limb. Your doctor may recommend not putting any weight on the injured area for 48 to 72 hours, so you may need to use crutches. A splint or brace also may be helpful initially. But don't avoid all activity.

Even with an ankle sprain, you can usually still exercise other muscles to minimize deconditioning. For example, you can use an exercise bicycle with arm exercise handles, working both your arms and the uninjured leg while resting the injured ankle on another part of the bike. That way you still get three-limb exercise to keep up your cardiovascular conditioning.

Ice the area. Use a cold pack, a slush bath or a compression sleeve filled with cold water to help limit swelling after an injury. Try to ice the area as soon as possible after the injury and continue to ice it for 15 to 20 minutes, four to eight times a day, for the first 48 hours or until swelling improves. If you use ice, be careful not to use it too long, as this could cause tissue damage.
Compress the area with an elastic wrap or bandage. Compressive wraps or sleeves made from elastic or neoprene are best.
Elevate the injured limb above your heart whenever possible to help prevent or limit swelling.\nSelect /commands to go back to menu.''')


@bot.message_handler(commands=['seizures'])
def command_help(message):
    bot.reply_to(message,'''Ease the person to the floor.
Turn the person gently onto one side. This will help the person breathe.
Clear the area around the person of anything hard or sharp. This can prevent injury.
Put something soft and flat, like a folded jacket, under his or her head.
Remove eyeglasses.
Loosen ties or anything around the neck that may make it hard to breathe.
Time the seizure. Call 911 if the seizure lasts longer than 5 minutes.\nSelect /commands to go back to menu.''')
	
@bot.message_handler(commands=['cprchild'])
def command_help(message):
    bot.reply_to(message,'''Performing Child & Baby CPR

1. Place the child or baby on their back on a firm, flat surface

For a child, kneel beside the child
For a baby, stand or kneel to the side of the baby, with your hips at a slight angle


2. Give 30 compressions

For a child, place the heel of one hand in the center of the child’s chest, with your other hand on top and your fingers interlaced and off the child’s chest
Position your shoulders directly over your hands and lock your elbows
Keep your arms straight
Push down hard and fast about 2 inches at a rate of 100 to 120 per minute
Allow the chest to return to normal position after each compression
For a small child, use a one-handed CPR technique
Place the heel of one hand in the center of the child’s chest
Push down hard and fast about 2 inches at a rate of 100 to 120 per minute
For a baby, place both thumbs (side-by-side) on the center of the baby’s chest, just below the nipple line
Use the other fingers to encircle the baby’s chest toward the back, providing support
Using both thumbs at the same time, push hard down and fast about 1 ½ inches at a rate of 100 to 120 per minute
Allow the chest to return to its normal position after each compression
Alternatively, for a baby, use the two-finger technique
Use two fingers placed parallel to the chest in the center of the chest
For a baby, if you can’t reach the depth of 1 ½ inches, consider using the one-hand technique


3. Give 2 breaths

For a child, open the airway to a slightly past-neutral position using the head-tilt/chin-lift technique
For a baby, open the airway to a neutral position using the head-tilt/chin-lift technique
Blow into the child or baby’s mouth for about 1 second
Ensure each breath makes the chest rise
Allow the air to exit before giving the next breath
If the first breath does not cause the chest to rise, retilt the head and ensure a proper seal before giving the second breath. If the second breath does not make the chest rise, an object may be blocking the airway



4. Continue giving sets of 30 chest compressions and 2 breaths until:

You notice an obvious sign of life
An AED is ready to use
Another trained responder is available to take over compressions
EMS personnel arrive and begin their care
You are alone and too tired to continue
The scene becomes unsafe
You have performed approximately 2 minutes of CPR (5 sets of 30:2), you are alone and caring for baby, and you need to call the ambulance.\nSelect /commands to go back to menu.''')

@bot.message_handler(commands=['cpradult'])
def command_help(message):
    bot.reply_to(message,'''If you have been trained in CPR, including rescue breaths, and feel confident using your skills, you should give chest compressions with rescue breaths.

If you're not completely confident, attempt hands-only CPR instead.

Hands-only CPR
To carry out a chest compression:

Kneel next to the person and place the heel of your hand on the breastbone at the centre of their chest. Place the palm of your other hand on top of the hand that's on their chest and interlock your fingers.
Position yourself so your shoulders are directly above your hands.
Using your body weight (not just your arms), press straight down by 5 to 6cm (2 to 2.5 inches) on their chest.
Keeping your hands on their chest, release the compression and allow their chest to return to its original position.
Repeat these compressions at a rate of 100 to 120 times a minute until an ambulance arrives or for as long as you can.
CPR with rescue breaths
Place the heel of your hand on the centre of the person's chest, then place the palm of your other hand on top and press down by 5 to 6cm (2 to 2.5 inches) at a steady rate of 100 to 120 compressions a minute.
After every 30 chest compressions, give 2 rescue breaths.
Tilt the person's head gently and lift the chin up with 2 fingers. Pinch the person's nose. Seal your mouth over their mouth and blow steadily and firmly into their mouth for about 1 second. Check that their chest rises. Give 2 rescue breaths.
Continue with cycles of 30 chest compressions and 2 rescue breaths until they begin to recover or emergency help arrives.\nSelect /commands to go back to menu.''')

bot.polling()

import pyjokes
import pyttsx3
joke = pyjokes.get_joke()
print (joke)
engine=pyttsx3
engine.speak(joke)
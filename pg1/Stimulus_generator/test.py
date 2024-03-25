from gtts import gTTS
import playsound

def speak(text):

     tts = gTTS(text=text, lang='ko')
     filename='voice.mp3'
     tts.save(filename)
     playsound.playsound(filename)

speak("안녕하십니까. 잠시 후 실험이 시작되오니. 몸을 편하게 해주시고 잠시후 신호가 시작되고 난 후 안내되는 방송에 집중해서 행동해주시기 바랍니다.")